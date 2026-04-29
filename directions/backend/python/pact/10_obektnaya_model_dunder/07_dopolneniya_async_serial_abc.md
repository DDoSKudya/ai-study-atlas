[← Назад к индексу части X](index.md)


Асинхронные dunder-методы — это «двойники» уже знакомых протоколов, но для мира `async` и event loop:

- `__await__` — поддержка `await obj`;
- `__aiter__`, `__anext__` — поддержка `async for`;
- `__aenter__`, `__aexit__` — поддержка `async with`.

Они используются, когда вы хотите:

- сделать **пользовательские awaitable-объекты** (свой «мини-future» или обёртку вокруг IO);
- реализовать **асинхронные итераторы/генераторы**, например, для источников данных «по кусочкам»;
- создать **асинхронные контекстные менеджеры**, которые открывают/закрывают ресурсы асинхронно (`async with pool.acquire() as conn:`).

### A.1. Протокол awaitable: `__await__`

Выражение:

```python
result = await obj
```

выполняется, только если `obj` — **awaitable**. Awaitable — это:

- coroutine-объект (полученный вызовом `async def` функции);
- объект, у которого определён метод `__await__`, возвращающий **итератор**.

Под капотом:

```python
it = obj.__await__()   # должен вернуть итератор
try:
    next(it)
    # event loop будет продолжать вызывать it.send(...) до StopIteration
except StopIteration as stop:
    result = stop.value
```

#### Пример: простой awaitable-объект

```python
class SimpleAwaitable:
    def __init__(self, value):
        self.value = value

    def __await__(self):
        # самый простой случай: сразу вернуть результат
        # должен быть итератор, поэтому используем генератор
        async def _wrapper():
            return self.value
        return _wrapper().__await__()
```

Использование:

```python
async def main():
    res = await SimpleAwaitable(42)
    print(res)  # 42
```

На практике `__await__` используют:

- в low-level примитивах (аналог `asyncio.Future`, обёртки над системными IO-вызовами);
- в библиотеках, где объект должен вести себя «как coroutine», но при этом хранить внутреннее состояние или настройки.

### A.2. Асинхронный итератор: `__aiter__`, `__anext__`

`async for` использует **асинхронный протокол итерации**:

```python
async for item in source:
    ...
```

Под капотом:

1. Получается асинхронный итератор:

   ```python
   it = source.__aiter__()
   ```

2. В цикле вызывается `await it.__anext__()`, пока не будет поднято `StopAsyncIteration`.

#### Минимальный асинхронный итератор

```python
class AsyncCounter:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        value = self.current
        self.current += 1
        return value
```

Использование:

```python
async def main():
    async for x in AsyncCounter(0, 3):
        print(x)  # 0, 1, 2
```

На практике вместо ручной реализации часто используют **асинхронные генераторы**:

```python
async def agen():
    yield 1
    yield 2
```

У такого объекта под капотом уже реализованы `__aiter__`/`__anext__`.

### A.3. Асинхронный контекстный менеджер: `__aenter__`, `__aexit__`

Синтаксис:

```python
async with manager as value:
    ...
```

требует, чтобы объект реализовывал:

- `__aenter__(self)` — асинхронный метод, возвращающий значение для `as value`;
- `__aexit__(self, exc_type, exc_val, exc_tb)` — асинхронный метод, вызываемый при выходе (аналог `__exit__`, но с `await` внутри).

Под капотом (упрощённо):

```python
mgr = manager
value = await mgr.__aenter__()
try:
    await body
except BaseException as exc:
    suppress = await mgr.__aexit__(type(exc), exc, exc.__traceback__)
    if not suppress:
        raise
else:
    await mgr.__aexit__(None, None, None)
```

#### Пример: асинхронный ресурс

```python
class AsyncResource:
    async def __aenter__(self):
        print("open resource async")
        # здесь мог бы быть await на открытие соединения
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("close resource async")
        # здесь мог бы быть await на закрытие/освобождение ресурса
        return False
```

Использование:

```python
async def main():
    async with AsyncResource() as r:
        ...
```

Часто асинхронные контекстные менеджеры строят поверх синхронных:

- оборачивая синхронный `__enter__`/`__exit__` в `loop.run_in_executor`;
- или используя `async with` для высокоуровневых клиентов (aiohttp, asyncpg и т.п.).

---

## Дополнение B. Сериализация и копирование: `__getstate__`, `__setstate__`, `__reduce__`, `__copy__`, `__deepcopy__`

Модуль `pickle` и модуль `copy` используют dunder-методы для того, чтобы:

- решить, **как сохранить и восстановить** объект (pickling);
- выбрать стратегию **поверхностного (`copy.copy`) и глубокого (`copy.deepcopy`) копирования**.

### B.1. Pickling: базовая модель

Когда вы вызываете:

```python
import pickle
data = pickle.dumps(obj)
obj2 = pickle.loads(data)
```

интерпретатор:

1. Строит **описание того, как создать объект заново**;
2. Строит **снимок его состояния** (state).

Для этого используются несколько dunder-методов (в порядке приоритета):

1. `__reduce_ex__(self, protocol)` — новый, предпочтительный API;
2. `__reduce__(self)` — старый API;
3. `__getstate__` / `__setstate__` — более high-level способ управления только состоянием.

### B.2. `__getstate__` и `__setstate__`

Если объект определяет `__getstate__`, `pickle` использует его, чтобы получить состояние:

```python
state = obj.__getstate__()
```

При восстановлении:

```python
obj = cls.__new__(cls, *args_from_reduce*)
obj.__setstate__(state)
```

Типичный паттерн:

```python
class Cache:
    def __init__(self):
        self._data = {}
        self._connection = None  # непиклируемый ресурс

    def __getstate__(self):
        state = self.__dict__.copy()
        # непиклируемые поля удаляем
        state["_connection"] = None
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # соединение нужно создать заново по необходимости
        self._connection = None
```

Использование:

```python
blob = pickle.dumps(cache)
cache2 = pickle.loads(blob)
```

Здесь:

- мы явно указываем, **что сериализовать**, а что — нет;
- при восстановлении сами приводим объект в валидное состояние.

### B.3. `__reduce__` и `__reduce_ex__`

Эти методы — более низкоуровневый API, возвращающий кортеж:

```python
callable, args, state, iteritems, iterdict = obj.__reduce_ex__(protocol)
```

Чаще всего достаточно трёх элементов:

```python
def __reduce__(self):
    return (self.__class__, (self.arg1, self.arg2), self.__dict__)
```

Это означает:

- при восстановлении вызвать `self.__class__(arg1, arg2)`;
- затем присвоить `__dict__ = state`.

В повседневном коде обычно хватает **`__getstate__`/`__setstate__`**, а к `__reduce__` прибегают:

- в библиотеках и низкоуровневом коде;
- когда нужно очень точно контролировать процесс (например, при наследовании от C-расширений).

### B.4. `__copy__` и `__deepcopy__`

Модуль `copy` использует:

- `__copy__(self)` для поверхностной копии:
  - создаётся новый объект;
  - **внутренние ссылки** на те же самые объекты, что и у исходника;
- `__deepcopy__(self, memo)` для глубокой копии:
  - рекурсивно копируются и под-объекты;
  - `memo` — словарь для отслеживания уже скопированных объектов (чтобы не зациклиться).

Пример:

```python
import copy

class Tree:
    def __init__(self, value, children=None):
        self.value = value
        self.children = list(children or [])

    def __copy__(self):
        # поверхностная копия: дети те же
        cls = self.__class__
        new = cls.__new__(cls)
        new.value = self.value
        new.children = self.children
        return new

    def __deepcopy__(self, memo):
        cls = self.__class__
        new = cls.__new__(cls)
        memo[id(self)] = new
        new.value = copy.deepcopy(self.value, memo)
        new.children = copy.deepcopy(self.children, memo)
        return new
```

Использование:

```python
root = Tree(1, [Tree(2), Tree(3)])
shallow = copy.copy(root)
deep = copy.deepcopy(root)
```

Глубокое понимание `__copy__`/`__deepcopy__` нужно, когда:

- вы пишете сложные структуры данных (деревья, графы);
- хотите контролировать, какие части структуры разделяются, а какие копируются.

---

## Дополнение C. ABC, introspection и dunder-методы

### C.1. Абстрактные базовые классы (`abc.ABC`) и dunder-методы

Модуль `abc` позволяет задать **контракты протоколов**:

```python
from abc import ABC, abstractmethod

class MyIterable(ABC):
    @abstractmethod
    def __iter__(self):
        ...
```

Класс, наследующий от `MyIterable`, обязан реализовать `__iter__`, иначе его нельзя инстанциировать.

Стандартные ABC в `collections.abc` (например, `Sized`, `Iterable`, `Container`, `Sequence`, `Mapping`) формализуют набор dunder-методов:

- `Sized` ⇒ `__len__`;
- `Container` ⇒ `__contains__`;
- `Iterable` ⇒ `__iter__`;
- `Sequence` ⇒ `__len__`, `__getitem__` (+ часто `__contains__`, `__iter__`, `__reversed__` реализованы по умолчанию).

Например:

```python
from collections.abc import Sequence

class MySeq(Sequence):
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]
```

Здесь:

- мы реализовали только `__len__` и `__getitem__`;
- `Sequence` добавит реализацию `__contains__`, `__iter__`, `__reversed__` на основе этих двух.

### C.2. `__mro__`, `__bases__` и `super()` в реальной жизни

Функция `super()` работает, опираясь на **MRO (Method Resolution Order)**:

```python
class Base:
    def __init__(self):
        print("Base")

class Mixin:
    def __init__(self):
        print("Mixin")
        super().__init__()

class Child(Mixin, Base):
    def __init__(self):
        print("Child")
        super().__init__()

print(Child.__mro__)
Child()
```

Под капотом `super()` получает:

- текущий класс (в котором он написан);
- экземпляр (или подкласс).

Дальше он ищет **следующий** класс в `__mro__` и вызывает метод оттуда. Это одинаково работает и для обычных методов, и для dunder-методов (если вы вызываете их явно через `super()`).

**Главный паттерн кооперативного наследования:**

- каждый класс в цепочке `__mro__` реализует метод, который **вызывает `super()`**;
- тогда все классы получают шанс отработать.

Это особенно важно для:

- `__init__`;
- `__new__` (вместе с метаклассами);
- dunder-методов, которые вы хотите расширить, а не заменить (например, добавить логирование в `__enter__`/`__exit__`).

### C.3. Метаклассы, `type.__call__` и dunder-методы

Мы уже видели, что:

- вызов `MyClass()` попадает в `type.__call__`;
- тот, в свою очередь, вызывает `__new__`/`__init__`.

Метакласс может переопределить `__call__`, чтобы изменить создание экземпляров:

```python
class TracingMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"Create {cls.__name__}{args, kwargs}")
        obj = super().__call__(*args, **kwargs)
        print(f"Created {obj!r}")
        return obj

class Traced(metaclass=TracingMeta):
    def __init__(self, x):
        self.x = x
```

Теперь `Traced(10)` будет проходить через `TracingMeta.__call__`, а затем через обычные `__new__`/`__init__`.  
Это пример того, как dunder-методы **типа (класса)** управляют поведением dunder-методов **экземпляра**.

### C.4. `__annotations__`, `dataclasses` и `typing`

Аннотации типов, записанные в `__annotations__`, активно используются:

- `dataclasses` — для генерации `__init__`, `__repr__`, `__eq__`, `__hash__` и др.;
- `typing` и `mypy` — для статической проверки типов;
- фреймворками (FastAPI, Pydantic) — для валидации/генерации схем.

Пример:

```python
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
```

`dataclass`:

- читает `User.__annotations__`;
- генерирует:
  - `__init__(self, id: int, name: str)`;
  - `__repr__`;
  - `__eq__` и опционально `__hash__`.

То есть:

- dunder-методы (`__init__`, `__repr__`, `__eq__`, `__hash__`) **порождаются автоматически** на основе метаданных в `__annotations__`;
- это ещё один пример взаимодействия объектной модели, introspection и метапрограммирования.

---

## §51c. Полная таблица «оператор → метод» (справочник)
