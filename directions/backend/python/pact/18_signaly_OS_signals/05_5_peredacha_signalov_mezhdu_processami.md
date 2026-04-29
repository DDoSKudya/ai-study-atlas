[← Назад к индексу части XVIII](index.md)


### 5.1. `os.kill` и группы процессов (103)

#### Цель раздела

Научиться **отправлять сигналы** другим процессам и понимать, как работают группы процессов.

#### Термины

| Термин | Определение |
|--------|-------------|
| **`os.kill(pid, signum)`** | Отправить сигнал `signum` процессу с PID `pid`. |
| **`os.killpg(pgid, signum)`** | Отправить сигнал **группе процессов** с идентификатором `pgid`. |
| **Группа процессов (process group)** | Механизм Unix для объединения нескольких процессов, чтобы посылать им сигналы разом (например, всем дочерним). |

#### Простейший пример

```python
import os
import signal
import time

def child():
    print(f"[child] PID={os.getpid()}, ждём SIGTERM...")
    try:
        while True:
            time.sleep(1)
            print("[child] Жив...")
    except KeyboardInterrupt:
        print("[child] KeyboardInterrupt (SIGINT)")

if __name__ == "__main__":
    pid = os.fork()
    if pid == 0:
        child()
    else:
        print(f"[parent] Дочерний PID={pid}")
        time.sleep(3)
        print("[parent] Посылаем SIGTERM дочернему...")
        os.kill(pid, signal.SIGTERM)
        os.wait()
        print("[parent] Готово.")
```

В реальном коде чаще используются высокоуровневые обёртки (`subprocess`, `multiprocessing`), но важно понимать, что под ними лежит именно `os.kill`.

Разбор:

1. `os.fork()` (Unix‑специфичная функция) «раздваивает» процесс:
   - в дочернем процессе `pid == 0`;
   - в родителе `pid` — это PID дочернего процесса.
2. В ветке `if pid == 0` запускается функция `child()`:
   - она каждую секунду печатает, что жива;
   - ждёт, пока кто‑то не пошлёт ей сигнал, который приведёт к завершению процесса.
3. В родителе:
   - мы печатаем PID дочернего;
   - ждём 3 секунды (даём поработать);
   - вызываем `os.kill(pid, signal.SIGTERM)` — посылаем `SIGTERM` конкретному PID;
   - затем `os.wait()` — ждём завершения дочернего (и одновременно «собираем» его статус, чтобы не было зомби).
4. После `os.wait()` ребёнок точно завершился, и мы печатаем «Готово».

Это минимальный пример, который показывает базовую идею: **сигналы можно не только ловить, но и посылать другим процессам**.

#### Запомните

- `os.kill(..., SIGTERM)` → **попросить** процесс завершиться (graceful shutdown).
- `os.kill(..., SIGKILL)` → **заставить** завершиться немедленно (когда не реагирует на `SIGTERM`).

---

### 5.2. `subprocess` и сигналы (103)

#### Цель раздела

Понять, как методы `Popen.terminate()` и `Popen.kill()` связаны с сигналами, и как управлять группами процессов при запуске через `subprocess`.

#### Термины

| Термин | Определение |
|--------|-------------|
| **`Popen.terminate()`** | На Unix обычно отправляет дочернему процессу `SIGTERM`. |
| **`Popen.kill()`** | На Unix обычно отправляет `SIGKILL`. На Windows — использует `TerminateProcess`. |
| **`preexec_fn` / `start_new_session`** | Параметры `subprocess.Popen`, позволяющие создать новую группу процессов (`os.setsid`) и управлять ей. |

#### Пример: аккуратно завершить дочерний процесс

```python
import subprocess
import time

proc = subprocess.Popen(["python3", "-c", "import time; time.sleep(60)"])
time.sleep(3)
print("Посылаем terminate() (SIGTERM)...")
proc.terminate()
try:
    proc.wait(timeout=5)
except subprocess.TimeoutExpired:
    print("Процесс не завершился, посылаем kill() (SIGKILL)...")
    proc.kill()
    proc.wait()
```

Разбор по шагам:

1. `subprocess.Popen([...])` запускает дочерний процесс и сразу возвращает объект `proc`.
   - Программа‑родитель продолжает жить дальше.
2. `time.sleep(3)` — просто даём дочернему процессу «пожить».
3. `proc.terminate()`:
   - на Unix это обычно означает: «послать `SIGTERM` дочернему процессу».
   - это *вежливая просьба* завершиться.
4. `proc.wait(timeout=5)`:
   - мы ждём до 5 секунд, чтобы дочерний процесс успел завершиться.
5. Если прошло 5 секунд, а процесс всё ещё жив:
   - ловим `subprocess.TimeoutExpired`;
   - вызываем `proc.kill()`:
     - на Unix это обычно `SIGKILL` (жёсткое убийство);
   - затем снова делаем `proc.wait()`, чтобы дочерний процесс точно завершился, и у нас не осталось «зомби».

#### Очень важный нюанс: дочерний процесс может породить своих детей

Если вы запускаете программу, которая запускает ещё процессы, ситуация усложняется:

- вы можете послать `SIGTERM` только «главному» дочернему процессу;
- а его «внуки» могут остаться жить.

Для таких случаев на Unix часто делают так:

1) запускать дочерний процесс в **новой сессии/группе процессов**;  
2) отправлять сигнал **всей группе**.

##### Пример: остановить всю группу процессов (Unix)

```python
import os
import signal
import subprocess
import time

# start_new_session=True делает примерно то же, что setsid():
# создаёт новую сессию, и процесс становится лидером новой группы.
proc = subprocess.Popen(
    ["python3", "-c", "import time; time.sleep(60)"],
    start_new_session=True,
)

time.sleep(2)

# PID процесса = ID группы процессов (в таком случае это часто так и есть)
pgid = os.getpgid(proc.pid)
print("proc.pid =", proc.pid, "pgid =", pgid)

print("Посылаем SIGTERM всей группе процессов...")
os.killpg(pgid, signal.SIGTERM)

try:
    proc.wait(timeout=5)
except subprocess.TimeoutExpired:
    print("Группа не завершилась вовремя — SIGKILL всей группе...")
    os.killpg(pgid, signal.SIGKILL)
    proc.wait()
```

Разбор «зачем это нужно»:

- если ваш дочерний процесс — это, например, shell‑скрипт или менеджер, который стартует другие процессы,
  то «убить только одного» может быть недостаточно;
- управление группой процессов — способ **убедиться**, что вы остановили весь набор процессов, который запустили.

#### Запомните

- `terminate()` → мягкое завершение (`SIGTERM`), `kill()` → жёсткое (`SIGKILL`).
- Важно **ждать завершения** процесса (`wait()`), иначе можно получить зомби‑процессы.

---

### 5.3. `multiprocessing` и координация завершения (103)

#### Цель раздела

Понять, как использовать сигналы вместе с модулем `multiprocessing`: ловить сигналы в родителе и передавать информацию дочерним процессам.

#### Идея

1. Родительский процесс:
   - регистрирует обработчики `SIGINT`/`SIGTERM`;
   - выставляет флаг или отправляет сообщение дочерним процессам, когда приходит сигнал.
2. Дочерние процессы:
   - периодически проверяют флаг или читают сообщения;
   - аккуратно завершаются, когда нужно.

#### Пример (упрощённый)

```python
import multiprocessing as mp
import signal
import time

stop = mp.Event()

def worker(i, stop_event):
    print(f"worker {i} started, PID={mp.current_process().pid}")
    while not stop_event.is_set():
        print(f"worker {i} working...")
        time.sleep(1)
    print(f"worker {i} stopping...")

def main():
    processes = [mp.Process(target=worker, args=(i, stop)) for i in range(2)]
    for p in processes:
        p.start()

    def handle_term(signum, frame):
        print("Получен сигнал, останавливаем воркеров...")
        stop.set()

    signal.signal(signal.SIGINT, handle_term)
    signal.signal(signal.SIGTERM, handle_term)

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
```

Здесь:

- сигнал ловится только в родителе;
- `mp.Event` используется как межпроцессный флаг.

#### Разбор по шагам (почему это работает)

1. `stop = mp.Event()` — это межпроцессное «событие‑флаг».
   - Оно лежит в разделяемом состоянии (через механизмы multiprocessing).
   - Любой процесс может сделать `stop.set()`, и другие процессы смогут увидеть `stop.is_set()`.
2. Каждый `worker` делает цикл:
   - «пока stop не установлен — работай»;
   - когда stop установлен — выйди из цикла и напечатай `stopping...`.
3. Родитель запускает процессы `p.start()`.
4. Родитель ставит обработчики `SIGINT` и `SIGTERM`.
5. Когда приходит сигнал:
   - обработчик `handle_term` выполняется в родителе;
   - он делает `stop.set()` — и тем самым сообщает всем воркерам «пора завершаться».
6. Родитель `join()`‑ится по воркерам и ждёт, пока они выйдут.

#### Частая проблема: воркер может «залипнуть» и не выйти

Иногда воркер может зависнуть в операции, которая не проверяет `stop_event` (например, блокирующий I/O без таймаута). Тогда `join()` может ждать бесконечно.

Практичный шаблон «мягко → жёстко» для multiprocessing:

```python
import multiprocessing as mp
import signal
import time

stop = mp.Event()

def worker(i, stop_event):
    print(f"worker {i} PID={mp.current_process().pid} started")
    while not stop_event.is_set():
        # имитируем работу
        time.sleep(1)
        print(f"worker {i} working...")
    print(f"worker {i} stopping...")

def main():
    procs = [mp.Process(target=worker, args=(i, stop)) for i in range(2)]
    for p in procs:
        p.start()

    def handle_term(signum, frame):
        print("Родитель: получен сигнал, просим воркеров остановиться")
        stop.set()

    signal.signal(signal.SIGINT, handle_term)
    signal.signal(signal.SIGTERM, handle_term)

    # 1) Мягко ждём завершения
    deadline = time.time() + 5
    while time.time() < deadline and any(p.is_alive() for p in procs):
        time.sleep(0.2)

    # 2) Если кто-то жив — жёстко завершаем
    for p in procs:
        if p.is_alive():
            print("Родитель: воркер не вышел вовремя, terminate()")
            p.terminate()

    for p in procs:
        p.join()

if __name__ == "__main__":
    main()
```

Этот шаблон полезен, потому что:

- сначала вы даёте шанс воркерам корректно завершиться (закрыть ресурсы);
- если они не реагируют — вы не зависаете навсегда, а жёстко завершаете процесс.

---

## 6. Справочник и проверка
