[← Назад к индексу части VI](index.md)

## §24. concurrent.futures

**Цель раздела §24:** использовать единый API для пулов потоков и процессов через **`concurrent.futures`**: **ThreadPoolExecutor** и **ProcessPoolExecutor**, получать **Future** через **`submit()`**, ждать результат через **`future.result(timeout)`**, итерировать по завершённым через **`as_completed()`**.

---

- **`ThreadPoolExecutor(max_workers=N)`** — пул потоков (по умолчанию N = min(32, os.cpu_count() + 4) в 3.8+).
- **`ProcessPoolExecutor(max_workers=N)`** — пул процессов (по умолчанию N = os.cpu_count()).
- **`executor.submit(func, *args, **kwargs)`** — отправить задачу; возвращает **Future**. **`future.result(timeout=None)`** — блокирующее ожидание результата; при исключении в задаче оно пробрасывается при вызове **result()**. **`future.exception(timeout=None)`** — получить исключение (или None). **`future.cancel()`** — отмена (успешна только если задача ещё не начала выполняться). **`future.done()`** — завершена ли задача.
- **`executor.map(func, *iterables)`** — применить функцию к элементам; возвращает итератор по результатам **в порядке аргументов**. **`executor.map(..., timeout=...)`** — таймаут на всю итерацию.
- **submit vs map:** **map** — один вызов на весь iterable, результаты в **порядке аргументов**, удобно когда нужны все результаты в том же порядке. **submit** — по одной задаче, возвращает **Future**; можно отправить много задач и получать результаты **по мере готовности** через **future.result()** или **as_completed(futures)**. Когда порядок не важен и нужна обработка «кто первый готов» — **submit** + **as_completed**; когда нужен порядок как у аргументов — **map**.
- **`concurrent.futures.as_completed(futures)`** — итератор по Future по мере завершения (первый пришедший результат — при следующей итерации).
- **`executor.shutdown(wait=True)`** — новые задачи не принимаются; при **wait=True** блокирует до завершения всех уже принятых. Контекстный менеджер **`with ThreadPoolExecutor() as ex: ...`** при выходе вызывает **shutdown(wait=True)**.

#### Пример: as_completed — обработка по мере готовности

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def task(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(task, i): i for i in range(10)}
    for future in as_completed(futures):
        idx = futures[future]
        try:
            result = future.result()
            print(idx, result)
        except Exception as e:
            print(idx, "ошибка:", e)
```

**Запомните:** для универсального пула потоков или процессов и единого стиля кода используйте **concurrent.futures**; **Future** даёт результат и отмену.

#### Пример: Future.result() и исключение из задачи

Если задача в executor завершилась с исключением, **future.result()** **пробрасывает** это исключение при вызове (не при submit). **future.exception(timeout)** возвращает исключение (или None при успехе).

```python
from concurrent.futures import ThreadPoolExecutor

def failing():
    raise ValueError("ошибка в задаче")

with ThreadPoolExecutor(max_workers=1) as ex:
    future = ex.submit(failing)
    try:
        future.result(timeout=5)
    except ValueError as e:
        print("Поймано:", e)  # Поймано: ошибка в задаче
```

#### Пример: executor.shutdown(wait=False)

**executor.shutdown(wait=False)** — запретить новые задачи; уже принятые продолжают выполняться; метод возвращается сразу (не ждёт их завершения). При **wait=True** (по умолчанию) метод блокирует до завершения всех принятых задач. Контекстный менеджер **with executor** при выходе вызывает **shutdown(wait=True)**.

```python
from concurrent.futures import ThreadPoolExecutor
import time

def slow():
    time.sleep(2)
    return "готово"

ex = ThreadPoolExecutor(max_workers=1)
future = ex.submit(slow)
ex.shutdown(wait=False)  # не ждём завершения slow
# future.result() можно вызвать позже — блокирует до результата
print(future.result(timeout=5))  # готово
```

#### Резюме по §24 (concurrent.futures)

- **ThreadPoolExecutor** и **ProcessPoolExecutor** — единый API: **submit(func, *args)** → **Future**; **future.result(timeout)**; **executor.map(func, *iterables)**; **as_completed(futures)**.
- **Future:** **result()**, **exception()**, **cancel()**, **done()**. Контекстный менеджер **with executor** вызывает **shutdown(wait=True)** при выходе.
- Для I/O — **ThreadPoolExecutor**; для CPU — **ProcessPoolExecutor**. В asyncio — **loop.run_in_executor(executor, func, *args)**.

---

## §25. Выбор: asyncio vs threading vs multiprocessing

| Тип нагрузки | Рекомендация | Пояснение |
|--------------|--------------|-----------|
| **I/O-bound** (сеть, диск, БД) | **asyncio** или **threading** | asyncio эффективнее при очень большом числе соединений; threading проще при малом числе и наличии блокирующих библиотек. |
| **CPU-bound** (вычисления) | **multiprocessing** | Обход GIL; реальный параллелизм. |
| **Смешанная** | **asyncio** + **run_in_executor(ProcessPoolExecutor)** | Async для I/O, пул процессов для тяжёлых вычислений. |
| **Много коротких I/O-задач** | **ThreadPoolExecutor** или asyncio | По ситуации. |
| **Тысячи одновременных соединений** | **asyncio** + async-библиотеки | Один поток, много корутин. |

#### Дерево решений: когда что выбирать

1. **Задача в основном ждёт I/O (сеть, диск, БД)?**  
   - Да, и нужно **много одновременных соединений** (сотни/тысячи) → **asyncio** + async-библиотеки (aiohttp, asyncpg и т.п.).  
   - Да, но соединений **мало** или уже есть **блокирующий код** (requests, sync БД) → **threading** или **ThreadPoolExecutor**; либо обёртка через **asyncio.to_thread** в asyncio-приложении.  
2. **Задача в основном считает (CPU)?**  
   - Да → **multiprocessing** или **ProcessPoolExecutor**; в asyncio — **run_in_executor(ProcessPoolExecutor(), func, ...)**.  
3. **Смесь I/O и CPU?**  
   - asyncio для I/O + **run_in_executor** с **ProcessPoolExecutor** для тяжёлых вычислений; либо отдельные потоки для I/O и процессы для CPU.  

**Практические нюансы:** asyncio требует async-совместимых библиотек (aiohttp, asyncpg); если весь стек блокирующий — проще начать с threading. Multiprocessing на Windows и macOS (spawn) — обязательно **`if __name__ == '__main__':`** и учёт pickle для аргументов.

#### Когда не использовать asyncio / threading / multiprocessing

| Модель | Когда не использовать (или использовать с осторожностью) |
|--------|----------------------------------------------------------|
| **asyncio** | Весь код блокирующий и нет желания оборачивать в to_thread/executor — проще **threading**. Нужен параллелизм CPU в одном процессе — asyncio не даёт; используйте **run_in_executor(ProcessPoolExecutor())** или отдельный скрипт с multiprocessing. |
| **threading** | Чисто CPU-bound задачи (много вычислений без I/O) — почти не ускорит из‑за GIL; используйте **multiprocessing**. Нужна изоляция памяти между «задачами» — потоки разделяют память; используйте процессы. |
| **multiprocessing** | Короткие задачи (накладные расходы на запуск процесса и pickle перевесят выигрыш). Много обмена данными между процессами — pickle и очереди дороги; рассмотрите **shared_memory** или один процесс с пулом потоков. На Windows/macOS без **`if __name__ == '__main__':`** — риск бесконечного порождения процессов при spawn. |

**Запомните:** I/O-bound — asyncio или threading; CPU-bound — multiprocessing; смешанная — asyncio + executor для CPU.

#### Резюме по §25 (выбор модели)

- **I/O-bound** (сеть, диск, БД): **asyncio** при большом числе соединений и async-библиотеках; **threading** при малом числе и блокирующем коде.
- **CPU-bound:** **multiprocessing** (или **ProcessPoolExecutor**); в asyncio — **run_in_executor(ProcessPoolExecutor(), ...)**.
- **Смешанная:** asyncio для I/O + **run_in_executor(ProcessPoolExecutor())** для тяжёлых вычислений.
- Решение: тип нагрузки → I/O или CPU → asyncio/threading или multiprocessing; учёт spawn и pickle для multiprocessing.

---

## §26. Гонки, deadlock, livelock

**Race condition** (гонка) — результат зависит от порядка выполнения потоков/процессов; возможен недетерминированный неправильный результат. **Критическая секция** (critical section) — участок кода, к которому должен быть эксклюзивный доступ (один поток/процесс в момент времени). Защита: блокировки (Lock), атомарные структуры (**queue.Queue** потокобезопасна; **list** — нет).

**Классическая гонка read–modify–write:** один поток читает переменную, другой в это время её меняет, первый записывает «старое» значение — изменение второго теряется. Пример без блокировки: инкремент счётчика `n += 1` (читаем n, прибавляем 1, пишем) — два потока могут прочитать одно и то же n и записать n+1 дважды; итог: +1 вместо +2. Защита: **Lock** вокруг всей операции или атомарная структура.

**Deadlock** (взаимоблокировка) — два (или больше) потока ждут друг друга (например, A держит Lock1 и ждёт Lock2, B держит Lock2 и ждёт Lock1). Предотвращение: фиксированный порядок захвата блокировок; таймауты при захвате; избегание вложенных блокировок где возможно.

**Livelock** — потоки активны, но не прогрессируют (постоянно «уступают» друг другу без продвижения). Пример: два потока при столкновении оба отступают и снова идут — снова столкновение, бесконечно. Устраняется изменением логики (например, случайная задержка, приоритеты, «один уступает — другой проходит»).

#### Таблица: как избежать гонок и взаимоблокировок

| Проблема | Решение |
|----------|---------|
| Гонка при доступе к общим данным | Один Lock на критическую секцию; или потокобезопасная структура (queue.Queue). |
| Гонка read–modify–write | Вся операция (прочитать + изменить + записать) под одной блокировкой. |
| Deadlock при двух блокировках | Единый порядок захвата во всех потоках (например, всегда сначала lock_a, потом lock_b). |
| Deadlock при вложенных вызовах с одним Lock | RLock (реентерабельный лок) в threading, если один поток входит в один и тот же лок несколько раз. |
| Livelock | Случайная задержка, приоритеты, упрощение логики «уступки». |

#### Пример: как возникает deadlock

```python
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_one():
    with lock_a:
        threading.current_thread().name  # имитация работы
        with lock_b:  # ждёт lock_b, который держит thread_two
            pass

def thread_two():
    with lock_b:
        with lock_a:  # ждёт lock_a, который держит thread_one
            pass

t1 = threading.Thread(target=thread_one)
t2 = threading.Thread(target=thread_two)
t1.start()
t2.start()
t1.join(timeout=1)
t2.join(timeout=1)
# Оба потока зависают: t1 держит lock_a и ждёт lock_b, t2 держит lock_b и ждёт lock_a
```

**Правило:** всегда захватывать блокировки в **одном и том же порядке** во всех потоках (например, сначала `lock_a`, потом `lock_b`). Тогда один из потоков получит обе блокировки, второй будет ждать первую — взаимной блокировки не будет.

#### Пример: как возникает livelock

При **livelock** потоки **активны** (не блокированы на lock, CPU загружен), но **не продвигаются** к цели — например, постоянно «уступают» друг другу и снова пытаются. От **deadlock** livelock отличается тем, что при deadlock потоки **ждут** (блокированы на lock, CPU может быть почти не загружен), а при livelock потоки **крутятся** в цикле (уступают, проверяют, снова уступают). Классический сценарий: два потока должны войти в «узкое место»; при обнаружении друг друга оба отступают и снова пытаются — снова видят друг друга и отступают, и так без конца.

```python
import threading

# Два потока хотят войти в «критическую секцию»; при виде друг друга оба «уступают» (сбрасывают флаг и повторяют).
# В итоге оба крутятся в цикле, но ни один не доходит до «работы» — livelock.
entering = [False, False]
lock = threading.Lock()

def worker(pid):
    other = 1 - pid
    for _ in range(100_000):
        with lock:
            if entering[other]:
                entering[pid] = False  # «уступить» другому
                continue
            entering[pid] = True
        # «критическая секция» — сюда при livelock никто не доходит
        with lock:
            entering[pid] = False

t1 = threading.Thread(target=worker, args=(0,))
t2 = threading.Thread(target=worker, args=(1,))
t1.start()
t2.start()
t1.join()
t2.join()
# Оба потока активны (CPU крутится), но из-за «вежливой» уступки оба постоянно сбрасывают флаг и повторяют — прогресса нет.
```

В реальности livelock часто возникает при «вежливой» логике (оба видят конфликт, оба отступают, затем оба снова делают шаг — конфликт повторяется) или при «экспоненциальном откате» в сетевых протоколах, когда две стороны одновременно отступают и снова сталкиваются. **Устранение:** ввести приоритет (один поток/участник всегда проходит первым), **случайную задержку** перед повтором (чтобы развести по времени попытки), либо упростить логику, чтобы один из потоков в данной ситуации не отступал.

**Запомните:** общие изменяемые данные защищайте блокировкой или потокобезопасной очередью; для предотвращения deadlock — единый порядок захвата блокировок; при livelock — изменить логику «уступки» (приоритеты, задержки).

#### Симптомы и что проверить при зависаниях и гонках

| Симптом | Возможная причина | Что проверить |
|---------|-------------------|---------------|
| Программа «зависла», CPU не загружен | Deadlock: потоки/корутины ждут друг друга | Порядок захвата блокировок (единый порядок?); нет ли A ждёт B, B ждёт A. |
| Программа «зависла», CPU загружен | Livelock или бесконечный цикл без await/sleep | Логика «уступки»; в asyncio — есть ли **await** в цикле (иначе loop не переключается). |
| Недетерминированный неправильный результат | Гонка (race condition) | Критические секции под одной блокировкой? Общие структуры (list, dict) без Lock — не потокобезопасны. |
| asyncio: «зависло», одна корутина не завершается | Блокирующий вызов без executor (time.sleep, sync I/O) | Найти блокирующий вызов; обернуть в **run_in_executor** или **to_thread**. |
| threading: счётчик меньше ожидаемого | Гонка при инкременте (read–modify–write) | Весь инкремент (read + modify + write) под **Lock**. |
| multiprocessing: дочерний процесс не стартует / PicklingError | Несериализуемая функция или аргументы | target — функция верхнего уровня; args — pickle-совместимые. |

#### Резюме по §26 (гонки, deadlock, livelock)

- **Race condition** — результат зависит от порядка выполнения; защита: **критическая секция** под одной блокировкой или потокобезопасная структура (**queue.Queue**).
- **Deadlock** — взаимное ожидание (A ждёт B, B ждёт A). Предотвращение: **единый порядок** захвата блокировок; таймауты; по возможности избегать вложенных блокировок.
- **Livelock** — потоки активны, но не продвигаются. Устранение: изменить логику (случайная задержка, приоритеты).
- **Атомарность:** **queue.Queue** потокобезопасна; **list** и **dict** без блокировки — нет.

---

## §27. contextvars

**Цель раздела §27:** передавать контекст (request_id, пользователь, trace_id) по цепочке корутин без явной передачи аргументов; понимать, что контекст **наследуется** при **`create_task`**, но **не** передаётся в **`run_in_executor`**.

---

**Контекстные переменные** — аналог thread-local для асинхронного кода: значение привязано к контексту выполнения (цепочке вызовов в одном потоке и при переходах между корутинами через create_task).

- **`contextvars.ContextVar(name, default=None)`** — объявление переменной.
- **`var.get(default=None)`** — текущее значение; **`var.set(value)`** — установить; возвращает **token** для отката: **`var.reset(token)`**.
- **`contextvars.copy_context()`** — копия текущего контекста; **`ctx.run(coro)`** — запустить корутину в этом контексте.

При **`asyncio.create_task(coro)`** дочерняя задача **наследует** контекст текущей (значения ContextVar копируются в контекст дочерней задачи). При **`loop.run_in_executor(...)`** код выполняется в другом потоке — контекст туда **не** передаётся; при необходимости передать значение в executor его нужно явно передать аргументом в функцию.

**Token и reset:** **`var.set(value)`** возвращает **token**; **`var.reset(token)`** откатывает переменную к значению до этого **set**. Удобно для временной подстановки значения в рамках одного контекста без затирания предыдущего.

**Запуск в другом контексте:** **`ctx = contextvars.copy_context()`** копирует текущий контекст; **`ctx.run(coro)`** или **`ctx.run(func, *args)`** запускает корутину/функцию в этом контексте (в том же потоке). Удобно для «запустить с тем же контекстом» в другом месте (например, в callback или в другом потоке — тогда контекст явно подставляется).

#### Пример: ContextVar в async-цепочке

```python
import asyncio
import contextvars

request_id_var = contextvars.ContextVar('request_id', default=None)

async def handle_request(rid: str):
    request_id_var.set(rid)
    await process()

async def process():
    # контекст унаследован — get() вернёт значение, установленное в handle_request
    print("request_id:", request_id_var.get())
    await asyncio.sleep(0)

async def main():
    await asyncio.gather(
        handle_request("req-1"),
        handle_request("req-2"),
    )

asyncio.run(main())
# request_id: req-1
# request_id: req-2
```

Каждая ветка `handle_request` имеет свой контекст (свой вызов), поэтому `request_id_var.get()` в `process` возвращает правильный идентификатор для своей цепочки.

**Запомните:** для передачи «контекста запроса» в async-цепочке используйте **contextvars**; при вызове кода в executor контекст не подхватывается — передавайте нужные значения аргументами.

#### Пример: token и reset — временная подстановка значения

**ContextVar.set(value)** возвращает **token**; **ContextVar.reset(token)** откатывает переменную к значению до этого **set**. Удобно для временной подстановки (например, в тестах или при вложенных вызовах).

```python
import contextvars

request_id_var = contextvars.ContextVar('request_id', default=None)

def handle(rid):
    token = request_id_var.set(rid)
    try:
        process()
    finally:
        request_id_var.reset(token)

def process():
    print(request_id_var.get())

handle("req-1")  # req-1
handle("req-2")  # req-2
# После reset в handle значение откатилось; следующий вызов handle задаёт новое.
```

#### Резюме по §27 (contextvars)

- **ContextVar(name, default=None)** — контекстная переменная; **get()**, **set(value)** (возвращает token), **reset(token)**.
- **copy_context()** — копия текущего контекста; **ctx.run(coro)** или **ctx.run(func, *args)** — запуск в этом контексте.
- Контекст **наследуется** при **create_task**; **не передаётся** в **run_in_executor** (код в другом потоке). Для executor передавайте значения аргументами.

---

