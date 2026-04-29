[← Назад к индексу части XIII](index.md)


Структурные паттерны отвечают на вопрос: **как связать классы и объекты**, чтобы:

- можно было расширять поведение;
- не плодить бесконечные иерархии наследования;
- не связывать компоненты слишком жёстко.

Часть этих паттернов уже затрагивалась в Часть XII (§65b) — здесь сделаем акцент на практических примерах.

### 5.1. Adapter

#### 5.1.1. Суть паттерна и терминология

- **Adapter (адаптер)** — паттерн, который позволяет объекту с «неподходящим» интерфейсом использоваться там, где ожидается другой интерфейс.
- Основная идея:
  - создать **обёртку (adapter)**;
  - обёртка реализует **целевой интерфейс** (тот, который ожидает клиент);
  - внутри она делегирует вызовы к «старому»/«чужому» объекту, **переводя параметры и формат результата**.

Термины:

- **Target (цель)** — интерфейс, который ожидает клиент;
- **Adaptee (адаптируемый)** — существующий класс/объект с неудобным интерфейсом;
- **Adapter** — класс/функция, который «подгоняет» Adaptee под Target.

---

#### 5.1.2. Базовый пример: адаптация платёжного API

```python
class OldPaymentAPI:
    def pay(self, amount: int) -> None:
        print(f"Paying {amount} via old API")


class PaymentClient:
    """Целевой интерфейс, который ожидает новый код."""

    def process_payment(self, amount: int) -> None:
        raise NotImplementedError


class OldPaymentAdapter(PaymentClient):
    """Адаптер, подгоняющий OldPaymentAPI под интерфейс PaymentClient."""

    def __init__(self, api: OldPaymentAPI):
        self._api = api

    def process_payment(self, amount: int) -> None:
        # Адаптация интерфейса и, при необходимости, формата данных
        self._api.pay(amount)
```

Клиентский код:

```python
def make_purchase(client: PaymentClient, amount: int) -> None:
    client.process_payment(amount)
```

Теперь:

- `make_purchase` не знает о `OldPaymentAPI` и не зависит от него;
- при появлении нового API можно написать другой адаптер:

```python
class NewPaymentAPI:
    def charge(self, value: float, currency: str) -> dict:
        ...


class NewPaymentAdapter(PaymentClient):
    def __init__(self, api: NewPaymentAPI):
        self._api = api

    def process_payment(self, amount: int) -> None:
        response = self._api.charge(float(amount), "USD")
        # При необходимости обработать response, выбросить исключение и т.п.
```

---

#### 5.1.3. Классовый и объектный Adapter

В классическом описании различают:

- **Class Adapter** — адаптер наследуется от Adaptee (многократное наследование);
- **Object Adapter** — адаптер содержит внутри экземпляр Adaptee и делегирует ему вызовы.

В Python почти всегда используют **object adapter**:

- множественное наследование возможно, но **слишком сильная связь** (Adapter становится «тем же типом», что и Adaptee);
- композиция (`self._wrapped = adaptee`) даёт большую гибкость.

Пример объектного адаптера для файлового интерфейса:

```python
class FileLike:
    """Целевой интерфейс: объект с методом read()."""

    def read(self) -> str:
        raise NotImplementedError


class Socket:
    def recv(self, bufsize: int) -> bytes:
        ...


class SocketFileAdapter(FileLike):
    def __init__(self, sock: Socket, encoding: str = "utf-8"):
        self._sock = sock
        self._encoding = encoding

    def read(self) -> str:
        data = self._sock.recv(4096)
        return data.decode(self._encoding)
```

---

#### 5.1.4. «Питоничные» адаптеры: функции, замыкания, `__getattr__`

В Python Adapter нередко реализуется **без отдельного класса**, через:

- простую функцию‑обёртку;
- замыкание;
- или универсальный прокси с `__getattr__`.

Функциональный адаптер:

```python
def use_filelike(obj_with_read):
    data = obj_with_read.read()
    ...


def adapt_socket(sock: Socket):
    class _Adapter:
        def read(self) -> str:
            return sock.recv(4096).decode("utf-8")

    return _Adapter()


sock = Socket()
use_filelike(adapt_socket(sock))
```

Универсальный адаптер через `__getattr__`:

```python
class LoggingAdapter:
    """Пример универсальной обёртки-адаптера."""

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def __getattr__(self, name):
        # Перехватываем доступ к атрибутам и можем менять поведение
        attr = getattr(self._wrapped, name)
        if callable(attr):
            def wrapper(*args, **kwargs):
                print(f"Calling {name} with {args} {kwargs}")
                return attr(*args, **kwargs)
            return wrapper
        return attr
```

Это уже ближе к Proxy/Decorator, но часто используется и как Adapter, если:

- нужно слегка изменить интерфейс (переименовать методы, добавить параметры по умолчанию);
- а остальное просто делегировать.

---

#### 5.1.5. Adapter в интеграциях и микросервисах

В реальных проектах Adapter часто появляется в слоях:

- **интеграции с внешними API**:
  - REST/GraphQL/GRPC‑клиенты;
  - SDK‑клиенты сторонних сервисов.

Например, у вас есть доменный интерфейс:

```python
class SmsSender(ABC):
    @abstractmethod
    def send_sms(self, phone: str, text: str) -> None:
        ...
```

И внешний SDK:

```python
class ThirdPartySmsClient:
    def send_message(self, destination: str, body: str, *, sender_id: str) -> None:
        ...
```

Адаптер:

```python
class ThirdPartySmsAdapter(SmsSender):
    def __init__(self, client: ThirdPartySmsClient, sender_id: str):
        self._client = client
        self._sender_id = sender_id

    def send_sms(self, phone: str, text: str) -> None:
        self._client.send_message(destination=phone, body=text, sender_id=self._sender_id)
```

Преимущества:

- весь остальной код работает через **абстракцию `SmsSender`**;
- для тестов можно подставить **фейковую реализацию** `SmsSender`, не трогая адаптер.

---

#### 5.1.6. Adapter vs Facade vs Decorator/Proxy

Эти паттерны легко перепутать, поэтому важно различать **цель**:

- **Adapter**:
  - главная задача — **совместимость интерфейсов**;
  - «чужой» объект уже существует, но его интерфейс не совпадает с тем, что ожидает клиент;
  - Adapter подгоняет **подписи методов и формат данных**.

- **Facade**:
  - цель — **упростить сложную подсистему**;
  - внутри может использовать несколько компонентов, ORM, кэш и т.д.;
  - интерфейс может быть совершенно новым, не похожим на внутренние.

- **Decorator / Proxy**:
  - цель — добавить **дополнительное поведение** (кеш, логирование, права) при сохранении того же интерфейса;
  - как правило, интерфейс исходного объекта уже «подходит», менять его не нужно.

Правило:

- если основная проблема — «подружить» **два разных интерфейса** → Adapter;
- если проблема — «слишком много мелких шагов/классов, хочу один упрощённый вход» → Facade;
- если проблема — «хочу дополнить объект логированием/кешем/безопасностью» → Decorator/Proxy.

---

#### 5.1.7. Частые ошибки при использовании Adapter

- **Смешивание нескольких ролей в одном классе**  
  Адаптер начинает:
  - и адаптировать интерфейс;
  - и содержать бизнес‑логику;
  - и кэшировать, и логировать…  
  В итоге он превращается в очередной God‑Object.

- **Жёсткая привязка клиента к конкретному адаптеру**  
  Если вместо зависимости от абстракции вы начинаете передавать `OldPaymentAdapter` повсюду по коду, вы теряете преимущество Adapter:
  - при замене внешнего API придётся править весь код, а не только точку создания адаптера.

- **Неявная адаптация через monkey patching**  
  Вместо явного адаптера:

  ```python
  some_module.func = my_compatible_func
  ```

  Такой код:
  - трудно отлаживать (поведение зависит от порядка импортов);
  - скрывает факт адаптации.  
  Лучше писать явные адаптеры и подменять только через DI/конфигурацию.

---

#### 5.1.8. Практические рекомендации

1. Держите адаптеры **тонкими**:
   - минимальное количество логики внутри;
   - без бизнес‑правил, только перевод между интерфейсами и форматами данных.
2. Размещайте адаптеры в слое интеграции (например, модуль `adapters/`, `infra/`):
   - доменный код видит только целевые интерфейсы (протоколы/ABC);
   - адаптеры реализуют эти интерфейсы и знают о конкретных SDK/клиентах.
3. Для тестов:
   - тестируйте адаптеры отдельно (юнит‑тестами);
   - в остальном коде подставляйте фейковые реализации интерфейсов, **не** реальные адаптеры.

---

#### 5.1.9. Упражнения

1. Найдите в своём проекте место, где вы напрямую вызываете внешний SDK/клиент (HTTP, БД, облачный сервис) из бизнес‑кода.  
   Попробуйте:
   - описать целевой интерфейс (Protocol/ABC);
   - реализовать Adapter, который подгоняет внешний SDK под этот интерфейс;
   - изменить бизнес‑код так, чтобы он зависел только от интерфейса.
2. Реализуйте два адаптера для одного интерфейса, например:
   - `SmsSender` для SMS‑сервиса A;
   - `SmsSender` для SMS‑сервиса B.  
   Напишите код, который выбирает нужный адаптер по конфигурации, **не меняя** остальной код.
3. Возьмите простую функциональность (логирование, отправка HTTP‑запроса) и реализуйте:
   - версию с Facade;
   - версию с Adapter;  
   Сравните, где главная цель — «упростить API», а где — «сделать совместимыми два разных интерфейса».

---

### 5.2. Bridge

#### 5.2.1. Суть Bridge: разделяем абстракцию и реализацию

Bridge подробно разбирался в Часть XII (§65b); здесь соберём суть применительно к паттернам.

- **Абстракция** — «что мы хотим делать»:
  - `Shape.draw()`;
  - `Storage.save()`;
  - `Notifier.notify()`.
- **Реализация** — «как именно это делается»:
  - отрисовка через OpenGL / Cairo / SVG;
  - хранение в Postgres / S3 / Redis;
  - отправка уведомлений через email / SMS / push.

**Bridge** говорит:

> Не наследуйтесь от всех возможных комбинаций.  
> Постройте **две независимые иерархии** (абстракций и реализаций) и свяжите их через **композицию**.

---

#### 5.2.2. Пример: фигуры и API рисования

```python
from abc import ABC, abstractmethod


class DrawingAPI(ABC):
    """Иерархия реализаций (implementation hierarchy)."""

    @abstractmethod
    def draw_circle(self, x: float, y: float, r: float) -> None:
        ...


class OpenGLDrawingAPI(DrawingAPI):
    def draw_circle(self, x: float, y: float, r: float) -> None:
        print(f"[OpenGL] circle at ({x}, {y}), r={r}")


class CairoDrawingAPI(DrawingAPI):
    def draw_circle(self, x: float, y: float, r: float) -> None:
        print(f"[Cairo] circle at ({x}, {y}), r={r}")


class Shape(ABC):
    """Иерархия абстракций (abstraction hierarchy)."""

    def __init__(self, api: DrawingAPI):
        self._api = api

    @abstractmethod
    def draw(self) -> None:
        ...


class Circle(Shape):
    def __init__(self, x: float, y: float, r: float, api: DrawingAPI):
        super().__init__(api)
        self.x = x
        self.y = y
        self.r = r

    def draw(self) -> None:
        self._api.draw_circle(self.x, self.y, self.r)
```

Использование:

```python
circle1 = Circle(0, 0, 10, OpenGLDrawingAPI())
circle2 = Circle(5, 5, 20, CairoDrawingAPI())

circle1.draw()
circle2.draw()
```

Здесь:

- можно добавлять новые фигуры (`Rectangle`, `Triangle`) **без изменения** классов реализаций;
- можно добавлять новые API (`VulkanDrawingAPI`, `SvgDrawingAPI`) **без изменения** классов фигур.

Без Bridge при двух фигурах и трёх API пришлось бы заводить до 6 классов (`CircleOpenGL`, `CircleCairo`, `CircleSvg`, `SquareOpenGL` и т.д.) — **взрыв комбинаций**.

---

#### 5.2.3. Типичный сценарий применения Bridge

Bridge полезен, когда одновременно выполняются условия:

1. Есть **два измерения изменчивости**:
   - например, «тип сущности» и «тип хранилища»;
   - или «тип фигуры» и «тип отрисовки».
2. Оба измерения потенциально **будут расширяться независимо**:
   - часто добавляются новые фигуры;
   - иногда появляется новый способ отрисовки.

Тогда:

- лучше разделить эти измерения в разные иерархии;
- соединять их **композицией** (поле `self._impl`, `self._api`, `self._driver`).

Ещё один пример — система логирования:

```python
class LogBackend(ABC):
    @abstractmethod
    def write(self, message: str) -> None: ...


class ConsoleBackend(LogBackend):
    def write(self, message: str) -> None:
        print(message)


class FileBackend(LogBackend):
    def __init__(self, filename: str):
        self._filename = filename

    def write(self, message: str) -> None:
        with open(self._filename, "a") as f:
            f.write(message + "\n")


class Logger:
    def __init__(self, backend: LogBackend):
        self._backend = backend

    def info(self, msg: str) -> None:
        self._backend.write(f"[INFO] {msg}")

    def error(self, msg: str) -> None:
        self._backend.write(f"[ERROR] {msg}")
```

Тут:

- иерархия реализаций: `ConsoleBackend`, `FileBackend`, `RemoteBackend` и т.д.;
- иерархия абстракций может усложняться: разные виды `Logger` (структурированный, JSON‑logger, security‑logger), но все они используют интерфейс `LogBackend`.

---

#### 5.2.4. Bridge vs Strategy vs Adapter vs Abstract Factory

Легко запутаться, чем Bridge отличается от других паттернов:

- **Strategy**:
  - тоже использует композицию: объект хранит ссылку на «алгоритм»;
  - но акцент на **подмене алгоритма** (стратегии) в рантайме;
  - обычно стратегия **очень узкая** (одна операция).
  - Bridge чуть шире: это **структурный приём разделения иерархий**, а не только выбор алгоритма.

- **Adapter**:
  - цель Adapter — **совместимость интерфейсов** (подогнать чужой API под ожидаемый);
  - Bridge проектируется **изначально**, чтобы избежать взрыва комбинаций;
  - Adapter чаще добавляется **позже**, чтобы вписать чужой код в уже существующие интерфейсы.

- **Abstract Factory**:
  - Abstract Factory создаёт **семейства объектов**;
  - Bridge описывает, как **структурно связать** две иерархии через композицию;
  - часто используются вместе: Abstract Factory создаёт реализацию (`DrawingAPI`), которая потом подсовывается в Bridge‑иерархию.

---

#### 5.2.5. Питоничные аспекты Bridge

В Python Bridge нередко «маскируется» под:

- передачу «клиента» или «драйвера» аргументом конструктора:

  ```python
  class Storage:
      def __init__(self, driver: "DriverProtocol"):
          self._driver = driver
  ```

- использование `Protocol` вместо ABC:

  ```python
  from typing import Protocol


  class StorageDriver(Protocol):
      def read(self, key: str) -> bytes: ...
      def write(self, key: str, data: bytes) -> None: ...
  ```

При этом важно:

- чтобы «абстракция» **не знала** о конкретных реализациях;
- чтобы реализаций можно было несколько, и им было достаточно реализовать протокол.

---

#### 5.2.6. Ошибки при проектировании Bridge

- **Слишком ранний Bridge**  
  Иногда разработчики создают две иерархии «на будущее», когда:
  - есть только одна фигура и один драйвер;
  - другие варианты не планируются.  
  В итоге архитектура усложняется без реальной пользы.

- **Подмена Bridge обычным наследованием**  
  Встречается структура:

  ```python
  class FileLogger(Logger, FileBackend): ...
  class ConsoleLogger(Logger, ConsoleBackend): ...
  ```

  Это не Bridge, а **множественное наследование конкретных реализаций**:
  - всё смешивается в одном классе;
  - трудно переиспользовать драйверы в других контекстах;
  - сложно тестировать отдельно абстракцию и реализацию.

- **Жёсткая привязка абстракции к конкретной реализации**  
  Если в коде абстракции появляется:

  ```python
  self._api = OpenGLDrawingAPI()
  ```

  — это нарушает идею Bridge (DIP нарушен).  
  Реализацию нужно **передавать снаружи**, а не создавать внутри.

---

#### 5.2.7. Практические рекомендации и упражнения

1. Найдите в своём коде место, где у вас есть **два измерения изменчивости**, например:
   - разные типы хранилищ и разные операции поверх них;
   - разные форматы вывода (JSON/HTML/text) и разные сущности, которые надо выводить.  
   Попробуйте мысленно нарисовать матрицу комбинаций и оценить, не приведёт ли наследование к взрыву классов.
2. Спроектируйте маленький Bridge:
   - абстракция: `ReportExporter.export(report)`;
   - реализации: `PdfBackend`, `HtmlBackend`, `JsonBackend`.  
   Добавьте две‑три конкретные абстракции (`UserReportExporter`, `SalesReportExporter`), которые принимают backend через конструктор.
3. Попробуйте объединить Bridge и Abstract Factory:
   - фабрика создаёт набор backend’ов (для прод/теста);
   - абстракции (`Service`, `Exporter`, `Repository`) получают backend’ы через конструктор.  
   Посмотрите, насколько проще становится переключать конфигурации (prod/test/dev).

---

### 5.3. Composite

**Вопрос:** как представить **дерево объектов** (меню, UI, файловая система), чтобы к «листу» и «контейнеру» можно было обращаться одинаково?

**Идея:** общий интерфейс `Component`, две реализации:

- `Leaf` — конечный элемент;
- `Composite` — узел с детьми.

```python
class Component:
    def render(self, indent: int = 0) -> None:
        raise NotImplementedError


class Text(Component):
    def __init__(self, text: str):
        self.text = text

    def render(self, indent: int = 0) -> None:
        print(" " * indent + self.text)


class Container(Component):
    def __init__(self, name: str):
        self.name = name
        self.children: list[Component] = []

    def add(self, child: Component) -> None:
        self.children.append(child)

    def render(self, indent: int = 0) -> None:
        print(" " * indent + f"[{self.name}]")
        for child in self.children:
            child.render(indent + 2)
```

Использование:

```python
root = Container("root")
root.add(Text("hello"))
sub = Container("sub")
sub.add(Text("world"))
root.add(sub)

root.render()
```

Composite часто используют:

- для UI‑деревьев, файловых систем, AST (дерево синтаксиса).

---

### 5.4. Decorator (структурный)

**Вопрос:** как динамически добавлять объекту поведение, **не меняя его класс** и не создавая кучу подклассов?

**Идея:** объект‑декоратор **содержит** оригинальный объект и реализует тот же интерфейс, добавляя свою логику.

```python
class Notifier:
    def send(self, message: str) -> None:
        print(f"Base: {message}")


class LoggingNotifier(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        print("Logging before send")
        self._wrapped.send(message)
```

Можно складывать несколько декораторов:

```python
class SMSNotifier(Notifier):
    def __init__(self, wrapped: Notifier):
        self._wrapped = wrapped

    def send(self, message: str) -> None:
        self._wrapped.send(message)
        print(f"Sending SMS: {message}")
```

В Python структурные декораторы часто реализуют через:

- композицию + делегирование (`__getattr__`);
- или через **функциональные декораторы** (см. §69).

---

### 5.5. Facade

**Вопрос:** как предоставить **простой API** к сложной подсистеме?

**Идея:** класс Facade инкапсулирует:

- работу с несколькими модулями/классами;
- сложную последовательность шагов.

```python
class AuthService:
    def login(self, username: str, password: str) -> str:
        ...


class PaymentService:
    def charge(self, user_id: int, amount: int) -> None:
        ...


class AppFacade:
    def __init__(self, auth: AuthService, payments: PaymentService):
        self._auth = auth
        self._payments = payments

    def login_and_pay(self, username: str, password: str, amount: int) -> None:
        user_id = int(self._auth.login(username, password))
        self._payments.charge(user_id, amount)
```

Клиенты видят только `AppFacade`, а не всю внутреннюю кухню.

---

### 5.6. Flyweight

**Вопрос:** как уменьшить расход памяти, когда у нас **много однотипных объектов** с общим состоянием?

**Идея:** разделить состояние на:

- **intrinsic** (общее, разделяемое);
- **extrinsic** (уникальное, передаётся при вызове).

Пример с текстовыми глифами:

```python
class Glyph:
    def __init__(self, char: str):
        self.char = char  # intrinsic состояние

    def draw(self, x: int, y: int) -> None:
        print(f"Draw '{self.char}' at ({x}, {y})")


class GlyphFactory:
    _cache: dict[str, Glyph] = {}

    @classmethod
    def get(cls, char: str) -> Glyph:
        if char not in cls._cache:
            cls._cache[char] = Glyph(char)
        return cls._cache[char]
```

Вместо тысячи объектов `'A'` у нас один `Glyph('A')`, а координаты — внешнее состояние.

В Python Flyweight иногда реализуется через:

- кеши (`functools.lru_cache`, словари);
- интернирование строк (`sys.intern`).

---

### 5.7. Proxy

**Вопрос:** как добавить к объекту **кеширование, ленивую загрузку, логирование, контроль доступа**, не меняя его код?

**Идея:** Proxy реализует тот же интерфейс, но:

- перехватывает вызовы;
- добавляет дополнительную логику.

```python
class RealImage:
    def __init__(self, filename: str):
        self.filename = filename
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        print(f"Loading {self.filename} from disk...")

    def display(self) -> None:
        print(f"Displaying {self.filename}")


class ImageProxy:
    def __init__(self, filename: str):
        self.filename = filename
        self._real: RealImage | None = None

    def display(self) -> None:
        if self._real is None:
            self._real = RealImage(self.filename)
        self._real.display()
```

Типичные виды Proxy:

- **virtual / lazy** (ленивая загрузка);
- **protection** (проверка прав);
- **remote** (вызовы по сети);
- **cache** (кеширование результата).

В Python роль Proxy часто выполняют:

- объекты‑обёртки, реализующие `__getattr__`;
- прокси ORM (ленивые запросы к БД).

---

## 6. Поведенческие паттерны (§68)
