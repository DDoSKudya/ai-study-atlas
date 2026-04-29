[← Назад к индексу части XIII](index.md)


Поведенческие паттерны описывают **как объекты взаимодействуют**, кто за что отвечает и как меняются алгоритмы или реакции системы.

### 6.1. Chain of Responsibility

**Вопрос:** как передавать запрос по цепочке обработчиков, пока кто‑то его не обработает?

**Идея:** каждый обработчик либо:

- обрабатывает запрос,
- либо передаёт дальше по цепочке.

```python
class Handler:
    def __init__(self, next_: "Handler | None" = None):
        self._next = next_

    def handle(self, request: str) -> None:
        handled = self._process(request)
        if not handled and self._next:
            self._next.handle(request)

    def _process(self, request: str) -> bool:
        raise NotImplementedError


class AuthHandler(Handler):
    def _process(self, request: str) -> bool:
        if request == "auth":
            print("Auth handled")
            return True
        return False


class LoggingHandler(Handler):
    def _process(self, request: str) -> bool:
        print(f"Logging: {request}")
        return False
```

Построение цепочки:

```python
chain = AuthHandler(LoggingHandler())
chain.handle("auth")
chain.handle("other")
```

Где полезно:

- обработка HTTP‑запросов (middleware‑цепочки);
- фильтры и валидация.

---

### 6.2. Command

**Вопрос:** как представить операцию (запрос) как **объект**, чтобы:

- хранить историю;
- выполнять отложенно;
- отменять.

**Идея:** объект Command инкапсулирует:

- **действие** (`execute`);
- (опционально) **откат** (`undo`).

```python
class Command:
    def execute(self) -> None:
        raise NotImplementedError

    def undo(self) -> None:
        raise NotImplementedError


class TextEditor:
    def __init__(self):
        self.text = ""


class AddTextCommand(Command):
    def __init__(self, editor: TextEditor, text: str):
        self._editor = editor
        self._text = text
        self._prev_len = 0

    def execute(self) -> None:
        self._prev_len = len(self._editor.text)
        self._editor.text += self._text

    def undo(self) -> None:
        self._editor.text = self._editor.text[: self._prev_len]
```

Можно делать стек команд и реализовать `undo/redo`.

В Python вместо выделенного класса для каждой команды часто используют:

- обычные функции (callables) + историю аргументов;
- или `dataclass` с `__call__`.

---

### 6.3. Iterator

В Python **Iterator** и так встроен в язык:

- протокол `__iter__` / `__next__`;
- генераторы (`yield`).

**Задача паттерна:** отделить **способ обхода коллекции** от самой коллекции.

```python
class MyRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1
```

Пользователь не знает, как именно реализован обход — он видит только «итерируемость».

---

### 6.4. Mediator

**Вопрос:** как уменьшить количество **прямых ссылок** между объектами, чтобы они не «знали» друг о друге слишком много?

**Идея:** объекты общаются через **посредника** (Mediator), а не напрямую.

```python
class ChatRoom:
    def __init__(self):
        self._users: list["User"] = []

    def join(self, user: "User") -> None:
        self._users.append(user)
        self.broadcast("system", f"{user.name} joined")

    def broadcast(self, sender: str, message: str) -> None:
        for user in self._users:
            if user.name != sender:
                user.receive(sender, message)


class User:
    def __init__(self, name: str, room: ChatRoom):
        self.name = name
        self._room = room

    def send(self, message: str) -> None:
        self._room.broadcast(self.name, message)

    def receive(self, sender: str, message: str) -> None:
        print(f"{self.name} <- {sender}: {message}")
```

Польза:

- новые правила общения можно добавлять/менять **в одном месте** (`ChatRoom`);
- объекты типа `User` не тянут прямых зависимостей друг на друга.

---

### 6.5. Memento

**Вопрос:** как **сохранять и восстанавливать** состояние объекта, не раскрывая его внутренности?

**Идея:** объект‑снимок (Memento) хранит внутреннее состояние; Originator умеет:

- сохранить («создать мементо»),
- восстановить из него.

```python
class EditorMemento:
    def __init__(self, text: str, cursor_pos: int):
        self.text = text
        self.cursor_pos = cursor_pos


class Editor:
    def __init__(self):
        self.text = ""
        self.cursor_pos = 0

    def write(self, text: str) -> None:
        self.text += text
        self.cursor_pos = len(self.text)

    def save(self) -> EditorMemento:
        return EditorMemento(self.text, self.cursor_pos)

    def restore(self, memento: EditorMemento) -> None:
        self.text = memento.text
        self.cursor_pos = memento.cursor_pos
```

Хранить историю можно в списке мементо.

---

### 6.6. Observer

**Вопрос:** как уведомлять **много подписчиков** об изменении объекта?

**Идея:** «издатель» (subject) хранит список подписчиков и уведомляет их при изменении.

```python
class Observable:
    def __init__(self):
        self._observers: list["Observer"] = []

    def attach(self, observer: "Observer") -> None:
        self._observers.append(observer)

    def detach(self, observer: "Observer") -> None:
        self._observers.remove(observer)

    def _notify(self, data) -> None:
        for obs in self._observers:
            obs.update(data)


class Observer:
    def update(self, data) -> None:
        raise NotImplementedError


class PrintObserver(Observer):
    def update(self, data) -> None:
        print(f"Got update: {data}")
```

Применение:

- события GUI;
- бизнес‑события (событийные шины, pub/sub).

В Python часто реализуют через:

- сигналы (например, в Django);
- callbacks / event emitter.

---

### 6.7. State

**Вопрос:** как менять поведение объекта в зависимости от **его текущего состояния**, не плодя `if status == ...` по всему коду?

**Идея:** выносить состояния в **отдельные объекты**, между которыми переключается контекст.

```python
class State:
    def handle(self, ctx: "Context") -> None:
        raise NotImplementedError


class Context:
    def __init__(self, state: State):
        self.state = state

    def request(self) -> None:
        self.state.handle(self)


class ConcreteStateA(State):
    def handle(self, ctx: Context) -> None:
        print("State A handling, switching to B")
        ctx.state = ConcreteStateB()


class ConcreteStateB(State):
    def handle(self, ctx: Context) -> None:
        print("State B handling, switching to A")
        ctx.state = ConcreteStateA()
```

В Python простые случаи State часто выражают:

- словарём из состояния в функцию;
- или отдельными методами + диспетчеризацией.

---

### 6.8. Strategy

**Вопрос:** как легко подменять **алгоритм**, не переписывая клиентский код?

**Идея:** разные стратегии реализуют единый интерфейс, контекст **принимает стратегию как зависимость**.

```python
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def apply(self, numbers: list[int]) -> int: ...


class SumStrategy(Strategy):
    def apply(self, numbers: list[int]) -> int:
        return sum(numbers)


class MaxStrategy(Strategy):
    def apply(self, numbers: list[int]) -> int:
        return max(numbers)


class Stats:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def compute(self, numbers: list[int]) -> int:
        return self._strategy.apply(numbers)
```

В Python Strategy часто = **просто функция**:

```python
def compute(numbers: list[int], op) -> int:
    return op(numbers)

compute([1, 2, 3], sum)
compute([1, 2, 3], max)
```

---

### 6.9. Template Method

**Вопрос:** как задать «скелет алгоритма», оставив некоторые шаги на реализацию подклассов?

**Идея:** базовый класс реализует алгоритм, вызывая **абстрактные/перегружаемые шаги**.

```python
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process(self) -> None:
        data = self.load()
        data = self.transform(data)
        self.save(data)

    @abstractmethod
    def load(self):
        ...

    @abstractmethod
    def transform(self, data):
        ...

    @abstractmethod
    def save(self, data):
        ...
```

Подклассы реализуют шаги.  
Template Method часто используется совместно с Factory Method и Strategy.

---

### 6.10. Interpreter (Интерпретатор)

#### 6.10.1. Когда нужен Interpreter

**Идея:** описать **простый язык или мини‑DSL** (Domain‑Specific Language) в виде набора классов, а затем реализовать «интерпретацию» этих объектов.

Типичные задачи:

- парсить и исполнять:
  - простые формулы (`1 + 2 * 3`);
  - фильтры (`status == 'active' AND age > 18`);
  - мини‑языки конфигурации;
- отделить:
  - **синтаксис** (структуру выражения);
  - **семантику** (как это выражение вычислять/исполнять).

В Python часто вместо полноценного Interpreter:

- используют уже готовые инструменты (`ast`, `eval`, библиотеки парсинга);
- но идея полезна, когда нужен **контролируемый, безопасный и расширяемый** мини‑язык.

---

#### 6.10.2. Простой пример: арифметические выражения

Опишем язык выражений:

- константа (`Number`);
- сложение (`Add`);
- умножение (`Mul`).

```python
class Expr:
    def interpret(self) -> int:
        raise NotImplementedError


class Number(Expr):
    def __init__(self, value: int):
        self.value = value

    def interpret(self) -> int:
        return self.value


class Add(Expr):
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() + self.right.interpret()


class Mul(Expr):
    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() * self.right.interpret()
```

Использование:

```python
# Выражение: (1 + 2) * 3
expr = Mul(
    Add(Number(1), Number(2)),
    Number(3),
)

print(expr.interpret())  # 9
```

Здесь:

- каждый класс представляет **нетерминал** грамматики;
- метод `interpret` реализует **семантику** для данного элемента языка;
- структура классов напоминает **AST (абстрактное синтаксическое дерево)**.

---

#### 6.10.3. Interpreter vs Visitor vs AST + функции

- **Interpreter**:
  - логика вычисления зашита в методы самих узлов (`interpret`);
  - чтобы добавить новую операцию (например, pretty‑print), нужно:
    - либо добавлять метод во все классы;
    - либо переходить к Visitor.

- **Visitor**:
  - узлы дерева знают только, как принять Visitor;
  - разные операции (eval, print, optimize) оформляются как разные visitor’ы;
  - удобно, когда нужно добавлять много разных операций над одним и тем же AST.

- **AST + функции**:
  - узлы — простые контейнеры (dataclass’ы);
  - логика интерпретации вынесена в одну или несколько функций, которые обходят дерево;
  - для Python это часто самый простой путь.

Пример AST + функции вместо классического Interpreter:

```python
from dataclasses import dataclass
from typing import Union


@dataclass
class Num:
    value: int


@dataclass
class AddExpr:
    left: "Expr"
    right: "Expr"


@dataclass
class MulExpr:
    left: "Expr"
    right: "Expr"


Expr = Union[Num, AddExpr, MulExpr]


def eval_expr(expr: Expr) -> int:
    if isinstance(expr, Num):
        return expr.value
    if isinstance(expr, AddExpr):
        return eval_expr(expr.left) + eval_expr(expr.right)
    if isinstance(expr, MulExpr):
        return eval_expr(expr.left) * eval_expr(expr.right)
    raise TypeError(f"Unknown expr: {expr!r}")
```

Это не чистый GoF‑Interpreter, но в духе Python — AST + интерпретирующая функция.

---

#### 6.10.4. Где Interpreter полезен на практике

- **Конфигурационные DSL**:
  - собственный формат конфигураций с условиями и выражениями;
  - правила валидации или «правила бизнеса», описанные не в коде, а во внешнем языке.

- **Фильтры и правила**:
  - язык фильтрации (`field > 10 AND (status = "active" OR status = "pending")`);
  - язык правил для антифрода, скоринга, маршрутизации.

- **Математические/логические выражения**:
  - калькуляторы, формулы в приложениях (финансы, наука);
  - безопасная альтернатива `eval`, когда нельзя пускать произвольный Python‑код.

Во всех этих случаях:

- выгодно иметь **чёткую модель языка** (классы/AST);
- легко расширять его (добавлять новые типы выражений);
- можно реализовывать несколько разных «интерпретаций»:
  - вычисление значения;
  - генерация SQL;
  - генерация кода на другом языке.

---

#### 6.10.5. Ограничения и альтернативы

Минусы классического Interpreter:

- при усложнении языка число классов быстро растёт;
- трудно поддерживать, если:
  - грамматика большая;
  - нужно много разных проходов (оптимизации, разные виды вывода).

Альтернативы в Python:

- модуль `ast`:
  - можно использовать встроенный парсер Python, а затем интерпретировать/трансформировать AST;
- библиотеки парсинга (`lark`, `ply`, `parsimonious`, `antlr` и др.):
  - описываете грамматику отдельно, код генерации AST и интерпретации — отдельно;
- **таблично‑управляемые правила**:
  - когда язык слишком простой, вместо классового AST можно хранить правила в виде структур данных (словари, списки) и интерпретировать их функцией.

---

#### 6.10.6. Упражнения

1. Опишите мини‑язык логических выражений:
   - `Var(name)`, `And(left, right)`, `Or(left, right)`, `Not(expr)`;  
   Реализуйте:
   - классовую модель (интерпретатор через методы `interpret(context: dict[str, bool]) -> bool`);
   - затем вариант через dataclass’ы + отдельную функцию `eval_expr`.
2. Реализуйте простой язык фильтрации для списка словарей:
   - выражения вида `Eq(field, value)`, `Gt(field, value)`, `And`, `Or`;  
   Реализуйте интерпретатор, который применяет выражение к элементу словаря и возвращает `True/False`.
3. Подумайте, для какой задачи в вашем проекте сейчас используется:
   - либо сложный набор `if/elif` по строковым правилам;
   - либо потенциально опасный `eval`.  
   Сформулируйте, можно ли заменить это небольшим DSL на основе Interpreter, с явной моделью и контролируемой семантикой.

---

### 6.11. Visitor

**Вопрос:** как добавлять новые операции над **иерархией классов**, не меняя сами классы?

**Идея:** объект Visitor посещает элементы структуры, а каждый элемент знает, **как себя принять**.

Пример для простого AST:

```python
class Node:
    def accept(self, visitor: "Visitor"):
        raise NotImplementedError


class Number(Node):
    def __init__(self, value: int):
        self.value = value

    def accept(self, visitor: "Visitor"):
        return visitor.visit_number(self)


class Add(Node):
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right

    def accept(self, visitor: "Visitor"):
        return visitor.visit_add(self)


class Visitor:
    def visit_number(self, node: Number):
        raise NotImplementedError

    def visit_add(self, node: Add):
        raise NotImplementedError


class EvalVisitor(Visitor):
    def visit_number(self, node: Number):
        return node.value

    def visit_add(self, node: Add):
        return node.left.accept(self) + node.right.accept(self)
```

Visitor полезен, когда:

- есть сложная иерархия (дерево классов), а операций над ней становится много;
- иерархию менять тяжело (например, это часть публичного API).

В Python Visitor часто реализуется:

- через `functools.singledispatch` по типу узла;
- через паттерн «двойная диспетчеризация» (`visit_<typename>` + `getattr`).

---

## 7. Pythonic‑паттерны (§69)
