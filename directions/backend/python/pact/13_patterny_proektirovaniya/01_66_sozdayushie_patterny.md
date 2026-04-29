[← Назад к индексу части XIII](index.md)


### 4.1. Singleton

#### 4.1.1. Суть и терминология

- **Singleton** — паттерн, который гарантирует, что у некоторого компонента есть **ровно один экземпляр** и к нему есть **глобальная точка доступа**.
- **Глобальное состояние (global state)** — данные, к которым можно обратиться «откуда угодно» без явной передачи (глобальные переменные, синглтоны, модули).
- **Жизненный цикл** — когда экземпляр создаётся, когда и как уничтожается (в случае Singleton — почти всегда «живёт всё время процесса»).

Важно: Singleton почти всегда означает **глобальное состояние**, а глобальное состояние:

- упрощает жизнь в мелких скриптах;
- сильно усложняет тестирование и сопровождение больших систем.

Типичные применения (где идея «один объект на процесс» логична):

- **конфигурация приложения** (но обычно удобнее модуль);
- **журналирование** (общая точка входа в лог‑систему);
- **пулы ресурсов** (подключения к БД, HTTP‑пулы);
- **центральные реестры** (например, реестр плагинов, если он действительно должен быть единственным).

Но в большинстве Python‑проектов классический Singleton‑класс **не нужен**: роль «единственного объекта» уже выполняют **модули**.

---

#### 4.1.2. Модуль как Singleton (рекомендуемый Python‑подход)

Файл `config.py`:

```python
# config.py
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/db")
DEBUG = os.getenv("DEBUG", "0") == "1"

def reload_from_env() -> None:
    """Перечитать настройки из переменных окружения."""
    global DATABASE_URL, DEBUG
    DATABASE_URL = os.getenv("DATABASE_URL", DATABASE_URL)
    DEBUG = os.getenv("DEBUG", "0") == "1"
```

Использование:

```python
import config

def main():
    if config.DEBUG:
        print("Debug mode ON")
    print("DB:", config.DATABASE_URL)
```

**Почему модуль — по сути Singleton:**

- при первом `import config` интерпретатор:
  - создаёт объект модуля;
  - выполняет его код;
  - сохраняет модуль в `sys.modules["config"]`;
- каждый последующий `import config` получает **тот же объект** модуля;
- состояния `config.DEBUG`, `config.DATABASE_URL` разделяются всеми частями программы.

Плюсы модульного подхода:

- **просто**: никакого метакласса, `__new__`, магии;
- модули естественно интегрируются с системой импорта;
- такой код проще читать другим Python‑разработчикам.

Минусы:

- всё равно формируется **глобальное состояние**, к которому легко обращаться из любой части кода;
- в тестах приходится:
  - либо подменять атрибуты модуля;
  - либо использовать `monkeypatch` / `unittest.mock.patch`.

---

#### 4.1.3. Классический Singleton через `__new__`

Иногда хочется именно **класс**, а не модуль, например:

- вы хотите реализовать общий интерфейс `ConfigInterface`, и конкретная реализация должна быть единственной;
- вы хотите, чтобы синглтон был **подтипом** другого класса (например, `Logger`).

```python
class Singleton:
    """Базовый класс-синглтон на уровне процесса."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        # Важно: здесь нет потокобезопасности
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class AppConfig(Singleton):
    def __init__(self, debug: bool = False):
        # __init__ вызывается КАЖДЫЙ раз при AppConfig()
        self.debug = debug
```

Проблемы такой реализации:

- **повторный вызов `__init__`**:
  - если вы создадите `AppConfig(debug=True)`, а потом где‑то `AppConfig(debug=False)`, второе создание переопределит состояние первого;
  - это трудно отследить.
- **потокобезопасность**:
  - при одновременном создании из нескольких потоков `_instance` может быть создан несколько раз;
  - для защиты нужен `threading.Lock`.

Исправление: инициализацию делать один раз:

```python
import threading


class SafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # double-checked locking
                    cls._instance = super().__new__(cls)
        return cls._instance


class SafeConfig(SafeSingleton):
    _initialized = False

    def __init__(self, debug: bool = False):
        if self._initialized:
            return
        self.debug = debug
        self._initialized = True
```

Здесь:

- `__new__` гарантирует, что создаётся ровно один объект;
- `__init__` защищён флагом `_initialized`, чтобы не выполняться повторно.

---

#### 4.1.4. Singleton через метакласс

Метакласс позволяет:

- использовать одну и ту же «синглтон‑логику» для многих классов;
- не наследоваться от специального базового класса (как `Singleton` выше).

```python
class SingletonMeta(type):
    """Метакласс, делающий каждый класс синглтоном."""

    _instances: dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        # __call__ вызывается при создании экземпляра: MyClass()
        if cls not in cls._instances:
            # super().__call__ создаёт экземпляр:
            #   1) вызывает __new__
            #   2) затем __init__
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppConfig(metaclass=SingletonMeta):
    def __init__(self, debug: bool = False):
        self.debug = debug
```

Особенности:

- любой класс, у которого `metaclass=SingletonMeta`, автоматически становится Singleton;
- контролировать повторную инициализацию (как с `_initialized`) по‑прежнему нужно внутри класса.

Минусы:

- метаклассы сложнее для новичков;
- трудно комбинировать несколько метаклассов (если уже используется другой);
- отладка поведения «создания класса и объекта» становится нетривиальной.

---

#### 4.1.5. Где Singleton уместен в Python, а где — нет

**Уместно**, если:

- действительно существует **одна глобальная сущность** в рамках процесса:
  - единая конфигурация (но чаще удобнее модуль);
  - глобальный реестр плагинов/типов;
  - общий объект журналирования, если вы строите свою лог‑систему (хотя стандартный модуль `logging` уже решает это).
- вы контролируете жизненный цикл процесса (CLI‑утилита, сервис).

**Неуместно**, если:

- вы можете **передать зависимость явно** (через аргументы конструктора или функции) — это почти всегда лучше:
  - сервис принимает `config` или `logger` параметром;
  - модули не «лезут» в глобальный Singleton, а получают его снаружи.
- вы пишете код, который нужно:
  - легко тестировать;
  - переиспользовать в других проектах.

В большинстве случаев правильнее применить **DIP + Dependency Injection** (см. Часть XII §63–§65a):

```python
class Service:
    def __init__(self, config: "Config", logger: "Logger"):
        self._config = config
        self._logger = logger
```

и уже в точке сборки приложения решить:

- будет ли `config` синглтоном (модуль/класс синглтон);
- или нужна возможность иметь несколько разных конфигураций (тесты, мульти‑тенантный сервис).

---

#### 4.1.6. Анти‑паттерны, связанные с Singleton

- **Hidden dependencies (скрытые зависимости)**  
  Класс внутри себя делает `from config import settings` или `from my_singleton import instance` и начинает пользоваться глобалом.
  - Такие зависимости **не видны в сигнатуре** конструктора/функций;
  - чтобы протестировать класс, приходится «подменять глобалы».

- **God‑Singleton (бог‑объект)**  
  В Singleton складывают «всё подряд»: конфигурацию, логику работы, кеши, статистику и т.д.  
  Это нарушает SRP (Single Responsibility Principle), см. Часть XII §63.

- **Трудно тестировать в параллели**  
  Если тесты запускаются параллельно (pytest‑xdist, несколько процессов/потоков), глобальное состояние от одного теста может влиять на другой.

- **Проблемы с порядком инициализации**  
  Если Singleton инициализируется «лениво» при первом обращении, легко получить ситуацию, когда:
  - часть кода ожидает, что он уже настроен;
  - другая часть его инициализирует «по‑своему» позже.

---

#### 4.1.7. Практические рекомендации по Singleton в Python

1. **По умолчанию используйте модуль вместо классического Singleton.**  
   Это проще, прозрачнее и естественнее для Python.
2. **Все зависимости старайтесь передавать явно.**  
   Пусть `Service` принимает `config` параметром, а не импортирует глобальный `config` у себя в модуле.
3. **Если всё‑таки пишете Singleton‑класс**:
   - сделайте его потокобезопасным, если есть многопоточность;
   - продумайте, когда именно он инициализируется (лениво/ eagerly);
   - добавьте способ **сбросить/переинициализировать** экземпляр для тестов (например, служебный метод `reset_for_tests()` или отдельный фабричный объект в тестах).
4. **В публичных библиотеках** избегайте Singleton’ов:
   - библиотека не должна навязывать пользователю глобальное состояние;
   - лучше предоставьте функции/классы, которые пользователь сам свяжет между собой на уровне приложения.

---

#### 4.1.8. Упражнения

1. Возьмите свой проект и найдите места, где вы используете **глобальные переменные** или одиночные модули как Singleton.  
   Попробуйте переписать один такой участок так, чтобы зависимость передавалась **явно** (через конструктор/функцию), и сравните:
   - стало ли проще писать тесты;
   - стало ли проще подменять конфигурацию.
2. Реализуйте потокобезопасный Singleton:
   - с использованием `threading.Lock`;
   - с ленивой инициализацией;
   - добавьте метод, который сбрасывает `_instance` в `None` для тестов.
3. Проанализируйте стандартный модуль `logging`:
   - где там используются идеи Singleton;
   - как организовано глобальное состояние (root‑логгер) и при этом остаётся возможность создавать свои логгеры.

---

### 4.2. Factory Method

#### 4.2.1. Суть паттерна и терминология

- **Factory Method (фабричный метод)** — паттерн, в котором **базовый класс** (или интерфейс) определяет метод для создания объектов, а **подклассы решают, какой конкретный класс возвращать**.
- **Создание через наследование**: выбор конкретного типа **зашит** в подклассах, а не в клиентском коде.
- Отличается от:
  - **Abstract Factory** — там фабрика сама по себе объект, создающий **семейство** связанных объектов;
  - **простого конструктора** — здесь сам «процесс выбора класса» вынесен в отдельный перегружаемый метод.

Задача:

- избавить базовый класс (и клиента) от знания о конкретных подклассах;
- позволить расширять систему добавлением новых подклассов **без изменения существующего кода** (принцип OCP).

---

#### 4.2.2. Классический пример с диалогами и кнопками

```python
from abc import ABC, abstractmethod


class Dialog(ABC):
    """Базовый диалог, не знающий, какие кнопки он рисует."""

    @abstractmethod
    def create_button(self) -> "Button":
        """Фабричный метод: создавать подходящую кнопку."""
        ...

    def render(self) -> None:
        # Общая логика рендера
        print("Rendering dialog frame")
        btn = self.create_button()
        btn.on_click()


class Button(ABC):
    @abstractmethod
    def on_click(self) -> None:
        ...


class WindowsButton(Button):
    def on_click(self) -> None:
        print("Windows button clicked")


class LinuxButton(Button):
    def on_click(self) -> None:
        print("Linux button clicked")


class WindowsDialog(Dialog):
    def create_button(self) -> Button:
        return WindowsButton()


class LinuxDialog(Dialog):
    def create_button(self) -> Button:
        return LinuxButton()
```

Здесь:

- `Dialog.render()` реализует **шаблонный метод** (Template Method) — общий алгоритм рендера диалога;
- `create_button()` — **фабричный метод**, определяемый в подклассах;
- чтобы добавить `MacDialog`, нам не нужно менять `Dialog` — мы просто создаём новый подкласс с другой реализацией `create_button`.

---

#### 4.2.3. Связь с Template Method и SOLID

Factory Method почти всегда идёт в паре с **Template Method**:

- Template Method задаёт **структуру алгоритма**;
- Factory Method — один из шагов этого алгоритма, отвечающий за «какой объект создать».

Связь с SOLID:

- **OCP (Open/Closed Principle)**:
  - чтобы добавить новый тип продукта, мы создаём новый подкласс, а не трогаем существующий код;
- **DIP (Dependency Inversion Principle)**:
  - клиент зависит от абстракции `Dialog` / `Button`, а не от конкретных `WindowsButton` / `LinuxButton`.

---

#### 4.2.4. «Питоничный» вариант: передача фабрики как зависимости

В Python, благодаря **функциям первого класса** и динамической типизации, часто нет смысла создавать отдельный абстрактный класс ради одного метода.

Вместо:

```python
class Dialog(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...
```

можно сделать:

```python
class Dialog:
    def __init__(self, button_factory: "Callable[[], Button]"):
        self._button_factory = button_factory

    def render(self) -> None:
        print("Rendering dialog frame")
        btn = self._button_factory()
        btn.on_click()
```

Использование:

```python
dialog = Dialog(button_factory=WindowsButton)
dialog.render()

dialog2 = Dialog(button_factory=LinuxButton)
dialog2.render()
```

Такой подход:

- сохраняет **идею фабричного метода** (есть точка, где создаётся объект по абстракции);
- но реализует её **через передачу функции/класса** (Strategy/DI), а не через иерархию абстрактных классов.

---

#### 4.2.5. Factory Method в реальных Python‑проектах

Типичные места, где встречается этот паттерн (часто неосознанно):

- **ORM / модели**:
  - базовый репозиторий (`BaseRepository`) может иметь метод `create_entity`, который возвращает экземпляр нужного доменного класса;
  - конкретные репозитории (`UserRepository`, `OrderRepository`) переопределяют `create_entity`.
- **Парсеры и обработчики**:
  - базовый класс `BaseParser` определяет метод `_create_token`, а конкретные парсеры возвращают разные типы токенов.
- **Фреймворки**:
  - базовый класс HTTP‑обработчика может иметь фабричный метод для создания `Response` (JSONResponse, HTMLResponse и т.п.).

Пример с репозиторием:

```python
from abc import ABC, abstractmethod


class Entity: ...


class User(Entity):
    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name


class BaseRepository(ABC):
    @abstractmethod
    def _create_entity(self, row: dict) -> Entity:
        ...

    def get_by_id(self, id_: int) -> Entity | None:
        row = self._fetch_row(id_)
        if row is None:
            return None
        return self._create_entity(row)

    def _fetch_row(self, id_: int) -> dict | None:
        # Имитация запроса к БД
        ...


class UserRepository(BaseRepository):
    def _create_entity(self, row: dict) -> User:
        return User(id_=row["id"], name=row["name"])
```

Здесь `BaseRepository` реализует общий алгоритм загрузки (`get_by_id`), а `_create_entity` — фабричный метод.

---

#### 4.2.6. Когда Factory Method действительно нужен, а когда — лишний слой

**Нужен, когда:**

- есть **базовый класс** с большим объёмом общей логики;
- при этом:
  - разные подклассы должны создавать **разные типы объектов**;
  - логика создания связана с **конкретным подклассом** (другой БД, другой формат, другой тип сущности).

**Лишний, когда:**

- у вас один‑два места создания объекта, и их легко выразить простым вызовом `ClassName(...)`;
- фабричный метод добавляет только «слоёв абстракции», а реальной расширяемости не даёт;
- проще передать конструктор/функцию в качестве параметра (как в варианте с `button_factory`).

Правильный вопрос при проектировании:

> «Мне действительно нужно, чтобы **каждый новый тип** добавлялся через **новый подкласс** с переопределением фабричного метода?  
> Или проще передать функцию/класс как зависимость?»

---

#### 4.2.7. Частые ошибки при использовании Factory Method

- **Смешивание фабричного метода и конструктора без необходимости**  
  Иногда проще написать `@classmethod`‑фабрику:

  ```python
  class User:
      def __init__(self, id_: int, name: str):
          self.id = id_
          self.name = name

      @classmethod
      def from_row(cls, row: dict) -> "User":
          return cls(id_=row["id"], name=row["name"])
  ```

  Это тоже разновидность фабричного метода (на уровне одного класса), но **без иерархии**.

- **Ненужное наследование «ради паттерна»**  
  Создаётся абстрактный класс, хотя достаточно функций/классов‑фабрик; в результате:
  - приходится поддерживать кучу мелких подклассов;
  - новичкам трудно понять, зачем столько абстракций.

- **Нарушение SRP**  
  В базовый класс загружают и бизнес‑логику, и фабрики, и логику хранения, и валидацию.  
  Иногда правильнее:
  - вынести создание объектов в **отдельную фабрику** (см. Abstract Factory / простые фабрики);
  - оставить базовый класс ответственным только за алгоритм.

---

#### 4.2.8. Связь Factory Method с другими приёмами в Python

- **Статические/классовые методы‑фабрики** (как `User.from_row`) — «локальный» Factory Method.
- **Регистрация фабрик** в словаре:

  ```python
  HANDLERS: dict[str, "Callable[[], Handler]"] = {}


  def register_handler(name: str):
      def decorator(cls):
          HANDLERS[name] = cls
          return cls
      return decorator
  ```

  Здесь выбор конкретного класса по имени (или типу) — тоже фабричный подход.

- **dataclasses / pydantic**:
  - методы `from_dict`, `model_validate` и т.п. — по сути, фабричные методы, которые знают, как из внешнего представления создать объект.

---

#### 4.2.9. Упражнения

1. Найдите в своём проекте базовый класс, у которого в подклассах **немного различается только логика создания частей** (например, создаётся разный тип клиента/репозитория/обработчика).  
   Попробуйте:
   - выделить фабричный метод в базовом классе;
   - перенести выбор конкретного типа в подклассы;
   - оцените, стало ли проще добавлять новый вариант.
2. Возьмите существующую реализацию с `if type == "A": ... elif type == "B": ...` внутри метода и попробуйте:
   - сначала сделать Factory Method (абстрактный класс + подклассы);
   - затем переписать на «питоничный» вариант с передачей функции/класса как параметра.  
   Сравните, какой вариант проще читается и тестируется.
3. Реализуйте класс репозитория с фабричным методом `_create_entity`, который:
   - в базовом классе объявлен как абстрактный;
   - в одном подклассе создаёт `User`, в другом — `Order`.  
   Затем напишите тесты, которые:
   - проверяют, что `get_by_id` возвращает правильные типы;
   - при этом сами тесты не знают о внутренней реализации `_create_entity`.

---

### 4.3. Abstract Factory

#### 4.3.1. Суть паттерна и терминология

- **Abstract Factory (абстрактная фабрика)** — паттерн, который предоставляет **интерфейс для создания семейств взаимосвязанных объектов**, не уточняя их конкретные классы.
- **Семейство продуктов** — набор типов, которые логически должны использоваться вместе:
  - `WinButton` + `WinCheckbox` + `WinWindow`;
  - `DarkThemeButton` + `DarkThemeCheckbox`;
  - разные варианты клиентов/репозиториев для разных хранилищ.
- Ключевая идея:
  - у нас есть **одна точка**, где описано, какие конкретные классы составляют это семейство;
  - клиент работает только с **интерфейсом фабрики** и абстрактными продуктами.

Отличие от Factory Method:

- Factory Method — о **перегружаемом методе** в базовом классе, который создаёт **один продукт**;
- Abstract Factory — о **самостоятельном объекте‑фабрике**, который создаёт **множество связанных продуктов**, гарантируя, что они «из одного семейства».

---

#### 4.3.2. Классический пример GUI‑фабрики

```python
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def draw(self) -> None: ...


class Checkbox(ABC):
    @abstractmethod
    def draw(self) -> None: ...


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...


class WinButton(Button):
    def draw(self) -> None:
        print("Drawing Windows button")


class WinCheckbox(Checkbox):
    def draw(self) -> None:
        print("Drawing Windows checkbox")


class MacButton(Button):
    def draw(self) -> None:
        print("Drawing Mac button")


class MacCheckbox(Checkbox):
    def draw(self) -> None:
        print("Drawing Mac checkbox")


class WinFactory(GUIFactory):
    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
```

Клиентский код:

```python
def render_ui(factory: GUIFactory) -> None:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.draw()
    checkbox.draw()
```

Клиенту **всё равно**, какие конкретные классы стоят за `Button` и `Checkbox`. Он знает только:

- что у фабрики есть методы `create_button` и `create_checkbox`;
- что у кнопки и чекбокса есть метод `draw`.

Чтобы добавить, например, `GtkFactory`, достаточно:

- определить `GtkButton`, `GtkCheckbox`;
- создать `GtkFactory`, реализующую интерфейс `GUIFactory`;
- клиентский код менять не нужно.

---

#### 4.3.3. Где Abstract Factory полезен в Python‑коде

Не только GUI. Типичные «семейства»:

- **Клиенты разных внешних сервисов**:
  - `PaymentClient`, `NotificationClient`, `AnalyticsClient` для «боевого» окружения;
  - и такие же, но для «песочницы»/тестов.
- **Разные хранилища**:
  - одна фабрика создаёт `UserRepository`, `OrderRepository`, `ProductRepository` для PostgreSQL;
  - другая — те же интерфейсы, но для Redis / файловой системы / in‑memory.
- **Разные конфигурации фреймворка**:
  - `SyncFactory` → синхронные реализации;
  - `AsyncFactory` → асинхронные реализации тех же интерфейсов.

Пример с репозиториями:

```python
class UserRepository(ABC):
    @abstractmethod
    def get(self, user_id: int) -> dict | None: ...


class OrderRepository(ABC):
    @abstractmethod
    def get(self, order_id: int) -> dict | None: ...


class RepositoryFactory(ABC):
    @abstractmethod
    def create_user_repo(self) -> UserRepository: ...

    @abstractmethod
    def create_order_repo(self) -> OrderRepository: ...
```

Две реализации:

```python
class PostgresUserRepo(UserRepository):
    ...


class PostgresOrderRepo(OrderRepository):
    ...


class InMemoryUserRepo(UserRepository):
    ...


class InMemoryOrderRepo(OrderRepository):
    ...


class PostgresRepoFactory(RepositoryFactory):
    def create_user_repo(self) -> UserRepository:
        return PostgresUserRepo()

    def create_order_repo(self) -> OrderRepository:
        return PostgresOrderRepo()


class InMemoryRepoFactory(RepositoryFactory):
    def create_user_repo(self) -> UserRepository:
        return InMemoryUserRepo()

    def create_order_repo(self) -> OrderRepository:
        return InMemoryOrderRepo()
```

Код сервиса:

```python
class Service:
    def __init__(self, factory: RepositoryFactory):
        self._users = factory.create_user_repo()
        self._orders = factory.create_order_repo()
```

Теперь:

- для продакшена вы передаёте в `Service` `PostgresRepoFactory`;
- для сложных интеграционных тестов — `InMemoryRepoFactory`.

---

#### 4.3.4. «Питоничный» вариант: фабрики как словари/функции

Во многих случаях вместо целой иерархии фабрик хватает **простого словаря функций**:

```python
from typing import Callable


def create_win_button() -> Button:
    return WinButton()


def create_win_checkbox() -> Checkbox:
    return WinCheckbox()


def create_mac_button() -> Button:
    return MacButton()


def create_mac_checkbox() -> Checkbox:
    return MacCheckbox()


FactoryDict = dict[str, Callable[[], object]]


WIN_FACTORY: FactoryDict = {
    "button": create_win_button,
    "checkbox": create_win_checkbox,
}

MAC_FACTORY: FactoryDict = {
    "button": create_mac_button,
    "checkbox": create_mac_checkbox,
}
```

Использование:

```python
def render_ui(factory: FactoryDict) -> None:
    button: Button = factory["button"]()
    checkbox: Checkbox = factory["checkbox"]()
    button.draw()
    checkbox.draw()
```

Такая реализация:

- проще по синтаксису;
- гибче (можно подмешивать свои фабрики, модифицировать словарь);
- особенно удобна, когда нужно **динамически регистрировать** новые типы (плагины).

Но важно **держать семантику семейства**:

- в одном словаре — только совместимые между собой реализации;
- не смешивать, например, WinButton с MacCheckbox.

---

#### 4.3.5. Связь Abstract Factory с DIP и модульной архитектурой

Abstract Factory — удобный инструмент для реализации **DIP (Dependency Inversion Principle)**:

- высокоуровневый код (`Service`) зависит от **абстракции фабрики**;
- конкретный выбор семейства (Postgres, Redis, InMemory) делается:
  - в конфигурации приложения;
  - в точке «сборки» (composition root).

Это особенно важно в:

- многоуровневых системах (UI → Application → Infrastructure);
- библиотечных/фреймворковых сценариях (пользователь должен иметь возможность подключить свои реализации).

---

#### 4.3.6. Отличия Abstract Factory от других паттернов

- **От Factory Method**:
  - Factory Method — это **один метод** в базовом классе;
  - Abstract Factory — **отдельный объект**, который создаёт **семейство продуктов**.
- **От Builder**:
  - Builder фокусируется на **пошаговой сборке сложного объекта**;
  - Abstract Factory — на **согласованности нескольких разных объектов**.
- **От Service Locator (анти‑паттерн)**:
  - фабрика получает зависимости **снаружи** и создаёт объекты явно;
  - Service Locator скрывает, откуда берутся зависимости (см. ниже).

---

#### 4.3.7. Частые ошибки и анти‑паттерны вокруг Abstract Factory

- **Слишком раннее введение фабрик**  
  Создают иерархию фабрик, когда пока есть только **одна реализация** и не видно реальной альтернативы.
  - В результате код усложняется без практической выгоды.
  - Лучше сначала сделать простую реализацию, а фабрику ввести, когда появится второй/третий вариант.

- **Service Locator под видом фабрики**  
  Иногда «фабрику» делают глобальным синглтоном:

  ```python
  class ServiceLocator:
      _factory: RepositoryFactory | None = None
  ```

  и по всему коду обращаются к `ServiceLocator.get_repo("user")`.  
  Это нарушает DIP: зависимость «затащена» внутрь кода, а не передаётся явно.

- **Смешивание разных семей в одной фабрике**  
  Фабрика начинает возвращать **смешанные продукты** (часть из PostgreSQL, часть из Redis), без чёткого понимания, что это разные конфигурации.  
  Правило: один экземпляр фабрики → одно осмысленное семейство.

---

#### 4.3.8. Практические рекомендации по Abstract Factory в Python

1. Используйте **классы‑фабрики**, если:
   - система большая и многослойная;
   - важно явно задокументировать, какие продукты образуют семейство;
   - нужны строгие контракты (ABC, Protocol).
2. Используйте **словари/функции‑фабрики**, если:
   - конфигурация динамическая (плагины, загрузка по имени);
   - нет необходимости в отдельной иерархии классов;
   - при этом вы всё равно придерживаетесь понятия «семейство» (не смешиваете несовместимые конструкции).
3. Выносите создание фабрики в **отдельный слой приложения**:
   - например, модуль `composition`/`bootstrap` создает фабрику в зависимости от настроек;
   - бизнес‑код получает уже готовую фабрику как зависимость (через конструктор).

---

#### 4.3.9. Упражнения

1. В своём проекте определите минимум **два семейства** сущностей, которые логически связаны:
   - разные окружения (prod / staging / test);
   - разные виды хранилищ (SQL / NoSQL / in‑memory).  
   Сформулируйте, какие именно сущности входят в каждое семейство.
2. Спроектируйте `RepositoryFactory` для вашего домена:
   - определите абстрактные интерфейсы репозиториев;
   - реализуйте две фабрики (например, Postgres и InMemory);
   - перепишите один сервис так, чтобы он зависел только от фабрики, а не от конкретных репозиториев.
3. Попробуйте реализовать тот же набор фабрик в двух вариантах:
   - через классы‑фабрики (как в примере выше);
   - через словари/функции‑фабрики.  
   Сравните:
   - где проще добавить новый продукт в семейство;
   - где проще обеспечить типобезопасность (с mypy/pyright).

---

### 4.4. Builder

#### 4.4.1. Суть паттерна и терминология

- **Builder (строитель)** — паттерн, который отделяет **пошаговый процесс конструирования сложного объекта** от его **итогового представления**.
- Основные участники:
  - **Product** — объект, который мы строим (готовый результат);
  - **Builder** — объект, который:
    - принимает параметры по шагам;
    - хранит промежуточное состояние;
    - умеет создать/вернуть готовый Product (`build()` / `get_result()`).
  - (опционально) **Director** — объект, который знает, **какие шаги и в каком порядке** надо вызывать у Builder, чтобы получить конкретную конфигурацию продукта.

Когда Builder полезен:

- объект имеет много параметров, часть которых:
  - опциональна;
  - зависит одна от другой;
  - формируется из разных источников в разное время;
- создание нужно разбить на **осмысленные шаги**, а не на гигантский конструктор.

---

#### 4.4.2. Простой пример: построение SQL‑запроса

```python
class Query:
    def __init__(self, table: str, fields: list[str], where: str | None = None):
        self.table = table
        self.fields = fields
        self.where = where

    def __str__(self) -> str:
        base = f"SELECT {', '.join(self.fields)} FROM {self.table}"
        if self.where:
            base += f" WHERE {self.where}"
        return base


class QueryBuilder:
    def __init__(self, table: str):
        self._table = table
        self._fields: list[str] = ["*"]
        self._where: list[str] = []

    def select(self, *fields: str) -> "QueryBuilder":
        """Задать список полей SELECT."""
        if fields:
            self._fields = list(fields)
        return self

    def where(self, condition: str) -> "QueryBuilder":
        """Добавить условие WHERE (объединяются через AND)."""
        self._where.append(condition)
        return self

    def build(self) -> Query:
        where = " AND ".join(self._where) if self._where else None
        return Query(self._table, self._fields, where)


q = (
    QueryBuilder("users")
    .select("id", "name")
    .where("id > 10")
    .where("active = 1")
    .build()
)
print(q)  # SELECT id, name FROM users WHERE id > 10 AND active = 1
```

Здесь:

- мы можем вызывать `select` и `where` в любом порядке, несколько раз;
- `build()` создаёт неизменяемый объект `Query`, который представляет конечный результат.

---

#### 4.4.3. Builder vs большой конструктор

Часто встречающийся анти‑пример:

```python
class Report:
    def __init__(
        self,
        user_id: int,
        start_date: str,
        end_date: str,
        include_charts: bool,
        include_raw_data: bool,
        format: str,
        timezone: str,
        locale: str,
        filters: dict | None = None,
        # ... ещё десяток параметров ...
    ):
        ...
```

Проблемы:

- сигнатура конструктора практически нечитаема;
- легко перепутать порядок аргументов;
- часть параметров взаимозависимы (например, `format` влияет на то, какие другие поля допустимы);
- невозможно на уровне типа/интерфейса выразить, что некоторые шаги **обязательны**.

Builder позволяет:

- разбить создание на **осмысленные шаги** (`for_user`, `with_period`, `with_format` и т.д.);
- валидировать конфигурацию **перед `build()`**, выбрасывая ошибки, если чего‑то не хватает.

---

#### 4.4.4. Пример: Builder для отчёта

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Report:
    user_id: int
    start_date: str
    end_date: str
    include_charts: bool
    include_raw_data: bool
    format: str


class ReportBuilder:
    def __init__(self) -> None:
        self._user_id: int | None = None
        self._start_date: str | None = None
        self._end_date: str | None = None
        self._include_charts: bool = False
        self._include_raw_data: bool = False
        self._format: str = "pdf"

    def for_user(self, user_id: int) -> "ReportBuilder":
        self._user_id = user_id
        return self

    def between(self, start_date: str, end_date: str) -> "ReportBuilder":
        self._start_date = start_date
        self._end_date = end_date
        return self

    def with_charts(self, enabled: bool = True) -> "ReportBuilder":
        self._include_charts = enabled
        return self

    def with_raw_data(self, enabled: bool = True) -> "ReportBuilder":
        self._include_raw_data = enabled
        return self

    def as_format(self, fmt: str) -> "ReportBuilder":
        if fmt not in {"pdf", "xlsx"}:
            raise ValueError("Unsupported format")
        self._format = fmt
        return self

    def build(self) -> Report:
        if self._user_id is None:
            raise ValueError("user_id is required")
        if self._start_date is None or self._end_date is None:
            raise ValueError("start_date and end_date are required")
        return Report(
            user_id=self._user_id,
            start_date=self._start_date,
            end_date=self._end_date,
            include_charts=self._include_charts,
            include_raw_data=self._include_raw_data,
            format=self._format,
        )
```

Использование:

```python
builder = (
    ReportBuilder()
    .for_user(123)
    .between("2025-01-01", "2025-01-31")
    .with_charts()
    .as_format("xlsx")
)
report = builder.build()
```

Преимущества:

- читабельный и самодокументирующийся код;
- в `build()` можно централизованно валидировать все зависимости;
- итоговый `Report` — **иммутабельный** (через `@dataclass(frozen=True)`).

---

#### 4.4.5. Director (директор) — нужен ли он в Python?

В классическом описании паттерна есть `Director`, который:

- знает, **какие шаги** у Builder вызвать и в каком порядке;
- сам Builder не знает последовательности шагов — он только предоставляет операции.

Пример (упрощённо):

```python
class ReportDirector:
    def __init__(self, builder: ReportBuilder):
        self._builder = builder

    def build_monthly_user_report(self, user_id: int, month: int, year: int) -> Report:
        start = f"{year}-{month:02d}-01"
        end = f"{year}-{month:02d}-31"
        return (
            self._builder
            .for_user(user_id)
            .between(start, end)
            .with_charts()
            .as_format("pdf")
            .build()
        )
```

В Python чаще делают **функцию‑фасад** вместо отдельного класса Director:

```python
def build_monthly_user_report(user_id: int, month: int, year: int) -> Report:
    builder = ReportBuilder()
    start = f"{year}-{month:02d}-01"
    end = f"{year}-{month:02d}-31"
    return (
        builder
        .for_user(user_id)
        .between(start, end)
        .with_charts()
        .as_format("pdf")
        .build()
    )
```

То есть роль Director выполняет:

- отдельная функция,
- или метод сервиса/фасада.

---

#### 4.4.6. «Питоничные» альтернативы Builder

Не всегда стоит вводить отдельный объект‑строитель. Альтернативы:

- **Ключевые аргументы с разумными значениями по умолчанию**:

  ```python
  class Report:
      def __init__(
          self,
          user_id: int,
          start_date: str,
          end_date: str,
          include_charts: bool = False,
          include_raw_data: bool = False,
          fmt: str = "pdf",
      ):
          ...
  ```

  При использовании именованных аргументов (`Report(user_id=1, start_date=..., ...)`) проблема «адского конструктора» частично снимается.

- **`dataclasses` + `replace`**:

  ```python
  from dataclasses import dataclass, replace


  @dataclass
  class Config:
      host: str = "localhost"
      port: int = 8000
      debug: bool = False


  base = Config()
  dev = replace(base, debug=True, port=8001)
  ```

  Можно рассматривать `replace` как микро‑Builder: из базовой конфигурации получаем вариации.

Тем не менее Builder особенно полезен, когда:

- **части конфигурации собираются в разных местах кода и/или в разное время**;
- требуется строгий контроль «обязательных шагов» до `build()`.

---

#### 4.4.7. Частые ошибки при использовании Builder

- **Хранить в Builder объект продукта и модифицировать его напрямую**  
  Тогда вы по сути получаете «мутабельный продукт», и Builder теряет смысл:
  - продукт оказывается «наполовину сконструированным» и может «утечь» в таком виде;
  - больше похоже на анемичный объект с кучей сеттеров.

  Лучше:
  - хранить **поля конфигурации** в Builder;
  - создавать Product только внутри `build()`/`get_result()`.

- **Позволять использовать `build()` в любом состоянии**  
  Если `build()` не проверяет, что требуемые поля установлены, легко получить полуконсистентный объект.
  - всегда валидируйте состояние Builder в `build()` и бросайте осмысленные исключения.

- **Использовать Builder там, где достаточно словаря/конфига**  
  Для простых наборов параметров (например, конфиг для запроса к API) иногда проще передать `dict`/`TypedDict`/`pydantic`‑модель, чем городить отдельный Builder.

---

#### 4.4.8. Связь Builder с другими паттернами

- С **Abstract Factory**:
  - Abstract Factory создаёт **варианты продуктов** из одного семейства;
  - Builder — по шагам собирает **один сложный продукт** (даже если фабрики используются внутри него).
- С **Prototype**:
  - Builder можно инициализировать из Prototype (`from_prototype(proto).with_change(...).build()`), чтобы изменять только часть параметров.
- С **Facade**:
  - Builder нередко скрыт внутри фасада: фасад предоставляет простые методы высокого уровня, которые внутри строят продукт с помощью Builder.

---

#### 4.4.9. Упражнения

1. Найдите в своём коде класс с «толстым» конструктором (много аргументов, особенно логически связанных).  
   Попробуйте:
   - выделить Builder;
   - перенести в него логику валидации конфигурации;
   - сделать сам продукт `@dataclass(frozen=True)` и сравнить читаемость.
2. Реализуйте Builder для сложного HTTP‑запроса:
   - обязательные поля: метод, URL;
   - опциональные: заголовки, параметры query‑строки, тело, таймауты, ретраи;
   - `build()` должен возвращать, например, `requests.Request` или вашу обёртку.  
   Добавьте валидацию (нельзя одновременно задать JSON‑тело и form‑data и т.п.).
3. Реализуйте две функции‑Director:
   - `build_get_user_request(user_id: int)`;
   - `build_search_request(query: str, page: int)`.  
   Обе должны использовать один и тот же Builder, но настраивать его по‑разному.

---

### 4.5. Prototype

#### 4.5.1. Суть паттерна Prototype

- **Prototype (прототип)** — паттерн, который предлагает создавать новые объекты **путём клонирования уже существующих**, а не через конструктор с множеством параметров.
- Прототип играет роль «образца», от которого можно быстро получать:
  - точные копии;
  - слегка модифицированные варианты.

Когда это нужно:

- конструктор объекта:
  - дорогой (много вычислений, запросов к БД, валидаций);
  - сложный (много параметров, завязанных друг на друга);
- в системе есть «типовые» конфигурации, от которых часто делают «вариации».

В Python есть встроенная поддержка копирования (`copy.copy`, `copy.deepcopy`), поэтому реализация Prototype получается довольно естественной.

---

#### 4.5.2. Поверхностная и глубокая копия

Важно различать:

- **поверхностная копия (shallow copy)**:
  - создаётся новый контейнер (список, словарь, объект);
  - **ссылки на вложенные объекты копируются как есть**;
  - изменения **внутри вложенных объектов** видны и в оригинале, и в копии.
- **глубокая копия (deep copy)**:
  - рекурсивно копирует объект и все вложенные объекты;
  - оригинал и копия полностью независимы (если нет специальных исключений).

В Python:

```python
import copy

shallow = copy.copy(obj)
deep = copy.deepcopy(obj)
```

Для Prototype обычно:

- выбирают **shallow copy**, если:
  - вложенные объекты иммутабельны (строки, числа, кортежи…);
  - либо по смыслу должны разделяться (общий кэш/конфиг).
- выбирают **deep copy**, если:
  - прототип должен быть **полностью независим**;
  - в нём много изменяемых структур (`list`, `dict`, `set`…).

---

#### 4.5.3. Базовый пример Prototype в Python

```python
import copy


class Shape:
    def __init__(self, x: int, y: int, color: str, tags: list[str] | None = None):
        self.x = x
        self.y = y
        self.color = color
        self.tags = tags or []

    def clone(self) -> "Shape":
        # По умолчанию сделаем глубокую копию, чтобы теги были независимы
        return copy.deepcopy(self)
```

Использование:

```python
base = Shape(0, 0, "red", tags=["draggable"])
clone = base.clone()

clone.x = 10
clone.tags.append("selected")

print(base.x)        # 0 — позиция не изменилась
print(base.tags)     # ['draggable'] — теги независимы
print(clone.tags)    # ['draggable', 'selected']
```

Если вместо `deepcopy` использовать `copy.copy`, `tags` были бы **общими**, что не всегда желаемо.

---

#### 4.5.4. Кастомизация `__copy__` и `__deepcopy__`

Модуль `copy` вызывает специальные методы:

- `__copy__(self)` — для `copy.copy(self)`;
- `__deepcopy__(self, memo)` — для `copy.deepcopy(self)`.

Вы можете управлять тем:

- что считать «копией» объекта;
- какие части состояния копировать, а какие — разделять.

```python
class Config:
    def __init__(self, name: str, options: dict[str, str] | None = None):
        self.name = name
        self.options = options or {}

    def __copy__(self):
        # Поверхностная копия: новый объект, но options разделяется
        new = type(self)(self.name, self.options)
        return new

    def __deepcopy__(self, memo):
        # Глубокая копия: копируем и словарь options
        import copy

        new = type(self)(self.name, copy.deepcopy(self.options, memo))
        return new
```

Далее `clone()` можно сделать просто обёрткой над `copy.copy` или `copy.deepcopy`.

---

#### 4.5.5. Прототипы и реестры прототипов

Классический сценарий: есть **реестр прототипов**, откуда можно достать образец и клонировать его:

```python
import copy


class PrototypeRegistry:
    def __init__(self):
        self._prototypes: dict[str, object] = {}

    def register(self, name: str, prototype: object) -> None:
        self._prototypes[name] = prototype

    def unregister(self, name: str) -> None:
        self._prototypes.pop(name, None)

    def clone(self, name: str, **changes):
        """Склонировать прототип и применить изменения к атрибутам."""
        proto = self._prototypes[name]
        obj = copy.deepcopy(proto)
        for attr, value in changes.items():
            setattr(obj, attr, value)
        return obj
```

Использование:

```python
registry = PrototypeRegistry()
registry.register("default_user", {"role": "user", "active": True})

admin = registry.clone("default_user", role="admin")
print(admin)  # {'role': 'admin', 'active': True}
```

Здесь:

- «прототипом» может быть не только объект класса, но и словарь/конфиг;
- PrototypeRegistry играет роль **фабрики на основе прототипов**.

---

#### 4.5.6. Где Prototype реально полезен в Python

- **GUI / визуальные редакторы**:
  - есть базовые элементы (кнопка, текстовое поле) с набором стилей/свойств;
  - пользователь копирует элемент и слегка меняет его;
  - проще клонировать существующий объект, чем заново собирать из параметров.

- **Игры / симуляторы**:
  - прототипы врагов, снарядов, объектов окружения;
  - при создании новой сущности мы:
    - клонируем прототип;
    - меняем только позицию/состояние.

- **Конфигурации и шаблоны**:
  - есть базовая конфигурация (`base_dev_config`);
  - различные окружения (test/stage/prod) получают конфиги через глубокое копирование прототипа + локальные изменения.

- **Кеширование сложных вычислений**:
  - объект создаётся один раз (дорого);
  - затем для похожих случаев делаются клоны с небольшими изменениями.

---

#### 4.5.7. Prototype vs Builder vs Abstract Factory

- **Prototype**:
  - создаёт новые объекты **через копирование** существующего;
  - хорошо подходит, когда уже есть **готовый эталонный объект**.
- **Builder**:
  - создаёт объекты **с нуля, по шагам**;
  - полезен, когда важен **процесс конструирования**.
- **Abstract Factory**:
  - создаёт **семейства** разных объектов;
  - акцент на согласованности разных типов, а не на копировании.

Комбинация:

- фабрика может внутри себя держать **прототипы** и клонировать их;
- Builder может иметь метод `from_prototype`, который заполняет часть полей из прототипа, а часть — достраивает.

---

#### 4.5.8. Потенциальные проблемы и анти‑паттерны с Prototype

- **Скрытые зависимости в состоянии**  
  При поверхностной копии прототип и его клоны могут разделять:
  - списки;
  - словари;
  - другие изменяемые объекты.  
  Из‑за этого изменения в одном объекте неожиданно отражаются в другом.

  Всегда явно решайте:
  - какие части состояния должны быть **общими**;
  - какие — **независимыми** (и копируйте их глубоко).

- **Огромные объекты и дорогой deepcopy**  
  `copy.deepcopy` может быть дорогим по времени и памяти:
  - для больших графов объектов;
  - при наличии сложных взаимных ссылок.  
  Возможно, выгоднее:
  - делать частичную копию (только части дерева);
  - или хранить состояние в более простой структуре (например, dataclass + неизменяемые вложенные объекты).

- **Неочевидные правила копирования**  
  Если в классе определены хитрые `__copy__`/`__deepcopy__`, другим разработчикам сложно понять, **что именно копируется, а что нет**.  
  Документируйте это в docstring’ах и комментариях.

---

#### 4.5.9. Практические рекомендации

1. Для простых случаев достаточно:
   - реализовать метод `clone(self)`, который внутри вызывает `copy.copy` или `copy.deepcopy`;
   - или использовать `dataclasses.replace` для dataclass’ов.
2. Если класс сложный:
   - явно реализуйте `__copy__` и/или `__deepcopy__`;
   - документируйте, какие поля копируются как есть, а какие — рекурсивно.
3. Для конфигов и шаблонов:
   - используйте прототипы на базе простых структур (`dict`, `list`, dataclass);
   - делайте функции `make_config_from_prototype(prototype, **overrides)`.

---

#### 4.5.10. Упражнения

1. Возьмите объект из своего проекта, который часто создаётся «почти таким же, как другой, но с парой отличий».  
   Реализуйте для него:
   - метод `clone`, использующий `copy.copy`;
   - затем вариант с `copy.deepcopy`, и сравните поведение при изменении вложенных структур.
2. Реализуйте `PrototypeRegistry` для:
   - шаблонов HTTP‑запросов (метод, базовый URL, общие заголовки);
   - или конфигураций сервисов.  
   Добавьте метод `clone(name, **overrides)`, который:
   - делает глубокую копию прототипа;
   - применяет переопределения (например, изменяет часть заголовков).
3. Для класса с большим числом полей реализуйте:
   - `__copy__`, который делает поверхностную копию;
   - `__deepcopy__`, который копирует только часть полей глубоко (например, списки), а часть оставляет общей (например, ссылку на общий кеш).  
   Протестируйте, что изменения в копии влияют только на те части, которые вы хотели сделать общими.

---

## 5. Структурные паттерны (§67)
