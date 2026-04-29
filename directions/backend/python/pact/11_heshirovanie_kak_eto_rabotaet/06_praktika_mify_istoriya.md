[← Назад к индексу части XI](index.md)


### Задача 1: Сделать список уникальных кортежей (дедупликация)

```python
# Дан список кортежей; нужно убрать дубликаты, сохранив порядок
pairs = [(1, 2), (2, 1), (1, 2), (3, 4)]
seen = set()
result = []
for p in pairs:
    if p not in seen:
        seen.add(p)  # p должен быть hashable — tuple hashable
        result.append(p)
# result = [(1, 2), (2, 1), (3, 4)]
```

### Задача 2: Группировка по ключу (list в качестве ключа — нельзя)

```python
# Плохо: list не hashable
# groups = {}
# for item in items:
#     key = [item.category, item.type]  # list!
#     groups.setdefault(key, []).append(item)  # TypeError

# Хорошо: использовать tuple
groups = {}
for item in items:
    key = (item.category, item.type)  # tuple — hashable
    groups.setdefault(key, []).append(item)
```

### Задача 3: Кеширование функции с list-аргументом

```python
from functools import lru_cache

# Плохо:
# @lru_cache(maxsize=128)
# def process(items: list):  # list не hashable!
#     return sum(items)

# Хорошо: преобразовать в tuple при вызове
@lru_cache(maxsize=128)
def _process_cached(items_tuple):
    return sum(items_tuple)

def process(items: list):
    return _process_cached(tuple(items))
```

### Задача 4: Создать set из объектов пользовательского класса

```python
# Класс должен быть hashable: либо не переопределять __eq__, либо определить согласованный __hash__
@dataclass(frozen=True)
class Key:
    a: int
    b: str
# frozen=True даёт __hash__ автоматически

keys = {Key(1, "x"), Key(2, "y"), Key(1, "x")}
len(keys)  # 2 — дубликат (1, "x") отфильтрован
```

### Задача 5: «Уникальные» объекты по содержимому (интернирование)

```python
# Иногда нужно кешировать объекты по содержимому — один «канонический» экземпляр на каждое уникальное значение
cache = {}
def intern(obj):
    """Вернуть канонический экземпляр для obj (obj должен быть hashable)."""
    if obj not in cache:
        cache[obj] = obj
    return cache[obj]
# Использование: canonical = intern(MyClass(1, 2))  # MyClass должен быть hashable
```

### Задача 6: Дедупликация с сохранением порядка (для unhashable)

Если элементы не hashable (например, list), нельзя использовать set. Альтернатива — перебор с проверкой `in` по уже добавленным (O(n²)) или приведение к hashable-представлению:

```python
# Элементы — списки; нужна дедупликация
lists = [[1, 2], [2, 1], [1, 2]]
seen = set()
result = []
for lst in lists:
    t = tuple(lst)  # tuple hashable
    if t not in seen:
        seen.add(t)
        result.append(lst)
# result = [[1, 2], [2, 1]]
```

### Задача 7: Составной ключ из нескольких полей

```python
# Нужен ключ (user_id, timestamp, action_type)
# Вариант 1: tuple — порядок важен
key = (user_id, timestamp, action_type)
cache[key] = result

# Вариант 2: NamedTuple — явная семантика
from typing import NamedTuple
class CacheKey(NamedTuple):
    user_id: int
    timestamp: float
    action_type: str
key = CacheKey(1, 1234567890.0, "click")
cache[key] = result  # CacheKey hashable, т.к. наследует tuple
```

### Задача 8: Обход «unhashable» при lru_cache с несколькими аргументами

```python
from functools import lru_cache

@lru_cache(maxsize=256)
def process(items_tuple: tuple, options_tuple: tuple):
    items = list(items_tuple)
    options = dict(options_tuple)
    # ... логика
    return result

# Вызов: преобразовать list и dict в tuple
process(tuple([1, 2, 3]), tuple({"a": 1}.items()))
```

### Задача 9: dict.fromkeys vs цикл с set — когда что

```python
# dict.fromkeys(seq) — дедупликация с сохранением порядка (первого вхождения)
# Ключи должны быть hashable
keys = ["a", "b", "a", "c", "b"]
d = dict.fromkeys(keys)  # {'a': None, 'b': None, 'c': None}
list(d)  # ['a', 'b', 'c'] — порядок сохранён

# set(keys) — порядок теряется
set(keys)  # {'a', 'b', 'c'} — порядок не гарантирован

# Если нужны значения — цикл с set
result = []
seen = set()
for k in keys:
    if k not in seen:
        seen.add(k)
        result.append((k, compute_value(k)))
```

### Задача 10: Хешируемый «снимок» изменяемого объекта

Если нужен ключ, отражающий текущее состояние мутабельного объекта, создайте неизменяемое представление:

```python
# Для dict: tuple(sorted(d.items())) — если ключи и значения hashable
d = {"a": 1, "b": 2}
snapshot = tuple(sorted(d.items()))  # (('a', 1), ('b', 2))
cache[snapshot] = result
# Внимание: при изменении d snapshot не обновится — это «моментальный снимок»
```

---

## Частые заблуждения

| Заблуждение | Реальность |
|-------------|------------|
| «Хеш — уникальный идентификатор объекта» | Хеш не обязан быть уникальным; коллизии допустимы. Важно: равные объекты → одинаковый хеш. |
| «hash() и hashlib — одно и то же» | Нет. `hash()` — для dict/set, не для криптографии. hashlib — криптографические хеши. |
| «Можно положить list в set, если не менять его» | Нет. list не hashable в принципе; попытка `{[]}` вызовет TypeError. |
| «Порядок в set детерминирован» | Нет. Порядок set не гарантирован; зависит от хешей и истории. |
| «При PYTHONHASHSEED=0 все хеши воспроизводимы» | Частично. str, bytes, datetime — да. int, float, tuple — и так детерминированы. |
| «Коллизия — ошибка в коде» | Нет. Коллизии неизбежны (принцип Дирихле); хеш-таблица обязана их обрабатывать. |
| «Если a != b, то hash(a) != hash(b)» | Неверно. Разные объекты могут иметь одинаковый хеш (коллизия). Требуется только: a == b ⇒ hash(a) == hash(b). |
| «Хеш объекта не меняется между запусками» | Для str/bytes — зависит от PYTHONHASHSEED. Для int, float, tuple — детерминирован. |
| «dict.fromkeys(keys) сохраняет порядок» | Да (Python 3.7+). Ключи должны быть hashable. |

---

## История и эволюция (Python 2 → 3, PEP)

| Версия/ PEP | Изменение |
|-------------|-----------|
| **Python 2** | str и int хешировались предсказуемо; уязвимость к hash-flooding DoS. |
| **PEP 456** (Python 3.4) | SipHash для str, bytes, datetime; PYTHONHASHSEED; защита от DoS. |
| **Python 3** | Классы с `__eq__` и без `__hash__` автоматически получают `__hash__ = None`. |
| **Python 3.6** | dict сохраняет порядок вставки (деталь реализации). |
| **Python 3.7** | Порядок вставки dict — гарантия языка. |

### Сводная таблица: когда что использовать

| Задача | Использовать | Не использовать |
|--------|--------------|-----------------|
| Быстрый поиск по ключу | dict, set | list с перебором |
| Кеш по аргументам функции | lru_cache (аргументы hashable) | Глобальный dict с list-ключами |
| Дедупликация с сохранением порядка | dict.fromkeys(seq) (3.7+) или цикл с set | set(seq) — порядок теряется |
| Криптографический хеш (пароль, файл) | hashlib.sha256, hashlib.blake2b | hash() |
| Ключ для weakref | hashable объект | list, dict |
| Составной ключ | tuple, NamedTuple, frozenset | list, dict |

---

## Справочник и проверка
