[← Назад к индексу части XX](index.md)

## 5. Декораторы и обёртки (§113)

### 5.0. Главная идея §113 (на пальцах)

Декоратор — это «обёртка на функцию».
Как в жизни:

- есть «основная работа» (функция);
- есть «обвязка» вокруг неё: логирование, измерение времени, кеширование, проверки прав.

Самая простая модель:

> декоратор берёт `func` и возвращает `wrapper`, который внутри вызывает `func`.

---

### 5.0a. Как декоратор «переписывает» функцию (очень простая модель)

Когда вы пишете:

```python
@decorator
def f():
    ...
```

это почти то же самое, что написать вручную:

```python
def f():
    ...

f = decorator(f)
```

То есть имя `f` начинает указывать уже не на «старую» функцию, а на результат работы `decorator`.

---

### 5.0b. Порядок нескольких декораторов (очень важно запомнить)

```python
@A
@B
def f():
    ...
```

Читается так:

```python
f = A(B(f))
```

То есть ближайший к функции декоратор (`@B`) применяется первым.

### 5.1. `@functools.lru_cache` — мемоизация

`lru_cache` кеширует результаты функции по аргументам:

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # бесконечный кеш (по сути — memoize)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))  # быстро
```

Особенности:

- кешируется по **позиционным и именованным аргументам**;
- аргументы должны быть **hashable** (подходить для использования как ключи в словаре);
- не используйте для функций с **побочными эффектами** (запись в БД, сетевые вызовы).

---

### 5.1a. Практические детали `lru_cache`, которые важно знать новичку

#### 1) Кеш — это память, и она может «разрастись»

Если вы поставили `maxsize=None`, кеш может расти без ограничений:

- это ускоряет повторные вызовы,
- но может съесть много памяти, если входов очень много.

Если вы не уверены — начните с ограниченного кеша:

```python
@lru_cache(maxsize=1024)
def heavy(x):
    ...
```

#### 2) Можно посмотреть статистику кеша

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def f(x):
    return x * 2

f(1); f(1); f(2)
print(f.cache_info())
```

`cache_info()` покажет:

- сколько попаданий (hits),
- сколько промахов (misses),
- текущий размер кеша,
- maxsize.

#### 3) Кеш можно очистить

```python
f.cache_clear()
```

#### 4) Аргументы должны быть hashable (иначе будет TypeError)

Плохо:

```python
@lru_cache(maxsize=128)
def g(xs):         # xs может быть list (нехешируемый)
    return sum(xs)

g([1, 2, 3])       # TypeError: unhashable type: 'list'
```

Как исправлять (варианты):

- передавать `tuple(xs)` вместо `list`;
- или менять дизайн функции так, чтобы ключ кеша был хешируемым.

### 5.2. `@functools.wraps` — сохранение метаданных

При написании собственных декораторов:

```python
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args=} {kwargs=}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b
```

`@wraps(func)`:

- сохраняет `__name__`, `__doc__`, аннотации и другие атрибуты оригинальной функции;
- делает обёрнутую функцию более дружелюбной к отладчикам, интроспекции и документации.

**Правило:** если пишете декоратор — почти всегда добавляйте `@wraps`.

---

### 5.2a. Что ломается без `wraps` (короткая демонстрация)

Без `wraps` у вас часто получится «функция с именем wrapper», и это мешает:

- логам (в логах будет `wrapper`, а не `add`);
- документации/подсказкам;
- отладке и профилированию.

Пример без `wraps`:

```python
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def add(a, b):
    "Sum two numbers."
    return a + b

print(add.__name__)  # wrapper
print(add.__doc__)   # None
```

Теперь с `wraps`:

```python
from functools import wraps

def good_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def add(a, b):
    "Sum two numbers."
    return a + b

print(add.__name__)  # add
print(add.__doc__)   # Sum two numbers.
```

### 5.3. Декоратор с аргументами

Иногда декоратору нужны свои параметры:

```python
from functools import wraps

def repeat(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name: str):
    print(f"Hello, {name}!")
```

Структура:

- **наружная функция** `repeat(times)` принимает параметры декоратора;
- она возвращает **собственно декоратор** `decorator(func)`;
- декоратор возвращает **обёртку** `wrapper`.

---

### 5.4. `functools.partial` — фиксация аргументов

`partial` позволяет заранее «прибить гвоздями» часть аргументов:

```python
from functools import partial

def send_message(to, text, *, urgent=False):
    ...

send_to_admin = partial(send_message, 'admin@example.com')

send_to_admin("Server is down", urgent=True)
```

Плюсы:

- удобно передавать функции в качестве колбеков (например, в `map`, `sorted`, GUI‑handlers);
- уменьшает дублирование кода.

---

### 5.5. Запомните по §113

- `lru_cache` — простой способ ускорить чистые функции.
- `wraps` — обязательный элемент почти любого корректного декоратора.
- Декоратор с аргументами — это «функция, возвращающая декоратор».
- `partial` — инструмент для аккуратной подготовки функций к передаче куда‑то ещё.

---

