[← Назад к индексу части XI](index.md)


### Цель раздела

Чётко понять, что значит «объект hashable», **какие именно** типы hashable, а какие нет, и почему — с точки зрения мутабельности и контракта. Научиться проверять hashable «на глаз» и понимать граничные случаи.

### Термины

| Термин | Определение |
|--------|-------------|
| **Hashable** | Объект, который можно использовать как ключ dict или элемент set: у него есть стабильный хеш и определённое равенство. |
| **Контракт hashable** | Два условия: (1) `hash(a)` не меняется за время жизни объекта; (2) если `a == b`, то `hash(a) == hash(b)`. |
| **Immutable** (неизменяемый) | Объект, состояние которого нельзя изменить после создания. Как правило, такие объекты hashable. |
| **Маркер «пустой слот»** | Во внутренней структуре dict значение хеша `-1` (или аналогичное) может означать «слот пуст»; поэтому `hash(-1)` в Python возвращает `-2`. |

### Правила и синтаксис

**Объект hashable, если:**

1. `hash(obj)` не меняется, пока объект живёт.
2. `a == b` влечёт `hash(a) == hash(b)` (обратное не обязательно: разные объекты могут иметь одинаковый хеш — коллизия).
3. `hash(obj)` не бросает исключение.

**Обратная импликация не требуется:** `hash(a) == hash(b)` **не** влечёт `a == b`. Разные объекты могут иметь одинаковый хеш (коллизия).

### Полный перечень: hashable типы

| Тип | Hashable? | Примечание |
|-----|-----------|------------|
| `int` | ✅ | Включая большие int |
| `float` | ✅ | `nan` — особый случай: `nan != nan`, но `hash(nan)` определён |
| `complex` | ✅ | По действительной и мнимой частям |
| `str` | ✅ | |
| `bytes` | ✅ | |
| `tuple` | ✅* | *Только если **все** элементы hashable |
| `frozenset` | ✅* | *Только если все элементы hashable |
| `None` | ✅ | |
| `bool` | ✅ | Подкласс int |
| `range` | ✅ | Хеш по start, stop, step; `hash(range(0, 10, 2))` |
| `slice` | ✅ | `hash(slice(1, 10, 2))` — определён; хеш по start, stop, step |
| `type` (классы) | ✅ | Хеш по id (класс как объект) |
| `types.FunctionType` | ✅ | Функции hashable (хеш по id) |
| `types.BuiltinFunctionType` | ✅ | |
| `enum.Enum` | ✅ | Enum-члены hashable по умолчанию |
| `decimal.Decimal` | ✅ | Неизменяемый |
| `fractions.Fraction` | ✅ | Неизменяемый |
| `datetime.date`, `datetime.time`, `datetime.datetime`, `datetime.timedelta` | ✅ | При условии, что `tzinfo` hashable (или None). `datetime.timezone.utc` — hashable. `zoneinfo.ZoneInfo` — hashable. |
| `Ellipsis` | ✅ | Синглтон, `hash(...)` определён |
| `ipaddress` объекты | ✅ | IPv4Address, IPv6Address и др. |
| `pathlib.PurePath` | ✅ | |
| `uuid.UUID` | ✅ | Неизменяемый |
| `object` (пользовательский) | ✅** | **По умолчанию хеш по `id`; если переопределён `__eq__` без `__hash__` — не hashable |
| `types.NoneType` | ✅ | То же, что `None` |

### Не hashable типы

| Тип | Почему не hashable |
|-----|--------------------|
| `list` | Мутабельный |
| `dict` | Мутабельный |
| `set` | Мутабельный |
| `bytearray` | Мутабельный (изменяемая последовательность байт; аналог list для байт — стабильный хеш невозможен) |
| `memoryview` | Мутабельный вид на память |
| `array.array` | Мутабельный |
| `collections.deque` | Мутабельный |
| Класс с `__eq__` и без `__hash__` | Python ставит `__hash__ = None` |
| Класс с `__hash__ = None` | Явно помечен как не hashable |

### Почему tuple hashable, а list нет: разбор по шагам

Рассмотрим сценарий «если бы list был hashable»:

1. **Хеш по id:** тогда `a = [1, 2]`, `b = [1, 2]` — `a == b` (True), но `id(a) != id(b)` ⇒ `hash(a) != hash(b)`. Нарушение контракта: равные объекты должны иметь одинаковый хеш.

2. **Хеш по содержимому:** тогда `a = [1, 2]`, добавляем `a` в set. Потом `a.append(3)`. Хеш `a` изменился, но объект уже лежит в set по старому индексу. Поиск `a in s` идёт по новому хешу → не найдёт. Объект «потерялся».

3. **Вывод:** для hashable нужна стабильность хеша. Мутабельный объект не может гарантировать стабильность (содержимое меняется). Tuple неизменяем — хеш можно вычислить один раз и он не изменится.

### Проверка: как узнать, hashable ли объект

```python
def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

is_hashable([1, 2])      # False
is_hashable((1, 2))      # True
is_hashable(frozenset()) # True
is_hashable({"a": 1})    # False
```

### Граничные случаи

#### tuple с вложенными структурами

```python
hash((1, 2))       # OK
hash((1, [2]))     # TypeError: unhashable type: 'list'
hash((1, (2, [3])))  # TypeError — вложенный list
hash((1, {}))      # TypeError: unhashable type: 'dict'
```

#### frozenset с frozenset

```python
hash(frozenset({frozenset({1, 2}), frozenset({3})}))  # OK — вложенные frozenset hashable
```

#### Enum

```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
hash(Color.RED)   # OK — Enum-члены hashable
{Color.RED: "красный"}  # OK
```

#### Decimal и Fraction

```python
from decimal import Decimal
from fractions import Fraction
hash(Decimal("3.14"))   # OK
hash(Fraction(1, 3))    # OK
{Decimal("0.1"): 1}     # OK
```

**Дополнительно:** Decimal и Fraction неизменяемы; хеш вычисляется по числовому значению. Равные значения дают равный хеш. Для Decimal с разной точностью (`Decimal("1.0")` и `Decimal("1.00")`) — при `Decimal("1.0") == Decimal("1.00")` (True) хеши обязаны совпадать; CPython хеширует по *нормализованному* числовому значению, поэтому оба дают один хеш. Точность хранения (trailing zeros) не влияет на хеш. Для Fraction: `Fraction(1, 2) == Fraction(2, 4)` ⇒ `hash(Fraction(1, 2)) == hash(Fraction(2, 4))` (стандартная реализация это гарантирует).

#### datetime, timezone и zoneinfo

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# tzinfo=None — hashable
hash(datetime(2025, 2, 10))  # OK
{datetime(2025, 2, 10): "сегодня"}  # OK

# timezone.utc — hashable
dt_utc = datetime(2025, 2, 10, tzinfo=timezone.utc)
hash(dt_utc)  # OK
{dt_utc: 1}   # OK

# ZoneInfo — hashable (Python 3.9+)
dt_tz = datetime(2025, 2, 10, tzinfo=ZoneInfo("Europe/Moscow"))
hash(dt_tz)   # OK
{dt_tz: 1}    # OK
```

**Важно:** хеш `datetime` зависит от tzinfo. Два datetime с разным tzinfo, но представляющие один момент времени, имеют разные хеши (и не равны по `==` в общем случае). `datetime(2025, 2, 10, 12, 0, tzinfo=timezone.utc)` и `datetime(2025, 2, 10, 15, 0, tzinfo=ZoneInfo("Europe/Moscow"))` — один момент, но разные объекты. Если tzinfo — кастомный класс, он должен быть hashable; иначе `hash(datetime(...))` даст `TypeError`.

#### Классы и функции (хеш по id)

```python
hash(str)         # OK — класс hashable
hash(len)         # OK — функция hashable
d = {str: "string type", len: "builtin"}  # OK
```

**Важно:** для классов и функций хеш основан на `id` — объектной идентичности. Два разных объекта (разные функции) всегда имеют разный id и разный хеш, даже если «содержимое» совпадает. Контракт выполняется: `a == b` (то же объект) ⇒ `hash(a) == hash(b)`.

#### dataclass

```python
from dataclasses import dataclass

@dataclass
class C:
    x: int
# C не hashable по умолчанию (есть __eq__, __hash__ не определён автоматически)
# hash(C(1))  # TypeError, т.к. dataclass с __eq__ и без frozen не получает __hash__

@dataclass(frozen=True)
class D:
    x: int
# frozen=True добавляет __hash__ по полям
hash(D(1))  # OK
```

### Примеры

```python
# Hashable
assert hash(1) == hash(1)
assert hash("a") == hash("a")
t = (1, 2)
assert hash(t) == hash((1, 2))
assert hash(frozenset([1, 2])) == hash(frozenset([2, 1]))  # frozenset хешируется по содержимому

# Не hashable
try:
    hash([1, 2])
except TypeError as e:
    print(e)  # unhashable type: 'list'

try:
    hash({1, 2})
except TypeError as e:
    print(e)  # unhashable type: 'set'

# tuple с не-hashable элементом — тоже не hashable
try:
    hash((1, [2]))
except TypeError as e:
    print(e)  # unhashable type: 'list'

# Почему tuple hashable, а list нет
# tuple неизменяем — после создания нельзя изменить элементы.
# Значит, hash(tuple) можно вычислить один раз и он не изменится.
# list можно изменить — hash(list) менялся бы, что нарушило бы контракт.
```

### Теоретическое подтверждение

**Почему мутабельность несовместима с hashable:**

Если бы `list` был hashable:

1. `a = [1, 2]`, `b = [1, 2]` — `a == b` ⇒ `hash(a) == hash(b)`.
2. Добавляем `a` в `set`: `s = {a}`.
3. Меняем `a`: `a.append(3)`.
4. Теперь `a` уже не равен `[1, 2]`, но его хеш не меняется (если бы хеш был по id — тогда `a` и `b` имели бы разные хеши при равенстве, что нарушает контракт).
5. Если хеш по содержимому — после изменения содержимого хеш должен был бы измениться, но объект уже лежит в `set` по старому индексу. Поиск `a in s` дал бы неверный результат.

**Вывод:** мутабельные объекты не могут быть hashable без нарушения контракта. Неизменяемость — необходимое условие (при хеше по содержимому).

### Плохой vs хороший пример: класс с __eq__

**Плохо:**
```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
# Python 3 автоматически ставит __hash__ = None
p1, p2 = Point(1, 2), Point(1, 2)
s = {p1}   # OK — p1 hashable по умолчанию? Нет!
# TypeError: unhashable type: 'Point'
```

**Почему плохо:** переопределён `__eq__`, но не `__hash__`. Python 3 обнуляет хеш; объект перестаёт быть hashable.

**Хорошо (вариант 1 — hashable):**
```python
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))  # те же поля, что в __eq__
# Point immutable по смыслу — поля не меняются
s = {Point(1, 2), Point(1, 2)}
len(s)  # 1
```

**Хорошо (вариант 2 — не hashable):**
```python
class MutablePoint:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __eq__(self, other):
        return isinstance(other, MutablePoint) and self.x == other.x and self.y == other.y
    __hash__ = None  # явно: не hashable
```

### Пошагово: что происходит при добавлении ключа в dict

1. Вычисляется `h = hash(key)`.
2. По хешу определяется индекс в массиве indices: `i = h & (size - 1)`.
3. Проверяется слот `indices[i]`: пуст — запись создаётся; занят — проверяется `key == entries[idx].key`.
4. При совпадении ключа — обновление значения.
5. При коллизии (ключ другой) — perturb: сдвиг h, новый индекс, повтор.
6. При вставке новая запись добавляется в конец entries (сохранение порядка вставки).

### Связь __hash__ с __eq__: полная картина

| Ситуация | __eq__ | __hash__ | Результат |
|----------|--------|----------|-----------|
| Класс по умолчанию (наследник object) | Сравнение по `id` | Хеш по `id` | Hashable; каждый объект уникален |
| Переопределён только `__eq__` | Кастомное | Python 3 ставит `__hash__ = None` | **Не hashable** |
| Переопределены `__eq__` и `__hash__` согласованно | По полям | По тем же полям | Hashable, если объект immutable |
| Явно `__hash__ = None` | Любой | None | Не hashable |
| `__eq__` не переопределён, `__hash__` переопределён | По id | Кастомный | Возможна ошибка: равные по id объекты будут иметь разный хеш, если `__hash__` не согласован с id |

**Важно:** при переопределении `__eq__` вы **обязаны** решить вопрос хеширования. Либо определяете `__hash__` по тем же полям, что и `__eq__` (и объект должен быть immutable), либо ставите `__hash__ = None`. Иначе Python 3 автоматически обнулит хеш.

### Когда hashable нужен на практике

- Ключи `dict`
- Элементы `set`
- Элементы `frozenset`
- Аргументы `functools.lru_cache` (должны быть hashable)
- Ключи `weakref.WeakKeyDictionary`
- Элементы `weakref.WeakSet`
- Группировка и подсчёт: `Counter`, `defaultdict` (ключи hashable)
- Классы, которые кладут экземпляры в set/dict — поля в `__eq__`/`__hash__`

### Запомните

> **Tuple hashable, list нет** — из-за неизменяемости. Хеш должен быть стабильным; для мутабельного объекта это невозможно без поломки семантики `dict`/`set`. Проверка: `hash(obj)` не бросает `TypeError` ⇒ объект hashable.

---

## 54. Хеш-таблицы (dict, set)
