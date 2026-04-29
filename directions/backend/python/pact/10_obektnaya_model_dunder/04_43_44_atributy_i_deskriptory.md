[← Назад к индексу части X](index.md)


### Порядок разрешения атрибутов (упрощённая модель)

Когда вы пишете `obj.attr`, Python делает примерно следующее:

1. Вызывает `obj.__getattribute__("attr")`.
2. Внутри `object.__getattribute__`:
   - ищет атрибут в **классе** и его родителях;
   - если атрибут — **дескриптор с `__get__` и `__set__`** (data descriptor), вызывает его `__get__`;
   - иначе смотрит в **`obj.__dict__`**;
   - иначе, если атрибут — дескриптор только с `__get__` (non-data), вызывает его;
   - иначе ищет в классе/базах как обычный атрибут.
3. Если `__getattribute__` поднял `AttributeError`, вызывается `__getattr__(self, name)` (если определён).

Такая схема нужна, чтобы:

- дать приоритет **дескрипторам** (в частности, свойствам) над обычными атрибутами;
- позволить экземплярам «перекрывать» **методы без `__set__`** (non-data дескрипторы);
- предоставить аккуратный **fallback** через `__getattr__`.

Можно думать о разрешении атрибутов как о «слоях»:

1. Data-дескрипторы (с `__set__`/`__delete__`);
2. Атрибуты экземпляра (`__dict__`);
3. Non-data дескрипторы (только `__get__`);
4. Обычные атрибуты класса/базовых классов.

`__getattr__` стоит «снаружи» этой системы: он вызывается только если все слои не сработали.

### `__getattr__` vs `__getattribute__`

| Метод | Когда вызывается | Типичное применение |
|-------|------------------|---------------------|
| `__getattribute__(self, name)` | **Всегда** при любом доступе к атрибуту | Тонкое проксирование, логирование доступа, динамические прокси (осторожно!) |
| `__getattr__(self, name)` | **Только если атрибут не найден обычным способом** | Fallback: ленивые атрибуты, вычисление «на лету», «ленивый импорт» |

#### Пример: `__getattr__` для ленивого атрибута

```python
class Config:
    def __init__(self, data):
        self._data = data

    def __getattr__(self, name):
        # Вызывается только если обычный поиск не нашёл атрибут
        try:
            return self._data[name]
        except KeyError:
            raise AttributeError(name) from None

cfg = Config({"host": "localhost"})
print(cfg.host)  # localhost
```

Здесь `cfg.host` будет найден через `__getattr__`, а атрибуты, записанные в `__dict__`, будут работать как обычно.

#### Пример: аккуратное использование `__getattribute__`

```python
class LoggingProxy:
    def __init__(self, target):
        object.__setattr__(self, "_target", target)

    def __getattribute__(self, name):
        if name == "_target":
            return object.__getattribute__(self, name)
        print(f"getattr {name!r}")
        target = object.__getattribute__(self, "_target")
        return getattr(target, name)

    def __setattr__(self, name, value):
        print(f"setattr {name!r} = {value!r}")
        target = object.__getattribute__(self, "_target")
        setattr(target, name, value)
```

**Критично:** внутри `__getattribute__` и `__setattr__` для доступа к реальным атрибутам нужно использовать **`object.__getattribute__` / `object.__setattr__`**, иначе получите **бесконечную рекурсию**.

#### Где удобно применять `__getattr__`

1. **Ленивые атрибуты (lazy-loading):**

   ```python
   class LazyUser:
       def __init__(self, loader):
           self._loader = loader
           self._data = None

       def _ensure_loaded(self):
           if self._data is None:
               self._data = self._loader()

       def __getattr__(self, name):
           # сюда попадём, если атрибут не найден в __dict__/классе
           self._ensure_loaded()
           try:
               return self._data[name]
           except KeyError:
               raise AttributeError(name) from None
   ```

2. **Обёртка над чужим объектом с «тонкой» прослойкой:**

   ```python
   class Wrapper:
       def __init__(self, target):
           self._target = target

       def __getattr__(self, name):
           # делегируем все неизвестные атрибуты
           return getattr(self._target, name)
   ```

   Здесь «свои» атрибуты (`_target` и т.п.) находятся обычным путём, а **всё остальное** уходит в `__getattr__` и делегируется.

#### Где оправдан `__getattribute__` (и почему с ним надо быть крайне осторожным)

`__getattribute__` нужен, когда вы хотите:

- логировать **каждый доступ** к атрибутам (например, профилирование, трассировка);
- реализовать сложное **проксирование** (например, объект, который маскируется под другой);
- внедрять дополнительные инварианты / защиту (например, запрет доступа к некоторым атрибутам после «закрытия» объекта).

Типичный безопасный шаблон:

```python
class SafeProxy:
    def __init__(self, target):
        object.__setattr__(self, "_target", target)
        object.__setattr__(self, "_closed", False)

    def __getattribute__(self, name):
        if name in {"_target", "_closed", "close"}:
            return object.__getattribute__(self, name)
        if object.__getattribute__(self, "_closed"):
            raise RuntimeError("Object is closed")
        target = object.__getattribute__(self, "_target")
        return getattr(target, name)

    def close(self):
        object.__setattr__(self, "_closed", True)
```

Здесь мы:

- явно перечисляем «служебные» атрибуты;
- никогда не вызываем `self.attr` внутри `__getattribute__`, только `object.__getattribute__`;
- всё остальное прозрачно проксируем.

#### `__setattr__` и `__delattr__`

Эти методы позволяют перехватывать присваивания и удаления атрибутов:

- `__setattr__(self, name, value)` — вызывается при `self.name = value`;
- `__delattr__(self, name)` — вызывается при `del self.name`.

Типичные применения:

- **валидация и нормализация** значений;
- автоматический **лог изменений**;
- запрет/ограничение добавления новых атрибутов.

Пример: запрет опечаток в именах атрибутов:

```python
class StrictAttrs:
    __slots__ = ("x", "y")  # допустим только x и y

    def __setattr__(self, name, value):
        if name not in self.__slots__:
            raise AttributeError(f"Unknown attribute {name!r}")
        object.__setattr__(self, name, value)
```

Здесь `__slots__` и `__setattr__` совместно не дают тихо создать «лишний» атрибут, что особенно полезно в больших моделях данных.

---

## §44. Дескрипторы

### Что такое дескриптор

**Дескриптор** — объект, у которого определён хотя бы один из методов:

- `__get__(self, instance, owner)`  
- `__set__(self, instance, value)`  
- `__delete__(self, instance)`

И который лежит как **атрибут класса**: тогда при обращении `instance.attr` будет вызываться его логика.

| Тип дескриптора | Методы | Приоритет |
|-----------------|--------|-----------|
| **Data descriptor** | `__get__` и `__set__` / `__delete__` | Выше атрибутов экземпляра |
| **Non-data descriptor** | Только `__get__` | Ниже атрибутов экземпляра |

### Встроенные дескрипторы

- `property` — дескриптор, реализующий **свойства**;
- `classmethod`, `staticmethod` — дескрипторы, управляющие тем, как функция привязывается к классу/экземпляру;
- функции, определённые в классе, — **non-data дескрипторы** (они реализуют привязку `self`).

Чтобы лучше понять дескрипторы, полезно увидеть, как **поведение методов и свойств** можно выразить через них.

#### Как работает `property` (концептуально)

Упрощённая реализация:

```python
class property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc or (fget.__doc__ if fget else None)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)
```

Когда вы пишете:

```python
class User:
    @property
    def age(self):
        ...
```

функция `age` заменяется объектом `property`, который лежит в `User.__dict__["age"]` и решает, что делать при `user.age` и `user.age = 10`.

#### Минимальная реализация свойства через дескриптор

```python
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self  # доступ через класс
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be {self.expected_type.__name__}")
        instance.__dict__[self.name] = value

class Person:
    age = Typed("age", int)

    def __init__(self, age):
        self.age = age
```

Этот паттерн используется, например, в ORM (описание полей моделей).

#### Data vs non-data дескрипторы (тонкости приоритета)

Рассмотрим:

```python
class Demo:
    @property
    def x(self):
        return 1

    def y(self):
        return 2

d = Demo()
```

- `Demo.__dict__["x"]` — data-дескриптор (`property` с `__get__` и `__set__`/`__delete__`);
- `Demo.__dict__["y"]` — функция, non-data дескриптор (есть только `__get__`).

Если мы сделаем:

```python
d.x = 100
```

— мы получим `AttributeError`, потому что data-дескриптор `property` перехватывает **и чтение, и запись**; значения в `d.__dict__` с таким именем вообще не будет.

А вот:

```python
d.y = 200
print(d.y)  # 200, а не метод
```

Здесь:

- присваивание создаёт запись `d.__dict__["y"] = 200`;
- при чтении `object.__getattribute__` сначала проверяет data-дескрипторы (нет), потом `d.__dict__` и находит обычное значение `200` — только после этого дошёл бы до non-data дескриптора из класса.

**Итого:** data-дескрипторы «жёстче» контролируют атрибут (как `property`), non-data позволяют экземпляру **переопределять** поведение (например, динамически подменять методы).

#### Практический пример: кеширующее свойство (lazy property)

```python
class cached_property:
    def __init__(self, func):
        self.func = func
        self.__doc__ = getattr(func, "__doc__", None)

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        value = self.func(instance)
        instance.__dict__[self.name] = value
        return value
```

Использование:

```python
class Article:
    def __init__(self, raw_text):
        self.raw_text = raw_text

    @cached_property
    def parsed(self):
        print("parse...")
        return self.raw_text.upper()

a = Article("hello")
print(a.parsed)  # parse... HELLO
print(a.parsed)  # HELLO (без повторного parse)
```

Здесь дескриптор `cached_property` **один раз** вычисляет значение и записывает его в `__dict__` экземпляра; последующие чтения возвращают кеш.

---

## §45. Контейнеры и последовательности
