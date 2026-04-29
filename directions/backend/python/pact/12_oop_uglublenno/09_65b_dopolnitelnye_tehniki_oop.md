[← Назад к индексу части XII](index.md)


Здесь кратко перечислены популярные ООП‑паттерны/техники, связанные с объектами и их жизненным циклом.

### Object Pool

- **Пул объектов** — переиспользование дорогих в создании объектов (соединения с БД, потоки и т.д.).

```python
class Connection:
    def __init__(self, id_: int):
        self.id = id_


class ConnectionPool:
    def __init__(self, size: int):
        self._available: list[Connection] = [Connection(i) for i in range(size)]

    def acquire(self) -> Connection:
        return self._available.pop()

    def release(self, conn: Connection) -> None:
        self._available.append(conn)
```

В реальных пулах:

- обычно есть блокировка/семафор для работы в многопоточной среде;
- может быть ограничение по времени ожидания (timeout) при `acquire`;
- пул может создавать новые соединения «по требованию» до некоторого максимума.

### Flyweight

- Разделение **общего состояния** между множеством объектов для экономии памяти.

Пример — кеширование однотипных объектов:

```python
class GlyphFactory:
    _cache: dict[str, "Glyph"] = {}

    @classmethod
    def get(cls, char: str) -> "Glyph":
        if char not in cls._cache:
            cls._cache[char] = Glyph(char)
        return cls._cache[char]


class Glyph:
    def __init__(self, char: str):
        self.char = char
```

### Proxy

- Заместитель реального объекта; добавляет **контроль доступа, кеширование, lazy‑loading** и т.п.

```python
class RealImage:
    def __init__(self, filename: str):
        self.filename = filename
        self._load_from_disk()

    def _load_from_disk(self):
        print(f"Loading {self.filename} from disk...")

    def display(self):
        print(f"Displaying {self.filename}")


class ImageProxy:
    def __init__(self, filename: str):
        self.filename = filename
        self._real: RealImage | None = None

    def display(self):
        if self._real is None:
            self._real = RealImage(self.filename)
        self._real.display()
```

Варианты прокси:

- **защитный** (protection proxy) — проверяет права доступа;
- **удалённый** (remote proxy) — представляет объект в другом процессе/на другом сервере;
- **кеширующий** (cache proxy) — сохраняет результаты вызовов.

### Decorator (структурный)

- Оборачивает объект для добавления поведения **без изменения** исходного класса.

```python
class Notifier:
    def send(self, message: str) -> None:
        print(f"Notify: {message}")


class LoggingNotifier:
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        print("Logging before send")
        self._wrapped.send(message)
```

Важно отличать:

- **структурный декоратор** (как здесь) — оборачивает объекты;
- **функциональный декоратор** (из мира Python‑функций) — оборачивает функции/методы. Идея та же, реализация на уровне функций (`@decorator`).

### Adapter

- Адаптирует интерфейс одного объекта под ожидания другого кода.

```python
class OldApi:
    def do_work(self, data: str) -> None:
        print(f"Old API: {data}")


class NewClient:
    def process(self, payload: str) -> None:
        print(f"Processing: {payload}")


class OldApiAdapter:
    def __init__(self, old_api: OldApi):
        self._old_api = old_api

    def process(self, payload: str) -> None:
        # Адаптируем вызов
        self._old_api.do_work(payload)
```

### Facade

- Упрощённый интерфейс к сложной подсистеме.

```python
class SubsystemA: ...
class SubsystemB: ...


class Facade:
    def __init__(self):
        self._a = SubsystemA()
        self._b = SubsystemB()

    def run(self):
        # Внутри — сложная последовательность действий
        ...
```

### Bridge

- **Bridge** — разделение абстракции и реализации так, чтобы они могли **развиваться независимо**.

Интуитивно:

- у нас есть **абстракция** (что мы хотим делать) и несколько вариантов **реализации** (как именно это делать);
- мы не хотим плодить взрыв комбинаций наследованием (`ColoredCircle`, `ColoredSquare`, `TexturedCircle`, ...);
- вместо этого мы **разделяем** иерархии и соединяем их через **композицию**.

Пример: система рисования фигур разными драйверами вывода.

```python
from abc import ABC, abstractmethod


class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        ...


class OpenGLDrawingAPI(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"[OpenGL] circle at ({x}, {y}), r={radius}")


class CairoDrawingAPI(DrawingAPI):
    def draw_circle(self, x: float, y: float, radius: float) -> None:
        print(f"[Cairo] circle at ({x}, {y}), r={radius}")


class Shape(ABC):
    def __init__(self, drawing_api: DrawingAPI):
        self._drawing_api = drawing_api

    @abstractmethod
    def draw(self) -> None:
        ...


class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float, drawing_api: DrawingAPI):
        super().__init__(drawing_api)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self) -> None:
        self._drawing_api.draw_circle(self.x, self.y, self.radius)
```

Использование:

```python
circle1 = Circle(0, 0, 10, OpenGLDrawingAPI())
circle2 = Circle(5, 5, 20, CairoDrawingAPI())

circle1.draw()
circle2.draw()
```

Здесь:

- иерархия `Shape` (абстракции) **не зависит** от конкретных библиотек отрисовки;
- иерархия `DrawingAPI` (реализации) **не знает** о конкретных фигурах;
- мы можем легко добавлять новые фигуры и новые API, не создавая экспоненциального числа подклассов.

#### Bridge vs Adapter vs Facade

- **Adapter**:
  - цель — **подогнать чужой интерфейс под ожидаемый**;
  - чаще всего используется при интеграции с уже существующим API;
  - архитектура системы уже есть, адаптер — «прослойка совместимости».
- **Facade**:
  - цель — **спрятать сложность** подсистемы за простым интерфейсом;
  - внутри фасада могут использоваться и Bridge, и Adapter, и другие паттерны;
  - упрощает жизнь пользователям сложной библиотеки.
- **Bridge**:
  - цель — **развязать параллельные иерархии** (абстракции и реализации);
  - проектируется **изначально**, чтобы избежать взрыва комбинаций классов;
  - активно использует композицию: абстракция хранит ссылку на реализацию.

### Composite

- Строит **древовидную структуру**, где листья и узлы имеют общий интерфейс.

```python
class Component:
    def operation(self) -> None:
        raise NotImplementedError


class Leaf(Component):
    def operation(self) -> None:
        print("Leaf")


class Composite(Component):
    def __init__(self):
        self.children: list[Component] = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def operation(self) -> None:
        for child in self.children:
            child.operation()
```

Composite удобно использовать для:

- представления иерархий UI‑элементов (виджеты/контейнеры);
- файловых систем (папки/файлы);
- деревьев выражений (узлы‑операторы и листья‑операнды).

---

## Частые ошибки и анти‑паттерны продвинутого ООП в Python
