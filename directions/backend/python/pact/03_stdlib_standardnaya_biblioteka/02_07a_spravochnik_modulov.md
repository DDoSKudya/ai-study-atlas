[← Назад к индексу части III](index.md)

## 7a. Модули стандартной библиотеки — справочник

> Полный перечень модулей stdlib по категориям. Подробнее по темам — в соответствующих разделах (§8–§15).

### Специальные и встроенные

****future** — фичи из будущих версий**

- [ ] **Что такое и зачем:** модуль ****future**** позволяет включать в текущей версии Python поведение, которое по умолчанию станет стандартным в **следующих** версиях. Импорт **обязательно** в начале файла (после docstring и комментариев); иначе **SyntaxError**. Используется для постепенной миграции кода и для совместимости одного кода с Py2 и Py3.
- [ ] **annotations** (PEP 563, 3.7+): аннотации типов хранятся как **строки** и не вычисляются при загрузке модуля. Позволяет использовать типы, объявленные позже в файле (forward references), и уменьшает время старта. С 3.10+ по умолчанию в некоторых контекстах; с 3.11 **from **future** import annotations** делает все аннотации отложенными. **Пример:** `def f() -> "MyClass":` без кавычек при annotations — **MyClass** не обязан существовать в момент определения. **Пошагово (annotations):** при загрузке модуля с **from **future** import annotations** каждое объявление **def f() -> MyClass:** превращается во внутреннее хранение **'MyClass'** (строка); при вызове **typing.get_type_hints(f)** или при проверке типов (mypy, pyright) строка разрешается в класс **MyClass** по текущему глобальному namespace модуля. Без ****future**** аннотации вычисляются при определении функции, и **MyClass** должен быть уже определён (или в кавычках).
- [ ] **division** (Py2): `/` — истинное деление (2/3 → 0.666...); `//` — целочисленное. В Py3 `/` уже всегда истинное; в Py2 `from __future__ import division` даёт такое же поведение.
- [ ] **print_function** (Py2): `print` становится функцией (скобки обязательны). В Py3 уже по умолчанию; в Py2 импорт позволяет писать `print(x)` и использовать `file=`, `sep=`, `end=`.
- [ ] **generator_stop** (3.5+): при завершении генератора в **yield from** выбрасывается **StopIteration** с атрибутом **value**; внутри подгенератора **return value** порождает именно это. Нужно для корректной передачи значения из вложенного генератора.
- [ ] **barry_as_FLUFL** (шутка): альтернативный оператор `<>` для «не равно»; на практике не используется.
- [ ] **Применения:** единый код для Py2/Py3 (division, print_function); уменьшение времени загрузки и циклических импортов (annotations); подготовка к следующей мажорной версии.

**Пример __future__**

```python
# В начале файла (после docstring)
from __future__ import annotations
class Node:
    def __init__(self, value: int, left: Node | None = None, right: Node | None = None):
        self.value = value
        self.left = left
        self.right = right
# Аннотации не вычисляются при загрузке — Node можно ссылаться до определения
def get_value(n: Node) -> int:
    return n.value
# В Py2 для истинного деления и print как функции:
# from __future__ import division, print_function
# print(2 / 3)  # 0.666...
```

****main** — точка входа**

- [ ] **Что такое и зачем:** при запуске скрипта **python script.py** или **python -m package.module** интерпретатор присваивает специальной переменной ****name**** значение **'**main**'** в запущенном модуле. В **импортированных** модулях ****name**** равен имени модуля (например **'package.module'**). Это позволяет в одном файле совмещать **определения** (классы, функции) и **код запуска** (тесты, CLI): код в блоке **if **name** == '**main**':** выполняется только при прямом запуске, а не при импорте.
- [ ] **Типичное использование:** в конце модуля писать **if **name** == '**main**':** и внутри вызывать **main()** или **argparse**, запуск тестов (**unittest.main()**), интерактивный демо-режим. При **import module** блок не выполняется — модуль только определяет объекты.
- [ ] **python -m package.module:** запуск модуля как скрипта; текущий каталог добавляется в **sys.path**[0] (часто корень проекта); ****name**** в **package.module** будет **'**main**'**. Удобно для CLI-точки входа внутри пакета (**python -m pip**, **python -m http.server**).
- [ ] **Файл **main**.py:** если в пакете есть ****main**.py**, то **python -m package** выполняет **package/**main**.py**; ****name**** там **'**main**'**. Используется для точки входа всего пакета без указания подмодуля.

**Пример __main__**

```python
# В конце модуля myapp.py
def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("input")
    args = p.parse_args()
    process(args.input)
if __name__ == "__main__":
    main()
# При python myapp.py или python -m myapp выполнится main()
# При import myapp блок if __name__ == "__main__" не выполнится
# В пакете: package/__main__.py с тем же if __name__ == "__main__": main()
# тогда python -m package запустит package/__main__.py
```

**builtins — встроенные объекты**

- [ ] **Что такое и зачем:** модуль **builtins** (в Py2 — ****builtin****) содержит **встроенные** имена интерпретатора: **len**, **open**, **print**, **str**, **int**, **list**, **dict**, **Exception** и т.д. Они доступны в любом модуле без импорта, потому что при компиляции функции её глобальные по умолчанию — это **builtins** (или ****builtins****, что может быть ссылкой на **builtins** или словарём в зависимости от контекста). Явный **import builtins** нужен для **перечисления** встроенных (**dir(builtins)**), **переопределения** в тестах (например **builtins.print = mock_print**), доступа к объектам, которые вы переопределили локально (через **builtins.len** и т.д.).
- [ ] **Применения:** (1) Подмена **input**/ **open**/ **print** в тестах — присвоить **builtins.input = lambda: 'test'**. (2) Проверка «встроенное ли имя»: **name in dir(builtins)**. (3) Динамический вызов по имени: **getattr(builtins, 'len')([1,2,3])**. (4) Документация и интроспекция — **help(builtins)**.
- [ ] **Осторожно:** переопределение глобальных имён (**builtins.open = ...**) влияет на **весь** процесс; в тестах лучше использовать **unittest.mock.patch('builtins.open', ...)** с ограниченной областью действия.

**Пример builtins**

```python
import builtins
# Список встроенных имён
len(dir(builtins))  # десятки имён
# Подмена в тесте (осторожно: глобально)
old_print = builtins.print
builtins.print = lambda *a, **k: None  # заглушка
# ... тест ...
builtins.print = old_print
# Доступ к len после локального переопределения
def f():
    len = lambda x: 99
    return builtins.len([1, 2, 3])  # 3, не 99
# Динамический вызов по имени
getattr(builtins, "sorted")([3, 1, 2])  # [1, 2, 3]
```

### abc — abstract base classes

**Что такое и зачем**

- [ ] **abc** — модуль для объявления **абстрактных базовых классов (ABC)**. Абстрактный класс задаёт **контракт** (какие методы должны быть у подкласса), но не реализует их полностью; экземпляр такого класса **нельзя** создать — только экземпляры конкретных подклассов, реализующих все абстрактные методы. **Применения:** единый интерфейс для плагинов (все реализуют одни и те же методы), документирование API (что должен реализовать подкласс), проверка типов и линтеры (isinstance, протоколы).
- [ ] Класс, наследующий **ABC** (или с метаклассом **ABCMeta**), объявляет абстрактные методы через декоратор **@abstractmethod**. **@abstractclassmethod**, **@abstractstaticmethod** — абстрактные классовый и статический методы (3.3+). **abc.ABCMeta** — метакласс **ABC**; при необходимости кастомного метакласса можно наследовать от **ABCMeta**. Подкласс обязан реализовать **все** абстрактные методы; иначе при создании экземпляра — **TypeError**. Проверка происходит в момент **создания экземпляра**, а не при наследовании.

**Пошагово: что происходит при создании Dog()**

1. Интерпретатор проверяет класс **Dog** на наличие нереализованных абстрактных методов из **Animal**.
2. Метод **speak** в **Animal** помечен **@abstractmethod**; в **Dog** он реализован — абстрактных не остаётся.
3. Создание экземпляра разрешено; **d = Dog()** выполняется. Если бы **Dog** не реализовал **speak**, на шаге 1–2 была бы **TypeError**.

**Пример**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"

# Animal()  # TypeError: Can't instantiate abstract class
d = Dog()
d.speak()  # "Woof"
```

### argparse, optparse, getopt

**argparse — парсинг аргументов CLI**

**Что такое и зачем**

- [ ] **argparse** — рекомендуемый способ **разбора аргументов командной строки**: флаги (**--verbose**, **-v**), опции со значением (**--output file.txt**), позиционные аргументы (**input.txt**), подкоманды (**git commit**, **git push**). Автоматическая генерация **--help** и сообщений об ошибках. **Применения:** CLI-утилиты, скрипты с конфигурируемым поведением, единообразный интерфейс для пользователя.

**Основной API**

- [ ] **ArgumentParser(description='...', epilog='...')** — создать парсер. **add_argument('--name', '-n', type=str, default=None, help='...')** — опция; **'--name'** — длинная форма, **'-n'** — короткая (опционально). **add_argument('path', ...)** — позиционный аргумент (без **--**). **parse_args()** — разобрать **sys.argv** и вернуть объект **Namespace** с атрибутами по именам аргументов (например **args.name**, **args.path**). **parse_known_args()** — разобрать и вернуть **(args, unknown_list)** (неизвестные аргументы в **unknown_list**).
- [ ] **nargs:** **'?'** — ноль или один аргумент; **'\*'** — ноль или более (список); **'+'** — один или более (список); **N** (целое) — ровно N аргументов. **choices=[...]** — допустимые значения; при неверном значении — ошибка. **required=True** — опция обязательна. **metavar='...'** — имя аргумента в справке.
- [ ] **action:** **'store'** (по умолчанию) — сохранить значение; **'store_true'** / **'store_false'** — флаг (True/False при наличии опции); **'append'** — добавлять значение в список (для **--add x --add y**); **'count'** — счётчик (например **-vvv** → 3). **'extend'** (3.8+) — расширять список.
- [ ] **type:** функция преобразования (**type=int**, **type=float**, **type=pathlib.Path**); при ошибке преобразования — сообщение об ошибке. **default** — значение по умолчанию; **default=argparse.SUPPRESS** — атрибут не создаётся, если опция не указана.
- [ ] **Подкоманды:** **add_subparsers(dest='cmd')** — группа подкоманд; **.add_parser('init', help='...')** — парсер для **init**; у каждого парсера свои **add_argument**. После **parse_args()** **args.cmd** — имя подкоманды; остальные атрибуты зависят от выбранного парсера.

**Пример: скрипт с опциями и позиционным аргументом**

```python
import argparse
p = argparse.ArgumentParser(description='Process files')
p.add_argument('input', help='Input file')
p.add_argument('-o', '--output', default='out.txt', help='Output file')
p.add_argument('-v', '--verbose', action='store_true', help='Verbose')
args = p.parse_args()
# python script.py data.txt -o result.txt -v
# args.input == 'data.txt', args.output == 'result.txt', args.verbose == True
```

**optparse и getopt**

- [ ] **optparse** — устаревший (deprecated в 3.2, удалён в 3.12); новый код на **argparse** (больше возможностей, единый стиль). **Миграция с optparse:** типичный **OptionParser** с **add_option** заменяется на **ArgumentParser** с **add_argument**; **parser.parse_args()** возвращает **Namespace** вместо **(options, args)**; опции становятся атрибутами (например **options.verbose** → **args.verbose**). Подкоманды и **nargs** в optparse не было — при сложном CLI переписать на argparse.
- [ ] **getopt** — минимальный парсер в стиле C: **getopt.getopt(args, shortopts, longopts)**. **shortopts** — строка коротких опций (**'ho:v'** — **-h**, **-o** с значением, **-v** без значения); **longopts** — список длинных (**['help', 'output=']**). Возвращает **(opts, args)** — список пар **(opt, value)** и список оставшихся позиционных аргументов. Удобен для быстрого разбора без подкоманд; для сложного CLI — **argparse**.

### array, struct

**array — компактные массивы однотипных элементов**

**Что такое и зачем**

- [ ] **array** — последовательность **однотипных** чисел (или байт), хранящаяся в памяти **компактно** (без накладных расходов на объекты Python). В отличие от **list**, каждый элемент — фиксированное число байт. **Применения:** большие числовые массивы (меньше памяти, чем list из int/float), обмен с C (совместимость с **array** в C через буферный протокол), чтение/запись бинарных файлов (**.tobytes()**, **.frombytes()**), аудио/видео буферы.
- [ ] **array.array(typecode, iterable=[])** — создать массив. **typecode** задаёт тип элемента; **array.typecodes** — строка доступных кодов. Методы и срезы как у **list** (индексация, **append**, **extend**, **insert**, **pop**, срезы **a[i:j]**). **.byteswap()** — поменять порядок байт элемента (для смены big/little endian). **.tobytes()** — массив как **bytes**; **.frombytes(b)** — дополнить массив из bytes. **.itemsize** — размер одного элемента в байтах. **buffer_info()** — адрес и длина буфера (для C-расширений).

**Типы (typecode):** **'b'** (signed char, 1 байт), **'B'** (unsigned char), **'h'** (short, 2), **'i'** (int, 4), **'I'** (unsigned int), **'l'** (long, 4 или 8), **'f'** (float, 4), **'d'** (double, 8), **'u'** (Unicode char, 2 или 4 байта в Py3 — deprecated для текста, для чисел **'H'** и т.д.).

**Пример array**

```python
import array
a = array.array('i', [1, 2, 3, 4, 5])
a.append(6)
a.tobytes()           # b'\x01\x00\x00\x00\x02\x00...' (4 байта на int)
b = array.array('i')
b.frombytes(a.tobytes())
```

**struct — упаковка и распаковка бинарных данных**

**Что такое и зачем**

- [ ] **struct** — преобразование между **Python-значениями** и **байтовой строкой** по **format string**: порядок байт (endianness) и тип каждого поля. **Применения:** бинарные протоколы (сетевые пакеты, заголовки файлов), обмен с C (структуры C), чтение/запись бинарных форматов (WAV, BMP и т.д.).
- [ ] **struct.pack(fmt, v1, v2, ...)** — упаковать значения в **bytes**. **struct.unpack(fmt, buffer)** — распаковать из buffer (bytes, bytearray, memoryview) в **кортеж**. **struct.pack_into(fmt, buffer, offset, v1, ...)** — записать по смещению в buffer; **struct.unpack_from(fmt, buffer, offset=0)** — прочитать с смещения. **struct.calcsize(fmt)** — размер результата в байтах.
- [ ] **Порядок байт (первый символ fmt):** **>** — big-endian (сетевой порядок); **<** — little-endian; **=** — native; **!** — network (= big-endian). **Типы:** **b**, **B** (1 байт); **h**, **H** (2); **i**, **I**, **l**, **L** (4 или 8); **q**, **Q** (8); **f** (4), **d** (8); **s** (bytes длины N — после числа, например **5s**); **?** (bool); **x** — padding (1 байт). **Размер и выравнивание:** **@** — native + native alignment; **c** — char (1 байт).

**Пример struct**

```python
import struct
# pack: два int (4 байта каждый), один float, порядок big-endian
b = struct.pack(">iif", 1, 2, 3.0)
# unpack
struct.unpack(">iif", b)  # (1, 2, 3.0)
struct.calcsize(">iif")   # 12
```

### ast, dis, tokenize, symtable

**ast — абстрактное синтаксическое дерево**

**Что такое и зачем**

- [ ] **ast** — работа с **AST (Abstract Syntax Tree)**: представление исходного кода в виде дерева узлов (выражения, операторы, определения). Парсинг **без выполнения** кода. **Применения:** линтеры и статический анализ (flake8, pylint), рефакторинг и трансформации кода, безопасное вычисление литералов (**literal_eval**), генерация кода, метрики (сложность, зависимости).
- [ ] **ast.parse(source, filename='<unknown>', mode='exec')** — разобрать **source** (строка) в узел **Module** (или **Expression** при **mode='eval'**). **mode**: **'exec'** — модуль/блок; **'eval'** — одно выражение; **'single'** — интерактивная строка (одно выражение, результат печатается). **ast.dump(node, indent=...)** — текстовое представление дерева (для отладки). **ast.walk(node)** — обход всех узлов в глубину; **ast.NodeVisitor** — подкласс с методами **visit\_<NodeType>** для обхода с действиями.
- [ ] **ast.literal_eval(node_or_string)** — **безопасное** вычисление литералов: числа, строки, bytes, кортежи, списки, dict, set, frozenset, True/False/None. **Не выполняет** вызовы функций, доступ к атрибутам, импорты — только константы. При передаче строки сначала парсится как выражение. **Применения:** разбор конфигов/данных в виде Python-литералов без риска инъекции (вместо **eval**).

**Пример ast.literal_eval**

```python
import ast
ast.literal_eval("[1, 2, 3]")     # [1, 2, 3]
ast.literal_eval("{'a': 1}")     # {'a': 1}
# ast.literal_eval("__import__('os').system('ls')")  # ValueError — не литерал
```

**dis — дизассемблер байткода**

- [ ] **Что такое и зачем:** **dis** выводит **инструкции байткода** Python (opcodes): как интерпретатор представляет функцию/модуль. Каждая операция (загрузка переменной, вызов, арифметика) соответствует одной или нескольким инструкциям виртуальной машины. **Применения:** понимание производительности (сколько операций, вызовов), отладка странного поведения, обучение (как работают циклы, генераторы), оптимизация (избежать лишних атрибутов/вызовов).
- [ ] **API:** **dis.dis(x=None, *, file=None, depth=None)** — дизассемблировать **x** (функция, метод, генератор, код, строка с кодом, модуль); вывод в **file** (по умолчанию **sys.stdout**); **depth** — глубина вложенности (None — без ограничения). Вывод: смещение (номер байта), имя инструкции (**LOAD_FAST**, **CALL_FUNCTION** и т.д.), аргументы. **dis.show_code(func)** — информация о коде: имена переменных (**co_varnames**), константы (**co_consts**), имя функции. **dis.get_instructions(x)** — итератор объектов **Instruction** (атрибуты **opname**, **opcode**, **arg**, **argval**, **offset**, **starts_line**); для программного анализа. **dis.findlinestarts(code)** — итератор **(offset, lineno)** для соответствия байткода и строк исходника. **Граничные случаи:** **dis.dis("x = 1")** — строка компилируется как код модуля; для строки с синтаксической ошибкой — **SyntaxError** при компиляции. **dis.dis(module)** выводит весь модуль; для больших модулей задают **depth=1** или передают конкретную функцию.

**Пример dis**

```python
import dis
def add_one(x):
    return x + 1
dis.dis(add_one)
#   2           0 LOAD_FAST                0 (x)
#               2 LOAD_CONST               1 (1)
#               4 BINARY_ADD
#               6 RETURN_VALUE
# Программный разбор инструкций
for instr in dis.get_instructions(add_one):
    print(instr.offset, instr.opname, instr.argval)
# 0 LOAD_FAST x
# 2 LOAD_CONST 1
# 4 BINARY_ADD None
# 6 RETURN_VALUE None
# Строка с кодом
dis.dis("y = [1, 2, 3]; z = len(y)")
# show_code — константы и имена
dis.show_code(add_one)
```

**tokenize — токенизатор исходного кода**

- [ ] **Что такое и зачем:** **tokenize** разбивает исходный код на **токены** (ключевые слова, идентификаторы, литералы, операторы, отступы). Каждый токен — тип (**NAME**, **NUMBER**, **STRING**, **NEWLINE**, **INDENT**, **DEDENT** и т.д.), значение (строка), координаты (строка, столбец). **Применения:** линтеры (проверка стиля без полного парсинга), подсветка синтаксиса, инструменты рефакторинга, анализ стиля (длина строк, отступы).
- [ ] **API:** **tokenize.generate_tokens(readline)** — итератор токенов; **readline** — callable без аргументов, возвращает следующую строку (как у файла); строка в **Unicode**. Токен — именованный кортеж **TokenInfo(type, string, start, end, line)**: **type** — константа (**tokenize.NAME**, **tokenize.NUMBER** и т.д.); **string** — подстрока; **start**, **end** — кортежи **(row, col)** начала и конца; **line** — полная строка. **tokenize.tokenize(readline)** — то же для **байтового** потока (readline возвращает bytes); кодировка определяется по BOM или cookie **# coding: utf-8**. **tokenize.untokenize(iterable)** — собрать токены обратно в строку (приблизительно; комментарии теряются). **Граничные случаи:** для неполного кода (строка без перевода строки) токенизатор может не выдать **ENDMARKER**; **readline** должен возвращать пустую строку в конце. Для строки с кодом удобно **io.StringIO(code).readline**.

**Пример tokenize**

```python
import tokenize
import io
code = "x = 1 + 2\nprint(x)"
gen = tokenize.generate_tokens(io.StringIO(code).readline)
for tok in gen:
    print(tokenize.tok_name[tok.type], repr(tok.string), tok.start)
# NAME 'x' (1, 0)
# OP '=' (1, 2)
# NUMBER '1' (1, 4)
# ...
# ENDMARKER '' (2, 6)
# Обратно в строку (без комментариев)
tokens = list(tokenize.generate_tokens(io.StringIO(code).readline))
tokenize.untokenize(tokens)  # 'x = 1 + 2\nprint (x)\n'  (пробел перед скобкой)
```

**symtable — таблицы символов**

- [ ] **Что такое и зачем:** **symtable** даёт **таблицу символов** скомпилированного кода: какие имена объявлены, в какой области видимости (локальная, глобальная, свободная для замыканий), являются ли они параметрами, глобальными и т.д. Строится **без выполнения** кода. **Применения:** статический анализ (какие переменные используются до присваивания), проверка области видимости без выполнения кода, линтеры (неиспользуемые переменные), поиск свободных переменных в замыканиях.
- [ ] **API:** **symtable.symtable(code, name, 'exec')** — построить таблицу для **code** (строка); **name** — имя блока (например **'module'** или имя функции); **'exec'** / **'eval'** / **'single'**. Возвращает объект **SymbolTable** с методами **get_children()** — вложенные блоки (функции, классы); **get_identifiers()** — имена символов в этом блоке; **lookup(name)** — объект **Symbol** с **.is_local()**, **.is_global()**, **.is_free()** (свободная переменная замыкания), **.is_parameter()**, **.get_namespaces()** и т.д. **SymbolTable.get_type()** — **'module'**, **'function'**, **'class'**. **Граничные случаи:** для кода с синтаксической ошибкой **symtable** выбрасывает **SyntaxError**; при разборе ненадёжного ввода оборачивать в **try/except**. Имена из **get_identifiers()** включают и локальные, и глобальные; **lookup(name)** уточняет роль.

**Пример symtable**

```python
import symtable
code = """
x = 1
def f(a, b):
    z = a + b
    return z + x
"""
st = symtable.symtable(code, "module", "exec")
print(st.get_identifiers())   # {'x', 'f'}
st.lookup("x").is_global()   # True
child = st.get_children()[0] # таблица функции f
child.get_identifiers()      # {'a', 'b', 'z', 'x'}
child.lookup("a").is_parameter()  # True
child.lookup("z").is_local()     # True
child.lookup("x").is_free()      # True (замыкание)
```

### asyncio

**Что такое и зачем**

- [ ] **asyncio** — модуль **асинхронного I/O** (PEP 3156): выполнение множества операций I/O **конкурентно** в одном потоке без блокировок. Корутины (**async def**) при **await** отдают управление event loop; loop запускает другие корутины, пока первая ждёт (сеть, таймер). **Применения:** сетевые серверы и клиенты (много соединений без потоков), скрапинг (много одновременных запросов), очереди сообщений, чат-боты.
- [ ] **Основной API:** **async def** — корутина; **await** — приостановка до завершения awaitable (другая корутина, **asyncio.sleep(sec)**). **asyncio.run(main())** — запустить главную корутину (создаёт loop, выполняет **main()**, закрывает loop); вызывать **один раз** в точке входа. **asyncio.create_task(coro)** — запланировать корутину как **Task** (выполняется конкурентно с текущей); не ждёт завершения. **asyncio.gather(*coros)** — выполнить корутины параллельно и вернуть список результатов; **return_exceptions=True** — не падать на первой ошибке, вернуть исключения в списке. **asyncio.sleep(sec)** — «подождать» sec секунд без блокировки потока. **asyncio.wait_for(aw, timeout)** — выполнить awaitable с таймаутом; при превышении — **asyncio.TimeoutError**.
- [ ] **Примитивы:** **asyncio.Queue(maxsize=0)** — очередь между корутинами; **.put(item)**, **.get()** — асинхронные; **asyncio.Lock()**, **asyncio.Semaphore(n)**, **asyncio.Event()** — синхронизация (использовать **async with lock:**). **asyncio.subprocess** — **asyncio.create_subprocess_exec(*args)**, **create_subprocess_shell(cmd)** — асинхронный subprocess; **process.communicate()** — await. **loop.run_in_executor(executor, func, *args)** — выполнить блокирующую функцию в пуле потоков (по умолчанию **ThreadPoolExecutor**), чтобы не блокировать loop; возвращает **Future**, можно **await**. **Граничные случаи:** внутри корутины **не вызывать** блокирующие операции (time.sleep, синхронный requests.get) без **run_in_executor** — иначе блокируется весь loop. **asyncio.run()** нельзя вызывать из уже работающего loop; в Jupyter/IPython использовать **await main()** при наличии встроенного loop.

**Пример asyncio (только stdlib: таймеры и очередь)**

```python
import asyncio
async def worker(name, queue):
    while True:
        x = await queue.get()
        if x is None:
            break
        await asyncio.sleep(0.1)  # имитация работы
        print(name, x)
        queue.task_done()
async def main():
    q = asyncio.Queue()
    for i in range(3):
        await q.put(i)
    await q.put(None)
    await q.put(None)
    t1 = asyncio.create_task(worker("A", q))
    t2 = asyncio.create_task(worker("B", q))
    await q.join()
    await asyncio.gather(t1, t2)
asyncio.run(main())
# Параллельный «sleep» и gather
async def f():
    await asyncio.sleep(1)
    return 1
async def g():
    await asyncio.sleep(0.5)
    return 2
results = asyncio.run(asyncio.gather(f(), g()))  # [1, 2] — ~1 сек суммарно
# run_in_executor для блокирующего кода
loop = asyncio.get_event_loop()
result = await loop.run_in_executor(None, lambda: sum(range(10**6)))
```

### base64, binascii, codecs

**base64 — кодирование в Base64/Base32/Base16**

**Что такое и зачем**

- [ ] **base64** — преобразование **bytes** в строку из **печатаемых ASCII**-символов (64, 32 или 16 символов алфавита) и обратно. Исходные байты разбиваются на блоки и кодируются символами; вывод можно передавать в текстовых протоколах (email, JSON, URL-параметры). **Применения:** вложения в email (MIME), данные в JSON (например изображение как строка), токены и ключи в URL (с **urlsafe**), хранение бинарных данных в конфигах.
- [ ] **base64.b64encode(s)** — **s** (bytes) → bytes (base64-строка в ASCII). **base64.b64decode(s)** — декодирование; **s** может быть bytes или str (только ASCII-символы). Для **str** в Python 3: **base64.b64encode(data.encode()).decode()** — если нужна строка; **base64.b64decode(s.encode() if isinstance(s, str) else s)** — декодировать из строки. **base64.b64decode(s, validate=True)** — проверять алфавит (при **False** игнорировать посторонние символы).
- [ ] **urlsafe_b64encode** / **urlsafe_b64decode** — алфавит без **+** и **/** (заменены на **-** и **\_**); подходит для URL и имён файлов без экранирования. **base32**, **base16** (hex) — **b32encode**/ **b32decode**, **b16encode**/ **b16decode**; base16 — только 0–9 и A–F, удлиняет строку сильнее base64.

**Пример base64**

```python
import base64
data = b'hello'
enc = base64.b64encode(data)   # b'aGVsbG8='
base64.b64decode(enc)          # b'hello'
# URL-safe (для токенов в URL)
base64.urlsafe_b64encode(data).decode()  # 'aGVsbG8='
```

**binascii — низкоуровневые преобразования бинарных данных**

- [ ] **Что такое и зачем:** **binascii** — низкоуровневые функции преобразования между **bytes** и текстовыми представлениями (hex, base64, uuencode, quoted-printable). Модуль **base64** использует **binascii** внутри и даёт более удобный API (обработка переносов строк, варианты алфавита); **binascii** полезен при работе с протоколами или форматами, требующими **точного контроля** над выводом (без обёрток base64). **Применения:** hex-дампы, протоколы с hex/base64 без лишней обработки, совместимость со старыми форматами (uuencode), бинарные протоколы с фиксированным форматом.
- [ ] **API:** **binascii.hexlify(b)** — bytes → bytes (строка hex в ASCII; каждый байт исходных данных → два символа 0-9a-f); **binascii.unhexlify(s)** — строка hex → bytes; **s** может быть bytes или str (только символы 0-9a-fA-F). **binascii.a2b_base64(s)**, **binascii.b2a_base64(b)** — base64 (ввод/вывод без переносов строк; **b2a_base64** добавляет перевод строки в конец). **binascii.a2b_uu(s)**, **binascii.b2a_uu(b)** — uuencode (старый формат Unix). **binascii.a2b_qp(s)**, **binascii.b2a_qp(b)** — quoted-printable (MIME). **Граничные случаи:** **unhexlify** при нечётной длине строки или неhex-символах выбрасывает **binascii.Error**; **a2b_base64** не игнорирует пробелы и переносы так, как **base64.b64decode** — для «грязного» ввода удобнее **base64**. **hexlify** возвращает **bytes**; для строки вызвать **.decode()**.

**Пример binascii**

```python
import binascii
# Hex
data = b"hello"
binascii.hexlify(data)        # b'68656c6c6f'
binascii.unhexlify(b'68656c6c6f')  # b'hello'
binascii.hexlify(data).decode()     # '68656c6c6f' — строка для логов
# Base64 (низкоуровневый; для гибкости)
binascii.b2a_base64(data)     # b'aGVsbG8=\n'
binascii.a2b_base64(b'aGVsbG8=\n')  # b'hello'
# Ошибка при неверном hex
try:
    binascii.unhexlify("xyz")
except binascii.Error as e:
    print(e)
# uuencode (редко; совместимость со старыми системами)
binascii.b2a_uu(b"short")     # b'0V%T\n'
```

**codecs — кодеки и поточное кодирование**

- [ ] **Что такое и зачем:** **codecs** — регистрация и поиск **кодеков** (преобразование str ↔ bytes по имени кодировки). **Применения:** единый интерфейс кодирования/декодирования по имени, кастомные кодеки (**codecs.register**), поточное чтение/запись с кодировкой (**StreamReader**/ **StreamWriter**), инкрементальное кодирование при потоковой обработке (по блокам без загрузки всего текста в память).
- [ ] **codecs.encode(obj, encoding, errors='strict')** — кодировать **obj** (str → bytes). **codecs.decode(obj, encoding, errors='strict')** — декодировать (bytes → str). Параметр **errors**: **'strict'** (ошибка при недопустимом символе), **'ignore'** (пропустить), **'replace'** (заменить на), **'backslashreplace'** (заменить на \\xNN), **'surrogateescape'** (сохранить байты в суррогатной области для последующего восстановления). **codecs.open(path, mode, encoding, ...)** — открыть файл с кодировкой (в Py3 обычно **open(path, encoding=...)**). **codecs.lookup(encoding)** — объект **CodecInfo** (encode, decode, streamreader, streamwriter). **codecs.register(search_function)** — зарегистрировать кодировку (поиск по имени). **codecs.getincrementalencoder(encoding)** — инкрементальный кодировщик: метод **.encode(s, final=False)** возвращает bytes (при **final=True** сбрасывает буфер); для посимвольной/поблочной обработки без накопления всей строки.
- [ ] **Граничные случаи:** при **decode** с **errors='strict'** недопустимая последовательность байт вызывает **UnicodeDecodeError**; при потоковом чтении из ненадёжного источника часто используют **errors='replace'** или **errors='ignore'**. **getincrementalencoder** нужен, когда строка приходит по частям (сеть, большой файл) и нельзя вызвать **encode** на всей строке сразу.

**Пример codecs: encode/decode и инкрементальный кодировщик**

```python
import codecs
# Единый интерфейс по имени кодировки
codecs.encode('привет', 'utf-8')     # b'\xd0\xbf\xd1\x80...'
codecs.decode(b'\xd0\xbf\xd1\x80...', 'utf-8')  # 'привет'
# Ошибки при декодировании
codecs.decode(b'\xff\xfe', 'utf-8', errors='replace')  # ''
# Инкрементальное кодирование (по блокам)
enc = codecs.getincrementalencoder('utf-8')()
enc.encode('при', final=False)  # b'\xd0\xbf\xd1\x80...'
enc.encode('вет', final=True)   # b'\xd0\xb2\xd0\xb5\xd1\x82'
```

### bisect, heapq

**bisect — бинарный поиск и вставка**

**Что такое и зачем**

- [ ] **bisect** — **бинарный поиск** и **вставка с сохранением порядка** в **отсортированную** последовательность. Вместо линейного перебора O(n) даёт поиск за O(log n); вставка остаётся O(n) из-за сдвига элементов списка. **Применения:** поиск границы (например «первый элемент ≥ x»), вставка в упорядоченный список без пересортировки, разбиение по диапазонам (баллы → оценки), поиск в уже отсортированных данных.
- [ ] **bisect_left(a, x)** — индекс, куда вставить **x**, чтобы **все элементы слева были строго меньше x** (если x уже есть, индекс слева от левого вхождения). **bisect_right(a, x)** (синоним **bisect.bisect**) — все элементы слева **меньше или равны x** (вставка справа от правого вхождения). **insort_left(a, x)** и **insort_right(a, x)** — вставить **x** в список **a** на место, найденное соответствующим bisect; список остаётся отсортированным. **Критично:** **a** должен быть **отсортирован** по тому же ключу; иначе результат неверен.

**Пример bisect**

```python
import bisect
a = [1, 2, 4, 5]
bisect.bisect_left(a, 3)   # 2 — вставить перед 4
bisect.insort_left(a, 3)   # a становится [1, 2, 3, 4, 5]
```

**heapq — куча (min-heap)**

**Что такое и зачем**

- [ ] **heapq** — операции с **кучей (min-heap)**: список интерпретируется как двоичная куча (родитель не больше детей); минимум всегда в **heap[0]**. Реализация **in-place** — список меняется. **Применения:** приоритетная очередь (задачи по срочности), n наименьших/наибольших элементов из потока без хранения всего (**nlargest**/ **nsmallest**), слияние отсортированных последовательностей, планировщики (следующее событие по времени).
- [ ] **heappush(heap, x)** — добавить элемент, сохраняя свойство кучи; **heappop(heap)** — извлечь и вернуть **минимум**; **heapify(x)** — превратить список **x** в кучу **in-place** за O(n). **nlargest(n, iterable)**, **nsmallest(n, iterable)** — n наибольших/наименьших элементов (для больших n используют кучу внутри; память O(n)). Для **приоритетной очереди**: хранить **(приоритет, элемент)**; при равных приоритетах порядок может зависеть от второго элемента — при необходимости добавлять счётчик **(приоритет, counter, элемент)** для стабильного порядка.

**Пример heapq: приоритетная очередь**

```python
import heapq
# Элементы: (приоритет, задача). Минимальный приоритет извлекается первым.
tasks = []
heapq.heappush(tasks, (2, 'low'))
heapq.heappush(tasks, (1, 'high'))
heapq.heappush(tasks, (3, 'mid'))
heapq.heappop(tasks)   # (1, 'high')
heapq.heappop(tasks)   # (2, 'low')
# nlargest/nsmallest без изменения исходной последовательности
heapq.nsmallest(2, [3, 1, 4, 1, 5])  # [1, 1]
```

### collections, collections.abc

**collections — специализированные контейнеры**

- [ ] **Что такое и зачем:** **collections** предоставляет **контейнеры** поверх встроенных типов с расширенным поведением. **Применения:** **deque** — очередь/стек с O(1) с обоих концов (очереди, скользящее окно); **Counter** — подсчёт элементов (частоты, топ-N); **defaultdict** — словарь с значением по умолчанию при отсутствии ключа; **OrderedDict** — порядок вставки (до 3.7 dict уже сохраняет порядок); **ChainMap** — цепочка словарей (конфиг + переопределения); **namedtuple** — кортеж с именованными полями (легковесные записи). См. также §11, §11a для углублённого разбора.

**Пример collections**

```python
from collections import deque, Counter, defaultdict, ChainMap, namedtuple
# deque — очередь с обоих концов O(1)
q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
q.pop()
q.popleft()
# Counter — подсчёт элементов
cnt = Counter("abracadabra")
cnt.most_common(2)   # [('a', 5), ('b', 2)]
cnt["x"] += 1
# defaultdict — значение по умолчанию при отсутствии ключа
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
# ChainMap — цепочка словарей (первый найденный ключ)
base = {"a": 1, "b": 2}
overrides = {"b": 99}
cm = ChainMap(overrides, base)
cm["a"], cm["b"]   # 1, 99
# namedtuple — кортеж с именованными полями
Point = namedtuple("Point", "x y")
p = Point(3, 4)
p.x, p.y   # 3, 4
```

**collections.abc — абстрактные базовые классы для контейнеров**

- [ ] **Что такое и зачем:** **collections.abc** определяет **интерфейсы** контейнеров: **Iterable**, **Iterator**, **Generator**; **Sequence**, **MutableSequence**; **Mapping**, **MutableMapping**; **Set**, **MutableSet**; **Callable**, **Container**, **Sized**, **Hashable**; **Awaitable**, **AsyncIterator**. **Применения:** проверка типа без привязки к конкретному классу (**isinstance(x, collections.abc.Sequence)**), аннотации типов (**def f(x: Sequence[str])**), реализация протоколов в своих классах. См. также §11, §11a.

**Пример collections.abc**

```python
from collections.abc import Sequence, Mapping, Callable
# Проверка типа без привязки к list/dict
def process(items: Sequence[str]):
    for i, x in enumerate(items):
        print(i, x)
process([ "a", "b" ])
process(("a", "b"))
# isinstance для протокола
isinstance([1, 2], Sequence)   # True
isinstance({"a": 1}, Mapping) # True
isinstance(len, Callable)      # True
```

### Сжатие: gzip, bz2, lzma, zipfile, tarfile

**gzip, bz2, lzma — сжатие потока**

**Что такое и зачем**

- [ ] **gzip**, **bz2**, **lzma** — сжатие **одного потока** данных (форматы .gz, .bz2, .xz). Интерфейс как у файла: при чтении данные распаковываются, при записи — сжимаются. **Применения:** сжатие логов, бэкапов, ответов HTTP (Content-Encoding: gzip); обмен сжатыми файлами. **gzip** — быстрее, широко поддерживается; **lzma** — лучшее сжатие при большей нагрузке; **bz2** — компромисс.
- [ ] **API:** **gzip.open(path, mode='rb'/'wb', compresslevel=9)** — открыть файл; **mode** как у **open**. **compresslevel**: для gzip 1–9 (9 — макс. сжатие, 1 — быстрее); для bz2 1–9; для lzma **preset** (по умолчанию сбалансирован). **gzip.open(..., 'rt'/'wt')** — текстовый режим (строки, кодировка). **gzip.compress(data, compresslevel=9)** — сжать **data** (bytes) целиком → bytes. **gzip.decompress(data)** — распаковать. Аналогично **bz2.open**, **bz2.compress**, **bz2.decompress**; **lzma.open**, **lzma.compress**, **lzma.decompress**. **Граничные случаи:** для очень больших данных предпочтительнее **open()** и чтение/запись блоками, чтобы не держать всё в памяти; **compress**/ **decompress** загружают весь объём в RAM.
- [ ] **Пример:** сжатие файла и чтение сжатого — **with gzip.open('log.gz', 'wt', encoding='utf-8') as f: f.write(text)**; **with gzip.open('log.gz', 'rt', encoding='utf-8') as f: text = f.read()**. Сжатие bytes в память: **compressed = gzip.compress(b'data')**; **gzip.decompress(compressed)**.

**zipfile — ZIP-архивы**

**Что такое и зачем**

- [ ] **zipfile** — чтение и создание **ZIP-архивов**: несколько файлов в одном, сжатие по отдельности, метаданные (дата, права). **Применения:** распаковка скачанных архивов, создание дистрибутивов, чтение .docx/.xlsx (это ZIP с XML внутри), бэкапы.
- [ ] **API:** **zipfile.ZipFile(path, mode='r'/'w'/'a'/'x')** — открыть архив; **'x'** — эксклюзивное создание (ошибка при существующем файле). **namelist()** — список имён в архиве; **infolist()** — список **ZipInfo**. **getinfo(name)** — **ZipInfo** (filename, file_size, compress_size, date_time). **read(name)** — прочитать файл в bytes. **extract(member, path=None)** — извлечь один файл; **extractall(path=None, members=None)** — извлечь все (или указанные). **write(filename, arcname=None)** — добавить файл в архив; **writestr(zinfo_or_arcname, data)** — записать из строки/bytes. **ZipFile** поддерживает контекстный менеджер **with**. **Безопасность:** **extractall** может записывать файлы вне **path** при злонамеренных именах (**path traversal**); проверять имена или использовать **ZipFile(path).extract(member, path=...)** с нормализацией путей.

**Пример: создать ZIP и прочитать файл**

```python
import zipfile
with zipfile.ZipFile('out.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.write('script.py', 'script.py')
with zipfile.ZipFile('out.zip', 'r') as zf:
    print(zf.namelist())           # ['script.py']
    data = zf.read('script.py')    # bytes
```

**tarfile — TAR-архивы**

**Что такое и зачем**

- [ ] **tarfile** — чтение и создание **TAR**-архивов (в т.ч. .tar.gz, .tar.bz2, .tar.xz). TAR — формат без сжатия (объединение файлов с метаданными); сжатие применяется ко всему потоку (gzip, bz2, lzma). **Применения:** распаковка исходников (например .tar.gz), создание бэкапов, обмен дистрибутивами.
- [ ] **API:** **tarfile.open(path, mode='r'/'w'/'a'/'x', ...)** — открыть; режим **'r'** / **'r:\*'** — чтение (автоопределение сжатия); **'r:gz'**, **'r:bz2'**, **'r:xz'** — чтение с указанным сжатием; **'w:gz'** — запись gzip; **'w'** — без сжатия. **getnames()** — список имён членов; **getmembers()** — список **TarInfo**. **extract(member, path='')**, **extractall(path='', members=None)** — извлечь (при **members=None** — все). **add(name, arcname=None)** — добавить файл по пути; **addfile(tarinfo, fileobj)** — из потока. **TarInfo** — атрибуты **name**, **size**, **type** (обычный файл, каталог и т.д.), **mtime**, права. **Безопасность:** при **extractall** от ненадёжного архива возможен path traversal; проверять и нормализовать пути членов перед извлечением.
- [ ] **Пример:** распаковка **archive.tar.gz** в каталог **out/** — **with tarfile.open('archive.tar.gz', 'r:gz') as tf: tf.extractall('out')**. Создание архива: **with tarfile.open('backup.tar.gz', 'w:gz') as tf: tf.add('project/', arcname='project')**.

### concurrent

**concurrent.futures — пулы потоков и процессов**

**Что такое и зачем**

- [ ] **concurrent.futures** — высокоуровневый API для **параллельного выполнения**: пул рабочих потоков или процессов, отправка задач (**submit** или **map**), получение результатов через **Future**. Не нужно вручную создавать **Thread**/ **Process** и очереди. **Применения:** параллельные HTTP-запросы (ThreadPoolExecutor), тяжёлые вычисления по ядрам (ProcessPoolExecutor), пакетная обработка данных.
- [ ] **ThreadPoolExecutor(max_workers=None)** — пул потоков; **max_workers** по умолчанию — 5 * число ядер (3.8+). **ProcessPoolExecutor(max_workers=None)** — пул процессов; по умолчанию — число ядер. **executor.submit(func, *args, **kwargs)** — отправить задачу; возвращает **Future**. **future.result(timeout=None)** — дождаться результата (блокирует); **TimeoutError** при таймауте. **future.done()** — завершена ли задача; **future.cancel()** — отменить (если не начата). **executor.map(func, \*iterables, timeout=None)** — применить **func** к элементам iterables параллельно; возвращает итератор по результатам в порядке аргументов. **executor.shutdown(wait=True)** — завершить пул (не принимать новые задачи); контекстный менеджер **with** вызывает **shutdown** при выходе.
- [ ] **Когда что использовать:** I/O-задачи (сеть, диск) — **ThreadPoolExecutor** (мало накладных, GIL отпускается при I/O). CPU-задачи (числа, парсинг) — **ProcessPoolExecutor** (обход GIL, изоляция по памяти). **as_completed(futures)** — итератор по Future по мере завершения (не по порядку).

**Пример: параллельная загрузка URL**

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import urllib.request

def fetch(url):
    with urllib.request.urlopen(url) as resp:
        return resp.read()

urls = ['https://example.com', 'https://python.org']
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch, u): u for u in urls}
    for future in as_completed(futures):
        url = futures[future]
        try:
            data = future.result()
        except Exception as e:
            print(f'{url} failed: {e}')
```

**concurrent.interpreters — суб-интерпретаторы в одном процессе (PEP 554, 3.9+)**

**Что такое и зачем**

- [ ] **concurrent.interpreters** предоставляет **суб-интерпретаторы (sub-interpreters)**: несколько изолированных интерпретаторов в **одном процессе** ОС. У каждого суб-интерпретатора свой глобальный namespace, свой GIL (в перспективе — параллельное выполнение Python-кода без GIL между интерпретаторами), изолированные импорты и глобальные переменные. Обмен данными между суб-интерпретаторами — через **каналы (channels)** или **shared memory** (ограниченный набор типов). **Применения:** изоляция плагинов или неподтверждённого кода в одном процессе, эксперименты с параллельным выполнением без multiprocessing (меньше накладных, чем порождение процессов). **Ограничения:** API помечен как **provisional** (может меняться); не все расширения C совместимы с суб-интерпретаторами; для стабильного продакшена обычно используют **multiprocessing** или **concurrent.futures**.
- [ ] **Основной API:** **concurrent.interpreters.create()** — создать новый суб-интерпретатор; возвращает объект **Interpreter**. **.exec(code)** — выполнить строку кода **code** в этом интерпретаторе (в его глобальном контексте); код выполняется в изоляции (не видит переменные основного интерпретатора). **list_all()** — список всех созданных суб-интерпретаторов. Обмен данными — через **Channel**: **Channel()** создаёт канал; **.send(obj)** / **.recv()** — передача объектов между интерпретаторами (объекты должны быть сериализуемы). **Граничные случаи:** передавать в суб-интерпретатор можно только код в виде строки; передача сложных объектов между интерпретаторами — через каналы с ограниченными типами. **Когда использовать:** если нужна изоляция в одном процессе без fork/spawn. Для параллельных вычислений по ядрам — **multiprocessing** или **ProcessPoolExecutor**; для I/O — **threading** или **asyncio**.

**Пример concurrent.interpreters**

```python
# Python 3.9+, API provisional
from concurrent import interpreters
interp = interpreters.create()
interp.exec("x = 42")
interp.exec("print(x)")  # 42 — в своём namespace
# Основной интерпретатор не видит x
# interp.exec("return 1")  # return вне функции — SyntaxError в том интерпретаторе
interpreters.list_all()   # список созданных интерпретаторов
# Передача данных между интерпретаторами — через Channel (если доступен)
# ch = interpreters.Channel()
# interp.exec("... ch.send(result) ...")
# main: result = ch.recv()
```

### configparser, json, csv, tomllib

**configparser — INI-подобные конфиги**

- [ ] **Что такое и зачем:** **configparser** читает и пишет файлы в формате **INI**: секции **\[section\]**, внутри пары **key = value** (или **key: value**). Комментарии **#** и **;**; многострочные значения через отступ. **Применения:** конфигурация приложений (БД, API-ключи, пути), настройки без программирования, совместимость с Windows-стилем .ini.
- [ ] **API:** **configparser.ConfigParser()** — объект парсера; **.read(filenames, encoding=None)** — загрузить один или несколько файлов (возвращает список успешно прочитанных); **.read_file(fp)** — из потока. Доступ: **cfg['section']['key']** или **cfg.get('section', 'key')**; **cfg.getint('section', 'key')**, **.getfloat()**, **.getboolean()** — типизированное чтение; **.get('section', 'key', fallback=...)** — значение по умолчанию при отсутствии ключа. **.sections()** — список секций; **.options(section)** — ключи в секции; **.has_section(section)**; **.has_option(section, key)**. Запись: **.add_section(section)**; **.set(section, option, value)**; **.write(fp)**. **ConfigParser(interpolation=None)** — отключить подстановку **%(...)s** (безопаснее для ненадёжного ввода).
- [ ] **Interpolation:** по умолчанию **BasicInterpolation** — в значениях подстановка **%(other_key)s** или **%(other_section)s** (ссылка на другую опцию/секцию). Для конфигов от ненадёжного источника отключать: **ConfigParser(interpolation=None)** — иначе возможна подстановка из системных переменных или чтение файлов (**%(home)s** и т.д.). Кодировка: **read(..., encoding='utf-8')** (по умолчанию UTF-8 с 3.2).
- [ ] **Граничные случаи:** отсутствующий ключ при **cfg.get('s', 'k')** даёт **NoOptionError**; отсутствующая секция — **NoSectionError**; использовать **get(..., fallback=...)** или **has_option** перед чтением. При записи **.set()** всегда преобразует значение в строку; числа и булевы при **getint**/ **getboolean** парсятся при чтении.

**Пример configparser: чтение и запись**

```python
import configparser
cfg = configparser.ConfigParser()
cfg.read('config.ini', encoding='utf-8')
# Чтение
db_host = cfg.get('database', 'host', fallback='localhost')
port = cfg.getint('database', 'port', fallback=5432)
for section in cfg.sections():
    for key in cfg.options(section):
        print(section, key, cfg[section][key])
# Запись
cfg.add_section('cache')
cfg.set('cache', 'size', '1000')
with open('config.ini', 'w', encoding='utf-8') as f:
    cfg.write(f)
```

**json — сериализация и десериализация JSON**

- [ ] **Что такое и зачем:** **json** — сериализация Python-объектов в **JSON** (JavaScript Object Notation) и обратно. JSON — текстовый формат обмена данными (API, конфиги, логи). **Применения:** REST API (запросы/ответы), сохранение конфигов и данных, обмен между языками.
- [ ] **API:** **json.load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, ...)** — прочитать JSON из файла/потока; **json.loads(s, ...)** — из строки (str). **json.dump(obj, fp, indent=None, ensure_ascii=True, sort_keys=False, default=None, ...)** — записать в файл; **json.dumps(obj, ...)** — в строку. **indent=2** — отступы для читаемости; **ensure_ascii=False** — не экранировать не-ASCII (кириллица и т.д. остаётся как есть); **sort_keys=True** — сортировать ключи словаря при выводе. При ошибке разбора — **json.JSONDecodeError** (атрибуты **msg**, **pos**, **lineno**, **colno**).
- [ ] **Кастомные типы:** поддерживаются только **dict**, **list**, **str**, **int**, **float**, **bool**, **None**. Для **datetime**, **bytes**, **Decimal**, **UUID** и т.д.: **default** — функция **obj → serializable** при сериализации (должна возвращать тип, поддерживаемый JSON, или вызывать **TypeError**); **object_hook** — функция **dict → object** при десериализации (вызывается для каждого dict); **cls** — подкласс **JSONEncoder** для сложной логики. **Граничные случаи:** **NaN**, **Infinity** не входят в стандарт JSON — при **allow_nan=True** (по умолчанию) они сериализуются как **NaN**/ **Infinity** (некоторые парсеры их не принимают); при **strict=False** в **loads** можно разрешить управляющие символы в строках. Кодировка файла — UTF-8 (или указать при **open**).

**Пример json**

```python
import json
from datetime import datetime
# Базовое чтение/запись
data = {"a": 1, "b": [2, 3], "c": "текст"}
s = json.dumps(data, ensure_ascii=False, indent=2)
obj = json.loads(s)
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
with open("config.json", encoding="utf-8") as f:
    loaded = json.load(f)
# Кастомные типы: datetime
def default(o):
    if hasattr(o, "isoformat"):
        return o.isoformat()
    raise TypeError(f"Object {o!r} is not JSON serializable")
json.dumps({"t": datetime.now()}, default=default)
# Ошибка разбора
try:
    json.loads("{ invalid }")
except json.JSONDecodeError as e:
    print(e.msg, e.lineno, e.colno)
```

**csv — чтение и запись CSV**

- [ ] **Что такое и зачем:** **csv** — чтение и запись **CSV** (Comma-Separated Values): таблицы в текстовом виде, строки — строки файла, столбцы — разделитель (запятая, точка с запятой, табуляция). **Применения:** импорт/экспорт из Excel и БД, логи, обмен табличными данными.
- [ ] **API:** **csv.reader(iterable, delimiter=',', quotechar='"', ...)** — итератор по строкам (каждая строка — список полей). **csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)** — запись; **.writerow(row)**; **.writerows(rows)**. **csv.DictReader(fp, fieldnames=None)** — итератор по строкам как dict (ключи — первая строка или **fieldnames**). **csv.DictWriter(fp, fieldnames)** — запись из dict; **.writeheader()**; **.writerow(dict)**. **csv.Sniffer()** — **.sniff(sample)** определяет **delimiter**, **quotechar** по образцу текста. **Dialect** — именованный набор параметров (разделитель, кавычки); **csv.register_dialect(name, ...)**; **reader(..., dialect='excel')**. **Граничные случаи:** поля с разделителем или переносами строк экранируются кавычками; при **quoting=csv.QUOTE_NONNUMERIC** нечисловые поля выводятся в кавычках. Кодировка: открывать файл с **encoding='utf-8'** (или нужной кодировкой); **newline=''** при записи на Windows, чтобы избежать двойных переводов строк.

**Пример csv: DictReader и DictWriter**

```python
import csv
# Чтение с заголовками
with open('data.csv', newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row['name'], row['score'])  # ключи из первой строки
# Запись с заголовками
with open('out.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=['name', 'score'])
    w.writeheader()
    w.writerow({'name': 'Alice', 'score': 90})
    w.writerows([{'name': 'Bob', 'score': 85}])
```

**tomllib — парсинг TOML (3.11+)**

- [ ] **Что такое и зачем:** **tomllib** парсит **TOML** (Tom's Obvious Minimal Language) — формат конфигов с секциями, ключами, типами (строки, числа, булевы, массивы, таблицы). **Применения:** конфиги современных инструментов (Rust, Python-проекты, pyproject.toml). **Только чтение:** запись TOML — сторонние библиотеки (tomli-w, tomli-w).
- [ ] **API:** **tomllib.load(fp)** — прочитать из **бинарного** потока (файл открыть в **'rb'**); возвращает **dict** (вложенные таблицы TOML — вложенные dict). **tomllib.loads(s)** — из строки (bytes). Типы: строки, int, float, bool, **datetime.datetime** (даты и время с зоной — **datetime** с **tzinfo**), массив как list, таблица как dict. Ключи с точкой (**a.b = 1**) превращаются во вложенные dict (**{'a': {'b': 1}}**). **Граничный случай:** файл обязательно открывать в **'rb'**; при **open(path)** в текстовом режиме **load(fp)** вызовет **TypeError**.

**Пример tomllib**

```python
# Python 3.11+
import tomllib
with open('pyproject.toml', 'rb') as f:
    data = tomllib.load(f)
name = data['project']['name']
deps = data['project'].get('dependencies', [])
# Вложенные таблицы: [tool.black] → data['tool']['black']
```

### contextlib, contextvars

**contextlib — утилиты для контекстных менеджеров**

**Что такое и зачем**

- [ ] **contextlib** предоставляет **удобные способы** создавать и комбинировать контекстные менеджеры (объекты для **with**). **@contextmanager** — описать контекст **генератором**: код до **yield** — вход, код после **yield** — выход; исключения из блока **with** пробрасываются в генератор. **suppress(\*exceptions)** — подавить указанные исключения в блоке (вместо пустого **except**). **redirect_stdout**/ **redirect_stderr** — подменить потоки вывода в контексте (тесты, перехват вывода). **ExitStack** — динамически открывать несколько контекстов (число неизвестно заранее); при выходе все откатываются в обратном порядке. **nullcontext(enter_result)** — пустой контекст (удобно при условном использовании: **ctx = open(f) if f else nullcontext()**). **closing(thing)** — вызвать **thing.close()** при выходе из **with**. См. также §14 для углублённого разбора.

**Пример contextlib**

```python
from contextlib import contextmanager, suppress, redirect_stdout, ExitStack, nullcontext
import io
# @contextmanager — контекст через генератор
@contextmanager
def managed_resource():
    r = acquire()
    try:
        yield r
    finally:
        release(r)
with managed_resource() as r:
    use(r)
# suppress — подавить исключения
with suppress(FileNotFoundError):
    os.remove("maybe_missing.txt")
# redirect_stdout — перехват вывода (тесты)
with redirect_stdout(io.StringIO()) as buf:
    print("hidden")
captured = buf.getvalue()
# ExitStack — динамически несколько контекстов
with ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in filenames]
    process(files)
# nullcontext — условный контекст
ctx = open(path) if path else nullcontext(None)
with ctx as f:
    if f:
        f.read()
```

**contextvars — контекстные переменные**

- [ ] **Что такое и зачем:** **contextvars** (PEP 567) предоставляет **контекстные переменные** — значения, привязанные к контексту выполнения (отдельно для каждого потока и для каждой цепочки корутин в asyncio). В отличие от глобальных переменных, значение в одном потоке/задаче не видно в другом. **Применения:** передача запроса/пользователя в веб-приложении без явной передачи аргументом по всей цепочке вызовов; хранение контекста в async без глобальных переменных.
- [ ] **API:** **contextvars.ContextVar(name, default=...)** — объявить переменную (**name** — для отладки); **.get(default=...)** — получить значение в текущем контексте (если не установлено — вернуть **default** или **LookupError** при отсутствии default у переменной). **.set(value)** — установить значение в текущем контексте; возвращает **Token** для отката. **.reset(token)** — вернуть значение к состоянию до **.set()** (обязательно передавать токен, возвращённый **.set()**). **contextvars.copy_context()** — копия текущего контекста (dict переменных → значения); **.run(func, \*args, **kwargs)** — выполнить **func(\*args, **kwargs)** в этом контексте (значения переменных из копии). В asyncio каждая **Task** имеет свой контекст; при **asyncio.create_task(coro)** контекст копируется из создающей задачи. **Граничные случаи:** **reset** с чужим токеном приводит к **ValueError**; в потоках (**threading**) контекст наследуется при создании потока, но изменения в дочернем потоке не видны в родителе.

**Пример contextvars (запрос в веб-приложении)**

```python
import contextvars
request_id_var = contextvars.ContextVar('request_id', default=None)

def handle_request(request_id):
    request_id_var.set(request_id)
    process()  # вложенные вызовы могут получить request_id через request_id_var.get()

def process():
    rid = request_id_var.get()  # без передачи аргументом по всей цепочке
    print(f'Processing {rid}')
```

### copy, pickle, marshal

**copy — поверхностная и глубокая копия**

**Что такое и зачем**

- [ ] **copy** — создание **копии** объекта. **copy.copy(x)** — **поверхностная** копия: создаётся новый объект того же типа, но **вложенные** объекты (элементы списка, значения словаря) остаются **теми же ссылками**. Изменение вложенного объекта в копии видно в оригинале. **copy.deepcopy(x)** — **глубокая** копия: рекурсивно копируются все вложенные объекты; копия независима от оригинала. **Применения:** дублирование структур данных без изменения оригинала (поверхностная — быстрая, но общие вложенные объекты); изоляция изменений (глубокая); обход изменяемых значений по умолчанию в функциях (создать копию списка/словаря).
- [ ] Для объектов с ****copy**(self)** и ****deepcopy**(self, memo)** вызываются эти методы; **memo** — словарь для обхода циклов (один объект копируется один раз). **Граничные случаи:** циклы ссылок (A → B → A) — **deepcopy** обрабатывает через **memo**. Модули, классы, функции — копируются по ссылке (не дублируются). **deepcopy** может быть медленным и потреблять много памяти для больших структур.

**Пример: поверхностная vs глубокая копия**

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0][0] = 99
print(a[0][0])   # 99 — вложенный список общий

c = copy.deepcopy(a)
c[0][0] = 0
print(a[0][0])   # 99 — оригинал не изменился
```

**pickle — сериализация Python-объектов**

**Что такое и зачем**

- [ ] **pickle** — преобразование **произвольных** Python-объектов в поток байт и обратно. Сохраняются типы, структура, ссылки на один и тот же объект (дедупликация). **Применения:** сохранение состояния приложения, кеш вычислений на диск, обмен объектами между процессами (multiprocessing), сессионные данные (осторожно: безопасность). **Не для ненадёжных данных:** загрузка pickle выполняет код; только доверенные источники.
- [ ] **pickle.dump(obj, file, protocol=None)** — записать объект в файл (файл открыть в **'wb'**); **pickle.load(file)** — прочитать один объект (файл в **'rb'**). **pickle.dumps(obj)** → bytes; **pickle.loads(data)** → объект. **protocol** 0 (текстовый, устаревший), 1 (бинарный), 2 (Python 2.3+), 3 (Python 3.0+, по умолчанию в Py3), 4 (3.4+ — большие объекты, эффективнее), 5 (3.8+ — out-of-band data). Не сериализуются: открытые файлы, сокеты, соединения БД, функции с замыканиями над несериализуемым; лямбды и вложенные функции — с ограничениями. **pickletools.dis(data)** — разбор потока pickle (отладка). **Граничные случаи:** при **pickle.load** недоверенных данных возможна выполнение произвольного кода; для обмена с другими языками или ненадёжным источником использовать **json** или **struct**. Один и тот же объект по ссылке сериализуется один раз (дедупликация).

**Пример pickle**

```python
import pickle
data = {"a": 1, "b": [2, 3]}
# В файл
with open("cache.pkl", "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
# Из файла
with open("cache.pkl", "rb") as f:
    loaded = pickle.load(f)
# В память (bytes) — для multiprocessing.Queue, сети
b = pickle.dumps(data)
obj = pickle.loads(b)
# Класс — сериализуется, если все атрибуты сериализуемы
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
p = Point(1, 2)
pickle.loads(pickle.dumps(p)).x  # 1
# Несериализуемое — PicklingError
pickle.dumps(open("x.txt"))  # PicklingError
```

**marshal — внутренняя сериализация интерпретатора**

**Что такое и зачем**

- [ ] **marshal** — модуль **внутренней сериализации** Python: преобразование объектов в байтовый поток в формате, используемом интерпретатором для хранения скомпилированного кода (.pyc), поддержки **marshal** в **persistence** и т.д. Формат **не документирован как стабильный** и может меняться между версиями Python; предназначен для внутреннего использования, а не для обмена данными между приложениями или долгосрочного хранения. **Применения:** только если вы пишете инструменты, работающие с .pyc или с внутренними структурами интерпретатора; для любых других задач — **pickle** (Python-объекты), **json** (обмен с другими системами) или **struct** (бинарные протоколы).
- [ ] **API:** **marshal.dumps(value, version)** — сериализовать объект в **bytes**; **version** (0–4) — версия формата (совместимость между версиями Py3). **marshal.loads(bytes)** — десериализовать из bytes. Поддерживаются только «простые» типы: **None**, **bool**, **int**, **float**, **str** (bytes в старых версиях), **tuple**, **list**, **dict**, **set**, **frozenset**, **code objects** (объекты байткода); **не поддерживаются** классы, экземпляры, функции, замыкания, многие встроенные объекты. **marshal.dump(obj, file, version)** и **marshal.load(file)** — запись/чтение в файл (бинарный режим).
- [ ] **Граничные случаи:** формат **marshal** не гарантирован между разными версиями Python (например 3.10 и 3.12); загрузка данных, созданных другой версией, может дать **ValueError** или несовместимое поведение. **Не использовать** для конфигов, кеша или обмена с другими процессами/машинами — только **pickle** или **json**. Безопасность: **marshal.loads** не выполняет произвольный код (в отличие от pickle), но некорректные данные могут вызвать сбой интерпретатора; данные должны быть из доверенного источника.

**Пример marshal (только для понимания API)**

```python
import marshal
# Сериализация простых типов (редко нужна в прикладном коде)
data = marshal.dumps([1, 2, 'hello'])
restored = marshal.loads(data)   # [1, 2, 'hello']
# Для персистентности и обмена — всегда pickle или json
```

### dataclasses, enum

**dataclasses — классы данных**

**Что такое и зачем**

- [ ] **dataclasses** — декоратор **@dataclass** и функции для **классов данных**: автоматическая генерация ****init****, ****repr****, ****eq**** по объявленным полям; опционально ****lt**** (order=True), ****hash**** (frozen=True), ****post_init**** для проверок. **field(default_factory=list)** решает проблему мутабельного default (один общий список у всех экземпляров). **Применения:** конфиги, DTO, записи с полями без ручного boilerplate; **asdict**/ **astuple** для сериализации; **replace()** для неизменяемых вариантов (frozen). См. также §10 для углублённого разбора.

**enum — перечисления**

**Что такое и зачем**

- [ ] **enum** — **именованные константы** с уникальными значениями: **Enum** (базовый), **IntEnum** (сравнимы с int), **StrEnum** (3.11+, сравнимы со str); **Flag**/ **IntFlag** для битовых флагов (объединение через **|**). **auto()** — автонумерация; **@unique** — запрет дубликатов value. **Применения:** статусы (**State.PENDING**), коды операций, варианты выбора вместо «магических» чисел/строк; типизация и автодополнение в IDE. См. также §15a0 для углублённого разбора.

### datetime, time, calendar

**datetime — дата и время**

**Что такое и зачем**

- [ ] **datetime** — типы для **даты и времени**: **date** (год, месяц, день), **time** (час, минута, секунда, микросекунда), **datetime** (date + time), **timedelta** (разница во времени), **timezone** (смещение от UTC). **Применения:** логи (время события), планировщики, отображение дат пользователю, расчёт интервалов, работа с временными зонами (см. **zoneinfo**).
- [ ] **datetime.now(tz=None)** — текущие дата и время (если **tz** передан — **aware**, иначе **naive**). **datetime.utcnow()** — UTC (рекомендуется **datetime.now(timezone.utc)**). **strftime(format)** — форматирование в строку по **format** (например **'%Y-%m-%d %H:%M:%S'**). **strptime(string, format)** — разбор строки в **datetime** по формату. **datetime.fromisoformat(s)** (3.7+) — разбор **ISO 8601** из строки (**YYYY-MM-DD**, **YYYY-MM-DDTHH:MM:SS**, с **+HH:MM** для зоны); аналогично **date.fromisoformat(s)** и **time.fromisoformat(s)** для типов **date** и **time**. **timedelta** — разница; поддерживает **+**, **-** с **date**/ **datetime**; атрибуты **days**, **seconds**, **microseconds**. Сравнение **naive** с **aware** — **TypeError**; см. §8b.

**Форматы strftime / strptime (основные):** **%Y** — год (4 цифры), **%m** — месяц (01–12), **%d** — день; **%H** — час (24), **%M** — минута, **%S** — секунда; **%A** / **%a** — полное/краткое имя дня недели; **%B** / **%b** — месяц; **%Z** — имя зоны; **%%** — литерал **%**.

**Пример datetime**

```python
from datetime import datetime, timedelta, timezone
now = datetime.now(timezone.utc)
s = now.strftime('%Y-%m-%d %H:%M')   # '2024-01-15 12:30'
dt = datetime.strptime('2024-01-15', '%Y-%m-%d')
tomorrow = dt + timedelta(days=1)
```

**time — метки и паузы**

**Что такое и зачем**

- [ ] **time** — **метки времени** и **паузы**. Разные часы решают разные задачи: **time.time()** — секунды с эпохи (1.1.1970 UTC); это **системные часы** — могут **идти назад** при NTP или ручной смене. **time.monotonic()** — **монотонные** часы (никогда не идут назад); для **интервалов** и **таймаутов** (например **deadline = time.monotonic() + 5**). **time.perf_counter()** — счётчик для **замеров производительности** (высокое разрешение, не привязан к календарю). **Применения:** таймауты — **monotonic**; замер скорости кода — **perf_counter**; календарное время (логи, отображение) — **time** + **localtime**/ **gmtime**.
- [ ] **time.sleep(sec)** — приостановить выполнение на **sec** секунд (может прерваться сигналом; на части платформ разрешение ниже секунды). **time.localtime(ts)** — метку в структуру **struct_time** (год, месяц, день, час и т.д.) в **локальной** зоне; **time.gmtime(ts)** — в UTC; **time.mktime(tuple)** — **struct_time** (локальное) обратно в метку. **Граничный случай:** сравнение интервалов по **time.time()** при смене системного времени даёт неверный результат; для интервалов всегда **monotonic**.

**Пример time**

```python
import time
# Таймаут через monotonic (не идёт назад при NTP)
deadline = time.monotonic() + 5.0
while time.monotonic() < deadline:
    if work_done():
        break
    time.sleep(0.1)
# Замер производительности
start = time.perf_counter()
heavy_computation()
elapsed = time.perf_counter() - start
# Календарное время: метка → struct_time
ts = time.time()
local = time.localtime(ts)   # локальная зона
utc = time.gmtime(ts)        # UTC
# Обратно: struct_time → метка
ts2 = time.mktime(local)
# Пауза (может прерваться сигналом)
time.sleep(1.5)
```

**calendar**

**Что такое и зачем**

- [ ] **calendar** — **календарные** расчёты без создания объектов **date**/ **datetime**: число дней в месяце, день недели, високосный год, сетка месяца по неделям. **Применения:** календари в UI (сетка на месяц), проверка допустимости даты (дней в месяце), расчёт «первый понедельник месяца» и т.п.
- [ ] **calendar.monthrange(year, month)** — кортеж **(день*недели*первого*дня (0=пн), число*дней)**; для февраля — **(..., 28|29)**. **calendar.isleap(year)** — високосный год. **calendar.weekday(year, month, day)** — день недели (0 = понедельник, 6 = воскресенье). **calendar.monthcalendar(year, month)** — список недель (каждая неделя — список из 7 чисел, 0 для дней «чужого» месяца); удобно для отрисовки календаря по строкам.

**Пример calendar**

```python
import calendar
calendar.monthrange(2024, 2)   # (3, 29) — 1 фев 2024 четверг, 29 дней
calendar.isleap(2024)          # True
calendar.weekday(2024, 1, 15)  # 0 — понедельник
calendar.monthcalendar(2024, 1)[0]  # [1, 2, 3, 4, 5, 6, 7] — первая неделя
```

### decimal, fractions, numbers, statistics, math, cmath

**decimal — десятичная арифметика**

**Что такое и зачем**

- [ ] **decimal** — арифметика в **десятичной** системе с заданной точностью (число значащих цифр). В отличие от **float** (IEEE 754, двоичное представление), **Decimal('0.1')** хранит ровно 0.1; нет ошибок вида **0.1 + 0.2 != 0.3**. **Применения:** финансы (суммы, проценты, налоги), учёт, любые расчёты, где важна точность в десятичной системе и предсказуемое округление.
- [ ] **Decimal(str_or_int)** — создать число; предпочтительно из **строки** (**Decimal('0.1')**), чтобы избежать погрешности float при **Decimal(0.1)**. **getcontext()** — глобальный контекст: **prec** (число значащих цифр, по умолчанию 28), **rounding** (ROUND_HALF_UP, ROUND_HALF_EVEN и др.). **decimal.localcontext(ctx)** — временно изменить контекст в блоке **with**. **quantize(exp)** — округлить до заданного экспонента (например до копеек). Арифметика **+**, **-**, **\***, **/** — без накопления двоичной погрешности.

**Пример decimal**

```python
from decimal import Decimal, getcontext
getcontext().prec = 4
a = Decimal('0.1') + Decimal('0.2')   # Decimal('0.3')
b = Decimal('10') / Decimal('3')      # Decimal('3.333')
# Округление до двух знаков после запятой
Decimal('3.14159').quantize(Decimal('0.01'))   # Decimal('3.14')
```

**fractions — рациональные числа**

**Что такое и зачем**

- [ ] **fractions** — **точные рациональные** числа (числитель/знаменатель): арифметика без погрешности float. **Fraction(a, b)** — дробь **a/b**; **Fraction(str)** — из строки (**Fraction('0.1')** даёт **Fraction(1, 10)**); **Fraction(float)** — из float, но **Fraction(0.1)** ≠ **Fraction(1, 10)** из-за представления 0.1 в float — для точности создавать из **строки**. **limit_denominator(max_denominator)** — приблизить к рациональному с ограничением знаменателя (удобно для «простых» дробей). **Применения:** символьная математика, точные дроби без потери точности, периодические дроби.

**Пример fractions**

```python
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)   # Fraction(1, 2)
Fraction('0.1')                   # Fraction(1, 10)
Fraction(0.1).limit_denominator(100)  # Fraction(1, 10) — приближение
```

**numbers — ABC для числовых типов**

**Что такое и зачем**

- [ ] **numbers** — **иерархия абстрактных базовых классов** для числовых типов: **Number** (корень) → **Complex** → **Real** → **Rational** → **Integral**. **isinstance(x, numbers.Real)** — True для **int**, **float**, **Fraction**, **Decimal** (все реализуют **Real**). **Применения:** проверка «число ли» без перечисления типов (**isinstance(x, numbers.Number)**); аннотации (**def f(x: numbers.Real)**); реализация своих числовых типов, совместимых с **+**, **-**, **\*** и т.д.
- [ ] **Иерархия:** **Integral** — целые (int, bool); **Rational** — рациональные (Fraction); **Real** — вещественные (+ float, Decimal); **Complex** — комплексные (+ complex). **numbers.Number** не реализуется напрямую; проверять **isinstance(x, (int, float, complex, Decimal, Fraction))** или **isinstance(x, numbers.Number)**. **Граничный случай:** **bool** — подкласс **int**, поэтому **isinstance(True, numbers.Integral)** — True; при необходимости «только целые, не bool» проверять **type(x) is int** или **isinstance(x, numbers.Integral) and not isinstance(x, bool)**.

**Пример numbers**

```python
import numbers
def accept_real(x):
    if not isinstance(x, numbers.Real):
        raise TypeError('Expected a real number')
    return x * 2
accept_real(1)      # 2
accept_real(1.5)    # 3.0
accept_real(1+0j)  # TypeError — complex не Real
```

**statistics — статистические функции**

**Что такое и зачем**

- [ ] **statistics** — **описательная статистика** по последовательности чисел: среднее, медиана, мода, дисперсия, стандартное отклонение, квантили. Работают с **итераторами** (не только списками); данные могут быть **однократно** потребляемым итератором (для многократного использования передавать список). **StatisticsError** — при пустой выборке, одном элементе (для stdev/variance нужны минимум два), несовместимых типах (например смешение str и int). **Применения:** анализ данных, отчёты, метрики (среднее время ответа, медиана задержки), дашборды.
- [ ] **Основной API:** **statistics.mean(data)** — среднее арифметическое; **median(data)** — медиана (при чётном числе — среднее двух центральных); **median_low**/ **median_high** — нижняя/верхняя медиана из пары; **mode(data)** — наиболее частое значение (при равных частотах — первый встреченный); **stdev(data)** — стандартное отклонение по выборке (делитель n-1); **variance(data)** — дисперсия; **quantiles(data, n=4)** — границы **n** квантилей (по умолчанию квартили, возвращает список из n-1 значений). **harmonic_mean**, **geometric_mean** (3.8+) — среднее гармоническое и геометрическое. **Граничные случаи:** **mean([])** и **median([])** — **StatisticsError**; **stdev([1])** — **StatisticsError** (нужно минимум 2 точки); **mode** при нескольких равных по частоте возвращает первый из них.

**Пример statistics**

```python
import statistics
data = [1, 2, 2, 3, 4, 5]
statistics.mean(data)    # 2.833...
statistics.median(data)  # 2.5
statistics.mode(data)    # 2
statistics.stdev(data)   # 1.471...
```

**math и cmath**

**Что такое и зачем**

- [ ] **math** — функции для **float**: тригонометрия (**sin**, **cos**, **tan**, **asin**, **acos**, **atan2** — углы в радианах), логарифмы и степени (**log**, **log10**, **exp**, **sqrt**, **pow**), округление (**floor**, **ceil**, **trunc**), **factorial**, **gcd**; **math.isclose(a, b, rel_tol=1e-09, abs_tol=0.0)** — сравнение с допуском (избегать **==** для float из-за погрешности); **math.inf**, **math.nan**. **cmath** — те же функции для **complex** (результат — комплексное число); **cmath.phase(z)** — аргумент (в радианах), **cmath.polar(z)** — (модуль, аргумент); **cmath.rect(r, phi)** — из полярных в комплексное. **Применения:** научные расчёты, графика, физика, геометрия. **Граничные случаи:** **math.sqrt(-1)** — **ValueError**; **cmath.sqrt(-1)** — **1j**. Для сравнения float использовать **math.isclose(a, b)**, а не **a == b**.

**Пример math и cmath**

```python
import math, cmath
math.isclose(0.1 + 0.2, 0.3)   # True (избегаем 0.1 + 0.2 == 0.3 → False)
math.gcd(12, 18)                # 6
cmath.phase(1 + 1j)              # 0.785... (π/4)
cmath.polar(1 + 1j)              # (1.414..., 0.785...)
cmath.rect(2, math.pi/2)         # (0+2j) — модуль 2, угол π/2
```

### difflib, filecmp

**difflib — сравнение последовательностей**

**Что такое и зачем**

- [ ] **difflib** — **сравнение** двух последовательностей (строк, списков строк): коэффициент сходства, блоки совпадений, генерация патча в формате unified diff, поиск «похожих» строк. **Применения:** автодополнение и исправление опечаток (**get_close_matches**), генерация патчей (**unified_diff**), сравнение версий текста, подсветка различий в UI (**HtmlDiff**).
- [ ] **SequenceMatcher(None, a, b)** — **a**, **b** — последовательности (например строки). **.ratio()** — число от 0 до 1 (1 — полное совпадение). **.get_matching_blocks()** — список блоков совпадений **(i, j, n)** (индексы и длина). **get_close_matches(word, possibilities, n=3, cutoff=0.6)** — до **n** наиболее похожих строк из **possibilities**; **cutoff** — минимальный ratio (0.6 по умолчанию).
- [ ] **unified_diff(a, b, fromfile='', tofile='', lineterm='\\n')** — итератор строк в формате **diff -u**; можно записать в файл или передать в **patch**. **Differ()** — построчное сравнение с маркерами **+** (только во втором), **-** (только в первом), **?** (подсказки). **HtmlDiff().make_file(...)** — HTML-страница с подсветкой различий.

**Пример difflib: автодополнение**

```python
import difflib
words = ['apple', 'application', 'apply', 'banana']
difflib.get_close_matches('appel', words, n=2, cutoff=0.6)   # ['apple', 'apply']
difflib.get_close_matches('app', words, n=3)   # ['apple', 'apply', 'application']
```

**filecmp — сравнение файлов и каталогов**

**Что такое и зачем**

- [ ] **filecmp** — **сравнение файлов и каталогов** по содержимому или по метаданным (размер, время). **Применения:** синхронизация каталогов, проверка бэкапов, «сухой прогон» копирования (что изменилось), тесты (ожидаемый вывод vs фактический).
- [ ] **filecmp.cmp(f1, f2, shallow=True)** — **равны ли** два файла. **shallow=True** (по умолчанию) — сравнение по **размеру** и **времени модификации** (быстро, но два файла с одинаковыми метаданными считаются равными без проверки содержимого); **shallow=False** — **побайтовое** сравнение содержимого. **filecmp.dircmp(dir1, dir2)** — сравнение **каталогов**: атрибуты **same_files** (одинаковое содержимое), **diff_files** (разное), **left_only** (только в первом), **right_only** (только во втором), **subdirs** (dict имён подкаталогов → **Dircmp**). **.report()** — печать текстового отчёта в stdout; **.report_full_closure()** — с рекурсией по подкаталогам.

**Пример filecmp**

```python
import filecmp
# Сравнение двух файлов
filecmp.cmp("a.txt", "b.txt")                    # по размеру и mtime (shallow=True)
filecmp.cmp("a.txt", "b.txt", shallow=False)    # побайтово
# Сравнение каталогов
dc = filecmp.dircmp("dir1", "dir2")
dc.same_files      # файлы с одинаковым содержимым
dc.diff_files      # файлы с разным содержимым
dc.left_only       # только в dir1
dc.right_only      # только в dir2
dc.report()        # текстовый отчёт в stdout
# Рекурсивно по подкаталогам
dc.report_full_closure()
# Или обход subdirs вручную
for name, sub_dc in dc.subdirs.items():
    print(name, sub_dc.diff_files)
```

### email, mimetypes, html

**email — парсинг и построение MIME-сообщений**

- [ ] **Что такое и зачем:** модуль **email** служит для **разбора** (парсинга) и **создания** почтовых сообщений в формате MIME (RFC 2822, MIME-расширения): заголовки (From, To, Subject, Content-Type и т.д.), тело в разных кодировках и типах контента, вложения (файлы), multipart (несколько частей в одном письме). Применения: парсинг писем из почтовых ящиков (mbox, Maildir), генерация писем для отправки через **smtplib**, разбор вложений и заголовков, обработка веб-форм с файлами (multipart/form-data использует ту же модель).
- [ ] **Парсинг:** **email.message_from_string(s)** — разобрать строку в объект **Message**; **email.message_from_file(fp)** — из файла/потока; **email.message_from_bytes(b)** — из bytes. У **Message**: **['Subject']**, **['From']** — доступ к заголовкам; **get_payload(decode=True)** — тело (декодированное из base64/quoted-printable при decode=True); **is_multipart()** — True если несколько частей; **walk()** — итератор по всем частям (включая вложенные multipart).
- [ ] **Построение сообщений:** **email.mime.text.MIMEText(body, subtype='plain', charset='utf-8')** — текстовая часть; **email.mime.multipart.MIMEMultipart()** — контейнер для нескольких частей; **attach(part)** — добавить часть. **email.mime.base.MIMEBase(maintype, subtype)** — произвольный MIME-тип; **set_payload(data)**; **add_header()**. **email.mime.image.MIMEImage** — изображения; **email.mime.application.MIMEApplication** — произвольные данные. Для вложений: открыть файл в бинарном режиме, прочитать, создать **MIMEBase** или **MIMEApplication**, задать заголовок **Content-Disposition: attachment; filename="..."**.
- [ ] **Политика и кодировки:** **email.policy** задаёт правила разбора (default, SMTP, HTTP); **message.as_string()** — сериализация в строку для отправки. Кодировка заголовков (например Subject на не-ASCII) через **Header** или **email.utils** (formataddr, formatdate).

**Пример: парсинг письма и извлечение вложений**

```python
import email
msg = email.message_from_string(raw_message)
subject = msg['Subject']
for part in msg.walk():
    if part.get_content_maintype() == 'multipart':
        continue
    filename = part.get_filename()
    if filename:
        with open(filename, 'wb') as f:
            f.write(part.get_payload(decode=True))
```

**mimetypes — определение MIME-типа по расширению**

- [ ] **Что такое и зачем:** **mimetypes** сопоставляет **расширение файла** (и иногда имя файла) с **MIME-типом** (например **.pdf** → **application/pdf**) и обратно. Используется веб-серверами для заголовка **Content-Type**, почтовыми клиентами для вложений, диалогами сохранения файлов и т.д. База типов загружается из системных файлов (например **/etc/mime.types**) и может быть дополнена.
- [ ] **API:** **mimetypes.guess_type(url_or_filename)** — возвращает кортеж **(type, encoding)**; type — строка MIME (например **'text/html'**) или **None**; encoding — например **'gzip'** для сжатых данных или **None**. Для **.gz** вернёт **(None, 'gzip')** (сжатие, а не тип содержимого). **mimetypes.guess_extension(type, strict=False)** — расширение по MIME-типу (например **'application/pdf'** → **'.pdf'**); при нескольких вариантах возвращает один из них. **mimetypes.add_type(type, ext, strict=True)** — добавить сопоставление в кеш (например **add_type('application/json', '.json')**). **mimetypes.init(files=None)** — перечитать базу из списка путей. **Граничные случаи:** для неизвестного расширения **guess_type** вернёт **(None, None)**; для URL с query-строками (**file.pdf?x=1**) расширение берётся из пути до **?**.
- [ ] **Пример:** **mimetypes.guess_type('doc.pdf')** → **('application/pdf', None)**; **mimetypes.guess_extension('image/png')** → **'.png'**; **mimetypes.add_type('application/vnd.myapp+json', '.myapp')** — зарегистрировать свой тип.

**Пример mimetypes**

```python
import mimetypes
mimetypes.guess_type("doc.pdf")        # ('application/pdf', None)
mimetypes.guess_type("archive.tar.gz") # (None, 'gzip')
mimetypes.guess_extension("image/png") # '.png'
mimetypes.guess_type("unknown.xyz")    # (None, None)
mimetypes.add_type("application/x-myapp", ".myapp")
mimetypes.guess_type("file.myapp")    # ('application/x-myapp', None)
```

**html — экранирование и парсинг HTML**

- [ ] **Что такое и зачем:** модуль **html** содержит утилиты для безопасной работы с HTML: **экранирование** спецсимволов (**<**, **>**, **&**, кавычки), чтобы пользовательский ввод не ломал разметку и не внедрял скрипты (XSS); **обратное преобразование** из HTML-сущностей в символы; **парсинг** HTML (базовый, без внешних зависимостей).
- [ ] **html.escape(s, quote=True)** — заменяет **&** на **&amp;**; **<** на **&lt;**; **>** на **&gt;**; при **quote=True** также **"** на **&quot;** и **'** на **&#x27;** (или **&#39;**). Обязательно применять к любому тексту, вставляемому в HTML (комментарии, поля форм, вывод в шаблонах).
- [ ] **html.unescape(s)** — обратное преобразование: **&amp;** → **&**; **&lt;** → **<**; числовые сущности **&#123;** и именованные **&nbsp;** и т.д. Удобно при извлечении текста из HTML.
- [ ] **html.parser.HTMLParser** — потоковый парсер HTML. Наследуют класс и переопределяют **handle_starttag(tag, attrs)**, **handle_endtag(tag)**, **handle_data(data)** и др.; затем **parser.feed(html_string)**. Не строит DOM; подходит для простого извлечения ссылок или текста без тяжёлых библиотек. Для сложного парсинга обычно используют **html.parsers** или сторонние **lxml**, **beautifulsoup4**. **Граничные случаи:** **escape** с **quote=False** не экранирует кавычки — для атрибутов в кавычках использовать **quote=True**.

**Пример html**

```python
import html
user_input = '<script>alert(1)</script>'
html.escape(user_input)  # '&lt;script&gt;alert(1)&lt;/script&gt;'
html.escape('Say "Hi"', quote=True)  # 'Say &quot;Hi&quot;'
html.unescape('&amp;&lt;&gt;')  # '&<>'
from html.parser import HTMLParser
class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
    def handle_data(self, data):
        self.text.append(data)
    def get_text(self):
        return "".join(self.text)
p = TextExtractor()
p.feed("<p>Hello <b>world</b></p>")
p.close()
p.get_text()  # 'Hello world'
```

### errno, faulthandler, traceback, warnings

**errno — коды ошибок ОС**

**Что такое и зачем**

- [ ] **errno** — **целые константы** кодов ошибок, возвращаемых системными вызовами (open, read, stat и т.д.). При возникновении **OSError** (или **FileNotFoundError**, **PermissionError** и др.) атрибут **e.errno** содержит код; по нему можно определить причину и обработать её. **Применения:** разная обработка «файл не найден» и «доступ запрещён», повтор при **EINTR**, логирование по коду.
- [ ] **errno.ENOENT** — файл/каталог не найден; **errno.EACCES** — доступ запрещён; **errno.EEXIST** — файл уже существует; **errno.EINTR** — системный вызов прерван сигналом; **errno.ENOSPC** — нет места на устройстве; **errno.EBUSY** — устройство или ресурс занят. **errno.errorcode** — dict: код → строка имени (**errorcode[2]** → **'ENOENT'**).

**Пример errno**

```python
import errno
import os
try:
    with open("missing.txt") as f:
        f.read()
except OSError as e:
    if e.errno == errno.ENOENT:
        print("File not found")
    elif e.errno == errno.EACCES:
        print("Permission denied")
    else:
        print(errno.errorcode.get(e.errno, "Unknown"), e.strerror)
# EINTR — повтор при прерывании сигналом
while True:
    try:
        data = sock.recv(1024)
        break
    except OSError as e:
        if e.errno != errno.EINTR:
            raise
```

**faulthandler — дамп при сбоях**

- [ ] **Что такое и зачем:** **faulthandler** выводит **traceback** текущих потоков в stderr (или в файл) при фатальных сбоях: segfault, abort в C-расширениях, фатальные сигналы (SIGSEGV, SIGABRT и т.д.). Без faulthandler процесс может завершиться без вывода; с **faulthandler.enable()** в момент сбоя печатается стек вызовов Python. **Применения:** отладка падений интерпретатора и нативных расширений, диагностика в продакшене (включить в начале и при необходимости писать дамп в файл).
- [ ] **API:** **faulthandler.enable(file=sys.stderr, all_threads=True)** — включить вывод при фатальном сбое; **file** — поток или путь к файлу (строка); **all_threads=True** — печатать стеки всех потоков. **faulthandler.dump_traceback(file=sys.stderr, all_threads=True)** — принудительно вывести текущий стек **сейчас** (без ожидания сбоя); удобно по сигналу (например SIGUSR1) для «снимка» состояния. **faulthandler.dump_traceback_later(delay, repeat=False, file=..., exit=False)** — вывести traceback через **delay** секунд (и при **repeat=True** повторять); применяют при подозрении на зависание (дать процессу N секунд, затем напечатать стек и при **exit=True** завершить). **Граничные случаи:** в момент сбоя допустимы только async-signal-safe операции; вывод может быть обрезан при очень глубоком стеке.

**Пример faulthandler**

```python
import faulthandler
import signal
# Включить в начале приложения (например в main)
faulthandler.enable()
# При SIGUSR1 — вывести стек всех потоков (для отладки зависаний)
def handler(signum, frame):
    faulthandler.dump_traceback(all_threads=True)
signal.signal(signal.SIGUSR1, handler)
# Или писать в файл
faulthandler.enable(file=open("/tmp/traceback.txt", "w"))
# При подозрении на зависание: через 5 сек вывести стек и выйти
faulthandler.dump_traceback_later(5, exit=True)
# ... код, который может зависнуть ...
faulthandler.cancel_dump_traceback_later()  # отменить, если не зависли
```

**traceback — форматирование стека вызовов**

**Что такое и зачем**

- [ ] **traceback** — **получение и форматирование** стека вызовов при исключении или текущего стека. **Применения:** логирование полного traceback (**format_exc**), кастомные обработчики ошибок, отладочные сообщения.
- [ ] **traceback.format_exc(limit=None, chain=True)** — строка с traceback **текущего** исключения (вызывать внутри **except**); **limit** — число кадров сверху/снизу. **traceback.print_exception(type, value, tb, limit=None, file=None, chain=True)** — печать в **file** (по умолчанию stderr); **type, value, tb** — из **sys.exc_info()**. **traceback.extract_tb(tb, limit=None)** — список **StackSummary** (FrameSummary: filename, lineno, name, line); для программной обработки. **traceback.print_stack(f=None, limit=None)** — печать текущего стека (без исключения). **traceback.format_tb(tb)** — список строк кадров. **traceback.format_exception(type, value, tb)** — список строк полного сообщения об исключении (включая заголовок и цепочку cause). **Граничные случаи:** в **except** без повторного raise **sys.exc_info()** и **format_exc** всё ещё доступны до выхода из блока.

**Пример traceback**

```python
import traceback
try:
    1 / 0
except ZeroDivisionError:
    # Полный traceback в строку для лога
    tb_str = traceback.format_exc()
    log.error(tb_str)
    # Список кадров для анализа
    for frame in traceback.extract_tb(sys.exc_info()[2]):
        print(frame.filename, frame.lineno, frame.name)
# Текущий стек без исключения
traceback.print_stack(limit=5)
```

**warnings — предупреждения**

**Что такое и зачем**

- [ ] **warnings** — механизм **предупреждений**: сообщения не прерывают выполнение, но выводятся в stderr (или обрабатываются фильтрами). **Применения:** устаревший API (**DeprecationWarning**), будущие изменения (**FutureWarning**), предупреждения о стиле или производительности (**UserWarning**).
- [ ] **warnings.warn(message, category=UserWarning, stacklevel=1)** — выдать предупреждение; **stacklevel** — откуда считать кадр (для обёрток: **stacklevel=2** — вызывающий код). **warnings.filterwarnings(action, message='', category=Warning, module='', lineno=0)** — глобальный фильтр: **action** — **'ignore'**, **'error'** (превратить в исключение), **'always'**, **'default'**, **'module'**, **'once'**. **warnings.catch_warnings(record=False, module=None)** — контекстный менеджер для временного подавления или записи предупреждений (**record=True** → список в **warnings_list**). Категории: **DeprecationWarning** (по умолчанию скрыт в ****main**** в 3.2+), **FutureWarning**, **SyntaxWarning**, **UserWarning**, **ImportWarning**. **Граничные случаи:** при **filterwarnings('error', category=DeprecationWarning)** предупреждение превращается в исключение; в тестах часто **warnings.simplefilter('ignore', DeprecationWarning)**.

**Пример warnings**

```python
import warnings
warnings.warn("This API is deprecated", DeprecationWarning, stacklevel=2)
# Подавить в блоке
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    old_api()
    assert len(w) == 1
    assert issubclass(w[0].category, DeprecationWarning)
# Превратить в исключение
warnings.filterwarnings("error", category=UserWarning)
# warnings.warn("oops", UserWarning)  # UserWarning как исключение
```

### functools, operator

**functools — утилиты для функций и декораторов**

**Что такое и зачем**

- [ ] **functools** предоставляет **инструменты для функций**: **partial** — зафиксировать часть аргументов; **reduce** — свёртка последовательности в одно значение; **lru_cache**/ **cache** — кеширование результатов (LRU или неограниченный); **wraps** — копировать метаданные обёрнутой функции в декоратор; **cmp_to_key** — преобразовать функцию сравнения двух аргументов в key function для **sorted**; **total_ordering** — по ****eq**** и одному из ****lt****/ ****le****/ ****gt****/ ****ge**** сгенерировать остальные методы сравнения; **singledispatch**/ **singledispatchmethod** — перегрузка по типу первого аргумента; **cached_property** — свойство с кешем при первом обращении. **Применения:** декораторы, кеширование, миграция с Py2 (cmp→key), перегрузка по типу, ленивые атрибуты. См. также §12 для углублённого разбора.

**Пример functools**

```python
from functools import partial, reduce, lru_cache, wraps, cmp_to_key, total_ordering, cached_property
# partial — зафиксировать аргументы
def greet(greeting, name):
    return f"{greeting}, {name}"
say_hi = partial(greet, "Hi")
say_hi("Alice")  # "Hi, Alice"
# reduce
reduce(lambda a, b: a * b, [1, 2, 3, 4])  # 24
# lru_cache — кеш результатов
@lru_cache(maxsize=128)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
# wraps — сохранить __name__/__doc__ в декораторе
def my_decorator(f):
    @wraps(f)
    def wrapper(*a, **k):
        return f(*a, **k)
    return wrapper
# cmp_to_key — для sorted (миграция с Py2)
sorted([3, 1, 2], key=cmp_to_key(lambda a, b: a - b))
# total_ordering — по __eq__ и __lt__ сгенерировать остальные сравнения
@total_ordering
class Node:
    def __init__(self, val): self.val = val
    def __eq__(self, o): return self.val == o.val
    def __lt__(self, o): return self.val < o.val
# cached_property — свойство с кешем при первом обращении
class C:
    @cached_property
    def expensive(self):
        return compute()
```

**operator — функции, соответствующие операторам**

- [ ] **Что такое и зачем:** модуль **operator** предоставляет функции, соответствующие **встроенным операторам** и доступу к атрибутам/элементам. Удобно когда нужна **функция** (например для **map**, **sorted(key=...)**, **reduce**), а не выражение. **Применения:** **sorted(items, key=operator.attrgetter('name'))**, **reduce(operator.mul, list)**, **map(operator.add, a, b)**.
- [ ] **Арифметика и сравнения:** **operator.add**, **operator.sub**, **operator.mul**, **operator.truediv**, **operator.floordiv**, **operator.mod**, **operator.pow**; **operator.eq**, **operator.lt**, **operator.le**, **operator.gt**, **operator.ge**, **operator.ne**; **operator.neg**, **operator.not\_**; **operator.truth(x)** — bool(x); **operator.is\_(a, b)** — a is b; **operator.is_not(a, b)**.
- [ ] **Доступ к элементам и атрибутам:** **operator.itemgetter(i)** — функция **lambda x: x[i]**; **itemgetter(1, 3)** — **lambda x: (x[1], x[3])** (кортеж для сортировки по нескольким полям). **operator.attrgetter('name')** — функция **lambda x: x.name**; **attrgetter('a', 'b')** — **lambda x: (x.a, x.b)**. **operator.methodcaller('method', \*args, **kwargs)** — функция, вызывающая метод с заданными аргументами: **lambda x: x.method(\*args, **kwargs)**.
- [ ] **Прочее:** **operator.contains(seq, item)** — **item in seq**; **operator.countOf(seq, item)**; **operator.indexOf(seq, item)**. **operator.setitem(obj, key, value)** — **obj[key] = value**; **operator.getitem(obj, key)** — **obj[key]**; **operator.delitem(obj, key)** — **del obj[key]**.

**Пример operator**

```python
import operator
from functools import reduce
# Сортировка по атрибуту и по нескольким полям
class Item:
    def __init__(self, name, score):
        self.name, self.score = name, score
items = [Item("Bob", 80), Item("Alice", 90)]
sorted(items, key=operator.attrgetter("score"))  # по score
sorted(items, key=operator.attrgetter("name", "score"))  # по name, затем score
# reduce
reduce(operator.mul, [1, 2, 3, 4])  # 24
# itemgetter для списков/кортежей
pairs = [(1, "a"), (2, "b"), (1, "c")]
sorted(pairs, key=operator.itemgetter(0, 1))  # по первому элементу, потом по второму
# methodcaller
f = operator.methodcaller("upper")
f("hello")  # "HELLO"
```

### gc, sys, types, copyreg

**gc — сборщик мусора**

**Что такое и зачем**

- [ ] **gc** — доступ к **сборщику мусора** (reference counting + циклический сборщик). В обычном коде вызывать не обязательно; нужен при отладке утечек, тонкой настройке (отключение циклического сбора в критичном участке) или работе с C-расширениями, выделяющими память вне управления Python. **Применения:** **gc.collect()** — принудительный цикл сбора; **gc.get_objects()** — список отслеживаемых объектов (осторожно: большой список); **gc.get_referrers(obj)** — кто ссылается на **obj**; **gc.get_referents(obj)** — на что ссылается **obj**. **gc.disable()** / **gc.enable()** — отключить/включить циклический сборщик.
- [ ] **Граничный случай:** **gc.get_objects()** возвращает все объекты, отслеживаемые сборщиком; на больших процессах это может быть медленно и потреблять память. Использовать точечно для отладки.

**Пример gc**

```python
import gc
# Принудительный цикл сбора (редко нужен)
gc.collect()
# Отладка: кто ссылается на объект
obj = []
refs = gc.get_referrers(obj)
# Отладка: на что ссылается объект
refs = gc.get_referents(obj)
# Временно отключить циклический сборщик (осторожно)
gc.disable()
# ... критичный участок ...
gc.enable()
```

**sys — системные параметры и окружение**

**Что такое и зачем**

- [ ] **sys** — **доступ к параметрам интерпретатора и окружению**: аргументы командной строки, путь поиска модулей, стандартные потоки, версия Python, лимиты. **Применения:** CLI (**sys.argv**), тесты (подмена **sys.stdout**, **sys.path**), проверка версии (**sys.version_info**), завершение с кодом (**sys.exit(code)**), отладка (**sys.getsizeof**, **sys.getrecursionlimit**).
- [ ] **sys.argv** — список аргументов (argv[0] — имя скрипта или **'-c'** при **-c**). **sys.path** — список каталогов для поиска модулей; можно изменять. **sys.modules** — dict загруженных модулей (имя → модуль). **sys.stdout**, **sys.stderr**, **sys.stdin** — объекты потоков; можно заменить для перенаправления вывода (например в тестах). **sys.exit(code)** — выбросить **SystemExit** (по умолчанию code 0). **sys.getsizeof(obj)** — приблизительный размер в байтах (только сам объект, без вложенных). **sys.version_info** — (major, minor, micro); сравнение **sys.version_info >= (3, 10)**. **sys.getrecursionlimit()** / **sys.setrecursionlimit(n)** — максимальная глубина стека вызовов (по умолчанию порядка 1000). **sys.breakpointhook** — функция, вызываемая встроенной **breakpoint()** (3.7+); по умолчанию подключает **pdb**; можно заменить для кастомной отладки или отключения в продакшене. **breakpoint()** — остановка в этой точке и вход в отладчик (эквивалент **pdb.set_trace()**).

**Пример sys**

```python
import sys
# Аргументы CLI: python script.py a b c → sys.argv == ['script.py', 'a', 'b', 'c']
if len(sys.argv) < 2:
    sys.exit(1)
input_file = sys.argv[1]
# Проверка версии
if sys.version_info < (3, 10):
    sys.exit("Requires Python 3.10+")
# Добавить каталог в путь поиска модулей
sys.path.insert(0, "/opt/mylib")
# Подмена stdout в тестах
old_stdout = sys.stdout
sys.stdout = io.StringIO()
print("captured")
out = sys.stdout.getvalue()
sys.stdout = old_stdout
# Завершение с кодом
sys.exit(0)
```

**types и copyreg**

- [ ] **types** — **типы** для интроспекции и динамического создания: **types.FunctionType**, **types.ModuleType**, **types.SimpleNamespace**, **types.new_class(name, bases, exec_body)** — создать класс в runtime (exec_body — callable, получает namespace для заполнения). **types.CoroutineType**, **types.GeneratorType**, **types.AsyncGeneratorType** — для **isinstance** (проверка «это корутина/генератор»). **types.MappingProxyType** — неизменяемая обёртка над dict (только чтение). **Применения:** плагины, метапрограммирование, проверка типа без жёсткой привязки к имени класса. **Граничный случай:** **type(x)** даёт конкретный класс; **isinstance(x, types.FunctionType)** — True для обычных функций, False для встроенных (например **len**); для «вызываемый объект» использовать **callable(x)** или **collections.abc.Callable**.
- [ ] **copyreg** — **расширение pickle**: **copyreg.pickle(type, func)** — при сериализации объектов **type** вызывать **func(obj)**; функция должна вернуть кортеж **(constructor, (args...))** или **(constructor, (args...), state)** для восстановления (constructor вызывается с *args при десериализации). **copyreg.pickle(type, func, constructor=None)** — при **constructor** восстановление идёт через \*\*constructor(*args)**. **Применения:** обратная совместимость при переименовании класса или модуля (зарегистрировать старый тип под новым конструктором); кастомная сериализация встроенных типов (например **datetime** с другим форматом). **Граничный случай:** при изменении структуры класса старые pickle-файлы могут не загрузиться; **copyreg** позволяет задать функцию, которая по старым данным вернёт аргументы для нового конструктора.

**Пример types**

```python
import types
# Проверка типа: корутина, генератор
def gen():
    yield 1
async def coro():
    pass
isinstance(gen(), types.GeneratorType)   # True
isinstance(coro(), types.CoroutineType)  # True
# SimpleNamespace — объект с атрибутами (как объект-конфиг)
ns = types.SimpleNamespace(a=1, b=2)
ns.a, ns.b  # 1, 2
# MappingProxyType — неизменяемый вид словаря (только чтение)
d = {"x": 1}
proxy = types.MappingProxyType(d)
proxy["x"]  # 1
# proxy["y"] = 2  # TypeError
# Обычная функция vs встроенная
def f(): pass
isinstance(f, types.FunctionType)    # True
isinstance(len, types.FunctionType)  # False (builtin)
callable(len)  # True
```

**Пример copyreg: кастомная сериализация**

```python
import copyreg, pickle
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
# При pickle Point вызывается reducer; он возвращает (конструктор, (аргументы,))
def point_reducer(p):
    return (Point, (p.x, p.y))
copyreg.pickle(Point, point_reducer)
# Теперь Point сериализуется через (Point, (x, y)); при переименовании Point
# можно зарегистрировать старый тип под новым конструктором для обратной совместимости
```

### getpass, getopt, gettext, locale

**getpass — безопасный ввод пароля**

**Что такое и зачем**

- [ ] **getpass** — **ввод пароля** без отображения символов на экране (символы не печатаются при вводе). Использует возможности терминала или читает из stdin при перенаправлении. **Применения:** CLI-скрипты (логин, API-ключ), интерактивная аутентификация. Всегда использовать вместо **input()** для паролей.
- [ ] **getpass.getpass(prompt='Password: ', stream=None)** — вывести **prompt**, прочитать пароль (без эха); вернуть строку. **stream** — поток для вывода prompt (по умолчанию sys.stderr). Если stdin не терминал (перенаправление, pipe), читает из stdin **без скрытия** — предупреждение выводится в stderr. **getpass.getuser()** — имя текущего пользователя (из **LOGNAME**/ **USER**/ **USERNAME** или из системы; на Windows — из переменных окружения). **Граничные случаи:** в неинтерактивном режиме (CI, cron) **getpass** читает до EOF; для скриптов лучше проверять **sys.stdin.isatty()** и не вызывать **getpass** при перенаправлении или передавать пароль через переменную окружения/файл.

**Пример getpass**

```python
import getpass
try:
    password = getpass.getpass("Enter password: ")
except getpass.GetPassWarning:
    pass  # ввод не из терминала
user = getpass.getuser()  # текущий пользователь ОС
# Для неинтерактивного режима:
import sys
if sys.stdin.isatty():
    pwd = getpass.getpass()
else:
    pwd = os.environ.get("MYAPP_PASSWORD") or sys.stdin.read().strip()
```

**getopt — разбор аргументов в стиле C**

**Что такое и зачем**

- [ ] **getopt** — **минимальный** парсер аргументов командной строки в стиле C (функция **getopt** в C и утилита getopt): разбор коротких опций (**-a**, **-b**), длинных опций (**--long**), опций со значением (**-o file**, **--output=file**). Не строит дерево подкоманд и не генерирует справку автоматически; подходит для простых скриптов с небольшим числом флагов. **Для нового кода предпочтителен argparse:** подкоманды, автогенерация **--help**, единообразные сообщения об ошибках, типы и значения по умолчанию.
- [ ] **API:** **getopt.getopt(args, shortopts, longopts=[])** — разобрать список **args** (обычно **sys.argv[1:]**). **shortopts** — строка коротких опций: буква без двоеточия — флаг без значения (**'v'** → **-v**); с **:** — опция со значением (**'o:'** → **-o file**). **longopts** — список длинных имён: **'help'** — флаг; **'output='** — опция со значением. Возвращает **(opts, args)**: **opts** — список пар **(opt, value)** (например **('-o', 'out.txt')**, **('--verbose', '')**); **args** — оставшиеся позиционные аргументы. **getopt.gnu_getopt(...)** — расширенный режим: необязательные аргументы, смешение опций и позиционных (GNU-стиль).
- [ ] **Пример:** разбор **-i input.txt -v** или **--input=input.txt --verbose**: **shortopts='i:v'** (i со значением, v — флаг), **longopts=['input=', 'verbose']**; цикл по **opts** для применения значений. **Типичные ошибки:** забыть **':'** в shortopts для опции со значением; при неизвестной опции **getopt** выбрасывает **GetoptError** — обрабатывать в **try/except** и выводить подсказку.

**Пример getopt**

```python
import getopt, sys
try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:vo', ['input=', 'verbose', 'output='])
except getopt.GetoptError as e:
    print(f'Error: {e}', file=sys.stderr)
    sys.exit(2)
input_file = None
verbose = False
for opt, arg in opts:
    if opt in ('-i', '--input'): input_file = arg
    elif opt in ('-v', '--verbose'): verbose = True
    elif opt in ('-o', '--output'): output_file = arg
# args — оставшиеся позиционные аргументы
```

**gettext — интернационализация (i18n)**

**Что такое и зачем**

- [ ] **gettext** — **перевод строк** по каталогам сообщений (.po/.mo): строка-идентификатор сопоставляется с переведённой строкой для выбранной локали. **Применения:** мультиязычные приложения, локализация сообщений и интерфейса.
- [ ] **gettext.translation(domain, localedir=None, languages=None)** — загрузить каталог; **domain** — имя домена (обычно имя приложения); **localedir** — каталог с подкаталогами **locale/LC_MESSAGES/**; **languages** — список кодов языков (**['ru_RU', 'ru']**). Возвращает объект с методами **gettext(msg)** — перевод строки; **ngettext(singular, plural, n)** — форма множественного числа. Часто создают алиас **\_ = translation(...).gettext** и оборачивают строки: **\_('Hello')**. Каталоги собирают из .po в .mo утилитой **msgfmt**. **gettext.install(domain, localedir)** — установить **_()** в builtins для всего приложения.

**Пример gettext**

```python
import gettext
# Структура: locale/ru/LC_MESSAGES/app.mo
t = gettext.translation("app", localedir="locale", languages=["ru"])
_ = t.gettext
print(_("Hello"))  # Привет (если есть ru)
# Множественное число
n = 2
print(t.ngettext("%d file", "%d files", n) % n)  # "2 файла" / "2 files"
# Установить _ глобально
gettext.install("app", localedir="locale")
```

**locale — локаль системы**

**Что такое и зачем**

- [ ] **locale** — **текущая локаль** (язык, территория, кодировка, форматы чисел и дат). Влияет на **strftime**, сортировку строк, **format_string** для чисел. **Применения:** вывод чисел и дат в формате пользователя, локализованная сортировка.
- [ ] **locale.getlocale(category=LC_CTYPE)** — кортеж **(language, encoding)** для категории (например **('ru_RU', 'UTF-8')**). **locale.setlocale(category, locale)** — установить локаль (**locale=''** — по переменным окружения **LANG**, **LC_ALL**); **locale.LC_ALL** — все категории; **LC_CTYPE**, **LC_COLLATE**, **LC_TIME** и др. **locale.format_string(fmt, val, grouping=False)** — форматировать число по локали (разделитель тысяч). **Граничные случаи:** **setlocale** влияет на весь процесс; в многопоточных приложениях предпочтительнее передавать локаль явно.

**Пример locale**

```python
import locale
locale.getlocale()  # ('ru_RU', 'UTF-8') или (None, None)
locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
locale.format_string("%d", 1234567, grouping=True)  # '1 234 567' (с разделителем)
# Сброс к умолчанию (C)
locale.setlocale(locale.LC_ALL, "")
```

### glob, fnmatch, pathlib, os, shutil, tempfile, fileinput

**glob — поиск путей по шаблону**

- [ ] **glob.glob(pattern)** — **список** путей (строк), совпадающих с **pattern**. Синтаксис: **\*** — любая последовательность символов в компоненте пути; **?** — один символ; **\[...\]** — класс символов. **glob.iglob(pattern)** — итератор (экономия памяти при большом числе файлов). **glob.glob('dir/**/\*.py', recursive=True)** (3.5+) — рекурсивный поиск в **dir** и подкаталогах. **pathlib.Path.glob()** предпочтительнее при работе с pathlib (возвращает объекты Path). **Применения:\*\* поиск всех .py в проекте, выбор файлов по маске.

**Пример glob**

```python
import glob
glob.glob("*.py")           # ['a.py', 'b.py']
glob.glob("src/**/*.py", recursive=True)  # все .py в src и подкаталогах
```

**fnmatch — сопоставление имён с шаблоном**

- [ ] **fnmatch.fnmatch(name, pattern)** — True/False; шаблон в стиле shell (**\***, **?**, **\[...\]**). **fnmatch.filter(names, pattern)** — отфильтровать список имён. **fnmatch.translate(pattern)** — преобразовать шаблон в строку регулярного выражения (для **re.match**). **Применения:** фильтрация имён файлов без реального доступа к ФС, конфиги с масками имён.

**Пример fnmatch**

```python
import fnmatch
fnmatch.fnmatch("test.py", "*.py")   # True
fnmatch.filter(["a.py", "b.txt", "c.py"], "*.py")  # ['a.py', 'c.py']
```

**pathlib — объектно-ориентированные пути**

- [ ] **Что такое и зачем:** **pathlib** даёт объектное представление путей: **Path** (конкретный путь с операциями I/O) и **PurePath** (без доступа к диску). Методы **.read_text()**, **.write_text()**, **.read_bytes()**, **.write_bytes()** — чтение/запись без явного **open**; **.glob()**, **.rglob()** — поиск по шаблону; оператор **/** — конкатенация путей; **.resolve()**, **.absolute()** — абсолютный путь. Класс зависит от ОС: **PosixPath** (Unix), **WindowsPath** (Windows). **Применения:** любой код, работающий с файлами и каталогами; предпочтительнее **os.path** в новом коде. См. также §8 для углублённого разбора.

**Пример pathlib**

```python
from pathlib import Path
p = Path(".") / "data" / "file.txt"
p.write_text("hello")
p.read_text()
list(Path(".").glob("*.py"))
list(Path("src").rglob("*.py"))
(p / "sub" / "f.json").resolve()
Path.cwd()
Path.home()
```

**os — интерфейс к ОС и файловой системе**

- [ ] **Что такое и зачем:** **os** — доступ к переменным окружения (**os.environ**, **os.getenv**, **os.putenv**), к файловой системе (**os.listdir**, **os.scandir**, **os.walk**, **os.mkdir**, **os.remove**, **os.chmod**, **os.rename**, **os.stat**), к процессу (**os.getpid**, **os.getcwd**, **os.chdir**, **os.system**), к идентификаторам пользователя (**os.getuid**, **os.geteuid** на Unix). **os.path** — функции для путей: **join**, **split**, **abspath**, **exists**, **isfile**, **isdir**, **getsize** и т.д. **Применения:** скрипты, зависящие от окружения и ФС; низкоуровневые операции, для которых в pathlib нет метода. См. также §8, §8a для углублённого разбора.

**Пример os**

```python
import os
os.environ.get("HOME")
os.getcwd()
os.chdir("/tmp")
os.listdir(".")
for root, dirs, files in os.walk("project"):
    for f in files:
        print(os.path.join(root, f))
os.path.exists("file.txt")
os.path.getsize("file.txt")
os.mkdir("newdir")
```

**shutil — высокоуровневые операции с файлами**

- [ ] **Что такое и зачем:** **shutil** — копирование файлов и каталогов (**shutil.copy**, **shutil.copy2** — с метаданными, **shutil.copytree** — рекурсивно), перемещение (**shutil.move** — между дисками копирует и удаляет), удаление дерева (**shutil.rmtree**), создание архива (**shutil.make_archive** — zip/tar). **shutil.which(cmd)** — поиск исполняемого **cmd** в **PATH** (возвращает путь или None). **shutil.disk_usage(path)** — объём диска (total, used, free). **Применения:** бэкапы, копирование конфигов, деплой, проверка наличия утилиты в PATH.

**Пример shutil**

```python
import shutil
shutil.copy("src.txt", "dst.txt")
shutil.copy2("src.txt", "dst.txt")  # с метаданными
shutil.copytree("project", "backup")
shutil.move("old.txt", "new.txt")
shutil.rmtree("temp_dir")
shutil.which("python")
total, used, free = shutil.disk_usage("/")
```

**tempfile — временные файлы и каталоги (кратко)**

- [ ] **Что такое и зачем:** **tempfile** создаёт **временные** файлы и каталоги с уникальными именами в системной директории (**/tmp** или аналог). **TemporaryFile()** — файл без имени в ФС (удаляется при закрытии); **NamedTemporaryFile(delete=True)** — с именем (**.name**); **TemporaryDirectory()** — каталог (удаляется при выходе из **with**). **mkstemp()**, **mkdtemp()** — низкоуровневый API (возвращают fd/path; удаление вручную). **Применения:** промежуточные данные, кеш, загрузки. Подробно — в блоке «tempfile, hashlib, secrets» ниже.

**fileinput — итерация по строкам нескольких файлов (кратко)**

- [ ] **Что такое и зачем:** **fileinput** даёт единый итератор по строкам **нескольких файлов** подряд или по **stdin**, с метаданными: **fileinput.filename()**, **fileinput.lineno()**, **fileinput.filelineno()**. Режим **inplace=True** — перенаправление stdout в текущий файл (замена «на месте»). **Применения:** скрипты вида **python script.py f1.txt f2.txt**; пакетная замена в файлах. Подробнее — см. подраздел «fileinput» ниже.

**fileinput — итерация по строкам нескольких файлов**

- [ ] **fileinput.input(files=None, inplace=False, ...)** — итератор по строкам. **files** — список имён файлов или None (тогда **sys.argv[1:]**); если пусто — stdin. **fileinput.filename()** — имя текущего файла; **fileinput.lineno()** — накопительный номер строки; **fileinput.filelineno()** — номер строки в текущем файле. **inplace=True** — запись идёт в тот же файл (stdout перенаправляется в файл; для замены «на месте»). **Применения:** скрипты вида **python script.py f1.txt f2.txt** (обработка как одного потока строк), пакетная замена в файлах.

**Пример fileinput**

```python
import fileinput
for line in fileinput.input(["a.txt", "b.txt"]):
    print(fileinput.filename(), fileinput.filelineno(), line, end="")
```

### hashlib, hmac, secrets

**hashlib — криптографические хеш-функции**

- [ ] **Что такое и зачем:** **hashlib** предоставляет **односторонние** хеш-функции: произвольные данные (bytes) преобразуются в фиксированную «отпечаток» (хеш) фиксированной длины. Одинаковые данные дают одинаковый хеш; малейшее изменение данных меняет хеш. **Применения:** проверка целостности файлов (checksums, контрольные суммы), дедупликация, хеш-таблицы для больших ключей, подписи (в связке с HMAC), хранение паролей (только через **pbkdf2_hmac** или **scrypt**, не «сырой» SHA). **Не для паролей в открытом виде:** для верификации паролей использовать **hashlib.pbkdf2_hmac** с солью и итерациями; для новых приложений предпочтительны **passlib** или **bcrypt** (сторонние).
- [ ] **Доступные алгоритмы:** **hashlib.algorithms_guaranteed** — набор, доступный на всех платформах (обычно **md5**, **sha1**, **sha224**, **sha256**, **sha384**, **sha512**, **blake2b**, **blake2s**, **sha3_224** и др.); **hashlib.algorithms_available** — все доступные в текущей сборке. **hashlib.new(name, data=b'', **kwargs)\*\* — создать объект хеша по имени строки (удобно для динамического выбора алгоритма).
- [ ] **API объекта хеша:** конструктор **hashlib.sha256(data)** или **hashlib.md5()** и т.д.; **.update(data)** — добавить данные (bytes); можно вызывать многократно. **.digest()** — хеш в виде **bytes** (длина зависит от алгоритма); **.hexdigest()** — строка из hex-символов (удобно для логов и сравнения). **.copy()** — копия состояния (для ветвления расчёта). **.block_size**, **.digest_size** — атрибуты алгоритма. Для файла: читать блоками и вызывать **h.update(chunk)**; в конце **h.hexdigest()**.
- [ ] **Хранение паролей:** **hashlib.pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None)** — производный ключ из пароля (PBKDF2); **salt** — случайные bytes (например **secrets.token_bytes(16)**); **iterations** — число итераций (десятки/сотни тысяч). Сравнивать через **secrets.compare_digest(derived1, derived2)**. **hashlib.scrypt(password, \*, salt, n, r, p, maxmem=..., dklen=64)** (3.6+) — альтернатива, устойчивее к GPU-атакам.

**Пример: хеш файла и проверка целостности**

```python
import hashlib
def file_hash(path, algo='sha256'):
    h = hashlib.new(algo)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()
# file_hash('archive.zip')  # 'a1b2c3...'
```

**hmac — HMAC (Hash-based Message Authentication Code)**

- [ ] **Что такое и зачем:** **HMAC** — механизм **аутентификации сообщений**: хеш вычисляется не только от данных, но и от **секретного ключа**. Получатель, зная ключ, может повторить расчёт и сравнить результат; без ключа подделать HMAC практически невозможно. **Применения:** подпись запросов (API-ключи), защита cookies, верификация целостности и подлинности данных в каналах (например Webhook).
- [ ] **API:** **hmac.new(key, msg=None, digestmod=hashlib.sha256)** — создать объект HMAC; **key** и **msg** — bytes. **.update(msg)** — добавить данные (можно вызывать несколько раз); **.digest()**, **.hexdigest()** — итоговый код. **hmac.compare_digest(a, b)** — сравнение двух строк/bytes **без утечки по времени** (constant-time), чтобы по длительности сравнения нельзя было подобрать токен. **digestmod** может быть строкой (**'sha256'**) или объектом из hashlib. Рекомендуется **sha256** или **sha512**; **md5**/ **sha1** — только для совместимости со старыми протоколами. **Граничные случаи:** ключ должен быть достаточно случайным и храниться в секрете; при верификации всегда использовать **hmac.compare_digest(calculated, received)**, а не **==**, иначе возможна timing-атака.

**Пример hmac: подпись запроса**

```python
import hmac
import hashlib
key = b'secret-api-key'
body = b'{"user": 123}'
sig = hmac.new(key, body, hashlib.sha256).hexdigest()
# Отправить body и заголовок X-Signature: sig
# На приёмной стороне:
expected = hmac.new(key, body, hashlib.sha256).hexdigest()
if not hmac.compare_digest(expected, received_signature):
    raise ValueError("Invalid signature")
```

**secrets — криптостойкие случайные данные**

- [ ] **Что такое и зачем:** модуль **secrets** предназначен для генерации **криптографически стойких** случайных данных (пароли, токены, ключи). Использует **os.urandom()** (или эквивалент ОС). **Не использовать random:** **random** предсказуем и не предназначен для безопасности; для паролей, токенов, соли — только **secrets**.
- [ ] **API:** **secrets.token_bytes(nbytes=None)** — n байт случайных данных (по умолчанию 32); возвращает **bytes**. **secrets.token_hex(nbytes=None)** — то же в виде строки hex (длина строки 2\*nbytes). **secrets.token_urlsafe(nbytes=None)** — строка в base64 без символов **+** и **/** (удобно для URL и cookies). **secrets.choice(sequence)** — случайный элемент последовательности (криптостойкий выбор). **secrets.compare_digest(a, b)** — сравнение двух строк/bytes **без утечки по времени** (защита от timing-attack при проверке токенов и паролей).
- [ ] **Применения:** генерация соли для паролей (**secrets.token_bytes(16)**), токенов сессии (**secrets.token_urlsafe(32)**), одноразовых ссылок сброса пароля; проверка токена через **secrets.compare_digest(provided, expected)**. **Граничные случаи:** **token_urlsafe** даёт строку длиной около **ceil(nbytes \* 4 / 3)** символов (base64); для 32 байт — 43 символа. Пароли для пользователей: **secrets.choice(string.ascii_letters + string.digits)** в цикле или использовать **secrets** для длины и набора символов.

**Пример secrets**

```python
import secrets
# Токен для URL (сброс пароля, подтверждение email)
token = secrets.token_urlsafe(32)   # строка, безопасная для query-параметра
# Соль для хеширования пароля
salt = secrets.token_bytes(16)
# Проверка токена (без timing-attack)
if not secrets.compare_digest(user_token, stored_token):
    raise PermissionError("Invalid token")
# Случайный пароль из 12 символов
alphabet = "abcdefghijkmnpqrstuvwxyz23456789"
password = "".join(secrets.choice(alphabet) for _ in range(12))
```

### http, urllib, socket, ssl

**http.client — низкоуровневый HTTP-клиент**

- [ ] **Что такое и зачем:** **http.client** реализует протокол HTTP на уровне запрос/ответ: установка TCP-соединения, отправка запроса (метод, путь, заголовки, тело), чтение ответа (статус, заголовки, тело). **Применения:** скрипты загрузки страниц, API-клиенты без зависимостей, когда нужен полный контроль над заголовками и телом. Для типичных задач (GET/POST с простыми заголовками) проще **urllib.request.urlopen** или библиотека **requests** (сторонняя).
- [ ] **API:** **http.client.HTTPConnection(host, port=80)** — объект соединения; **.request(method, url, body=None, headers={})** — отправить запрос (**method** — **'GET'**, **'POST'** и т.д.; **url** — путь с query, например **'/path?k=v'**; **body** — bytes для POST); **.getresponse()** — получить объект **HTTPResponse**: **.status** (200, 404 и т.д.), **.reason**, **.getheaders()**, **.read()** (тело — bytes). **http.client.HTTPSConnection(host, port=443)** — то же через TLS. После **getresponse()** можно вызвать **.request()** снова для следующего запроса (keep-alive) или **.close()**. **Граничные случаи:** при редиректах (301, 302) нужно вручную следовать **Location** или использовать **urllib**; таймауты задаются через **HTTPConnection(..., timeout=10)**.

**Пример http.client**

```python
import http.client
conn = http.client.HTTPSConnection("example.com")
conn.request("GET", "/")
resp = conn.getresponse()
print(resp.status, resp.reason)
body = resp.read()
print(body.decode())
conn.request("POST", "/api", b'{"x":1}', headers={"Content-Type": "application/json"})
resp2 = conn.getresponse()
conn.close()
```

**http.server — простой HTTP-сервер**

- [ ] **Что такое и зачем:** **http.server** предоставляет **простые** классы для обслуживания HTTP-запросов: раздача файлов по пути URL (GET), логирование. **Применения:** локальная раздача статики (**python -m http.server 8000**), быстрый демо-сервер для разработки, прототипы. **Не для продакшена:** нет аутентификации, ограничения скорости, полноценной обработки ошибок; для продакшена используют **gunicorn**, **uwsgi**, **nginx** и т.д.
- [ ] **Классы:** **socketserver.TCPServer** подкласс **HTTPServer(server_address, RequestHandlerClass)** — сервер; **server_address** — кортеж **(host, port)** (пустая строка **''** — все интерфейсы). **BaseHTTPRequestHandler** — базовый обработчик: переопределяют **do_GET()**, **do_POST()** и т.д.; **self.path** — путь из URL; **self.headers** — заголовки; **self.wfile** — поток для ответа (write bytes); **self.send_response(code)** — отправить статус; **self.send_header(name, value)**; **self.end_headers()**. **SimpleHTTPRequestHandler** — раздаёт файлы из текущего каталога по пути из URL (без выхода за пределы каталога); **CGIHTTPRequestHandler** — плюс запуск CGI-скриптов в подкаталоге **cgi-bin**. **server.serve_forever()** — цикл приёма запросов; **server.shutdown()** — остановить. **Граничные случаи:** путь из URL может содержать **..** — SimpleHTTPRequestHandler не отдаёт файлы вне текущего каталога; для привязки только к localhost использовать **('127.0.0.1', 8000)**.

**Пример http.server**

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
server = HTTPServer(("", 8000), SimpleHTTPRequestHandler)
# Запуск: python -m http.server 8000  — то же самое
server.serve_forever()
# Кастомный обработчик — только GET с логированием
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path, self.client_address)
        super().do_GET()
HTTPServer(("", 8000), MyHandler).serve_forever()
```

**urllib.request — открытие URL (HTTP, HTTPS, file)**

- [ ] **Что такое и зачем:** **urllib.request** — высокоуровневый API для **открытия** URL: HTTP/HTTPS GET (и POST с data), **file:**, **ftp:** (ограниченно). Возвращает объект, ведущий себя как файл (read, readline и т.д.). **Применения:** быстрая загрузка страницы или файла по URL, скрипты автоматизации без сторонних библиотек.
- [ ] **API:** **urllib.request.urlopen(url, data=None, timeout=..., cafile=..., capath=...)** — открыть URL; возвращает **http.client.HTTPResponse**-подобный объект с **.read()**, **.status**, **.getheader()**. **data** — bytes для POST (при **data** метод автоматически POST); **timeout** — таймаут в секундах. **Request(url, data=None, headers={})** — сформировать запрос с заголовками (например **Request(url, headers={'User-Agent': 'MyApp/1.0'})**); передать в **urlopen(request)**. **OpenerDirector**, **build_opener()** — кастомные обработчики (редиректы, cookies, Basic Auth через **HTTPBasicAuthHandler**, **HTTPPasswordMgr**). **urllib.error.URLError** (включая **HTTPError**) — ошибки сети и HTTP (код 404, 500 и т.д.); у **HTTPError** атрибуты **.code**, **.reason**, **.headers**. **Граничные случаи:** по умолчанию редиректы обрабатываются автоматически; при необходимости отключить — кастомный opener без **HTTPRedirectHandler**. Для проверки SSL-сертификатов используются **cafile**/ **capath** или системное хранилище.

**Пример urllib.request**

```python
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
try:
    with urlopen("https://example.com", timeout=10) as resp:
        data = resp.read()
        print(resp.status)
except HTTPError as e:
    print(e.code, e.reason)
except URLError as e:
    print(e.reason)
# POST с заголовками
req = Request("https://api.example.com", data=b'{"k":"v"}', headers={"Content-Type": "application/json"}, method="POST")
with urlopen(req) as resp:
    result = resp.read()
```

**urllib.parse — разбор и сборка URL**

- [ ] **Что такое и зачем:** **urllib.parse** разбирает и формирует **строки URL**: извлечение схемы, хоста, пути, query-строки, фрагмента; кодирование/декодирование query-параметров; объединение базового URL и относительного пути. **Применения:** парсинг ссылок, построение URL для API (query-параметры), нормализация путей.
- [ ] **Функции:** **urlparse(url)** — разбить на **ParseResult** (scheme, netloc, path, params, query, fragment); **.geturl()** — собрать обратно; **ParseResult** — named tuple, можно подставлять через **.\_replace(path=...)**. **urlunparse(parts)** — собрать URL из итерируемого из 6 элементов. **parse_qs(query_string)** — query-строка в словарь списков значений (**key=val&key=val2** → **{'key': ['val', 'val2']}**); **parse_qsl** — список пар. **urlencode(query, doseq=False)** — словарь или список пар в строку **key=value&...**; при **doseq=True** значения-списки разворачиваются в несколько ключей. **urljoin(base, url)** — объединить базовый URL и относительный (учёт базового пути и схемы); если **url** абсолютный (начинается с схемы), возвращается **url**. **quote(s, safe='/')** — кодировать символы для использования в URL (пробел → **%20**); **unquote(s)** — декодировать. **Граничные случаи:** при разборе URL без схемы **urlparse** может интерпретировать первый компонент как path или netloc в зависимости от наличия **//**; для относительных путей **urljoin** отсекает последний сегмент базового path перед присоединением.

**Пример urllib.parse**

```python
from urllib.parse import urlparse, urljoin, urlencode, parse_qs, quote
p = urlparse("https://example.com/path?a=1&b=2#anchor")
# p.scheme, p.netloc, p.path, p.query, p.fragment
params = parse_qs(p.query)  # {'a': ['1'], 'b': ['2']}
urljoin("https://example.com/a/b", "c")   # https://example.com/a/c
urljoin("https://example.com/a/b", "/c")  # https://example.com/c
urlencode({"q": "hello world", "page": 1})  # q=hello+world&page=1
quote("/path?x=1")  # %2Fpath%3Fx%3D1 — для пути с зарезервированными символами
```

**socket — низкоуровневые сокеты**

- [ ] **Что такое и зачем:** **socket** — интерфейс к **BSD-сокетам**: создание TCP/UDP/Unix-сокетов, привязка к адресу, подключение, приём/отправка данных. Основа для **http.client**, **urllib**, **asyncio** и любых сетевых протоколов. **Применения:** кастомные протоколы, серверы с полным контролем, multicast, raw-сокеты (с ограничениями ОС).
- [ ] **Основное API:** **socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0)** — создать сокет; **AF_INET** (IPv4), **AF_INET6** (IPv6), **SOCK_STREAM** (TCP), **SOCK_DGRAM** (UDP). **.bind((host, port))** — привязать к адресу (сервер); **host** — строка или **''** (все интерфейсы); **.listen(backlog)** — начать приём подключений (**backlog** — размер очереди); **.accept()** — принять новое подключение (возвращает **conn, addr** — новый сокет и адрес клиента). **.connect((host, port))** — подключиться (клиент). **.send(data)** / **.recv(bufsize)** — отправка/приём bytes (TCP); **.sendall(data)** — отправить все байты (повторяет send до конца). **.sendto(data, addr)** / **.recvfrom(bufsize)** — UDP. **.settimeout(sec)** — таймаут операций (None — блокирующий режим). **.close()** — закрыть. Контекстный менеджер **with socket.socket(...) as s:** закрывает сокет при выходе. **Граничные случаи:** **recv** может вернуть меньше байт, чем **bufsize**; для полного сообщения — цикл или протокол с длиной/разделителем. **send** может отправить не все байты — использовать **sendall**. При разрыве соединения **recv** вернёт пустой bytes.

**Пример socket (TCP сервер и клиент)**

```python
import socket
# Сервер
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", 9999))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        conn.sendall(b"Echo: " + data)
# Клиент
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 9999))
    s.sendall(b"Hello")
    print(s.recv(1024))  # b'Echo: Hello'
```

**ssl — TLS/SSL (шифрование и сертификаты)**

- [ ] **Что такое и зачем:** модуль **ssl** оборачивает сокеты в **TLS/SSL**: шифрование трафика, проверка сертификатов сервера (и клиента при mutual TLS). **Применения:** HTTPS, защищённые API, SMTP over TLS, любое TCP-соединение с шифрованием.
- [ ] **Основное API:** **ssl.wrap_socket(sock, ...)** — устаревший упрощённый API; предпочтительнее **ssl.SSLContext**. **ssl.create_default_context()** — контекст с разумными настройками (проверка сертификата, современные протоколы). **context.wrap_socket(sock, server_side=False, server_hostname=hostname)** — обернуть сокет; для **клиента** **server_hostname** обязателен для проверки имени в сертификате (SNI). **context.load_cert_chain(certfile, keyfile)** — для сервера: загрузить сертификат и ключ. **context.load_verify_locations(cafile=..., capath=...)** — доверенные корневые сертификаты; по умолчанию **create_default_context()** загружает системное хранилище. **context.check_hostname** — включена ли проверка имени (для клиента по умолчанию True). Исключения: **ssl.SSLError** (в т.ч. ошибки проверки сертификата), **ssl.CertificateError**. **Граничные случаи:** для самоподписанного сертификата на сервере клиент может использовать **context.check_hostname = False** и **context.verify_mode = ssl.CERT_NONE** (только в тестах/внутренней сети).

**Пример ssl (HTTPS-клиент через сокет)**

```python
import socket, ssl
ctx = ssl.create_default_context()
with socket.create_connection(("example.com", 443)) as sock:
    with ctx.wrap_socket(sock, server_hostname="example.com") as ssock:
        ssock.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        print(ssock.recv(1024).decode()[:200])
```

**ftplib, smtplib, poplib, imaplib — протоколы прикладного уровня**

- [ ] **ftplib** — **FTP-клиент**: **ftplib.FTP(host='', user='', passwd='', acct='')** — подключение (если **host** пустой, потом **.connect(host, port)**); **.login(user, passwd)** — аутентификация. **.nlst(path='')** — список имён в каталоге (строка); **.dir(path='')** — подробный список (как **ls -l**). **.retrbinary(cmd, callback, blocksize=8192)** — скачать; **cmd** — строка типа **'RETR filename'**; **callback** вызывается с блоками bytes. **.storbinary(cmd, fp, blocksize=8192)** — загрузить; **cmd** — **'STOR filename'**; **fp** — файлоподобный объект. **.cwd(path)** — сменить каталог; **.pwd()** — текущий каталог; **.quit()** — закрыть. **Граничные случаи:** FTP передаёт пароль в открытом виде; для безопасной передачи использовать **FTP_TLS** и **.prot_p()** после подключения. **Применения:** автоматизация загрузки на FTP-серверы, бэкапы по FTP.

**Пример ftplib**

```python
import ftplib
with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("user", "password")
    ftp.cwd("/pub")
    names = ftp.nlst()
    with open("local.txt", "wb") as f:
        ftp.retrbinary("RETR remote.txt", f.write)
```

- [ ] **smtplib** — **SMTP-клиент** (отправка почты): **smtplib.SMTP(host, port=25)** или **SMTP_SSL(host, port=465)** для сразу TLS. **.connect(host, port)** — если не указано в конструкторе. **.ehlo()** — приветствие (вызывается автоматически при **login**). **.starttls(context=...)** — перевести соединение на TLS (после **connect** для порта 25/587). **.login(user, password)** — аутентификация (для Gmail — пароль приложения). **.sendmail(from_addr, to_addrs, msg)** — отправить; **to_addrs** — список строк; **msg** — строка или bytes (заголовки + пустая строка + тело; формировать через **email.mime**). **.quit()** — закрыть. **Граничные случаи:** **msg** должен содержать заголовки **From**, **To**, **Subject** и т.д.; для кириллицы в темах — **email.header.Header** или **email.generator** с правильной кодировкой. **Применения:** отправка писем из скриптов, уведомления, рассылки.

**Пример smtplib**

```python
import smtplib
from email.mime.text import MIMEText
msg = MIMEText("Body text")
msg["Subject"] = "Subject"
msg["From"] = "me@example.com"
msg["To"] = "you@example.com"
with smtplib.SMTP("localhost", 25) as smtp:
    smtp.sendmail("me@example.com", ["you@example.com"], msg.as_string())
# С TLS на порту 587:
# smtp = smtplib.SMTP("smtp.gmail.com", 587); smtp.starttls(); smtp.login(user, app_password)
```

- [ ] **poplib** — **POP3-клиент** (получение почты): **poplib.POP3(host, port=110)** или **POP3_SSL(host, port=995)** для TLS. **.user(username)** — отправить имя пользователя; **.pass\_(password)** — пароль (подчёркивание из-за конфликта с **pass**). **.stat()** — кортеж **(message_count, mailbox_size)**; **.list()** — список **(response, [b'1 1234', ...])** — номер и размер каждого письма; **.retr(n)** — получить письмо номер **n** (возвращает **(response, [lines])** — строки письма в байтах); **.dele(n)** — пометить письмо к удалению (удаляется при **quit**); **.quit()** — закрыть. **Граничные случаи:** POP3 не поддерживает папки — один ящик; для TLS использовать **POP3_SSL** или **stls()** после подключения. **Применения:** скрипты обработки входящей почты, бэкап писем.

**Пример poplib**

```python
import poplib
with poplib.POP3_SSL("pop.example.com", 995) as pop:
    pop.user("user@example.com")
    pop.pass_("password")
    num, total = pop.stat()
    for i in range(1, min(num, 6) + 1):
        resp, lines, _ = pop.retr(i)
        msg = b"\n".join(lines)
        # разбор через email.message_from_bytes(msg)
```

- [ ] **imaplib** — **IMAP4-клиент** (почтовые ящики, папки, поиск): **imaplib.IMAP4(host, port=143)** или **IMAP4_SSL(host, port=993)**. **.login(user, password)** — аутентификация. **.list(directory='""', pattern='\*')** — список почтовых ящиков (папок); **.select(mailbox='INBOX', readonly=False)** — выбрать ящик; **.search(charset, criterion)** — поиск (критерий **'ALL'**, **'UNSEEN'**, **'FROM "user"'** и т.д.); возвращает **(status, [b'1 2 3 ...'])** — номера писем. **.fetch(message_set, '(RFC822)')** — получить письма (тело в формате RFC822); **.store(message_set, '+FLAGS', '\\Seen')** — пометить прочитанным; **.close()** — закрыть текущий ящик; **.logout()** — выйти. **Граничные случаи:** номера писем — строки (**'1'**, **'2:5'**); для Gmail нужен пароль приложения при включённой 2FA. **Применения:** доступ к почте по IMAP (Gmail, корпоративная почта), автоматическая сортировка, фильтры.

**Пример imaplib**

```python
import imaplib
with imaplib.IMAP4_SSL("imap.example.com", 993) as imap:
    imap.login("user@example.com", "password")
    imap.select("INBOX")
    status, data = imap.search(None, "UNSEEN")
    for num in data[0].split():
        status, msg_data = imap.fetch(num, "(RFC822)")
        # msg_data — [(b'1 (RFC822 {size}', b'...'), ...]
        # разбор: email.message_from_bytes(msg_data[0][1])
    imap.close()
imap.logout()
```

### importlib, pkgutil, runpy, modulefinder

**importlib — программный импорт и интроспекция**

- [ ] **Что такое и зачем:** **importlib** предоставляет **программный** доступ к механизму импорта: загрузка модуля по имени строки, построение spec из пути к файлу, доступ к файлам внутри пакета, метаданные установленных пакетов. **Применения:** плагины (загрузка модуля по имени из конфига), динамический импорт из нестандартных путей (**spec_from_file_location**), доступ к ресурсам пакета без ****file**** (**importlib.resources**), получение версии пакета и entry points (**importlib.metadata**).
- [ ] **importlib.import_module(name, package=None)** — импортировать модуль по имени строки; **name** — полное имя модуля (например **'mypkg.submod'**); **package** — пакет для относительного импорта (например **'mypkg'** для **'.submod'**). Возвращает объект модуля. **importlib.util.spec_from_file_location(name, location)** — создать **ModuleSpec** из пути к файлу; затем **util.module_from_spec(spec)** и **spec.loader.exec_module(module)** — выполнить модуль в созданном объекте. Удобно для загрузки конфига как модуля или скрипта по пути.
- [ ] **importlib.resources** (3.9+; в 3.7–3.8 **importlib_resources** как backport): **files(package)** — трассируемый объект к файлам пакета (каталог пакета); **as_file(path)** — контекстный менеджер, дающий временный путь к файлу/каталогу на диске. **read_text(package, resource, encoding=...)** — прочитать текстовый файл из пакета; **read_binary** — бинарный. Применение: доступ к шаблонам, данным, иконкам внутри пакета без зависимости от ****file**** и упаковки (zip-импорт).
- [ ] **importlib.metadata** (3.8+): **version(distribution_name)** — версия установленного пакета (например **version('pip')**). **requires(distribution_name)** — список строк зависимостей пакета (Requires-Dist из метаданных). **entry_points(group=None)** — entry points (плагины, консольные скрипты); **group** — например **'console_scripts'** или **'myapp.plugins'**. Возвращает объекты **EntryPoint** с **.name**, **.value**, **.load()**. **metadata('pip')** — объект метаданных пакета (имя, версия, **.get('Requires-Dist')** и т.д.).

**Пример importlib**

```python
import importlib
# Импорт по имени строки (плагины, конфиг)
mod = importlib.import_module("json")
mod = importlib.import_module(".utils", package="mypkg")  # относительный
# Загрузка модуля из файла по пути
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location("config", "/path/to/config.py")
mod = module_from_spec(spec)
spec.loader.exec_module(mod)
# Ресурсы пакета (3.9+)
from importlib.resources import files, as_file
pkg_files = files("mypkg")
text = (pkg_files / "templates" / "base.html").read_text(encoding="utf-8")
# Метаданные (3.8+)
from importlib.metadata import version, entry_points
version("pip")  # '24.0'
for ep in entry_points(group="console_scripts"):
    print(ep.name, ep.value)
```

**pkgutil — утилиты для пакетов**

- [ ] **pkgutil.iter_modules(path=None, prefix='')** — итератор по **модулям** в каталогах из **path** (по умолчанию **sys.path**); каждый элемент — **(finder, name, ispkg)**. **path** может быть список каталогов или ****path**** пакета. **pkgutil.walk_packages(path=None, prefix='', onerror=None)** — рекурсивный обход всех подмодулей и подпакетов по **path**; **onerror** — callable при ошибке импорта (например логирование). **Применения:** автоподключение плагинов (импорт всех модулей в пакете **plugins**), список доступных модулей пакета, построение дерева пакета.
- [ ] **pkgutil.get_data(package, resource)** — прочитать **ресурс** (файл) из пакета как bytes; **package** — имя пакета (строка), **resource** — путь относительно пакета (например **'templates/index.html'**). Работает и при упаковке в zip. В новом коде предпочтительнее **importlib.resources**. **Граничные случаи:** **iter_modules** не загружает модули, только перечисляет имена; для загрузки нужен **importlib.import_module(name)**.

**Пример pkgutil**

```python
import pkgutil
import myapp.plugins as plugins_pkg
for finder, name, ispkg in pkgutil.iter_modules(plugins_pkg.__path__, plugins_pkg.__name__ + "."):
    mod = __import__(name, fromlist=[""])
    if hasattr(mod, "register"):
        mod.register()
# Рекурсивный обход пакета
for imp, name, ispkg in pkgutil.walk_packages(plugins_pkg.__path__, prefix=plugins_pkg.__name__ + "."):
    print(name, "package" if ispkg else "module")
```

**runpy — запуск модуля/пути как скрипта**

- [ ] **runpy.run_path(path_name, init_globals=None, run_name=None)** — выполнить код по **пути к файлу** (строка или pathlike). Устанавливает ****name**** в **run_name** (по умолчанию **'**main**'**), ****file**** в путь, добавляет каталог файла в **sys.path**[0]. **init_globals** — начальный глобальный словарь (например **{'config': my_config}**); если передан, в нём должны быть ****name****, ****file**** и т.д. при необходимости. Возвращает итоговый глобальный словарь после выполнения. **Применения:** замена **execfile** в Py3, запуск скрипта из другого процесса с подменой контекста.
- [ ] **runpy.run_module(mod_name, init_globals=None, run_name=None, alter_sys=False)** — выполнить модуль по имени (например **'http.server'**) как ****main****; **alter_sys=True** подменяет **sys.argv[0]** и **sys.path**[0] (как при **python -m mod_name**). **alter_sys=False** — не менять **sys** (модуль выполняется в текущем окружении). **Граничные случаи:** при исключении в выполняемом коде оно пробрасывается наверх; **run_path** читает файл с диска — путь должен существовать.

**Пример runpy**

```python
import runpy
# Выполнить script.py как __main__
globs = runpy.run_path("script.py")
print(globs.get("result"))

# Выполнить модуль как python -m http.server
runpy.run_module("http.server", run_name="__main__", alter_sys=True)
# С подменой контекста
runpy.run_path("config_loader.py", init_globals={"config_file": "prod.ini"})
```

**modulefinder — зависимости модуля**

- [ ] **modulefinder.ModuleFinder(path=None)** — анализ кода для определения **какие модули** импортируются (прямо и косвенно). **path** — список каталогов для поиска (аналог **sys.path**). **.run_script(path)** — выполнить скрипт по пути и собрать зависимости (код реально выполняется в изолированном окружении). **.load_module(name)** — загрузить модуль по имени. Атрибуты: **modules** — dict (имя → объект **Module** с **.**file****, **.**code**** и т.д.); **badmodules** — множество имён модулей, которые не удалось найти; **report()** — вывести отчёт о модулях и отсутствующих. **Граничные случаи:** динамический импорт (**importlib.import_module** по строке) не учитывается; **run_script** выполняет скрипт — не подходит для недоверенного кода. **Применения:** упаковка приложения (включить только нужные модули), аудит зависимостей скрипта.

**Пример modulefinder**

```python
from modulefinder import ModuleFinder
finder = ModuleFinder()
finder.run_script("myscript.py")
print("Loaded:", list(finder.modules.keys()))
print("Missing:", list(finder.badmodules))
finder.report()  # текстовый отчёт
```

### inspect, pdb, trace, tracemalloc, timeit, cProfile, profile, pstats

**inspect — интроспекция объектов**

- [ ] **Что такое и зачем:** **inspect** позволяет **изучать** объекты во время выполнения: сигнатуры функций и методов, исходный код, стек вызовов, иерархию классов. **Применения:** фреймворки (валидация аргументов по сигнатуре), документация (извлечение сигнатур), отладка (стек, источник), декораторы и обёртки (получение параметров функции).
- [ ] **Сигнатуры:** **inspect.signature(func)** — объект **Signature** с **.parameters** (dict имён → **Parameter**: **name**, **default**, **annotation**, **kind** — POSITIONAL_ONLY, KEYWORD_ONLY, VAR_POSITIONAL, VAR_KEYWORD). **Parameter.kind** — способ передачи аргумента. **signature.bind(\*args, **kwargs)** — привязать аргументы к параметрам; **bind_partial\*\* — частичная привязка.
- [ ] **Исходный код и объекты:** **inspect.getsource(obj)** — исходный код функции/класса/модуля (строка); **getfile(obj)** — путь к файлу; **getsourcelines(obj)** — список строк с номерами. **getmro(cls)** — порядок разрешения методов (MRO). **getmembers(obj)** — все атрибуты объекта (имя, значение); фильтр по предикату (например **inspect.isfunction**).
- [ ] **Стек вызовов:** **inspect.stack()** — список кадров текущего стека; каждый элемент — **FrameInfo** (frame, filename, lineno, function, code_context, index). **inspect.currentframe()** — текущий кадр. **inspect.getframeinfo(frame)** — информация о кадре. Применение: логирование контекста вызова, отладка.

**Пример inspect**

```python
import inspect
def foo(a, b=10, *args, **kwargs):
    pass
sig = inspect.signature(foo)
for name, param in sig.parameters.items():
    print(name, param.default, param.kind)
# a <Parameter.empty> POSITIONAL_OR_KEYWORD
# b 10 POSITIONAL_OR_KEYWORD
# args POSITIONAL_VARARG
# kwargs KEYWORD_VARARG
bound = sig.bind(1, 2, 3, x=4)
bound.arguments  # {'a': 1, 'b': 2, 'args': (3,), 'kwargs': {'x': 4}}
# Исходный код и файл
print(inspect.getfile(foo))
print(inspect.getsource(foo))
# Стек вызовов
def log_caller():
    for fi in inspect.stack()[1:3]:
        print(fi.filename, fi.lineno, fi.function)
```

**pdb — отладчик**

- [ ] **Что такое и зачем:** **pdb** — интерактивный **отладчик** в консоли: пошаговое выполнение, точки останова, просмотр переменных и стека. **Применения:** отладка падений, пошаговый разбор логики, проверка значений в цикле или рекурсии.
- [ ] **Запуск:** **pdb.set_trace()** — остановить выполнение в этой точке и войти в отладчик (в 3.7+ предпочтительнее **breakpoint()**). **python -m pdb script.py** — запустить скрипт под отладчиком. **pdb.run(expr)**, **pdb.runcall(func, \*args)** — выполнить выражение или вызов под отладчиком.
- [ ] **Команды (кратко):** **n** (next) — следующая строка; **s** (step) — войти в вызов; **c** (continue) — продолжить до следующей точки останова; **b** (break) — установить точку останова; **p expr** — вывести выражение; **pp expr** — pretty-print; **l** (list) — показать код вокруг текущей строки; **w** (where) — стек вызовов; **q** — выход.

**Пример pdb**

```python
# В коде: остановка и вход в отладчик
import pdb
def buggy(x):
    y = x + 1
    pdb.set_trace()  # или breakpoint() в 3.7+
    return y * 2
# buggy(5) — выполнение остановится; в консоли:
# (Pdb) p x, y    — вывести переменные
# (Pdb) n         — следующая строка
# (Pdb) s         — войти в вызов функции
# (Pdb) w         — стек вызовов
# (Pdb) l         — код вокруг текущей строки
# (Pdb) b 10      — точка останова на строке 10
# (Pdb) c         — продолжить до следующего break
# (Pdb) q         — выход
# Запуск скрипта под отладчиком: python -m pdb script.py
```

**trace — трассировка выполнения**

- [ ] **trace** — модуль для **трассировки** выполнения: какие строки выполнялись, какие функции вызывались. **trace.Trace(count=1, trace=1, countfuncs=1, countcallers=1)** — создать объект: **count** — считать выполнение строк; **trace** — печатать каждую выполняемую строку; **countfuncs** — считать вызовы функций; **countcallers** — считать, кто кого вызвал. **.run(cmd)** — выполнить строку **cmd** как код (например **"import mymodule; mymodule.main()"**); **.runfunc(func, \*args, **kwargs)** — выполнить **func(\*args, **kwargs)**. После выполнения: **.results** — объект с собранной статистикой; **.results.write_results(coverdir=..., show_missing=...)** — записать отчёт покрытия (в т.ч. для **coverage.py**-совместимого вывода). **Граничные случаи:** трассировка замедляет выполнение; для больших программ лучше ограничить **count**/ **trace** или использовать **coverage.py**. **Применения:** покрытие кода (coverage), анализ вызовов, отладка «что реально выполнилось».

**Пример trace**

```python
import trace
t = trace.Trace(count=1, trace=0, countfuncs=1)
t.runfunc(my_function, arg1, arg2)
# Результаты в t.results; для отчёта по файлам:
# t.results.write_results(coverdir="covdir", show_missing=True)
```

**tracemalloc — трассировка аллокаций памяти**

- [ ] **tracemalloc** (3.4+): **tracemalloc.start(nframe=1)** — начать отслеживание выделений памяти; **nframe** — глубина стека для каждой аллокации (больше — точнее, но больше памяти). **tracemalloc.stop()** — остановить. **get_traced_memory()** — кортеж **(current, peak)** в байтах (текущий размер трассируемой памяти и пик). **get_object_traceback(obj)** — **Traceback** или **None**: где был выделен объект (файл, строка). **take_snapshot()** — снимок текущих аллокаций (**Snapshot**); **Snapshot.compare_to(old_snapshot)** — **StatisticDiff** по блокам (разница по размеру/количеству). **Snapshot.statistics("lineno")** или **"filename"** — топ аллокаций по строке или файлу. **Граничные случаи:** **start()** нужно вызвать как можно раньше (до основных аллокаций); на производительность трассировка влияет заметно. **Применения:** поиск утечек памяти, анализ роста памяти.

**Пример tracemalloc**

```python
import tracemalloc
tracemalloc.start()
# ... код, после которого смотрим снимок
snap1 = tracemalloc.take_snapshot()
# ... ещё код
snap2 = tracemalloc.take_snapshot()
top = snap2.compare_to(snap1, "lineno")[:5]
for stat in top:
    print(stat)
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024:.1f} KiB, Peak: {peak / 1024:.1f} KiB")
```

**timeit — замер времени выполнения**

- [ ] **timeit** — точный **замер времени** выполнения небольшого фрагмента кода (многократный прогон, усреднение). **timeit.timeit(stmt='pass', setup='pass', number=1000000, globals=...)** — выполнить **stmt** **number** раз и вернуть общее время в секундах; **setup** выполняется один раз перед серией; **globals** — словарь глобальных переменных (чтобы **stmt** видел объекты из текущего модуля). **timeit.repeat(stmt, setup, repeat=3, number=...)** — несколько серий замеров; возвращает список времён (обычно берут **min(repeat(...))** как лучший результат). **timeit.Timer(stmt, setup, globals=...)** — объект; **.timeit(number=...)**; **.autorange()** — подобрать **number** автоматически (возвращает **(number, time)**). Командная строка: **python -m timeit -s "setup" "stmt"**. **Граничные случаи:** для коротких операций **number** должен быть большим; **stmt**/ **setup** — строки кода, поэтому кавычки внутри экранировать или использовать точку с запятой. **Применения:** сравнение производительности двух вариантов кода, бенчмарки.

**Пример timeit**

```python
import timeit
# Строки кода (или многострочные с \n)
t = timeit.timeit("x = sum(range(100))", number=10000)
print(t)
# С глобальными переменными (из текущего модуля)
t = timeit.timeit("f(10)", setup="from __main__ import f", number=100000)
# Несколько прогонов, взять минимум
times = timeit.repeat("x = 2**64", number=100000, repeat=5)
print(min(times))
# Командная строка: python -m timeit -s "a=1" "a+1"
```

**cProfile и profile — профилировщики**

- [ ] **cProfile** (C-расширение, меньше накладных): **cProfile.run(statement, filename=None, sort='cumulative')** — выполнить **statement** (строка кода) и собрать статистику вызовов; **filename** — сохранить в файл (для последующего разбора **pstats**); **sort** — ключ сортировки при выводе. **cProfile.Profile()** — объект профилировщика; **.enable()** — начать сбор; **.disable()** — остановить; **.print_stats(sort='cumulative', limit=20)** — вывести отчёт. Вывод: **ncalls** (число вызовов; **1/2** — 1 прямой, 2 рекурсивных), **tottime** (время в функции без подвызовов), **cumtime** (с подвызовами), **percall** (время на вызов). **Применения:** поиск «узких мест» в коде (какие функции занимают больше всего времени). **profile** — чистая Python-реализация; API совместим с **cProfile**, но медленнее и искажает замеры. **Граничные случаи:** профилирование замедляет выполнение; для многопоточного кода статистика может быть неточной.

**Пример cProfile**

```python
import cProfile
cProfile.run("sum(range(10**6))", sort="cumulative")
# В файл для разбора
cProfile.run("my_main()", filename="out.prof", sort="tottime")
# Программно
pr = cProfile.Profile()
pr.enable()
my_main()
pr.disable()
pr.print_stats(sort="cumulative", limit=15)
```

**pstats — анализ результатов профилирования**

- [ ] **pstats.Stats(filename)** — загрузить результат профилирования из файла (передать **filename** в **cProfile.run(..., filename='out.prof')**). **.strip_dirs()** — убрать пути из имён (короче вывод). **.sort_stats('cumulative')** или **'tottime'**, **'calls'**, **'name'** — сортировка; **.print_stats(n)** — вывести топ **n** строк (None — все); **.print_callers(\*restrictions)** — кто вызывал данные функции; **.print_callees(\*restrictions)** — кого вызывали данные функции. **restrictions** — фильтр по имени/пути (регулярные выражения или подстроки). **Применения:** интерактивный разбор дампа профилирования, поиск вызывающих узкое место.

**Пример pstats**

```python
import pstats
from pstats import SortKey
p = pstats.Stats("out.prof")
p.strip_dirs()
p.sort_stats(SortKey.CUMULATIVE)
p.print_stats(20)
p.print_callers("my_slow_func")
```

### io, select, selectors, mmap

**io — потоки и буферы в памяти**

- [ ] **Что такое и зачем:** модуль **io** предоставляет **потоки ввода-вывода** (иерархия классов) и **буферы в памяти**, ведущие себя как файлы. **Применения:** тесты (подмена файла без диска), накопление текста/байт в памяти, сериализация в память, понимание иерархии **open()**.
- [ ] **StringIO:** **io.StringIO(initial_value='', newline='\\n')** — строковый буфер в памяти. Методы: **.write(s)** — записать строку; **.read(n)** / **.read()** — прочитать n символов или до конца; **.readline()**, **.readlines()**; **.getvalue()** — вернуть всё содержимое как строку; **.seek(0)** — вернуться в начало; **.truncate(0)** — очистить (размер 0). Режим только текст; кодировка при создании не задаётся (всегда Unicode). **Применения:** тесты (передать StringIO вместо файла), построение длинной строки по частям.
- [ ] **BytesIO:** **io.BytesIO(initial_bytes=b'')** — буфер байт в памяти. **.write(b)** — записать bytes; **.read(n)** / **.read()**; **.getvalue()** — все байты; **.getbuffer()** — **memoryview** на буфер (без копирования, изменяемый). **.seek(0)**; **.truncate(0)**. **Применения:** тесты бинарных протоколов, сериализация (pickle, zip) в память, передача данных по API без файла.
- [ ] **Иерархия потоков:** **io.RawIOBase** — низкоуровневый (чтение/запись байт); **io.BufferedIOBase** — буферизованный (уменьшение системных вызовов); **io.TextIOBase** — текстовый (строки, кодировка). **open()** в режиме **'r'**/ **'w'** возвращает **TextIOWrapper** (текст + буфер + файл); в **'rb'**/ **'wb'** — **BufferedReader**/ **BufferedWriter**. **io.open** — алиас **open**; в Py3 **open** в текстовом режиме всегда с **encoding** (по умолчанию из локали). **BufferedIOBase.readinto(buffer)** — zero-copy чтение в заранее выделенный буфер (bytes-like). **Граничные случаи:** после **getvalue()** позиция не сбрасывается — для повторного чтения вызвать **seek(0)**; **StringIO** не поддерживает **encoding** — только Unicode-строки.

**Пример io (StringIO, BytesIO)**

```python
import io
# Текстовый буфер — тест функции, читающей из файла
buf = io.StringIO("line1\nline2\n")
def read_lines(f):
    return f.readlines()
assert read_lines(buf) == ["line1\n", "line2\n"]
buf.seek(0)
assert buf.read() == "line1\nline2\n"

# Бинарный буфер — pickle в память
import pickle
bio = io.BytesIO()
pickle.dump({"a": 1}, bio)
bio.seek(0)
obj = pickle.load(bio)
# getbuffer — без копирования
mv = bio.getbuffer()
```

**select и selectors — мультиплексирование I/O**

- [ ] **select** (Unix): **select.select(rlist, wlist, xlist[, timeout])** — ждать, пока хотя бы один из файловых объектов (сокетов, pipe) станет готов к чтению (**rlist**), записи (**wlist**) или «исключению» (**xlist**). Возвращает три списка готовых объектов. **timeout** — таймаут в секундах (None — бесконечно; 0 — не блокировать). **Применения:** серверы с несколькими сокетами без потоков (один поток обслуживает много соединений). **select.poll()** — альтернативный API на части платформ (масштабируется лучше при большом числе дескрипторов). **Граничные случаи:** на Windows **select** работает только с сокетами; максимальное число дескрипторов ограничено (обычно 512–1024); при большом числе соединений предпочтительнее **selectors** или **asyncio**.
- [ ] **selectors** — высокоуровневая обёртка над **select**/ **poll**/ **epoll** (кроссплатформенно). **selectors.DefaultSelector()** — выбрать лучший доступный механизм (на Linux — **epoll**, на Windows — **select**). **.register(fileobj, events, data=None)** — зарегистрировать объект на события **selectors.EVENT_READ**, **EVENT_WRITE** (или побитовое объединение); **data** — произвольный объект (возвращается в **key.data**). **.unregister(fileobj)**; **.modify(fileobj, events, data=None)** — изменить события. **.select(timeout=None)** — ждать событий; возвращает список **(key, events)**; **key** — **SelectorKey** (fileobj, fd, events, data). **.close()** — освободить ресурсы. **Применения:** асинхронные серверы, event loop без asyncio.

**Пример selectors**

```python
import selectors
import socket
sel = selectors.DefaultSelector()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 9998))
sock.listen(5)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, data=None)
while True:
    events = sel.select(timeout=1.0)
    for key, mask in events:
        if key.data is None:
            conn, addr = key.fileobj.accept()
            conn.setblocking(False)
            sel.register(conn, selectors.EVENT_READ, data=addr)
        else:
            data = key.fileobj.recv(1024)
            if not data:
                sel.unregister(key.fileobj)
                key.fileobj.close()
            else:
                key.fileobj.send(data)
```

**mmap — отображение файла в память**

- [ ] **Что такое и зачем:** **mmap** отображает **файл** (или анонимную область) в адресное пространство процесса: доступ к данным через срезы **mv[i:j]** как к bytes без явного read/write; изменения (при **ACCESS_WRITE**) записываются в файл. **Применения:** случайный доступ к большим файлам без загрузки целиком, общая память между процессами (shared memory), быстрый доступ к данным по смещению.
- [ ] **API:** **mmap.mmap(fileno, length, access=mmap.ACCESS_WRITE, ...)** — отобразить **length** байт файла с дескриптором **fileno**; **access**: **ACCESS_READ** (только чтение), **ACCESS_WRITE** (чтение/запись), **ACCESS_COPY** (копия при записи). **mv[i:j]** — срез bytes; **mv[i:j] = b'...'** — запись (при ACCESS_WRITE). **.seek(pos)**; **.read(n)**; **.flush()** — сбросить на диск. **.close()** — отменить отображение.

### ipaddress

**ipaddress — адреса и сети IPv4/IPv6**

- [ ] **Что такое и зачем:** модуль **ipaddress** предоставляет типы для представления **IPv4-** и **IPv6-**адресов и **подсетей** (сеть + маска). Поддерживаются проверка вхождения адреса в сеть, итерация по хостам, арифметика адресов, обращение в строку и из строки. **Применения:** валидация ввода (IP, CIDR), проверка доступа по белому/чёрному списку подсетей, конфигурация сетевых интерфейсов, парсинг логов и конфигов.
- [ ] **Типы:** **ipaddress.ip_address(address)** — один адрес (**IPv4Address** или **IPv6Address**); **address** — строка (**'192.168.1.1'**) или целое. **ipaddress.ip_network(address, strict=True)** — сеть (**IPv4Network** или **IPv6Network**); **address** — строка в формате CIDR (**'192.168.0.0/24'**); **strict=True** — хостовые биты должны быть нулевыми. **ipaddress.interface_address** — адрес с маской (хост в сети).
- [ ] **Операции:** **addr in network** — входит ли адрес в сеть. **network.netmask**, **network.hostmask**, **network.num_addresses** — маска, инвертированная маска, число адресов. **network.hosts()** — итератор по пригодным хостовым адресам (исключая сеть и broadcast где применимо). **addr + n**, **addr - n** — сдвиг адреса. **network1.overlaps(network2)** — пересекаются ли сети. **IPv4Address** и **IPv6Address** сравнимы, приводимы к **int** (для сортировки и хранения). **Граничные случаи:** **ip_network('192.168.1.0/24', strict=False)** допускает ненулевые хостовые биты (адрес нормализуется к сети); **ip_address** принимает строку или int; для валидации ввода ловить **ValueError**.

**Пример ipaddress**

```python
import ipaddress
addr = ipaddress.ip_address("192.168.1.1")
net = ipaddress.ip_network("192.168.0.0/24")
print(addr in net)           # True
print(net.num_addresses)     # 256
for host in list(net.hosts())[:3]:
    print(host)
# Валидация ввода
try:
    ipaddress.ip_address(user_input)
except ValueError:
    print("Invalid IP")
# Белый список подсетей
allowed = [ipaddress.ip_network(cidr) for cidr in ["10.0.0.0/8", "172.16.0.0/12"]]
if any(ipaddress.ip_address(client_ip) in n for n in allowed):
    allow_access()
```

### itertools

**Что такое и зачем**

- [ ] **itertools** — **итераторы** для комбинаторики, слияния, фильтрации и циклов без создания списков в памяти. **chain** — объединить несколько итераторов в один; **tee** — разветвить один итератор на несколько; **cycle**, **repeat** — бесконечные повторы; **islice**, **takewhile**, **dropwhile** — срезы и фильтрация по условию; **groupby** — группировка подряд идущих по ключу (перед **groupby** обычно нужна **сортировка**); **zip_longest** — zip до самой длинной последовательности; **permutations**, **combinations**, **product** — перестановки, сочетания, декартово произведение; **accumulate**, **pairwise** — накопление и пары подряд идущих. **Применения:** ленивая обработка больших данных, комбинаторика, группировка потоков, разветвление без копирования. См. также §13 для углублённого разбора.
- [ ] **Бесконечные:** **cycle(iterable)** — повтор цикла; **repeat(x, times=None)** — повтор **x**. **Цепочки:** **chain(\*iterables)** — объединить итераторы; **chain.from_iterable(iterable)** — из вложенных. **Выборка:** **islice(iterable, start, stop, step)** — срез; **takewhile(pred, iterable)**; **dropwhile(pred, iterable)**. **Группировка:** **groupby(iterable, key=None)** — подряд идущие группы по **key** (требуется предварительная сортировка по тому же key). **Комбинаторика:** **permutations(iterable, r)**; **combinations(iterable, r)**; **product(\*iterables)**. **Накопление:** **accumulate(iterable, func=operator.add)**; **pairwise(iterable)** (3.10+). **Прочее:** **zip_longest**, **starmap**, **compress**, **filterfalse**.

**Пример itertools**

```python
import itertools
# chain — объединить итераторы
list(itertools.chain([1, 2], [3, 4]))  # [1, 2, 3, 4]
# islice — срез без копирования
list(itertools.islice(range(10), 2, 6))  # [2, 3, 4, 5]
# cycle, repeat — бесконечные (ограничивать islice)
list(itertools.islice(itertools.cycle("AB"), 5))  # ['A', 'B', 'A', 'B', 'A']
# groupby — группировка подряд идущих (сортировка по key заранее)
data = [(1, "a"), (1, "b"), (2, "c")]
for k, g in itertools.groupby(data, key=lambda x: x[0]):
    print(k, list(g))  # 1 [(1,'a'), (1,'b')], 2 [(2,'c')]
# combinations, permutations, product
list(itertools.combinations("AB", 2))   # [('A','B')]
list(itertools.permutations("AB", 2))   # [('A','B'), ('B','A')]
list(itertools.product([1, 2], ["a", "b"]))  # [(1,'a'), (1,'b'), (2,'a'), (2,'b')]
# accumulate
list(itertools.accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10]
# zip_longest
list(itertools.zip_longest([1, 2], "ab", fillvalue="-"))  # [(1,'a'), (2,'b'), ('-','-')]
```

### logging

**Что такое и зачем**

- [ ] **logging** — встроенный **фреймворк логирования**: сообщения с уровнем (DEBUG, INFO, WARNING, ERROR, CRITICAL), вывод в консоль/файл, формат с датой и именем логгера. Иерархия логгеров по имени (точечная: **a.b** — потомок **a**). **Применения:** отладка (DEBUG), мониторинг работы (INFO), предупреждения (WARNING), ошибки (ERROR), аудит и диагностика в продакшене.
- [ ] Один раз при старте приложения: **logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')** — настраивает корневой логгер (если он ещё не сконфигурирован). В каждом модуле: **logger = logging.getLogger(**name**)** — логгер с именем модуля; затем **logger.debug()**, **logger.info()**, **logger.warning()**, **logger.error()**, **logger.exception()** (добавляет traceback текущего исключения). **getLogger()** без аргумента — корневой логгер; с именем — дочерний (наследует настройки от корня, если не заданы свои).
- [ ] **Handlers:** **StreamHandler()** — вывод в поток (по умолчанию stderr); **FileHandler(path)** — в файл; **RotatingFileHandler(path, maxBytes, backupCount)** — ротация по размеру. **Formatter(fmt)** — формат строки (**%(name)s**, **%(levelname)s**, **%(message)s**, **%(asctime)s** и др.). **logger.addHandler(h)**; **handler.setFormatter(f)**. **logging.config.dictConfig(config)** — конфигурация из словаря (из файла YAML/JSON). Для продакшена: уровень INFO или WARNING на корне, **FileHandler** с ротацией, единый формат.

**Пошагово: что происходит при logger.info("Started")**

1. **logger** — объект с именем (например ****name**** модуля); проверяется уровень логгера (если уровень выше INFO, сообщение отбрасывается).
2. Создаётся **LogRecord** (сообщение, уровень, имя логгера, время, номер строки и т.д.).
3. Запись передаётся всем **handlers** этого логгера и родительским (по иерархии имён); каждый handler проверяет свой уровень и форматирует строку через **Formatter**, затем выводит (в консоль, файл и т.д.).

**Пример**

```python
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
logger.info("Started")
logger.warning("Deprecated API")
logger.error("Failed", exc_info=True)
```

### subprocess — запуск внешних команд

**Что такое и зачем**

- [ ] **subprocess** — **запуск внешних программ** и взаимодействие с ними: передача аргументов, перехват stdout/stderr, отправка данных в stdin, таймауты, проверка кода возврата. **Применения:** вызов системных утилит (grep, tar, git), скрипты сборки, оркестрация процессов, автоматизация CLI-инструментов.
- [ ] **subprocess.run(args, capture_output=False, text=False, timeout=None, check=False, cwd=None, env=None, ...)** — **рекомендуемый** высокоуровневый вызов: запускает процесс, ждёт завершения, возвращает **CompletedProcess**. **args** — список аргументов (предпочтительно, **без shell**) или строка при **shell=True**. **capture_output=True** — перехватить stdout и stderr (иначе наследуются от родителя). **text=True** — stdout/stderr как **str** (иначе **bytes**). **timeout=N** — прервать через N секунд (**TimeoutExpired**). **check=True** — при ненулевом **returncode** выбросить **CalledProcessError** (атрибуты **returncode**, **cmd**, **stdout**, **stderr**). **cwd** — рабочий каталог процесса; **env** — окружение (dict или None — наследовать).
- [ ] **subprocess.Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, ...)** — низкоуровневый: процесс **запускается сразу**; возвращается объект **Popen**. **.communicate(input=None)** — отправить **input** в stdin, дождаться завершения, вернуть **(stdout_data, stderr_data)**. **.wait(timeout)** — только ждать. **.returncode** — код возврата (None пока не завершён). Нужен при пайпах между процессами или потоковом чтении вывода.
- [ ] **shell=True:** команда выполняется через **/bin/sh** (Unix) или **cmd.exe** (Windows). Позволяет пайпы и перенаправления в строке, но при подстановке пользовательского ввода возможна **инъекция команд**. Предпочитать **shell=False** и **list** аргументов; для пайпов — несколько **Popen** и связывание потоков вручную.
- [ ] **Граничные случаи:** при **capture_output=True** большой вывод может заполнить pipe (deadlock при переполнении); для потокового чтения использовать **Popen** и читать из **process.stdout**. На Windows **args** при **shell=False** должен быть список; путь к исполняемому файлу с пробелами — элемент списка в кавычках не нужен (передаётся как один аргумент).

**Пример**

```python
import subprocess
r = subprocess.run(["ls", "-la"], capture_output=True, text=True)
print(r.stdout)
r = subprocess.run(["false"], check=True)  # CalledProcessError
```

### tempfile, hashlib, secrets

**tempfile — временные файлы и каталоги**

**Что такое и зачем**

- [ ] **tempfile** — **безопасное** создание временных файлов и каталогов с уникальными именами в системной директории (**/tmp** или аналог). Файлы не конфликтуют с другими процессами; при выходе из контекстного менеджера можно автоматически удалить. **Применения:** промежуточные данные при обработке, кеш, загрузки (сохранить во временный файл и обработать), тесты.
- [ ] **tempfile.TemporaryFile(mode='w+b', ...)** — временный файл, **удаляется при закрытии**; не имеет имени в ФС (на Unix — unlink сразу после создания). **NamedTemporaryFile(delete=True, ...)** — временный файл с именем (**.name** — путь); при **delete=True** удаляется при закрытии. **TemporaryDirectory()** — временный каталог; при выходе из **with** каталог и содержимое удаляются. **tempfile.mkstemp(suffix='', prefix='tmp', dir=None)** — возвращает **(fd, path)**; файл нужно закрыть и при необходимости удалить вручную. **tempfile.mkdtemp()** — путь к новому временному каталогу; удаление вручную. **tempfile.gettempdir()** — каталог по умолчанию. **tempfile.gettempprefix()** — префикс имён (например **tmp**).

**Пример tempfile**

```python
import tempfile
with tempfile.TemporaryDirectory() as tmpdir:
    path = Path(tmpdir) / 'data.txt'
    path.write_text('hello')
    # обработать path
# каталог и файл удалены
```

**hashlib и secrets** — см. блок «hashlib, hmac, secrets» выше (полное описание с примерами).

### multiprocessing, threading, queue, \_thread

**multiprocessing — параллельное выполнение в процессах**

- [ ] **Что такое и зачем:** **multiprocessing** запускает код в **отдельных процессах** (отдельные интерпретаторы, отдельная память). Обход **GIL**: CPU-нагруженные задачи масштабируются по ядрам. **Применения:** параллельные вычисления (числа, обработка данных), изоляция (крах одного процесса не роняет остальные), использование нескольких ядер для одной задачи.
- [ ] **Process:** **Process(target=func, args=(...), kwargs={...})** — объект процесса; **.start()** — запустить; **.join(timeout)** — дождаться завершения; **.is_alive()**; **.terminate()** — принудительно завершить. **multiprocessing.current_process()** — текущий процесс; **.name**, **.pid**. Передача данных между процессами — через **Queue**, **Pipe** или **Manager** (общие объекты в отдельном процессе-менеджере).
- [ ] **Pool:** **Pool(processes=N)** — пул из N рабочих процессов; **.map(func, iterable)** — применить **func** к элементам (распределение по процессам); **.apply_async(func, args)** — асинхронный вызов; **.close()**, **.join()**. Удобно для «map-reduce» по списку задач.
- [ ] **Queue, Pipe:** **multiprocessing.Queue(maxsize=0)** — потокобезопасная очередь между процессами; **.put(obj)**, **.get()**; объекты должны быть pickle-сериализуемы. **Pipe(duplex=True)** — пара **(conn1, conn2)**; **.send(obj)**, **.recv()** — канал между двумя процессами. **Manager()** — прокси к общим объектам (dict, list и т.д.) в процессе-менеджере; медленнее, но гибко.
- [ ] **Запуск:** **spawn** (по умолчанию на Windows) — новый интерпретатор; **fork** (Unix) — копирование процесса; **forkserver** — отдельный сервер-процесс для fork. **if **name** == '**main**':** обязателен при **spawn**, иначе возможна рекурсивная порча процессов. **Граничные случаи:** передаваемые в Process функции и аргументы должны быть pickle-сериализуемы; глобальные переменные в дочернем процессе — копии на момент fork/spawn.

**Пример multiprocessing**

```python
import multiprocessing
def worker(n):
    return n * n
if __name__ == "__main__":
    # Один процесс
    p = multiprocessing.Process(target=worker, args=(10,))
    p.start()
    p.join()
    # Пул
    with multiprocessing.Pool(4) as pool:
        results = pool.map(worker, range(10))
    # Очередь между процессами
    q = multiprocessing.Queue()
    def producer(q):
        q.put("data")
    p = multiprocessing.Process(target=producer, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

**threading — потоки в одном процессе**

- [ ] **Что такое и зачем:** **threading** — **потоки** в рамках одного процесса (общая память, один GIL). Подходят для I/O-задач (сеть, диск), пока один поток ждёт I/O, другие могут выполняться. **Применения:** параллельные запросы к API, фоновые задачи (логирование, обновление UI), серверы с потоком на соединение.
- [ ] **Thread:** **Thread(target=func, args=(...), kwargs={...}, daemon=False)** — объект потока; **.start()** — запустить; **.join(timeout)** — дождаться завершения; **.is_alive()**. **daemon=True** — поток не блокирует завершение процесса. **threading.current_thread()** — текущий поток; **threading.local()** — объект для thread-local хранилища (атрибуты уникальны для каждого потока).
- [ ] **Синхронизация:** **Lock()** — взаимное исключение; **.acquire()**, **.release()** или **with lock:**. **RLock()** — реентерабельная блокировка (тот же поток может захватить повторно). **Semaphore(n)** — счётчик; не более **n** потоков одновременно. **Event()** — флаг; **.set()**, **.clear()**, **.wait(timeout)** — ждать установки. **Condition(lock)** — условные переменные (ожидание условия с уведомлением). **Граничные случаи:** из-за GIL потоки не ускоряют CPU-задачи; для I/O (сеть, диск) threading даёт выигрыш.

**Пример threading**

```python
import threading
counter = 0
lock = threading.Lock()
def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
threads = [threading.Thread(target=increment) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter)  # 400000
# Thread-local данные
local = threading.local()
def f():
    local.x = threading.current_thread().name
threading.Thread(target=f).start()
```

**queue — потокобезопасные очереди (для threading)**

- [ ] **queue.Queue(maxsize=0)** — FIFO-очередь; **.put(item, block=True, timeout=None)** — при **maxsize** и полной очереди блокируется или **queue.Full**; **.get(block=True, timeout=None)** — при пустой очереди блокируется или **queue.Empty**. **.task_done()** — отметить задачу выполненной (после **get**); **.join()** — ждать, пока все задачи отмечены (для пула рабочих потоков). **queue.LifoQueue()** — LIFO. **queue.PriorityQueue()** — приоритетная (меньший элемент извлекается первым; элементы сравнимы или **(priority, item)**). **queue.SimpleQueue()** (3.7+) — упрощённая очередь без **task_done**/ **join**. **Применения:** очередь задач между потоками (producer-consumer), ограничение нагрузки.

**Пример queue (producer-consumer)**

```python
import queue
import threading
def producer(q):
    for i in range(5):
        q.put(i)
    q.put(None)  # сигнал завершения
def consumer(q):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print(item)
        q.task_done()
q = queue.Queue()
t1 = threading.Thread(target=producer, args=(q,))
t2 = threading.Thread(target=consumer, args=(q,))
t1.start()
t2.start()
q.join()
t1.join()
t2.join()
```

**\_thread — низкоуровневый API потоков**

- [ ] **Что такое и зачем:** **\_thread** — минимальный **низкоуровневый** API для создания потоков: один вызов запускает функцию в новом потоке. Нет объектов **Thread**, нет встроенных блокировок (Lock реализуют вручную через **\_thread.allocate_lock()**, **.acquire()**, **.release()**). Обычно используют **threading**, который построен поверх **\_thread** и даёт **Thread**, **Lock**, **RLock**, **Semaphore** и т.д. **Применения:** когда нужен один «фоновый» поток без зависимостей от **threading**; встраивание Python (минимальный набор); редко в прикладном коде.
- [ ] **API:** **\_thread.start_new_thread(function, args)** — запустить **function(\*args)** в новом потоке; **args** — кортеж аргументов (пустой **()** если аргументов нет). Возвращает идентификатор потока (целое). Поток завершается при возврате из **function** или при необработанном исключении (при исключении вывод в stderr и завершение потока). **\_thread.allocate_lock()** — создать объект блокировки; **.acquire(waitflag=1)** — захватить (при **waitflag=0** не блокироваться, вернуть True/False); **.release()** — освободить (вызывать только из потока, захватившего блокировку). **\_thread.exit()** — завершить текущий поток (вызов **\_thread.exit()** эквивалентен **sys.exit()** для потока). **Граничные случаи:** при падении потока из **start_new_thread** главный процесс не останавливается; координация и синхронизация — вручную через **allocate_lock** или через **threading**.

**Пример _thread**

```python
import _thread
import time
def worker(name):
    for i in range(3):
        print(f"{name} {i}")
        time.sleep(0.1)
_thread.start_new_thread(worker, ("A",))
_thread.start_new_thread(worker, ("B",))
time.sleep(0.5)  # дать потокам завершиться (иначе процесс может выйти раньше)
# С блокировкой
lock = _thread.allocate_lock()
def safe_print(msg):
    lock.acquire()
    try:
        print(msg)
    finally:
        lock.release()
_thread.start_new_thread(safe_print, ("first",))
_thread.start_new_thread(safe_print, ("second",))
time.sleep(0.1)
```

### pprint, reprlib

**pprint — «красивый» вывод структур**

- [ ] **Что такое и зачем:** **pprint** форматирует сложные структуры (dict, list, вложенные объекты) с **отступами** и **переносами строк**, чтобы вывод был читаемым. Обычный **print(d)** даёт одну длинную строку; **pprint.pprint(d)** — иерархию с отступами. **Применения:** отладка (вывод больших dict/списков), логирование конфигов и ответов API, интерактивная работа в REPL.
- [ ] **API:** **pprint.pprint(object, stream=None, indent=1, width=80, depth=None, compact=False)** — вывести объект в **stream** (по умолчанию **sys.stdout**). **width** — максимальная ширина строки; **depth** — глубина вложенности (глубже — **...**). **pprint.pformat(object, ...)** — вернуть строку без вывода. **PrettyPrinter(indent=1, width=80, ...)** — объект с настраиваемыми параметрами; **.pprint(obj)**. Рекурсивные структуры выводятся с пометкой **<Recursion on ...>**.

**Пример pprint**

```python
import pprint
d = {"a": 1, "b": [2, 3, 4], "c": {"x": "y"}}
pprint.pprint(d)
# {'a': 1,
#  'b': [2, 3, 4],
#  'c': {'x': 'y'}}
s = pprint.pformat(d, width=40)
pprint.pprint(d, depth=1)  # вложенные — ...
```

**reprlib — ограниченное repr**

- [ ] **reprlib.repr(obj)** — строковое представление объекта с **ограничением длины**: длинные списки/словари обрезаются (**[1, 2, 3, ...]**), вложенность ограничена. Используется при переполнении **repr()** (например бесконечная рекурсия или огромный список). **reprlib.aRepr** — объект с атрибутами **maxlevel** (глубина), **maxdict**, **maxlist**, **maxlong** и т.д.; настраивать при необходимости. **Применения:** переопределение ****repr**** в своих классах через **reprlib.repr(self)** для безопасности от огромного вывода.

**Пример reprlib**

```python
import reprlib
reprlib.repr(list(range(100)))
# '[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ...]'
class Big:
    def __repr__(self):
        return reprlib.repr(self.data)
```

### random

**random — псевдослучайные числа**

- [ ] **Что такое и зачем:** модуль **random** генерирует **псевдослучайные** числа по алгоритму Mersenne Twister: воспроизводимая последовательность при одном **seed**, равномерное распределение в заданных диапазонах. **Не для криптографии:** последовательность предсказуема; для паролей, токенов, соли — **secrets**. **Применения:** симуляции, игры, тесты (воспроизводимость через seed), выбор случайного элемента, перемешивание.
- [ ] **Базовые функции:** **random.random()** — float в **[0.0, 1.0)**. **random.uniform(a, b)** — float в **[a, b]**. **random.randrange(stop)** или **randrange(start, stop[, step])** — целое из range; **random.randint(a, b)** — целое от **a** до **b** включительно (эквивалент **randrange(a, b+1)**).
- [ ] **Выбор из последовательности:** **random.choice(seq)** — один случайный элемент из непустой последовательности. **random.choices(seq, weights=None, cum_weights=None, k=1)** — **k** элементов **с возвращением** (один элемент может выпасть несколько раз); **weights** — веса элементов. **random.sample(seq, k)** — **k** различных элементов **без возвращения**; **seq** может быть множество или диапазон. **random.shuffle(seq)** — перемешать последовательность **на месте** (только mutable); **random.sample(seq, len(seq))** — новый список в случайном порядке без изменения исходного.
- [ ] **Распределения:** **random.gauss(mu, sigma)** — нормальное распределение; **random.expovariate(lambd)** — экспоненциальное; **random.betavariate(alpha, beta)**; **random.gammavariate(alpha, beta)** и др. — для симуляций и статистики.
- [ ] **Воспроизводимость:** **random.seed(a=None, version=2)** — инициализировать генератор; **a** — целое или hashable; при одном **a** последовательность одинакова. **random.getstate()** — сохранить состояние; **random.setstate(state)** — восстановить (для воспроизведения или сохранения в тестах).

**Пример random**

```python
import random
random.seed(42)
random.random()           # 0.6394267984578837
random.randint(1, 10)     # целое от 1 до 10 включительно
random.choice(["a", "b", "c"])
random.choices(["a", "b"], weights=[3, 1], k=10)  # с возвращением
random.sample(range(100), 5)  # 5 уникальных чисел
lst = [1, 2, 3]
random.shuffle(lst)       # на месте
random.gauss(0, 1)        # нормальное распределение
# Воспроизводимость в тестах
random.seed(123)
state = random.getstate()
# ... позже
random.setstate(state)
```

### re — регулярные выражения (краткий обзор)

**Что такое и зачем**

- [ ] **re** — **регулярные выражения**: поиск, замена и разбиение текста по **паттернам** (шаблонам). Паттерн задаёт класс символов (**\d** — цифра, **\w** — буква/цифра/\_), повторы (**+**, **\***, **{n,m}**), позиции (**^**, **$**), группы **(...)** для извлечения частей. **Применения:** валидация (email, телефон), парсинг логов и конфигов, поиск и замена в тексте, разбиение по разделителям.
- [ ] **re.compile(pattern, flags=0)** — скомпилировать паттерн в объект **Pattern**; при многократном использовании быстрее. **re.match(pattern, string)** — совпадение **с начала** строки (или с текущей позиции при **^** в MULTILINE). **re.search(pattern, string)** — первое совпадение **в любом месте**. **re.fullmatch(pattern, string)** — совпадение **всей** строки. **re.findall(pattern, string)** — список всех совпадений (или списков групп при наличии групп). **re.finditer(pattern, string)** — итератор объектов **Match**. **re.sub(pattern, repl, string, count=0)** — заменить совпадения; **repl** — строка (с **\\1**, **\\g<name>** для групп) или функция **Match → str**. **re.subn** — то же + число замен. **re.split(pattern, string)** — разбить по паттерну.
- [ ] У **Match**: **.group()** / **.group(0)** — всё совпадение; **.group(1)** — первая группа; **.group('name')** — именованная группа; **.groups()** — кортеж групп; **.groupdict()** — dict именованных групп. **.start()**, **.end()**, **.span()** — позиции совпадения.
- [ ] **Флаги:** **re.IGNORECASE** (re.I) — без учёта регистра; **re.MULTILINE** (re.M) — **^** и **$** на границы строк; **re.DOTALL** (re.S) — **.** захватывает **\\n**; **re.VERBOSE** (re.X) — игнорировать пробелы и комментарии в паттерне. См. также §15b для углублённого разбора.

**Пример: извлечение групп и замена**

```python
import re
# Поиск с группами
m = re.search(r'(\d+)-(\d+)', 'Tel: 123-456')
if m:
    print(m.group(1), m.group(2))   # 123 456

# Замена с обратной ссылкой
re.sub(r'(\w+) (\w+)', r'\2 \1', 'John Doe')   # 'Doe John'

# Разбиение по нескольким разделителям
re.split(r'[\s,;]+', 'a, b; c  d')   # ['a', 'b', 'c', 'd']
```

### sched, shelve, sqlite3, dbm

**sched — планировщик событий**

- [ ] **Что такое и зачем:** **sched** — **очередь событий** по времени: регистрация вызова функции на заданное время или через заданный интервал; выполнение в одном потоке в порядке времени. **Применения:** отложенный запуск задач, периодические действия (без threading), симуляции по времени.
- [ ] **API:** **sched.scheduler(timefunc=time.monotonic, delayfunc=time.sleep)** — планировщик; **timefunc** — текущее время (монотонное предпочтительно); **delayfunc** — функция паузы (например **time.sleep**). **.enter(delay, priority, action, argument=(), kwargs={})** — запланировать **action(\*argument, **kwargs)** через **delay** секунд; **priority** — при равном времени (меньше — раньше); возвращает **event** (ид для **cancel**). **.enterabs(time, priority, action, ...)** — выполнить в абсолютное время **time** (по **timefunc**). **.run(blocking=True)** — обработать очередь (ждать и вызывать события); при **blocking=False** выполняет только готовые события и выходит. **.cancel(event)** — отменить событие. **.empty()** — пуста ли очередь. **Граничные случаи:** планировщик однопоточный; для периодических задач нужно в обработчике снова вызывать **.enter(...)\*\*.

**Пример sched**

```python
import sched
import time
s = sched.scheduler(time.monotonic, time.sleep)
def job(name):
    print(name, time.monotonic())
s.enter(2, 1, job, ("first",))
s.enter(1, 0, job, ("second",))  # выполнится раньше
ev = s.enter(5, 1, job, ("third",))
s.cancel(ev)  # отменили
s.run()  # блокируется, пока не выполнятся first и second
```

**shelve — персистентный dict**

- [ ] **Что такое и зачем:** **shelve** — **dict-подобное** хранилище, данные которого сохраняются на диск (через **dbm** и **pickle**). Ключи — строки; значения — любые pickle-сериализуемые объекты. **Применения:** простой кеш, конфиг, состояние приложения между запусками без полноценной БД.
- [ ] **API:** **shelve.open(filename, flag='c', protocol=None, writeback=False)** — открыть хранилище; **flag**: **'c'** (создать при отсутствии), **'r'** (только чтение), **'w'** (чтение/запись), **'n'** (новый, перезапись). **writeback=True** — кешировать изменения в памяти и сбрасывать при **sync()**/ **close()** (удобно при изменении изменяемых значений, но расход памяти). **shelf[key] = value**; **del shelf[key]**; **key in shelf**; **shelf.keys()** (итератор). **.sync()** — сбросить на диск; **.close()** — закрыть. Не потокобезопасно; для многопоточности — блокировки снаружи. **Граничные случаи:** при **writeback=False** изменение «на месте» (например **shelf['list'].append(1)**) не сохранится, пока не сделать **shelf['list'] = shelf['list']** и **sync()**; ключи должны быть строками (bytes не подходят в части реализаций).

**Пример shelve**

```python
import shelve
with shelve.open("cache.db", flag="c") as db:
    db["config"] = {"theme": "dark"}
    db["items"] = [1, 2, 3]
# При следующем открытии
with shelve.open("cache.db", flag="r") as db:
    print(db["config"])
    # Изменение списка «на месте» без writeback не сохранится:
    # db["items"].append(4)  — нужно db["items"] = db["items"] + [4] и sync
```

**sqlite3 — встроенная СУБД SQLite**

- [ ] **Что такое и зачем:** **sqlite3** — встроенный драйвер для **SQLite**: база данных в одном файле (или в памяти), без отдельного сервера. Поддержка SQL (CREATE TABLE, INSERT, SELECT, транзакции, индексы). **Применения:** локальное хранилище приложений, кеш, прототипы, встроенные БД в десктоп/мобильных приложениях.
- [ ] **API:** **sqlite3.connect(database, timeout=5.0, ...)** — подключение к файлу или **':memory:'**; возвращает **Connection**. **conn.cursor()** — курсор; **cursor.execute(sql, parameters=())** — выполнить запрос; **parameters** — подстановка **?** или **:name** (защита от SQL-инъекций). **cursor.fetchone()**, **cursor.fetchall()**, **cursor.fetchmany(n)** — результаты SELECT. **conn.commit()** — зафиксировать транзакцию; **conn.rollback()** — откат. **conn.close()**. Контекстный менеджер **with sqlite3.connect('file.db') as conn:** коммитит при выходе (или откатывает при исключении). **conn.execute(sql)** — короткая форма (создаёт курсор). **Row** — доступ к столбцам по имени: **cursor.row_factory = sqlite3.Row**; **row['col']**. **Граничные случаи:** для вставки многих строк эффективнее **cursor.executemany(sql, seq_of_params)**; **timeout** — сколько секунд ждать блокировку при конкурирующей записи.

**Пример sqlite3**

```python
import sqlite3
with sqlite3.connect("app.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    conn.commit()
    conn.row_factory = sqlite3.Row
    for row in conn.execute("SELECT id, name FROM users"):
        print(row["id"], row["name"])
# В памяти
conn = sqlite3.connect(":memory:")
conn.executemany("INSERT INTO t VALUES (?, ?)", [(1, "a"), (2, "b")])
```

**dbm — интерфейс к dbm-подобным БД**

- [ ] **Что такое и зачем:** **dbm** — общий интерфейс к **key-value** хранилищам в стиле **dbm** (Unix): ключ и значение — **bytes**. Несколько реализаций: **dbm.gnu** (GDBM), **dbm.ndbm** (NDBM), **dbm.dumb** (чистый Python, без внешних библиотек; медленнее, но везде доступен). **dbm.open(file, flag='r', mode=0o666)** — открыть; **flag**: **'r'** (чтение), **'w'** (чтение/запись), **'c'** (создать при отсутствии), **'n'** (всегда создать новый). Возвращает объект dict-подобный: **db[key]**, **db[key] = value**, **del db[key]**, **key in db**, **.keys()** (итератор), **.close()**. **Граничные случаи:** ключи и значения — только bytes; для строк использовать **key.encode()** и **value.decode()**; при **flag='r'** запись вызовет ошибку; на разных платформах может подхватываться разная реализация (gnu/ndbm/dumb). **Применения:** простой кеш по ключу, совместимость с утилитами Unix (dbm). Для произвольных типов и строковых ключей — **shelve**.

**Пример dbm**

```python
import dbm
with dbm.open("cache.dbm", "c") as db:
    db[b"user:1"] = b"data"
    db["user:2".encode()] = "value".encode()
# Чтение
with dbm.open("cache.dbm", "r") as db:
    print(db.get(b"user:1"))  # b'data'
    print(list(db.keys()))
```

### signal, atexit

**signal — обработка сигналов ОС**

- [ ] **Что такое и зачем:** **signal** позволяет перехватывать **сигналы** ОС (SIGINT при Ctrl+C, SIGTERM при завершении процесса, SIGALRM для таймера и т.д.) и вызывать обработчик в Python. **Применения:** корректное завершение при Ctrl+C (сохранение состояния, закрытие соединений), таймауты через SIGALRM (осторожно: не все функции перезапускаются после прерывания), обработка SIGCHLD в серверах.
- [ ] **API:** **signal.signal(signum, handler)** — установить обработчик для **signum**; **handler** — callable с двумя аргументами (signum, frame) или **SIG_IGN** (игнорировать), **SIG_DFL** (по умолчанию). **signal.SIGINT** (2), **signal.SIGTERM** (15) — типичные номера. **signal.alarm(seconds)** — через **seconds** секунд будет отправлен **SIGALRM** (только один таймер; 0 отменяет); **signal.pause()** — ждать любого сигнала. **signal.siginterrupt(signum, flag)** — перезапускать ли системные вызовы после обработчика (по умолчанию для SIGINT — да). **Ограничения:** обработчик должен быть быстрым; не все функции безопасны для вызова из обработчика (например выделение памяти). В многопоточном коде только главный поток получает сигналы (на большинстве платформ).

**Пример signal**

```python
import signal
import sys
def handler(signum, frame):
    print("Got Ctrl+C, cleaning up...")
    sys.exit(0)
signal.signal(signal.SIGINT, handler)
# Или установить флаг и выйти из цикла:
running = True
def stop(signum, frame):
    global running
    running = False
signal.signal(signal.SIGINT, stop)
while running:
    do_work()
```

**atexit — выполнение при выходе**

- [ ] **Что такое и зачем:** **atexit** регистрирует функции, которые будут вызваны при **нормальном** завершении интерпретатора (sys.exit, окончание главного потока). Не вызывается при kill -9, segfault, os.\_exit(). **Применения:** закрытие файлов и соединений, сброс кеша на диск, удаление временных файлов, логирование «shutdown».
- [ ] **API:** **atexit.register(func, \*args, **kwargs)** — зарегистрировать **func(\*args, **kwargs)** при выходе; можно вызывать многократно — функции выполняются в порядке, обратном регистрации (LIFO). **atexit.unregister(func)** — удалить из списка. Декоратор **@atexit.register** — зарегистрировать функцию без аргументов. **Граничные случаи:** при исключении в одной из зарегистрированных функций следующие всё равно вызываются; **os.\_exit()** не вызывает atexit.

**Пример atexit**

```python
import atexit
f = open("log.txt", "a")
def close_log():
    f.write("Shutdown\n")
    f.close()
atexit.register(close_log)
# или
@atexit.register
def cleanup():
    print("Exiting")
```

### string, textwrap, unicodedata

**string — константы и шаблоны**

- [ ] **Что такое и зачем:** модуль **string** предоставляет **константы** символов и простой **шаблонный** подстановочный синтаксис (**$variable**). **Применения:** проверка символов (цифра, буква), генерация паролей/токенов из набора символов, простые шаблоны без зависимостей (безопаснее eval при пользовательском шаблоне).
- [ ] **Константы:** **string.ascii_letters** — **abcdef...XYZ**; **string.ascii_lowercase**, **string.ascii_uppercase**; **string.digits** — **0123456789**; **string.hexdigits**; **string.octdigits**; **string.punctuation** — знаки препинания; **string.whitespace** — пробельные символы; **string.printable** — все печатаемые. Используются в **random.choice(string.ascii_letters + string.digits)** и т.д.
- [ ] **string.Template:** **string.Template(template_string)** — шаблон с подстановками **$var** или **${expr}**; **$$** — литерал **$**. **.substitute(mapping, **kwargs)** — подставить значения (ключ должен существовать; при отсутствии ключа — **KeyError**); **.safe_substitute(...)** — отсутствующие ключи оставить как есть (без ошибки). Безопаснее **str.format** при шаблоне от пользователя: нет доступа к атрибутам (**{obj.attr}**) и вызовам (**{func()}**), только подстановка по имени. **string.templatelib** (3.15+) — расширенный API шаблонов. **Граничные случаи:** разделитель по умолчанию **$**; для **$identifier** после идентификатора нужен пробел или конец строки, иначе используйте **${identifier}\*\*.

**Пример string.Template**

```python
from string import Template
t = Template("Hello, $name! Balance: $$ $amount.")
print(t.substitute(name="User", amount=100))   # Hello, User! Balance: $ 100.
print(t.safe_substitute(name="User"))           # Hello, User! Balance: $ $amount.
# Безопасность: пользовательский шаблон не может выполнить код
t2 = Template("$user said $msg")  # user не может подставить "{__import__('os').system('rm -rf /')}"
t2.substitute(user="alice", msg="hi")
```

**textwrap — форматирование текста**

- [ ] **Что такое и зачем:** **textwrap** — **перенос строк** и **выравнивание** текста: разбиение длинной строки на строки заданной ширины, удаление общего ведущего пробела, добавление отступа. **Применения:** форматирование вывода в консоль, подготовка текста для отображения в фиксированной ширине, docstring-форматирование.
- [ ] **API:** **textwrap.wrap(text, width=70, ...)** — список строк не длиннее **width**; **textwrap.fill(text, width=70, ...)** — одна строка с переносами **\n**. **textwrap.dedent(text)** — убрать общий ведущий пробел у всех строк (удобно для многострочных строк в коде). **textwrap.indent(text, prefix)** — добавить **prefix** к каждой строке. **textwrap.shorten(text, width=70, placeholder='...')** — обрезать до **width** символов, заменив конец на **placeholder**. **textwrap.TextWrapper(width=70, ...)** — объект с настройками (**expand_tabs**, **replace_whitespace**, **initial_indent**, **subsequent_indent** и т.д.); **.wrap(text)**, **.fill(text)**. **Граничные случаи:** **wrap** не разбивает слова по середине; длинное слово без пробелов может превысить **width** (параметр **break_long_words**).

**Пример textwrap (§7a)**

```python
import textwrap
s = "The quick brown fox jumps over the lazy dog."
textwrap.wrap(s, width=15)  # ['The quick', 'brown fox', 'jumps over', ...]
textwrap.fill(s, width=20)
textwrap.dedent("  line1\n    line2")  # 'line1\n  line2'
textwrap.indent("a\nb", "> ")  # '> a\n> b'
textwrap.shorten("Long text here", width=10)  # 'Long te...'
```

**unicodedata — свойства символов Unicode**

- [ ] **Что такое и зачем:** **unicodedata** предоставляет доступ к **базе данных Unicode**: имя символа, категория (буква, цифра, пробел и т.д.), нормализация форм (NFC, NFD, NFKC, NFKD), разложение символов. **Применения:** нормализация текста для сравнения и поиска, проверка типа символа, отладка отображения (имя символа). См. также §15d для углублённого разбора.
- [ ] **API:** **unicodedata.normalize(form, unistr)** — нормализовать строку (**form**: **'NFC'**, **'NFD'**, **'NFKC'**, **'NFKD'**). **unicodedata.name(chr)** — имя символа (например **'LATIN SMALL LETTER A'**); **ValueError** для неопределённых символов; **unicodedata.category(chr)** — категория (**'Lu'** — буква верхнего регистра, **'Nd'** — цифра и т.д.). **unicodedata.decomposition(chr)** — строка разложения (пустая или например **'0041 0300'**). **unicodedata.numeric(chr)** — числовое значение для цифровых символов (римские, дроби); **ValueError** для нечисловых. **Граничные случаи:** сравнение строк после **normalize('NFC', s)** устраняет различия комбинирующих символов; для поиска/сортировки часто используют **NFKC**.

**Пример unicodedata**

```python
import unicodedata
unicodedata.name("a")      # 'LATIN SMALL LETTER A'
unicodedata.category("9") # 'Nd'
unicodedata.normalize("NFC", "café")  # объединённая форма
unicodedata.numeric("½")   # 0.5
# Нормализация для сравнения
s1 = "café"  # e + combining acute
s2 = "café"  # может быть один символ e-acute
unicodedata.normalize("NFC", s1) == unicodedata.normalize("NFC", s2)
```

### unittest, doctest

**unittest — фреймворк модульных тестов**

- [ ] **Что такое и зачем:** **unittest** — встроенный фреймворк для **модульного тестирования**: классы тестов, фикстуры (setUp/tearDown), множество assert-методов, запуск из командной строки и обнаружение тестов. **Применения:** тестирование библиотек и приложений, CI/CD, регрессии.
- [ ] **Структура:** класс, наследующий **unittest.TestCase**; методы тестов — имена с **test\_**. **self.assertEqual(a, b)** — равенство; **self.assertNotEqual(a, b)**; **self.assertRaises(ExceptionType, callable, \*args)** — ожидаемое исключение (или контекстный менеджер **with self.assertRaises(ValueError): ...**); **self.assertIn(member, container)**; **self.assertTrue(x)**; **self.assertIsNone(x)**; **self.assertAlmostEqual(a, b, places=7)** — для float (сравнение с точностью); **self.assertRegex(s, r)**; **self.assertDictEqual**, **self.assertListEqual**, **self.assertSequenceEqual** и др. **setUp()** — перед каждым тестом; **tearDown()** — после; **setUpClass(cls)** / **tearDownClass(cls)** — один раз на класс (декоратор **@classmethod**).
- [ ] **Запуск:** **unittest.main()** в конце файла — запуск всех тестов в модуле; **python -m unittest discover -s tests -p 'test\_\*.py'** — автоматическое обнаружение тестов; **python -m unittest module.TestClass.test_method** — один тест. **unittest.skip(reason)**, **unittest.skipIf(condition, reason)** — пропуск теста; **@unittest.expectedFailure** — тест ожидаемо падает. **Граничные случаи:** порядок выполнения тестов внутри класса не гарантирован; не полагаться на общее состояние между тестами — использовать **setUp**/ **tearDown**.
- [ ] **unittest.mock** (отдельный подмодуль): **Mock**, **MagicMock** — объекты-заглушки (автоматические атрибуты); **patch('module.obj', new)** — подмена атрибута/объекта в тесте; **@patch**, **with patch(...)**. **Применения:** изоляция теста от внешних зависимостей (сеть, БД, файлы).

**Пример unittest**

```python
import unittest
def add(a, b):
    return a + b
class TestAdd(unittest.TestCase):
    def setUp(self):
        pass  # подготовка перед каждым тестом
    def tearDown(self):
        pass  # очистка после каждого теста
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
    def test_raises(self):
        with self.assertRaises(TypeError):
            add("a", 1)
    @unittest.skip("not implemented")
    def test_future(self):
        self.fail("todo")
if __name__ == "__main__":
    unittest.main()
# Запуск: python -m unittest test_module.TestAdd
```

**doctest — тесты в docstring**

- [ ] **Что такое и зачем:** **doctest** извлекает из **docstring** интерактивные сессии Python (>>> и вывод) и выполняет их как тесты: сравнивает фактический вывод с ожидаемым. **Применения:** документация с проверяемыми примерами, быстрые тесты для простых функций, регрессии примеров в документации.
- [ ] **API:** **doctest.testmod(m=None, name=None, verbose=None, ...)** — тестировать текущий модуль **m** (по умолчанию ****main****); **verbose=True** — печать каждого теста. **doctest.testfile(filename)** — тесты из файла. В docstring: строки **>>> выражение** и следующая строка — ожидаемый вывод (пустая строка разделяет примеры). **doctest.run_docstring_examples(func, globs)** — запустить примеры из docstring функции. Директивы: **# doctest: +ELLIPSIS** — **...** в ожидаемом выводе совпадает с любой подстрокой; **# doctest: +SKIP** — пропустить пример; **# doctest: +NORMALIZE_WHITESPACE** — игнорировать разницу в пробелах. **Граничные случаи:** сравнение по строке — порядок ключей в dict может отличаться; для float использовать **ELLIPSIS** или округление в примере.

**Пример doctest**

```python
def div(a, b):
    """Divide a by b.
    >>> div(10, 2)
    5.0
    >>> div(1, 3)  # doctest: +ELLIPSIS
    0.333...
    >>> div(1, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return a / b
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

### uuid, weakref

**uuid — уникальные идентификаторы**

- [ ] **Что такое и зачем:** модуль **uuid** генерирует и разбирает **UUID** (Universally Unique Identifier) — 128-битные идентификаторы, практически уникальные без координации. **Применения:** первичные ключи в БД, токены сессий, имена временных файлов, идентификаторы сообщений в распределённых системах.
- [ ] **Версии:** **uuid.uuid4()** — случайный UUID (криптостойкая случайность от ОС); наиболее часто используется. **uuid.uuid1(node=None, clock_seq=None)** — на основе времени и MAC (уникальность по сети); **uuid.uuid3(namespace, name)** — MD5-хеш от namespace и имени; **uuid.uuid5(namespace, name)** — SHA-1-хеш (предпочтительнее uuid3). **uuid.NAMESPACE_DNS**, **uuid.NAMESPACE_URL** и т.д. — стандартные пространства имён для uuid3/uuid5.
- [ ] **API:** объект **UUID** имеет атрибуты **.hex**, **.bytes**; **str(uuid)** — каноническая строка **xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx**. **uuid.UUID(string)** — разобрать строку или hex. **uuid.uuid4()** возвращает объект **UUID**.

**Пример uuid**

```python
import uuid
uid = uuid.uuid4()
str(uid)     # 'a1b2c3d4-e5f6-7890-abcd-ef1234567890'
uid.hex      # 'a1b2c3d4e5f67890abcdef1234567890'
uuid.UUID(uid.hex)  # тот же UUID
# Детерминированный UUID из имени (uuid5 предпочтительнее uuid3)
uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
```

**weakref — слабые ссылки**

- [ ] **Что такое и зачем:** **weakref** позволяет хранить ссылку на объект **без увеличения** счётчика ссылок: если других ссылок нет, объект может быть собран сборщиком мусора. **Применения:** кеши без утечек (объект удаляется, когда больше нигде не нужен), обратные ссылки без циклов (родитель → дети без дети → родитель по сильной ссылке), подписки/наблюдатели без удержания объектов.
- [ ] **API:** **weakref.ref(obj, callback=None)** — слабая ссылка; **ref()** возвращает объект или **None** если объект удалён; **callback(ref)** вызывается при удалении объекта. **weakref.proxy(obj, callback=None)** — прокси: обращение как к объекту, при удалении — **ReferenceError**. **weakref.WeakValueDictionary()** — dict, значения которого — слабые ссылки; ключи остаются, значения могут исчезнуть. **weakref.WeakKeyDictionary()** — слабые ключи. **weakref.WeakSet** — множество со слабыми ссылками. **weakref.finalize(obj, func, \*args, **kwargs)** — вызвать **func** при уничтожении **obj** (аналог деструктора без ****del**\*\*).

**Пример weakref: кеш без утечек**

```python
import weakref
cache = weakref.WeakValueDictionary()
class Big:
    pass
b = Big()
cache["key"] = b
cache["key"] is b   # True
del b
# при следующей сборке мусора cache["key"] может исчезнуть
# cache.get("key")  # None (если объект уже собран)
```

### zoneinfo (3.9+)

**zoneinfo — часовые пояса IANA**

- [ ] **Что такое и зачем:** модуль **zoneinfo** (PEP 615) предоставляет **часовые пояса** по базе IANA (Olson): смещение от UTC, правила перехода на летнее время (DST). **ZoneInfo** подставляется в **datetime** для создания **aware** времени. **Применения:** корректная работа с датой/временем в разных регионах (логи, планировщики, отображение пользователю), замена **pytz** в новом коде.
- [ ] **API:** **zoneinfo.ZoneInfo(key)** — объект часового пояса; **key** — строка имени (**'Europe/Moscow'**, **'America/New_York'**, **'UTC'**). **datetime.now(ZoneInfo('Europe/Moscow'))** — текущее время в Москве (aware). **datetime(2024, 1, 15, 12, 0, tzinfo=ZoneInfo('UTC'))** — конкретное время в UTC. **.utcoffset(dt)** — смещение для данной даты/времени (учёт DST). База данных загружается из системных файлов (например **/usr/share/zoneinfo**) или из пакета **tzdata** (PyPI) на Windows. **zoneinfo.available_timezones()** — множество имён доступных зон.

**Пример zoneinfo**

```python
from datetime import datetime
from zoneinfo import ZoneInfo
utc_now = datetime.now(ZoneInfo("UTC"))
moscow_now = datetime.now(ZoneInfo("Europe/Moscow"))
# Конвертация: naive → aware или смена зоны
dt_utc = datetime(2024, 6, 15, 12, 0, tzinfo=ZoneInfo("UTC"))
dt_moscow = dt_utc.astimezone(ZoneInfo("Europe/Moscow"))
```

### Платформо-зависимые

**Что такое и зачем**

Модули ниже доступны только на соответствующих ОС; импорт на другой платформе даёт **ModuleNotFoundError** или **ImportError**. Они дают прямой доступ к API ОС: системные вызовы, базы пользователей/групп, режимы терминала, блокировки файлов, реестр Windows. В прикладном коде часто достаточно **os**, **pathlib**, **subprocess**; эти модули нужны для тонкой настройки, демонов, TUI, интеграции с ОС.

**Unix: posix, pwd, grp**

- [ ] **posix** — низкоуровневый интерфейс к **POSIX**: системные вызовы (**posix.open**, **posix.read**, **posix.write**, **posix.stat**, **posix.chmod** и т.д.), константы (**posix.O_RDONLY**, **posix.S_IRWXU**), функции, дублируемые в **os**. В прикладном коде обычно используют **os** (кроссплатформеннее); **posix** — для тонкой настройки или доступа к вызовам, отсутствующим в **os**. **Граничные случаи:** при ошибке системного вызова возбуждается **OSError** с **errno**; проверять **errno.EINTR** при прерывании сигналом.
- [ ] **pwd** — информация о **пользователях** из базы системы (/etc/passwd): **pwd.getpwnam(name)** — структура **struct_passwd** по имени пользователя (**pw_uid**, **pw_gid**, **pw_dir**, **pw_shell** и т.д.); **pwd.getpwuid(uid)** — по UID; **pwd.getpwall()** — все записи. **KeyError** при отсутствии пользователя. **Применения:** получение домашнего каталога пользователя (**getpwnam(os.getenv('USER')).pw_dir**), UID/GID для **os.chown**, проверка существования пользователя.

**Пример pwd/grp (Unix)**

```python
import os
import pwd
import grp
# Домашний каталог текущего пользователя
uid = os.getuid()
pw = pwd.getpwuid(uid)
home = pw.pw_dir  # '/home/user'
# Имя группы по GID
gid = pw.pw_gid
gr = grp.getgrgid(gid)
group_name = gr.gr_name
# Проверка: пользователь root?
is_root = uid == 0
```

- [ ] **grp** — информация о **группах** (/etc/group): **grp.getgrnam(name)** — по имени группы (**gr_gid**, **gr_mem** — список имён пользователей); **grp.getgrgid(gid)** — по GID; **grp.getgrall()** — все записи. **Применения:** отображение имён групп по GID, проверка членства в группе (**username in grp.getgrgid(gid).gr_mem**).

**Unix: termios, tty, fcntl, pty, resource**

- [ ] **termios** — управление **режимами терминала** (POSIX termios): скорость передачи (baudrate), флаги (raw/cooked), символы управления (erase, kill). **termios.tcgetattr(fd)** — текущие атрибуты (список из 6 элементов); **termios.tcsetattr(fd, when, attrs)** — установить (**when**: **termios.TCSANOW**, **TCSADRAIN**, **TCSAFLUSH**). **termios.tcsendbreak(fd, duration)** — послать break. **Применения:** интерактивный ввод посимвольно (без Enter), скрытие эха для паролей, настройка последовательных портов.
- [ ] **tty** — утилиты для **терминала**: **tty.setraw(fd)** — перевести в raw-режим (символы передаются сразу, без обработки); **tty.setcbreak(fd)** — cbreak (символы по одному, но Ctrl+C обрабатывается). **Применения:** упрощение переключения режимов терминала по сравнению с ручным **termios**.
- [ ] **fcntl** — управление **файловыми дескрипторами**: **fcntl.flock(fd, operation)** — рекомендательные блокировки файла (**fcntl.LOCK_SH** — разделяемая, **LOCK_EX** — эксклюзивная, **LOCK_UN** — снять); **fcntl.LOCK_NB** — не блокироваться при занятости. **fcntl.fcntl(fd, cmd, arg)** — низкоуровневые команды (**F_SETFL** для **O_NONBLOCK** и т.д.). **Применения:** блокировка файлов между процессами (lock-файлы), неблокирующий I/O.

**Пример fcntl: lock-файл (Unix)**

```python
import fcntl
import os
f = open("/tmp/mylock.lock", "w")
try:
    fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    print("Already locked by another process")
    f.close()
    raise
try:
    # критическая секция
    pass
finally:
    fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    f.close()
```

- [ ] **pty** — **псевдо-терминалы** (master/slave): **pty.openpty()** — пара **(master_fd, slave_fd)**; подпроцесс, привязанный к slave, ведёт себя как интерактивный терминал. **pty.fork()** — fork с дочерним процессом, подключённым к slave; возвращает **(pid, fd)** в родителе и 0 в ребёнке. **Применения:** интерактивные подпроцессы (ssh, sudo), тестирование TUI.
- [ ] **resource** — **лимиты ресурсов** процесса (getrlimit/setrlimit): **resource.getrlimit(resource.RLIMIT_CPU)** — кортеж **(soft, hard)** лимита CPU (секунды); **resource.RLIMIT_AS** — размер виртуальной памяти; **resource.RLIMIT_NOFILE** — число открытых файлов; **resource.setrlimit(rlimit, (soft, hard))** — установить. **Применения:** демоны и серверы (ограничить память/файлы), песочницы.

**Windows: msvcrt, winreg**

- [ ] **msvcrt** — консольный ввод/вывод и блокировки под **Windows** (использует MSVC runtime): **msvcrt.kbhit()** — есть ли символ в буфере без блокировки (True/False); **msvcrt.getch()** — один байт без эха; **msvcrt.getwch()** — wide-символ (Unicode). **msvcrt.locking(fd, mode, nbytes)** — блокировка области файла (**msvcrt.LK_LOCK**, **LK_UNLCK** и т.д.). **Применения:** консольные утилиты с посимвольным вводом (пароль без эха), блокировка файлов на Windows.
- [ ] **winreg** — доступ к **реестру Windows**: **winreg.OpenKey(key, sub_key, reserved=0, access=KEY_READ)** — открыть ключ (key — **HKEY_LOCAL_MACHINE**, **HKEY_CURRENT_USER** и др.); **winreg.QueryValue(key, sub_key)** — значение по умолчанию ключа; **winreg.QueryValueEx(key, name)** — **(value, type)** по имени; **winreg.SetValueEx(key, name, reserved, type, value)** — записать; **winreg.CreateKey(key, sub_key)**; **winreg.DeleteKey(key, sub_key)**; **winreg.EnumKey(key, index)** — имя подключа по индексу; **winreg.EnumValue(key, index)** — имя и значение по индексу. **Применения:** чтение/запись настроек приложений в реестре, проверка установленного ПО.

**Пример winreg (Windows)**

```python
import winreg
# Прочитать значение из реестра
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\MyApp")
val, _ = winreg.QueryValueEx(key, "Setting")
winreg.CloseKey(key)
# Перечислить подключи
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE")
for i in range(winreg.QueryInfoKey(key)[0]):
    sub = winreg.EnumKey(key, i)
    print(sub)
winreg.CloseKey(key)
```

**curses — терминальный UI (полноэкранный)**

- [ ] **Что такое и зачем:** **curses** — биндинги к библиотеке **ncurses** (Unix): полноэкранный текстовый интерфейс — окна, цвета, атрибуты (жирный, подчёркивание), ввод с клавиатуры (включая F-клавиши, стрелки). **Применения:** TUI-приложения (меню, формы, дашборды в консоли), игры в терминале, интерактивные утилиты (top, htop-подобные).
- [ ] **Основной API:** **curses.initscr()** — инициализация экрана; **curses.endwin()** — восстановить терминал при выходе. **stdscr.addstr(y, x, text, attr)** — вывести строку в позиции (y, x) с атрибутами; **stdscr.getch()** — один символ/код клавиши; **curses.newwin(h, w, y, x)** — создать окно. **curses.cbreak()** / **curses.nocbreak()** — режим ввода; **curses.echo()** / **curses.noecho()** — эхо. **curses.wrapper(func)** — вызвать **func(stdscr)** и по завершении (нормальному или по исключению) восстановить терминал — предпочтительный способ запуска. На **Windows** модуль **curses** может быть собран с **PDCurses** или через **windows** (ограниченный API). **Граничные случаи:** при падении программы нужно вызвать **endwin()**, иначе терминал остаётся в «сыром» режиме; обычно оборачивают в **try/finally** или используют **curses.wrapper(func)**.

**Пример curses**

```python
import curses
def main(stdscr):
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)
    stdscr.clear()
    stdscr.addstr(0, 0, "Press 'q' to quit", curses.A_BOLD)
    stdscr.addstr(2, 0, "Hello, curses!")
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == ord("q"):
            break
        stdscr.addstr(5, 0, f"Key: {key}   ")
        stdscr.refresh()
curses.wrapper(main)  # восстанавливает терминал при выходе или исключении
```

### Специализированные (реже используемые)

**Аудио: aifc, sunau, audioop**

- [ ] **aifc** — чтение и запись файлов **AIFF** (Audio Interchange File Format): заголовок (каналы, частота, битность), аудио-фrames. **aifc.open(file, mode)** — открыть файл; **.getnchannels()**, **.getframerate()**, **.readframes(n)**; **.writeframes(data)**. Часть API помечена deprecated; для новой разработки часто используют **soundfile**, **wave** (для WAV) или сторонние библиотеки.
- [ ] **sunau** — чтение/запись формата **Sun AU** (.au): аналогичный API (открытие, параметры, readframes/writeframes). Реже используется, чем WAV/AIFF.
- [ ] **audioop** — операции над **сырыми** аудио-данными (строки байт сэмплов): **audioop.ratecv(fragment, width, nchannels, inrate, outrate)** — изменение частоты дискретизации; **audioop.tomono(fragment, width, lfactor, rfactor)** — стерео в моно; **audioop.tostereo(fragment, width, lfactor, rfactor)** — моно в стерео; **audioop.avg(fragment, width)** — среднее значение; **audioop.rms(fragment, width)** — RMS. В Python 3.13 **audioop** помечен **deprecated**; рекомендуется использовать **numpy** или специализированные библиотеки для обработки аудио.

**colorsys — конвертация цветовых пространств**

- [ ] **Что такое и зачем:** **colorsys** конвертирует цвета между **RGB** (красный, зелёный, синий; значения 0–1) и **HLS** (Hue, Lightness, Saturation), **HSV** (Hue, Saturation, Value), **YIQ** (используется в NTSC). **Применения:** генерация палитр (перебор по оттенку/насыщенности), конвертация для графических библиотек, доступность (contrast) цветов.
- [ ] **API:** **colorsys.rgb_to_hls(r, g, b)** — (h, l, s); **colorsys.hls_to_rgb(h, l, s)** — (r, g, b). **colorsys.rgb_to_hsv(r, g, b)** и **colorsys.hsv_to_rgb(h, s, v)**. **colorsys.rgb_to_yiq(r, g, b)** и **colorsys.yiq_to_rgb(y, i, q)**. Все компоненты в диапазоне 0–1 (H в colorsys тоже 0–1, не 0–360). **Граничные случаи:** при L=0 или L=1 в HLS оттенок (H) не определён; при S=0 в HSV оттенок не определён.

**Пример colorsys**

```python
import colorsys
# RGB (1, 0, 0) — красный
h, l, s = colorsys.rgb_to_hls(1, 0, 0)
r, g, b = colorsys.hls_to_rgb(h, l, s)  # (1, 0, 0)
# Генерация палитры по оттенку
for i in range(5):
    h = i / 5
    r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
    print(r, g, b)
```

**graphlib — топологическая сортировка (3.9+)**

- [ ] **Что такое и зачем:** **graphlib** даёт **топологическую сортировку** ориентированного ациклического графа (DAG): порядок узлов, при котором все зависимости идут раньше зависимых. **Применения:** порядок сборки (зависимости модулей/пакетов), планирование задач с зависимостями, порядок выполнения шагов в пайплайне.
- [ ] **API:** **graphlib.TopologicalSorter(graph=None)** — объект сортировщика; **.add(node, \*dependencies)** — добавить узел и его зависимости (узлы, которые должны быть обработаны раньше); **.prepare()** — завершить добавление и подготовить сортировку; **.get_ready()** — итератор узлов, готовых к выполнению (все зависимости уже «выполнены»); **.done(node)** — отметить узел выполненным (разблокирует зависимые). **.static_order()** — итератор по узлам в топологическом порядке (если граф статичен). Циклы в графе приводят к **CycleError**.

**Пример graphlib**

```python
# Python 3.9+
import graphlib
# Зависимости: C зависит от A и B, D зависит от C
ts = graphlib.TopologicalSorter()
ts.add("C", "A", "B")
ts.add("D", "C")
ts.add("A")   # без зависимостей
ts.add("B")
ts.prepare()
# Статический порядок (все узлы известны заранее)
list(ts.static_order())  # например ['A', 'B', 'C', 'D'] (зависимые после зависимостей)
# Или пошагово: get_ready() → выполнить → done(node)
# ready = list(ts.get_ready())   # узлы без невыполненных зависимостей
# for node in ready:
#     process(node)
#     ts.done(node)
# ready = list(ts.get_ready())   # следующие готовые
```

**Почта и протоколы: mailbox, mailcap, netrc, quopri**

- [ ] **mailbox** — парсинг и итерация по **почтовым ящикам** в форматах **mbox**, **Maildir**, **MH**: **mailbox.mbox(path)** — mbox; **mailbox.Maildir(path)** — Maildir; **mailbox.MH(path)** — MH. Общий интерфейс: итерация по сообщениям (**for msg in mbox:**), добавление (**mbox.add(message)** — message — **email.message.Message** или bytes/str), удаление (**mbox.remove(key)** по ключу сообщения). **mbox[key]** — сообщение по ключу; **mbox.keys()** — ключи. **Применения:** скрипты обработки почты, миграция ящиков, анализ писем. **Граничные случаи:** mbox — один файл, блокировки при одновременной записи; Maildir — каталог с файлами, лучше для параллельного доступа.
- [ ] **mailcap** — сопоставление **MIME-типов** с командами просмотра/обработки из файла **mailcap** (стандарт Unix): **mailcap.findmatch(caps, MIMEtype)** — **(command, plist)** — команда и параметры для отображения типа; **caps** — список из **mailcap.getcaps()**. **Применения:** открытие вложений «внешней» программой по типу.
- [ ] **netrc** — парсинг файла **.netrc** (логин и пароль для машин): **netrc.netrc(file=None)** — загрузить (по умолчанию **~/.netrc**); **.authenticators(host)** — **(login, account, password)** для хоста или **None**. **.hosts** — dict хостов. **Применения:** автоматический логин в FTP/другие протоколы без хранения пароля в коде. **Граничные случаи:** права на файл должны быть 600 (иначе предупреждение или отказ).
- [ ] **quopri** — кодирование/декодирование **quoted-printable** (MIME): **quopri.encode(data)** — байты в quoted-printable (bytes); **quopri.decode(data)** — обратно. Символы вне печатаемого ASCII представляются как **=XX** (hex). **Применения:** кодирование тела письма (Content-Transfer-Encoding: quoted-printable), совместимость с email-сообщениями.

**Пример mailbox**

```python
import mailbox
from email import message_from_bytes
# Итерация по mbox (один файл с письмами)
mbox = mailbox.mbox("/var/mail/user")
for key, msg in mbox.items():
    subject = msg.get("Subject", "")
    print(key, subject)
# Добавить письмо (message — email.message.Message или bytes)
new_msg = message_from_bytes(b"From: a@b.com\nSubject: Hi\n\nBody")
mbox.add(new_msg)
mbox.flush()
mbox.close()
# Maildir — каталог с файлами
mdir = mailbox.Maildir("/home/user/Maildir")
for msg in mdir:
    print(msg.get("Subject"))
```

**Пример netrc**

```python
import netrc
# Файл ~/.netrc: machine ftp.example.com login user password secret
n = netrc.netrc()
login, account, password = n.authenticators("ftp.example.com")
# login, password — для FTP и т.д.
# n.authenticators("unknown")  # None
```

**Пример quopri**

```python
import quopri
data = "Привет, мир!".encode("utf-8")
encoded = quopri.encode(data)  # bytes, нечитаемые символы как =XX
decoded = quopri.decode(encoded)
decoded.decode("utf-8")  # 'Привет, мир!'
```

**socketserver — базовые классы для сетевых серверов**

- [ ] **Что такое и зачем:** **socketserver** предоставляет **базовые классы** для TCP- и UDP-серверов: обработка привязки, приёма подключений и передачи запроса обработчику. **Применения:** простые серверы (эхо, тестовый HTTP), прототипы без asyncio/threading вручную.
- [ ] **API:** **socketserver.TCPServer(server_address, RequestHandlerClass)** — TCP-сервер; **socketserver.UDPServer(...)** — UDP. **BaseRequestHandler** — базовый обработчик; подкласс переопределяет **handle()** — один запрос на соединение. **self.request** — сокет (TCP) или (data, socket) (UDP); **self.client_address** — адрес клиента; **self.server** — сервер. **ThreadingMixIn**, **ForkingMixIn** — примеси для многопоточного/многопроцессного обслуживания: **class ThreadedTCPServer(ThreadingMixIn, TCPServer): pass**. **serve_forever()** — цикл приёма запросов; **shutdown()** — остановить. **Граничные случаи:** один запрос — одно соединение (TCP); для длинных сессий в **handle()** читать/писать в цикле.

**Пример socketserver**

```python
import socketserver
class EchoHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        self.request.sendall(data)
with socketserver.TCPServer(("", 9997), EchoHandler) as server:
    server.serve_forever()
# Многопоточный сервер
class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
ThreadedTCPServer(("", 9997), EchoHandler).serve_forever()
```

**stat, stringprep, plistlib**

- [ ] **stat** — константы и утилиты для разбора **режима файла** (результат **os.stat().st_mode**): **stat.S_IFREG** — обычный файл; **stat.S_IFDIR** — каталог; **stat.S_IRWXU** — права пользователя (rwx); **stat.S_IRUSR**, **stat.S_IWUSR** и т.д. **stat.filemode(mode)** — строка в стиле ls (например **'-rwxr-xr-x'**). **stat.S_ISDIR(mode)** — каталог ли; **stat.S_ISREG(mode)** — обычный файл; **stat.S_ISLNK(mode)** — символическая ссылка. **Применения:** проверка типа файла и прав по **os.stat()**, отображение прав в стиле **ls -l**.
- [ ] **stringprep** — **подготовка строк** по RFC (профили для идентификаторов, имён и т.д.): **stringprep.in_table_c11(s)** — проверка символа по таблице (Unicode); **stringprep.map_table_b11(s)** — замена по таблице. Используется для нормализации идентификаторов (например Unicode-имена в протоколах). **Применения:** совместимость с XMPP, IDNA и др. стандартами.
- [ ] **plistlib** — чтение и запись **plist** (Property List, формат macOS/Apple — XML или бинарный): **plistlib.load(fp)** — из потока; **plistlib.loads(data)** — из bytes; **plistlib.dump(obj, fp)** — записать; **plistlib.dumps(obj)** — в bytes. Поддерживаются типы: dict, list, str, int, float, bool, bytes, datetime. **plistlib.load(..., dict_type=collections.OrderedDict)** — сохранить порядок ключей. **Применения:** конфиги и метаданные в экосистеме Apple, скрипты для macOS.

**Пример stat**

```python
import os
import stat
st = os.stat("file.txt")
mode = st.st_mode
stat.S_ISREG(mode)   # True — обычный файл
stat.S_ISDIR(mode)   # False
stat.filemode(mode)  # '-rw-r--r--' (в стиле ls)
# Проверка прав на запись для владельца
if mode & stat.S_IWUSR:
    print("Owner can write")
```

**Пример plistlib**

```python
import plistlib
# Запись
data = {"name": "MyApp", "version": "1.0", "enabled": True}
with open("config.plist", "wb") as f:
    plistlib.dump(data, f)
# Чтение
with open("config.plist", "rb") as f:
    loaded = plistlib.load(f)
loaded["name"]  # 'MyApp'
# Из строки (bytes)
b = plistlib.dumps({"key": "value"})
plistlib.loads(b)  # {'key': 'value'}
```

**XML: xml.etree.ElementTree, xml.dom, xml.sax**

- [ ] **xml.etree.ElementTree** — **парсинг и построение** XML: **ET.parse(file)** — дерево **Element**; **root.find('tag')**, **root.findall('.//tag')**, **root.iter('tag')**; **elem.text**, **elem.attrib**; **ET.fromstring(s)** — из строки; **ET.Element('tag', attrib={})** — построение дерева; **ET.dump(elem)** — отладочный вывод. См. также §15h для углублённого разбора.

**Пример xml.etree.ElementTree**

```python
import xml.etree.ElementTree as ET
# Парсинг из файла
tree = ET.parse("config.xml")
root = tree.getroot()
# Парсинг из строки
root = ET.fromstring("<root><a>1</a><b>2</b></root>")
root.find("a").text
root.findall(".//item")
for elem in root.iter("tag"):
    print(elem.attrib, elem.text)
# Построение
root = ET.Element("root", attrib={"id": "1"})
child = ET.SubElement(root, "child")
child.text = "value"
ET.dump(root)
```
- [ ] **xml.dom** — API в стиле **DOM** (Document Object Model): дерево узлов (Document, Element, Text и т.д.), методы **getElementsByTagName**, **createElement**. Тяжелее по памяти и по коду, чем ElementTree; используют при необходимости DOM-модели.
- [ ] **xml.sax** — **потоковый** парсинг (SAX): обработчики событий (startElement, endElement, characters). Экономия памяти при огромных файлах; сложнее для произвольного обхода дерева.

**GUI и графика: tkinter, turtle**

- [ ] **tkinter** — биндинги к **Tk**: кроссплатформенный GUI (окна, кнопки, метки, поля ввода, списки, меню, canvas для рисования). **tkinter.Tk()** — главное окно; **tkinter.Button(parent, text='...', command=callback)** — кнопка; **.pack()**, **.grid()**, **.place()** — геометрия. **Применения:** десктоп-приложения, простые утилиты с окнами, обучение GUI.
- [ ] **turtle** — **образовательная** графика: «черепашка» движется по экрану и оставляет след. **turtle.forward(d)**, **turtle.left(angle)**; **turtle.penup()**, **turtle.pendown()**; **turtle.color()**, **turtle.fillcolor()**. Работает поверх **tkinter**. **Применения:** обучение программированию (циклы, функции), простые визуализации.

---

