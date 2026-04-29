[← Назад к индексу части X](index.md)


### Ключевые методы

| Операция | Метод |
|----------|-------|
| `len(obj)` | `__len__` |
| `x in obj` | `__contains__` (иначе через `__iter__`) |
| `obj[i]` | `__getitem__` |
| `obj[i] = v` | `__setitem__` |
| `del obj[i]` | `__delitem__` |
| `for x in obj` | `__iter__` (fallback — `__getitem__`) |
| `reversed(obj)` | `__reversed__` (fallback — `__len__` + `__getitem__`) |
| оптимизация длинны | `__length_hint__` (используется `operator.length_hint`) |

### Пример: простая последовательность

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return reversed(self._items)  # итерация сверху вниз

    def __contains__(self, item):
        return item in self._items
```

Если вы хотите полноценный «списокоподобный» объект, можно наследоваться от абстракций в `collections.abc` (например, `MutableSequence`) и реализовывать минимальный набор методов, остальные будут сгенерированы.

#### Поддержка срезов в `__getitem__`

В `__getitem__(self, key)` параметр `key` может быть:

- целым числом (индекс);
- объектом `slice`;
- кортежем (для многомерной индексации, если вы так решите).

Пример: список с поддержкой срезов:

```python
class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def __getitem__(self, key):
        if isinstance(key, slice):
            # вернуть такой же тип, а не обычный list
            return SimpleList(self._items[key])
        return self._items[key]

    def __len__(self):
        return len(self._items)
```

Теперь:

```python
sl = SimpleList([1, 2, 3, 4])
print(sl[1])       # 2
print(sl[1:3])     # SimpleList([...])
```

#### Многомерные индексы через tuple

Если вы хотите поддерживать синтаксис `obj[x, y]`, Python передаст в `__getitem__` **кортеж**:

```python
key = (x, y)
obj.__getitem__((x, y))
```

Пример (упрощённая двумерная матрица):

```python
class Matrix:
    def __init__(self, rows):
        self._rows = rows  # список списков

    def __getitem__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            r, c = key
            return self._rows[r][c]
        raise TypeError("Use matrix[row, col]")
```

#### Как работает `in` и когда нужен `__contains__`

При выражении:

```python
item in obj
```

Python делает:

1. Если у `type(obj)` есть метод `__contains__(self, item)`, вызывает его.
2. Иначе пытается:
   - получить итератор `iter(obj)`;
   - последовательно сравнивать элементы через `==` до первого совпадения или конца.

Следствия:

- Если ваш контейнер может реализовать **быстрый поиск** (`O(1)` или `O(log n)`) — определение `__contains__` имеет смысл.
- Если у вас уже есть `__iter__`, но поиск по контейнеру всегда линейный — можно полагаться на fallback (но явный `__contains__` всё равно часто делает код более читаемым).

Пример с оптимизированным membership:

```python
class NameSet:
    def __init__(self, names):
        self._names = set(names)  # используем встроенное множество

    def __contains__(self, name):
        return name in self._names  # O(1) в среднем

    def __iter__(self):
        return iter(self._names)
```

---

## §46. Итераторы

### Протокол итерируемого объекта и итератора

- **Итерируемый объект** — реализует `__iter__`, который возвращает **итератор**.
- **Итератор** — реализует `__next__`, который:
  - возвращает следующий элемент;
  - поднимает `StopIteration`, когда элементы заканчиваются.

Часто объект является **и тем, и другим**: `__iter__` возвращает `self`.

#### Пример: конечный итератор

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for x in Countdown(3):
    print(x)  # 3 2 1
```

В реальном коде чаще используют **генераторы** (`yield`), но понимание протокола важно для работы с магическими методами.

### Одноразовость итераторов vs переиспользуемость итерируемых

Важно различать:

- **итератор** — объект, у которого `__iter__` возвращает `self`, и который «исчерпывается»;
- **итерируемый контейнер** — у которого каждый вызов `__iter__` возвращает **новый** итератор.

Пример проблемы:

```python
it = iter([1, 2, 3])
list(it)   # [1, 2, 3]
list(it)   # [] — уже исчерпан
```

Поэтому, когда вы проектируете свои классы:

- если это **контейнер** (список, дерево, коллекция) — `__iter__` должен возвращать **новый** итератор;
- если это сущность типа «поток событий» или «курсора БД» — он сам может быть итератором (одноразовым).

Пример контейнера:

```python
class Bag:
    def __init__(self, items):
        self._items = list(items)

    def __iter__(self):
        # каждый раз новый итератор
        return iter(self._items)
```

### Взаимодействие с генераторами

Генераторные функции:

```python
def gen():
    yield 1
    yield 2
```

создают объект, который реализует:

- `__iter__` (возвращаёт `self`);
- `__next__` (переход к следующему `yield`).

То есть генератор **является итератором**, и всё, что вы знаете про протокол итератора, к нему относится: он одноразовый, `StopIteration` сигнализирует о завершении и так далее.

---

## §47. Вызов (callable)

### Зачем нужен `__call__`

Метод `__call__(self, *args, **kwargs)` делает объекты **вызываемыми**:

```python
class Adder:
    def __init__(self, addend):
        self.addend = addend

    def __call__(self, x):
        return x + self.addend

add5 = Adder(5)
print(add5(10))  # 15
```

Типичные применения:

- конфигурируемые коллбеки и обработчики;
- объекты, имитирующие функции, но с внутренним состоянием;
- удобные API в DSL/фреймворках.

**Важно:** функции, методы, классы — тоже **callable**, но через свои механизмы (`function.__call__`, `type.__call__` и т.п.).

#### `obj()` — это синтаксический сахар для `obj.__call__(...)`

При выражении:

```python
result = obj(1, 2, key="v")
```

Python под капотом делает примерно:

```python
result = obj.__call__(1, 2, key="v")
```

Поэтому:

- вы можете обращаться к `__call__` напрямую (редко нужно, но полезно знать);
- любой объект с определённым `__call__` можно передавать как обычную функцию (`callback(obj)`).

#### Типичный паттерн: объект-конфигуратор функции

```python
class ThresholdFilter:
    def __init__(self, threshold):
        self.threshold = threshold

    def __call__(self, value):
        return value >= self.threshold

is_adult = ThresholdFilter(18)
print(list(filter(is_adult, [12, 18, 20])))  # [18, 20]
```

Здесь `ThresholdFilter` «оборачивает» значение порога, и сам объект становится функцией.

---

## §48. Контекстный менеджер

### Протокол `with`

Контекстный менеджер реализует:

- `__enter__(self)` — вызывается при входе в блок `with`; его результат — значение после `as` (если есть).
- `__exit__(self, exc_type, exc_val, exc_tb)` — вызывается при выходе (всегда, даже при исключении). Если возвращает **`True`**, исключение считается **обработанным** и подавляется.

#### Пример: простой таймер

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        print(f"elapsed: {self.elapsed:.3f}s")
        # не подавляем исключения
        return False

with Timer():
    time.sleep(0.1)
```

### `contextlib.contextmanager`

Удобный способ писать контекстные менеджеры **функциями**, но под капотом всё равно создаётся объект с `__enter__`/`__exit__`.

#### Семантика параметров `__exit__`

Под капотом блок:

```python
with manager as value:
    body
```

превращается (упрощённо) в:

```python
mgr = manager
value = mgr.__enter__()
try:
    body
except BaseException as exc:
    suppress = mgr.__exit__(type(exc), exc, exc.__traceback__)
    if not suppress:
        raise
else:
    mgr.__exit__(None, None, None)
```

Выводы:

- если исключения **не было**, `__exit__` вызывается с `(None, None, None)`;
- если было — получает **тип**, **экземпляр** и **traceback**;
- возвращаемое значение `True`/`False` решает, будет ли исключение **подавлено**.

#### Пример: подавлять только конкретный тип ошибки

```python
class IgnoreFileNotFound:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        return self.path

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is FileNotFoundError:
            print(f"файл {self.path} не найден, но это не критично")
            return True  # подавляем только этот тип
        return False      # остальные исключения не трогаем
```

#### `contextlib.contextmanager`: функция, преврашаемая в менеджер

```python
from contextlib import contextmanager

@contextmanager
def open_utf8(path, mode="r"):
    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()
```

Здесь декоратор автоматически создаёт объект с `__enter__`/`__exit__`, который реализует тот же протокол, что и ручная реализация.

---

## §49. Числовые протоколы
