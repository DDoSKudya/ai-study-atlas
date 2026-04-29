# Глобальный план перехода с Python 2.7 на Python 3

> Цель: полностью переобучиться на Python 3 со всеми тонкостями, чтобы быть ещё лучше.

---

## Последовательность изучения (от простого к сложному)

**Изучай по этой последовательности — всё от простого к сложному.** Используй при создании md-файлов по темам.

### Шаг 0 — Введение *(параллельно с шагом 1)*
**Часть 0** — Философия, границы, ментальные модели
- 0.1 История решений и дизайн-философия Python (Zen, PEP, GIL, BDFL, Py2 vs Py3)
- 0.2 Границы языка и экосистема (когда Python подходит/не подходит, PyPI, PyPy/Cython)
- 0.3 Ментальные модели (Everything is object, name binding, EAFP, duck typing, мутабельность)

### Шаг 1 — Базовый синтаксис
**Часть I (§1–4), Часть II (§6)**
- §1 Синтаксис: print, str/bytes/unicode, деление, raise, исключения (BaseException, chaining, add_note)
- §2 Типы: range, dict (views, |), list (sort, extend), set/frozenset, tuple (namedtuple)
- §3 Итераторы и генераторы: __iter__/__next__, yield, yield from, send/throw/close, async generators, itertools
- §4 Функции: *args/**kwargs, positional/keyword-only, LEGB, global/nonlocal, closures, mutable default, builtins обзор
- §6 Unicode и кодировки: ord/chr, UTF-8, open(encoding), bytes/bytearray, decode/encode

### Шаг 2 — Практика и stdlib
**Часть I (§5), Часть III (§7–8, §10–15)**
- §5 Классы и ООП: object, MRO, super(), @staticmethod/@classmethod/@property, дескрипторы, __slots__, метаклассы
- §7 Py2→Py3: удалённые модули, urllib→urllib.request, ConfigParser→configparser, Queue→queue
- §8 pathlib: Path, PurePath, read_text/write_text, glob, /, resolve, walk (3.12)
- §10 dataclasses: @dataclass, field, asdict/astuple/replace, slots, KW_ONLY
- §11 collections: defaultdict, Counter, OrderedDict, deque, ChainMap, namedtuple, UserDict/List/String
- §11a Подклассирование: list.sort/dict.update обход, UserList/UserDict, __slots__ наследование
- §12 functools: partial, reduce, lru_cache, wraps, cmp_to_key, cached_property, singledispatch/method
- §13 itertools: chain, tee, cycle, repeat, islice, groupby, zip_longest, permutations/combinations/product, accumulate, pairwise, starmap, compress, filterfalse
- §14 contextlib: @contextmanager, suppress, redirect_stdout, ExitStack, nullcontext
- §15 Модули stdlib: argparse, logging, json, re, os, shutil, getpass, subprocess, tempfile, hashlib, random, secrets, enum
- §15a0 enum: Enum, IntEnum, StrEnum, Flag, IntFlag, auto, @unique
- §15b re: compile, match/search/findall/sub/split, flags, named groups, lookahead/lookbehind
- §15c subprocess: run, Popen, communicate, PIPE, CompletedProcess
- §15d Unicode: unicodedata, NFC/NFD/NFKC/NFKD, grapheme clusters, bidi, surrogate pairs
- §15e Buffer protocol, memoryview
- §15f __set_name__, §15g module __getattr__, §15h архивы, XML, i18n
- §7a *(справочник)* — полный список модулей stdlib

### Шаг 3 — Современный синтаксис
**Часть IV (§16–19), Часть V (§20)**
- §16 f-strings: f'{x}', выражения, форматирование, f'{x=}'
- §17 Распаковка: a,*rest=, *args/**kwargs в вызовах
- §18 match/case: литералы, последовательности, as, |, guard, _, __match_args__
- §19 Walrus :=: в условиях, comprehensions
- §19a–f Python 3.10–3.13: X|Y, zip(strict), ExceptionGroup/except*, Self/Never/assert_never, TypeVarTuple, type statement, @override, free-threaded
- §20 Контекстные менеджеры: __enter__/__exit__, @contextmanager, ExitStack
- §20a Асинхронные: __aenter__/__aexit__, @asynccontextmanager, asyncio.timeout

### Шаг 4 — Типизация
**Часть III (§9, §9a)**
- §9 typing: List/Dict/Tuple/Set, Optional, Union, Callable, TypeVar, Generic, Protocol, Literal, Final, TypedDict, NewType, ClassVar, ParamSpec, @overload, Annotated, __future__ annotations
- §9a Теория: variance (covariant, contravariant, invariant), TypeGuard, narrowing, assert_type, cast, structural vs nominal

### Шаг 5 — Инструменты
**Часть VIII (§28–34), Часть IX (§35–37)**
- §28 venv, PEP 668, pip, pip-tools, ensurepip, zipapp
- §29 pyproject.toml: [build-system], [project], dependencies
- §29a Упаковка: wheel, sdist, build, twine, editable install, entry points, MANIFEST.in, src layout, py.typed
- §30 Poetry, uv, pipx, conda, pyenv
- §31 Ruff, Pylint, Black, isort, §31a pre-commit
- §32 mypy, pyright, typing_extensions
- §33 unittest, pytest, §33a hypothesis, mutation testing
- §34 Документация, docstrings
- §35–37 Миграция Py2→Py3: 2to3, six, future, стратегии

### Шаг 6 — Конкурентность
**Часть VI (§21–27)**
- §21 asyncio: event loop, async/await, create_task, gather, sleep, wait_for, shield, Lock, Semaphore, Queue, Event, TaskGroup, run_in_executor, cancel, Streams, subprocess
- §22 threading: Thread, Lock, RLock, Semaphore, Event, Condition, Barrier, queue.Queue, daemon
- §23 multiprocessing: Process, Pool, Queue, Pipe, Value, Array, Manager, shared_memory, initializer, maxtasksperchild
- §24 concurrent.futures: ThreadPoolExecutor, ProcessPoolExecutor
- §25 Выбор: asyncio vs threading vs multiprocessing
- §26 Race condition, deadlock, livelock
- §27 contextvars

### Шаг 7 — ООП углублённо
**Часть X (§38–51), Часть XI (§52–57), Часть XII (§58–65)**
- §38–51 Магические методы: __new__/__init__/__del__, __repr__/__str__/__format__, сравнение, __hash__, __bool__/__len__, __getattr__/__setattr__, дескрипторы, контейнеры, итераторы, __call__, __enter__/__exit__, числовые, битовые, slice/Ellipsis, __class_getitem__, §51c таблица оператор→метод
- §52–57 Хеширование: hash(), контракт hashable, хеш-таблицы, коллизии, weakref, кастомный __hash__, PYTHONHASHSEED
- §58–65 ООП: наследование, MRO, композиция vs наследование, abc, Protocol, SOLID, инкапсуляция, метаклассы, §65a все связи (композиция, агрегация, ассоциация, делегирование, миксин, trait, DI), §65b Object Pool, Flyweight, Proxy

### Шаг 8 — Внутренности
**Часть VII (§23–27), Часть XV (§85–89), Часть XVII (§91–98)**
- §23–27 Часть VII: объектная модель, импорт (sys.path, meta_path, path_hooks, циклические), память и GIL, copy, pickle/marshal/shelve
- §85–89 Часть XV: поиск атрибутов, __dict__/__slots__, жизненный цикл, байткод, inspect, AST, компиляция CPython, структура объектов, code/frame, GIL
- §91–98 Часть XVII: reference counting, gc, аллокация, память коллекций, weakref, утечки, оптимизация

### Шаг 9 — Паттерны и тонкости
**Часть XIII–XIV, Часть XVI, XVIII–XX**
- §66–69 Паттерны: Creational (Singleton, Factory, Builder), Structural (Adapter, Decorator, Proxy), Behavioral (Iterator, Observer, Strategy), Pythonic
- §70–84 Алгоритмы: O-нотация, массивы, стеки/очереди, связные списки, кучи, деревья, хеш-таблицы, графы, сортировки, поиск, DP, жадные, divide&conquer
- §88–90 Часть XVI: ловушки (mutable default, late binding), производительность, pdb, безопасность, ReDoS
- §99–103 Часть XVIII: сигналы ОС
- §104–108 Часть XIX: анти-паттерны (God Object, bare except, mutable default)
- §109–116 Часть XX: хаки (распаковка, слияние, условные, декораторы, отладка)

### Шаг 10 — Специализация
**Часть XXI–XXVII**
- §117–127 Часть XXI: requests/httpx/aiohttp, sqlite/SQLAlchemy/asyncpg, json/yaml/pydantic, logging/structlog, pytest/hypothesis, click/typer/rich, datetime/zoneinfo
- §128–133 Часть XXII: Django/Flask/FastAPI, Celery/RQ/Kafka, PostgreSQL/Redis, Docker/K8s, Sentry/Prometheus, CI/CD
- §134–140 Часть XXIII: NumPy/Pandas, PyTorch/TensorFlow, Transformers/LangChain, RAG, OpenCV, MLOps
- §141–144 Часть XXIV: выбор веб-фреймворка, Data Science, CLI, декораторы углублённо
- §145–148 Часть XXV: ctypes, cffi, pybind11, сборка C-расширений
- §149–153 Часть XXVI: retry/backoff, кеширование, rate limiting, circuit breaker, msgpack/protobuf
- §154–157 Часть XXVII: как читать PEP, ключевые PEP по категориям, связь PEP, практика

---

**Справочники** (используй при создании md-файлов): §4.4a–d (builtins, константы, типы, методы), §7a (модули stdlib), §51c (оператор→метод).

**Навигация:** [Краткий обзор структуры](#краткий-обзор-структуры-плана-для-навигации) — в конце документа.

---

## Часть 0. Философия, границы и ментальные модели

> **Материалы:** [→ Навигация по Части 0](pact/00_filosofiya_granicy_mentalnye_modeli/index.md)
>
> Концептуальная основа: *почему* Python такой и *как* на нём думать. Изучать можно параллельно с Частью I.

### 0.1 История решений и дизайн-философия Python

- [ ] **Zen of Python** (PEP 20): `import this` — Explicit is better than implicit; Readability counts; и др.
- [ ] Эволюция через PEP: консенсус, обратная совместимость, deprecation period
- [ ] Ключевые решения: GIL, «batteries included», «one obvious way» vs «multiple ways»
- [ ] BDFL и переход к Steering Council; роль PEP в архитектуре языка
- [ ] Python 2 vs 3: причины раскола, уроки (unicode-first, print как функция, bytes/str разделение)
- [ ] Почему typing опциональный; почему async/await, а не greenlets; мотивация match/case

### 0.2 Границы языка и его место в экосистеме

- [ ] Когда Python подходит: прототипирование, скрипты, data science, веб, автоматизация, glue-код
- [ ] Когда Python — не лучший выбор: низкоуровневый ввод-вывод, real-time, тяжёлые вычисления без C/Rust
- [ ] Python как «второй язык» в стеке: интеграция с C/C++/Rust, subprocess, FFI
- [ ] Экосистема: PyPI, виртуальные окружения, tooling (ruff, mypy, pytest) — роль стандартной библиотеки vs сторонние пакеты
- [ ] Ограничения реализации: GIL, скорость startup, потребление памяти; когда нужен PyPy или Cython

### 0.3 Ментальные модели: как думать на Python

- [ ] **«Everything is an object»**: ссылки, тождество (`is`) vs равенство (`==`), `id()`
- [ ] **Name binding**: имена — ярлыки объектов; присваивание не копирует; `a = b` — не «переменная»
- [ ] **Мутабельность vs неизменяемость**: list/dict/set vs tuple/str/frozenset; последствия для передачи и сравнения
- [ ] **EAFP vs LBYL**: «Easier to Ask Forgiveness than Permission» — `try`/`except` вместо `if` проверок
- [ ] **Протоколы и утиная типизация**: duck typing; `__iter__`, `__len__`, `__getitem__` — не наследование, а наличие методов
- [ ] **Явное лучше неявного**: `import` явный; `return None` не нужен; явные аннотации типов
- [ ] **Плоский лучше вложенного**: список, генератор, comprehensions вместо глубокой вложенности
- [ ] **Один способ vs множество**: «There should be one obvious way» — но с гибкостью для особых случаев

---

## Часть I. Отличия Python 3 от Python 2.7

> **Материалы:** [→ Навигация по Части I](pact/01_otlichiya_python3_ot_python27/index.md)

### 1. Синтаксис и базовые конструкции

#### 1.1 print
- [ ] `print` — встроенная функция, не инструкция
- [ ] `print(*args, sep=' ', end='\n', file=sys.stdout, flush=False)`
- [ ] Подавление перевода строки: `end=''`
- [ ] Вывод в stderr: `file=sys.stderr`
- [ ] Буферизация и `flush=True`

#### 1.2 Строки (str/bytes/unicode)
- [ ] `str` — последовательность Unicode-символов (в Py2 было байты)
- [ ] `bytes` — неизменяемая последовательность байт (0–255)
- [ ] `bytearray` — изменяемая последовательность байт
- [ ] Удаление `unicode`; `str` теперь всегда Unicode
- [ ] Строковые литералы: `'...'`, `"..."`, `'''...'''`, `r'...'`, `b'...'`, `f'...'`
- [ ] `str.removeprefix(prefix)`, `str.removesuffix(suffix)` (3.9+) — удаление префикса/суффикса без лишних проверок
- [ ] `str.split(sep=None, maxsplit=-1)` — разбиение; `maxsplit` — ограничить число разбиений (например `split(maxsplit=1)` для "key=value")
- [ ] `str.partition(sep)`, `str.rpartition(sep)` — разбить на (before, sep, after); удобно для парсинга
- [ ] Кодировка исходного кода: `# -*- coding: utf-8 -*-` (по умолчанию UTF-8 в Py3)
- [ ] Тонкость: `b'text'[0]` возвращает `int`, а не `bytes`

#### 1.3 Деление и числовые операции
- [ ] `/` — всегда вещественное деление (даже для int)
- [ ] `//` — целочисленное деление (floor division)
- [ ] Удаление `long`; `int` неограниченной точности
- [ ] `int()` принимает второй аргумент: `int('1010', 2)`
- [ ] Подчёркивания в числах: `1_000_000`

#### 1.4 raise и исключения
- [ ] `raise Exception(...)` — синтаксис без скобок устарел
- [ ] `raise ... from ...` — explicit exception chaining; `__cause__`
- [ ] `raise` без аргументов — повторный raise в except; implicit chaining через `__context__`
- [ ] **`__context__` vs `__cause__`**: implicit (raise внутри except) vs explicit (`raise ... from ...`)
- [ ] **`__suppress_context__`**: подавление implicit chaining при явном указании причины
- [ ] `except E as e:` — `e` удаляется в конце блока (экономия памяти)
- [ ] Иерархия: `BaseException` → `Exception` → конкретные типы
- [ ] `SystemExit`, `KeyboardInterrupt`, `GeneratorExit` наследуют `BaseException`, не `Exception` — почему (не для обычного перехвата)
- [ ] **`sys.exc_info()` vs `sys.exception()`** (3.11+): текущее исключение; `sys.exception()` безопаснее в корутинах
- [ ] **`exc.add_note(note)`** (PEP 678, 3.11+): добавление заметки к исключению; `__notes__`; доп. контекст в traceback

### 2. Типы и встроенные коллекции

#### 2.1 range
- [ ] `range` — отдельный тип, не список
- [ ] Ленивое вычисление, экономия памяти
- [ ] `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- [ ] Не поддерживает slice напрямую; `itertools.islice`
- [ ] Эквивалент `xrange` из Py2

#### 2.2 dict
- [ ] `.keys()`, `.values()`, `.items()` возвращают view-объекты (dict_keys, dict_values, dict_items)
- [ ] View отражает изменения словаря «на лету»
- [ ] Гарантирован порядок вставки (с Python 3.7)
- [ ] `{**d1, **d2}` — слияние словарей
- [ ] `d | other` — union (Python 3.9+)
- [ ] `d |= other` — update in-place (Python 3.9+)
- [ ] Удаление `.iterkeys()`, `.itervalues()` — `.keys()` и т.д. возвращают view, не итератор

#### 2.3 list
- [ ] `.sort()` vs `sorted()`; стабильная сортировка
- [ ] List comprehension, вложенные и вложенные с условиями
- [ ] Присваивание с распаковкой: `a, *rest = [1,2,3,4]`
- [ ] Копирование: slice `[:]`, `list()`, `copy.copy()` — shallow copy
- [ ] `.extend(iterable)` vs `.append(x)` — extend добавляет элементы итерабельного; append — один элемент (в т.ч. вложенный список)

#### 2.4 set и frozenset
- [ ] Неупорядоченные, уникальные элементы
- [ ] Элементы должны быть hashable
- [ ] Операции: `|`, `&`, `-`, `^` и их in-place версии

#### 2.5 tuple
- [ ] Named tuple через `collections.namedtuple` или `typing.NamedTuple`
- [ ] Распаковка: `a, b = (1, 2)`; `*args` в распаковке

### 3. Итераторы и генераторы

#### 3.1 Итераторы
- [ ] Протокол итератора: `__iter__` + `__next__` (в Py2 был `next`)
- [ ] `iter(obj)` и `next(obj, default)`
- [ ] Различие: iterable vs iterator
- [ ] `StopIteration` и изменение семантики в генераторах (PEP 479)

#### 3.2 Генераторы
- [ ] `yield` vs `return`
- [ ] `yield from` — делегирование подгенератору
- [ ] Генераторные выражения: `(x**2 for x in range(10))`
- [ ] Ленивость и потребление памяти
- [ ] `generator.send(value)` — отправка значения в генератор; `yield` возвращает его
- [ ] `generator.throw(exc)` — бросок исключения в генератор
- [ ] `generator.close()` — закрытие генератора; `GeneratorExit`
- [ ] PEP 479: `StopIteration` в генераторе преобразуется в `RuntimeError` (Python 3.7+)

#### 3.3 Асинхронные генераторы (Python 3.6+)
- [ ] `async def` с `yield` — async generator
- [ ] `async for x in agen:` — асинхронный перебор
- [ ] `__aiter__`, `__anext__` — протокол async iterator
- [ ] `agen.asend()`, `agen.athrow()`, `agen.aclose()`
- [ ] `collections.abc.AsyncIterator`, `AsyncGenerator`

#### 3.4 Тонкости
- [ ] Одноразовость итератора
- [ ] `itertools` — chain, cycle, islice, groupby и др.

### 4. Функции

#### 4.1 Объявление и вызов
- [ ] Позиционные и именованные аргументы
- [ ] `*args` — произвольное число позиционных
- [ ] `**kwargs` — произвольное число именованных
- [ ] Keyword-only аргументы (после `*`): `def f(a, *, b):`
- [ ] Positional-only аргументы (Python 3.8+): `def f(a, /, b):`
- [ ] Аннотации типов: `def f(x: int) -> str:`

#### 4.2 Области видимости (LEGB)
- [ ] Local, Enclosing, Global, Built-in
- [ ] `global` и `nonlocal`
- [ ] Замыкания (closures) и late binding
- [ ] Известная ловушка: цикл и замыкание (`lambda x=x`)

#### 4.3 Ловушки
- [ ] Mutable default argument: `def f(a=[])` — опасность
- [ ] Правило: `def f(a=None): a = a or []`

#### 4.4 Встроенные функции (builtins) — обзор

- [ ] `len`, `min`, `max`, `sum`, `any`, `all` — агрегации
- [ ] `map`, `filter`, `zip`, `enumerate` — итераторы; `enumerate(seq, start=N)`
- [ ] `sorted`, `reversed` — сортировка, разворот
- [ ] `iter(obj, sentinel)` — итератор до sentinel
- [ ] `next(iterator, default)` — следующий элемент или default
- [ ] `round(x, ndigits)`, `pow(base, exp, mod)`, `divmod(a, b)`
- [ ] `isinstance(obj, type)`, `issubclass(cls, base)` — можно передать tuple типов
- [ ] `getattr`, `setattr`, `delattr`, `hasattr`; `hasattr` вызывает getattr — ловит исключения
- [ ] `callable(obj)` — проверка callable (3.2+)
- [ ] `globals()`, `locals()` — словари областей видимости; `vars(obj)` = `obj.__dict__`
- [ ] `eval`, `exec`, `compile` — выполнение кода; риски безопасности
- [ ] `open`, `input`, `print`, `help`
- [ ] `id`, `type`, `hash`, `repr`, `str`, `format`
- [ ] `slice`, `property`, `classmethod`, `staticmethod`, `super`

#### 4.4a ВСЕ встроенные функции (builtins) — полный список Python 3 *(справочник)*

- [ ] `abs(x)` — модуль числа; `__abs__`
- [ ] `aiter(async_iterable)` — async iterator (3.10+); `__aiter__`
- [ ] `all(iterable)` — True если все истинны
- [ ] `anext(async_iterator[, default])` — следующий элемент async iterator (3.10+)
- [ ] `any(iterable)` — True если хотя бы один истинен
- [ ] `ascii(obj)` — repr с экранированием не-ASCII
- [ ] `bin(x)` — строка двоичного представления с "0b"
- [ ] `bool(x)` — булево значение; truth testing
- [ ] `breakpoint(*args, **kws)` — вход в отладчик (3.7+); `PYTHONBREAKPOINT`
- [ ] `bytearray([source[, encoding[, errors]]])` — изменяемая последовательность байт
- [ ] `bytes([source[, encoding[, errors]]])` — неизменяемая последовательность байт
- [ ] `callable(obj)` — True если объект вызываемый (3.2+)
- [ ] `chr(codepoint)` — символ по Unicode коду; обратное к `ord()`
- [ ] `classmethod(func)` — декоратор; метод получает cls первым аргументом
- [ ] `compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)` — компиляция в code object; mode: 'exec', 'eval', 'single'
- [ ] `complex([real[, imag]])` — комплексное число; `__complex__`, `__float__`, `__index__`
- [ ] `delattr(obj, name)` — удаление атрибута; эквивалент `del obj.name`
- [ ] `dict(**kw)` / `dict(mapping)` / `dict(iterable)` — словарь
- [ ] `dir([obj])` — список атрибутов; без аргумента — локальные имена
- [ ] `divmod(a, b)` — (a//b, a%b); для чисел
- [ ] `enumerate(iterable, start=0)` — (index, value)
- [ ] `eval(source[, globals[, locals]])` — выполнение выражения; опасно с user input
- [ ] `exec(source[, globals[, locals[, closure]]])` — выполнение кода; опасно
- [ ] `filter(function, iterable)` — итератор элементов, для которых function истинна
- [ ] `float(x)` — число с плавающей точкой; `__float__`, `__index__`
- [ ] `format(value[, format_spec])` — форматирование; `value.__format__(format_spec)`
- [ ] `frozenset([iterable])` — неизменяемое множество
- [ ] `getattr(obj, name[, default])` — атрибут; default при AttributeError
- [ ] `globals()` — словарь глобальной области видимости
- [ ] `hasattr(obj, name)` — есть ли атрибут; вызывает getattr, ловит исключения
- [ ] `hash(obj)` — хеш; hashable объекты; `__hash__`
- [ ] `help([obj])` — встроенная справка; интерактивная
- [ ] `hex(x)` — строка шестнадцатеричного представления с "0x"
- [ ] `id(obj)` — уникальный идентификатор объекта (адрес в памяти)
- [ ] `input([prompt])` — ввод строки; Py3: всегда str (было raw_input в Py2)
- [ ] `int(x)` / `int(x, base)` — целое число; base 2–36
- [ ] `isinstance(obj, class_or_tuple)` — проверка типа; tuple типов — OR
- [ ] `issubclass(cls, class_or_tuple)` — подкласс; tuple — OR
- [ ] `iter(obj)` / `iter(callable, sentinel)` — итератор; sentinel — до вызова, возвращающего sentinel
- [ ] `len(obj)` — длина; `__len__`
- [ ] `list([iterable])` — список
- [ ] `locals()` — словарь локальной области видимости
- [ ] `map(function, iterable, *iterables)` — итератор результатов function(elem)
- [ ] `max(iterable)` / `max(arg1, arg2, *args)` / `max(iterable, *, key=...)` / `max(iterable, *, default=...)`
- [ ] `memoryview(obj)` — buffer protocol; представление памяти без копирования
- [ ] `min(iterable)` / `min(arg1, arg2, *args)` / `min(iterable, *, key=...)` / `min(iterable, *, default=...)`
- [ ] `next(iterator[, default])` — следующий элемент; default при StopIteration
- [ ] `object()` — базовый класс; экземпляр без атрибутов
- [ ] `oct(x)` — строка восьмеричного представления с "0o"
- [ ] `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)` — файл; encoding по умолчанию UTF-8 в Py3
- [ ] `ord(c)` — Unicode код символа; обратное к `chr()`
- [ ] `pow(base, exp[, mod])` — base**exp; с mod — эффективнее для больших чисел
- [ ] `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)` — вывод; функция в Py3
- [ ] `property(fget=None, fset=None, fdel=None, doc=None)` — дескриптор свойства
- [ ] `range(stop)` / `range(start, stop[, step])` — ленивый диапазон; не список
- [ ] `repr(obj)` — строковое представление для отладки; `__repr__`
- [ ] `reversed(seq)` — обратный итератор; `__reversed__` или `__len__`+`__getitem__`
- [ ] `round(number[, ndigits])` — округление; banker's rounding для .5
- [ ] `set([iterable])` — изменяемое множество
- [ ] `setattr(obj, name, value)` — присвоение атрибута
- [ ] `slice(stop)` / `slice(start, stop[, step])` — объект среза; `seq[slice(...)]`
- [ ] `sorted(iterable, *, key=None, reverse=False)` — новый отсортированный список
- [ ] `staticmethod(func)` — декоратор; метод без self/cls
- [ ] `str(object)` — строка Unicode; `__str__`, `__repr__`
- [ ] `sum(iterable, /, start=0)` — сумма
- [ ] `super([type[, object_or_type]])` — без аргументов в Py3: автоматический MRO
- [ ] `tuple([iterable])` — кортеж
- [ ] `type(obj)` — тип объекта
- [ ] `type(name, bases, dict)` — создание класса (метакласс)
- [ ] `vars([obj])` — `obj.__dict__`; без аргумента — `locals()`
- [ ] `zip(*iterables, strict=False)` — итератор кортежей (3.10+ strict: равная длина)
- [ ] `__import__(name, globals=None, locals=None, fromlist=(), level=0)` — низкоуровневый импорт; предпочитать `importlib.import_module()`

#### 4.4b Встроенные константы (builtins) *(справочник)*
- [ ] `True`, `False` — булевы; подкласс int; единственные экземпляры bool
- [ ] `None` — единственный экземпляр NoneType; отсутствие значения
- [ ] `Ellipsis` / `...` — Ellipsis; используется в срезах `[..., :]`; в type hints: `Tuple[int, ...]`
- [ ] `NotImplemented` — для сравнений/бинарных операций; сигнал «не реализовано»; не путать с `NotImplementedError`
- [ ] `__debug__` — True, если не -O; assert проверяется только при True
- [ ] `quit`, `exit` — для интерактивного выхода; не использовать в скриптах
- [ ] `copyright`, `credits`, `license` — информационные объекты

#### 4.4c Встроенные типы и исключения (builtins) *(справочник)*
- [ ] **Встроенные типы**: `int`, `float`, `complex`, `bool`, `str`, `bytes`, `bytearray`, `list`, `tuple`, `range`, `set`, `frozenset`, `dict`, `slice`, `type`, `object`, `memoryview`
- [ ] **Встроенные исключения**: `BaseException` — корень; `Exception` — перехватываемые; `SystemExit`, `KeyboardInterrupt`, `GeneratorExit` — не наследуют Exception
- [ ] `ArithmeticError`, `AssertionError`, `AttributeError`, `EOFError`, `ImportError`, `KeyError`, `LookupError`, `MemoryError`, `NameError`, `OSError`, `OverflowError`, `RecursionError`, `ReferenceError`, `RuntimeError`, `StopIteration`, `StopAsyncIteration`, `SyntaxError`, `IndentationError`, `TabError`, `TypeError`, `UnboundLocalError`, `UnicodeError`, `UnicodeDecodeError`, `UnicodeEncodeError`, `UnicodeTranslateError`, `ValueError`, `ZeroDivisionError`
- [ ] `ExceptionGroup` (3.11+) — группа исключений; `except*` для параллельных исключений
- [ ] `OSError` — подклассы: `BlockingIOError`, `ChildProcessError`, `ConnectionError`, `FileNotFoundError`, `InterruptedError`, `IsADirectoryError`, `NotADirectoryError`, `PermissionError`, `ProcessLookupError`, `TimeoutError`
- [ ] Исключения — callable; `raise ValueError('msg')`; `args` — аргументы

#### 4.4d ВСЕ методы ВСЕХ встроенных объектов Python 3 *(справочник)*

##### str — строки (текстовые последовательности)
- [ ] `str.__getitem__(key)` — индексация и срезы; `s[0]`, `s[1:5]`; key: int или slice
- [ ] `str.__add__(other)` — конкатенация `s + t`; для цикла лучше `''.join(parts)` — эффективнее
- [ ] `str.capitalize()` — первая буква заглавная
- [ ] `str.casefold()` — Unicode casefolding; для case-insensitive сравнения
- [ ] `str.center(width[, fillchar])` — центрирование
- [ ] `str.count(sub[, start[, end]])` — количество вхождений
- [ ] `str.encode(encoding='utf-8', errors='strict')` — в bytes
- [ ] `str.endswith(suffix[, start[, end]])` — заканчивается на suffix; suffix может быть tuple
- [ ] `str.expandtabs(tabsize=8)` — табуляция в пробелы
- [ ] `str.find(sub[, start[, end]])` — индекс первого вхождения; -1 если не найдено
- [ ] `str.format(*args, **kwargs)` — форматирование; `str.format_map(mapping)` — через mapping
- [ ] `str.index(sub[, start[, end]])` — как find, но ValueError
- [ ] `str.isalnum()`, `str.isalpha()`, `str.isascii()` (3.7+), `str.isdigit()`, `str.isidentifier()`, `str.islower()`, `str.isnumeric()`, `str.isprintable()`, `str.isspace()`, `str.istitle()`, `str.isupper()` — проверки
- [ ] `str.join(iterable)` — склейка; `sep.join(iterable)`
- [ ] `str.ljust(width[, fillchar])`, `str.rjust(width[, fillchar])` — выравнивание
- [ ] `str.lower()`, `str.upper()` — регистр
- [ ] `str.lstrip([chars])`, `str.rstrip([chars])`, `str.strip([chars])` — удаление символов с краёв
- [ ] `str.maketrans(x[, y[, z]])` — статический; таблица для translate
- [ ] `str.partition(sep)`, `str.rpartition(sep)` — (before, sep, after)
- [ ] `str.removeprefix(prefix)` (3.9+), `str.removesuffix(suffix)` (3.9+) — удаление без проверок
- [ ] `str.replace(old, new[, count])` — замена
- [ ] `str.rfind(sub[, start[, end]])`, `str.rindex(sub[, start[, end]])` — поиск справа
- [ ] `str.rsplit(sep=None, maxsplit=-1)` — split справа
- [ ] `str.split(sep=None, maxsplit=-1)` — разбиение
- [ ] `str.splitlines(keepends=False)` — по переводам строк
- [ ] `str.startswith(prefix[, start[, end]])` — начинается с; prefix может быть tuple
- [ ] `str.swapcase()` — инвертировать регистр
- [ ] `str.title()` — заголовочный регистр
- [ ] `str.translate(table)` — замена по таблице
- [ ] `str.zfill(width)` — дополнение нулями слева

##### bytes, bytearray — бинарные последовательности
- [ ] Методы как у str: `capitalize`, `center`, `count`, `endswith`, `expandtabs`, `find`, `index`, `isalnum`, `isalpha`, `isdigit`, `islower`, `isspace`, `istitle`, `isupper`, `join`, `ljust`, `lower`, `lstrip`, `partition`, `removeprefix`, `removesuffix`, `replace`, `rfind`, `rindex`, `rjust`, `rpartition`, `rsplit`, `rstrip`, `split`, `splitlines`, `startswith`, `strip`, `swapcase`, `title`, `translate`, `upper`, `zfill`
- [ ] `bytes.decode(encoding='utf-8', errors='strict')` — в str; `bytearray.decode(...)`
- [ ] `bytes.fromhex(string)` — classmethod; hex-строка в bytes; `bytearray.fromhex(...)`
- [ ] `bytes.hex([sep[, bytes_per_sep]])` — hex-представление; `bytearray.hex(...)`
- [ ] **bytearray** (доп. мутирующие): `append(x)`, `clear()`, `copy()`, `extend(iterable_of_ints)`, `insert(i, x)`, `pop([i])`, `remove(x)`, `reverse()` — in-place

##### list — списки
- [ ] `list.append(x)` — добавить в конец
- [ ] `list.clear()` — очистить (in-place)
- [ ] `list.copy()` — shallow copy
- [ ] `list.count(x)` — количество x
- [ ] `list.extend(iterable)` — добавить элементы
- [ ] `list.index(x[, start[, end]])` — индекс первого x
- [ ] `list.insert(i, x)` — вставить x в позицию i
- [ ] `list.pop([i])` — извлечь и удалить; по умолчанию последний
- [ ] `list.remove(x)` — удалить первое вхождение x
- [ ] `list.reverse()` — развернуть in-place
- [ ] `list.sort(*, key=None, reverse=False)` — сортировать in-place

##### tuple — кортежи
- [ ] `tuple.count(x)` — количество x
- [ ] `tuple.index(x[, start[, end]])` — индекс первого x

##### range — диапазоны
- [ ] `range.count(x)` — входит ли x (O(1))
- [ ] `range.index(x)` — индекс x (ValueError если нет)
- [ ] Атрибуты: `range.start`, `range.stop`, `range.step`

##### dict — словари
- [ ] `dict.clear()` — очистить
- [ ] `dict.copy()` — shallow copy
- [ ] `dict.fromkeys(iterable[, value])` — classmethod; ключи из iterable, значение value
- [ ] `dict.get(key[, default])` — значение или default
- [ ] `dict.items()` — view (key, value)
- [ ] `dict.keys()` — view ключей
- [ ] `dict.pop(key[, default])` — извлечь и удалить; default при отсутствии
- [ ] `dict.popitem()` — (key, value) — LIFO; KeyError если пусто
- [ ] `dict.setdefault(key[, default])` — get или set default
- [ ] `dict.update([other])` — обновить из other (mapping или iterable пар)
- [ ] `dict.values()` — view значений
- [ ] `dict | other` (3.9+), `dict |= other` — объединение

##### set, frozenset — множества
- [ ] `set.add(elem)` — добавить (только set)
- [ ] `set.clear()` — очистить (только set)
- [ ] `set.copy()` — shallow copy
- [ ] `set.difference(*others)` — разность; `set - other`
- [ ] `set.difference_update(*others)` — разность in-place (только set)
- [ ] `set.discard(elem)` — удалить, если есть (только set)
- [ ] `set.intersection(*others)` — пересечение; `set & other`
- [ ] `set.intersection_update(*others)` — пересечение in-place (только set)
- [ ] `set.isdisjoint(other)` — нет общих элементов
- [ ] `set.issubset(other)` — подмножество; `set <= other`
- [ ] `set.issuperset(other)` — надмножество; `set >= other`
- [ ] `set.pop()` — извлечь произвольный элемент (только set)
- [ ] `set.remove(elem)` — удалить; KeyError если нет (только set)
- [ ] `set.symmetric_difference(other)` — симметричная разность; `set ^ other`
- [ ] `set.symmetric_difference_update(other)` — in-place (только set)
- [ ] `set.union(*others)` — объединение; `set | other`
- [ ] `set.update(*others)` — объединение in-place (только set)

##### int — целые числа
- [ ] `int.bit_length()` — число бит для представления (без знака и ведущих нулей)
- [ ] `int.bit_count()` (3.10+) — число единиц в двоичном представлении (popcount)
- [ ] `int.to_bytes(length=1, byteorder='big', *, signed=False)` — int в bytes
- [ ] `int.from_bytes(bytes, byteorder='big', *, signed=False)` — classmethod; bytes в int
- [ ] `int.as_integer_ratio()` — (self, 1)
- [ ] `int.is_integer()` (3.12+) — всегда True

##### float — числа с плавающей точкой
- [ ] `float.as_integer_ratio()` — (numerator, denominator)
- [ ] `float.is_integer()` — целое ли значение
- [ ] `float.hex()` — hex-представление
- [ ] `float.fromhex(s)` — classmethod; hex-строка в float

##### complex — комплексные числа
- [ ] `complex.conjugate()` — сопряжённое
- [ ] Атрибуты: `complex.real`, `complex.imag`

##### slice — срезы
- [ ] Атрибуты: `slice.start`, `slice.stop`, `slice.step`

##### memoryview — представление памяти
- [ ] `memoryview.cast(format[, shape])` — приведение формата
- [ ] Атрибуты: `itemsize`, `nbytes`, `ndim`, `obj`, `readonly`, `shape`, `strides`, `suboffsets`
- [ ] `memoryview.release()` — освободить буфер
- [ ] `memoryview.tolist()` — в список
- [ ] `memoryview.tobytes()` — в bytes
- [ ] `memoryview.hex()` — hex-представление

##### file object (io.TextIOWrapper, io.BufferedIOBase)
- [ ] `file.close()` — закрыть
- [ ] `file.closed` — атрибут
- [ ] `file.fileno()` — файловый дескриптор
- [ ] `file.flush()` — сбросить буфер
- [ ] `file.isatty()` — TTY?
- [ ] `file.read([size])` — чтение
- [ ] `file.readable()` — можно читать?
- [ ] `file.readline([size])` — одна строка
- [ ] `file.readlines([hint])` — список строк
- [ ] `file.seek(offset[, whence])` — позиция
- [ ] `file.seekable()` — поддерживает seek?
- [ ] `file.tell()` — текущая позиция
- [ ] `file.truncate(size=None)` — обрезать
- [ ] `file.writable()` — можно писать?
- [ ] `file.write(s)` — запись
- [ ] `file.writelines(lines)` — запись списка строк

##### iterator — итераторы
- [ ] `iterator.__iter__()` — возвращает self
- [ ] `iterator.__next__()` — следующий элемент; StopIteration при исчерпании

##### generator — генераторы
- [ ] `generator.__iter__()`, `generator.__next__()`
- [ ] `generator.send(value)` — отправить в yield
- [ ] `generator.throw(type[, value[, tb]])` — бросить исключение в yield
- [ ] `generator.close()` — закрыть генератор

##### Exception — исключения
- [ ] `Exception.args` — аргументы
- [ ] `Exception.add_note(note)` (3.11+) — добавить заметку
- [ ] `Exception.__notes__` (3.11+) — список заметок
- [ ] `Exception.with_traceback(tb)` — установить traceback

##### object — базовый класс (магические методы)
- [ ] `__new__(cls[, ...])` — создание
- [ ] `__init__(self[, ...])` — инициализация
- [ ] `__del__(self)` — финализатор
- [ ] `__repr__(self)` — repr()
- [ ] `__str__(self)` — str()
- [ ] `__bytes__(self)` — bytes()
- [ ] `__format__(self, format_spec)` — format()
- [ ] `__lt__`, `__le__`, `__gt__`, `__ge__`, `__eq__`, `__ne__` — сравнения
- [ ] `__hash__(self)` — hash()
- [ ] `__bool__(self)` — bool()
- [ ] `__getattribute__(self, name)` — доступ к атрибуту
- [ ] `__getattr__(self, name)` — атрибут не найден
- [ ] `__setattr__(self, name, value)` — присвоение атрибута
- [ ] `__delattr__(self, name)` — удаление атрибута
- [ ] `__dir__(self)` — dir()
- [ ] `__getitem__(self, key)` — obj[key]
- [ ] `__setitem__(self, key, value)` — obj[key]=value
- [ ] `__delitem__(self, key)` — del obj[key]
- [ ] `__iter__(self)` — iter()
- [ ] `__next__(self)` — next() (итератор)
- [ ] `__len__(self)` — len()
- [ ] `__contains__(self, item)` — in
- [ ] `__call__(self[, ...])` — obj()
- [ ] `__enter__(self)`, `__exit__(self, exc_type, exc_val, exc_tb)` — with
- [ ] `__get__(self, instance, owner)` — дескриптор get
- [ ] `__set__(self, instance, value)` — дескриптор set
- [ ] `__delete__(self, instance)` — дескриптор delete
- [ ] `__slots__` — ограничение атрибутов
- [ ] `__class__`, `__dict__`, `__module__`, `__qualname__`, `__doc__`, `__annotations__` — атрибуты класса

##### type (класс) — метакласс и фабрика классов
- [ ] `type(name, bases, dict)` — создать класс
- [ ] `type.mro()` — Method Resolution Order
- [ ] `type.__subclasses__()` — подклассы
- [ ] `type.__bases__` — базовые классы
- [ ] `type.__mro__` — кортеж MRO

##### function — функции
- [ ] Атрибуты: `__code__`, `__defaults__`, `__kwdefaults__`, `__globals__`, `__closure__`, `__annotations__`, `__name__`, `__qualname__`
- [ ] `__call__(*args, **kwargs)` — вызов

##### property — свойство
- [ ] `property.getter(fget)` — геттер
- [ ] `property.setter(fset)` — сеттер
- [ ] `property.deleter(fdel)` — делитер
- [ ] Атрибуты: `fget`, `fset`, `fdel`

##### module — модуль
- [ ] Атрибуты: `__name__`, `__file__`, `__doc__`, `__package__`, `__loader__`, `__spec__`, `__path__` (для пакетов)
- [ ] `__dict__` — словарь атрибутов модуля

### 5. Классы и ООП

#### 5.1 Базовые механизмы
- [ ] Все классы наследуют от `object` по умолчанию
- [ ] MRO (Method Resolution Order) — C3 linearization
- [ ] `super()` без аргументов — автоматический выбор родителя
- [ ] `super()` в Py3 работает с `__class__` в замыкании

#### 5.2 Декораторы методов
- [ ] `@staticmethod` — не получает `self`/`cls`
- [ ] `@classmethod` — первый аргумент `cls`
- [ ] `@property` — геттер; `.setter`, `.deleter`

#### 5.3 Магические методы (dunder)
- [ ] `__init__` vs `__new__` (создание объекта)
- [ ] `__str__` vs `__repr__`
- [ ] `__eq__`, `__hash__` — контракт hashable
- [ ] `__len__`, `__getitem__`, `__iter__` — протоколы контейнера
- [ ] `__enter__`, `__exit__` — контекстный менеджер
- [ ] `__call__` — callable объект

#### 5.4 Дескрипторы
- [ ] `__get__`, `__set__`, `__delete__`
- [ ] Как работают `property`, `classmethod`, `staticmethod`
- [ ] Дескрипторы в атрибутах класса

#### 5.5 __slots__
- [ ] Экономия памяти, запрет динамических атрибутов
- [ ] Наследование и `__slots__`

#### 5.6 Метаклассы
- [ ] `type` как фабрика классов
- [ ] `__metaclass__` (в Py3: `class C(metaclass=Meta):`)
- [ ] Когда метакласс реально нужен

---

## Часть II. Строки, кодировки, bytes

> **Материалы:** [→ Навигация по Части II](pact/02_stroki_kodirovki_bytes/index.md)

### 6. Unicode и кодировки

#### 6.1 Основы
- [ ] Unicode code points и представление в памяти
- [ ] UTF-8, UTF-16, UTF-32, Latin-1
- [ ] `ord()`, `chr()` — код и символ
- [ ] `'\N{EM DASH}'`, `'\u2022'`, `'\U0001F600'`

#### 6.2 Работа с файлами и I/O
- [ ] `open(..., encoding='utf-8')` — текстовый режим по умолчанию UTF-8
- [ ] `open(..., mode='rb')` — бинарный режим, `bytes`
- [ ] `errors='strict'|'ignore'|'replace'|'surrogateescape'`
- [ ] `sys.stdout.encoding`, `sys.getdefaultencoding()`

#### 6.3 bytes и bytearray
- [ ] Индексация возвращает `int`
- [ ] Срезы возвращают `bytes`/`bytearray`
- [ ] `bytes(iterable_of_ints)` — создание bytes из int (0–255); `bytes([65, 66, 67])` → `b'ABC'`
- [ ] `bytes.decode()`, `str.encode()` — преобразование bytes↔str; параметры `encoding`, `errors`
- [ ] `str.join(iterable)` — правильная конкатенация строк; `''.join(parts)` вместо цикла с `+=`; `sep.join(iterable)`
- [ ] `bytearray` — изменяемый

---

## Часть III. Стандартная библиотека (stdlib)

> **Материалы:** [→ Навигация по Части III](pact/03_stdlib_standardnaya_biblioteka/index.md)

### 7. Удалённые и переименованные модули (Py2 → Py3)

#### Синтаксис и builtins
- [ ] `exec` — функция, не инструкция; `exec(code, globals, locals)`; принимает строку или code object
- [ ] `print` — функция; `print(x)` вместо `print x`
- [ ] `<>` — удалён; только `!=`
- [ ] `cmp(a, b)` — удалён; использовать `(a > b) - (a < b)`; `functools.cmp_to_key` для `sorted(key=...)`
- [ ] `apply(f, args, kwargs)` — удалён; использовать `f(*args, **kwargs)`
- [ ] `` `x` `` (backticks) — удалён; использовать `repr(x)`
- [ ] `execfile('script.py')` — удалён; `exec(open('script.py').read())` или `runpy.run_path()`
- [ ] `xrange` → `range`; `range` теперь ленивый
- [ ] `dict.iteritems()`, `.iterkeys()`, `.itervalues()` — удалены; `.items()`, `.keys()`, `.values()` возвращают view
- [ ] `unicode` — удалён; `str` всегда Unicode
- [ ] `long` — удалён; `int` неограниченной точности

#### Модули
- [ ] `urllib` + `urllib2` → `urllib.request`, `urllib.parse`, `urllib.error`
- [ ] `httplib` → `http.client`
- [ ] `ConfigParser` → `configparser`
- [ ] `Queue` → `queue`
- [ ] `cPickle` → `pickle` (C-реализация по умолчанию)
- [ ] `__builtin__` → `builtins`
- [ ] `reduce` → `functools.reduce`
- [ ] `raw_input` → `input`
- [ ] `basestring` — удалён (использовать `(str, bytes)`)
- [ ] `dict.has_key()` — удалён, использовать `in`
- [ ] `file` — удалён, использовать `open()`

### 7a. ВСЕ модули стандартной библиотеки (imports) — полный справочник *(см. Путь обучения: Справочники)*

#### Специальные и встроенные
- [ ] `__future__` — фичи из будущих версий; `from __future__ import annotations`, `division`, `print_function`
- [ ] `__main__` — точка входа; `if __name__ == '__main__':`; `python -m package.module`
- [ ] `builtins` — встроенные объекты; `dir(builtins)` — список builtins

#### abc — abstract base classes
- [ ] `abc` — ABC; `@abstractmethod`; `ABC` базовый класс; `abstractmethod`, `abstractclassmethod`, `abstractstaticmethod`
- [ ] `abc.ABCMeta` — метакласс ABC

#### argparse, optparse, getopt
- [ ] `argparse` — парсинг аргументов CLI; `ArgumentParser`; `add_argument`, `parse_args`; `nargs`, `choices`, `action`
- [ ] `optparse` — устаревший парсер опций
- [ ] `getopt` — простой парсер; C-подобный getopt

#### array, struct
- [ ] `array` — массивы однотипных чисел; `array.array(typecode, iterable)`
- [ ] `struct` — упаковка/распаковка бинарных данных; `pack`, `unpack`; format strings

#### ast, dis, tokenize, symtable
- [ ] `ast` — AST; `ast.parse()`, `ast.dump()`; `ast.literal_eval()` — безопасный eval литералов
- [ ] `dis` — дизассемблер байткода; `dis.dis(func)`
- [ ] `tokenize` — токенизатор исходного кода
- [ ] `symtable` — таблицы символов компилятора

#### asyncio
- [ ] `asyncio` — асинхронный I/O; `async`/`await`; `asyncio.run()`; `Task`, `Future`; `create_task`, `gather`
- [ ] `asyncio.Queue`, `asyncio.Lock`, `asyncio.Semaphore`
- [ ] `asyncio.subprocess`; `asyncio.streams`; `run_in_executor`

#### base64, binascii, codecs
- [ ] `base64` — base64, base32, base16; `b64encode`, `b64decode`
- [ ] `binascii` — hexlify, unhexlify; binary ↔ ASCII
- [ ] `codecs` — регистрация и поиск кодеков; `codecs.encode()`, `codecs.decode()`; StreamReader/Writer

#### bisect, heapq
- [ ] `bisect` — бинарный поиск; `bisect_left`, `bisect_right`; `insort_left`, `insort_right`
- [ ] `heapq` — куча; `heappush`, `heappop`, `heapify`; `nlargest`, `nsmallest`

#### collections, collections.abc
> Подробнее: раздел 11 (collections), раздел 11a (подклассирование).

- [ ] `collections` — `deque`, `Counter`, `defaultdict`, `OrderedDict`, `ChainMap`, `namedtuple`
- [ ] `collections.abc` — ABC для контейнеров; `Iterable`, `Iterator`, `Mapping`, `Sequence`, `Callable`, `Generator`

#### compress: gzip, bz2, lzma, zipfile, tarfile
- [ ] `gzip` — gzip; `open()` для чтения/записи
- [ ] `bz2` — bzip2
- [ ] `lzma` — LZMA
- [ ] `zipfile` — ZIP; `ZipFile`, `ZipInfo`; `extractall`, `write`
- [ ] `tarfile` — TAR; gzip, bz2, lzma

#### concurrent
- [ ] `concurrent.futures` — `ThreadPoolExecutor`, `ProcessPoolExecutor`; `submit`, `map`; `Future.result()`
- [ ] `concurrent.interpreters` — множественные интерпретаторы (PEP 554)

#### configparser, json, csv, tomllib
- [ ] `configparser` — INI-подобные конфиги; `ConfigParser`; `[section]`, `key=value`
- [ ] `json` — JSON; `json.load()`, `json.dump()`; `json.loads()`, `json.dumps()`; `JSONDecodeError`
- [ ] `csv` — CSV; `csv.reader()`, `csv.writer()`; `csv.DictReader`, `DictWriter`
- [ ] `tomllib` (3.11+) — парсинг TOML; read-only

#### contextlib, contextvars
- [ ] `contextlib` — `contextmanager`, `@contextmanager`; `closing`, `suppress`, `nullcontext`; `ExitStack`
- [ ] `contextvars` — переменные контекста; `ContextVar`; для async без глобальных переменных

#### copy, pickle, marshal
- [ ] `copy` — `copy.copy()`, `copy.deepcopy()`
- [ ] `pickle` — сериализация Python-объектов; `pickle.dump`, `pickle.load`; протоколы; `pickletools`
- [ ] `marshal` — внутренняя сериализация; не для произвольных данных

#### dataclasses, enum
- [ ] `dataclasses` — `@dataclass`, `field()`, `asdict`, `astuple`, `replace`
- [ ] `enum` — `Enum`, `IntEnum`, `StrEnum` (3.11+), `Flag`, `IntFlag`; `auto()`, `@unique`

#### datetime, time, calendar
- [ ] `datetime` — `date`, `time`, `datetime`, `timedelta`, `timezone`; `strftime`, `strptime`
- [ ] `datetime.datetime.fromisoformat(string)` (3.7+) — парсинг ISO 8601 строки; `date.fromisoformat()`, `time.fromisoformat()`
- [ ] `time` — `time.time()`, `time.sleep()`, `time.monotonic()`; `time.perf_counter()`
- [ ] `calendar` — календарные функции

#### decimal, fractions, numbers, statistics, math, cmath
- [ ] `decimal` — `Decimal`; точная десятичная арифметика; `getcontext()`
- [ ] `fractions` — `Fraction`; рациональные числа
- [ ] `numbers` — ABC: `Number`, `Complex`, `Real`, `Integral`
- [ ] `statistics` — `mean`, `median`, `mode`, `stdev`, `variance`
- [ ] `math` — математика; `sin`, `cos`, `sqrt`, `ceil`, `floor`, `isnan`, `inf`
- [ ] `cmath` — математика для complex

#### difflib, filecmp
- [ ] `difflib` — сравнение последовательностей; `unified_diff`, `SequenceMatcher`
- [ ] `filecmp` — сравнение файлов; `cmp()`, `dircmp()`

#### email, mimetypes, html
- [ ] `email` — парсинг MIME; `message_from_string()`; `email.mime.*`; multipart
- [ ] `mimetypes` — расширение → MIME; `guess_type()`
- [ ] `html` — `html.escape()`, `html.unescape()`; `html.parser` — HTMLParser

#### errno, faulthandler, traceback, warnings
- [ ] `errno` — коды ошибок; `errno.ENOENT`, `errno.EACCES`
- [ ] `faulthandler` — дамп traceback при segfault
- [ ] `traceback` — `traceback.format_exc()`, `traceback.print_exception()`
- [ ] `warnings` — `warnings.warn()`; `DeprecationWarning`, `FutureWarning`; `filterwarnings`

#### functools, operator
- [ ] `functools` — `partial`, `reduce`, `lru_cache`, `cache` (3.9+), `wraps`, `cmp_to_key`, `total_ordering`, ` singledispatch`
- [ ] `operator` — `add`, `mul`, `itemgetter`, `attrgetter`, `methodcaller`

#### gc, sys, types, copyreg
- [ ] `gc` — сборщик мусора; `gc.collect()`, `gc.get_objects()`; `gc.disable()`
- [ ] `sys` — `sys.argv`, `sys.path`, `sys.modules`, `sys.stdout`, `sys.exit()`; `sys.getsizeof()`; `sys.version_info`; `sys.breakpointhook`
- [ ] `types` — `types.FunctionType`, `types.ModuleType`; `types.SimpleNamespace`; `types.new_class()`
- [ ] `copyreg` — регистрация функций для pickle

#### getpass, getopt, gettext, locale
- [ ] `getpass` — `getpass.getpass()`; `getpass.getuser()`
- [ ] `gettext` — интернационализация; `gettext.translation()`
- [ ] `locale` — форматирование по локали

#### glob, fnmatch, pathlib, os, os.path, shutil, tempfile, fileinput
- [ ] `glob` — `glob.glob(pattern)`; `glob.iglob()`
- [ ] `fnmatch` — сопоставление имён файлов; `fnmatch.fnmatch()`
- [ ] `pathlib` — `Path`, `PurePath`; `.read_text()`, `.glob()`, `/`
- [ ] `os` — `os.path`, `os.environ`, `os.getenv()`, `os.listdir()`, `os.scandir()`, `os.walk()`; `os.mkdir()`, `os.remove()`
- [ ] `shutil` — `copy()`, `copytree()`, `rmtree()`, `move()`; `shutil.which()`
- [ ] `tempfile` — `TemporaryFile()`, `NamedTemporaryFile()`, `TemporaryDirectory()`; `mkstemp()`, `mkdtemp()`
- [ ] `fileinput` — итерация по stdin или списку файлов

#### hashlib, hmac, secrets
- [ ] `hashlib` — `md5()`, `sha256()`, `blake2b()`; `.update()`, `.digest()`, `.hexdigest()`
- [ ] `hmac` — HMAC; `hmac.new(key, msg, digestmod)`
- [ ] `secrets` — криптостойкие случайные; `token_hex()`, `token_urlsafe()`; для паролей

#### http, urllib, ftplib, smtplib, poplib, imaplib, socket, ssl
- [ ] `http.client` — низкоуровневый HTTP; `HTTPConnection`, `HTTPSConnection`
- [ ] `http.server` — простой HTTP-сервер; `BaseHTTPRequestHandler`
- [ ] `urllib.request` — `urlopen()`, `Request`; `urllib.parse` — `urlparse`, `urljoin`; `urllib.error` — `URLError`, `HTTPError`
- [ ] `socket` — низкоуровневые сокеты; `socket.socket()`
- [ ] `ssl` — TLS/SSL; `ssl.wrap_socket()`; сертификаты

#### importlib, pkgutil, runpy, modulefinder
- [ ] `importlib` — `importlib.import_module()`; `importlib.util.spec_from_file_location()`; `importlib.resources`
- [ ] `importlib.metadata` — метаданные пакетов; `version()`, `requires()`
- [ ] `pkgutil` — `pkgutil.iter_modules()`; `pkgutil.walk_packages()`
- [ ] `runpy` — `runpy.run_path()`, `runpy.run_module()`
- [ ] `modulefinder` — поиск модулей, используемых скриптом

#### inspect, pdb, trace, tracemalloc, timeit, cProfile, profile, pstats
- [ ] `inspect` — `inspect.signature()`, `inspect.getsource()`; `inspect.stack()`; `Parameter`, `Signature`
- [ ] `pdb` — отладчик; `pdb.set_trace()`; `breakpoint()` вызывает его
- [ ] `trace` — трассировка выполнения
- [ ] `tracemalloc` — трассировка аллокаций памяти
- [ ] `timeit` — замер времени; `timeit.timeit()`, `timeit.Timer`
- [ ] `cProfile`, `profile` — профилировщики; `pstats` — анализ результатов

#### io, select, selectors, mmap
- [ ] `io` — `io.StringIO`, `io.BytesIO`; `io.TextIOWrapper`; `io.open`
- [ ] `select` — `select.select()`, `select.poll()`; multiplexing I/O
- [ ] `selectors` — высокоуровневый I/O multiplexing; `DefaultSelector`
- [ ] `mmap` — memory-mapped files

#### ipaddress, ssl
- [ ] `ipaddress` — IPv4/IPv6; `ip_address()`, `ip_network()`; проверка, арифметика

#### itertools, more_itertools (внешний)
- [ ] `itertools` — `chain`, `cycle`, `islice`, `groupby`, `tee`, `zip_longest`; `permutations`, `combinations`, `product`; `accumulate`, `pairwise` (3.10+)

#### logging
- [ ] `logging` — `logging.basicConfig()`; `getLogger()`; `debug`, `info`, `warning`, `error`; `logging.handlers`; `logging.config`

#### multiprocessing, threading, queue, _thread
- [ ] `multiprocessing` — `Process`, `Pool`; `Queue`, `Pipe`; `Manager`; `shared_memory`; spawn/fork
- [ ] `threading` — `Thread`; `Lock`, `RLock`, `Semaphore`, `Event`; `ThreadLocal`; `daemon`
- [ ] `queue` — `Queue`, `LifoQueue`, `PriorityQueue`; thread-safe
- [ ] `_thread` — низкоуровневый threading API

#### numbers — см. decimal
#### os — см. glob
#### pathlib — см. glob
#### pdb — см. inspect
#### pickle — см. copy
#### pprint, reprlib
- [ ] `pprint` — `pprint.pprint()`; форматированный вывод
- [ ] `reprlib` — `reprlib.repr()` с ограничением длины

#### random
- [ ] `random` — `random()`, `randint()`, `choice()`, `choices()`, `shuffle()`, `sample()`; `seed()`; не для криптографии

#### re
- [ ] `re` — `re.match()`, `re.search()`, `re.findall()`, `re.sub()`, `re.split()`; `re.compile()`; группы, named groups; `re.MULTILINE`, `re.DOTALL`

#### sched, shelve, sqlite3, dbm
- [ ] `sched` — планировщик событий; `scheduler.enter()`, `run()`
- [ ] `shelve` — персистентное хранилище dict-подобное
- [ ] `sqlite3` — SQLite; `connect()`, `cursor()`; `execute()`, `fetchall()`

#### signal, atexit
- [ ] `signal` — `signal.signal()`, `signal.alarm()`; SIGTERM, SIGINT; обработчики
- [ ] `atexit` — `atexit.register()` — функции при выходе

#### string, textwrap, unicodedata
- [ ] `string` — `string.ascii_letters`, `string.digits`; `string.Template`; `string.templatelib` (3.15+)
- [ ] `textwrap` — `wrap()`, `fill()`, `dedent()`; перенос текста
- [ ] `unicodedata` — `unicodedata.name()`, `unicodedata.category()`; нормализация NFC, NFD

#### threading — см. multiprocessing
#### typing — см. Часть III, раздел 9
#### unittest, doctest
- [ ] `unittest` — `TestCase`; `setUp`, `tearDown`; `assertEqual`, `assertRaises`; `mock`
- [ ] `doctest` — тесты в docstring; `doctest.testmod()`

#### uuid, weakref
- [ ] `uuid` — `uuid.uuid4()`; UUID v1–v5
- [ ] `weakref` — `weakref.ref()`, `weakref.proxy()`; `WeakValueDictionary`, `WeakKeyDictionary`; `weakref.finalize()`

#### zoneinfo (3.9+)
- [ ] `zoneinfo` — IANA timezone; `ZoneInfo('Europe/Moscow')`; замена pytz

#### Платформо-зависимые (Unix / Windows)
- [ ] `posix`, `pwd`, `grp`, `termios`, `tty`, `fcntl`, `pty`, `resource` (Unix)
- [ ] `msvcrt`, `winreg` (Windows)
- [ ] `curses` — терминальный UI (Unix, нужна ncurses)

#### Специализированные (реже используемые)
- [ ] `aifc`, `sunau` — аудио (часть deprecated)
- [ ] `audioop` — операции над аудио (deprecated в 3.13)
- [ ] `colorsys` — конвертация цветовых пространств
- [ ] `graphlib` — топологическая сортировка (3.9+)
- [ ] `mailbox`, `mailcap` — почтовые ящики
- [ ] `netrc` — .netrc файлы
- [ ] `plistlib` — Apple plist
- [ ] `quopri` — quoted-printable кодирование
- [ ] `smtpd` — SMTP сервер (deprecated в 3.12)
- [ ] `socketserver` — TCP/UDP серверы
- [ ] `stat` — константы режимов файлов
- [ ] `stringprep` — подготовка строк (RFC 3453)
- [ ] `xml.etree.ElementTree`, `xml.dom`, `xml.sax` — парсинг XML
- [ ] `tkinter` — GUI Tk
- [ ] `turtle` — образовательная графика

### 8. pathlib и файловая система

- [ ] `Path`, `PurePath`, `PurePosixPath`, `PureWindowsPath`
- [ ] **PurePath vs Path**: PurePath — манипуляции с путями без доступа к ФС; Path — с операциями I/O; кроссплатформенность
- [ ] `.read_text()`, `.write_text()`, `.read_bytes()`, `.write_bytes()`
- [ ] `.glob()`, `.rglob()`
- [ ] `Path.walk()` (3.12+) — рекурсивный обход; `top_down`; аналог `os.walk()`
- [ ] `/` для конкатенации путей
- [ ] `.resolve()`, `.absolute()`
- [ ] `Path.cwd()`, `Path.home()`

#### 8a. Файловая система: низкоуровневые детали
- [ ] **`os.scandir()` vs `os.listdir()`**: scandir возвращает `DirEntry` с кешированными атрибутами (тип, размер) — быстрее для фильтрации
- [ ] **`mmap`**: memory-mapped files; zero-copy чтение/запись; разделяемая память между процессами
- [ ] **`os.sendfile()`**: zero-copy передача файлов в сокеты; обход пользовательского пространства

#### 8b. Время и даты: тонкости
- [ ] **`time.monotonic()` vs `time.time()`**: monotonic — не зависит от системного времени (защита от коррекции NTP); для измерения интервалов
- [ ] **datetime naive vs aware**: naive — без временной зоны; сравнение/арифметика между разными зонами — проблемы
- [ ] **Летнее время (DST)**: 2:30 AM дважды в день при переходе; атрибут `fold` в datetime (PEP 495)
- [ ] **zoneinfo** (3.9+): IANA timezone database; как обновляется; локальные правила перехода

### 9. typing

- [ ] `typing.List`, `typing.Dict`, `typing.Tuple`, `typing.Set`
- [ ] В Python 3.9+ — `list[str]` вместо `List[str]`
- [ ] `Optional[T]` = `Union[T, None]`
- [ ] `Union`, `Callable`, `TypeVar`, `Generic`
- [ ] `Callable[..., Ret]` — Ellipsis для «любые аргументы»
- [ ] `Protocol` — structural subtyping (PEP 544)
- [ ] `Literal`, `Final`, `TypedDict`
- [ ] `NewType('UserId', int)` — семантически отличный тип; не создаёт runtime-стоимости
- [ ] `ClassVar[T]` — атрибут класса, не экземпляра; для type checker
- [ ] `ParamSpec`, `Concatenate` (для декораторов)
- [ ] `@overload` для перегрузки сигнатур
- [ ] `typing.Annotated[T, x, y]` (PEP 593) — метаданные в типах; используется FastAPI, pydantic
- [ ] `typing.Type[T]` — тип класса; для фабрик: `def factory(cls: Type[T]) -> T`; `isinstance` принимает tuple типов
- [ ] `typing.Any` — escape hatch; отключает проверку; использовать минимально
- [ ] `from __future__ import annotations` (PEP 563, 3.7+) — отложенная оценка аннотаций; все как строки; избегание forward reference

### 9a. Теория типизации (variance, type guards, narrowing)

#### Variance (ковариантность, контравариантность, инвариантность)
- [ ] **Covariant** — `Producer[T]`; если `A <: B`, то `Producer[A] <: Producer[B]`; используется в return type
- [ ] **Contravariant** — `Consumer[T]`; если `A <: B`, то `Consumer[B] <: Consumer[A]`; используется в аргументах
- [ ] **Invariant** — `Container[T]`; ни covariant, ни contravariant; используется в mutables (list, dict)
- [ ] `TypeVar('T', covariant=True)` — covariant; `TypeVar('T', contravariant=True)` — contravariant
- [ ] `Callable[[Arg], Ret]` — contravariant в Arg, covariant в Ret
- [ ] Зачем: типобезопасность при подстановке типов; `list` — invariant, т.к. mutable

#### Type guards и narrowing
- [ ] **Type narrowing** — сужение типа после проверки; `if isinstance(x, int):` — в блоке x: int
- [ ] **Type guard** — `TypeGuard[T]`; функция, которая сужает тип; `def is_str(x: Any) -> TypeGuard[str]:`
- [ ] `typing.assert_type(x, T)` — проверка на этапе type check; не runtime
- [ ] `typing.cast(T, x)` — явное приведение типа; только для type checker; не runtime
- [ ] Narrowing: `if x is None:`, `if isinstance(x, T):`, `if hasattr(x, 'attr'):`
- [ ] PEP 647: `TypeGuard` — пользовательские type guards; `@typing.overload` для narrowing
- [ ] Exhaustive checking — `assert_never(x)` в `else`; типобезопасность match/case

#### Structural vs nominal subtyping
- [ ] **Nominal** — подтип по явному наследованию; `class B(A):`
- [ ] **Structural** — подтип по структуре (протокол); `Protocol` в Python
- [ ] Утиная типизация — structural; «если ходит как утка…»
- [ ] `@runtime_checkable` — `isinstance(x, Protocol)` работает для Protocol

### 10. dataclasses

- [ ] `@dataclass`
- [ ] `@dataclass(slots=True)` (3.10+) — автоматический `__slots__`; экономия памяти; несовместимо с `__dict__`
- [ ] `field()`, `default`, `default_factory`
- [ ] `repr`, `eq`, `order`, `frozen`
- [ ] `__post_init__`
- [ ] Наследование dataclass
- [ ] `dataclasses.asdict()`, `dataclasses.astuple()`
- [ ] `dataclasses.replace(obj, **changes)` — копия с изменениями
- [ ] `field(init=False)`, `field(repr=False)`, `field(compare=False)`, `field(hash=None)`
- [ ] `field(metadata={})` — метаданные; `fields(obj)` — список полей
- [ ] `dataclasses.make_dataclass()`, `is_dataclass()`
- [ ] `dataclasses.KW_ONLY` (3.10+) — keyword-only поля после разделителя

### 11. collections

- [ ] `defaultdict` — `.default_factory`; при отсутствии ключа вызывается фабрика; `defaultdict(list)` для группировки
- [ ] `Counter` — подсчёт элементов; `.most_common(n)`; арифметика `+`, `-`; `elements()`
- [ ] `OrderedDict` (с 3.7 порядок dict гарантирован, но OrderedDict имеет доп. методы)
- [ ] `namedtuple`
- [ ] `deque` — `deque(maxlen=N)` — ограниченная очередь; автоматическое отбрасывание при переполнении; скользящее окно
- [ ] **deque методы**: `append(x)`, `appendleft(x)`, `pop()`, `popleft()`, `extend(iterable)`, `extendleft(iterable)`, `rotate(n)` — сдвиг на n; атрибут `maxlen` — None или int
- [ ] `ChainMap` — объединение нескольких dict; поиск по цепочке; для layered config, defaults + overrides
- [ ] `UserDict`, `UserList`, `UserString`

### 11a. Подклассирование встроенных типов: тёмные углы

- [ ] **Подклассирование list/dict/str**: `list.sort()` не вызывает `__setitem__`; `dict.update()` не вызывает `__setitem__` — оптимизации обходят Python-методы
- [ ] **Обход**: `UserList`, `UserDict`, `UserString` — реализованы через композицию; все методы вызывают Python-код
- [ ] **`obj.__class__ = NewClass`**: когда работает (обычные объекты), когда нет (встроенные типы — ограничения)
- [ ] **`__slots__` и наследование**: `__slots__` не наследуется автоматически; как комбинировать слоты в иерархии; `__weakref__` в слотах при необходимости

### 12. functools

- [ ] `functools.partial`
- [ ] `functools.reduce(func, iterable, initial)` — свёртка; `initial` — начальное значение (иначе первый элемент); `reduce(add, [1,2,3], 0)`
- [ ] `functools.lru_cache` — maxsize, typed
- [ ] `functools.wraps` — сохранение метаданных декоратора
- [ ] `functools.cmp_to_key`
- [ ] `functools.cached_property` (Python 3.8+)
- [ ] `functools.singledispatch` — перегрузка по первому аргументу; для функций
- [ ] `functools.singledispatchmethod` (3.4+) — перегрузка методов по первому аргументу; декоратор для методов класса

### 13. itertools

- [ ] `chain`, `chain.from_iterable`
- [ ] `itertools.tee(iterable, n=2)` — разветвление итератора; каждый tee — независимый итератор; кеширование
- [ ] `cycle`, `repeat`
- [ ] `islice`, `takewhile`, `dropwhile`
- [ ] `groupby` — важно сортировать перед groupby
- [ ] `zip_longest`
- [ ] `permutations`, `combinations`, `product`
- [ ] `accumulate`, `pairwise` (3.10+)
- [ ] `starmap(func, iterable)` — `func(*args)` для каждого args; аргументы уже распакованы
- [ ] `compress(data, selectors)` — фильтр по маске; где selector истинен
- [ ] `filterfalse(pred, iterable)` — элементы, для которых pred ложен; обратное к filter

### 14. contextlib

- [ ] `@contextmanager` — генераторный контекст
- [ ] `contextlib.suppress`
- [ ] `contextlib.redirect_stdout` / `redirect_stderr`
- [ ] `contextlib.ExitStack` — динамический набор контекстов
- [ ] `contextlib.nullcontext`

### 15. Прочие важные модули stdlib

> Полный список модулей stdlib — см. раздел 7a (справочник).

- [ ] `argparse` — парсинг аргументов
- [ ] `logging` — логирование
- [ ] `json` — сериализация JSON
- [ ] `re` — регулярные выражения
- [ ] `os`, `os.path` — работа с ОС; `os.environ` — переменные окружения; `os.getenv()`, `os.environ.get()`
- [ ] `shutil` — копирование, перемещение; `copy()`, `copytree()`, `rmtree()`, `move()`; `shutil.which()`
- [ ] `getpass` — ввод пароля без эха; `getpass.getpass()`, `getpass.getuser()`
- [ ] `subprocess` — запуск процессов
- [ ] `threading`, `multiprocessing`
- [ ] `concurrent.futures` — ThreadPoolExecutor, ProcessPoolExecutor
- [ ] `tempfile` — `mkstemp()`, `mkdtemp()`; `TemporaryFile()`, `NamedTemporaryFile()`, `TemporaryDirectory()` — контекстные менеджеры; `tempfile.gettempdir()`
- [ ] `hashlib` — `hashlib.md5()`, `sha256()`, `blake2b()`; `.update()`, `.digest()`, `.hexdigest()`; алгоритмы (md5, sha1, sha256, sha512)
- [ ] `random` — `random.random()`, `randint()`, `choice()`, `choices(seq, k=1, weights=None)` (выбор с возвращением), `shuffle()`; не для криптографии; `random.seed()` для воспроизводимости
- [ ] `secrets` — криптографически стойкие случайные числа; `secrets.token_hex()`, `token_urlsafe()`; для токенов/паролей
- [ ] `enum` — перечисления

### 15a0. enum — углублённо

- [ ] `Enum` — базовый; `IntEnum` — наследует int; сравнение с числами
- [ ] `StrEnum` (3.11+) — наследует str; строковое сравнение; `str(Member)` без `.value`
- [ ] `Flag`, `IntFlag` — битовые флаги; `|`, `&`, `^`, `~`
- [ ] `@enum.unique` — уникальные значения; `auto()` — автозначения
- [ ] `Enum.value`, `Enum.name`; итерация по членам
- [ ] `member in Enum` — проверка членства; `Enum['NAME']`

#### io
- [ ] `io.StringIO` — строковый буфер; `getvalue()`, `read()`, `write()`
- [ ] `io.BytesIO` — буфер байт; для тестов, сериализации
- [ ] `io.TextIOWrapper`, `io.BufferedIOBase`, `io.RawIOBase`
- [ ] `io.BufferedIOBase.readinto(buffer)` — zero-copy чтение в pre-allocated buffer; возвращает число прочитанных байт
- [ ] `open()` — `buffering`, `newline`, `errors`; бинарный vs текстовый режим

#### decimal, fractions, statistics — числовая модель (углублённо)
- [ ] `decimal.Decimal` — точные десятичные; `getcontext()`, `ROUND_HALF_UP`, `ROUND_HALF_EVEN` (banker's rounding)
- [ ] **decimal контекст**: `getcontext().prec` — точность; `decimal.localcontext()` — локальный контекст
- [ ] `Decimal.quantize()` — округление до заданной точности
- [ ] **decimal vs float**: float — IEEE 754, двоичная арифметика; decimal — десятичная; для финансов — decimal
- [ ] **IEEE 754 тонкости**: почему `0.1 + 0.2 != 0.3`; двоичное представление дробей
- [ ] `math.nextafter(x, y)`, `math.ulp(x)`, `math.copysign(x, y)` — работа с float
- [ ] `fractions.Fraction` — точное представление рациональных; сравнение с float без потерь
- [ ] **Fraction и float**: `Fraction(0.1) ≠ Fraction(1, 10)` — потери точности; создавать из строки: `Fraction('0.1')`
- [ ] **math.fsum() vs sum()**: fsum — компенсированная сумма для float; избегание ошибок округления при суммировании
- [ ] **numbers** — абстрактная иерархия: Number → Complex → Real → Rational → Integral; как создать совместимый числовой тип
- [ ] **int неограниченной точности**: реализация как массива «цифр» в базе 2³⁰ (или 2¹⁵); `sys.int_info`
- [ ] `statistics` — `mean`, `median`, `mode`, `stdev`, `variance`; `StatisticsError`

#### struct, array
- [ ] `struct.pack(fmt, *values)`, `struct.unpack(fmt, buffer)` — бинарные данные
- [ ] Форматы: `i`, `f`, `d`, `s`, `?`; порядок байт: `>`, `<`, `=`
- [ ] `array.array(typecode)` — компактные массивы; `typecodes` — `b`, `i`, `f`, `d`

#### collections.abc
- [ ] `Iterable`, `Iterator`, `Generator`
- [ ] `Sequence`, `MutableSequence`, `Mapping`, `MutableMapping`
- [ ] `Set`, `MutableSet`, `Collection`
- [ ] `Callable`, `Container`, `Sized`, `Hashable`
- [ ] `Awaitable`, `AsyncIterator`, `AsyncGenerator`
- [ ] `Reversible`, `Buffer` (3.12+); использование для type hints

#### sys, platform, errno
- [ ] `sys.version_info` — кортеж (major, minor, micro); проверка версии: `sys.version_info >= (3, 10)`; `sys.version`
- [ ] `sys.getsizeof(obj)`, `sys.getrefcount(obj)` — размер, ссылки
- [ ] `sys.setrecursionlimit(n)`, `sys.getrecursionlimit()` — стек вызовов; RecursionError; хвостовая рекурсия не оптимизируется
- [ ] `sys.modules`, `sys.path`, `sys.argv`, `sys.exit()`
- [ ] `sys.stdout`, `sys.stderr`, `sys.stdin`; перенаправление
- [ ] `platform.system()`, `platform.machine()`, `platform.python_implementation()`
- [ ] `errno` — коды ошибок; `errno.ENOENT`, `errno.EACCES`

#### Ограничения и границы реализации
- [ ] **`sys.getrecursionlimit()`**: стек вызовов; RecursionError; как увеличить (осторожно); хвостовая рекурсия не оптимизируется
- [ ] **`sys.maxsize`**: максимальный размер коллекций; зависит от разрядности (2**63 - 1 на 64-bit); Py_ssize_t
- [ ] **Глубина вложенности**: ограничение на вложенность выражений (≈1000 по умолчанию); `ast.parse(mode='exec')`
- [ ] **Длина строковых литералов**: ограничения компилятора; конкатенация длинных строк через + в исходном коде

#### traceback, warnings, atexit, faulthandler
- [ ] `traceback.format_exc()`, `traceback.print_exception()`, `traceback.extract_tb()`
- [ ] `warnings.warn()`, `warnings.filterwarnings()`, `warnings.catch_warnings()`
- [ ] **Категории warnings**: `DeprecationWarning` (скрыт по умолчанию в `__main__`); `FutureWarning` (показывается); `PendingDeprecationWarning`; `warnings.warn('msg', DeprecationWarning)` — правильная пометка устаревшего API
- [ ] `atexit.register(func)` — вызов при выходе
- [ ] `faulthandler.enable()` — dump traceback при segfault; `dump_traceback()`
- [ ] **faulthandler internals**: перехват SIGSEGV/SIGABRT; вывод трейсбэка до падения интерпретатора

#### importlib.resources, importlib.metadata (3.8+)
- [ ] `importlib.resources.files(pkg)` — доступ к файлам пакета
- [ ] `importlib.resources.as_file()` — временный путь
- [ ] `importlib.metadata.version('package')` — версия установленного пакета
- [ ] `importlib.metadata.entry_points()` — entry points (plugins)

#### tomllib (3.11+), graphlib (3.9+)
- [ ] `tomllib.loads()`, `tomllib.load()` — чтение TOML (только read; запись — tomli-w)
- [ ] `graphlib.TopologicalSorter` — топологическая сортировка; DAG
- [ ] `sorter.add()`, `sorter.prepare()`, `sorter.get_ready()`, `sorter.done()`

#### functools.cache (3.9+), zip(strict)
- [ ] `@functools.cache` — `lru_cache(maxsize=None)`; неограниченный кеш
- [ ] `zip(a, b, strict=True)` — проверка равной длины

### 15b. Регулярные выражения (re) — углублённо

- [ ] `re.compile(pattern, flags)` — скомпилированный паттерн; быстрее при многократном использовании
- [ ] `re.match()`, `re.search()`, `re.fullmatch()` — match, search, full match
- [ ] `re.findall()`, `re.finditer()` — все совпадения; finditer — итератор Match
- [ ] `re.sub()`, `re.subn()` — замена; `count`, callback
- [ ] `re.split()` — разбиение по паттерну
- [ ] Флаги: `re.I` (ignore case), `re.M` (multiline), `re.S` (dotall), `re.X` (verbose)
- [ ] Named groups: `(?P<name>...)`; `match.groupdict()`, `match.group('name')`
- [ ] Backreferences: `\1`, `(?P=name)`
- [ ] Lookahead/lookbehind: `(?=...)`, `(?!...)`, `(?<=...)`, `(?<!...)`
- [ ] Модуль `regex` — дополнительные возможности (backreferences, fuzzy)

### 15c0. Системные вызовы и ОС-интеграция

- [ ] **OSError иерархия**: FileNotFoundError, PermissionError, TimeoutError — наследуют OSError; маппинг errno → исключение
- [ ] **os и системные вызовы**: `os.open()` оборачивает open(2); `os.stat()` → stat(2); обработка EINTR (прерванные системные вызовы)
- [ ] **signal и системные вызовы**: `signal.siginterrupt(signum, flag)` — перезапускать ли системные вызовы после обработчика сигнала; поведение по умолчанию

### 15c. subprocess — углублённо

- [ ] `subprocess.run(cmd, capture_output=True, text=True, timeout=N)` — возвращает `CompletedProcess`
- [ ] `subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)` — низкоуровневый
- [ ] `process.communicate(input=None)` — отправка в stdin, ожидание завершения
- [ ] `subprocess.PIPE`, `subprocess.DEVNULL`, `subprocess.STDOUT`
- [ ] `shell=True` — риски безопасности; injection; предпочитать `list` аргументов
- [ ] `env`, `cwd`, `timeout`; `check=True` — raise при ненулевом коде
- [ ] `subprocess.CalledProcessError`, `subprocess.TimeoutExpired`
- [ ] **CompletedProcess**: `returncode`, `stdout`, `stderr`, `args` — атрибуты результата `run()`

### 15d. Unicode: за пределами encode/decode

#### unicodedata, normalisation
- [ ] `unicodedata.normalize('NFC'|'NFD'|'NFKC'|'NFKD', s)` — нормализация Unicode
- [ ] **Каноническая** (NFC/NFD) vs **совместимостная** (NFKC/NFKD); когда что использовать; сравнение строк
- [ ] `unicodedata.category(c)` — категория символа; `unicodedata.name(c)`

#### Grapheme clusters и «символы»
- [ ] **Grapheme clusters**: флаг 🇷🇺 = 2 code points (U+1F1F7 U+1F1FA); эмодзи с модификаторами кожи
- [ ] `len('🇷🇺')` ≠ количество «видимых» символов; regex `\X` (модуль `regex`) для grapheme
- [ ] Как правильно считать «символы» для пользователя; разрезка строк

#### Bidirectional (bidi) и RTL
- [ ] **Bidirectional algorithm**: смешение LTR (латиница) и RTL (арабский, иврит)
- [ ] Корректное отображение; библиотека `python-bidi` для обработки

#### Surrogate pairs и UTF-16
- [ ] **Surrogate pairs** в UTF-16: символы > U+FFFF представляются двумя code units
- [ ] Среда Windows API — UTF-16; `surrogatepass` error handler для работы с surrogate
- [ ] `errors='surrogateescape'` — для round-trip байтов в str

### 15d1. textwrap, difflib

- [ ] `textwrap.wrap()`, `textwrap.fill()`, `textwrap.indent()`, `textwrap.dedent()`
- [ ] `textwrap.shorten()` — обрезка с многоточием
- [ ] `difflib.unified_diff()`, `difflib.SequenceMatcher()`, `difflib.Differ()`
- [ ] `difflib.get_close_matches()` — fuzzy matching

### 15e. Buffer protocol и memoryview

- [ ] Buffer protocol — низкоуровневый интерфейс для доступа к памяти
- [ ] `memoryview(obj)` — объект памяти без копирования; `bytes`, `bytearray`, `array`
- [ ] `mv[0]`, `mv[1:5]`, `mv.tobytes()`, `mv.tolist()`
- [ ] `mv.readonly`, `mv.format`, `mv.itemsize`, `mv.nbytes`
- [ ] `__getbuffer__`, `__releasebuffer__` — протокол (C-расширения)

### 15f. Дескриптор __set_name__ (3.6+)

- [ ] `__set_name__(self, owner, name)` — вызывается при создании класса
- [ ] `name` — имя атрибута в классе; удобно для дескрипторов
- [ ] Автоматический вызов; не нужно передавать имя вручную

### 15g. Модуль на уровне __getattr__ (PEP 562, 3.7+)

- [ ] `def __getattr__(name):` на уровне модуля — ленивая загрузка
- [ ] Вызывается при обращении к несуществующему атрибуту модуля
- [ ] `def __dir__():` — кастомный `dir(module)`

### 15h. Дополнительные модули stdlib (архивы, XML, i18n)

#### Архивы
- [ ] `zipfile` — ZIP; `ZipFile`, `ZipInfo`; чтение, запись; `extractall()`, `write()`
- [ ] `tarfile` — TAR; `open()`, `extractall()`; gzip, bz2, lzma
- [ ] `gzip`, `bz2`, `lzma` — сжатие; `open()` для чтения/записи
- [ ] `zlib` — низкоуровневое сжатие; `compress()`, `decompress()`

#### XML и HTML
- [ ] `xml.etree.ElementTree` — парсинг XML; `Element`, `fromstring()`, `parse()`
- [ ] `xml.dom`, `xml.sax` — альтернативные API
- [ ] `html.parser` — `HTMLParser`; `handle_starttag`, `handle_data`; базовый парсинг HTML
- [ ] `html.entities`, `html.escape()`, `html.unescape()`

#### Интернационализация
- [ ] `gettext` — переводы; `translation()`, `gettext()`, `ngettext()`
- [ ] `.po`, `.mo` файлы; `locale.getlocale()`, `locale.setlocale()`
- [ ] `locale` — форматирование чисел, дат; зависят от локали ОС

#### HTTP и прочее
- [ ] `http.server` — `python -m http.server 8000`; простой HTTP-сервер для разработки; `BaseHTTPRequestHandler`
- [ ] `email` — парсинг MIME; `email.message_from_string()`; заголовки, body; multipart
- [ ] `mimetypes` — `mimetypes.guess_type(path)`; маппинг расширений → MIME; `guess_extension()`

#### Планировщик и прочее
- [ ] `sched` — планировщик задач; `scheduler.enter()`, `scheduler.run()`
- [ ] `uuid` — `uuid.uuid4()`, `uuid.uuid5()`; уникальные идентификаторы
- [ ] `base64` — кодирование base64; `b64encode()`, `b64decode()`
- [ ] `binascii` — hex, base64; низкоуровневые преобразования
- [ ] `quopri` — quoted-printable; `codecs` — `codecs.open()`, `encode()`, `decode()`; регистрация кастомных кодеков; `open()` с encoding
- [ ] `netrc` — парсинг ~/.netrc; `shlex` — shell-подобный парсинг; `shlex.quote()` — экранирование для shell
- [ ] `fnmatch` — `fnmatch.fnmatch(name, pat)`; паттерны для имён файлов; `fnmatch.filter(names, pat)`
- [ ] `glob` — `glob.glob(pattern)`, `glob.iglob()`; `**` для рекурсии (3.5+); `pathlib.glob` альтернатива
- [ ] `os.walk(top)` — рекурсивный обход директорий; `(dirpath, dirnames, filenames)`; альтернатива `Path.walk()` (3.12)
- [ ] `webbrowser` — открытие URL в браузере; `webbrowser.open()`
- [ ] `ipaddress` — IPv4Address, IPv6Address, ip_network; валидация IP

#### CSV и конфигурация
- [ ] `csv` — `DictReader`, `DictWriter`; `Dialect`, `Sniffer`; `QUOTE_MINIMAL`
- [ ] `configparser` — INI-файлы; секции, опции; `interpolation`; `BasicInterpolation`

---

## Часть IV. Современный синтаксис Python 3

> **Материалы:** [→ Навигация по Части IV](pact/04_sovremennyj_sintaksis_python3/index.md)

### 16. f-strings

- [ ] Базовый синтаксис: `f'{x}'`
- [ ] Выражения: `f'{x**2}'`
- [ ] Форматирование: `f'{x:.2f}'`, `f'{n:>10}'`
- [ ] `f'{x=}'` — debug (Python 3.8+)
- [ ] Вложенные кавычки
- [ ] Дата/время: `f'{dt:%Y-%m-%d}'`

### 17. Распаковка и упаковка

- [ ] `a, b = 1, 2`
- [ ] `a, *rest = [1,2,3,4]`
- [ ] `*args` в вызовах: `func(*[1,2,3])`
- [ ] `**kwargs` в вызовах
- [ ] Распаковка в for: `for k, v in dict.items():`
- [ ] Распаковка словарей: `{**d1, 'x': 1}`

### 18. match/case (Python 3.10+)

- [ ] Сопоставление с образцом
- [ ] Сопоставление литералов, последовательностей, отображений
- [ ] `as` — захват подшаблона
- [ ] `|` — OR в образцах
- [ ] Guard: `case x if x > 0:`
- [ ] `_` — wildcard
- [ ] `__match_args__` — атрибут класса; порядок полей для позиционного сопоставления; `case Point(x, y):`

### 19. Walrus operator (:=) (Python 3.8+)

- [ ] Присваивание внутри выражения
- [ ] Использование в условиях: `if (n := len(data)) > 0:`
- [ ] В comprehensions: ограничения и стиль; нельзя в `for`-части
- [ ] Скобки обязательны в некоторых контекстах (условие, comprehensions)

### 19a. Python 3.10+: Union | None, zip(strict=True)

- [ ] `X | Y` вместо `Union[X, Y]`; `X | None` вместо `Optional[X]` (PEP 604)
- [ ] `zip(a, b, strict=True)` — проверка равной длины; `ValueError` иначе (3.10+)
- [ ] `int | str` — union types без `typing` (3.10+)

### 19b. Python 3.11+: ExceptionGroup, except*

- [ ] `ExceptionGroup(msg, [exc1, exc2])` — группа исключений (PEP 654)
- [ ] `except* ValueError:` — частичная обработка; остальные пробрасываются
- [ ] `except* (A, B):` — несколько типов
- [ ] `raise ExceptionGroup(...)` — при параллельном выполнении (TaskGroup)
- [ ] `exceptions` — список исключений в группе; `exc.subgroup(ValueError)`

### 19c. Python 3.11+: Self, Never, assert_never

- [ ] `typing.Self` — возврат self; `def copy(self) -> Self` (PEP 673)
- [ ] `typing.Never` — bottom type; функция никогда не возвращается (PEP 484)
- [ ] `typing.assert_never(x)` — exhaustive matching; `TypeError` если достигнуто
- [ ] Использование с match/case для полного покрытия вариантов

### 19d. Python 3.11+: TypeVarTuple, Unpack, Required, NotRequired

- [ ] `TypeVarTuple` — переменное число типов; `tuple[str, *tuple[int, ...]]`
- [ ] `Unpack[Ts]` — распаковка TypeVarTuple
- [ ] `TypedDict` — `Required[key]`, `NotRequired[key]` (PEP 655)
- [ ] `LiteralString` (PEP 675) — защита от SQL injection; только литералы

### 19e. Python 3.12+: type statement, @override

- [ ] `type Point = tuple[float, float]` — объявление type alias (PEP 695)
- [ ] `@override` — проверка переопределения метода; mypy/pyright (PEP 698)
- [ ] PEP 696: `TypeDefault` — значение по умолчанию для TypeVar
- [ ] PEP 709: comprehension inlining — оптимизация в 3.12

### 19f. Python 3.13+

- [ ] **Free-threaded Python** (экспериментально) — PEP 703; `python -X gil=0`; без GIL
- [ ] `@typing.deprecated` (PEP 702) — пометка устаревших сущностей
- [ ] PEP 719: `python -P` — отключение site-packages для изоляции
- [ ] `importlib.util.PEP723` — inline script metadata
- [ ] Другие нововведения 3.13; следить за What's New

---

## Часть V. Контекстные менеджеры и ресурсы

> **Материалы:** [→ Навигация по Части V](pact/05_kontekstnye_menedzhery_i_resursy/index.md)

### 20. Контекстные менеджеры

- [ ] Протокол: `__enter__`, `__exit__`
- [ ] Обработка исключений в `__exit__`; возврат `True` — подавить исключение
- [ ] `@contextmanager` + `yield`
- [ ] Вложенные `with`
- [ ] `ExitStack` для динамического набора
- [ ] `contextlib.closing(obj)` — вызывает `obj.close()` при выходе
- [ ] `contextlib.chdir(path)` (3.11+) — временная смена директории

### 20a. Асинхронные контекстные менеджеры

- [ ] Протокол: `__aenter__`, `__aexit__`
- [ ] `async with obj:` — вызывает `__aenter__`, `__aexit__`
- [ ] `@asynccontextmanager` — асинхронный вариант `@contextmanager`
- [ ] `asyncio.timeout(seconds)` (3.11+) — async context manager для таймаута
- [ ] `contextlib.asynccontextmanager`

---

## Часть VI. Асинхронность, потоки, мультипроцессинг (углублённо)

> **Материалы:** [→ Навигация по Части VI](pact/06_asinchronnost_potoki_multiprocessing/index.md)

### 21. asyncio — основы

#### 21.1 Основы
- [ ] Событийный цикл (event loop) — однопоточная модель
- [ ] `async def` — корутина; `await` — ожидание awaitable
- [ ] Различие: coroutine vs coroutine function vs Task
- [ ] Корутина не выполняется до `await` или `create_task`
- [ ] `asyncio.run()` — создание loop, запуск главной корутины
- [ ] Event loop: `get_event_loop()`, `new_event_loop()`, `set_event_loop()`

#### 21.2 Примитивы
- [ ] `asyncio.create_task()` — запуск задачи; возвращает Task
- [ ] `asyncio.gather()` — параллельное выполнение; `return_exceptions=True`
- [ ] `asyncio.sleep()` — неблокирующая задержка; отдаёт контроль loop
- [ ] `asyncio.wait_for()` — таймаут; `asyncio.TimeoutError`
- [ ] `asyncio.shield()` — защита от отмены
- [ ] `asyncio.wait()` — wait для множества Task; `FIRST_COMPLETED`, `ALL_COMPLETED`
- [ ] `asyncio.as_completed()` — итератор по завершённым задачам
- [ ] `asyncio.TaskGroup` (Python 3.11+) — structured concurrency

#### 21.3 Синхронизация
- [ ] `asyncio.Lock` — мьютекс; `async with lock`
- [ ] `asyncio.Semaphore` — ограничение параллелизма
- [ ] `asyncio.Queue` — async очередь; `put`, `get`, `join`, `task_done`
- [ ] `asyncio.Event` — событие; `set`, `wait`, `clear`
- [ ] `asyncio.Condition` — условная переменная
- [ ] `asyncio.Barrier` (Python 3.11+) — барьер для синхронизации
- [ ] Взаимоблокировки в async: deadlock при неправильном порядке lock

#### 21.4 Совместимость с синхронным кодом
- [ ] `loop.run_in_executor(executor, func)` — запуск блокирующего кода
- [ ] `asyncio.to_thread(func, *args)` (Python 3.9+) — в ThreadPoolExecutor
- [ ] `loop.run_until_complete()` vs `asyncio.run()` — для встроенного кода
- [ ] Блокирующий код в async — блокирует весь event loop; использовать executor

#### 21.5 Отмена и исключения
- [ ] `task.cancel()` — отмена задачи; `CancelledError`
- [ ] `task.add_done_callback()` — callback при завершении
- [ ] Проброс исключений из Task при `await`
- [ ] `asyncio.CancelledError` — не ловить без re-raise

#### 21.6 Тонкости asyncio
- [ ] Один event loop на поток
- [ ] `nest_asyncio` — вложенные loops (осторожно)
- [ ] `uvloop` — быстрая альтернатива event loop (C-реализация)
- [ ] Debug mode: `PYTHONASYNCIODEBUG=1`
- [ ] `asyncio.run()` закрывает loop; нельзя повторно использовать
- [ ] `asyncio.current_task()` — текущая Task (None вне async контекста)
- [ ] `asyncio.all_tasks()` — множество всех активных Task в loop

#### 21.7 asyncio: потоки (Streams) и subprocess

- [ ] `asyncio.open_connection(host, port)` — TCP-клиент; StreamReader, StreamWriter
- [ ] `asyncio.start_server(callback, host, port)` — TCP-сервер
- [ ] `StreamReader.read(n)`, `readline()`, `readuntil(separator)`
- [ ] `StreamWriter.write()`, `drain()`, `close()`, `wait_closed()`
- [ ] `asyncio.create_subprocess_exec(cmd, *args)` — асинхронный subprocess
- [ ] `asyncio.create_subprocess_shell(cmd)` — shell; осторожно с безопасностью
- [ ] `process.communicate()` — async ожидание завершения
- [ ] `process.returncode`, `process.pid`

### 22. threading — многопоточность

#### 22.1 Основы
- [ ] `threading.Thread(target=func, args=())` — создание потока
- [ ] `thread.start()`, `thread.join()`, `thread.is_alive()`
- [ ] Потоки разделяют память процесса; GIL — один поток выполняет Python-байткод
- [ ] GIL освобождается при I/O (чтение/запись, сеть); CPU-bound — без выигрыша

#### 22.2 Синхронизация потоков
- [ ] `threading.Lock` — мьютекс; `with lock`
- [ ] `threading.RLock` — реентерабельный лок; один поток может захватить несколько раз
- [ ] `threading.Semaphore` — семафор
- [ ] `threading.Event` — событие
- [ ] `threading.Condition` — условная переменная
- [ ] `threading.Barrier` — барьер
- [ ] `threading.local()` — thread-local storage

#### 22.3 Очереди
- [ ] `queue.Queue` — потокобезопасная FIFO очередь
- [ ] `queue.LifoQueue`, `queue.PriorityQueue`
- [ ] `queue.put()`, `queue.get()` — блокирующие; `timeout`, `block=False`
- [ ] `queue.Queue.join()`, `task_done()` — ожидание завершения задач

#### 22.4 Daemon-потоки
- [ ] `thread.daemon = True` — поток завершится с главным
- [ ] Не ждать daemon при `join`; они могут быть прерваны в любой момент

#### 22.5 Когда использовать threading
- [ ] I/O-bound задачи: сеть, диск, БД
- [ ] Параллельные HTTP-запросы, чтение файлов
- [ ] GUI: основной поток — UI, фоновый — вычисления

### 23. multiprocessing — мультипроцессинг

#### 23.1 Основы
- [ ] `multiprocessing.Process(target=func, args=())` — отдельный процесс
- [ ] Каждый процесс — отдельная память; нет GIL между процессами
- [ ] CPU-bound задачи — multiprocessing; полный параллелизм
- [ ] `process.start()`, `process.join()`, `process.terminate()`
- [ ] `multiprocessing.set_start_method('spawn'|'fork'|'forkserver')` — до создания Process

#### 23.2 Обмен данными между процессами
- [ ] `multiprocessing.Queue` — очередь между процессами; pickle-сериализация
- [ ] `multiprocessing.Pipe` — двунаправленный канал
- [ ] `multiprocessing.Value`, `multiprocessing.Array` — shared memory (typecode)
- [ ] `multiprocessing.Manager` — прокси-объекты; dict, list, Namespace
- [ ] Pickle — всё, что передаётся между процессами, должно быть сериализуемо

#### 23.3 Пулы процессов
- [ ] `multiprocessing.Pool(processes=N)` — пул воркеров
- [ ] `pool.map(func, iterable)` — параллельное применение
- [ ] `pool.apply_async()`, `pool.map_async()` — неблокирующие
- [ ] `pool.close()`, `pool.join()` — корректное завершение
- [ ] `pool.imap()`, `pool.imap_unordered()` — ленивая итерация

#### 23.4 Синхронизация процессов
- [ ] `multiprocessing.Lock`, `Semaphore`, `Event`, `Condition`, `Barrier`
- [ ] `multiprocessing.Value` с `lock=True` — атомарный доступ
- [ ] `multiprocessing.Array` — разделяемый массив

#### 23.5 Тонкости multiprocessing
- [ ] `if __name__ == '__main__':` — обязательно при spawn (Windows, macOS)
- [ ] fork vs spawn: fork копирует память; spawn — чистый старт
- [ ] Передача больших данных — дорого; лучше shared memory или файлы
- [ ] Zombie-процессы — `process.join()` или daemon

#### 23.6 multiprocessing.shared_memory (3.8+)

- [ ] `multiprocessing.shared_memory.SharedMemory(name=..., create=True, size=N)`
- [ ] Разделяемая память между процессами; без pickle
- [ ] `shm.buf` — memoryview; `shm.close()`, `shm.unlink()`
- [ ] Именованная память; передача `name` в дочерние процессы
- [ ] `multiprocessing.Manager().Value()` vs shared_memory — когда что

#### 23.7 Pool initializer и maxtasksperchild

- [ ] `Pool(processes=N, initializer=func, initargs=())` — инициализация воркеров
- [ ] `Pool(maxtasksperchild=M)` — перезапуск воркера после M задач; против утечек

### 24. concurrent.futures

- [ ] `ThreadPoolExecutor(max_workers=N)` — пул потоков
- [ ] `ProcessPoolExecutor(max_workers=N)` — пул процессов
- [ ] Единый API: `executor.submit(func, *args)` → Future
- [ ] `future.result(timeout)` — ожидание результата
- [ ] `executor.map(func, *iterables)` — параллельное отображение
- [ ] `concurrent.futures.as_completed(futures)` — итератор по завершённым
- [ ] `executor.shutdown(wait=True)` — корректное завершение
- [ ] Контекстный менеджер: `with ThreadPoolExecutor() as ex:`

### 25. Выбор: asyncio vs threading vs multiprocessing

- [ ] **I/O-bound** (сеть, диск): asyncio или threading; asyncio эффективнее при многих соединениях
- [ ] **CPU-bound** (вычисления): multiprocessing; обход GIL
- [ ] **Смешанная нагрузка**: asyncio + `run_in_executor(ProcessPoolExecutor)` для CPU
- [ ] **Много коротких задач**: ThreadPoolExecutor
- [ ] **Долгие вычисления**: ProcessPoolExecutor
- [ ] **Тысячи одновременных соединений**: asyncio + async-библиотеки

### 26. Гонки, deadlock, livelock

- [ ] Race condition — недетерминированный результат при параллельном доступе
- [ ] Critical section — участок кода, требующий эксклюзивного доступа
- [ ] Deadlock — взаимная блокировка (A ждёт B, B ждёт A)
- [ ] Предотвращение deadlock: фиксированный порядок захвата lock; timeout
- [ ] Livelock — потоки активны, но не прогрессируют
- [ ] Атомарность: `queue.Queue` потокобезопасна; `list` — нет

### 27. contextvars

- [ ] Контекстные переменные — аналог thread-local для async
- [ ] `contextvars.ContextVar(name, default=None)`
- [ ] `var.get()`, `var.set(value)`, `var.reset(token)`
- [ ] `contextvars.copy_context()` — копия контекста; `context.run(coro)`
- [ ] Зачем: передача request_id, user, trace_id в async-цепочке
- [ ] Контекст наследуется при `create_task`; в `run_in_executor` — нет

---

## Часть VII. Модель выполнения и внутренности

> **Материалы:** [→ Навигация по Части VII](pact/07_model_vypolneniya_vnutrennosti/index.md)

### 23. Объектная модель

- [ ] Всё — объект; `id()`, `type()`, `is`
- [ ] Сравнение: `==` vs `is`
- [ ] Hashability: объект должен быть immutable и реализовать `__hash__` и `__eq__`
- [ ] Мелкие целые числа кешируются (-5..256)

### 24. Импорт (import system)

- [ ] `import` vs `from ... import`
- [ ] `sys.path`, `PYTHONPATH`
- [ ] Модули и пакеты (`__init__.py`)
- [ ] Namespace packages (PEP 420)
- [ ] `importlib`, динамический импорт
- [ ] Относительный импорт: `.`, `..`
- [ ] `__all__`

#### 24a. Импорт — углублённо

- [ ] `sys.meta_path` — список MetaPathFinder; вызываются при импорте
- [ ] `sys.path_hooks` — PathEntryFinder для путей
- [ ] `sys.path_importer_cache` — кеш для path hooks
- [ ] `importlib.util.spec_from_file_location()` — загрузка из файла
- [ ] `importlib.util.module_from_spec(spec)` — создание модуля из spec
- [ ] `importlib.import_module(name)` — динамический импорт
- [ ] `importlib.reload(module)` — перезагрузка модуля
- [ ] `runpy.run_module(name)` — запуск модуля как скрипта
- [ ] `pkgutil.iter_modules()` — итерация по модулям пакета
- [ ] `zipimport` — импорт из zip-архивов; `__pycache__`, `.pyc`

#### 24b. Импорт: крайние случаи
- [ ] **Циклические импорты**: A импортирует B, B импортирует A; модуль может быть частично загружен
- [ ] Как работает: `sys.modules` заполняется до завершения загрузки; второй импорт возвращает частичный объект
- [ ] Решения: отложить импорт (внутри функции); реструктурировать; Dependency Injection
- [ ] **`__path__` динамические пакеты**: мутация `__path__` для изменения поиска субмодулей; PEP 420 namespace packages
- [ ] **`pkgutil.extend_path()`** — расширение `__path__` для namespace packages (старый стиль)
- [ ] **`importlib.util.module_from_spec()`** — создание модуля из ModuleSpec; ручная загрузка без import
- [ ] **`__package__` vs `__name__`**: почему `__package__` может быть None; как относительные импорты используют `__package__`
- [ ] **zipimport**: импорт из .zip архивов; как работает `__pycache__` внутри zip

#### 24c. Модульная система: продвинутые механизмы
- [ ] **`__spec__` объект** (ModuleSpec): origin, loader, submodule_search_locations, parent — полная информация об импорте
- [ ] **importlib.abc**: MetaPathFinder, PathEntryFinder, Loader — как реализовать кастомный импорт (из БД, сети)
- [ ] **`__main__` и `-m` флаг**: разница между `python script.py` и `python -m package.module`; как устанавливается `__package__`

### 25. Память и GIL

- [ ] Счётчик ссылок (reference counting)
- [ ] Циклический сборщик мусора (gc)
- [ ] GIL (Global Interpreter Lock) — один поток выполняет Python-байткод
- [ ] Последствия GIL для CPU-bound задач
- [ ] Освобождение GIL в C-расширениях и I/O

### 26. Модуль copy

- [ ] `copy.copy()` — shallow copy
- [ ] `copy.deepcopy()` — глубокое копирование
- [ ] `__copy__`, `__deepcopy__`

### 27. Сериализация: pickle и за его пределами

#### pickle
- [ ] Поддержка типов, ограничения
- [ ] **pickle протоколы (0–5)**: протокол 5 — `pickle.PickleBuffer` для zero-copy передачи между процессами
- [ ] `pickle.HIGHEST_PROTOCOL`; обратная совместимость протоколов
- [ ] **`__reduce__` / `__reduce_ex__`**: кастомная сериализация; объект → вызов функции + аргументы
- [ ] **`__getstate__` / `__setstate__`**: контроль над состоянием; исключение временных/вычисляемых полей
- [ ] Безопасность: не загружать pickle из ненадёжных источников

#### marshal, shelve
- [ ] **marshal** — низкоуровневая сериализация байткода; используется для `.pyc`; нестабилен между версиями Python
- [ ] **shelve** — persistent dict поверх pickle + dbm; транзакционность; блокировки

---

## Часть VIII. Инструменты и экосистема

> **Материалы:** [→ Навигация по Части VIII](pact/08_instrumenty_i_ekosistema/index.md)

### 28. Виртуальные окружения

- [ ] `python -m venv .venv`
- [ ] **PEP 668** — externally managed environment; `pip install` в системный Python блокируется (Linux); обязательно venv/conda
- [ ] Активация: `source .venv/bin/activate` (Unix), `.venv\Scripts\activate` (Windows)
- [ ] `virtualenv` — расширенный venv; `--system-site-packages`
- [ ] `pip`, `pip freeze`, `pip install -r requirements.txt`
- [ ] `pip-tools` — pip-compile для детерминированных зависимостей
- [ ] `venv.EnvBuilder()` — программное создание venv
- [ ] `ensurepip` — установка pip в venv; `--upgrade`
- [ ] `zipapp` — упаковка приложения в .pyz; `python -m zipapp app`

### 29. pyproject.toml

- [ ] [build-system], [project], [tool.*]
- [ ] Зависимости: `dependencies`, `optional-dependencies`
- [ ] Интеграция с setuptools, flit, hatch
- [ ] Версионирование (PEP 440)

### 29a. Упаковка (packaging) — углублённо

#### Форматы и сборка
- [ ] **wheel** (`.whl`) — бинарный формат; быстрая установка; `bdist_wheel`
- [ ] **sdist** (source distribution) — `.tar.gz`, `.zip`; `python setup.py sdist`
- [ ] `python -m build` — современная сборка; wheel + sdist
- [ ] `twine upload dist/*` — загрузка на PyPI; проверка перед загрузкой
- [ ] Editable install: `pip install -e .` — установка в режиме разработки; изменения сразу видны
- [ ] `pip install -e ".[dev]"` — editable с extra-зависимостями

#### Entry points и плагины
- [ ] Entry points в `pyproject.toml`: `[project.scripts]`, `[project.entry-points.group]`
- [ ] `console_scripts` — CLI-команды; `myapp = myapp.cli:main`
- [ ] `importlib.metadata.entry_points()` — получение entry points; `group='plugin'`
- [ ] Плагины: discovery через entry points; расширяемые приложения

#### Конфигурация сборки
- [ ] `setuptools.setup()` — `packages`, `install_requires`, `extras_require`
- [ ] `setuptools.Extension()` — C-расширения; `include_dirs`, `library_dirs`
- [ ] `MANIFEST.in` — включение/исключение файлов в sdist
- [ ] `pyproject.toml` [tool.setuptools] — конфигурация setuptools

#### src layout и py.typed
- [ ] **src layout** — пакет в `src/mypkg/`; `packages=find_packages('src')`, `package_dir={'': 'src'}`; изоляция от тестов; pip install в editable не импортирует из source
- [ ] **py.typed** — маркер PEP 561; `mypkg/py.typed` (пустой файл); пакет поддерживает типизацию; mypy/pyright используют stub'ы из пакета

### 30. Менеджеры зависимостей и окружений

- [ ] Poetry — pyproject.toml, poetry.lock
- [ ] uv — быстрый менеджер (Rust)
- [ ] pipx — установка CLI-инструментов
- [ ] conda / mamba — альтернатива для data science
- [ ] pyenv, asdf — менеджеры версий Python; установка нескольких версий; `pyenv local 3.12`

### 31. Линтеры и форматтеры

- [ ] Ruff — быстрый линтер + форматтер
- [ ] Pylint — глубокий анализ
- [ ] Flake8 — стиль + ошибки
- [ ] Black — «бескомпромиссный» форматтер; `--line-length`
- [ ] isort — сортировка импортов; профили (black, django)

#### 31a. Конфигурация инструментов и pre-commit
- [ ] `ruff.toml` / `pyproject.toml [tool.ruff]` — правила, ignore, fix
- [ ] `mypy.ini` / `pyproject.toml [tool.mypy]` — strict mode, per-module
- [ ] `pyrightconfig.json` — конфигурация pyright
- [ ] `pre-commit` — хуки перед коммитом; `.pre-commit-config.yaml`
- [ ] pre-commit hooks: black, ruff, mypy, pytest; `pre-commit run --all-files`

### 32. Проверка типов

- [ ] mypy — статический анализ типов
- [ ] pyright / Pylance — альтернатива
- [ ] Настройка: strict mode, игнор определённых модулей
- [ ] Типизация в библиотеках: stubs (types-*); **typing_extensions** — backports (Self, ParamSpec и др.) для совместимости со старыми версиями Python

### 33. Тестирование

- [ ] `unittest` — встроенный фреймворк
- [ ] pytest — фикстуры, параметризация, плагины
- [ ] `pytest.fixture`, `conftest.py`
- [ ] `pytest.mark.parametrize`
- [ ] Mocking: `unittest.mock`, `pytest-mock`
- [ ] Покрытие: `coverage`, `pytest-cov`

### 33a. Тестирование — углублённо

- [ ] `doctest` — тесты в docstrings; `doctest.testmod()`; ограничения
- [ ] **Property-based testing**: генерация входных данных по стратегиям; hypothesis shrinking к минимальному контрпримеру
- [ ] `hypothesis.strategies` — `integers()`, `text()`, `lists()`, `dictionaries()`, `composite()`
- [ ] **Mutation testing**: мутация кода для проверки качества тестов; инструменты: mutmut, cosmic-ray
- [ ] **Test doubles taxonomy**: Stub (заглушка ответов) vs Mock (проверка вызовов) vs Spy (запись + проверка) vs Fake (рабочая упрощённая реализация) vs Dummy (placeholder)
- [ ] `unittest.mock` — `spec`, `return_value`, `side_effect`; `patch.object`, `patch.dict`
- [ ] `pytest.fixture` — scope: function, class, module, session
- [ ] `pytest.raises()`, `pytest.warns()` — проверка исключений и предупреждений

### 34. Документация и документационные строки

- [ ] docstring — PEP 257
- [ ] Sphinx — генерация документации; autodoc; mkdocs
- [ ] Type hints в docstring (Google, NumPy стили)

---

## Часть IX. Миграция с Python 2.7

> **Материалы:** [→ Навигация по Части IX](pact/09_migraciya_s_python27/index.md)

### 35. Инструменты миграции

- [ ] `2to3` — автоматическое преобразование
- [ ] Ограничения 2to3, необходимость ручной правки
- [ ] `futurize` (из `future`) — совместимость 2/3

### 36. Библиотеки совместимости

- [ ] `six` — обёртки для 2/3
- [ ] `future` — backports и обёртки
- [ ] Когда отказываться от six и переходить на чистый Py3

### 37. Стратегии миграции

- [ ] **Чеклист Py2→Py3**: exec/print синтаксис; str/bytes; dict.items() vs iteritems(); encoding в open(); тесты на обеих версиях
- [ ] Постепенная миграция модулей
- [ ] Dual-support период
- [ ] Тесты перед и после миграции

---

## Часть X. Объектная модель: магические методы (dunder) — полный справочник

> **Материалы:** [→ Навигация по Части X](pact/10_obektnaya_model_dunder/index.md)

### 38. Создание и уничтожение объекта

- [ ] `__new__(cls, ...)` — создание объекта; вызывается до `__init__`
- [ ] `__init__(self, ...)` — инициализация; не возвращает значение
- [ ] `__del__(self)` — финализатор; вызывается перед сборкой мусора
- [ ] Порядок вызова: `__new__` → `__init__`; при удалении — `__del__`
- [ ] Когда использовать `__new__`: singleton, immutable, наследование от str/int

### 39. Представление (representation)

- [ ] `__repr__(self)` — однозначное представление; `repr(obj)`; для разработчика
- [ ] `__str__(self)` — читаемое представление; `str(obj)`, `print(obj)`
- [ ] `__format__(self, format_spec)` — `format(obj, spec)`; `f'{obj:spec}'`
- [ ] `__bytes__(self)` — `bytes(obj)`
- [ ] Правило: `__repr__` должен быть таким, чтобы `eval(repr(obj)) == obj` (где возможно)

### 40. Сравнение

- [ ] `__eq__(self, other)` — `==`
- [ ] `__ne__(self, other)` — `!=`; по умолчанию `not __eq__`
- [ ] `__lt__(self, other)` — `<`
- [ ] `__le__(self, other)` — `<=`
- [ ] `__gt__(self, other)` — `>`
- [ ] `__ge__(self, other)` — `>=`
- [ ] `functools.total_ordering` — достаточно `__eq__` и одного из `__lt__`/`__le__`/`__gt__`/`__ge__`
- [ ] Возврат `NotImplemented` — передача сравнения другому объекту

### 41. Хеширование (см. также раздел 42)

- [ ] `__hash__(self)` — `hash(obj)`; должен возвращать `int`
- [ ] Контракт: если `a == b`, то `hash(a) == hash(b)`; если определён `__eq__`, нужен `__hash__`
- [ ] Объект с `__eq__` без `__hash__` → `__hash__ = None`; нельзя класть в set/dict
- [ ] Hashable: immutable + стабильный `__hash__`

### 42. Булево значение и проверки

- [ ] `__bool__(self)` — `bool(obj)`; если нет — вызывается `__len__` (0 → False)
- [ ] `__len__(self)` — `len(obj)`; должен возвращать неотрицательный `int`

### 43. Доступ к атрибутам

- [ ] `__getattr__(self, name)` — атрибут не найден; fallback
- [ ] `__getattribute__(self, name)` — любой доступ; осторожно с рекурсией
- [ ] `__setattr__(self, name, value)` — присваивание атрибута
- [ ] `__delattr__(self, name)` — `del obj.attr`
- [ ] Порядок поиска: `__getattribute__` → дескриптор/data → `__dict__` → классов → `__getattr__`

### 44. Дескрипторы (детально)

- [ ] `__get__(self, instance, owner)` — data/non-data дескриптор
- [ ] `__set__(self, instance, value)` — только у data-дескриптора
- [ ] `__delete__(self, instance)` — только у data-дескриптора
- [ ] Приоритет: data-дескриптор > атрибут экземпляра > non-data дескриптор > атрибут класса
- [ ] `property`, `classmethod`, `staticmethod` реализованы через дескрипторы

### 45. Контейнеры и последовательности

- [ ] `__getitem__(self, key)` — `obj[key]`; key может быть int, slice, tuple
- [ ] `__setitem__(self, key, value)` — `obj[key] = value`
- [ ] `__delitem__(self, key)` — `del obj[key]`
- [ ] `__contains__(self, item)` — `item in obj`; иначе перебор через `__iter__`
- [ ] `__iter__(self)` — возвращает итератор; для `for x in obj`
- [ ] `__reversed__(self)` — `reversed(obj)`
- [ ] `__length_hint__(self)` — `operator.length_hint(obj)`; для оптимизации

### 46. Итераторы

- [ ] `__iter__(self)` — итератор возвращает `self`
- [ ] `__next__(self)` — следующий элемент; `StopIteration` для завершения
- [ ] `iter(obj)` вызывает `obj.__iter__()`; fallback — `__getitem__` (если есть)

### 47. Вызов (callable)

- [ ] `__call__(self, *args, **kwargs)` — `obj(*args, **kwargs)`
- [ ] Позволяет использовать объект как функцию

### 48. Контекстный менеджер

- [ ] `__enter__(self)` — вход в `with`; возвращаемое значение — в `as x`
- [ ] `__exit__(self, exc_type, exc_val, exc_tb)` — выход; `True` — подавить исключение

### 49. Числовые протоколы

- [ ] `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`
- [ ] `__radd__`, `__rsub__` и т.д. — правосторонние версии
- [ ] `__iadd__`, `__isub__` и т.д. — in-place: `+=`, `-=`
- [ ] `__neg__`, `__pos__`, `__abs__`, `__invert__`
- [ ] `__int__`, `__float__`, `__complex__`, `__index__` (для срезов)
- [ ] `__round__`, `__trunc__`, `__floor__`, `__ceil__`

### 50. Битовые операции

- [ ] `__and__`, `__or__`, `__xor__`, `__lshift__`, `__rshift__`
- [ ] `__rand__`, `__ror__` и т.д. — правосторонние
- [ ] `__iand__`, `__ior__` и т.д. — in-place

### 51a. Slice и Ellipsis

- [ ] `slice(start, stop, step)` — объект среза; `obj.__getitem__(slice(1,5,2))`
- [ ] `...` (Ellipsis) — `Ellipsis`; используется в numpy, typing
- [ ] `__getitem__(self, key)` — key может быть int, slice, tuple (многомерный индекс)

### 51b. __class_getitem__ (Python 3.9+)

- [ ] `__class_getitem__(cls, item)` — для дженериков: `list[int]`, `dict[str, int]`
- [ ] Позволяет классу поддерживать параметризацию: `C[T]`

### 51c. Полная таблица «оператор → метод» *(справочник; см. Путь обучения)*

| Оператор | Метод | Примечание |
|----------|-------|------------|
| `+` | `__add__`, `__radd__` | |
| `-` | `__sub__`, `__rsub__` | |
| `*` | `__mul__`, `__rmul__` | |
| `/` | `__truediv__`, `__rtruediv__` | |
| `//` | `__floordiv__`, `__rfloordiv__` | |
| `%` | `__mod__`, `__rmod__` | |
| `**` | `__pow__`, `__rpow__` | |
| `&` | `__and__`, `__rand__` | |
| `\|` | `__or__`, `__ror__` | |
| `^` | `__xor__`, `__rxor__` | |
| `<<` | `__lshift__`, `__rlshift__` | |
| `>>` | `__rshift__`, `__rrshift__` | |
| `~` | `__invert__` | унарный |
| `-x` | `__neg__` | унарный |
| `+x` | `__pos__` | унарный |
| `abs(x)` | `__abs__` | |
| `==` | `__eq__` | |
| `!=` | `__ne__` | |
| `<` | `__lt__` | |
| `<=` | `__le__` | |
| `>` | `__gt__` | |
| `>=` | `__ge__` | |
| `in` | `__contains__` | иначе итерация через `__iter__` |
| `obj[key]` | `__getitem__` | key: int, slice, tuple |
| `obj[key]=v` | `__setitem__` | |
| `del obj[key]` | `__delitem__` | |
| `obj()` | `__call__` | |
| `len(obj)` | `__len__` | |
| `bool(obj)` | `__bool__` | иначе `__len__` |
| `iter(obj)` | `__iter__` | |
| `next(obj)` | `__next__` | итератор |
| `repr(obj)` | `__repr__` | |
| `str(obj)` | `__str__` | |
| `hash(obj)` | `__hash__` | |
| `format(obj, spec)` | `__format__` | |
| `with obj:` | `__enter__`, `__exit__` | |

### 51. Специальные атрибуты объекта

- [ ] `__dict__` — словарь атрибутов экземпляра
- [ ] `__class__` — класс объекта
- [ ] `__doc__` — docstring
- [ ] `__module__` — имя модуля
- [ ] `__name__`, `__qualname__` — у классов и функций
- [ ] `__slots__` — фиксированный набор атрибутов; экономия памяти
- [ ] `__weakref__` — слабые ссылки (если нужны)
- [ ] `__annotations__` — аннотации
- [ ] `__bases__`, `__mro__` — у классов

---

## Часть XI. Хеширование: как это работает

> **Материалы:** [→ Навигация по Части XI](pact/11_heshirovanie_kak_eto_rabotaet/index.md)

### 52. Хеш-функция

- [ ] `hash(obj)` — вызывает `obj.__hash__()`
- [ ] Хеш — целое число фиксированного диапазона (зависит от разрядности)
- [ ] В Python: `hash(x) & ((1 << 61) - 1)` используется для индексации в хеш-таблице
- [ ] Цель: равномерное распределение, минимум коллизий

### 53. Контракт hashable

- [ ] Объект hashable, если: `hash(a)` не меняется за время жизни; `a == b` ⇒ `hash(a) == hash(b)`
- [ ] Hashable типы: int, float, str, bytes, tuple (если элементы hashable), frozenset
- [ ] Не hashable: list, dict, set (изменяемые)
- [ ] Почему tuple hashable, а list нет: tuple immutable

### 54. Хеш-таблицы (dict, set)

- [ ] Внутренняя структура: массив бакетов (buckets)
- [ ] Индекс: `hash(key) % len(buckets)` (упрощённо; реально сложнее)
- [ ] Коллизии: цепочки или открытая адресация (в CPython — открытая адресация)
- [ ] Load factor — заполненность; при переполнении — resize

### 55. Коллизии и перехеширование

- [ ] Коллизия — два ключа дают один индекс
- [ ] Стратегии: chaining, open addressing (linear/quadratic probing)
- [ ] Resize — увеличение таблицы при высокой заполненности
- [ ] Порядок вставки сохраняется (CPython 3.7+)

### 56. Слабые ссылки и хеши

- [ ] `weakref` — не увеличивает счётчик ссылок
- [ ] `__weakref__` — слот для weakref
- [ ] Key в WeakKeyDictionary, WeakValueDictionary — должны быть hashable

### 57. Кастомный __hash__

- [ ] При переопределении `__eq__` часто нужно переопределить `__hash__`

#### 57a. Детерминированность и хеш-рандомизация
- [ ] **PYTHONHASHSEED=random** (по умолчанию): рандомизация хешей для защиты от DoS; влияние на порядок в set/dict
- [ ] **PYTHONHASHSEED=0**: детерминированный порядок; для воспроизводимости (тесты, CI)
- [ ] **Порядок итерации**: dict — гарантирован с 3.7 (порядок вставки); set — нет; зависит от хеша и истории вставок
- [ ] **Порядок **kwargs**: порядок ключей сохраняется (3.6+); влияние на сигнатуры функций; `inspect.signature` отражает порядок

- [ ] Или установить `__hash__ = None` — объект не hashable
- [ ] Хорошая практика: хешировать те же поля, что участвуют в `__eq__`

---

## Часть XII. ООП углублённо

> **Материалы:** [→ Навигация по Части XII](pact/12_oop_uglublenno/index.md)

### 58. Наследование

- [ ] Одиночное и множественное наследование
- [ ] Diamond problem и MRO
- [ ] `super()` — кооперативное наследование
- [ ] Порядок вызовов при `super().__init__()`

### 59. MRO (Method Resolution Order)

- [ ] C3 linearization — алгоритм вычисления порядка
- [ ] `ClassName.__mro__` — кортеж классов
- [ ] `ClassName.mro()` — метод
- [ ] Правила: локальный приоритет, monotonicity
- [ ] Когда порядок может быть неочевидным при множественном наследовании

### 60. Композиция vs наследование

- [ ] «Favor composition over inheritance»
- [ ] Композиция — объект содержит другой объект
- [ ] Агрегация — слабая связь; композиция — сильная (жизненный цикл)
- [ ] Mixin — класс для добавления поведения без иерархии

### 61. Абстрактные классы

- [ ] `abc.ABC` — базовый абстрактный класс
- [ ] `@abstractmethod` — метод должен быть переопределён
- [ ] Нельзя инстанциировать класс с непереопределёнными abstract-методами
- [ ] `abc.abstractclassmethod`, `abc.abstractstaticmethod`, `abc.abstractproperty`

### 62. Протоколы и утиная типизация

- [ ] «If it walks like a duck…» — типизация по поведению
- [ ] `typing.Protocol` — structural subtyping
- [ ] `runtime_checkable` — проверка на isinstance
- [ ] Протоколы: Iterable, Sequence, Mapping, Sized, Container и др.

### 63. SOLID и принципы ООП

- [ ] **S**ingle Responsibility — один класс, одна ответственность
- [ ] **O**pen/Closed — открыт для расширения, закрыт для изменения
- [ ] **L**iskov Substitution — подтипы заменяемы базовым типом
- [ ] **I**nterface Segregation — много маленьких интерфейсов лучше одного большого
- [ ] **D**ependency Inversion — зависимость от абстракций

### 64. Инкапсуляция и сокрытие

- [ ] Один underscore `_attr` — «приватный» по соглашению
- [ ] Name mangling: `__attr` → `_ClassName__attr`; не «настоящая» приватность
- [ ] `property` для контролируемого доступа

### 65. Метаклассы (углублённо)

- [ ] `type(name, bases, dict)` — создание класса
- [ ] Метакласс — класс класса; `__new__`, `__init__`, `__call__` метакласса
- [ ] Порядок: метакласс создаёт класс, класс создаёт экземпляр
- [ ] Использование: валидация, автоРегистрация, ORM, API-генерация
- [ ] `__init_subclass__` — альтернатива метаклассам (Python 3.6+)

### 65a. Все вариации связей в ООП

#### Композиция (Composition)
- [ ] «Содержит» — объект владеет другим; жизненный цикл связан
- [ ] Внутренний объект создаётся в конструкторе; уничтожается с владельцем
- [ ] Пример: `Engine` внутри `Car`; без машины двигатель не существует
- [ ] Реализация: объект создаётся в `__init__`; хранится как атрибут

#### Агрегация (Aggregation)
- [ ] «Имеет ссылку» — слабая связь; объект может существовать отдельно
- [ ] Внутренний объект передаётся извне; не уничтожается при удалении контейнера
- [ ] Пример: `Department` содержит `Employee`; сотрудник может сменить отдел
- [ ] Реализация: объект передаётся в конструктор; хранится ссылка

#### Ассоциация (Association)
- [ ] Общая связь между классами; не владение
- [ ] Unidirectional: один знает о другом; bidirectional: оба знают друг о друге
- [ ] Пример: `Student` — `Course`; многие ко многим
- [ ] Реализация: ссылки/списки ссылок; не создание в конструкторе

#### Наследование (Inheritance)
- [ ] «Является» — иерархия типов
- [ ] Single, multiple inheritance; diamond problem, MRO
- [ ] `super()` — кооперативное наследование
- [ ] Composition over inheritance — когда предпочтительнее композиция

#### Делегирование (Delegation)
- [ ] Передача вызова другому объекту; «вместо нас это делает другой»
- [ ] Реализация: метод вызывает метод делегата
- [ ] Пример: `ListProxy` делегирует методы реальному списку

#### Миксин (Mixin)
- [ ] Класс для добавления поведения; не самостоятельная сущность
- [ ] Множественное наследование; миксин обычно без состояния или с минимальным
- [ ] Порядок в MRO: миксин после базового класса
- [ ] Пример: `JSONMixin`, `LoggingMixin`

#### Трейт (Trait)
- [ ] Похож на миксин; набор методов без состояния
- [ ] В Python — миксин; в других языках (Rust, Scala) — отдельная сущность
- [ ] Отличие от миксина: trait — строго поведение, без наследования иерархии

#### Интерфейс (Interface)
- [ ] Контракт: какие методы должен реализовать класс
- [ ] В Python: `abc.ABC` + `@abstractmethod`; `typing.Protocol` — structural
- [ ] Protocol — утиная типизация; проверка по структуре, не по наследованию
- [ ] `runtime_checkable` — проверка `isinstance` для Protocol

#### Абстрактный класс (Abstract Base Class)
- [ ] `abc.ABC` — нельзя инстанциировать без реализации абстрактных методов
- [ ] `@abstractmethod` — метод должен быть переопределён
- [ ] `@abstractclassmethod`, `@abstractstaticmethod`, `@abstractproperty`

#### Параметрический полиморфизм
- [ ] Дженерики: `Generic[T]`, `TypeVar`
- [ ] Один код для разных типов; `list[int]`, `dict[str, int]`
- [ ] `typing.Protocol` — structural subtyping; не nominal (наследование)

#### Ad-hoc полиморфизм
- [ ] Перегрузка операторов: `__add__`, `__radd__` — разные типы
- [ ] `functools.singledispatch` — перегрузка по типу первого аргумента

#### Dependency Injection
- [ ] Зависимости передаются извне; не создаются внутри
- [ ] Constructor injection — в конструктор; setter injection — через сеттер
- [ ] Упрощает тестирование; inversion of control

### 65b. Дополнительные техники ООП

- [ ] **Object Pool** — переиспользование объектов; пул соединений, пул потоков
- [ ] **Flyweight** — разделение общего состояния; экономия памяти
- [ ] **Proxy** — заместитель объекта; lazy loading, контроль доступа
- [ ] **Decorator (структурный)** — обёртка для добавления поведения
- [ ] **Adapter** — адаптация интерфейса; wrapping чужого API
- [ ] **Facade** — упрощённый интерфейс к сложной подсистеме
- [ ] **Bridge** — разделение абстракции и реализации
- [ ] **Composite** — древовидная структура; один интерфейс для узлов и листьев

---

## Часть XIII. Паттерны проектирования

> **Материалы:** [→ Навигация по Части XIII](pact/13_patterny_proektirovaniya/index.md)

### 66. Создающие (Creational)

- [ ] **Singleton** — один экземпляр; реализация через `__new__`, модуль, metaclass
- [ ] **Factory Method** — фабричный метод в классе
- [ ] **Abstract Factory** — семейство связанных фабрик
- [ ] **Builder** — пошаговое построение сложного объекта
- [ ] **Prototype** — клонирование через `copy.copy`/`copy.deepcopy`

### 67. Структурные (Structural)

- [ ] **Adapter** — адаптер интерфейса
- [ ] **Bridge** — разделение абстракции и реализации
- [ ] **Composite** — древовидная структура объектов
- [ ] **Decorator** — обёртка для добавления поведения (функциональные декораторы)
- [ ] **Facade** — упрощённый интерфейс к подсистеме
- [ ] **Flyweight** — разделение общего состояния
- [ ] **Proxy** — заместитель объекта (ленивая загрузка, контроль доступа)

### 68. Поведенческие (Behavioral)

- [ ] **Chain of Responsibility** — цепочка обработчиков
- [ ] **Command** — инкапсуляция запроса как объекта
- [ ] **Iterator** — протокол итератора в Python
- [ ] **Mediator** — посредник между объектами
- [ ] **Memento** — сохранение и восстановление состояния
- [ ] **Observer** — уведомления (events, callbacks)
- [ ] **State** — смена поведения при смене состояния
- [ ] **Strategy** — взаимозаменяемые алгоритмы
- [ ] **Template Method** — шаблонный метод
- [ ] **Visitor** — операции над иерархией классов

### 69. Pythonic-паттерны

- [ ] Context manager — `with`
- [ ] `operator` — модуль для операторов: `operator.add`, `operator.itemgetter`, `operator.attrgetter`, `operator.methodcaller('meth', arg)`
- [ ] Iterator/Generator — ленивые вычисления
- [ ] Decorator — AOP, кеширование, валидация
- [ ] Descriptor — property, lazy attributes
- [ ] Monkey patching — осторожно
- [ ] EAFP vs LBYL — «Easier to Ask Forgiveness than Permission»

---

## Часть XIV. Алгоритмы и структуры данных

> **Материалы:** [→ Навигация по Части XIV](pact/14_algoritmy_i_struktury_dannyh/index.md)

### 70. Асимптотический анализ (O-нотация)

- [ ] O(1) — константа
- [ ] O(log n) — логарифм (бинарный поиск)
- [ ] O(n) — линейно
- [ ] O(n log n) — сортировка слиянием, quicksort (средний случай)
- [ ] O(n²) — квадратично (пузырёк, вложенные циклы)
- [ ] O(2ⁿ) — экспонента (наивная рекурсия Fibonacci)
- [ ] O(n!) — факториал (полный перебор перестановок)
- [ ] Big-O, Big-Ω, Big-Θ
- [ ] Амортизированный анализ (например, append в list)

### 71. Массивы и списки

- [ ] Динамический массив — list в Python
- [ ] Амортизированная O(1) для append
- [ ] O(n) для insert(0) — сдвиг элементов
- [ ] Срезы — копирование O(k), где k — размер среза

### 72. Стеки и очереди

- [ ] Стек — LIFO; list с append/pop
- [ ] `collections.deque` — двусторонняя очередь; O(1) append/pop с обоих концов
- [ ] `queue.Queue` — потокобезопасная очередь
- [ ] `queue.LifoQueue`, `queue.PriorityQueue`

### 73. Связные списки

- [ ] Односвязный список — Node(value, next)
- [ ] Двусвязный список — Node(prev, value, next)
- [ ] Сравнение с массивом: вставка/удаление в середине O(1) при наличии указателя
- [ ] Отсутствует в stdlib; реализация вручную при необходимости

### 74. Кучи (heaps)

- [ ] Binary heap — полное бинарное дерево; родитель ≤ потомки (min-heap)
- [ ] `heapq` — min-heap на list
- [ ] `heapq.heappush`, `heapq.heappop`, `heapq.heapify`
- [ ] Использование: priority queue, merge k sorted lists, top-k
- [ ] `heapq.nlargest(n, iterable)`, `heapq.nsmallest(n, iterable)` — top-k без полной сортировки; эффективнее `sorted()[:n]` для больших коллекций
- [ ] Сложность: push O(log n), pop O(log n)

### 75. Деревья

- [ ] Бинарное дерево — узел с левым и правым потомком
- [ ] Бинарное дерево поиска (BST) — left < root < right
- [ ] Обход: inorder, preorder, postorder
- [ ] AVL, Red-Black — сбалансированные деревья
- [ ] B-дерево — для дисков, баз данных
- [ ] `sortedcontainers.SortedDict` — реализация на дереве (вне stdlib)

### 76. Хеш-таблицы (повтор и углубление)

- [ ] dict, set — реализация через хеш-таблицу
- [ ] Среднее O(1) для get/set/delete
- [ ] Худший случай O(n) при многих коллизиях

### 77. Графы

- [ ] Представление: список смежности, матрица смежности
- [ ] BFS (поиск в ширину) — очередь
- [ ] DFS (поиск в глубину) — стек/рекурсия
- [ ] Топологическая сортировка
- [ ] Алгоритмы: Dijkstra, Bellman-Ford (кратчайший путь)
- [ ] Минимальное остовное дерево: Prim, Kruskal
- [ ] Union-Find (Disjoint Set Union) — для Kruskal

### 78. Сортировки

- [ ] Bubble sort — O(n²)
- [ ] Selection sort — O(n²)
- [ ] Insertion sort — O(n²); хорош для почти отсортированных
- [ ] Merge sort — O(n log n), стабильная, дополнительная память O(n)
- [ ] Quick sort — O(n log n) в среднем, O(n²) в худшем; in-place
- [ ] Timsort — гибрид merge + insertion; используется в Python (`list.sort`, `sorted`)
- [ ] Counting sort, Radix sort — O(n+k) при ограниченном диапазоне

### 79. Поиск

- [ ] Линейный поиск — O(n)
- [ ] Бинарный поиск — O(log n) для отсортированного массива
- [ ] `bisect` — bisect_left, bisect_right, insort_left, insort_right
- [ ] Поиск в BST — O(log n) в среднем

### 80. Рекурсия и динамическое программирование

- [ ] Рекурсия — базовый случай, рекуррентное соотношение
- [ ] Мемоизация — кеширование результатов (lru_cache)
- [ ] Динамическое программирование — таблица снизу вверх
- [ ] Примеры: Fibonacci, рюкзак, edit distance (Levenshtein), LCS

### 81. Жадные алгоритмы

- [ ] Локально оптимальный выбор
- [ ] Примеры: Huffman, задача о выборе активностей, покрытие множества

### 82. Разделяй и властвуй

- [ ] Разбиение на подзадачи, рекурсия, комбинирование
- [ ] Merge sort, Quick sort, бинарный поиск

### 83. Строковые алгоритмы

- [ ] Поиск подстроки: наивный O(n·m), KMP, Boyer-Moore
- [ ] Регулярные выражения — `re`; NFA, backtracking, RE2
- [ ] Edit distance (Levenshtein)
- [ ] Префиксное дерево (trie)

### 84. Числовые алгоритмы

- [ ] GCD — алгоритм Евклида
- [ ] Быстрое возведение в степень (бинарное)
- [ ] Простые числа: решето Эратосфена, проверка на простоту
- [ ] Комбинаторика: факториал, перестановки, сочетания

---

## Часть XV. Внутренности Python: как всё заполняется и работает

> **Материалы:** [→ Навигация по Части XV](pact/15_vnutrennosti_python_kak_vse_zapolnyaetsya_i_rabotaet/index.md)

### 85. Поиск атрибутов

- [ ] Цепочка: экземпляр → класс → базовые классы (MRO) → метакласс
- [ ] Дескрипторы перехватываются на уровне класса
- [ ] `__getattribute__` перехватывает всё
- [ ] `object.__getattribute__` — базовая реализация

### 86. __dict__ и __slots__

- [ ] Обычный объект: атрибуты хранятся в `__dict__` (словарь)
- [ ] `__slots__` — фиксированный список имён; `__dict__` не создаётся
- [ ] Экономия памяти; нельзя добавлять произвольные атрибуты
- [ ] Наследование: `__slots__` у потомка не наследует слоты родителя автоматически

### 87. Жизненный цикл объекта

- [ ] Создание: `__new__` → выделение памяти → `__init__`
- [ ] Использование: счётчик ссылок увеличивается/уменьшается
- [ ] Удаление: счётчик = 0 → `__del__` (если есть) → освобождение памяти
- [ ] Циклы: циклический сборщик мусора (gc) обнаруживает и собирает

### 88. Байткод и выполнение

- [ ] `dis.dis(func)` — дизассемблирование байткода
- [ ] Байткод выполняется в CPython виртуальной машиной
- [ ] LOAD_FAST, LOAD_GLOBAL, CALL_FUNCTION и др.

### 89. Модуль inspect

- [ ] `inspect.signature` — сигнатура функции
- [ ] `inspect.getsource` — исходный код
- [ ] `inspect.getmro` — MRO класса
- [ ] `inspect.isfunction`, `inspect.isclass` и др.
- [ ] `inspect.getframeinfo()`, `inspect.currentframe()`, `inspect.stack()`
- [ ] `inspect.Parameter` — kind: POSITIONAL_ONLY, KEYWORD_ONLY, VAR_POSITIONAL, VAR_KEYWORD

#### 89. Интроспекция и рефлексия: глубокий уровень
- [ ] **`__annotations__`**: строковые аннотации; `from __future__ import annotations` — все аннотации становятся строками (3.7+)
- [ ] **`typing.get_type_hints()`**: разрешает строковые аннотации через eval() в правильном namespace
- [ ] **inspect.signature() vs inspect.getfullargspec()**: signature — современный API; getfullargspec — legacy; обработка *args/**kwargs
- [ ] **Parameter.kind**: POSITIONAL_ONLY, POSITIONAL_OR_KEYWORD, VAR_POSITIONAL, KEYWORD_ONLY, VAR_KEYWORD
- [ ] **`__wrapped__` и декораторы**: `functools.wraps` устанавливает `__wrapped__`; `inspect.unwrap()` — доступ к оригинальной функции
- [ ] **`sys._getframe(depth)`**: depth=0 — текущий фрейм; depth=1 — вызывающий; риски (производительность, отладка); кеширование фреймов

### 89a. Метапрограммирование: AST, байткод, eval/exec

#### AST-трансформации
- [ ] `ast.parse(source)` — парсинг в AST; `ast.dump(node)`
- [ ] `ast.NodeVisitor`, `ast.NodeTransformer` — обход и преобразование AST
- [ ] Как работают декораторы/макросы на уровне дерева; применение в Ruff, autoflake
- [ ] `ast.fix_missing_locations()`, `ast.copy_location()` — сохранение позиций при трансформации

#### Bytecode manipulation
- [ ] `dis.dis(func)` — дизассемблирование; `dis.show_code()`; LOAD_FAST, CALL_FUNCTION и др.
- [ ] Модификация байткода в рантайме: `types.CodeType`; инструменты: bytecode, codetransformer
- [ ] `compile(source, filename, mode, flags=0)` — флаги влияют на поведение

#### eval/exec и compile() флаги
- [ ] **`ast.literal_eval`** — безопаснее eval; только литералы; почему eval/exec опасны (injection, произвольный код)
- [ ] **`compile()` флаги**: `PyCF_ALLOW_TOP_LEVEL_AWAIT` (3.8+) — await на верхнем уровне; `PyCF_DONT_IMPLY_DEDENT` — не добавлять dedent
- [ ] `compile(mode='eval')` vs `mode='exec')` vs `mode='single'`; влияние на результат

### 89a1. Полный цикл компиляции в CPython

- [ ] **Исходный код** → **Токены** (lexer): `tokenize.generate_tokens()`; токены (NAME, NUMBER, OP, NL…)
- [ ] **Токены** → **AST** (parser): `ast.parse()`; дерево узлов (Module, FunctionDef, Assign…)
- [ ] **AST** → **Байткод** (compiler): `compile()`; Python/compile.c; генерация opcodes
- [ ] **Байткод** → **Выполнение** (VM): eval loop; интерпретация opcodes; стек, локальные переменные
- [ ] **Оптимизации 3.11+**: specialized adaptive interpreter; inline caching; quickening
- [ ] **Оптимизации 3.12+**: PEP 709 — comprehension inlining; улучшения eval loop
- [ ] `sys.settrace()` — отладка на уровне opcodes; profile/trace
- [ ] `.pyc` файлы — кеширование байткода; magic number; timestamp/hash

### 89a2. Структура объектов в CPython

- [ ] **PyObject** — базовый тип; каждый объект начинается с PyObject_HEAD
- [ ] **PyObject_HEAD**: `ob_refcnt` (счётчик ссылок), `ob_type` (указатель на PyTypeObject)
- [ ] **PyTypeObject** — структура типа; tp_name, tp_hash, tp_call, tp_getattr; слоты (slots)
- [ ] Типы — тоже объекты; `type` — метатип PyType_Type
- [ ] **PyVarObject** — объекты переменной длины; PyObject_HEAD + ob_size (list, tuple, str)
- [ ] Реализация типов: `PyLong_Type`, `PyList_Type`, `PyDict_Type`; C-структуры в Objects/
- [ ] `ob_type` → диспетчеризация методов; виртуальная таблица в PyTypeObject
- [ ] Заголовок объекта — накладные расходы; `sys.getsizeof()` — только Python-объект
- [ ] **Компактный dict** (PEP 412): раздельные массивы — индексы (sparse) + записи (dense); экономия памяти + порядок без доп. структур
- [ ] **Overallocation в list**: формула роста [0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...]; амортизированная O(1) для append
- [ ] **String interning**: автоматический (identifiers, small ascii) vs ручной `sys.intern()`; когда `a is b` для строк
- [ ] **Small integer cache**: диапазон -5..256; кеширование на уровне интерпретатора; `sys.intern()` не для чисел
- [ ] **PyVarObject**: базовая структура для объектов переменной длины (list, tuple, str); поле `ob_size`

### 89a2a. Code и frame objects: как устроены функции «под капотом»

- [ ] **Code object** — `func.__code__`; хранит байткод, константы, имена переменных
- [ ] `types.CodeType` — создание code object; co_code, co_consts, co_names, co_varnames, co_freevars
- [ ] **Frame object** — кадр выполнения; один frame на вызов функции; `frame.f_code`, `frame.f_locals`
- [ ] `inspect.currentframe()`, `sys._getframe()` — доступ к текущему frame
- [ ] Связь: функция → code object (статический) → frame object (при вызове)
- [ ] `__code__.co_argcount`, `co_kwonlyargcount`, `co_posonlyargcount` — сигнатура

### 89a3. Эволюция GIL

- [ ] **Классический GIL** (до 3.12): один lock на весь интерпретатор; один поток выполняет байткод
- [ ] GIL освобождается при I/O (read, write, socket); C-расширения могут освобождать (Py_BEGIN_ALLOW_THREADS)
- [ ] **Per-interpreter GIL** (PEP 684, 3.12): отдельный GIL на суб-интерпретатор; `Py_NewInterpreterFromConfig()`
- [ ] Суб-интерпретаторы — изоляция; отдельные модули, объекты; нет shared state
- [ ] **Free-threaded Python** (PEP 703, 3.13): экспериментальный build без GIL; `python -X gil=0`
- [ ] Free-threaded: тонкая блокировка на уровне объектов; совместимость с C-расширениями
- [ ] Путь к multithreading без GIL; экспериментально; следить за PEP 703
- [ ] Когда что использовать: классический — совместимость; per-interpreter — изоляция; free-threaded — будущее

### 89b. Сеть: select, selectors, socket

- [ ] `select.select(rlist, wlist, xlist, timeout)` — I/O multiplexing; Unix
- [ ] `select.poll()` — poll; более эффективен при многих fd
- [ ] `selectors.DefaultSelector()` — высокоуровневый выбор селектора
- [ ] `selectors.SelectSelector`, `EpollSelector` (Linux), `KqueueSelector` (BSD)
- [ ] `socket.socket()` — TCP/UDP; `create_connection()`, `gethostbyname()`, `getaddrinfo()`
- [ ] `ssl.wrap_socket()`, `ssl.create_default_context()` — TLS

### 89c. queue.Queue — тонкости

- [ ] `queue.Empty`, `queue.Full` — исключения при `get(block=False)`, `put(block=False)`
- [ ] `Queue.get(timeout=N)` — блокировка с таймаутом
- [ ] `Queue.task_done()` — после обработки; для `join()`
- [ ] `Queue.qsize()` — приблизительный размер; не надёжен для синхронизации
- [ ] `Queue.maxsize` — 0 = бесконечная очередь
- [ ] `PriorityQueue` — приоритет: кортеж `(priority, item)`; меньше = выше приоритет

### 89d. threading.Timer

- [ ] `threading.Timer(interval, function, args=[])` — вызов через N секунд
- [ ] `timer.start()`, `timer.cancel()` — отмена до выполнения
- [ ] Timer — отдельный поток; альтернатива: `threading.Event.wait(timeout)` + флаг

### 89e. types — SimpleNamespace, MappingProxyType

- [ ] `types.SimpleNamespace(**kwargs)` — объект с атрибутами; как пустой класс
- [ ] `types.MappingProxyType(dict)` — read-only view словаря; изменения отражаются
- [ ] `types.CoroutineType`, `types.GeneratorType`, `types.AsyncGeneratorType`
- [ ] `types.FunctionType`, `types.MethodType`, `types.BuiltinFunctionType`
- [ ] `types.ModuleType` — создание модуля программно
- [ ] `types.UnionType` (3.10+) — тип для `X | Y`

### 89f0. Внутренности интерпретатора (углублённо)

- [ ] `__build_class__` — встроенная функция; вызывается при `class C:`; можно перехватить
- [ ] `metaclass.__prepare__(name, bases)` — возвращает namespace; вызывается до `__new__`
- [ ] `__prepare__` — можно вернуть OrderedDict для сохранения порядка атрибутов
- [ ] Порядок: `__prepare__` → `__new__` → `__init__` метакласса → `__new__` → `__init__` класса
- [ ] `super()` — использует `__class__` (в замыкании) и MRO; неявная передача self/cls
- [ ] `super().__init__()` — кооперативный вызов; поиск в MRO после текущего класса
- [ ] Cell variables — переменные в замыкании; `func.__closure__`; `cell.cell_contents`
- [ ] Free variables — имена из enclosing scope; `func.__code__.co_freevars`

### 89f. argparse — subparsers, mutually_exclusive_group

- [ ] `parser.add_subparsers(dest='cmd')` — подкоманды; `add_parser('name')`
- [ ] `group = parser.add_mutually_exclusive_group()` — взаимоисключающие опции
- [ ] `parser.add_argument('--foo', nargs='+', choices=[...], action='store_true')`
- [ ] `action='store_const'`, `action='append'`, `action='count'`
- [ ] `type=func` — преобразование аргумента; `default`, `required`
- [ ] `metavar`, `help`, `dest`; `argparse.Namespace`

### 89g. logging — dictConfig, LoggerAdapter, Filter

- [ ] `logging.config.dictConfig(config)` — конфигурация из словаря
- [ ] Handlers: `StreamHandler`, `FileHandler`, `RotatingFileHandler`, `TimedRotatingFileHandler`
- [ ] Formatters: `%(name)s`, `%(levelname)s`, `%(message)s`, `%(asctime)s`
- [ ] `logging.NullHandler()` — подавление логов
- [ ] `LoggerAdapter(logger, extra)` — контекст в логах
- [ ] `logging.Filter` — фильтрация записей

---

## Часть XVI. Тонкости и «подводные камни»

> **Материалы:** [→ Навигация по Части XVI](pact/16_tonkosti_i_podvodnye_kamni/index.md)

### 88. Известные ловушки (расширенные)

- [ ] Mutable default argument: `def f(a=[])` — один список на все вызовы
- [ ] Late binding в замыканиях: цикл и `lambda` — захват по ссылке
- [ ] Изменение списка во время итерации — нестабильное поведение
- [ ] `is` для сравнения с None — правильно; с числами/строками — опасно (интернирование)
- [ ] Цепочка `or`: `x or []` — проблема для 0, '', False
- [ ] Цепочка `and`: short-circuit evaluation
- [ ] Мелкие целые числа (-5..256) — один объект в памяти; `a is b` может быть True
- [ ] Строки: интернирование; `'hello' is 'hello'` — implementation-defined
- [ ] `del` — удаляет ссылку; объект освобождается, когда ссылок 0
- [ ] `assert` — отключен при `python -O`; не для валидации ввода
- [ ] `__debug__` — `False` при `-O`; оптимизации при `if __debug__`
- [ ] Рекурсия: `sys.setrecursionlimit()`; stack overflow; tail recursion не оптимизируется
- [ ] Классовая vs экземплярная переменная: изменение через класс влияет на все экземпляры

### 89. Производительность и профилирование

- [ ] Профилирование: `cProfile`, `profile` — статистика вызовов
- [ ] `pstats.Stats` — сортировка, фильтрация результатов
- [ ] `timeit.Timer()` — микробенчмарки; `repeat()`, `autorange()`
- [ ] `py-spy` — sampling profiler; без модификации кода; production
- [ ] `tracemalloc` — профилирование памяти; `start()`, `get_traced_memory()`, `take_snapshot()`
- [ ] `memory_profiler`, `memray`, `scalene` — инструменты памяти
- [ ] `faulthandler` — traceback при segfault; отладка C-расширений
- [ ] Избегание преждевременной оптимизации
- [ ] Когда использовать PyPy, Cython, Numba
- [ ] Список vs кортеж — кортеж быстрее и легче
- [ ] Генераторы vs списки — память vs скорость доступа

### 89a. Отладка (debugging)

- [ ] `pdb` — пошаговая отладка; `breakpoint()`, `import pdb; pdb.set_trace()`
- [ ] `pdb` команды: `n`, `s`, `c`, `l`, `p`, `pp`, `w`, `u`, `d`
- [ ] `PYTHONBREAKPOINT=0` — отключить `breakpoint()`; `ipdb.set_trace`
- [ ] `sys.settrace()`, `sys.setprofile()` — trace/profile хуки
- [ ] `debugpy` — отладка в VS Code; attach к процессу
- [ ] `trace` — трассировка выполнения; coverage-like

### 90. Безопасность и инструменты проверки

- [ ] SQL injection — параметризованные запросы
- [ ] pickle — не загружать из ненадёжных источников
- [ ] `eval`, `exec` — риски; альтернативы (ast.literal_eval)
- [ ] `secrets` вместо `random` для токенов/паролей
- [ ] Зависимости: проверка уязвимостей (pip-audit, safety)
- [ ] **Bandit** — статический анализ безопасности; SQL injection, eval, pickle
- [ ] **safety** — проверка CVE в зависимостях
- [ ] **pip-audit** — аудит зависимостей
- [ ] **semgrep** — статический анализ; кастомные правила
- [ ] **LiteralsString** (3.11+) — защита от SQL injection на уровне типов
- [ ] `ast.literal_eval` — безопасная альтернатива eval для литералов

#### 90a. Безопасность: системный уровень
- [ ] **`sys.audit()` / `sys.addaudithook()`** (PEP 578): перехват опасных операций — `os.open()`, `subprocess.Popen()`, `ctypes`; для песочниц
- [ ] **hmac vs hashlib**: hmac — криптографическая подпись сообщений; защита от подмены данных; `hmac.new(key, msg, digestmod)`
- [ ] **secrets vs random**: secrets — CSPRNG (Cryptographically Secure PRNG); для токенов/паролей; `random` — не для криптографии

### 90a. ReDoS и безопасность регулярных выражений

- [ ] **ReDoS (Regular expression Denial of Service)** — катастрофический backtracking
- [ ] Паттерны типа `(a+)+`, `(a|a)*` — экспоненциальное время на злонамеренном вводе
- [ ] Использование `re.match()` с user input — риски; ограничение длины
- [ ] Модуль `regex` с `timeout` — защита от ReDoS (сторонняя библиотека)
- [ ] Альтернативы: валидация без regex; `re.compile()` + ограничение ввода

### 90b. Дополнительные тонкости Python

- [ ] **Классовая vs экземплярная переменная**: присваивание через `obj.attr` создаёт экземплярный атрибут; изменение через `Cls.attr` влияет на все экземпляры
- [ ] **Bound vs unbound метод**: метод класса; при вызове через экземпляр — bound (self подставляется)
- [ ] **Сравнение цепочки**: `a < b < c` эквивалентно `a < b and b < c`; `b` вычисляется один раз
- [ ] **Truthiness**: пустая коллекция — False; непустая — True; `None` — False; числа 0 — False
- [ ] **Числовая иерархия**: `numbers.Number` → `numbers.Complex` → `numbers.Real` → `numbers.Rational` → `numbers.Integral`
- [ ] **Оператор `in`**: вызывает `__contains__` или итерирует через `__iter__` с поиском
- [ ] **Вызов `obj()`**: вызывает `obj.__call__()`
- [ ] **Индексация `obj[key]`**: вызывает `obj.__getitem__(key)`; key может быть slice, tuple (многомерный)
- [ ] **Оператор `with`**: вызывает `__enter__`, затем блок, затем `__exit__` (даже при исключении)
- [ ] **Оператор `for`**: вызывает `iter(obj)` → `__iter__` или `__getitem__` (fallback), затем `next()`
- [ ] **Comprehensions**: list `[]`, dict `{}`, set `{}`, generator `()`; scope — вложенная функция
- [ ] **`else` в цикле**: выполняется, если цикл завершился без `break`
- [ ] **`else` в try**: выполняется, если не было исключения; `finally` — всегда

---

## Часть XVII. Память: аллокация, сборка мусора, использование объектов

> **Материалы:** [→ Навигация по Части XVII](pact/17_pamyat_allokaciya_sborka_musora_ispolzovanie_obektov/index.md)

### 91. Счётчик ссылок (reference counting)

- [ ] Каждый объект имеет `ob_refcnt` — число ссылок
- [ ] `sys.getrefcount(obj)` — сколько ссылок (включая аргумент функции)
- [ ] Присваивание, передача в функцию — увеличение счётчика
- [ ] Выход из области видимости, `del` — уменьшение
- [ ] Счётчик = 0 → объект освобождается немедленно
- [ ] Циклы — счётчик не обнуляется; нужен gc

### 92. Циклический сборщик мусора (gc)

- [ ] Модуль `gc` — управление сборщиком
- [ ] Обнаружение циклов: unreachable объекты
- [ ] Generations: 0, 1, 2 — объекты разного возраста
- [ ] `gc.collect()` — принудительная сборка
- [ ] `gc.disable()`, `gc.enable()` — отключение/включение
- [ ] `gc.get_objects()` — все отслеживаемые объекты (осторожно с памятью)
- [ ] `gc.get_referrers(obj)`, `gc.get_referents(obj)` — отладка утечек

#### Алгоритм сборки: триколорная маркировка
- [ ] **Tricolor marking** — белый (не посещён), серый (в обработке), чёрный (обработан)
- [ ] Обход графа ссылок; обнаружение циклически недостижимых объектов
- [ ] Фазы: mark (маркировка достижимых) → sweep (освобождение недостижимых)

#### Тонкости __del__
- [ ] Объекты с `__del__` — в отдельной группе (uncollectable); не собираются сразу
- [ ] Цикл с `__del__`: порядок вызова не гарантирован; возможна утечка
- [ ] **Resurrection** — объект «воскресает» в `__del__` (сохраняет ссылку); gc может вызвать __del__ позже
- [ ] Рекомендация: избегать `__del__`; использовать context manager, weakref.finalize
- [ ] **`weakref.finalize(obj, callback, *args)`** — регистрация callback при сборке obj; надёжнее `__del__`; вызывается при gc; возвращает finalizer с `.detach()`, `.alive`

### 93. Аллокация памяти при создании объектов

- [ ] Выделение через CPython allocator (pymalloc)
- [ ] Пул мелких объектов — быстрее, меньше фрагментации
- [ ] Размер объекта: `sys.getsizeof(obj)` — только сам объект, без вложенных
- [ ] Overhead: каждый объект имеет заголовок (PyObject)

### 94. Память при вычислениях и копировании

- [ ] Присваивание — копирование ссылки, не данных
- [ ] Shallow copy — копируются ссылки на вложенные объекты
- [ ] Deep copy — рекурсивное копирование; может быть медленно и тяжёло
- [ ] Конкатенация строк/списков — создание нового объекта; `+=` для list — in-place
- [ ] Comprehensions — создание нового списка/словаря; генераторы — лениво, экономия памяти

### 95. Память коллекций: list, dict, set

- [ ] List — динамический массив; зарезервированная ёмкость > длины
- [ ] Dict — хеш-таблица; resize при load factor
- [ ] Set — аналогично dict (только ключи)
- [ ] `.clear()` — освобождение, но ёмкость может сохраняться
- [ ] `dict.fromkeys()` — экономия памяти при общих значениях (осторожно с mutable)

### 96. Слабые ссылки (weakref)

- [ ] `weakref.ref(obj)` — слабая ссылка; не увеличивает счётчик
- [ ] `weakref.proxy(obj)` — прозрачный доступ
- [ ] `weakref.WeakKeyDictionary`, `WeakValueDictionary`, `WeakSet`
- [ ] Зачем: кеши, callback, избежание циклов
- [ ] Ограничение: ключи/значения в WeakKey/WeakValue должны быть hashable

### 97. Утечки памяти и их поиск

- [ ] Циклические ссылки — gc должен собирать
- [ ] Глобальные списки/словари — объекты не освобождаются
- [ ] Замыкания, держащие большие объекты
- [ ] C-расширения — утечки вне контроля Python
- [ ] Инструменты: `tracemalloc`, `objgraph`, `memory_profiler`, `guppy3`

### 98. Оптимизация потребления памяти

- [ ] `__slots__` — экономия на `__dict__`
- [ ] Генераторы вместо списков — ленивые вычисления
- [ ] `array.array` — компактные числовые массивы
- [ ] `mmap` — отображение файла в память
- [ ] `itertools` — ленивые итераторы

---

## Часть XVIII. Сигналы ОС (signals)

> **Материалы:** [→ Навигация по Части XVIII](pact/18_signaly_OS_signals/index.md)

### 99. Базовые концепции

- [ ] Сигнал — уведомление процесса от ОС или другого процесса
- [ ] `signal.SIGINT` (Ctrl+C), `SIGTERM`, `SIGKILL`, `SIGUSR1`, `SIGUSR2`
- [ ] Сигналы прерывают выполнение; обработчик вызывается асинхронно
- [ ] `SIGKILL` и `SIGSTOP` — нельзя перехватить

### 100. Модуль signal

- [ ] `signal.signal(signum, handler)` — установка обработчика
- [ ] `handler` — функция `(signum, frame)` или `SIG_DFL`, `SIG_IGN`
- [ ] `signal.getsignal(signum)` — текущий обработчик
- [ ] `signal.alarm(seconds)` — SIGALRM через N секунд
- [ ] `signal.pause()` — ожидание сигнала
- [ ] `signal.siginterrupt(signum, flag)` — перезапуск системных вызовов после обработчика

### 101. Безопасность при работе с сигналами

- [ ] Обработчик должен быть асинхронно-безопасным (async-signal-safe)
- [ ] В обработчике нельзя: malloc, I/O, большинство Python-операций
- [ ] Исключение: установить флаг, проверить его в основном коде
- [ ] `signal.signal` — только из main thread (Linux)
- [ ] Threading: сигналы доставляются main thread

### 102. Альтернативы для длительных операций

- [ ] `signal.set_wakeup_fd()` — записать в fd при сигнале; совместимость с select/poll
- [ ] `asyncio` — обработка сигналов в event loop: `loop.add_signal_handler()` (Unix)
- [ ] Graceful shutdown: установить флаг по SIGTERM, корректно завершить цикл

### 103. Передача сигналов между процессами

- [ ] `os.kill(pid, signum)` — отправить сигнал процессу
- [ ] `multiprocessing` — координация завершения дочерних процессов
- [ ] `subprocess` — `terminate()`, `kill()` — отправка SIGTERM/SIGKILL

---

## Часть XIX. Анти-паттерны

> **Материалы:** [→ Навигация по Части XIX](pact/19_anti_patterny/index.md)

### 104. Общие анти-паттерны

- [ ] **God Object** — класс делает всё; разбить на мелкие классы
- [ ] **Spaghetti Code** — запутанный поток управления; рефакторинг, функции
- [ ] **Copy-Paste Programming** — дублирование; DRY, функции, наследование
- [ ] **Magic Numbers** — константы в коде; вынести в именованные константы
- [ ] **Bare except** — `except:` ловит всё; указывать конкретные исключения
- [ ] **Pass in except** — игнорировать исключение без логирования; хотя бы `logging`

### 105. Анти-паттерны Python

- [ ] **Mutable default argument** — `def f(a=[])`; использовать `None`
- [ ] **Using `len()` for truthiness** — `if len(x) > 0` вместо `if x`
- [ ] **Comparing with `==` to None** — использовать `is None`
- [ ] **String concatenation in loop** — `''.join(list)` вместо `s += part`
- [ ] **`except Exception`** — слишком широко; ловить конкретные типы
- [ ] **`from module import *`** — засоряет namespace; явный импорт
- [ ] **`eval(input())`** — опасно; `ast.literal_eval` или парсинг
- [ ] **Modifying list while iterating** — использовать срез `[:]` или `list()`

### 106. Анти-паттерны ООП

- [ ] **Inheritance for code reuse only** — композиция лучше
- [ ] **Deep inheritance hierarchy** — плохо тестировать; mixins, композиция
- [ ] **Breaking Liskov Substitution** — подтип должен быть заменяем
- [ ] **Anemic model** — объекты только с данными, логика снаружи

### 107. Анти-паттерны производительности

- [ ] **N+1 queries** — в циклах делать запросы; batch, join
- [ ] **Creating objects in tight loop** — вынести создание наружу
- [ ] **Unnecessary list copy** — `list(x)` когда можно итерировать
- [ ] **Global lookup in loop** — `local_f = func` перед циклом

### 108. Анти-паттерны тестирования

- [ ] **No tests** — писать тесты
- [ ] **Testing implementation, not behavior** — тестировать интерфейс
- [ ] **Flaky tests** — нестабильные; убрать зависимость от времени, порядка
- [ ] **God test** — один тест проверяет всё; разделить на мелкие

---

## Часть XX. Полезные хаки и трюки

> **Материалы:** [→ Навигация по Части XX](pact/20_haki_i_tryuki/index.md)

### 109. Обмен переменных и распаковка

- [ ] `a, b = b, a` — обмен без временной переменной
- [ ] `first, *rest = iterable` — первый и остальные
- [ ] `*_, last = iterable` — только последний
- [ ] `dict(zip(keys, values))` — словарь из двух списков

### 110. Объединение и слияние

- [ ] `{**d1, **d2}` — слияние словарей
- [ ] `[*a, *b]` — объединение списков
- [ ] `(x for t in tuples for x in t)` — flatten кортежей
- [ ] `itertools.chain.from_iterable(nested)` — flatten

### 111. Условные выражения и значения по умолчанию

- [ ] `x = a or b` — осторожно: 0, '' дадут b
- [ ] `x = a if condition else b` — тернарный оператор
- [ ] `d.get(key, default)` — безопасный доступ к dict; `d.setdefault(key, default)` — get или set; `d.pop(key, default)` — извлечь с default
- [ ] `next((x for x in items if cond), default)` — первый совпадающий или default

### 112. Работа с None и optional

- [ ] `x = value or default` — если value falsy
- [ ] `x = value if value is not None else default` — только для None
- [ ] `x = getattr(obj, 'attr', default)` — атрибут или default
- [ ] Walrus: `if (x := f()) is not None:`

### 113. Декораторы и обёртки

- [ ] `@functools.lru_cache(maxsize=None)` — мемоизация
- [ ] `@functools.wraps(f)` — сохранение метаданных
- [ ] Декоратор с аргументами: вложенные функции
- [ ] `functools.partial(func, arg)` — фиксация аргументов

### 114. Контексты и ресурсы

- [ ] `contextlib.suppress(FileNotFoundError)` — игнорировать исключение
- [ ] `contextlib.nullcontext()` — пустой контекст
- [ ] `with open(...) as f1, open(...) as f2:` — несколько ресурсов
- [ ] `contextlib.ExitStack()` — динамический набор контекстов

### 115. Отладка и интроспекция

- [ ] `breakpoint()` — отладочная точка (Python 3.7+); вызывает `sys.breakpointhook()`; можно переопределить
- [ ] `vars(obj)` — `__dict__` объекта
- [ ] `pprint.pprint(obj)` — форматированный вывод для вложенных структур; `width`, `depth`
- [ ] `reprlib.repr(obj)` — сокращённый repr для больших структур; избегание переполнения при вложенности
- [ ] `dir(obj)` — имена атрибутов
- [ ] `f'{var=}'` — debug-вывод (Python 3.8+)
- [ ] `__debug__` — False при `python -O`
- [ ] `traceback.print_exc()` — печать текущего исключения

### 116. Однострочники (с осторожностью)

- [ ] List comprehension с условием: `[x for x in items if cond]`
- [ ] Dict comprehension: `{k: v for k, v in items}`
- [ ] Swap в одну строку: `a, b = b, a`
- [ ] Читаемость важнее краткости

---

## Часть XXI. Актуальные библиотеки и их тонкости

> **Материалы:** [→ Навигация по Части XXI](pact/21_aktualnye_biblioteki_i_ih_tonkosti/index.md)

### 117. HTTP и сети

- [ ] **requests** — простой API; сессии для keep-alive; таймауты обязательно
- [ ] **httpx** — async, HTTP/2; совместим с requests
- [ ] **aiohttp** — async HTTP; клиент и сервер
- [ ] **urllib3** — низкоуровневый; используется requests
- [ ] Тонкость: `requests` блокирует; для async — httpx/aiohttp

### 118. Базы данных

- [ ] **sqlite3** — stdlib; один writer; `executemany` для batch
- [ ] **SQLAlchemy** — ORM и Core; session lifecycle, lazy loading
- [ ] **asyncpg** — async PostgreSQL; быстрее psycopg2
- [ ] **alembic** — миграции для SQLAlchemy
- [ ] Тонкость: connection pooling; не держать соединения открытыми

### 119. Сериализация и конфигурация

- [ ] **json** — stdlib; `default` и `object_hook` для кастомных типов; `ensure_ascii`, `indent`; `JSONEncoder`, `JSONDecoder`; `cls` для кастомного encoder
- [ ] `json.JSONDecodeError` — при невалидном JSON от `loads()`; наследник `ValueError`; `exc.lineno`, `exc.colno`, `exc.pos` для отладки
- [ ] **yaml** — PyYAML; `safe_load` вместо `load` (безопасность)
- [ ] **toml** — tomli (чтение), tomli-w (запись); tomllib в stdlib (3.11+, только чтение); pyproject.toml
- [ ] **pydantic** — валидация и сериализация; BaseModel, Settings
- [ ] **python-dotenv** — загрузка .env

### 120. Логирование и мониторинг

- [ ] **logging** — stdlib; логгеры, хендлеры, форматтеры; `dictConfig`
- [ ] **structlog** — структурированные логи; контекст, процессоры
- [ ] **loguru** — простой API; меньше конфигурации
- [ ] **sentry-sdk** — отслеживание ошибок в продакшене

### 121. Тестирование

- [ ] **pytest** — фикстуры, параметризация, плагины; `conftest.py`
- [ ] **pytest-asyncio** — тесты async-кода
- [ ] **pytest-cov** — покрытие
- [ ] **hypothesis** — property-based testing
- [ ] **factory_boy**, **Faker** — тестовые данные
- [ ] **responses**, **respx** — мок HTTP-запросов
- [ ] **freezegun** — мок времени
- [ ] Тонкость: изоляция тестов; не использовать глобальное состояние

### 122. CLI и упаковка

- [ ] **click** — декораторы, группы; `@click.option`, `@click.argument`
- [ ] **typer** — поверх Click; автогенерация из type hints
- [ ] **rich** — красивый вывод в терминал; таблицы, прогресс
- [ ] **setuptools** — сборка пакетов; `pyproject.toml`
- [ ] **hatch**, **flit** — современная сборка

### 123. Дата и время

- [ ] **datetime** — stdlib; naive vs aware; timezone
- [ ] **zoneinfo** — stdlib (3.9+); IANA timezone database
- [ ] **python-dateutil** — парсинг, относительные даты
- [ ] **pendulum**, **arrow** — альтернативы с удобным API
- [ ] Тонкость: всегда использовать timezone-aware для приложений

### 124. Файлы и пути

- [ ] **pathlib** — stdlib; объектный API
- [ ] **watchdog** — мониторинг изменений файловой системы
- [ ] **aiofiles** — async чтение/запись файлов
- [ ] **py7zr**, **rarfile** — архивы

### 125. Конкурентность и async

- [ ] **asyncio** — stdlib; event loop, корутины
- [ ] **aiohttp**, **asyncpg**, **aioredis** — async-драйверы
- [ ] **anyio** — абстракция над asyncio/trio; задачи, блокирующий код
- [ ] **trio** — альтернатива asyncio; structured concurrency
- [ ] Тонкость: не смешивать sync и async без `run_in_executor`

### 126. Валидация и схемы

- [ ] **pydantic** — валидация, сериализация; BaseModel
- [ ] **marshmallow** — сериализация/десериализация
- [ ] **cerberus** — валидация словарей
- [ ] **jsonschema** — валидация JSON

### 127. Утилиты

- [ ] **orjson** — быстрый JSON; C-реализация; `orjson.dumps()`, `orjson.loads()`
- [ ] **attrs** — альтернатива dataclasses; больший контроль
- [ ] **tenacity** — retry с экспоненциальной задержкой
- [ ] **cachetools** — TTLCache, LFUCache; кеширование
- [ ] **humanize** — человекочитаемые числа, даты
- [ ] **more-itertools** — chain, chunked, sliding_window и др.
- [ ] **boltons** — набор утилит (часть stdlib-подобных)

---

## Часть XXII. Фреймворки, сервисы и инфраструктура

> **Материалы:** [→ Навигация по Части XXII](pact/22_freimvorki_servisy_i_infrastruktura/index.md)

### 128. Web-фреймворки

#### Full-stack
- [ ] **Django** — полноценный фреймворк; ORM, админка, миграции, формы; MTV; middleware; Django REST Framework
- [ ] **Django Ninja** — FastAPI-подобный API поверх Django; типы, async
- [ ] **Pyramid** — гибкий; traversal, URL dispatch; подходит для API и больших приложений

#### Микрофреймворки
- [ ] **Flask** — минималистичный; blueprints, extensions; WSGI; Jinja2
- [ ] **FastAPI** — async, type hints, OpenAPI/Swagger; Pydantic; Starlette под капотом
- [ ] **Quart** — async-версия Flask; совместим с Flask API
- [ ] **Litestar** — альтернатива FastAPI; flexible, plugins
- [ ] **Starlette** — ASGI toolkit; минимальный; основа для FastAPI
- [ ] **Sanic** — async, быстрый; uvloop; Flask-подобный API

#### ASGI vs WSGI
- [ ] **WSGI** — синхронный; один запрос — один поток; Gunicorn, uWSGI
- [ ] **ASGI** — async; один поток — много соединений; Uvicorn, Hypercorn, Daphne
- [ ] **Gunicorn** — WSGI-сервер; workers; gevent/eventlet для pseudo-async
- [ ] **Uvicorn** — ASGI-сервер; uvloop; для FastAPI, Starlette

### 129. Очереди, брокеры сообщений, фоновые задачи

- [ ] **Celery** — распределённая очередь задач; Redis/RabbitMQ; beat для периодики
- [ ] **Celery + Django** — celery.py, CELERY_BROKER_URL; shared_task
- [ ] **RQ (Redis Queue)** — простые фоновые задачи; Redis; легче Celery
- [ ] **Dramatiq** — альтернатива Celery; RabbitMQ; middleware, retries
- [ ] **ARQ** — async RQ; asyncio; Redis
- [ ] **Huey** — лёгкая очередь; Redis, SQLite, in-memory
- [ ] **Redis** — pub/sub, очереди; используется как брокер для Celery, RQ
- [ ] **RabbitMQ** — AMQP; очереди, exchange; Celery, Dramatiq
- [ ] **Apache Kafka** — стриминг; партиции, consumer groups; aiokafka, confluent-kafka

### 130. Сервисы и базы данных (драйверы и интеграция)

- [ ] **PostgreSQL** — psycopg2, asyncpg; connection pooling (SQLAlchemy, pgBouncer)
- [ ] **MySQL/MariaDB** — PyMySQL, mysqlclient; SQLAlchemy
- [ ] **MongoDB** — pymongo, motor (async)
- [ ] **Redis** — redis-py; aioredis (async); pipelines, pub/sub
- [ ] **Elasticsearch** — elasticsearch-py; индексация, поиск
- [ ] **S3-совместимое хранилище** — boto3 (AWS), aioboto3; MinIO
- [ ] **ClickHouse** — clickhouse-driver; аналитика
- [ ] **SQLite** — stdlib; APSW для низкоуровневого доступа

### 131. Оркестрация, контейнеры, деплой

- [ ] **Docker** — docker-py; сборка образов, управление контейнерами
- [ ] **Kubernetes** — kubernetes-client; Python-операторы; Helm charts
- [ ] **AWS** — boto3; Lambda, ECS, S3, RDS; serverless
- [ ] **Terraform** — провайдеры; инфраструктура как код (не Python, но рядом)
- [ ] **Ansible** — автоматизация; модули на Python; playbooks
- [ ] **Serverless** — AWS Lambda, Google Cloud Functions; Zappa, Mangum (ASGI→Lambda)

### 132. Мониторинг, логирование, трейсинг

- [ ] **Sentry** — отслеживание ошибок; sentry-sdk; контекст, breadcrumbs
- [ ] **Prometheus** — метрики; prometheus_client; counters, gauges, histograms
- [ ] **OpenTelemetry** — трейсинг; otel-api, otel-sdk; распределённая трассировка
- [ ] **Datadog** — APM; datadog; трейсинг, метрики
- [ ] **structlog** — структурированные логи; JSON; процессоры, контекст
- [ ] **ELK/Loki** — централизованные логи; интеграция с Python

### 133. CI/CD и тестирование инфраструктуры

- [ ] **GitHub Actions** — workflows; Python setup; pytest, coverage
- [ ] **GitLab CI** — .gitlab-ci.yml; stages, jobs
- [ ] **tox** — тесты в разных окружениях; py37, py38; lint, test
- [ ] **nox** — гибкие сессии; альтернатива tox
- [ ] **pre-commit** — хуки перед коммитом; black, ruff, mypy
- [ ] **mypy** — в CI; strict mode

---

## Часть XXIII. ИИ и машинное обучение (Python)

> **Материалы:** [→ Навигация по Части XXIII](pact/23_ii_i_mashinnoe_obuchenie/index.md)

### 134. Основы ML и data science

- [ ] **NumPy** — массивы, операции; broadcasting; dtype; memory layout
- [ ] **Pandas** — DataFrame, Series; индексы; группировка; merge, concat
- [ ] **Scikit-learn** — ML-алгоритмы; fit/predict; pipeline; cross-validation; метрики
- [ ] **Matplotlib**, **Seaborn** — визуализация; plotly — интерактивные графики
- [ ] **Jupyter** — ноутбуки; ipykernel; виртуальные окружения в Jupyter
- [ ] **SciPy** — научные вычисления; оптимизация; статистика

### 135. Глубокое обучение (Deep Learning)

- [ ] **PyTorch** — тензоры; autograd; nn.Module; DataLoader; GPU; torchvision
- [ ] **TensorFlow / Keras** — Sequential, Functional API; tf.data; распределённое обучение
- [ ] **JAX** — автоматическое дифференцирование; JIT; XLA; альтернатива PyTorch для исследований
- [ ] **ONNX** — обмен моделями между фреймворками
- [ ] **TensorRT**, **OpenVINO** — оптимизация инференса; GPU, edge

### 136. NLP и языковые модели

- [ ] **Hugging Face Transformers** — BERT, GPT; pipeline; tokenizer; model hub
- [ ] **tokenizers** — быстрая токенизация; BPE, WordPiece
- [ ] **spaCy** — NLP-пайплайн; NER, POS; языковые модели
- [ ] **NLTK** — классические NLP-алгоритмы; корпуса
- [ ] **LangChain** — цепочки для LLM; prompts; agents; RAG; LangSmith
- [ ] **LlamaIndex** — индексация данных для LLM; RAG
- [ ] **OpenAI API** — GPT; chat completions; embeddings; rate limits
- [ ] **Anthropic API** — Claude
- [ ] **Ollama** — локальные LLM; llama, mistral
- [ ] **vLLM**, **TGI** — быстрый инференс LLM; batching

### 137. RAG, агенты, приложения на LLM

- [ ] **RAG (Retrieval-Augmented Generation)** — поиск + генерация; векторные БД
- [ ] **Chroma**, **FAISS**, **Milvus**, **Pinecone** — векторные хранилища
- [ ] **sentence-transformers** — эмбеддинги; similarity search
- [ ] **LangChain** — chains, agents; tools; memory
- [ ] **CrewAI** — мультиагентные системы
- [ ] **AutoGPT**, **BabyAGI** — автономные агенты (концептуально)

### 138. Компьютерное зрение

- [ ] **OpenCV** — обработка изображений; cv2; детекция, трекинг
- [ ] **torchvision** — модели для CV; ResNet, YOLO; трансформации
- [ ] **Ultralytics YOLO** — детекция объектов; обучение, инференс
- [ ] **PIL/Pillow** — базовые операции с изображениями
- [ ] **albumentations** — аугментации для обучения
- [ ] **mediapipe** — face, pose, hands; real-time

### 139. Рекомендательные системы, MLOps

- [ ] **Surprise** — коллаборативная фильтрация; SVD
- [ ] **LightFM** — гибридные рекомендации
- [ ] **MLflow** — эксперименты; логирование; модели; регистри; деплой
- [ ] **DVC** — версионирование данных; pipelines
- [ ] **Weights & Biases** — эксперименты; визуализация; артефакты
- [ ] **Kubeflow** — ML на Kubernetes; pipelines
- [ ] **BentoML** — упаковка моделей; сервинг; Docker
- [ ] **Seldon** — деплой ML-моделей; Kubernetes

### 140. Тонкости ML и ИИ в Python

- [ ] **GPU** — CUDA; PyTorch/TensorFlow на GPU; memory management
- [ ] **Batch size** — влияние на память и скорость
- [ ] **Mixed precision** — fp16, bf16; ускорение обучения
- [ ] **Distributed training** — DataParallel, DistributedDataParallel; multi-GPU
- [ ] **Quantization** — INT8; уменьшение размера модели; ONNX
- [ ] **Версионирование моделей** — MLflow, DVC; reproducibility
- [ ] **Этика и ограничения** — bias; interpretability; LLM hallucinations

---

## Часть XXIV. Дополнительные темы (по интересам)

> **Материалы:** [→ Навигация по Части XXIV](pact/24_dopolnitelnye_temy_po_interesam/index.md)

### 141. Web-фреймворки (повтор с фокусом на выбор)

- [ ] Когда FastAPI, когда Django, когда Flask
- [ ] Async vs sync; масштабируемость
- [ ] ASGI vs WSGI — выбор сервера

### 142. Data Science (практика)

- [ ] NumPy — broadcasting, advanced indexing
- [ ] Pandas — оптимизация; category dtype; chunking для больших данных
- [ ] Matplotlib, Seaborn — best practices; публикация

### 143. CLI и автоматизация

- [ ] `argparse`, `click`, `typer`
- [ ] subprocess, shutil
- [ ] pathlib для скриптов
- [ ] Rich — прогресс-бары, таблицы, панели

### 144. Декораторы (углублённо)

- [ ] Декоратор без параметров и с параметрами
- [ ] `functools.wraps`
- [ ] Сохранение сигнатуры: `inspect.signature`
- [ ] Декораторы классов

---

## Часть XXV. C-расширения и FFI

> **Материалы:** [→ Навигация по Части XXV](pact/25_c_rasshireniya_i_ffi/index.md)

### 145. ctypes

- [ ] `ctypes.CDLL(path)` — загрузка C-библиотеки (shared library)
- [ ] `ctypes.POINTER`, `ctypes.c_int`, `ctypes.c_char_p` — типы
- [ ] `lib.func.argtypes`, `lib.func.restype` — сигнатура
- [ ] `ctypes.byref(obj)`, `ctypes.pointer(obj)` — передача указателей
- [ ] Освобождение GIL: `c_func.argtypes`; осторожно с памятью
- [ ] Ограничения: ручное управление типами; нет автоматической проверки

### 146. cffi

- [ ] **ABI mode** — как ctypes; без компиляции; `ffi.dlopen()`
- [ ] **API mode** — компиляция C-кода; `ffi.cdef()`; `ffi.verify()` / `ffi.compile()`
- [ ] `ffi.new()`, `ffi.from_buffer()` — выделение памяти
- [ ] `ffi.string()`, `ffi.buffer()` — работа с буферами
- [ ] PyPy-совместимость; часто быстрее ctypes

### 147. pybind11

- [ ] C++ → Python; шаблоны, STL; автоматическая конвертация
- [ ] `PYBIND11_MODULE(name, m)` — объявление модуля
- [ ] `m.def()`, `m.attr()` — функции, классы, атрибуты
- [ ] Освобождение GIL: `py::call_guard<py::gil_scoped_release>()`
- [ ] NumPy support: `py::array_t`; zero-copy
- [ ] Требует C++11; сборка через setuptools/CMake

### 148. Сборка C-расширений

- [ ] `setuptools.Extension(name, sources, include_dirs=[], library_dirs=[], libraries=[])`
- [ ] `python setup.py build_ext --inplace` — сборка на месте
- [ ] `pyproject.toml` [build-system] с setuptools для C-ext
- [ ] Cython — написание на Python-подобном; компиляция в C
- [ ] `numpy.distutils` — для расширений с NumPy (устаревает)

---

## Часть XXVI. Практические паттерны (resilience, caching)

> **Материалы:** [→ Навигация по Части XXVI](pact/26_prakticheskie_patterny_resilience_i_caching/index.md)

### 149. Retry и backoff

- [ ] **tenacity** — `@retry`; `stop_after_attempt`, `wait_exponential`
- [ ] `retry_if_exception_type()`, `retry_if_result()`
- [ ] Exponential backoff — задержка растёт экспоненциально
- [ ] Jitter — случайное отклонение; избежание thundering herd

### 150. Кеширование

- [ ] **cachetools** — `TTLCache`, `LRUCache`, `LFUCache`
- [ ] **Redis** — распределённый кеш; redis-py; `get`, `set`, `delete`
- [ ] **Memcached** — pymemcache; простой key-value
- [ ] `functools.lru_cache` — in-memory; для функций
- [ ] Cache invalidation — стратегии; TTL, tag-based

### 151. Rate limiting

- [ ] **Token bucket** — токены пополняются с фиксированной скоростью
- [ ] **Leaky bucket** — фиксированная скорость выхода
- [ ] **Sliding window** — окно по времени
- [ ] Библиотеки: `limits`, `ratelimit`; Redis для распределённого
- [ ] Защита API от abuse; throttling

### 152. Circuit breaker

- [ ] Паттерн: при серии ошибок — «размыкание»; не вызывать сервис
- [ ] Состояния: closed, open, half-open
- [ ] **pybreaker** — реализация circuit breaker
- [ ] Использование при вызовах внешних сервисов; отказоустойчивость

### 153. Message serialization (msgpack, protobuf)

- [ ] **msgpack** — бинарная сериализация; быстрее JSON; `msgpack.packb()`, `msgpack.unpackb()`
- [ ] **Protocol Buffers** — protobuf; `.proto` файлы; `protoc`; строгая схема
- [ ] **Avro** — схема; используется в Kafka
- [ ] **Cap'n Proto**, **FlatBuffers** — zero-copy; для высоконагруженных систем
- [ ] Выбор: JSON (универсальность), msgpack (скорость), protobuf (схема, версионирование)

---

## Часть XXVII. PEP как система знаний: мотивация и контекст изменений

> **Материалы:** [→ Навигация по Части XXVII](pact/27_pep_kak_sistema_znanii_motivaciya_i_kontekst_izmenenii/index.md)

### 154. Как читать и использовать PEP

- [ ] **PEP** — Python Enhancement Proposal; процесс изменения языка и экосистемы
- [ ] Структура PEP: Abstract, Motivation, Rationale, Specification, Backwards Compatibility
- [ ] Статусы: Draft, Active, Accepted, Final, Deferred, Rejected, Superseded
- [ ] **Не просто список — понимание мотивации**: для каждого PEP читать Motivation и Rationale; *почему* изменение нужно, *какие* альтернативы рассмотрены, *какие* компромиссы
- [ ] Контекст: исторические причины; проблемы, которые решает; rejected альтернативы
- [ ] Ресурсы: pep.python.org; What's New in Python X.Y; python.org/dev/peps

### 155. Ключевые PEP по категориям (с мотивацией)

#### Синтаксис и семантика
- [ ] **PEP 8** — стиль кода; читаемость; консенсус сообщества
- [ ] **PEP 572** (walrus `:=`) — мотивация: избежать дублирования в conditions/comprehensions
- [ ] **PEP 634–636** (match/case) — мотивация: pattern matching; читаемость; exhaustiveness
- [ ] **PEP 479** (StopIteration в генераторах) — мотивация: скрытые баги; явный RuntimeError
- [ ] **PEP 604** (`X | Y`) — мотивация: упрощение union; меньше импортов

#### Типизация
- [ ] **PEP 484** (type hints) — мотивация: статический анализ; документация; IDE
- [ ] **PEP 563** (postponed evaluation) — мотивация: `from __future__ import annotations`; аннотации как строки; forward references без кавычек
- [ ] **PEP 593** (Annotated) — мотивация: метаданные в типах; FastAPI, pydantic; не влияет на runtime
- [ ] **PEP 544** (Protocol) — мотивация: structural subtyping; утиная типизация
- [ ] **PEP 585** (builtin generics) — мотивация: `list[int]` без импорта; консистентность
- [ ] **PEP 647** (TypeGuard) — мотивация: пользовательские type guards; narrowing
- [ ] **PEP 673** (Self) — мотивация: возврат self; цепочки методов; наследование
- [ ] **PEP 695** (type statement) — мотивация: чистое объявление алиасов; PEP 613 legacy

#### Асинхронность и конкурентность
- [ ] **PEP 492** (async/await) — мотивация: читаемость; замена callback hell
- [ ] **PEP 3156** (asyncio) — мотивация: стандартная библиотека для async I/O
- [ ] **PEP 684** (per-interpreter GIL) — мотивация: параллелизм; изоляция интерпретаторов
- [ ] **PEP 703** (free-threaded) — мотивация: истинный multithreading; путь к no-GIL

#### ООП и модель объектов
- [ ] **PEP 3135** (super без аргументов) — мотивация: простота; правильный MRO
- [ ] **PEP 422** (__prepare__) — мотивация: кастомный namespace при создании класса
- [ ] **PEP 487** (__init_subclass__) — мотивация: альтернатива метаклассам; простота
- [ ] **PEP 562** (module __getattr__) — мотивация: ленивая загрузка; backward compat

#### Исключения и контроль потока
- [ ] **PEP 3134** (exception chaining) — мотивация: `raise ... from ...`; полный traceback
- [ ] **PEP 654** (ExceptionGroup) — мотивация: параллельные исключения; TaskGroup
- [ ] **PEP 678** (add_note) — мотивация: доп. контекст в исключениях; `__notes__` в traceback
- [ ] **PEP 3132** (extended unpacking) — мотивация: `*rest`; удобство распаковки

#### Импорт и упаковка
- [ ] **PEP 420** (namespace packages) — мотивация: пакеты без `__init__.py`; распространяемые
- [ ] **PEP 517/518** (pyproject.toml) — мотивация: стандартизация сборки; единый конфиг
- [ ] **PEP 561** (py.typed) — мотивация: типизированные пакеты; stub'ы из установленных пакетов
- [ ] **PEP 621** (project metadata) — мотивация: метаданные в pyproject.toml
- [ ] **PEP 668** (externally managed) — мотивация: защита системного Python; обязательный venv

#### Производительность и интерпретатор
- [ ] **PEP 709** (comprehension inlining) — мотивация: оптимизация 3.12; меньше накладных расходов
- [ ] **PEP 659** (specializing adaptive interpreter) — мотивация: оптимизация 3.11; быстрее циклы

### 156. Связь PEP между собой

- [ ] PEP часто отменяют/расширяют другие: PEP 585 supersedes часть PEP 484
- [ ] Цепочки: PEP 484 → PEP 544, 585, 604, 613, 647, 673, 675, 692, 695, 696
- [ ] Понимание эволюции: type hints начались с PEP 484; каждый PEP добавляет кусок
- [ ] Deferred/Rejected — почему не принято; контекст решений сообщества

### 157. Практика: как применять знания из PEP

- [ ] При изучении фичи — читать Motivation и Rationale; не только Specification
- [ ] При миграции — Backwards Compatibility; DeprecationWarning; переходный период
- [ ] При дизайне API — опираться на PEP; ссылаться в docstring
- [ ] Следить за Accepted/Final — готовящиеся изменения; адаптироваться заранее

---

*Дата создания: 2025-02-07*
*Последнее обновление: 2025-02-07*
*Расширение: Python 3.10–3.12+, stdlib, async, OOP, тонкости*

---

## Краткий обзор структуры плана (для навигации)

> Порядок изучения: см. [Последовательность изучения](#последовательность-изучения-от-простого-к-сложному) в начале документа.

| Часть | Уровень | Тема |
|-------|---------|------|
| 0 | 0 | Философия, границы и ментальные модели |
| I | 1 | Отличия Python 3 от Python 2.7 |
| II | 1 | Строки, кодировки, bytes |
| III | 2, 4 | Стандартная библиотека |
| IV | 3 | Современный синтаксис Python 3 |
| V | 3 | Контекстные менеджеры |
| VI | 6 | Асинхронность, потоки, мультипроцессинг |
| VII | 8 | Модель выполнения и внутренности |
| VIII | 5 | Инструменты и экосистема |
| IX | 5 | Миграция с Python 2.7 |
| X | 7 | Магические методы (dunder) |
| XI | 7 | Хеширование |
| XII | 7 | ООП углублённо |
| XIII | 9 | Паттерны проектирования |
| XIV | 9 | Алгоритмы и структуры данных |
| XV | 8 | Внутренности Python |
| XVI | 9 | Тонкости и подводные камни |
| XVII | 8 | Память: аллокация, gc |
| XVIII | 9 | Сигналы ОС |
| XIX | 9 | Анти-паттерны |
| XX | 9 | Полезные хаки и трюки |
| XXI | 10 | Актуальные библиотеки |
| XXII | 10 | Фреймворки и инфраструктура |
| XXIII | 10 | ИИ и машинное обучение |
| XXIV | 10 | Дополнительные темы |
| XXV | 10 | C-расширения и FFI |
| XXVI | 10 | Практические паттерны |
| XXVII | 10 | PEP как система знаний |

---

## Основные добавления (последнее обновление)

| Область | Добавлено |
|---------|-----------|
| **Генераторы** | `send()`, `throw()`, `close()`; async generators; PEP 479 |
| **Python 3.10+** | `X \| Y`, `zip(strict=True)` |
| **Python 3.11+** | ExceptionGroup, `except*`, Self, Never, assert_never; TypeVarTuple; Required, NotRequired; LiteralString |
| **Python 3.12+** | `type` statement, `@override` |
| **Контексты** | `__aenter__`, `__aexit__`, `@asynccontextmanager` |
| **asyncio** | Streams, subprocess; `asyncio.timeout()` |
| **stdlib** | io.StringIO/BytesIO; decimal, fractions, statistics; struct, array; collections.abc |
| **stdlib** | sys (version_info, modules, path); platform, errno; traceback, warnings, atexit, faulthandler |
| **stdlib** | importlib.resources, importlib.metadata; tomllib, graphlib; functools.cache |
| **stdlib** | re (fullmatch, finditer, flags, named groups); subprocess (PIPE, communicate) |
| **stdlib** | unicodedata, textwrap, difflib; buffer protocol, memoryview |
| **stdlib** | __set_name__; module __getattr__ (PEP 562) |
| **Import** | sys.meta_path, path_hooks; циклические импорты; __getattr__ модуля |
| **dataclasses** | replace, KW_ONLY; field(init=False), metadata; slots=True (3.10) |
| **enum** | Flag, IntFlag, StrEnum (3.11), unique, auto |
| **multiprocessing** | shared_memory; Pool initializer, maxtasksperchild |
| **Профилирование** | cProfile, tracemalloc, memory_profiler, faulthandler |
| **Отладка** | pdb, debugpy; PYTHONBREAKPOINT |
| **ast, dis** | parse, NodeVisitor; literal_eval; dis.dis |
| **Сеть** | select, selectors; socket, ssl |
| **queue** | Empty, Full; task_done, join |
| **threading** | Timer |
| **types** | SimpleNamespace, MappingProxyType |
| **argparse** | subparsers, mutually_exclusive_group |
| **logging** | dictConfig, LoggerAdapter, Filter |
| **venv** | EnvBuilder; ensurepip; zipapp |
| **Безопасность** | Bandit, safety, pip-audit, semgrep |
| **Тонкости** | else в цикле/try; bound method; truthiness; операторы → методы |
| **Python 3.13** | Free-threaded (PEP 703), @deprecated (PEP 702), -P |
| **ReDoS** | Безопасность регулярных выражений; катастрофический backtracking |
| **stdlib** | zipfile, tarfile, gzip; xml.etree, html.parser; gettext, locale; sched, uuid, base64; ipaddress |
| **stdlib** | csv Dialect/Sniffer; configparser interpolation |
| **Интерпретатор** | __build_class__, __prepare__; super() и cell variables |
| **Упаковка** | wheel, sdist; editable install; twine, build; entry points, MANIFEST.in; src layout; py.typed |
| **Тестирование** | doctest; hypothesis (property-based); mutation testing; pytest.raises/warns |
| **Инструменты** | pre-commit; ruff/mypy/pyright config |
| **C-расширения** | ctypes, cffi, pybind11; setuptools.Extension |
| **CPython** | PyObject_HEAD; compact dict (PEP 412); overallocation в list; code/frame objects |
| **GC** | Триколорная маркировка; поколения; __del__ тонкости (resurrection, циклы) |
| **Компиляция** | Токены → AST → байткод → VM; оптимизации 3.11+/3.12+ |
| **GIL** | Классический; per-interpreter (PEP 684); free-threaded (PEP 703) |
| **Теория типов** | Variance (covariant, contravariant, invariant); TypeGuard; narrowing; NewType; ClassVar; Type[T]; Any; Annotated; __future__ annotations |
| **PEP** | Мотивация изменений; ключевые PEP по категориям; связь между PEP |
| **Философия и ментальные модели** | Zen of Python; история решений; границы языка; EAFP; name binding; duck typing |
| **Числовая модель** | IEEE 754; decimal vs float; Decimal.quantize; ROUND_HALF_EVEN; sys.int_info; numbers hierarchy |
| **Unicode** | Grapheme clusters; bidi; surrogate pairs; NFKC/NFKD; сравнение строк |
| **Сериализация** | pickle протоколы 0–5; __reduce__; __getstate__/__setstate__; marshal; shelve |
| **Исключения** | __context__ vs __cause__; __suppress_context__; sys.exception (3.11+); exc.add_note (3.11) |
| **Безопасность** | sys.audit/addaudithook; faulthandler internals; hmac vs hashlib; secrets vs random |
| **Время/даты** | monotonic vs time; naive vs aware; DST/fold; zoneinfo |
| **Файловая система** | scandir vs listdir; mmap; PurePath vs Path; os.sendfile; Path.walk (3.12); shutil |
| **Тестирование** | Property-based; mutation testing; test doubles (Stub, Mock, Spy, Fake, Dummy) |
| **Метапрограммирование** | AST-трансформации; bytecode manipulation; compile() флаги; eval/exec безопасность |
| **Подклассирование** | list.sort()/dict.update(); __class__ assignment; __slots__ наследование; UserList/UserDict |
| **Интроспекция** | __annotations__; get_type_hints; signature vs getfullargspec; __wrapped__; sys._getframe |
| **Модульная система** | __spec__; importlib.abc; __main__ и -m; __package__ vs __name__ |
| **Ограничения** | getrecursionlimit; sys.maxsize; глубина вложенности; длина строковых литералов |
| **Детерминированность** | PYTHONHASHSEED; порядок итерации dict/set; порядок **kwargs |
| **Математика** | math.fsum vs sum; decimal localcontext; Fraction(0.1) gotcha |
| **Системные вызовы** | OSError иерархия; os/stat; EINTR; siginterrupt |
| **Окружение** | PEP 668 (externally managed); os.environ; getpass; pyenv/asdf |
| **Py2→Py3 миграция** | exec, print, cmp, apply, execfile; iteritems→items; xrange→range; encoding |
| **stdlib доп.** | fnmatch, glob, os.walk; tempfile (TemporaryDirectory); pprint, reprlib; http.server, email, mimetypes |
| **Строки** | str.removeprefix/removesuffix (3.9) |
| **weakref** | weakref.finalize — альтернатива __del__; operator.methodcaller |
