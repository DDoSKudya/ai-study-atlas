[← Назад к индексу части VI](index.md)

# Часть VI. Асинхронность, потоки, мультипроцессинг (углублённо)

> **Цель:** уверенно выбирать и использовать модель конкурентности в Python 3: asyncio для асинхронного I/O, threading для многопоточности в рамках одного процесса, multiprocessing для параллельных вычислений; понимать GIL, гонки, deadlock и livelock; применять contextvars в async-коде.

**Краткая шпаргалка (суть):**

| Модель | Модуль / API | Назначение |
|--------|--------------|------------|
| Асинхронный I/O | `asyncio`, `async`/`await`, event loop | Много соединений I/O без блокировки потока; кооперативная многозадачность |
| Многопоточность | `threading`, `Thread`, Lock, Queue | Параллельные задачи I/O в одном процессе; общая память, GIL |
| Мультипроцессинг | `multiprocessing`, `Process`, Pool, Queue | CPU-bound; отдельная память на процесс, обход GIL |
| Пулы | `concurrent.futures`, ThreadPoolExecutor, ProcessPoolExecutor | Единый API для потоков и процессов; Future |
| Контекст в async | `contextvars` | Передача контекста (request_id и т.п.) по цепочке корутин |

---

## Маршрут изучения

**Что вы изучите и в каком порядке.** Сначала — **asyncio** (§21): **event loop**, **async**/**await**, примитивы (**create_task**, **gather**), синхронизация (Lock, Queue), совместимость с блокирующим кодом (**run_in_executor**, **to_thread**), отмена, Streams и subprocess. Затем — **threading** (§22) и **multiprocessing** (§23): основы потоков и процессов, синхронизация, очереди, пулы. Дальше — **concurrent.futures** (§24): единый API для пулов (**ThreadPoolExecutor**, **ProcessPoolExecutor**, **Future**). После — **выбор модели** (§25): когда использовать asyncio, threading или multiprocessing; **гонки, deadlock, livelock** (§26); **contextvars** (§27) для контекста в async. В конце части — справочник (сценарии, терминология, вопросы, типичные ошибки, резюме) для повторения и самопроверки.

**Что желательно знать заранее:** функции, генераторы (yield), исключения; полезно контекстные менеджеры (§20) и базовое представление об I/O и CPU-bound задачах.

---

## Структура материала (что в какой группе)

| Группа | О чём раздел | Зачем это изучать |
|--------|---------------|-------------------|
| **§21 asyncio** | Event loop, async/await, create_task, gather, Lock, Queue, run_in_executor, отмена, Streams, subprocess | Писать асинхронный I/O и кооперативную многозадачность |
| **§22 threading** | Thread, Lock, RLock, Semaphore, Event, Condition, Barrier, queue.Queue, daemon | Многопоточность в одном процессе |
| **§23 multiprocessing** | Process, Pool, Queue, Pipe, Value, Array, Manager, shared_memory, initializer | Параллелизм процессов и обход GIL |
| **§24 concurrent.futures** | ThreadPoolExecutor, ProcessPoolExecutor, Future, as_completed | Единый API для пулов потоков и процессов |
| **§25–§27** | Выбор модели, гонки/deadlock/livelock, contextvars | Выбирать модель конкурентности и избегать типичных ошибок |
| **Справочник и проверка** | Сценарии, терминология, вопросы, типичные ошибки, резюме | Повторять и проверять себя после изучения |

**Связь с планом:** Часть VI — **Шаг 6 (Конкурентность)** глобального плана; §21–§27.

#### Версии Python и конкурентность (краткая таблица)

| Версия | Asyncio / конкурентность |
|--------|---------------------------|
| 3.4 | **asyncio** в stdlib (PEP 3156); корутины через **@asyncio.coroutine** и **yield from**. |
| 3.5 | **async/await** (PEP 492); **async def**, **await**. |
| 3.7 | **asyncio.run()**; **get_event_loop()** в deprecated-режиме при отсутствии текущего loop; **contextvars** (PEP 567). |
| 3.8 | **multiprocessing.shared_memory** (SharedMemory). |
| 3.9 | **asyncio.to_thread()** — запуск блокирующей функции в потоке пула. |
| 3.10 | **get_event_loop()** deprecated — предпочтительно **get_running_loop()** внутри async-кода. |
| 3.11 | **asyncio.TaskGroup**, **asyncio.Barrier**; **ExceptionGroup**, **except***. |
| 3.12 | Улучшения asyncio (в т.ч. производительность). |
| 3.13 | **free-threaded** build (экспериментально): сборка без GIL — потоки могут выполняться параллельно в одном процессе; пока не по умолчанию, нужна специальная сборка интерпретатора. |

**Запомните:** для современного кода используйте **asyncio.run()** (3.7+), **asyncio.to_thread()** (3.9+), **TaskGroup** (3.11+); при spawn в multiprocessing — **`if __name__ == '__main__':`** на всех платформах.

#### Конкурентность и параллелизм: в чём разница

- **Конкурентность (concurrency)** — несколько задач «в процессе» одновременно: выполнение может чередоваться (одна задача приостанавливается, другая продолжается). Не обязательно в один момент времени выполняются несколько инструкций разных задач (на одном ядре может выполняться одна, а остальные ждут).
- **Параллелизм (parallelism)** — несколько задач действительно выполняются одновременно (на разных ядрах/процессорах). В Python реальный параллелизм даёт **multiprocessing** (отдельные процессы — отдельные GIL). **threading** в CPython при чисто Python-коде даёт конкурентность, но не параллелизм (один GIL); параллелизм появляется при I/O, когда GIL освобождается. **asyncio** — конкурентность в одном потоке (параллелизма нет; переключение в точках await).

---

## Как устроены разделы и оглавление

В каждом разделе (§21.1–§27) материал идёт по одному шаблону: **цель раздела** (что вы освоите) → **термины** (event loop, корутина, GIL и т.д., с кратким определением) → **правила и синтаксис** (как вызывать API, в каком порядке) → **примеры кода** (рабочие фрагменты с пояснением) → **граничные случаи** (где легко ошибиться) → блок **«Запомните»** (краткий вывод). Термины в тексте сохранены (**PEP**, **протокол**, **awaitable** и т.д.); в начале раздела или в шпаргалке они расшифрованы.

**Оглавление** разбито на этапы изучения. Каждая строка таблицы — раздел: по ссылке переходите к материалу. В столбце «Содержание» — о чём раздел; в «Ключевые понятия» — термины, которые нужно знать после изучения. Идите по этапам сверху вниз; справочник в конце — для повторения и самопроверки.

---

## Оглавление

### Этап 1. asyncio (§21)

| Раздел | Содержание | Ключевые понятия |
|--------|------------|------------------|
| [§21.1 Основы](01_21_asyncio.md#211-основы-asyncio-event-loop-async-await) | Event loop, async def, await, coroutine vs Task | Event loop, coroutine, awaitable |
| [§21.2 Примитивы](01_21_asyncio.md#212-примитивы-create_task-gather-sleep-wait_for-shield) | create_task, gather, sleep, wait_for, shield, wait, as_completed, TaskGroup | Task, gather, shield, TaskGroup |
| [§21.3 Синхронизация](01_21_asyncio.md#213-синхронизация-lock-semaphore-queue-event) | Lock, Semaphore, Queue, Event, Condition, Barrier | Async Lock, async Queue |
| [§21.4 Совместимость с синхронным кодом](01_21_asyncio.md#214-совместимость-с-синхронным-кодом-run_in_executor-to_thread) | run_in_executor, to_thread, блокирующий код | Executor, to_thread |
| [§21.5 Отмена и исключения](01_21_asyncio.md#215-отмена-и-исключения-cancel-cancellederror) | cancel, add_done_callback, CancelledError | CancelledError, re-raise |
| [§21.6 Тонкости asyncio](01_21_asyncio.md#216-тонкости-asyncio) | Один loop на поток, nest_asyncio, uvloop, debug | PYTHONASYNCIODEBUG |
| [§21.7 Streams и subprocess](01_21_asyncio.md#217-asyncio-streams-и-subprocess) | open_connection, start_server, create_subprocess_exec | StreamReader, StreamWriter |

### Этап 2. threading (§22) и multiprocessing (§23)

| Раздел | Содержание | Ключевые понятия |
|--------|------------|------------------|
| [§22 threading](02_22_threading.md#22-threading--многопоточность) | Thread, Lock, RLock, Semaphore, Event, Condition, Barrier, queue.Queue, daemon | GIL, thread-local |
| [§23 multiprocessing](03_23_multiprocessing.md#23-multiprocessing--мультипроцессинг) | Process, Pool, Queue, Pipe, Value, Array, Manager, shared_memory, initializer | fork/spawn, pickle, GIL обход |

### Этап 3. concurrent.futures и выбор модели (§24–§27)

| Раздел | Содержание | Ключевые понятия |
|--------|------------|------------------|
| [§24 concurrent.futures](04_24_25_26_27_concurrent_vybor_gonki_contextvars.md#24-concurrentfutures) | ThreadPoolExecutor, ProcessPoolExecutor, Future, map, as_completed | Future, submit |
| [§25 Выбор модели](04_24_25_26_27_concurrent_vybor_gonki_contextvars.md#25-выбор-asyncio-vs-threading-vs-multiprocessing) | I/O-bound, CPU-bound, смешанная нагрузка | Когда что использовать |
| [§26 Гонки, deadlock, livelock](04_24_25_26_27_concurrent_vybor_gonki_contextvars.md#26-гонки-deadlock-livelock) | Race condition, critical section, deadlock, livelock, атомарность; симптомы и что проверить | Критическая секция |
| [§27 contextvars](04_24_25_26_27_concurrent_vybor_gonki_contextvars.md#27-contextvars) | ContextVar, copy_context, run; наследование при create_task | Контекст в async |

### Этап 4. Справочник и проверка

| Раздел | Назначение |
|--------|------------|
| [Вопросы по теме (с ответами)](05_spravochnik_voprosy_i_testy.md#вопросы-по-теме-с-краткими-ответами) | Краткие ответы на типичные вопросы |
| [Примеры из практики](05_spravochnik_voprosy_i_testy.md#примеры-из-практики-часть-vi) | Реальные сценарии использования |
| [Частые сценарии](05_spravochnik_voprosy_i_testy.md#частые-сценарии-часть-vi) | Задача → решение |
| [Терминология](05_spravochnik_voprosy_i_testy.md#краткое-повторение-терминологии-часть-vi) | Словарь терминов |
| [Сводная таблица API](05_spravochnik_voprosy_i_testy.md#сводная-таблица-asyncio-vs-threading-vs-multiprocessing-api) | asyncio / threading / multiprocessing — сравнение API |
| [Сводная таблица: исключения](05_spravochnik_voprosy_i_testy.md#сводная-таблица-исключения-часть-vi) | CancelledError, TimeoutError, QueueEmpty, PicklingError и др. |
| [Практические рекомендации](05_spravochnik_voprosy_i_testy.md#практические-рекомендации-когда-что-использовать-часть-vi) | Когда что использовать |
| [Типичные ошибки](05_spravochnik_voprosy_i_testy.md#типичные-ошибки-часть-vi) | Частые ошибки и как избежать |
| [Вопросы и задания](05_spravochnik_voprosy_i_testy.md#вопросы-и-задания-часть-vi) | Самопроверка |
| [Связь с другими темами плана](05_spravochnik_voprosy_i_testy.md#связь-с-другими-темами-плана-часть-vi) | Контекстные менеджеры, исключения, типизация |
| [Проверка: как убедиться что всё настроено](05_spravochnik_voprosy_i_testy.md#проверка-как-убедиться-что-всё-настроено-правильно-часть-vi) | Как проверить asyncio/threading/multiprocessing |
| [Что проверить перед использованием](05_spravochnik_voprosy_i_testy.md#что-проверить-перед-использованием-часть-vi) | Чек-лист перед asyncio/threading/multiprocessing |
| [Связь с PEP и документацией](05_spravochnik_voprosy_i_testy.md#связь-с-pep-и-документацией-часть-vi) | PEP 492, 3156, 567 и ссылки на документацию |
| [Отладка и диагностика](05_spravochnik_voprosy_i_testy.md#отладка-и-диагностика-часть-vi) | Что проверить при проблемах |
| [Резюме](05_spravochnik_voprosy_i_testy.md#резюме-по-части-vi) | Сводка |

---

