[← Назад к индексу части XI](index.md)


### Цель раздела

Понять связь слабых ссылок (`weakref`) с хешированием: почему для `WeakKeyDictionary` и `WeakSet` ключи/элементы должны быть **hashable**, и что происходит, когда объект-ключ удаляется.

### Термины

| Термин | Определение |
|--------|-------------|
| **Weakref** (слабая ссылка) | Ссылка, которая не увеличивает счётчик ссылок объекта; объект может быть собран GC, если нет других сильных ссылок. |
| **WeakKeyDictionary** | Словарь, где ключи хранятся как слабые ссылки; при сборке ключа запись автоматически удаляется. |
| **WeakValueDictionary** | Словарь, где значения — слабые ссылки; при сборке значения запись удаляется. |
| **WeakSet** | Множество элементов, хранимых как слабые ссылки; при сборке элемента он исчезает из множества. |
| **__weakref__** | Слот в объекте для хранения слабых ссылок на него; если класс определяет `__slots__`, для weakref нужно явно добавить `__weakref__`. |

### Правила и синтаксис

1. **WeakKeyDictionary:** ключи должны быть **hashable** и поддерживать слабые ссылки (большинство пользовательских классов — да). Внутри — хеш-таблица по ключам; при обращении `d[key]` используется `hash(key)` для поиска.
2. **WeakValueDictionary:** ключи — обычные (hashable); значения — слабые ссылки. Ключи должны быть hashable (внутри используется обычный dict по ключам). Значения — объекты, поддерживающие weakref. При сборке значения запись удаляется; ключ при этом может быть любым hashable-типом.
3. **WeakSet:** элементы должны быть **hashable** и поддерживать weakref.
4. **Не поддерживают weakref:** встроенные типы (list, dict, int, str и т.д.) в большинстве случаев не поддерживают weakref; `weakref.ref(42)` или `weakref.ref([1,2])` вызовет ошибку.

### Почему нужен hashable для WeakKeyDictionary и WeakSet

Внутренняя структура `WeakKeyDictionary` — по сути словарь, где ключи — слабые ссылки на объекты. Для быстрого поиска «по ключу» нужен хеш: `hash(key)` используется для индексации. Без hashable ключа невозможна работа хеш-таблицы. Аналогично `WeakSet` — множество требует hashable элементов.

### Примеры

```python
import weakref

class C:
    pass

# WeakKeyDictionary: ключи — объекты с weakref
obj = C()
d = weakref.WeakKeyDictionary()
d[obj] = "value"
print(len(d))  # 1
del obj
# После удаления obj запись исчезнет (при сборке мусора)
import gc
gc.collect()
print(len(d))  # 0

# list нельзя использовать как ключ: 1) не hashable, 2) не поддерживает weakref
try:
    d[[1, 2]] = 1
except TypeError as e:
    print(e)  # cannot create weak reference to 'list' object

# WeakSet — элементы должны быть hashable
ws = weakref.WeakSet()
c = C()
ws.add(c)
print(len(ws))  # 1
del c
gc.collect()
print(len(ws))  # 0
```

### Почему встроенные типы (int, str) не поддерживают weakref

`weakref.ref(42)` и `weakref.ref("hello")` вызывают `TypeError: cannot create weak reference to 'int' object`. Причины: (1) встроенные типы реализованы на C и могут не иметь слота для хранения слабых ссылок; (2) мелкие int и некоторые строки интернированы — они живут всё время работы интерпретатора, слабые ссылки на них мало осмыслены. Для weakref нужны пользовательские объекты (экземпляры своих классов) или специальные типы.

### Связь с __slots__

Если класс определяет `__slots__` и вы хотите использовать его в `WeakKeyDictionary` или `WeakSet`, нужно добавить `__weakref__` в слоты:

```python
class C:
    __slots__ = ('x', '__weakref__')  # __weakref__ обязателен для weakref
```

### Запомните

> **WeakKeyDictionary** и **WeakSet** требуют hashable-ключи/элементы, потому что внутри используется хеш-таблица. Плюс объекты должны поддерживать weakref (пользовательские классы — по умолчанию поддерживают; при `__slots__` нужен `__weakref__`).

---

## 57. Кастомный __hash__

### Цель раздела

Научиться правильно определять `__hash__` в своих классах: когда это нужно, когда — нет, как не нарушить контракт, и как это связано с `dataclass`, `NamedTuple`, `functools.lru_cache`.

### Термины

| Термин | Определение |
|--------|-------------|
| **__hash__** | Магический метод; вызывается при `hash(obj)`. Должен возвращать `int`. |
| **__hash__ = None** | Явно пометить класс как не hashable; экземпляры нельзя класть в set/dict. |
| **Кеширование хеша** | Сохранение вычисленного хеша в поле объекта (для неизменяемых объектов), чтобы не пересчитывать при повторных вызовах. |

### Правила и синтаксис

1. **Если переопределяете `__eq__`:** нужно либо переопределить `__hash__` согласованно с `__eq__`, либо установить `__hash__ = None` (тогда объект не hashable). Иначе Python 3 сам поставит `__hash__ = None` для классов с кастомным `__eq__`.
2. **Контракт:** если `a == b`, то `hash(a) == hash(b)`.
3. **Практика:** хешируйте **те же поля**, что участвуют в `__eq__`. Стандартный приём: `return hash((self.field1, self.field2, ...))`.
4. **Immutable:** кастомный hashable-класс должен быть логически неизменяемым (поля, участвующие в `__eq__`/`__hash__`, не меняются после создания).

### Когда Python автоматически даёт __hash__

- **object:** по умолчанию `__hash__` основан на `id(obj)` — каждая сущность имеет свой хеш.
- **При наследовании:** если вы переопределяете `__eq__` и не определяете `__hash__`, Python устанавливает `__hash__ = None` (начиная с Python 3).
- **frozen dataclass:** `@dataclass(frozen=True)` автоматически генерирует `__hash__` по полям.
- **NamedTuple:** `__hash__` наследуется от tuple (если все поля hashable).
- **Enum:** члены Enum имеют `__hash__` по умолчанию.

### Паттерны реализации __hash__

#### 1. Хеш из кортежа полей (рекомендуемый шаблон)

```python
def __hash__(self):
    return hash((self.x, self.y, self.z))
```

Подходит для любого набора hashable-полей. Порядок полей должен совпадать с `__eq__`. Этот паттерн — наиболее распространённый и читаемый.

**Шаблон для класса с несколькими полями:**
```python
def __eq__(self, other):
    if not isinstance(other, type(self)):
        return NotImplemented
    return (self.a, self.b, self.c) == (other.a, other.b, other.c)

def __hash__(self):
    return hash((self.a, self.b, self.c))
```

#### 2. XOR-комбинация (для множеств)

Если семантика «множества» (порядок не важен), можно использовать XOR. Осторожно: `hash(a) ^ hash(b) ^ hash(b) == hash(a)` — дубликаты «исчезают». Для tuple-like объектов лучше `hash((...))`.

#### 2a. Антипаттерн: __hash__ возвращает константу

```python
class Bad:
    def __eq__(self, other):
        return isinstance(other, Bad)
    def __hash__(self):
        return 42  # ВСЕ экземпляры дают один хеш!
```

Технически контракт не нарушен: равные объекты (по `__eq__` все Bad равны) имеют один хеш. Но **все** разные объекты тоже имеют один хеш — сплошная коллизия. `{Bad(), Bad(), Bad()}` — три вставки в один и тот же слот; поиск вырождается в O(n). **Не делайте так.**

#### 3. Кеширование хеша (для тяжёлых вычислений)

Если вычисление хеша дорогое и объект immutable, можно кешировать:

```python
def __hash__(self):
    if not hasattr(self, '_hash'):
        object.__setattr__(self, '_hash', hash((self.x, self.y)))
    return self._hash
```

Для frozen dataclass с `__slots__` или при использовании `__getattribute__` нужно аккуратно обращаться к полю кеша.

### dataclass и hash

```python
from dataclasses import dataclass

# Без frozen — нет __hash__, не hashable
@dataclass
class A:
    x: int
# hash(A(1))  # TypeError

# frozen=True — __hash__ генерируется автоматически по полям
@dataclass(frozen=True)
class B:
    x: int
hash(B(1))  # OK

# unsafe_hash=True — генерировать __hash__ по полям даже без frozen (осторожно: объект должен быть immutable)
# hash=False — явно отключить __hash__ (сделать не hashable)
```

### Наследование и __hash__

При наследовании от класса с переопределённым `__eq__` и `__hash__`:

- Подкласс **наследует** `__hash__` и `__eq__`; если поля те же — всё работает.
- Если подкласс добавляет поля в `__eq__`, нужно переопределить `__hash__`, включив новые поля: иначе нарушение контракта (равные объекты подкласса могут иметь разный хеш).
- При наследовании от класса с `__hash__ = None` подкласс тоже не hashable, пока явно не определит `__hash__`.

```python
class Base:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return isinstance(other, Base) and self.x == other.x
    def __hash__(self):
        return hash(self.x)

class Derived(Base):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
    def __eq__(self, other):
        return isinstance(other, Derived) and self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))  # нужно переопределить — добавили y в __eq__
```

### dataclass: field(hash=...) — исключение поля из хеша

Для frozen dataclass можно исключить отдельные поля из `__hash__` и `__eq__`:

```python
from dataclasses import dataclass, field

@dataclass(frozen=True)
class C:
    id: int
    name: str
    _cache: str = field(default="", compare=False, hash=False)  # не участвует в __eq__ и __hash__
```

### functools.lru_cache и hashable

`lru_cache` кеширует результаты по аргументам. Аргументы выступают ключами во внутреннем dict, значит **все аргументы должны быть hashable**:

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive(a: int, b: tuple):
    return a + sum(b)

expensive(1, (2, 3))  # OK — int и tuple hashable
# expensive(1, [2, 3])  # TypeError: unhashable type: 'list'
```

Для list/dict в аргументах нужно преобразовать в tuple/frozenset **до** вызова кешируемой функции. Пример: внутренняя функция принимает `tuple(lst)`, внешняя — `list`; вызывающий передаёт `tuple(items)` в кешируемую обёртку. Важно: преобразование должно давать одинаковый hashable для семантически равных входов: `tuple(sorted(d.items()))` для dict, `tuple(lst)` для list.

### Примеры

```python
# Правильно: __eq__ и __hash__ согласованы
class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)
assert p1 == p2
assert hash(p1) == hash(p2)
s = {p1, p2}
assert len(s) == 1

# Не hashable: __hash__ = None
class MutablePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if not isinstance(other, MutablePoint):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    __hash__ = None

# NamedTuple — hashable
from typing import NamedTuple
class NP(NamedTuple):
    x: int
    y: int
hash(NP(1, 2))  # OK
```

### Чек-лист при реализации __hash__

- [ ] Определяю `__hash__` только если определён `__eq__` и объект должен быть hashable.
- [ ] Хеширую **те же** поля, что участвуют в `__eq__` (и в том же порядке для tuple).
- [ ] Возвращаю `int`; не возвращаю `None`, `float` или другой тип.
- [ ] Объект **неизменяем** (поля, участвующие в `__eq__`/`__hash__`, не меняются после создания).
- [ ] Если объект мутабельный — ставлю `__hash__ = None`.

### Плохо vs лучше

| Плохо | Лучше |
|-------|-------|
| Переопределить `__eq__` и не трогать `__hash__` | Либо согласованный `__hash__`, либо `__hash__ = None` |
| Хешировать поля, не участвующие в `__eq__` | Хешировать те же поля, что в `__eq__` |
| Менять поля после добавления в set/dict | Делать объект immutable для полей, участвующих в `__eq__`/`__hash__` |
| Передавать list в lru_cache | Преобразовать в tuple или другой hashable |
| `return hash(self.id)` при `__eq__` по (id, name) | `return hash((self.id, self.name))` |

### Запомните

> **При переопределении `__eq__`** обязательно решите: либо определяете согласованный `__hash__` (и объект immutable), либо ставите `__hash__ = None`. Хешируйте те же поля, что в `__eq__`. `lru_cache` и weakref требуют hashable аргументы/ключи.

---

## 57a. Детерминированность и хеш-рандомизация
