[← Назад к индексу части VI](index.md)

## Вопросы по теме (с краткими ответами)

1. **Чем корутинная функция отличается от корутины?** Корутинная функция — это `async def f(): ...`. При вызове `f()` возвращается объект корутины; тело функции не выполняется до тех пор, пока корутину не передадут в event loop (await, create_task, asyncio.run).
2. **Что произойдёт, если вызвать корутинную функцию и не передать результат в await или create_task?** Тело не выполнится; в Python 3.7+ при завершении программы выдаётся RuntimeWarning: coroutine was never awaited.
3. **Зачем в asyncio нужен Lock, если в один момент выполняется только одна корутина?** Переключение между корутинами происходит в точках await. Между двумя await одна корутина может прочитать общие данные, затем сделать await — управление перейдёт к другой корутине, та изменит данные — после возврата первая запишет устаревшее значение (гонка read–modify–write). Lock защищает критическую секцию от переключения.
4. **В чём разница между threading и multiprocessing с точки зрения памяти и GIL?** Threading: общая память процесса, один GIL — в один момент выполняется один поток (байткод Python). Multiprocessing: у каждого процесса своя память, свой GIL — реальный параллелизм, обмен через pickle или shared memory.
5. **Когда использовать asyncio.to_thread, когда run_in_executor(ProcessPoolExecutor)?** to_thread (или run_in_executor с None/ThreadPoolExecutor) — для блокирующего I/O или вызовов, отпускающих GIL. ProcessPoolExecutor — для CPU-bound вычислений; обход GIL, но сериализация аргументов и результата через pickle.
6. **Что такое contextvars и когда контекст наследуется, а когда нет?** Контекстные переменные — аналог thread-local для async: значение привязано к контексту выполнения. Наследуется при **create_task** (дочерняя задача получает копию контекста). Не передаётся в **run_in_executor** — код выполняется в другом потоке; нужные значения передавайте аргументами.
7. **Когда использовать threading.local(), когда contextvars?** **threading.local()** — для многопоточного **синхронного** кода: данные, привязанные к потоку (соединение с БД, request_id в потоке и т.п.), без явной передачи по аргументам. **contextvars** — для **async** (контекст по цепочке корутин); наследуется при **create_task**, не передаётся в **run_in_executor**. В потоках contextvars тоже можно использовать (значение привязано к контексту выполнения). Итог: синхронные потоки — **threading.local()**; async-цепочка (и при необходимости в потоках) — **contextvars**.

---

## Вопросы по всем данным (2–3 на тему, ответы скрыты)

Ответы раскрываются по клику на «Ответ».

### Конкурентность и параллелизм, версии Python

1. В чём разница между конкурентностью и параллелизмом в контексте Python?

<details>
<summary>Ответ</summary>

**Конкурентность** — несколько задач «в процессе» одновременно; выполнение может чередоваться (одна приостанавливается, другая продолжается). Не обязательно в один момент выполняются инструкции разных задач. **Параллелизм** — несколько задач действительно выполняются одновременно (разные ядра). В Python реальный параллелизм даёт **multiprocessing** (отдельные процессы — отдельные GIL). **threading** в CPython при чистом Python-коде даёт конкурентность, но не параллелизм; параллелизм появляется при I/O, когда GIL освобождается. **asyncio** — конкурентность в одном потоке (параллелизма нет).
</details>

2. Что даёт free-threaded сборка Python 3.13?

<details>
<summary>Ответ</summary>

**Free-threaded** build (экспериментально) — сборка интерпретатора **без GIL**. Потоки могут выполняться **параллельно** в одном процессе (реальный параллелизм потоков). Пока не стандартная сборка; нужна специальная сборка интерпретатора.
</details>

3. С какой версии Python появились asyncio.run() и когда get_event_loop() стал deprecated?

<details>
<summary>Ответ</summary>

**asyncio.run()** — с Python 3.7. **get_event_loop()** в deprecated-режиме при отсутствии текущего loop — с 3.7; в 3.10 **get_event_loop()** deprecated в пользу **get_running_loop()** внутри async-кода.
</details>

### §21.1 Event loop, async/await, корутина

4. Чем корутинная функция отличается от корутины и от Task?

<details>
<summary>Ответ</summary>

**Корутинная функция** — это `async def f(): ...`. При вызове `f()` возвращается **корутина** (объект); тело не выполняется, пока корутину не передадут в loop (await, create_task, asyncio.run). **Task** — обёртка вокруг корутины, уже запланированная в loop; создаётся через **create_task(coro)**. И корутина, и Task являются awaitable.
</details>

5. Что произойдёт при вызове async def f(): ...; f() без await или create_task?

<details>
<summary>Ответ</summary>

Тело функции не выполнится; создаётся только объект корутины. В Python 3.7+ при завершении программы выдаётся **RuntimeWarning: coroutine 'f' was never awaited**. Нужно передать корутину в loop: **await f()**, **asyncio.create_task(f())** или **asyncio.run(f())**.
</details>

6. Что по сути делает asyncio.run(main()) по шагам?

<details>
<summary>Ответ</summary>

Создаётся новый event loop (**new_event_loop()**), устанавливается как текущий (**set_event_loop(loop)**), выполняется **loop.run_until_complete(main())**, затем **loop.run_until_complete(loop.shutdown_asyncgens())** и **loop.close()**. Повторно использовать этот loop нельзя.
</details>

### §21.2 create_task, gather, wait_for, shield, TaskGroup

7. В чём разница между gather и wait?

<details>
<summary>Ответ</summary>

**gather(*aws)** — запускает все awaitable и возвращает **список результатов в порядке аргументов**; при одной ошибке без return_exceptions=True исключение пробрасывается. **wait(aws, return_when=...)** — возвращает **(done, pending)** — два множества; можно FIRST_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED; отменённые задачи в pending нужно вручную отменять при выходе.
</details>

8. Что делает wait_for(aw, timeout) при истечении таймаута?

<details>
<summary>Ответ</summary>

Задача **aw отменяется** (ей уходит CancelledError); возбуждается **asyncio.TimeoutError**. Чтобы внутренняя задача не отменялась при таймауте, её оборачивают в **shield(aw)**.
</details>

9. Зачем нужен TaskGroup (3.11+) и чем он отличается от gather?

<details>
<summary>Ответ</summary>

**TaskGroup** — структурированная конкурентность: все задачи, созданные через **tg.create_task()**, при **первом исключении** в любой из них **отменяются**, группа дожидается их завершения, затем пробрасывается первое исключение (через ExceptionGroup). При **gather** без return_exceptions одна ошибка пробрасывается, но остальные задачи продолжают выполняться в фоне. TaskGroup гарантирует: при первой ошибке все задачи группы отменены — не остаётся висящих.
</details>

### §21.3 Lock, Semaphore, Queue, Event, Condition, Barrier

10. Зачем в asyncio Lock, если в один момент выполняется только одна корутина?

<details>
<summary>Ответ</summary>

Переключение между корутинами происходит в точках **await**. Между двумя await одна корутина может прочитать общие данные, сделать await — управление перейдёт к другой, та изменит данные — после возврата первая запишет устаревшее значение (гонка read–modify–write). **Lock** защищает критическую секцию от переключения: пока корутина держит lock, другие не войдут в тот же блок.
</details>

11. Когда использовать asyncio.Condition, когда Event?

<details>
<summary>Ответ</summary>

**Condition** — когда ждём **истинности условия** над общими данными (например, «очередь не пуста»): проверяем условие в цикле, при ложном вызываем **await condition.wait()**, другой вызывает **notify()** после изменения данных. **Event** — когда достаточно «кто-то сказал: готово» без проверки общего состояния; один раз **set()** — все ждущие разблокируются.
</details>

12. Что возвращает asyncio.Barrier(3).wait() и зачем барьер?

<details>
<summary>Ответ</summary>

**await barrier.wait()** блокирует корутину, пока все N корутин не вызовут wait(); когда N-я вызовет — все N разблокируются. Возвращает **индекс участника** (0..N-1). Нужен для синхронизации фазы: «все подготовились — все одновременно стартуют» (например, все воркеры загрузили конфиг — все начинают обработку).
</details>

### §21.4 run_in_executor, to_thread

13. Когда использовать run_in_executor(None, func), когда ProcessPoolExecutor?

<details>
<summary>Ответ</summary>

**run_in_executor(None, func)** (или **to_thread**) — для **блокирующего I/O** или вызовов, отпускающих GIL (файлы, сеть, time.sleep); выполнение в потоке пула по умолчанию. **ProcessPoolExecutor** — для **CPU-bound** вычислений; обход GIL, но аргументы и результат сериализуются через pickle, накладные расходы выше.
</details>

14. Можно ли в одной async-программе вызывать и to_thread, и run_in_executor(ProcessPoolExecutor(), ...)?

<details>
<summary>Ответ</summary>

Да. Для I/O — **to_thread** или **run_in_executor(None, io_func)**; для тяжёлых вычислений — **run_in_executor(ProcessPoolExecutor(), cpu_func, arg)**. Смешанная нагрузка так и обрабатывается.
</details>

### §21.5 cancel, CancelledError

15. Что нужно делать в except asyncio.CancelledError после своей очистки?

<details>
<summary>Ответ</summary>

Обязательно снова **raise** (re-raise). Иначе отмена «поглощается»: задача считается успешно завершённой, а не отменённой; код, ожидающий отмену (например, wait_for по таймауту), может повести себя некорректно.
</details>

16. Вызвали task.cancel(). Когда задача реально остановится?

<details>
<summary>Ответ</summary>

Не мгновенно. При следующем **await** внутри этой задачи туда «вбрасывается» **CancelledError**. Если корутина не перехватывает его или перехватывает и пробрасывает — задача завершается. Если перехватывает и не пробрасывает — отмена скрыта, задача продолжит выполняться.
</details>

### §21.6 loop, run_until_complete, get_running_loop, uvloop

17. Когда создавать loop вручную (new_event_loop + run_until_complete), а не asyncio.run()?

<details>
<summary>Ответ</summary>

Когда нужно **несколько раз** запускать корутины в одном loop (тесты, REPL); когда нужен **доступ к loop** до/после запуска (callback’и, свой executor); при **интеграции с фреймворком**, который сам создаёт loop (GUI, легаси). Тогда: **new_event_loop()**, **set_event_loop(loop)**, **loop.run_until_complete(coro)**; по завершении — **shutdown_asyncgens** и **close()**.
</details>

18. Внутри async-функции как получить текущий loop? Что использовать в 3.10+?

<details>
<summary>Ответ</summary>

**asyncio.get_running_loop()** — возвращает текущий запущенный loop. В Python 3.10+ **get_event_loop()** deprecated в пользу **get_running_loop()** внутри async-кода. Вызов get_running_loop() из синхронного контекста без запущенного loop возбуждает **RuntimeError**.
</details>

19. Что даёт uvloop и как его подключить?

<details>
<summary>Ответ</summary>

**uvloop** — быстрая реализация event loop на C (на базе libuv). Подключение: **asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())** до первого **asyncio.run()** или создания loop. Даёт существенный прирост производительности на I/O-bound; совместим с большинством API asyncio.
</details>

### §21.7 Streams, StreamReader, create_subprocess_exec/shell

20. Чем read(n), readline() и readuntil(separator) у StreamReader отличаются?

<details>
<summary>Ответ</summary>

**read(n=-1)** — до n байт или до EOF (фиксированные блоки/буфер). **readline()** — до первого **b'\\n'** (построчное чтение). **readuntil(separator)** — до первого вхождения разделителя (например, b'\\r\\n' или b'|'). readuntil при закрытии соединения до появления разделителя возбуждает **IncompleteReadError**.
</details>

21. Почему предпочтительнее create_subprocess_exec, а не create_subprocess_shell?

<details>
<summary>Ответ</summary>

**create_subprocess_shell(cmd)** передаёт одну строку в shell; при подстановке пользовательских или внешних данных возможна **инъекция команд** (shell интерпретирует `;`, `|`, `$()` и т.д.). **create_subprocess_exec(program, *args)** передаёт аргументы в процесс **напрямую**, без разбора shell’ом — инъекция невозможна. Shell допустим только когда cmd полностью под вашим контролем или нужна семантика shell (перенаправления, пайпы).
</details>

22. Что возвращает process.communicate() у asyncio subprocess?

<details>
<summary>Ответ</summary>

**await process.communicate(input=None)** — ожидание завершения процесса и обмен данными через stdin/stdout/stderr. Возвращает **(stdout_data, stderr_data)** — байты или None, если соответствующий поток не был в PIPE.
</details>

### §22 Threading: Thread, GIL, Lock, RLock, Condition, Barrier, queue.Queue

23. В чём разница между threading и multiprocessing с точки зрения памяти и GIL?

<details>
<summary>Ответ</summary>

**Threading:** общая память процесса, **один GIL** — в один момент выполняется один поток (байткод Python). **Multiprocessing:** у каждого процесса **своя память**, свой GIL — реальный параллелизм; обмен через pickle или shared memory.
</details>

24. Когда GIL освобождается и когда нет?

<details>
<summary>Ответ</summary>

**Освобождается:** при I/O (файлы, сокеты), при **time.sleep()**, при вызовах C-расширений, явно отпускающих GIL (например, многие операции NumPy). **Не освобождается:** при выполнении «чистого» Python-байткода (арифметика, циклы, вызовы Python-функций). Поэтому два потока, занятых только вычислениями на Python, по сути выполняются по очереди.
</details>

25. Зачем нужен RLock вместо Lock?

<details>
<summary>Ответ</summary>

**RLock** (реентерабельный лок) — один и тот же поток может захватить его **несколько раз** (нужно столько же release). Удобно, когда одна функция вызывается рекурсивно или из одного потока входит в несколько уровней кода, защищённых одним локом. Обычный **Lock** при повторном захвате тем же потоком приведёт к **deadlock** (поток ждёт сам себя).
</details>

26. Как у queue.Queue добиться неблокирующего put/get?

<details>
<summary>Ответ</summary>

**put_nowait(item)** / **get_nowait()** — не блокируют; при полной очереди put_nowait возбуждает **queue.Full**, при пустой get_nowait — **queue.Empty**. Либо **put(item, block=False)** / **get(block=False)** с теми же исключениями.
</details>

27. Что такое daemon-поток и чем он отличается от обычного?

<details>
<summary>Ответ</summary>

**daemon=True** у Thread: при завершении **главного** процесса все daemon-потоки принудительно завершаются; их **join()** обычно не вызывают. Обычный (не daemon) поток нужно явно дождаться (**join()**), иначе при выходе из программы процесс может ждать его завершения. Daemon удобен для фоновых задач (логгер, мониторинг), которые можно оборвать при выходе.
</details>

### §23 Multiprocessing: Process, fork/spawn/forkserver, Queue, Pipe, Value, Manager, Pool

28. Почему при spawn обязателен if __name__ == '__main__':?

<details>
<summary>Ответ</summary>

При **spawn** код модуля **импортируется заново** в дочернем процессе. Если код создания процессов (Process(...).start()) на верхнем уровне модуля, при импорте в дочернем процессе он выполнится снова — дочерний создаст своих детей, те — своих, и т.д. **Бесконечное порождение процессов**. Точка входа (создание процессов, main) должна быть только в **if __name__ == '__main__':`**, тогда в дочернем процессе при импорте этот блок не выполнится.
</details>

29. Когда выбирать fork, когда spawn, когда forkserver?

<details>
<summary>Ответ</summary>

**fork** — быстрый старт, копирование памяти; на Windows недоступен. **spawn** — по умолчанию на Windows и macOS (3.8+); чистый старт, новый интерпретатор; обязателен **if __name__ == '__main__'**. **forkserver** — отдельный процесс-сервер создаёт детей через fork; изоляция лучше, старт медленнее; уместен когда после fork в основном процессе загружались потоки/сложное состояние (риски fork). На Windows доступен только spawn.
</details>

30. Чем multiprocessing.Queue отличается от multiprocessing.Pipe?

<details>
<summary>Ответ</summary>

**Queue** — очередь сообщений между процессами; объекты сериализуются через pickle; несколько производителей/потребителей, один конец очереди. **Pipe** — **двунаправленный** канал между двумя процессами; возвращает (conn_parent, conn_child); каждый конец можно передать одному процессу; send/recv с pickle или send_bytes/recv_bytes для сырых байт.
</details>

31. Что такое Value(typecode, value, lock=True) и зачем lock?

<details>
<summary>Ответ</summary>

**Value** — разделяемая между процессами переменная с типом C (typecode: 'i', 'd', 'f' и т.д.). Доступ: **value.value**. **lock=True** (по умолчанию) даёт **атомарный** доступ через внутренний Lock (защита от гонок при read–modify–write). **lock=False** — быстрее, но атомарность обеспечивать нужно самому (например, отдельным Lock).
</details>

32. Чем Pool.map отличается от Pool.apply_async и от map_async?

<details>
<summary>Ответ</summary>

**map** — применить функцию ко всем элементам iterable, вернуть **список в порядке аргументов**; **блокирует** до завершения всех. **apply_async** — одна задача, возвращает **AsyncResult**; **get()** блокирует до результата. **map_async** — неблокирующий аналог map: возвращает **AsyncResult**, **get()** возвращает **список** в порядке iterable после завершения всех; удобно отправить все задачи и позже одним get() дождаться результатов.
</details>

33. Зачем Pool(..., initializer=func, initargs=()) и maxtasksperchild=M?

<details>
<summary>Ответ</summary>

**initializer** — при **старте каждого воркера** вызывается **func(*initargs)** до первой задачи (например, открыть соединение с БД, загрузить данные). **maxtasksperchild=M** — после M задач воркер завершается и создаётся новый; снижает накопление утечек памяти в долгоживущих пулах.
</details>

### §23.5 Zombie-процессы, §23.6 Manager vs shared_memory

34. Что такое zombie-процесс и как его избежать?

<details>
<summary>Ответ</summary>

**Zombie** — дочерний процесс уже **завершился**, но запись о нём ещё в ядре (код выхода хранится до **wait**). Занимает запись в таблице процессов; при большом числе — лимит ОС. **Избежать:** вызывать **process.join()** для каждого созданного процесса (reap); либо **process.daemon = True** до start() — при завершении родителя дочерний принудительно завершается, зомби не накапливаются. Для Pool — **pool.close()** и **pool.join()**.
</details>

35. Когда использовать Manager().dict()/Value(), когда shared_memory?

<details>
<summary>Ответ</summary>

**Manager** — для разделяемого **dict/list** или нескольких **скаляров** с простым API; нечастый доступ; накладные расходы на прокси и pickle. **shared_memory** — для **больших массивов/буферов**, частый обмен, минимальные накладные расходы, без pickle; типы и layout задаёте сами (memoryview). Итог: сложные структуры, редкий доступ — Manager; большие буферы, скорость — shared_memory.
</details>

36. Нужно ли вызывать shm.unlink() у SharedMemory и где?

<details>
<summary>Ответ</summary>

Да. **shm.unlink()** удаляет именованную область из ОС. Вызывать в **процессе-создателе** после завершения **всех** дочерних процессов, иначе область останется в системе. **shm.close()** — только закрыть доступ в текущем процессе; unlink — удалить саму область.
</details>

### §24 concurrent.futures: submit, map, as_completed

37. В чём разница между executor.submit и executor.map?

<details>
<summary>Ответ</summary>

**submit(func, *args)** — одна задача, возвращает **Future**; можно отправить много задач и получать результаты **по мере готовности** через **future.result()** или **as_completed(futures)**. **map(func, *iterables)** — один вызов на весь iterable, возвращает **итератор по результатам в порядке аргументов**; удобно когда нужны все результаты в том же порядке.
</details>

38. Пробрасывается ли исключение из задачи при submit() или при result()?

<details>
<summary>Ответ</summary>

При вызове **future.result()** (не при submit). **submit()** только планирует задачу; если задача завершилась с исключением, это исключение **пробрасывается** при **result()**. **future.exception(timeout)** возвращает исключение (или None при успехе) без проброса.
</details>

39. Что делает executor.shutdown(wait=False)?

<details>
<summary>Ответ</summary>

Запрещает **новые** задачи; уже принятые продолжают выполняться. При **wait=False** метод возвращается сразу (не ждёт их завершения). При **wait=True** (по умолчанию) блокирует до завершения всех принятых задач. Контекстный менеджер **with executor** при выходе вызывает **shutdown(wait=True)**.
</details>

### §25 Выбор модели: asyncio vs threading vs multiprocessing

40. Когда предпочтительнее asyncio, когда threading для I/O-bound?

<details>
<summary>Ответ</summary>

**asyncio** — при **большом числе** сетевых соединений/запросов; один поток, много корутин; эффективнее при тысячах соединений. **threading** — при малом числе задач и наличии блокирующих библиотек (requests, sync БД); проще интеграция без переписывания на async. Оба подходят для I/O-bound; выбор по масштабу и экосистеме.
</details>

41. Для CPU-bound задач что использовать и почему не threading?

<details>
<summary>Ответ</summary>

**multiprocessing** или **ProcessPoolExecutor** (или в asyncio — **run_in_executor(ProcessPoolExecutor(), cpu_func, arg)**). **Threading** при чисто CPU-bound не даёт прироста: один GIL, в момент времени выполняется один поток (байткод Python); потоки по сути по очереди. Отдельные процессы — отдельные GIL, реальный параллелизм на нескольких ядрах.
</details>

### §26 Гонки, deadlock, livelock

42. Как избежать deadlock при двух блокировках?

<details>
<summary>Ответ</summary>

**Единый порядок захвата** блокировок во всех потоках/корутинах: например, всегда сначала **lock_a**, потом **lock_b**. Тогда один поток получит обе, второй будет ждать первую — взаимной блокировки (A ждёт B, B ждёт A) не будет.
</details>

43. Чем livelock отличается от deadlock по симптомам?

<details>
<summary>Ответ</summary>

При **deadlock** потоки **ждут** (блокированы на lock), CPU почти не загружен. При **livelock** потоки **активны** (крутятся в цикле), CPU загружен, но к цели не продвигаются (например, постоянно «уступают» друг другу). Устранение livelock: приоритеты, случайная задержка, упрощение логики уступки.
</details>

44. Что такое критическая секция и как её защитить в asyncio и threading?

<details>
<summary>Ответ</summary>

**Критическая секция** — участок кода с эксклюзивным доступом к общим данным. В **asyncio**: **async with asyncio.Lock():** перед доступом. В **threading**: **with lock:** (или **with threading.Lock():**). Альтернатива — потокобезопасная структура (**queue.Queue**, **asyncio.Queue**) вместо общих list/dict.
</details>

### §27 contextvars

45. Наследуется ли контекст (ContextVar) при create_task и при run_in_executor?

<details>
<summary>Ответ</summary>

При **create_task(coro)** — **да**, дочерняя задача получает **копию** контекста (значения ContextVar). При **run_in_executor(...)** — **нет**; код выполняется в **другом потоке**, контекст туда не передаётся. Нужные значения передавайте **аргументами** в функцию для executor.
</details>

46. Как запустить код в другом контексте (скопировать текущий и выполнить там)?

<details>
<summary>Ответ</summary>

**ctx = contextvars.copy_context()** копирует текущий контекст. **ctx.run(coro)** или **ctx.run(func, *args)** запускает корутину/функцию в этом контексте (в том же потоке). Удобно для callback’ов или другого потока — тогда контекст явно подставляется.
</details>

### Исключения, типичные ошибки, отладка

47. Какое исключение возбуждается при отмене задачи в asyncio и что с ним делать?

<details>
<summary>Ответ</summary>

**asyncio.CancelledError**. При перехвате — сделать очистку ресурсов и обязательно **raise** (re-raise), иначе отмена скрывается и поведение кода (wait_for, shutdown) может быть некорректным.
</details>

48. Что проверить, если asyncio-программа «зависла» (одна корутина не завершается)?

<details>
<summary>Ответ</summary>

Нет ли **блокирующего вызова** без обёртки: **time.sleep**, синхронный **requests.get**, sync БД и т.п. Такой вызов блокирует весь event loop. Вынести в **run_in_executor** или **asyncio.to_thread**. Включить **PYTHONASYNCIODEBUG=1**; посмотреть **asyncio.all_tasks(loop)** — какие задачи не завершились.
</details>

49. При spawn в multiprocessing процесс «размножается». В чём причина и как исправить?

<details>
<summary>Ответ</summary>

Код создания процессов (Process(...).start()) выполняется на **верхнем уровне модуля**; при импорте в дочернем процессе он выполняется снова — каждый дочерний создаёт своих детей. **Исправить:** весь код создания процессов и вызов main поместить в **if __name__ == '__main__':**.
</details>

---

## Примеры из практики (Часть VI)

- **Параллельная загрузка нескольких URL с таймаутом:** запустить несколько корутин через **create_task** или **gather**, каждую обернуть в **wait_for(coro, timeout)**; при необходимости обработать часть успешных и часть с ошибками — **gather(..., return_exceptions=True)**.
- **Ограничение числа одновременных запросов к API:** **asyncio.Semaphore(n)** + **async with sem** перед каждым запросом; не более n корутин одновременно выполняют запрос.
- **Фоновая задача при старте приложения:** в asyncio — **create_task(background_worker())** в main; не забыть обработать отмену при shutdown. В threading — **Thread(target=worker, daemon=True)** или обычный поток с **join** при выходе.
- **Очередь задач с пулом воркеров:** главный поток/корутина кладёт задачи в **queue.Queue** (threading) или **asyncio.Queue** (asyncio); N воркеров забирают задачи и обрабатывают; **join** + **task_done** для ожидания обработки всех.
- **Тяжёлые вычисления в async-приложении:** **loop.run_in_executor(ProcessPoolExecutor(), cpu_bound_func, arg)** — не блокирует event loop; результат получаете через **await**.
- **Передача request_id по цепочке async-вызовов:** **contextvars.ContextVar('request_id')**; в точке входа **var.set(rid)**; в глубине вызовов **var.get()** — без явной передачи аргументом.

**Пример: ограничение числа одновременных запросов (Semaphore)**

```python
sem = asyncio.Semaphore(10)
async def limited_fetch(url):
    async with sem:
        return await fetch(url)  # не более 10 одновременных
```

**Пример: фоновая задача при старте приложения (create_task)**

```python
async def main():
    task = asyncio.create_task(background_worker())
    try:
        await run_server()
    finally:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
```

---

## Частые сценарии (Часть VI)

| Задача | Решение |
|--------|---------|
| Запустить одну async-программу | `asyncio.run(main())` |
| Параллельно выполнить несколько корутин | `await asyncio.gather(coro1(), coro2())` или `create_task` + `await` |
| Таймаут на операцию | `await asyncio.wait_for(coro, timeout=5)` |
| Вызвать блокирующую функцию из async | `await asyncio.to_thread(blocking_func, arg)` или `run_in_executor` |
| Синхронный доступ к общему ресурсу в async | `async with asyncio.Lock(): ...` |
| Ограничить число одновременных запросов | `asyncio.Semaphore(n)` + `async with sem` |
| Поток для фоновой задачи | `threading.Thread(target=..., daemon=True)` |
| Потокобезопасная очередь | `queue.Queue()` + `put`/`get` |
| CPU-bound параллельно | `multiprocessing.Pool` или `ProcessPoolExecutor` |
| Единый API для потоков и процессов | `concurrent.futures.ThreadPoolExecutor` / `ProcessPoolExecutor` + `submit`/`map` |
| Передать контекст по async-цепочке | `contextvars.ContextVar` + `set`/`get` |

---

## Краткое повторение терминологии (Часть VI)

| Термин | Определение |
|--------|-------------|
| **Event loop** | Однопоточный диспетчер выполнения корутин и обработки I/O. |
| **Корутина** | Объект от вызова `async def`-функции; выполняется только в loop. |
| **Task** | Запланированная в loop обёртка вокруг корутины. |
| **Awaitable** | Объект, допустимый в `await` (корутина, Task, Future). |
| **GIL** | Global Interpreter Lock; в CPython один поток выполняет байткод в момент времени. |
| **I/O-bound** | Задача, ограниченная ожиданием I/O (сеть, диск). |
| **CPU-bound** | Задача, ограниченная вычислениями (CPU). |
| **Race condition** | Недетерминированный результат из-за порядка выполнения потоков/процессов. |
| **Critical section** | Участок кода с эксклюзивным доступом. |
| **Deadlock** | Взаимная блокировка (потоки ждут друг друга). |
| **Livelock** | Потоки активны, но не продвигаются. |
| **Context variable** | Переменная, привязанная к контексту выполнения (async/поток). |
| **Concurrency** | Несколько задач «в процессе»; выполнение может чередоваться. |
| **Parallelism** | Несколько задач выполняются одновременно (разные ядра/процессы). |
| **Structured concurrency** | Жизненный цикл дочерних задач ограничен областью видимости (например, TaskGroup). |

---

## Сводная таблица: asyncio vs threading vs multiprocessing (API)

| Концепция | asyncio | threading | multiprocessing |
|-----------|---------|-----------|-----------------|
| Запуск «задачи» | create_task(coro), await coro() | Thread(target=..., args=...), start() | Process(target=..., args=...), start() |
| Ожидание завершения | await task | thread.join() | process.join() |
| Мьютекс | asyncio.Lock, async with | threading.Lock, with | multiprocessing.Lock, with |
| Очередь | asyncio.Queue, await put/get | queue.Queue, put/get | multiprocessing.Queue, put/get |
| Событие | asyncio.Event, await wait() | threading.Event, wait() | multiprocessing.Event, wait() |
| Пул | run_in_executor(executor, func) | ThreadPoolExecutor | ProcessPoolExecutor, Pool |
| Память | Общая (один процесс) | Общая (один процесс) | Раздельная (каждый процесс) |
| GIL | Один поток — GIL не мешает | Один поток выполняет байткод в момент времени | Свой GIL на процесс |

---

## Сводная таблица: исключения (Часть VI)

| Контекст | Исключение | Когда возникает |
|----------|------------|------------------|
| asyncio | **asyncio.CancelledError** | Задача отменена (task.cancel()); при await отменённой задачи. |
| asyncio | **asyncio.TimeoutError** | **wait_for(aw, timeout)** — таймаут истёк; задача отменена. |
| asyncio | **asyncio.QueueFull** | **put_nowait** в полную очередь (maxsize>0). |
| asyncio | **asyncio.QueueEmpty** | **get_nowait** из пустой очереди. |
| threading | **queue.Full** | **put(..., block=False)** в полную очередь. |
| threading | **queue.Empty** | **get(..., block=False)** из пустой очереди. |
| multiprocessing | **multiprocessing.Process** (и др.) | **PicklingError** при передаче несериализуемого объекта в процесс. |
| multiprocessing | **BrokenPipeError**, **ConnectionError** | Ошибка при обмене через **Pipe** или **Queue** (процесс завершился и т.п.). |
| concurrent.futures | **TimeoutError** (или **concurrent.futures.TimeoutError**) | **future.result(timeout=...)** — таймаут истёк. |
| concurrent.futures | Исключение из задачи | Пробрасывается при вызове **future.result()** (не при submit). |

**Запомните:** в asyncio при перехвате **CancelledError** всегда делайте очистку и **raise**; не подавляйте отмену без явной необходимости.

---

## Практические рекомендации: когда что использовать (Часть VI)

- **Новый проект с большим числом сетевых соединений:** предпочтительно **asyncio** + async-библиотеки (aiohttp, asyncpg); один поток, тысячи корутин.
- **Существующий код на блокирующих библиотеках (requests, sync БД):** **threading** или **ThreadPoolExecutor**; либо постепенный переход на asyncio с **asyncio.to_thread** для блокирующих вызовов.
- **Тяжёлые вычисления (циклы, мат. операции):** **multiprocessing** или **ProcessPoolExecutor**; в asyncio — **run_in_executor(ProcessPoolExecutor(), ...)**.
- **Простая фоновая задача (логгер, периодическая проверка):** **threading.Thread(daemon=True)** или **create_task** в asyncio.
- **Очередь задач с воркерами:** **queue.Queue** + потоки или **asyncio.Queue** + корутины; для CPU-задач — **multiprocessing.Queue** + процессы.

---

## Типичные ошибки (Часть VI)

| Ошибка | Почему плохо | Как правильно |
|--------|--------------|---------------|
| Блокирующий вызов в async без executor | Блокирует весь event loop | `await asyncio.to_thread(blocking_func)` или `run_in_executor` |
| Ловить CancelledError без re-raise | Скрывает отмену, нарушает контракт | В except: очистка, затем `raise` |
| Забыть `if __name__ == '__main__':` при multiprocessing (spawn) | Бесконечное порождение процессов на Windows/macOS | Всегда оборачивать точку входа |
| Общая изменяемая структура (list/dict) без блокировки | Гонки, повреждение данных | Lock или queue.Queue / потокобезопасные структуры |
| Разный порядок захвата двух блокировок в разных потоках | Deadlock | Единый порядок захвата (например, всегда сначала A, потом B) |
| Долгая работа в daemon-потоке без учёта обрыва | Потеря данных при выходе | Либо non-daemon + join, либо короткие задачи и допустимость обрыва |
| Вызвать coro() без await/create_task/run | Тело не выполняется; «coroutine was never awaited» | `await coro()` или `asyncio.create_task(coro())` или `asyncio.run(coro)` |
| asyncio.run() изнутри уже работающего loop | «This event loop is already running» | Из async-кода только **await** другой корутины |
| Один поток захватывает Lock дважды без release | Deadlock (поток ждёт сам себя) | **RLock** или освобождать между захватами |
| Передать в Process lambda или несериализуемый объект | PicklingError в дочернем процессе | Функция верхнего уровня; аргументы — pickle-совместимые |
| Pool без close/join при ручном создании | Воркеры остаются висеть | **`with Pool() as pool:`** или явно **close()** и **join()** |
| Полагаться на contextvars в run_in_executor | Контекст не передаётся в другой поток | Передавать нужные значения аргументами в функцию для executor |

---

## Вопросы и задания (Часть VI)

1. Чем корутинная функция отличается от корутины? Что произойдёт, если вызвать корутинную функцию и не передать результат в `await` или `create_task`?
2. Зачем в asyncio нужен Lock, если в один момент выполняется только одна корутина?
3. В чём разница между threading и multiprocessing с точки зрения памяти и GIL?
4. Когда использовать `asyncio.to_thread`, а когда `run_in_executor(ProcessPoolExecutor())`?
5. Что такое contextvars и когда контекст наследуется, а когда нет (create_task vs run_in_executor)?

**Задания:** (1) Написать async-функцию, которая параллельно загружает несколько URL через `aiohttp` (или эмуляцию через `asyncio.sleep`) с таймаутом на каждый. (2) Реализовать пул из N воркеров на `queue.Queue` (threading): главный поток кладёт задачи, воркеры забирают и обрабатывают. (3) Посчитать сумму по большому списку чисел, разбив на части и посчитав в `ProcessPoolExecutor`, затем сложить результаты.

**Почему asyncio.sleep(0) полезен в цикле:** **await asyncio.sleep(0)** приостанавливает текущую корутину и отдаёт управление event loop без реальной задержки. Loop может выполнить другие готовые задачи (например, обработать I/O или другие корутины). В длинном цикле без await другие корутины не получат управление — loop «зависнет» на одной задаче. Поэтому в циклах, где возможна долгая работа без I/O, иногда вставляют **await asyncio.sleep(0)** (или небольшую задержку), чтобы дать шанс выполниться другим задачам.

**Вопросы для углублённой самопроверки:**

7. Почему asyncio.sleep(0) полезен в цикле? (Подсказка: отдаёт управление в loop, давая шанс выполниться другим корутинам.)
8. В чём разница между gather(return_exceptions=False) и return_exceptions=True при исключении в одной из корутин?
9. Зачем нужен asyncio.shield и в каких сценариях его используют?
10. Почему при spawn в multiprocessing код модуля выполняется в дочернем процессе заново?
11. Когда использовать threading.local(), когда contextvars?
12. Что такое «критическая секция» и как её защитить в asyncio и в threading?

---

## Резюме по Части VI

- **asyncio** — кооперативная многозадачность в одном потоке; event loop, `async`/`await`, `create_task`, `gather`, Lock, Queue, Event; блокирующий код — в executor или `to_thread`; отмена через `cancel`, не подавлять `CancelledError` без re-raise; Streams и subprocess для сети и процессов.
- **threading** — потоки в одном процессе, общая память, GIL; I/O-bound; синхронизация через Lock, RLock, Semaphore, Event, Condition, Barrier; потокобезопасная очередь — `queue.Queue`; daemon для фоновых задач.
- **multiprocessing** — отдельные процессы, своя память, обход GIL; CPU-bound; обмен через Queue, Pipe, Value, Array, Manager, shared_memory; Pool, initializer, maxtasksperchild; при spawn — `if __name__ == '__main__':`.
- **concurrent.futures** — единый API для пулов потоков и процессов; Future, submit, map, as_completed.
- **Выбор:** I/O — asyncio или threading; CPU — multiprocessing; смешанная — asyncio + ProcessPoolExecutor в executor.
- **Гонки** — защита критических секций; **deadlock** — единый порядок блокировок; **livelock** — изменить логику.
- **contextvars** — контекст по async-цепочке; наследуется при create_task, не передаётся в run_in_executor.

**Связь с другими частями плана:** контекстные менеджеры (§20, §20a) для Lock и ресурсов; исключения и chaining при отмене и ошибках в задачах; типизация (Protocol для awaitable) в §9.

---

## Проверка: как убедиться, что всё настроено правильно (Часть VI)

**Asyncio:**

- **Корутина выполняется:** после вызова `async def f(): ...; coro = f()` тело не выполнилось; после **`await coro()`** или **`asyncio.run(coro)`** или **`asyncio.create_task(coro)`** — выполнится. Проверка: добавить **print** в начало корутины; при «coroutine was never awaited» — корутина не передана в loop.
- **Event loop не блокируется:** если в корутине есть **time.sleep(1)** или синхронный **requests.get**, другие корутины не выполняются во время этого вызова. Проверка: запустить две корутины (одна — sleep(2), вторая — print каждую секунду); при блокировке вторая не печатает до завершения первой.
- **Отмена доходит до задачи:** после **task.cancel()** при **await task** получите **CancelledError**; внутри задачи при следующем **await** получит **CancelledError**. Если отмена «не доходит» — проверьте, не перехватываете ли **CancelledError** без re-raise.

**Threading:**

- **Общие данные защищены:** инкремент счётчика из N потоков без Lock даёт значение меньше N*итераций; с Lock — ровно N*итераций. Проверка: запустить инкремент 100_000 раз из 5 потоков без Lock и с Lock; сравнить итог.
- **Поток завершился:** **thread.is_alive()** вернёт False после **join()**; **thread.join(timeout=1)** не блокирует дольше timeout. Проверка: после **join()** убедиться, что **is_alive()** == False.

**Multiprocessing (spawn):**

- **Точка входа защищена:** при spawn код создания процессов должен быть под **`if __name__ == '__main__':`**. Проверка: на Windows/macOS без этой защиты при запуске скрипта процесс может «размножиться» (много дочерних процессов). Добавить **print** в начало модуля и внутри **if __name__** — при импорте в дочернем процессе выполнится только первый print.
- **Функция и аргументы pickle-совместимы:** при **PicklingError** в дочернем процессе проверьте, что target — функция верхнего уровня модуля (не lambda, не вложенная) и аргументы сериализуемы.

---

## Что проверить перед использованием (Часть VI)

**Перед использованием asyncio:**

- Есть ли в коде блокирующие вызовы (time.sleep, requests.get, sync БД)? → Вынести в **run_in_executor** или **asyncio.to_thread**.
- Все ли корутины передаются в loop (await / create_task / run)? → Иначе «coroutine was never awaited».
- Перехватывается ли **CancelledError**? → После очистки обязательно **raise**.
- Нужен ли один loop на весь процесс или отдельный loop в другом потоке? → **asyncio.run()** создаёт и закрывает loop; для вложенного запуска — nest_asyncio (с осторожностью).

**Перед использованием threading:**

- Есть ли общие изменяемые данные? → Защитить **Lock** или использовать **queue.Queue**.
- Один и тот же поток захватывает один и тот же Lock дважды? → Использовать **RLock**.
- Порядок захвата двух блокировок в разных потоках одинаков? → Иначе риск deadlock.
- Нужно ли ждать завершения потока при выходе из программы? → Если да — не daemon и **join()**.

**Перед использованием multiprocessing:**

- Используется ли spawn (Windows, macOS по умолчанию)? → Весь код создания процессов и main под **`if __name__ == '__main__':`**.
- Функция и аргументы сериализуемы через pickle? → Функция — верхний уровень модуля; аргументы — встроенные типы или pickle-совместимые.
- Нужен ли пул с перезапуском воркеров против утечек? → **Pool(..., maxtasksperchild=M)**.
- Используется ли SharedMemory? → После завершения всех процессов вызвать **shm.unlink()** в создателе.

---

## Связь с PEP и документацией (Часть VI)

- **PEP 492** — Coroutines with async and await (Python 3.5): синтаксис **async def** и **await**; протокол **__aiter__** / **__anext__**.
- **PEP 3156** — Asyncio: event loop, корутины, задачи, транспорты и протоколы; стандартная библиотека **asyncio**.
- **PEP 567** — Context Variables (Python 3.7): **contextvars** — контекстные переменные для async и многопоточности.
- **Документация:** [asyncio](https://docs.python.org/3/library/asyncio.html), [threading](https://docs.python.org/3/library/threading.html), [multiprocessing](https://docs.python.org/3/library/multiprocessing.html), [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html), [contextvars](https://docs.python.org/3/library/contextvars.html).

---

## Связь с другими темами плана (Часть VI)

- **§20, §20a (контекстные менеджеры):** все примитивы синхронизации (Lock, Semaphore и т.д.) в asyncio и threading поддерживают **`with`** / **`async with`** — гарантированное освобождение блокировки при выходе из блока.
- **Исключения (Часть I):** при отмене задачи в asyncio возбуждается **`asyncio.CancelledError`**; при перехвате — обязательно **re-raise**. Исключения из дочерней задачи пробрасываются в месте **`await task`** или возвращаются в **gather(..., return_exceptions=True)**.
- **§9 (typing):** для аннотаций async-кода используются **`Awaitable[T]`**, **`Coroutine[Any, Any, T]`**; для контекстных менеджеров — **`AbstractAsyncContextManager[T]`**.
- **§15c (subprocess):** синхронный **subprocess.run** блокирует поток; в async-коде используйте **asyncio.create_subprocess_exec** и **process.communicate()**.

---

## Отладка и диагностика (Часть VI)

- **asyncio:** включите **`PYTHONASYNCIODEBUG=1`** — предупреждения о неожиданных корутинах (never awaited), о долгих операциях (slow callback). **`asyncio.current_task()`** и **`asyncio.all_tasks(loop)`** — список активных задач; полезно при зависании (какие задачи не завершились). Если loop «завис» — проверьте, нет ли блокирующего вызова без run_in_executor (time.sleep, requests.get и т.п.).
- **threading:** задайте имена потокам **`Thread(..., name="worker-1")`** и логируйте **threading.current_thread().name**; при зависании проверьте порядок захвата блокировок (deadlock: A ждёт B, B ждёт A). Используйте **threading.get_ident()** или **thread.name** в логах.
- **multiprocessing:** при spawn убедитесь, что точка входа в **`if __name__ == '__main__':`**; при «зависании» проверьте, не блокируется ли дочерний процесс на **Queue.get** без поставки данных из родителя (или на Pipe.recv). Проверьте, что аргументы и функция pickle-совместимы (нет PicklingError в дочернем процессе).
- **Общее:** при гонках используйте потокобезопасные структуры (**queue.Queue**) или один Lock на критическую секцию; избегайте вложенных блокировок с разным порядком захвата. При недетерминированных ошибках добавьте логирование до/после критических секций и проверку инвариантов.
