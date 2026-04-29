[← Назад к индексу части XIII](index.md)


Эта группа — набор **идиом и механизмов языка**, которые частично перекрывают классические паттерны или дают более удобные реализации.

### 7.1. Context manager (`with`)

Заменяет:

- паттерны Resource Acquisition Is Initialization (RAII),
- вручную написанные `try/finally` для ресурсов.

```python
with open("file.txt", "w") as f:
    f.write("hello")
```

Эквивалентно:

```python
f = open("file.txt", "w")
try:
    f.write("hello")
finally:
    f.close()
```

Свой менеджер контекста:

```python
class managed_file:
    def __init__(self, name: str):
        self._name = name
        self._f = None

    def __enter__(self):
        self._f = open(self._name, "w")
        return self._f

    def __exit__(self, exc_type, exc, tb):
        if self._f:
            self._f.close()
        # вернуть False, чтобы исключения не подавлялись
        return False
```

Реализует своего рода **Template Method** для работы с ресурсами.

---

### 7.2. Iterator / Generator

Генераторы — **питоничное воплощение паттерна Iterator**:

```python
def countdown(n: int):
    print("Start")
    while n > 0:
        yield n
        n -= 1
```

Преимущества:

- ленивые вычисления (экономия памяти);
- простой синтаксис `for` и `yield`.

Генераторные выражения:

```python
squares = (x * x for x in range(10))
```

Фактически: Strategy/Iterator в одной конструкции.

---

### 7.3. Декораторы функций

Декораторы функций — **частный случай структурного Decorator / Proxy**, реализованный на уровне функций.

```python
import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            duration = time.perf_counter() - start
            print(f"{func.__name__} took {duration:.3f}s")

    return wrapper
```

Применение:

```python
@timeit
def slow():
    ...
```

Типичные паттерны использования:

- кеширование (`functools.lru_cache`);
- валидация, логирование;
- контроль доступа.

---

### 7.4. Дескрипторы

**Дескриптор** — объект, который управляет доступом к атрибуту класса:

- методы `__get__`, `__set__`, `__delete__`.

`property` — частный случай дескриптора.

Простой дескриптор:

```python
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("must be >= 0")
        setattr(obj, self.private_name, value)


class Account:
    balance = Positive()

    def __init__(self, balance: int):
        self.balance = balance
```

Дескрипторы позволяют:

- реализовать «интеллектуальные» атрибуты;
- строить ORM, валидацию полей, ленивые свойства.

---

### 7.5. Monkey patching (осторожно)

**Идея:** менять поведение кода **во время выполнения**, подменяя атрибуты модулей/классов.

```python
import some_module


def fake_func(*args, **kwargs):
    return "fake"


some_module.real_func = fake_func
```

Где иногда оправдано:

- в тестах, когда нет DI/инверсии зависимостей;
- для временного обхода бага во внешней библиотеке.

Опасности:

- трудная отладка (поведение зависит от порядка импортов);
- сложно понять, где и почему функция была подменена.

**Рекомендация:** предпочитать:

- явное внедрение зависимостей (DIP, Strategy);
- стандартные инструменты мокинга (`unittest.mock`).

---

### 7.6. EAFP vs LBYL

**EAFP** — *Easier to Ask Forgiveness than Permission* («легче попросить прощения, чем разрешения»):

- идиома Python: **сначала пробуем сделать**, при ошибке — перехватываем исключение.

**LBYL** — *Look Before You Leap*:

- сначала всё проверяем, только потом делаем.

Пример LBYL:

```python
if key in d:
    value = d[key]
else:
    value = default
```

Пример EAFP:

```python
try:
    value = d[key]
except KeyError:
    value = default
```

В Python EAFP часто:

- короче;
- лучше работает в многопоточной/конкурентной среде (между проверкой и действием состояние может измениться).

Идиома EAFP — фактически поведенческий паттерн обработки ошибок:

- «пусть код бросит исключение, если что‑то не так»;
- вместо «напиши 10 проверок перед каждым действием».

---

## 8. Практические советы по применению паттернов
