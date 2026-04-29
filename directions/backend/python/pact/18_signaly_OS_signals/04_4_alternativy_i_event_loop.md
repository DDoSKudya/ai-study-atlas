[← Назад к индексу части XVIII](index.md)


### 4.1. `signal.set_wakeup_fd` и интеграция с select/poll (102)

#### Цель раздела

Понять, как **разбудить** блокирующий вызов (`select`, `poll`, event loop), когда приходит сигнал, не полагаясь на исключения.

#### Термины

| Термин | Определение |
|--------|-------------|
| **`signal.set_wakeup_fd(fd)`** | Указывает файловый дескриптор `fd`, в который Python **запишет байт**, когда обрабатывает сигнал. Это пробуждает `select`/`poll`/`epoll` или другой event loop, ожидающий на этом дескрипторе. |

#### Идея

1. Создаём **пару соединённых дескрипторов** (например, через `os.pipe()`).
2. Один конец (`wakeup_fd`) регистрируем через `signal.set_wakeup_fd(wakeup_fd)`.
3. Другой (`read_fd`) добавляем в список дескрипторов для `select`/`poll`.
4. Когда приходит сигнал, Python записывает байт в `wakeup_fd` → `select` просыпается → вы читаете байт и обрабатываете сигнал.

Это низкоуровневый механизм, но понимание его поможет лучше понять, как внутри работают фреймворки/loop’ы.

#### Очень понятная аналогия

Представьте, что ваш код делает:

- «Я сяду и буду ждать у двери, пока кто‑то не постучит».

Это и есть `select/poll`: они «сидят и ждут», пока какой‑то файловый дескриптор станет готов.

Проблема: сигнал — это не «стук в дверь», а как будто вам **крикнули из окна**.  
Если вы сидите и ждёте у двери, вы можете не услышать (или услышать, но не проснуться правильно).

`set_wakeup_fd` делает так, что при сигнале кто‑то **бросает камешек в дверь** (пишет байт в FD).  
Тогда `select/poll` просыпается *естественным способом* — потому что «в дверь постучали».

#### Полный пример с `selectors` (читается легче, чем raw `select`)

Этот пример показывает идею «pipe + set_wakeup_fd», но без сложных деталей:

```python
import os
import selectors
import signal
import time

sel = selectors.DefaultSelector()

# 1) Создаём pipe: (read_fd, write_fd)
read_fd, write_fd = os.pipe()

# 2) Говорим Python: при сигнале писать байт в write_fd
signal.set_wakeup_fd(write_fd)

stop = False

def handle_sigterm(signum, frame):
    # В обработчике делаем минимум
    global stop
    stop = True

signal.signal(signal.SIGTERM, handle_sigterm)
signal.signal(signal.SIGINT, handle_sigterm)

# 3) Регистрируем read_fd в селекторе
sel.register(read_fd, selectors.EVENT_READ)

print("PID:", os.getpid())
print("Ждём события или сигнала...")

while not stop:
    # select ждёт, пока что-то станет готово к чтению
    events = sel.select(timeout=5)
    if not events:
        print("Таймаут ожидания, всё ещё работаем...")
        continue

    for key, mask in events:
        if key.fileobj == read_fd:
            # 4) Читаем байты (очищаем pipe)
            data = os.read(read_fd, 1024)
            # data — это «маркер», что пришёл сигнал
            print("Проснулись из select из-за сигнала, bytes=", data)

print("Выходим аккуратно (cleanup здесь).")
```

Разбор по шагам:

1. `os.pipe()` создаёт «трубку» из двух концов:
   - в `write_fd` можно писать;
   - из `read_fd` можно читать.
2. `signal.set_wakeup_fd(write_fd)` делает так, что при сигнале Python автоматически пишет 1 байт в `write_fd`.
3. `sel.select(...)` ждёт событий ввода/вывода.  
   Когда байт появляется в pipe — это событие, и `select` просыпается.
4. Мы читаем из `read_fd`, чтобы «очистить» pipe, иначе он будет постоянно готов к чтению.
5. Параллельно обработчик сигнала ставит `stop = True`, и цикл завершает работу.

#### Важные ограничения `set_wakeup_fd`

- Это в основном **Unix‑механизм** (на Windows поведение может быть ограничено/другое).
- Переданный FD должен быть **неблокирующим** или рассчитанным на быструю запись, иначе можно получить проблемы (в продакшене часто делают FD неблокирующим и аккуратно читают/сливают байты).
- Это низкоуровневая штука: вы редко используете её напрямую, но она лежит под капотом многих event loop’ов.

---

### 4.2. Сигналы и `asyncio` (Unix) (102)

#### Цель раздела

Научиться интегрировать сигналы с `asyncio` через `loop.add_signal_handler` и реализовывать graceful shutdown асинхронного приложения.

#### Термины

| Термин | Определение |
|--------|-------------|
| **`loop.add_signal_handler(signum, callback, *args)`** | Зарегистрировать обработчик сигнала в event loop (Unix only). При сигнале будет вызван `callback(*args)` в контексте loop. |

#### Пример: graceful shutdown `asyncio`‑сервиса

```python
import asyncio
import signal

stop_event = asyncio.Event()

async def worker():
    while not stop_event.is_set():
        print("Рабочая корутина делает что-то полезное...")
        await asyncio.sleep(1)
    print("worker: завершаемся по сигналу")

async def main():
    loop = asyncio.get_running_loop()

    def ask_stop():
        # Обработчик сигналов: переводит stop_event в установленное состояние
        if not stop_event.is_set():
            print("Получен сигнал, попросим остановиться...")
            stop_event.set()

    loop.add_signal_handler(signal.SIGTERM, ask_stop)
    loop.add_signal_handler(signal.SIGINT, ask_stop)

    await worker()

if __name__ == "__main__":
    asyncio.run(main())
```

Здесь:

- при `SIGINT`/`SIGTERM` вызывается `ask_stop()`, который устанавливает `stop_event`;
- корутина `worker` в своём цикле периодически проверяет `stop_event` через `await stop_event.wait()` или `is_set()`.

#### Разбор: почему это «правильный» способ для asyncio

В `asyncio` обычно есть много корутин, которые:

- ждут `await asyncio.sleep(...)`;
- ждут I/O;
- ждут очередь задач;
- и т.д.

Если вы в обработчике сигнала попробуете «сразу всё остановить» (например, сразу `raise SystemExit`), вы:

- оборвёте программу резко;
- не дадите корутинам закрыть соединения/сохранить данные.

Паттерн «сигнал → выставить Event → корутины сами завершаются» хорош тем, что:

- сигнал переводит систему в режим «останавливаемся»;
- каждая корутина *в своём месте* аккуратно выходит.

#### Улучшение: корректно завершать несколько задач и отменять оставшиеся

Ниже пример чуть ближе к реальности: есть несколько задач, и при сигнале мы:

1) просим их остановиться через `stop_event`;  
2) ждём ограниченное время;  
3) если кто‑то не остановился — отменяем задачи (`task.cancel()`).

```python
import asyncio
import signal

stop_event = asyncio.Event()

async def worker(name: str):
    try:
        while not stop_event.is_set():
            print(f"{name}: работаю...")
            await asyncio.sleep(1)
        print(f"{name}: увидел stop_event, завершаюсь аккуратно")
    except asyncio.CancelledError:
        print(f"{name}: отменён (CancelledError), завершаюсь быстро")
        raise

async def main():
    loop = asyncio.get_running_loop()

    def ask_stop():
        if not stop_event.is_set():
            print("Получен сигнал: начинаем shutdown")
            stop_event.set()

    loop.add_signal_handler(signal.SIGTERM, ask_stop)
    loop.add_signal_handler(signal.SIGINT, ask_stop)

    tasks = [
        asyncio.create_task(worker("worker-1")),
        asyncio.create_task(worker("worker-2")),
    ]

    # Ждём, пока stop_event будет установлен
    await stop_event.wait()

    # Даём задачам время завершиться "по-хорошему"
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), timeout=5)
    except asyncio.TimeoutError:
        print("Не все задачи завершились вовремя — отменяем оставшиеся")
        for t in tasks:
            t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    asyncio.run(main())
```

Разбор:

- `stop_event.set()` — это «мягкая команда» всем корутинам: «пора завершаться».
- Каждая `worker` в цикле проверяет `stop_event.is_set()` и выходит сама.
- Если какая‑то корутина зависла и не выходит, мы делаем «план Б» — отменяем её через `cancel()`.

#### Почему `loop.add_signal_handler` только на Unix

Потому что эта функция опирается на POSIX‑модель сигналов. На Windows она либо отсутствует, либо работает иначе.  
Если вам нужно кроссплатформенное `asyncio`‑приложение, обычно используют:

- другие механизмы остановки (например, управляющую команду по TCP, событие, файл‑флаг, IPC),  
а сигналы — только на Unix‑сервере.

#### Запомните

- `loop.add_signal_handler` доступен **только на Unix**.
- Паттерн «сигнал → установить `Event` → корутины завершаются» — идиоматичный для `asyncio`.

---

## 5. Передача сигналов между процессами (§103)
