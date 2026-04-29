[← Назад к индексу части XX](index.md)

## 3. Условные выражения и значения по умолчанию (§111)

### 3.0. Главная идея §111 (на пальцах)

Задача этого раздела: научиться писать «если нет нормального значения — возьми запасное»
так, чтобы код был:

- коротким;
- понятным;
- и **не ломался** на `0`, `''`, `False`.

Ключевая мысль:

> `or` работает по **truthiness** (истинность/ложность),  
> а `is None` работает по **отсутствию значения**.

### 3.1. `x = a or b` — «значение по умолчанию» через short‑circuit

Выражение:

```python
x = a or b
```

читается как:

> «Возьми `a`, если оно **истинно** (truthy), иначе возьми `b`».

Пример:

```python
user_input = ''
default_name = 'Anonymous'
name = user_input or default_name
print(name)  # 'Anonymous'
```

**Подводный камень:** `0`, `''`, `[]`, `False` — тоже считаются «ложными».

```python
count = 0
result = count or 10
print(result)  # 10 (вдруг вы этого не хотели)
```

Если вам нужно различать `0` и `None`, используйте явную проверку:

```python
x = 0
default = 10
value = x if x is not None else default  # здесь останется 0
```

---

### 3.1a. Очень важно: `or` возвращает НЕ True/False, а один из операндов

Это часто удивляет новичков.

```python
print([] or [1, 2, 3])     # [1, 2, 3]
print("hi" or "bye")       # hi
print(0 or 10)             # 10
print(None or "default")   # default
```

То есть `or` — это ещё и «оператор выбора значения».

А если вы хотите именно True/False, используйте `bool(...)`:

```python
value = []
print(bool(value))  # False
```

---

### 3.1b. Что считается falsy в Python (мини‑таблица) и почему это важно

**Falsy** (в `if not x`) считаются, например:

- `None`
- `False`
- `0`, `0.0`
- `''` (пустая строка)
- `[]`, `{}`, `set()` (пустые коллекции)

Примеры:

```python
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool([1]))    # True
```

**Почему так происходит (упрощённо):**

Когда Python делает `if x:`, он вызывает `bool(x)`.  
`bool(x)` смотрит:

1) есть ли у объекта `__bool__` (и что он возвращает);
2) если `__bool__` нет — смотрит `__len__` (длина 0 → False, иначе True).

Можно увидеть это на своём классе:

```python
class Box:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

print(bool(Box([])))     # False
print(bool(Box([1, 2]))) # True
```

**И главный вывод:**  
`x = a or b` выбирает `b` не только когда `a is None`, но и когда `a` просто falsy (например `0` или `''`).

### 3.2. Тернарный оператор: `x = a if condition else b`

Python‑эквивалент «условного оператора» в выражении:

```python
age = 20
status = 'adult' if age >= 18 else 'minor'
```

Важно:

- обязательно есть **ветка `else`** — выражение всегда что‑то возвращает;
- **не вкладывайте** один тернарный оператор в другой без крайней нужды.

Плохо:

```python
status = 'child' if age < 12 else 'teen' if age < 18 else 'adult'
```

Лучше так:

```python
if age < 12:
    status = 'child'
elif age < 18:
    status = 'teen'
else:
    status = 'adult'
```

Тернарный оператор хорош, когда:

- и `condition`, и оба выражения (`a` и `b`) **короткие**;
- логика легко читается «слева направо».

---

### 3.3. `dict.get`, `setdefault`, `pop` с default

**`dict.get(key, default=None)`**

```python
config = {'host': 'localhost'}
port = config.get('port', 5432)
```

- если ключ есть — вернётся его значение;
- если нет — вернётся `default`, **ключ не будет создан**.

**`dict.setdefault(key, default)`**

```python
groups = {}
user = 'alice'
groups.setdefault(user, []).append('admin')
```

- если `user` нет в словаре — создаётся запись `user: []`;
- возвращается список (новый или существующий), к которому мы сразу можем обращаться.

Очень важная тонкость: выражение `default` **вычисляется до вызова** `setdefault`.
То есть это:

```python
d.setdefault('k', expensive())
```

вызовет `expensive()` **всегда**, даже если `'k'` уже есть в `d`.

Если `default` дорогой, лучше:

```python
if 'k' not in d:
    d['k'] = expensive()
```

или использовать `collections.defaultdict`, если логика подходит.

**`dict.pop(key, default)`**

```python
data = {'token': 'abc', 'user': 'alice'}
token = data.pop('token', None)  # вытащили и удалили
```

- если ключ есть — он **удаляется** из словаря, а его значение возвращается;
- если нет — возвращается `default`, **ошибки нет**.

---

### 3.4. `next((x for x in items if cond), default)`

Идиома «найти первый элемент, удовлетворяющий условию»:

```python
users = [
    {'name': 'Alice', 'active': False},
    {'name': 'Bob', 'active': True},
    {'name': 'Carol', 'active': True},
]

first_active = next(
    (u for u in users if u['active']),
    None,
)

print(first_active)  # {'name': 'Bob', 'active': True}
```

Читается как:

> «Возьми первый `u`, для которого `u['active']` истинно,  
>  или верни `None`, если таких нет».

Плюсы:

- ленивый перебор, как только найден первый — генератор останавливается;
- аккуратная запись без явного цикла и `break`.

---

### 3.4a. Альтернатива: `next(filter(...), default)`

То же самое можно написать через `filter`.
Иногда это читается проще, особенно если предикат уже есть.

```python
xs = [0, 0, 5, 0]
first_non_zero = next(filter(bool, xs), None)
print(first_non_zero)  # 5
```

Идея:

- `filter(bool, xs)` оставляет только truthy‑элементы;
- `next(..., None)` берёт первый или возвращает `None`.

### 3.5. Запомните по §111

- `a or b` удобно для дефолтов, но не забывайте про `0`, `''`, `False`.
- Тернарный оператор хорош для **простых ветвлений**, а не для вложенных лесенок.
- `get`, `setdefault` и `pop(..., default)` позволяют элегантно работать с отсутствующими ключами.
- `next((...), default)` — прекрасный заменитель «цикла с `break`», когда нужен только первый результат.

---

