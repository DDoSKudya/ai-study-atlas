[← Назад к индексу части III](index.md)

## Частые сценарии и решения (stdlib)

Ниже — типичные задачи и рекомендуемые средства stdlib.

- **Парсинг аргументов CLI:** **argparse**. Создать **ArgumentParser()**, **add_argument** для позиционных и опциональных аргументов, **parse_args()**. Поддержка **nargs**, **choices**, **action='store_true'**, подсказки **--help** из описаний.
- **Чтение/запись JSON:** **json.load(fp)** / **json.dump(obj, fp)** для файлов; **json.loads(s)** / **json.dumps(obj)** для строк. Для кастомных типов — **default** и **object_hook** или наследование **JSONEncoder**/ **JSONDecoder**.
- **Логирование:** **logging.basicConfig(level=..., format=...)** один раз при старте; **getLogger(**name**)** в модулях; **logger.info()**, **logger.error()** и т.д. Уровни: DEBUG, INFO, WARNING, ERROR, CRITICAL. Для вывода в файл — **FileHandler**; для ротации — **RotatingFileHandler**.
- **Запуск внешней команды и получение вывода:** **subprocess.run(cmd, capture_output=True, text=True, timeout=N)**. Результат — **CompletedProcess** с **.returncode**, **.stdout**, **.stderr**. **check=True** — исключение при ненулевом коде. Для интерактивного ввода/вывода — **subprocess.Popen** и **communicate()**.
- **Временный файл/каталог:** **tempfile.NamedTemporaryFile(delete=False)** или **tempfile.TemporaryDirectory()** как контекстный менеджер — файл/каталог удаляются при выходе из **with**. **tempfile.gettempdir()** — каталог для временных файлов по умолчанию.
- **Хеш от строки или файла:** **hashlib.sha256(data).hexdigest()**; для файла — читать блоками и **hasher.update(chunk)**. Для паролей и токенов — **secrets.token_hex()**, **secrets.token_urlsafe()** (не **random**).
- **Проверка «если файл существует — прочитать, иначе — значение по умолчанию»:** **Path(p).read_text() if Path(p).exists() else default** или **try: return Path(p).read_text(); except FileNotFoundError: return default**.
- **Рекурсивно удалить каталог:** **shutil.rmtree(path)** (осторожно: без корзины). **pathlib:** **for f in Path(path).rglob('\*'): f.unlink()** затем **Path(path).rmdir()** или по-прежнему **shutil.rmtree(path)**.

---

## 15. Прочие важные модули stdlib

Краткий перечень модулей, которые чаще всего нужны в повседневной разработке. Подробности — в §7a и в указанных подразделах.

- [ ] **argparse** — **парсинг аргументов CLI**: флаги (**--verbose**), опции со значением (**--output file**), позиционные аргументы, подкоманды; автогенерация **--help** и сообщений об ошибках. Альтернативы: **getopt** (минимальный), **optparse** (устаревший).
- [ ] **logging** — **логирование**: уровни (DEBUG, INFO, WARNING, ERROR, CRITICAL), **getLogger(**name**)** в модулях, **handlers** (FileHandler, RotatingFileHandler), **formatters**; **basicConfig()** один раз при старте.
- [ ] **json** — **сериализация/десериализация JSON**: **load**/ **loads**, **dump**/ **dumps**; для кастомных типов — **default** и **object_hook** или свой **JSONEncoder**/ **JSONDecoder**.
- [ ] **re** — **регулярные выражения**: **compile**, **match**, **search**, **findall**, **finditer**, **sub**; группы, именованные группы, флаги (§15b).
- [ ] **os**, **os.path** — **переменные окружения** (**os.environ**, **os.getenv()**), список каталогов (**listdir**, **scandir**), **walk**, **mkdir**, **remove**, **chmod**; **os.path.join**, **os.path.abspath**, **os.path.exists** (в новом коде предпочтителен **pathlib**).
- [ ] **shutil** — **копирование**, **перемещение**, **удаление** файлов и деревьев (**copy**, **copytree**, **rmtree**); **shutil.which(cmd)** — поиск исполняемого файла в PATH.
- [ ] **getpass** — **ввод пароля** без эха в терминале (**getpass.getpass()**); **getpass.getuser()** — имя текущего пользователя.
- [ ] **subprocess** — **запуск процессов**: **run()** (высокоуровневый, ждать завершения), **Popen** (низкоуровневый); **capture_output**, **text**, **timeout**, **check** (§15c).
- [ ] **threading** — **потоки** (GIL: один поток выполняет байткод); **multiprocessing** — **процессы** (параллельность по ядрам). Очереди: **queue.Queue** (потоки), **multiprocessing.Queue** (процессы).
- [ ] **concurrent.futures** — **ThreadPoolExecutor** (пул потоков), **ProcessPoolExecutor** (пул процессов); **submit()**, **map()**, **Future.result()**; не нужно вручную создавать потоки/процессы и очереди.
- [ ] **tempfile** — **временные файлы и каталоги**: **NamedTemporaryFile**, **TemporaryDirectory** (контекстные менеджеры — удаление при выходе); **gettempdir()**, **mkstemp()**.
- [ ] **hashlib** — **хеши** (md5, sha256, blake2b и др.): **hasher.update(chunk)** для потоковой обработки; **secrets** — **криптостойкие** случайные (**token_hex()**, **token_urlsafe()**); для паролей и токенов не использовать **random**.
- [ ] **random** — **псевдослучайные** числа (не для криптографии): **random()**, **randint**, **choice**, **shuffle**; **seed()** для воспроизводимости.
- [ ] **enum** — **перечисления**: именованные константы (**State.PENDING**), **Enum**, **IntEnum**, **Flag**, **auto()** (§15a0).

---

## 15a0–15h. Углублённые и дополнительные модули

### 15a0. enum — углублённо

**Что такое enum и зачем**

- [ ] **enum** — модуль **перечислений (enumeration)**: набор именованных констант с уникальными значениями. Используется для статусов, кодов операций, вариантов выбора и т.д. Вместо «магических» чисел или строк (**state = 1**, **role = 'admin'**) — **State.PENDING**, **Role.ADMIN**: читаемо, меньше опечаток, типизация и автодополнение в IDE.

**Базовый Enum**

- [ ] **Enum** — базовый класс. Члены объявляются как атрибуты класса с уникальными значениями; у каждого члена есть **name** (имя атрибута) и **value** (значение). **IntEnum** — наследует **int**; члены сравнимы с числами (**Member == 1**). **StrEnum** (3.11+) — наследует **str**; **str(Member)** возвращает значение без явного **.value**; удобно для API и логов.
- [ ] **auto()** — автоматическое присвоение значений: для **Enum** — целые с 1; для **Flag** — степени двойки. **@enum.unique** — декоратор класса: все **value** должны быть уникальны; иначе **ValueError** при создании класса.
- [ ] Итерация по членам: **for m in EnumClass** (порядок объявления). Проверка членства: **member in EnumClass** (по идентичности). Доступ по имени: **EnumClass['NAME']** (при отсутствии — **KeyError**). Доступ по значению: **EnumClass(value)** (при отсутствии — **ValueError**).

**Flag и IntFlag**

- [ ] **Flag**, **IntFlag** — перечисления **битовых флагов**; комбинируются операциями **|** (объединение), **&** (пересечение), **^** (симметричная разность), **~** (инверсия). **IntFlag** наследует **int**; можно сравнивать с числом. **Flag** — только между членами. Проверка вхождения: **flag in combination** (оператор **in** для комбинации флагов).

**Примеры**

```python
from enum import Enum, auto, unique

@unique
class State(Enum):
    PENDING = auto()   # 1
    RUNNING = auto()   # 2
    DONE = auto()      # 3

State.PENDING.name   # 'PENDING'
State.PENDING.value  # 1
list(State)          # [State.PENDING, State.RUNNING, State.DONE]
State['PENDING']     # State.PENDING
State(2)             # State.RUNNING
```

```python
from enum import IntFlag

class Perm(IntFlag):
    R = 4
    W = 2
    X = 1

rw = Perm.R | Perm.W
Perm.R in rw   # True
rw & Perm.X    # Perm.X if X in rw else 0
```

### 15b. Регулярные выражения (re)

**Что такое и зачем**

- [ ] **re** — **регулярные выражения**: поиск и замена подстрок по **паттерну** (шаблону). **Применения:** валидация (email, телефон), извлечение полей из текста (логи, HTML), замена по шаблону, разбор простых форматов. **re.compile(pattern, flags)** — скомпилированный паттерн; **быстрее** при многократном использовании (паттерн разбирается один раз). **re.match(pattern, string)** — совпадение **с начала** строки; **re.search(pattern, string)** — первое совпадение **где угодно** в строке; **re.fullmatch(pattern, string)** — совпадение **всей** строки.
- [ ] **re.findall(pattern, string)** — список всех совпадений (или списков групп при наличии групп); **re.finditer(pattern, string)** — итератор объектов **Match**. У **Match**: **.group()**, **.group(0)** — всё совпадение; **.group(1)** — первая группа; **.group('name')** — именованная группа; **.groups()** — кортеж групп; **.groupdict()** — dict именованных групп.
- [ ] **re.sub(pattern, repl, string, count=0)** — замена; **repl** может быть строка (с обратными ссылками **\\1**, **\\g<name>**) или функция **Match → str**; **re.subn** — то же плюс число замен. **re.split(pattern, string)** — разбиение по паттерну.
- [ ] **Флаги:** **re.IGNORECASE** (re.I) — без учёта регистра; **re.MULTILINE** (re.M) — **^** и **$** на границы строк; **re.DOTALL** (re.S) — **.** захватывает перевод строки; **re.VERBOSE** (re.X) — игнорировать пробелы и комментарии в паттерне.
- [ ] **Группы:** **(...)** — нумерованная; **(?P<name>...)** — именованная; **(?P=name)** — обратная ссылка по имени; **\\1**, **\\g<name>** в repl. **Lookahead:** **(?=...)** — положительный; **(?!...)** — отрицательный. **Lookbehind:** **(?<=...)** — положительный; **(?<!...)** — отрицательный.
- [ ] **Модуль regex** (внешний, **pip install regex**) — расширенный движок регулярных выражений: совместим с **re**, плюс **fuzzy matching** (допуск опечаток), **\X** для графемных кластеров (один «видимый» символ), расширенные границы слов и др. **Применения:** нечёткий поиск, разбор текста с опечатками, подсчёт «символов» для пользователя (grapheme).

**Примеры паттернов**

| Паттерн          | Описание                            | Пример совпадения   |
| ---------------- | ----------------------------------- | ------------------- |
| **\d+**          | Одна или более цифр                 | "123", "0"          |
| **\w+**          | Буквы, цифры, \_                    | "hello", "a1"       |
| **\s+**          | Пробельные символы                  | " ", "\\t\\n"       |
| **.**            | Любой символ (кроме \\n без re.S)   | "a", " "            |
| **^**            | Начало строки (или строки при re.M) | —                   |
| **$**            | Конец строки (или строки при re.M)  | —                   |
| **[a-z]**        | Один символ из набора               | "a", "z"            |
| **(?P<num>\d+)** | Именованная группа                  | "42" → group('num') |

### 15c0. Системные вызовы и ОС

**Что такое и зачем**

- [ ] При работе с файлами, сокетами, процессами ошибки ОС (errno) превращаются в иерархию **OSError**: **FileNotFoundError** (ENOENT), **PermissionError** (EACCES), **TimeoutError**, **ConnectionError** и др. Это позволяет ловить конкретный тип (**except FileNotFoundError**) или общий (**except OSError**); у исключения есть атрибуты **.errno**, **.strerror**, **.filename** (где применимо). **Применения:** разная обработка «файл не найден» и «доступ запрещён»; повтор при **EINTR** (прерванный системный вызов).
- [ ] **os** оборачивает системные вызовы (open, stat, read, write и т.д.); при прерывании сигналом часть вызовов может вернуть **InterruptedError** (EINTR) — в таком случае вызов повторяют. **signal.siginterrupt(signum, flag)** — при **flag=True** системные вызовы после обработчика сигнала **signum** будут прерваны с EINTR; при **False** — вызовы перезапускаются. Для **SIGINT** (Ctrl+C) по умолчанию **siginterrupt(SIGINT, True)** — вызовы прерываются, что позволяет корректно выйти из блокирующего read/accept.

### 15c. subprocess

- [ ] **subprocess.run(args, capture_output=False, text=False, timeout=None, check=False, ...)** — высокоуровневый вызов: запускает процесс, ждёт завершения, возвращает **CompletedProcess**. **args** — список аргументов (рекомендуется) или строка при **shell=True**. **capture_output=True** — перехватить stdout и stderr (иначе они наследуются от родителя). **text=True** — stdout/stderr как **str** (иначе **bytes**). **timeout=N** — прервать через N секунд; **TimeoutExpired**. **check=True** — выбросить **CalledProcessError** при ненулевом **returncode**. Атрибуты результата: **.returncode**, **.stdout**, **.stderr**, **.args**.
- [ ] **subprocess.Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE, ...)** — низкоуровневый: процесс запускается сразу, возвращается объект **Popen**. **process.communicate(input=None)** — отправить **input** в stdin, дождаться завершения, вернуть **(stdout_data, stderr_data)**. **process.wait(timeout=None)** — только ждать завершения. **process.returncode** — код возврата (None пока процесс не завершён).
- [ ] **subprocess.PIPE** — специальное значение: создать канал для stdin/stdout/stderr. **subprocess.DEVNULL** — перенаправить в **/dev/null** (игнорировать). **subprocess.STDOUT** — объединить stderr с stdout.
- [ ] **shell=True:** команда выполняется через shell (**/bin/sh** на Unix, **cmd.exe** на Windows). Позволяет использовать пайпы, перенаправления, переменные окружения в строке. **Риск:** при подстановке пользовательского ввода возможна **инъекция команд**. Предпочитать **shell=False** и передавать **list** аргументов; для пайпов использовать несколько **Popen** и связывать их вручную или **subprocess.run(..., shell=True)** только с доверенной строкой.
- [ ] **env**, **cwd** — окружение и рабочий каталог процесса. **check=True** — при ненулевом коде **run** выбросит **CalledProcessError** (атрибуты **returncode**, **cmd**, **output**, **stderr**). **TimeoutExpired** — при **timeout** в **run** или **communicate**.

**Пример run**

```python
import subprocess
r = subprocess.run(["echo", "hello"], capture_output=True, text=True)
r.stdout   # "hello\n"
r.returncode  # 0
r = subprocess.run(["python", "-c", "exit(1)"], check=True)  # CalledProcessError
```

**Пример Popen и communicate**

```python
p = subprocess.Popen(["cat"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
out, err = p.communicate(input="hello")
out  # "hello"
```

### 15d. Unicode: за пределами encode/decode

- [ ] **unicodedata.normalize(form, s)** — **нормализация** Unicode. **NFC** (каноническая композиция) — предпочтительная форма для хранения и сравнения: составные символы собраны в один code point (например, **é** как U+00E9). **NFD** (каноническая декомпозиция) — разложенные: **é** как **e** + combining acute (U+0065 U+0301). **NFKC/NFKD** — совместимостная композиция/декомпозиция: объединяют совместимые варианты (например, **½** и **1⁄2**); полезны для поиска и сортировки, но могут менять внешний вид. Для отображения и сравнения строк обычно используют **NFC**; для поиска без учёта вариантов начертания — **NFKC** с осторожностью.
- [ ] **Grapheme clusters (графемные кластеры):** один **видимый** символ может состоять из нескольких code points (например, **é** = e + accent; эмодзи флагов **🇷🇺** = региональные индикаторы; эмодзи с тоном кожи). **len(s)** возвращает число **code points**, а не видимых символов. Для разбиения по «символам» с точки зрения пользователя нужны библиотеки (например, **grapheme**) или **unicodedata** с учётом границ графем.
- [ ] **Bidirectional (bidi):** смешение LTR (слева направо) и RTL (справа налево) в одной строке (арабский, иврит). Логический порядок символов может отличаться от порядка отображения. Для корректного отображения может понадобиться библиотека (например, **python-bidi**).
- [ ] **Surrogate pairs** в UTF-16: символы вне BMP (U+10000 и выше) кодируются парой 16-битных суррогатов. В Python **str** хранит code points; при записи в UTF-16 (например, в файл или API) суррогатные пары обрабатываются автоматически. **surrogateescape** — обработчик ошибок кодировки: невалидные байты представляются как суррогатные code points в str, что позволяет round-trip произвольных байтов через str без потери данных.

### 15d1. textwrap, difflib

**textwrap — перенос и форматирование текста**

**Что такое и зачем**

- [ ] **textwrap** — **перенос строк** и **форматирование** текста по заданной ширине, удаление/добавление отступов, сокращение с плейсхолдером. **Применения:** вывод в консоль (абзацы по 70 символов), подписи и описания в UI, подготовка текста для email/логов, многострочные строки в коде без лишних отступов (**dedent**).
- [ ] **wrap(text, width=70)** — список строк, каждая не длиннее **width** (перенос по границам слов). **fill(text, width=70)** — одна строка с переносами (эквивалент **'\n'.join(wrap(...))**). **dedent(text)** — убрать **общий** ведущий пробел у всех строк (удобно для тройных кавычек в коде). **indent(text, prefix)** — добавить **prefix** к каждой строке (в т.ч. к пустым, если не **predicate**). **shorten(text, width, placeholder='...')** — обрезать до **width** символов, сохраняя слова; в конец добавляется **placeholder**. **expandtabs(tabsize=8)** — заменить табуляции на пробелы перед переносом.

**difflib (кратко)**

- [ ] **difflib** — **сравнение последовательностей**: **unified_diff()**, **SequenceMatcher()**, **Differ()**; **get_close_matches()** — нечёткое совпадение (автодополнение, исправление опечаток). Подробнее — в §7a (difflib, filecmp).

**Пример textwrap**

```python
import textwrap
s = "  first line\n  second line\n  third"
textwrap.dedent(s)     # "first line\nsecond line\nthird"
textwrap.fill("long " * 20, width=40)  # строки по 40 символов
textwrap.shorten("Hello world", width=8)  # "Hello..."
```

**Пример difflib**

```python
import difflib
difflib.get_close_matches("helo", ["hello", "world", "help"], n=2, cutoff=0.5)
# ['hello', 'help']
list(difflib.unified_diff(["a", "b"], ["a", "x", "b"], lineterm=""))
# ['--- \n', '+++ \n', '@@ -1,2 +1,3 @@\n', '-b\n', '+x\n', '+b\n']
```

### 15e. Buffer protocol и memoryview

**Что такое и зачем**

- [ ] **Buffer protocol** (PEP 3118) — **низкоуровневый** интерфейс доступа к непрерывному блоку памяти. Объекты, его поддерживающие (**bytes**, **bytearray**, **array.array**, **memoryview**), могут передавать данные в C-расширения и обратно **без копирования**. **Применения:** высокопроизводительный обмен данными (сокеты, файлы, numpy-подобные массивы), zero-copy срезы и слайсы.
- [ ] **memoryview(obj)** — **вид на память** объекта, поддерживающего buffer protocol; сам по себе **не копирует** данные. **Срезы** **mv[i:j]** создают **новый memoryview** на той же памяти (zero-copy). **mv.tobytes()** — копия в **bytes**; **mv.tolist()** — список элементов по формату. Атрибуты: **readonly** (только чтение), **format** (например **'B'** для байт, **'i'** для int), **itemsize**, **nbytes**, **ndim**, **shape** (для многомерных). **Применения:** передача куска буфера в сокет/файл без копирования; изменение **bytearray** через срез **memoryview**; обмен с **array.array** и C-структурами. **Граничный случай:** изменение **readonly** memoryview вызывает **TypeError**; для записи нужен изменяемый объект (bytearray, array).

**Пример memoryview**

```python
b = bytearray(b"hello")
mv = memoryview(b)
mv[0]        # 104
mv[1:4].tobytes()  # b'ell'  (без копирования данных)
mv.readonly  # False
mv.nbytes    # 5
# изменение mv меняет исходный b
mv[0] = 72
b            # bytearray(b'Hello')
```

### 15f. Дескриптор **set_name** (3.6+)

- [ ] ****set_name**(self, owner, name)** — вызывается при **создании класса** для каждого дескриптора, объявленного как атрибут класса; **owner** — класс, **name** — имя атрибута. Удобно для дескрипторов: не нужно передавать имя вручную (**LoggedAttribute('x')** → имя **'x'** получаем из **name**). Порядок: при интерпретации **class C: x = Descriptor()** Python вызывает **Descriptor.**set_name**(descriptor, C, 'x')**.

**Пример дескриптора с **set_name****

```python
class LoggedAttribute:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        print(f"Setting {self.name!r} to {value!r}")
        obj.__dict__[self.name] = value

class A:
    x = LoggedAttribute()  # __set_name__ вызывается с name='x'

a = A()
a.x = 10  # печатает: Setting 'x' to 10
```

### 15g. Модуль: **getattr** (PEP 562, 3.7+)

- [ ] **def **getattr**(name)** на уровне **модуля** — вызывается при обращении к **несуществующему** атрибуту модуля. Используется для **ленивой загрузки** (тяжёлые подмодули подгружаются при первом обращении), прокси, обратной совместимости (алиасы имён). **def **dir**()** на уровне модуля — кастомный список атрибутов для **dir(module)** (PEP 562).

**Пример ленивой загрузки в модуле**

```python
# в mypackage/__init__.py
def __getattr__(name):
    if name == "heavy_submodule":
        import mypackage.heavy_submodule as m
        return m
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

# при первом обращении к mypackage.heavy_submodule выполнится import
```

### io — строковые и байтовые буферы

**Что такое и зачем**

- [ ] **io.StringIO(initial_value='')** — **строковый буфер в памяти**: объект с методами **read()**, **write(s)**, **getvalue()**, **seek()**, **readline()** и т.д. Ведут себя как файл, но данные хранятся в памяти. **Применения:** тесты (подмена файла без создания на диске), накопление строки по частям (**write** несколько раз, затем **getvalue()**), парсеры, ожидающие файлоподобный объект.
- [ ] **io.BytesIO(initial_bytes=b'')** — **буфер байт** в памяти; API аналогичен (read/write/getvalue/getbuffer). **Применения:** тесты бинарных протоколов, сериализация в память (pickle, zip), передача «файла» по API без диска. **.getbuffer()** возвращает **memoryview** на буфер (без копирования).

**Пример StringIO и BytesIO**

```python
import io
# Накопление вывода
buf = io.StringIO()
buf.write("Hello ")
buf.write("world")
buf.getvalue()   # "Hello world"
buf.seek(0)
buf.read()       # "Hello world"

# BytesIO для pickle в память
bio = io.BytesIO()
pickle.dump(obj, bio)
bio.seek(0)
pickle.load(bio)
```

- [ ] **io.TextIOWrapper**, **io.BufferedIOBase**, **io.RawIOBase** — иерархия потоков: **open()** в текстовом режиме возвращает **TextIOWrapper** (поверх буфера и низкоуровневого потока); в бинарном — **BufferedReader**/ **BufferedWriter**. **BufferedIOBase.readinto(buffer)** — zero-copy чтение в заранее выделенный буфер (bytes-like). **open()**: **buffering** (размер буфера), **newline** (универсальные переводы строк при записи/чтении), **errors** (обработка ошибок кодировки); различие текстового (`'r'`/`'w'`) и бинарного (`'rb'`/`'wb'`) режима.

### decimal, fractions, statistics — числовая модель (углублённо)

**Что такое и зачем**

- [ ] **decimal.Decimal** — **точная десятичная** арифметика: числа представляются в десятичной системе, без ошибок округления float (0.1 + 0.2 в float даёт 0.30000000000000004). **Применения:** финансы (суммы, проценты), учёт, любые задачи, где важна точность в десятичной системе. **getcontext()** — глобальный контекст (точность, режим округления); **ROUND_HALF_UP** (школьное округление), **ROUND_HALF_EVEN** (banker's rounding). **decimal.localcontext(ctx)** — временно подменить контекст внутри блока.
- [ ] **Decimal.quantize(exp)** — округление до заданной **экспоненты** или другого Decimal (например **Decimal('0.01')** — до копеек). **Decimal(str)** — создавать из **строки** (**Decimal('0.1')**), не из float, иначе переносятся погрешности float.
- [ ] **decimal vs float:** float — IEEE 754, **двоичное** представление; 0.1 и 0.2 в float не представимы точно, накапливается ошибка. decimal — **десятичная** модель; для денег и человеко-читаемых дробей предпочтителен decimal.
- [ ] **math.nextafter(x, y)** — следующий float после **x** в направлении **y**; **math.ulp(x)** — единица в последнем разряде; **math.copysign(x, y)** — **x** со знаком **y**. **Применения:** граничные тесты, сравнения с допуском.
- [ ] **fractions.Fraction** — **точные рациональные** числа (числитель/знаменатель). **Fraction(0.1)** ≠ **Fraction(1, 10)** из-за представления 0.1 в float; создавать из **строки**: **Fraction('0.1')** или **Fraction(1, 10)**. **Применения:** символьная арифметика дробей без потери точности.
- [ ] **math.fsum(iterable)** — **компенсированная** сумма для float; уменьшает накопленную ошибку округления по сравнению с **sum()**. **Применения:** суммирование большого числа float (научные расчёты).
- [ ] **numbers** — ABC для числовой иерархии: **Number** → **Complex** → **Real** → **Rational** → **Integral**; для реализации своих числовых типов и аннотаций (**def f(x: Real)**).
- [ ] **int** неограниченной точности: внутренне массив «цифр» в большой базе; **sys.int_info** — параметры. **statistics** — **mean**, **median**, **mode**, **stdev**, **variance**; **StatisticsError** при пустой выборке или несовместимых типах.

**Пример decimal**

```python
from decimal import Decimal, getcontext
getcontext().prec = 4
Decimal('0.1') + Decimal('0.2')   # Decimal('0.3')
(Decimal('1') / Decimal('3')).quantize(Decimal('0.01'))  # Decimal('0.33')
```

### struct, array — бинарные данные

**Что такое и зачем**

- [ ] **struct.pack(fmt, \*values)** — упаковка Python-значений в **bytes** по формату; **struct.unpack(fmt, buffer)** — распаковка из buffer (bytes, bytearray, memoryview) в **кортеж**. **fmt** задаёт порядок байт и тип каждого поля: **>** (big-endian), **<** (little-endian), **=** (native); **i** (int), **f** (float), **d** (double), **s** (bytes фиксированной длины), **?** (bool). **struct.calcsize(fmt)** — размер результата в байтах. **Применения:** бинарные протоколы, заголовки файлов, обмен с C.
- [ ] **array.array(typecode, iterable=[])** — **компактный** массив однотипных чисел; **typecode** задаёт тип (**b**, **i**, **f**, **d** и др.); **array.typecodes** — строка доступных кодов. Методы как у list (append, extend, срезы); **.tobytes()**, **.frombytes(b)** — обмен с bytes. **Применения:** большие числовые массивы (меньше памяти, чем list), обмен с C через буферный протокол.

**Пример struct и array**

```python
import struct, array
# Упаковка/распаковка
data = struct.pack(">i f", 42, 3.14)   # big-endian int + float
struct.unpack(">i f", data)             # (42, 3.14)
# array
a = array.array('i', [1, 2, 3])
a.tobytes()   # b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
```

### collections.abc — ABC для контейнеров

**Что такое и зачем**

- [ ] **collections.abc** — **абстрактные базовые классы** для интерфейсов контейнеров и итерации. **Iterable** (**iter**), **Iterator** (**next**), **Generator** — итерация. **Sequence** (**getitem**, **len**), **MutableSequence** (+ **setitem**, insert, pop), **Mapping**, **MutableMapping**, **Set**, **MutableSet**, **Collection** (**contains**, **iter**, **len**). **Callable**, **Container** (**contains**), **Sized** (**len**), **Hashable**. **Awaitable**, **AsyncIterator**, **AsyncGenerator**. **Reversible**; **Buffer** (3.12+). **Применения:** type hints (**def f(x: Sequence[int])**), проверка интерфейса (**isinstance(x, MutableMapping)**), документирование контракта без жёсткого наследования.

### sys, platform, errno

**Что такое и зачем**

- [ ] **sys** — доступ к **переменным интерпретатора** и окружению выполнения: версия Python, путь поиска модулей, стандартные потоки, лимиты, загруженные модули. **Применения:** проверка версии (**sys.version_info >= (3, 10)**), отладка (**sys.getsizeof**, **getrefcount**), изменение поведения (**sys.path**, **sys.stdout**), выход с кодом (**sys.exit(1)**).
- [ ] **sys.version_info** — кортеж **(major, minor, micro)**; проверка: **sys.version_info >= (3, 10)** или **sys.version_info.major == 3**. **sys.getsizeof(obj)** — приблизительный размер объекта в байтах (только сам объект, без вложенных); **sys.getrefcount(obj)** — число ссылок (только CPython, для отладки). **sys.setrecursionlimit(n)**, **sys.getrecursionlimit()** — лимит глубины стека; при превышении — **RecursionError**; увеличивать осторожно (риск переполнения стека). Хвостовая рекурсия в Python **не** устраняется.
- [ ] **sys.modules** — dict загруженных модулей (имя → модуль); **sys.path** — список каталогов для поиска модулей (**import**). **sys.argv** — аргументы командной строки (**argv[0]** — имя скрипта). **sys.exit(code)** — завершить процесс с кодом **code** (0 — успех). **sys.stdout**, **sys.stderr**, **sys.stdin** — стандартные потоки; подмена для тестов (**io.StringIO**) или перенаправления вывода.
- [ ] **platform.system()** — **'Linux'**, **'Windows'**, **'Darwin'** и т.д.; **platform.machine()** — архитектура (**'x86_64'**, **'arm64'**); **platform.python_implementation()** — **'CPython'**, **'PyPy'** и т.д. **errno** — константы кодов ошибок ОС (**errno.ENOENT**, **errno.EACCES**); **except OSError as e: if e.errno == errno.ENOENT: ...**

### Ограничения и границы реализации

**Что такое и зачем**

- [ ] Стандартная библиотека и CPython накладывают **ограничения** на размер структур, глубину рекурсии и длину выражений. Знание границ помогает избежать **RecursionError**, **OverflowError** и падений компилятора при экстремальных данных.
- [ ] **sys.getrecursionlimit()** — типично около **1000**; при каждом вызове функции стек растёт; при достижении лимита — **RecursionError**. **sys.setrecursionlimit(n)** увеличивает лимит, но при слишком большом **n** возможен переполнение стека ОС (краш). **Хвостовая рекурсия** в Python **не** оптимизируется — глубокую рекурсию заменяют циклом или явным стеком.
- [ ] **sys.maxsize** — максимальное значение для **индексов** и **длины** последовательностей (тип **Py_ssize_t** в C). На 64-bit обычно **2⁶³−1**; на 32-bit — **2³¹−1**. **len(list)** и срезы не могут превышать это значение.
- [ ] **Глубина вложенности** выражений в AST ограничена (компилятор/парсер имеют лимит на вложенность скобок и конструкций); очень длинные строковые литералы или списки аргументов могут вызвать ошибку компиляции или долгий разбор.

### traceback, warnings, atexit, faulthandler

**Что такое и зачем**

- [ ] **traceback** — **форматирование стека вызовов** при исключении или текущего стека. **Применения:** логирование полного traceback в **except** (**format_exc()**), кастомные обработчики ошибок, отладочные сообщения. **traceback.format_exc()** — строка с traceback **текущего** исключения (вызывать внутри **except**). **traceback.print_exception(type, value, tb, file=...)** — печать в файл. **traceback.extract_tb(tb)** — список кадров (filename, lineno, name, line) для программной обработки.
- [ ] **warnings** — механизм **предупреждений** без прерывания выполнения. **warnings.warn(message, category=UserWarning, stacklevel=1)** — выдать предупреждение; **stacklevel** — откуда считать кадр (для обёрток). **warnings.filterwarnings(action, ...)** — глобальный фильтр (**'ignore'**, **'error'**, **'always'** и т.д.). **warnings.catch_warnings(record=True)** — контекстный менеджер для временного подавления или записи предупреждений. Категории: **DeprecationWarning** (по умолчанию скрыт в ****main**** в 3.2+), **FutureWarning**, **UserWarning**. Для пометки устаревшего API: **warnings.warn('Use new_api()', DeprecationWarning, stacklevel=2)**.
- [ ] **atexit** — **регистрация функций** при **нормальном** завершении интерпретатора. **atexit.register(func, \*args, **kwargs)** — вызвать **func(\*args, **kwargs)** при выходе (в обратном порядке регистрации). **Не вызывается** при **kill -9**, падении процесса (segfault) или **os.\_exit()**. **Применения:** закрытие соединений, сброс кеша на диск, финальная статистика.
- [ ] **faulthandler** — **вывод traceback** при фатальных сбоях (segfault, abort в C-расширениях), когда обычный **except** не срабатывает. **faulthandler.enable()** — включить перехват SIGSEGV/SIGABRT и вывод стека в stderr; **faulthandler.dump_traceback(file)** — принудительно вывести текущий стек в файл. **Применения:** отладка падений интерпретатора, диагностика в продакшене (логировать в файл при старте).

### importlib.resources, importlib.metadata (3.8+)

**Что такое и зачем**

- [ ] **importlib.resources** — доступ к **файлам внутри пакета** (данные, шаблоны, конфиги) без привязки к ****file**** и без предположений о том, откуда пакет загружен (zip, каталог). **Применения:** загрузка ресурсов из своего пакета (**package/data/config.json**), кросс-платформенные пути, работа при упаковке в zip/pex.
- [ ] **importlib.resources.files(package)** — трассируемый объект к «корню» пакета; **.joinpath('data', 'config.json')** — путь к файлу (Traversable); **.read_text()** / **.read_bytes()** — прочитать содержимое. **as_file(traversable)** — контекстный менеджер, дающий **pathlib.Path** (временный каталог при загрузке из zip). **Примечание:** **package** — строка имени пакета или объект модуля (**'mypkg'** или **mypkg**).

**Пример importlib.resources**

```python
from importlib.resources import files
# Прочитать файл из пакета mypkg/data/default.json
pkg = files('mypkg')
data = (pkg / 'data' / 'default.json').read_text(encoding='utf-8')
# Или с временным путём (если нужен Path для стороннего API)
from importlib.resources import as_file
with as_file(pkg / 'data') as data_dir:
    path = data_dir / 'default.json'
    content = path.read_text()
```

- [ ] **importlib.metadata** — **метаданные установленных пакетов** (версия, entry points, зависимости) без запуска пакета. **Применения:** проверка версии зависимости, обнаружение плагинов по entry points, консольные скрипты (**console_scripts**).
- [ ] **importlib.metadata.version('package')** — строка версии установленного пакета (**'3.12.0'**); **PackageNotFoundError** если не установлен. **importlib.metadata.requires('package')** — список зависимостей пакета (строки **Requires-Dist**). **entry_points(group='console_scripts')** — итератор **EntryPoint** (**.name**, **.value**, **.load()** — загрузить вызываемый объект). **metadata('package')** — объект **PackageMetadata** (Metadata 2.x); **.get('Requires-Dist')** и т.д.

### tomllib (3.11+), graphlib (3.9+), functools.cache, zip(strict)

**Что такое и зачем**

- [ ] **tomllib** — парсинг **TOML** (Tom's Obvious Minimal Language): конфиги с секциями **[section]**, ключами **key = value**, вложенными таблицами. **tomllib.loads(s)** — из строки; **tomllib.load(fp)** — из файла (бинарный режим). Возвращает **dict** (вложенные dict для таблиц). **Только чтение;** запись TOML — сторонняя библиотека (tomli-w). **Применения:** конфиги проектов (pyproject.toml), настройки приложений.
- [ ] **graphlib.TopologicalSorter** (3.9+) — **топологическая сортировка** ориентированного графа без циклов (DAG). **add(node, \*predecessors)** — добавить узел и его зависимости; **prepare()** — зафиксировать граф; **get_ready()** — кортеж узлов без неподготовленных предшественников; **done(\*nodes)** — пометить узлы выполненными; **is_active()** — есть ли ещё необработанные узлы. Для **простого** случая без параллелизма удобнее **static_order()** — итератор по узлам в топологическом порядке. **Применения:** порядок сборки, планирование задач по зависимостям.

**Пример graphlib.TopologicalSorter**

```python
from graphlib import TopologicalSorter
# Простой случай — static_order()
ts = TopologicalSorter({"C": {"A", "B"}, "B": {"A"}, "A": set()})
list(ts.static_order())   # например ['A', 'B', 'C']

# С пошаговой обработкой (get_ready / done)
ts = TopologicalSorter()
ts.add("C", "A", "B"); ts.add("A"); ts.add("B", "A")
ts.prepare()
order = []
while ts.is_active():
    ready = ts.get_ready()
    order.extend(ready)
    ts.done(*ready)
# order — один из допустимых порядков
```

- [ ] **@functools.cache** (3.9+) — **неограниченный** кеш (эквивалент **lru_cache(maxsize=None)**): все результаты сохраняются, вытеснения нет. **zip(a, b, strict=True)** (3.10+) — как **zip**, но при **разной** длине итераторов выбрасывается **ValueError**; без **strict** короткий итератор обрезает результат без предупреждения.

### 15h. Дополнительные модули (архивы, XML, i18n)

**Архивы и сжатие**

**Что такое и зачем**

- [ ] **zipfile** — чтение и создание **ZIP-архивов**: несколько файлов в одном, сжатие по отдельности. **ZipFile(path, 'r'/'w'/'a'/'x')** — открыть архив; **namelist()** — список имён; **read(name)** — прочитать файл в bytes; **extract(member, path)** / **extractall(path)** — извлечь; **write(filename, arcname)** / **writestr(arcname, data)** — добавить. **Применения:** распаковка скачанных архивов, создание дистрибутивов, чтение .docx/.xlsx (ZIP с XML внутри). **Безопасность:** при **extractall** проверять имена на path traversal.
- [ ] **tarfile** — чтение и создание **TAR**-архивов (.tar, .tar.gz, .tar.bz2, .tar.xz). **tarfile.open(path, 'r'/'w'/'a'/'x', ...)** — режимы **'r:gz'**, **'w:gz'** для gzip; **getmembers()**, **extractall()**, **add()**. **Применения:** распаковка исходников (.tar.gz), бэкапы.
- [ ] **gzip**, **bz2**, **lzma** — сжатие **одного потока**: **open(path, 'rb'/'wb')** как у файла; **compress(data)** / **decompress(data)** для bytes. **zlib** — низкоуровневое сжатие (**compress**/ **decompress**). **Применения:** сжатие логов, ответов HTTP (gzip), обмен сжатыми данными.

**XML и HTML**

**Что такое и зачем**

- [ ] **xml.etree.ElementTree** — **парсинг и построение** XML: **ET.parse(path)** / **ET.fromstring(s)** — дерево элементов; у элемента **find(tag)**, **findall(tag)**, **iter(tag)**, **get(attr)**, **text**, **attrib**. **Применения:** конфиги в XML, API-ответы, обмен данными. **xml.dom**, **xml.sax** — альтернативы (DOM — дерево в памяти, SAX — потоковый парсинг).
- [ ] **html.parser.HTMLParser** — потоковый парсинг HTML (подкласс с **handle_starttag**, **handle_endtag**, **handle_data**); **html.escape(s)** — экранирование для HTML (XSS); **html.unescape(s)** — обратно. **Применения:** извлечение ссылок/текста из HTML, безопасная вставка пользовательского ввода в разметку.

**Интернационализация (i18n)**

**Что такое и зачем**

- [ ] **gettext** — **перевод строк** по каталогам сообщений (.po/.mo): **gettext.translation(domain, localedir, languages)** загружает каталог; **\_.gettext(msg)** или **\_(msg)** — переведённая строка для текущей локали. **Применения:** мультиязычные приложения, локализация интерфейса.
- [ ] **locale** — **локаль ОС** (язык, форматы чисел и дат): **locale.getlocale()**, **locale.setlocale(category, locale)**; **locale.format_string(fmt, val)** — форматирование чисел по локали (разделитель тысяч и т.д.). **Применения:** вывод чисел и дат в формате пользователя.

**Прочие утилиты**

- [ ] **http.server** — **HTTPServer**, **BaseHTTPRequestHandler**; **SimpleHTTPRequestHandler** раздаёт файлы из каталога. Запуск: **python -m http.server 8000**. Только для разработки; для продакшена — gunicorn, nginx и т.д.
- [ ] **email** — парсинг и построение MIME-сообщений; **mimetypes.guess_type(filename)** — MIME по расширению.
- [ ] **sched** — **планировщик событий** (очередь с приоритетом по времени): **scheduler.enter(delay, priority, func, args)**; **scheduler.run()**.
- [ ] **uuid** — **uuid.uuid4()** (случайный UUID), **uuid.uuid1()** (по времени и MAC), **uuid.uuid3**/ **uuid5** (по namespace и имени).
- [ ] **base64**, **binascii**, **quopri**, **codecs** — кодирование/декодирование (base64, hex, quoted-printable, кодировки).
- [ ] **netrc** — парсинг файла **.netrc** (логин/пароль для FTP и др.). **shlex.quote(s)** — экранирование строки для передачи в shell (безопасная подстановка).
- [ ] **fnmatch**, **glob**, **os.walk** — шаблоны имён файлов (**\***, **?**, **\[...\]**) и обход дерева каталогов. **webbrowser.open(url)** — открыть URL в браузере по умолчанию.
- [ ] **ipaddress** — **парсинг и арифметика** IP-адресов (IPv4/IPv6) и подсетей: **ip_address()**, **ip_network()**, проверка вхождения в подсеть, итерация по хостам.
- [ ] **csv** — **DictReader**, **DictWriter**, **Dialect**, **Sniffer** (определение разделителя по образцу). **configparser** — INI-файлы с секциями и **interpolation** (подстановка **%(key)s**).

---

