[← Назад к индексу части X](index.md)


### Основные группы методов

| Операция | Методы |
|----------|--------|
| Бинарные арифметические | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__` |
| Обратные (right-hand) | `__radd__`, `__rsub__`, `__rmul__`, ... |
| In-place | `__iadd__`, `__isub__`, `__imul__`, ... (`+=`, `-=`, ...) |
| Унарные | `__neg__`, `__pos__`, `__abs__`, `__invert__` |
| Преобразования | `__int__`, `__float__`, `__complex__`, `__index__` |
| Округление | `__round__`, `__trunc__`, `__floor__`, `__ceil__` |

Числовые протоколы позволяют вашим объектам:

- участвовать в **арифметических выражениях** вместе с числами и друг другом;
- корректно конвертироваться в `int`/`float`/`complex` и использоваться там, где ожидается целое число (`range`, индексы, битовые операции);
- вести себя как «число с единицами измерения» (метры, секунды, деньги) или математический объект (вектор, матрица).

### Модель вызова бинарных операторов

Для выражения:

```python
result = a + b
```

интерпретатор делает примерно следующее:

1. Пытается вызвать `a.__add__(b)`.
2. Если этот метод **отсутствует** или вернул `NotImplemented`, интерпретатор:
   - проверяет, что типы операндов различаются (тип `b` — подтип типа `a` или наоборот);
   - пытается вызвать `b.__radd__(a)`.
3. Если и обратный метод вернул `NotImplemented`, поднимается `TypeError`.

Таблично:

| Выражение | Прямая версия | Обратная версия |
|----------|---------------|------------------|
| `a + b` | `a.__add__(b)` | `b.__radd__(a)` |
| `a - b` | `a.__sub__(b)` | `b.__rsub__(a)` |
| `a * b` | `a.__mul__(b)` | `b.__rmul__(a)` |
| и т.д. | | |

Это важно, если ваш класс должен уметь работать **вместе** с другим типом (например, `Vec2 + (1, 2)` или `Money + int`): вы либо принимаете `other` в прямом методе, либо реализуете корректный `__radd__`.

### Обратные и in-place операции

- `a + b` пробует `a.__add__(b)`, если вернул `NotImplemented` — `b.__radd__(a)`.
- `a += b` пробует `a.__iadd__(b)`; если он не реализован, трактуется как `a = a + b`.

#### Пример: вектор с базовыми операциями

```python
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vec2({self.x!r}, {self.y!r})"

    def __add__(self, other):
        if not isinstance(other, Vec2):
            return NotImplemented
        return Vec2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        if not isinstance(other, Vec2):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self
```

Здесь:

- `v1 + v2` создаёт **новый** `Vec2`;
- `v1 += v2` изменяет существующий объект `v1` (если вы не переопределите `__iadd__`, будет создан новый объект, а ссылка переприсвоится).

### Протокол числовых преобразований

Методы:

- `__int__(self)` — поведение `int(obj)`;
- `__float__(self)` — `float(obj)`;
- `__complex__(self)` — `complex(obj)`;
- `__index__(self)` — использование в контекстах, где требуется целое (индексы, срезы, битовые операции).

Типичные правила:

- `__int__` и `__float__` должны по возможности сохранять **математический смысл** типа (учитывая погрешности представления);
- `__index__` обязан возвращать **строго `int`**, без потерь (не округление дроби, а именно целое).

### `__index__`

Метод `__index__(self)` позволяет объекту использоваться там, где ожидается **целое число**:

- индексация последовательностей `obj[my_index_like]`;
- операции сдвига битов, `range`, `slice` и т.п.

```python
class Step:
    def __init__(self, value):
        self.value = value

    def __index__(self):
        return int(self.value)

step = Step(2)
print(list(range(0, 10, step)))  # [0, 2, 4, 6, 8]
```

Если вы реализуете «число с единицами» (например, `Meters`), то:

- `__int__`/`__float__` можно использовать для получения «сырых чисел»;
- `__index__` — только если объект действительно можно использовать как **целый шаг/индекс** (обычно не реализуется для физических величин c плавающей точкой).

### Смешанные операции с встроенными типами

Когда в выражении участвуют **разные числовые типы** (например, ваш класс и `int`/`float`), Python применяет правила:

- сначала пробует **прямой метод** левого операнда (`left.__add__(right)`);
- если он вернул `NotImplemented`, пробует **обратный метод** правого (`right.__radd__(left)`).

Для корректного взаимодействия с числами:

- ваш класс должен в `__add__`/`__radd__` и других операциях уметь:
  - либо приводить `other` к внутреннему представлению (например, `Meters(1) + 5` → трактовать `5` как метры);
  - либо возвращать `NotImplemented`, позволяя противоположному операнду (если это встроенный тип) отклонить операцию.

Пример:

```python
class Meters:
    def __init__(self, value):
        self.value = float(value)

    def __add__(self, other):
        if isinstance(other, Meters):
            return Meters(self.value + other.value)
        if isinstance(other, (int, float)):
            return Meters(self.value + other)
        return NotImplemented

    def __radd__(self, other):
        # поддержим int/float + Meters
        return self.__add__(other)
```

Здесь:

- `Meters(3) + 2` и `2 + Meters(3)` оба работают и возвращают `Meters(5)`;
- `Meters(3) + "x"` корректно возвращает `NotImplemented`, что приводит к `TypeError`.

### Округление и математические функции

Для поддержки:

- `round(x)` — `x.__round__()`;
- `math.trunc(x)` — `x.__trunc__()`;
- `math.floor(x)` — `x.__floor__()`;
- `math.ceil(x)` — `x.__ceil__()`.

Если ваш класс представляет число (или величину), разумно реализовать эти методы через внутреннее числовое представление:

```python
import math

class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def __float__(self):
        return float(self.celsius)

    def __round__(self, ndigits=None):
        return Temperature(round(self.celsius, ndigits))

    def __trunc__(self):
        return math.trunc(self.celsius)
```

---

## §50. Битовые операции

### Основные методы

| Оператор | Методы |
|----------|--------|
| `&` | `__and__`, `__rand__`, `__iand__` |
| `\|` | `__or__`, `__ror__`, `__ior__` |
| `^` | `__xor__`, `__rxor__`, `__ixor__` |
| `<<` | `__lshift__`, `__rlshift__`, `__ilshift__` |
| `>>` | `__rshift__`, `__rrshift__`, `__irshift__` |
| `~x` | `__invert__` |

Типичное применение — классы для **битовых масок**, **флагов**, низкоуровневых протоколов.

### Пример: флаги доступа как битовая маска

```python
class Permissions:
    READ  = 0b001
    WRITE = 0b010
    EXEC  = 0b100

    def __init__(self, mask=0):
        self.mask = mask

    def __and__(self, other):
        if not isinstance(other, Permissions):
            return NotImplemented
        return Permissions(self.mask & other.mask)

    def __or__(self, other):
        if not isinstance(other, Permissions):
            return NotImplemented
        return Permissions(self.mask | other.mask)

    def __contains__(self, flag):
        # поддержим синтаксис: Permissions.READ in p
        return bool(self.mask & flag)

    def __repr__(self):
        return f"Permissions(mask={self.mask:#05b})"
```

Использование:

```python
p = Permissions(Permissions.READ | Permissions.WRITE)
print(p)                        # Permissions(mask=0b011)
print(Permissions.READ in p)    # True
print(Permissions.EXEC in p)    # False
```

Здесь мы не реализуем `__rand__`/`__ror__`, потому что работаем только с `Permissions` против `Permissions`. Если бы мы хотели поддержать `int & Permissions`, потребовались бы обратные версии (`__rand__` и т.п.).

---

## §51a. Slice и Ellipsis

### Объект `slice`

Оператор `obj[start:stop:step]` под капотом формирует объект:

```python
slice_obj = slice(start, stop, step)
obj.__getitem__(slice_obj)
```

Если `key` — это `slice`, ваша реализация `__getitem__` может выполнять нужную логику для срезов.

Атрибуты объекта `slice`:

- `slice_obj.start`
- `slice_obj.stop`
- `slice_obj.step`

Могут быть `None`, если соответствующая часть в срезе опущена (`a[:5]`, `a[::2]` и т.п.).

Для удобства есть метод `slice_obj.indices(length)`, который приводит срез к «нормализованным» значениям `(start, stop, step)` для последовательности длины `length`, учитывая отрицательные индексы и `None`:

```python
s = slice(1, None, 2)
start, stop, step = s.indices(len(seq))
for i in range(start, stop, step):
    ...
```

### Ellipsis (`...`)

Выражение `...` — это объект `Ellipsis`. Его часто используют:

- в **многомерных массивах** (например, NumPy): `arr[..., 0]`;
- в **type hints** (исторически, до `...` в dataclass/Protocol);
- как маркер «заглушки».

В `__getitem__` вы можете интерпретировать `Ellipsis` по-своему.

#### Пример: обработка `Ellipsis` и нескольких срезов

```python
class Tensor:
    def __init__(self, data):
        self._data = data  # вложенные списки, упрощённо

    def __getitem__(self, key):
        if key is Ellipsis:
            # Вернуть "всё" — в реальном коде логика будет сложнее
            return self._data
        if isinstance(key, tuple):
            # разбираем комбинированный ключ, например (slice(...), Ellipsis, int)
            # здесь можно реализовать собственную логику
            ...
        # остальное — как обычно
        return self._data[key]
```

В библиотеках вроде NumPy и PyTorch `...` означает «все оставшиеся оси»: `arr[..., 0]` — взять последний индекс по последней оси, а остальные оставить без изменений.

---

## §51b. `__class_getitem__` (Python 3.9+)

Метод **класса** `__class_getitem__(cls, item)` позволяет поддерживать синтаксис:

- `MyClass[int]`
- `Mapping[str, int]`

#### Пример: простой generic-объект

```python
class Box:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Box({self.value!r})"

    @classmethod
    def __class_getitem__(cls, item):
        # Можно просто вернуть cls или создать "параметризованный" класс
        print(f"{cls.__name__}[{item}] запрошен")
        return cls

Box[int]("x")  # напечатает "Box[int] запрошен"
```

В стандартной библиотеке через `__class_getitem__` реализованы generics в `typing`, `list[int]`, `dict[str, int]`, `collections.abc.Sequence[int]` и др.

### Как `__class_getitem__` используется в typing / generics

В Python 3:

- `list[int]` — это не просто синтаксис, а вызов `list.__class_getitem__(int)`;
- для пользовательских классов это позволяет делать:

  ```python
  class Box(Generic[T]):
      ...

  Box[int]  # параметризованный тип
  ```

Упрощённая картина:

- `__class_getitem__` может вернуть:
  - сам класс (игнорируя `item`);
  - **новый объект**, описывающий параметризацию (как это делает `typing`);
  - модифицированный/специализированный подкласс.

Пример «регистрации» параметров:

```python
class Registry:
    _types = {}

    @classmethod
    def __class_getitem__(cls, key):
        # key может быть типом, кортежем типов и т.п.
        cls._types.setdefault(key, [])
        return cls._types[key]

Registry[int].append("handler_for_int")
Registry[str].append("handler_for_str")
print(Registry._types)
```

Здесь `Registry[int]` использует `__class_getitem__`, чтобы вернуть **контейнер, привязанный к ключу**, а не сам класс.

---

## Дополнение A. Асинхронные протоколы и dunder-методы
