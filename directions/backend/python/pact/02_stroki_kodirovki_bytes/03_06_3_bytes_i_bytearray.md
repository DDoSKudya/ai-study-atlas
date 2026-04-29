[← Назад к индексу части II](index.md)


## 6.3 bytes и bytearray

### 6.3.1 Индексация и срезы

#### Индексация: возвращается int (важное отличие от Python 2!)

В **Python 3** при индексации **bytes** или **bytearray** **одним индексом** возвращается **целое число** (код байта 0–255), а **не** однобайтовая строка, как в Python 2. Это одно из самых частых мест ошибок при миграции с Py2 на Py3.

```python
b = b'ABC'
b[0]    # 65 (int)
b[1]    # 66 (int)
b[-1]   # 67 (int)
type(b[0])  # <class 'int'>

ba = bytearray(b'ABC')
ba[0]   # 65 (int)
```

**Пошагово: что происходит при b'AB'[0].** (1) Интерпретатор обращается к элементу последовательности `bytes` по индексу 0. (2) Элемент — это **целое число** (код байта в диапазоне 0–255). (3) Возвращается `65` — код латинской буквы A в ASCII.

**Теоретическое обоснование:** `bytes` — последовательность **целых чисел 0–255** (байтов), а не символов. Каждый элемент — это один байт; естественное представление байта как числа — int. В Python 2 `str` был и текстом, и байтами; `b'x'[0]` (или `'x'[0]`) возвращал однобайтовую строку `'x'`. В Python 3 чёткое разделение: **bytes** — байты (int при индексации), **str** — символы (str при индексации).

**Как получить однобайтовый bytes вместо int:** используйте **срез** `b[i:i+1]`:

```python
b = b'AB'
b[0]      # 65 (int)
b[0:1]    # b'A' (bytes, длина 1)
b[0:1][0] # 65 (int) — индексация среза
```

#### Срезы: возвращается bytes или bytearray

При **срезе** тип сохраняется: срез `bytes` даёт `bytes`, срез `bytearray` даёт `bytearray`.

```python
b = b'Hello'
b[0:1]   # b'H'  (bytes)
b[1:4]   # b'ell'
b[:3]    # b'Hel'
b[-2:]   # b'lo'

ba = bytearray(b'Hello')
ba[0:1]  # bytearray(b'H')
ba[1:4]  # bytearray(b'ell')
```

**Граничные случаи срезов:**

```python
b = b'AB'
b[0:0]   # b'' — пустой срез
b[1:0]   # b'' — пустой срез (start > stop)
b[10:20] # b'' — индексы за пределами (не IndexError для среза)
b[:]     # b'AB' — полная копия
```

#### Типичные ошибки при работе с индексацией bytes

```python
# Ошибка: ожидать str при индексации bytes
b = b'AB'
# x = b[0] + " suffix"   # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Правильно: преобразовать в str или использовать срез
char_bytes = b[0:1]   # b'A'
char_str = b[0:1].decode()  # 'A'
# или
char_str = chr(b[0])  # 'A' — если байт в ASCII

# Ошибка: передать int в ord()
ord(b[0])   # TypeError: ord() expected str, got int
chr(b[0])   # 'A' — chr() принимает int
```

---

### 6.3.2 Создание bytes и bytearray

#### Литералы

```python
b'hello'           # bytes
b"hello"
b'''multi
line'''
rb'\n'             # сырой bytes: два символа \ и n

B = bytes([65, 66, 67])   # b'ABC'
BA = bytearray([65, 66, 67])  # bytearray(b'ABC')
```

#### Конструкторы bytes — подробно

**bytes:**  
`bytes([source[, encoding[, errors]]])`

Возможные формы вызова:

| Вызов | Результат |
|-------|-----------|
| `bytes()` | Пустая последовательность `b''` |
| `bytes(n)` | n нулевых байт (n — целое >= 0); `bytes(0)` → `b''` |
| `bytes(iterable_of_ints)` | Последовательность байт из целых 0–255; каждый int — один байт |
| `bytes(str, encoding[, errors])` | Эквивалент `str.encode(encoding, errors)` |
| `bytes(bytes_or_bytearray)` | Копия (для bytes — тот же объект; для bytearray — копия) |

```python
bytes()               # b''
bytes(5)              # b'\x00\x00\x00\x00\x00'
bytes([65, 66, 67])   # b'ABC'
bytes(range(65, 68))  # b'ABC'
bytes('ABC', 'utf-8') # b'ABC'
bytes(b'ABC')         # b'ABC' (тот же объект, bytes неизменяем)

# Ошибки
bytes([256])          # ValueError: bytes must be in range(0, 256)
bytes([-1])           # ValueError: bytes must be in range(0, 256)
bytes('ABC')          # TypeError: string argument without an encoding
bytes([1.0])          # TypeError: 'float' object cannot be interpreted as an integer

# bytes от итератора
bytes(iter([65, 66, 67]))  # b'ABC'
bytes(range(97, 100))      # b'abc'
```

**Граничные случаи bytes(n):**

```python
bytes(0)   # b''
bytes(1)   # b'\x00'
bytes(10)  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
```

**bytearray:**  
`bytearray([source[, encoding[, errors]]])`

Аналогично bytes, но результат — **изменяемый** bytearray. Всегда создаётся новый объект (даже при `bytearray(bytearray(b'x'))` — копия).

**Отличие от bytes при копировании:** `bytes(b'hello')` возвращает тот же объект (bytes неизменяем, копия не нужна); `bytearray(b'hello')` и `bytearray(bytearray(b'hello'))` всегда создают новый bytearray — изменяемость требует изолированной копии при «конструкторе от bytearray».

```python
bytearray()               # bytearray(b'')
bytearray(5)              # bytearray(b'\x00\x00\x00\x00\x00')
bytearray([65, 66, 67])   # bytearray(b'ABC')
bytearray('ABC', 'utf-8') # bytearray(b'ABC')
bytearray(b'ABC')         # bytearray(b'ABC') — копия
```

#### fromhex (class method) — hex-строка в bytes

Создание из hex-строки: каждая **пара** шестнадцатеричных цифр (0–9, a–f, A–F) преобразуется в один байт. Пробелы и переводы строк игнорируются.

```python
bytes.fromhex('48656c6c6f')   # b'Hello' (48='H', 65='e', ...)
bytearray.fromhex('DEADBEEF') # bytearray(b'\xde\xad\xbe\xef')
bytes.fromhex('41')           # b'A'
bytes.fromhex('4142')         # b'AB'
bytes.fromhex('4 1 4 2')      # b'AB' — пробелы игнорируются
```

**Обратное преобразование:** метод `hex()` у bytes/bytearray:

```python
b'Hello'.hex()   # '48656c6c6f'
b'A'.hex()       # '41'
bytes().hex()    # '' — пустая строка
b'\x00\xff'.hex()  # '00ff'
```

**Граничные случаи fromhex:** `bytes.fromhex('')` → `b''`. Нечётное число hex-цифр — `ValueError`. Недопустимые символы (не 0-9, a-f, A-F, пробел) — `ValueError`.

---

### 6.3.3 encode() и decode() — преобразование str↔bytes

#### str.encode(encoding='utf-8', errors='strict') -> bytes

Преобразует строку (последовательность Unicode code points) в байты по заданной кодировке.

**Сигнатура:** `str.encode(encoding='utf-8', errors='strict') -> bytes`

**Теоретическое обоснование:** encode — отображение из пространства Unicode (code points) в пространство байтовых последовательностей. Кодировка задаёт правила этого отображения. Не все code points представимы во всех кодировках: ASCII не может закодировать 'П', Latin-1 — '€' (U+20AC > 255). При непредставимом символе поведение определяется `errors`. Результат — неизменяемый объект bytes, готовый для записи в файл, передачи по сети или хранения.

**Параметры:**
- **encoding** — имя кодировки (например, `'utf-8'`, `'ascii'`, `'cp1251'`); по умолчанию UTF-8
- **errors** — обработка ошибок кодирования (`'strict'`, `'ignore'`, `'replace'`, `'backslashreplace'`, `'namereplace'`, `'xmlcharrefreplace'` и др.)

**Возвращает:** объект `bytes`.

```python
"Привет".encode()              # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
"Привет".encode('utf-8')       # то же
"ABC".encode('ascii')          # b'ABC'
"€".encode('utf-8')            # b'\xe2\x82\xac'
"€".encode('latin-1')          # UnicodeEncodeError: latin-1 не содержит €

# С errors
"€".encode('ascii', errors='replace')   # b'?'
"€".encode('ascii', errors='ignore')    # b''
"€".encode('ascii', errors='backslashreplace')  # b'\\u20ac'
"€".encode('ascii', errors='xmlcharrefreplace') # b'&#8364;'
"€".encode('ascii', errors='namereplace')       # b'\\N{EURO SIGN}'
```

**Таблица errors при encode (кратко):**

| errors | Поведение |
|--------|-----------|
| strict | UnicodeEncodeError |
| ignore | Пропуск непредставимого символа |
| replace | Замена на `?` (байт 0x3F) |
| backslashreplace | `\uNNNN` или `\UNNNNNNNN` |
| xmlcharrefreplace | `&#N;` (десятичный code point) |
| namereplace | `\N{NAME}` (если есть Unicode name) |

**Пошагово: что происходит при "П".encode("utf-8").** (1) Интерпретатор берёт строку `"П"` — один code point U+041F (1055). (2) Кодировка UTF-8: U+041F попадает в диапазон U+0080–U+07FF → 2 байта. (3) Формула UTF-8: `110xxxxx 10xxxxxx`; биты code point распределяются по шаблону. (4) Результат: `0xD0 0x9F`. (5) Возвращается `b'\xd0\x9f'`.

#### bytes.decode(encoding='utf-8', errors='strict') -> str  
#### bytearray.decode(encoding='utf-8', errors='strict') -> str

Преобразует байты в строку (последовательность Unicode code points).

**Сигнатура:** `bytes.decode(encoding='utf-8', errors='strict') -> str`

**Параметры:**
- **encoding** — имя кодировки
- **errors** — обработка ошибок декодирования (`'strict'`, `'ignore'`, `'replace'`, `'surrogateescape'`, `'backslashreplace'` и др.)

**Возвращает:** объект `str`.

```python
b'\xd0\x9f\xd1\x80'.decode('utf-8')   # 'Пр'
b'ABC'.decode('ascii')                 # 'ABC'
b'\xff\xfe'.decode('utf-8')            # UnicodeDecodeError (при strict)
b'\xff\xfe'.decode('utf-8', errors='replace')  # '\ufffd\ufffd'

# decode без аргументов — encoding по умолчанию (UTF-8)
b'Hello'.decode()    # 'Hello'
```

**Пошагово: что происходит при b'\xd0\x9f'.decode("utf-8").** (1) Интерпретатор читает байты `0xD0 0x9F`. (2) Первый байт `0xD0` (11010000) — старшие биты `110` → двухбайтовая последовательность UTF-8. (3) Декодер извлекает биты из обоих байт, собирает code point 1055 (0x041F). (4) Символ U+041F — буква 'П'. (5) Возвращается строка `"П"`.

#### Круг преобразований и правило «границы»

```
str --encode(encoding)--> bytes --decode(encoding)--> str
```

**Правило «декодируй как можно раньше, кодируй как можно позже»:**

- **Внутри приложения** работайте с `str` (Unicode) — единый формат для всего текста
- **На границах** (файл, сеть, внешний API, аргументы командной строки) преобразуйте:
  - **Вход:** байты → str через `decode(encoding)`
  - **Выход:** str → байты через `encode(encoding)`
- Это устраняет путаницу кодировок внутри кода и делает границы явными.

#### Пошагово: полный цикл чтения и записи текстового файла

**Чтение:**
1. `open("file.txt")` — создаётся `TextIOWrapper` с encoding='utf-8' (по умолчанию)
2. `f.read()` — читаются байты из файла через буфер
3. Байты декодируются в str по UTF-8
4. Возвращается str

**Запись:**
1. `open("out.txt", "w")` — создаётся `TextIOWrapper`
2. `f.write(s)` — строка s кодируется в байты по UTF-8
3. Байты записываются в буфер, затем в файл

**Инвариант:** `open(path).read()` → str; `open(path, "w").write(s)` → файл содержит байты `s.encode(encoding)`. При `encoding='utf-8'` и корректных данных: `open(path).read() == s` после `open(path, "w").write(s)`.

#### Пошагово: что происходит при print("Привет") в консоль

1. **print** получает строку `str` — последовательность code points (П, р, и, в, е, т).
2. **sys.stdout** — объект `io.TextIOWrapper`, обёртка над бинарным потоком консоли.
3. **Запись в stdout:** строка кодируется в байты по кодировке `sys.stdout.encoding` (обычно UTF-8 в современных терминалах, или CP1251/CP866 на Windows в зависимости от chcp).
4. Байты передаются в консоль/терминал.
5. Терминал интерпретирует байты по своей кодировке и отображает символы.

**Если консоль использует другую кодировку:** «Привет» в UTF-8 — байты `\xd0\x9f\xd1\x80...`; если консоль ожидает CP1251, те же байты будут интерпретированы как другие символы → «кракозябры». Решение: настроить консоль на UTF-8 (`chcp 65001` в Windows) или явно кодировать перед выводом.

---

### 6.3.4 str.join() — эффективная конкатенация строк

Для склейки нескольких строк в одну **не** используйте конкатенацию в цикле (`s += x`), а метод **`str.join(iterable)`**:

```python
parts = ['a', 'b', 'c']
''.join(parts)    # 'abc'
'; '.join(parts)  # 'a; b; c'
'\n'.join(parts)  # 'a\nb\nc'
', '.join(str(x) for x in [1, 2, 3])  # '1, 2, 3'
```

**Пошагово: что происходит при ''.join(parts).** (1) Метод `join` вызывается у разделителя (здесь пустая строка `''`). (2) Итерабельный объект `parts` перебирается, каждый элемент приводится к строке (если не str). (3) Строки склеиваются: между ними вставляется разделитель (здесь — ничего). (4) Результат — одна строка, возвращается как новый объект.

**Почему join эффективнее конкатенации в цикле:**

- **str неизменяемы:** при `s += x` создаётся **новая** строка (копия `s` + `x`); исходная `s` отбрасывается
- **Квадратичная сложность:** для N элементов выполняется N операций конкатенации; каждая операция `s += x` копирует всю текущую строку (длина растёт: 1, 2, 3, ..., N) — суммарно O(N²) операций
- **join — линейная сложность:** сначала вычисляется общая длина результата, затем выделяется один буфер и заполняется за один проход — O(N)

**Сравнение производительности (упрощённо):**

```python
# Плохо: O(N²)
s = ''
for x in parts:
    s += x

# Хорошо: O(N)
s = ''.join(parts)
```

**Для bytes:**

```python
parts = [b'a', b'b', b'c']
b''.join(parts)   # b'abc'
b'-'.join(parts)  # b'a-b-c'

# Итерабельный из int (0–255)
b''.join(bytes([x]) for x in [65, 66, 67])  # b'ABC'
```

**Граничные случаи join:**

```python
''.join([])       # '' — пустой результат
''.join(['a'])    # 'a' — один элемент, разделитель не вставляется (между 0 пар)
'-'.join([''])    # '' — один пустой элемент
'-'.join(['a', ''])  # 'a-' — разделитель между парами элементов
'-'.join(['', 'a'])  # '-a'
''.join(['a', 'b', 'c'])  # 'abc' — пустой разделитель
repr(''.join)     # join — метод, не функция
```

**Важно:** `str.join(iterable)` — метод вызывается у **разделителя** (sep), а не у собираемых строк. Поэтому `','.join(items)`, а не `items.join(',')`.

---

### 6.3.5 bytearray — изменяемая последовательность байт

**bytearray** — изменяемый аналог **bytes**. Поддерживает те же операции, что и bytes (индексация, срезы, методы decode, find, split и т.д.), плюс **мутирующие** методы и присваивание по индексу/срезу.

#### Мутирующие методы bytearray

| Метод | Сигнатура | Назначение |
|-------|-----------|------------|
| `append` | `append(x)` | Добавить байт `x` (int 0–255) в конец |
| `extend` | `extend(iterable)` | Добавить байты из итерабельного (int 0–255 или bytes-like) |
| `insert` | `insert(i, x)` | Вставить байт `x` в позицию `i` |
| `pop` | `pop([i])` | Удалить и вернуть байт в позиции `i` (по умолчанию последний) |
| `remove` | `remove(x)` | Удалить первое вхождение байта `x`; ValueError если нет |
| `reverse` | `reverse()` | Развернуть последовательность in-place |
| `clear` | `clear()` | Удалить все элементы |

**Присваивание:** `ba[i] = x` (x — int 0–255); `ba[i:j] = iterable` — заменить срез.

```python
ba = bytearray(b'hello')
ba[0] = ord('H')     # bytearray(b'Hello')
ba.append(ord('!'))  # bytearray(b'Hello!')
ba.extend(b'!!')     # bytearray(b'Hello!!!')
ba.pop()             # 33 (код '!'); ba == bytearray(b'Hello!!')
ba.reverse()         # bytearray(b'!!olleH') — in-place
ba.clear()           # bytearray(b'')

# Присваивание среза
ba = bytearray(b'abc')
ba[1:2] = b'XX'      # bytearray(b'aXXc')
```

**Пошагово: что происходит при ba.append(x).** (1) Интерпретатор проверяет, что `x` — целое в диапазоне 0–255 (иначе `ValueError`). (2) Добавляет байт `x` в конец **bytearray**; длина `len(ba)` увеличивается на 1. (3) Объект `ba` тот же (мутация на месте); `append` возвращает `None`.

**Пошагово: что происходит при ba.extend(b'!!').** (1) Аргумент `b'!!'` — итерабельный объект типа bytes. (2) Метод `extend` перебирает каждый элемент итерабельного — здесь байты 0x21, 0x21 (коды '!'). (3) Каждый байт добавляется в конец bytearray; длина увеличивается на 2. (4) Объект `ba` мутируется на месте; `extend` возвращает `None`. (5) Итог: `ba` содержит на 2 байта больше.

**Когда использовать bytearray:**

- Накопление байтов по частям (парсеры, протоколы) — `append`/`extend` эффективнее, чем `bytes + bytes` (которое создаёт новый объект при каждой конкатенации)
- Изменение отдельных байт «на месте» — `ba[i] = x`
- Буферизация ввода-вывода — модифицируемый буфер без лишних копий
- Парсинг бинарных протоколов — можно менять буфер «на лету» без создания промежуточных копий

**Когда использовать bytes:**

- Константные данные, ключи, аргументы функций
- Когда изменение не требуется — bytes неизменяем и hashable (можно использовать как ключ dict)

---

### 6.3.6 Методы bytes и bytearray — полный обзор

bytes и bytearray поддерживают многие методы str (с учётом того, что аргументы и результаты — bytes/bytearray). Специфика: аргументы — bytes/bytearray или int (0–255 для некоторых методов); результаты — bytes/bytearray или int.

#### Таблица методов bytes/bytearray

| Метод | bytes | bytearray | str | Примечание |
|-------|-------|-----------|-----|------------|
| `capitalize`, `center`, `count`, `endswith`, `expandtabs`, `find`, `index` | да | да | да | Аналоги str |
| `join`, `ljust`, `lower`, `lstrip`, `partition`, `replace`, `rfind`, `rindex`, `rjust`, `rpartition`, `rsplit`, `rstrip`, `split`, `splitlines`, `startswith`, `strip`, `swapcase`, `title`, `translate`, `upper`, `zfill` | да | да | да | Аналоги str |
| `removeprefix`, `removesuffix` (3.9+) | да | да | да | Удаление префикса/суффикса |
| `decode` | да | да | нет | bytes/bytearray → str |
| `encode` | нет | нет | да | str → bytes |
| `fromhex` | да (classmethod) | да (classmethod) | нет | hex-строка → bytes |
| `hex` | да | да | нет | bytes → hex-строка |

#### Примеры ключевых методов bytes/bytearray

**find, index, count, in:**

```python
b = b'hello world'
b.find(b'll')      # 2 — индекс первого вхождения
b.find(b'x')       # -1 — не найдено
b.index(b'll')     # 2
b.index(b'x')      # ValueError — index выбрасывает исключение при отсутствии
b.find(b'x')       # -1 — find возвращает -1, не исключение
# Выбор: index — когда отсутствие считается ошибкой; find — когда нужно обработать «не найдено»
b.count(b'l')      # 3
b'l' in b          # True (ищется байт 108, т.е. ord('l'))
b'hello' in b      # True — подпоследовательность
```

**split(sep=None, maxsplit=-1)** и **rsplit** — разбиение по разделителю:

```python
# split(sep=None, maxsplit=-1)
# sep — разделитель (bytes); maxsplit — макс. число разбиений (-1 = все)

b'aa,bb,cc'.split(b',')        # [b'aa', b'bb', b'cc']
b'aa,bb,cc'.split(b',', 1)     # [b'aa', b'bb,cc'] — maxsplit=1, одно разбиение слева
b'aa,bb,cc'.split(b',', 2)     # [b'aa', b'bb', b'cc'] — два разбиения
b'aa,bb,cc'.split(b',', 0)     # [b'aa,bb,cc'] — maxsplit=0: без разбиения, весь объект
b'aa,bb,cc'.split(b',', 100)   # [b'aa', b'bb', b'cc'] — больше разделителей нет

# Пограничные случаи maxsplit
b'a,b,c'.split(b',', 1)        # [b'a', b'b,c'] — только первый sep
b'a,b,c'.split(b',', 2)        # [b'a', b'b', b'c'] — два sep, три части
b'aaa'.split(b'a')             # [b'', b'', b'', b''] — sep по краям и между; 4 пустых
b'aaa'.split(b'a', 1)          # [b'', b'aa'] — одно разбиение: '' + 'aa'
b'aaa'.split(b'a', 2)          # [b'', b'', b'a']
b''.split(b',')                # [b''] — пустая строка → список из одной пустой
b''.split()                    # [] — пустая строка без sep → []
b','.split(b',')               # [b'', b''] — два пустых между разделителем
b',,'.split(b',')              # [b'', b'', b'']
b'  aa  bb  '.split()          # [b'aa', b'bb'] — без sep: по пробельным символам
b'  aa  bb  '.split(None)      # то же
b'  aa  bb  '.split(None, 1)   # [b'aa', b'bb  '] — одно разбиение по пробелам
b'  '.split()                  # [] — только пробелы → пустой список
b' \t\n '.split()              # []
b'a'.split(b',')               # [b'a'] — sep нет → один элемент

# rsplit(sep=None, maxsplit=-1) — разбиение справа
b'aa,bb,cc'.rsplit(b',')       # [b'aa', b'bb', b'cc'] — как split при maxsplit=-1
b'aa,bb,cc'.rsplit(b',', 1)    # [b'aa,bb', b'cc'] — одно разбиение справа
b'path/to/file'.rsplit(b'/', 1)  # [b'path/to', b'file'] — отделить имя файла от пути
b'a,b,c'.rsplit(b',', 1)       # [b'a,b', b'c'] — разбиение с конца
b'aaa'.rsplit(b'a', 1)         # [b'aa', b''] — одно разбиение справа
```

# find(sub[, start[, end]]), rfind(sub[, start[, end]]) — поиск слева и справа
b'hello world'.find(b'll')     # 2 — индекс первого вхождения
b'hello world'.rfind(b'o')     # 7 — последнее 'o' в "world"
b'hello'.rfind(b'l')           # 3 — последнее 'l' в "hello"
b'hello'.find(b'x')            # -1 — не найдено
b'abab'.find(b'ab', 1)         # 2 — поиск начиная с индекса 1
b'ababab'.rfind(b'ab')         # 4 — последнее вхождение "ab"

# partition(sep), rpartition(sep)
b'a=b'.partition(b'=')         # (b'a', b'=', b'b') — всегда три элемента
b'a=b=c'.partition(b'=')       # (b'a', b'=', b'b=c') — разбиение по первому
b'abc'.partition(b'x')         # (b'abc', b'', b'') — sep не найден

# splitlines(keepends=False)
b'line1\nline2\n'.splitlines() # [b'line1', b'line2']
b'line1\nline2\n'.splitlines(keepends=True)  # [b'line1\n', b'line2\n']
b''.splitlines()               # []
```

**strip, lstrip, rstrip** (chars — байты для удаления с краёв; по умолчанию пробельные):

```python
b'  hello  '.strip()        # b'hello'
b'\t\n hello \n'.strip()    # b'hello'
b'xxhelloxx'.strip(b'x')    # b'hello'
b'xyxyhelloxyxy'.strip(b'xy')  # b'hello' — удаляет любой из x,y с краёв
b'xxx'.strip(b'x')          # b'' — всё удалено
b'xyx'.strip(b'xy')         # b'' — strip удаляет все вхождения chars с обоих краёв
b'  \t  '.strip()           # b'' — только пробельные по умолчанию
# strip(chars) — chars интерпретируется как множество: любой символ из chars удаляется с краёв
```

**startswith, endswith** (prefix/suffix может быть tuple — проверка «начинается/заканчивается одним из»):

```python
b'hello'.startswith(b'he')           # True
b'hello'.startswith((b'he', b'ha'))  # True
b'file.py'.endswith((b'.py', b'.txt'))  # True
b'file.py'.endswith(b'.py', 0, 4)    # False — срез b'file' не заканчивается на .py
```

**replace(old, new[, count])** — замена; count — максимальное число замен (по умолчанию все):

```python
b'hello'.replace(b'l', b'L')     # b'heLLo'
b'hello'.replace(b'l', b'L', 1)  # b'heLlo' — одна замена
b'aaa'.replace(b'aa', b'b')      # b'ba' — не перекрывающиеся вхождения
b'aaa'.replace(b'a', b'')        # b'' — удаление
```

**translate(table)** — замена и удаление байт по таблице. Таблица — результат `bytes.maketrans()` или `dict[int, int | None]`.

#### bytes.maketrans — создание таблицы перевода

**Сигнатура:**

```python
bytes.maketrans(from_bytes, to_bytes)           # замена
bytes.maketrans(from_bytes, to_bytes, delete)   # замена + удаление
```

**bytes.maketrans(from, to)** — `from` и `to` должны быть bytes **одинаковой длины**. Каждый байт из `from` заменяется на соответствующий байт из `to` по позиции.

```python
t = bytes.maketrans(b'aeiou', b'AEIOU')
b'hello'.translate(t)   # b'hEllO' — e→E, o→O
b'xyz'.translate(t)     # b'xyz' — байты не из from остаются без изменений
```

**bytes.maketrans(from, to, delete)** — дополнительный аргумент `delete`: байты, которые нужно **удалить** (не включать в результат). `delete` — bytes.

```python
# Замена a→A, b→B, c→C; байт x удаляется
t = bytes.maketrans(b'abc', b'ABC', b'x')
b'abcx'.translate(t)    # b'ABC'
b'xaxbxc'.translate(t)  # b'ABC' — все x удалены, остальные заменены
b'xyz'.translate(t)     # b'yz' — x удалён, y и z без изменений (не в from)
```

**Таблица как dict:** ключ — int (код байта 0–255); значение — int (замена) или `None` (удалить). Байты, отсутствующие в dict, остаются без изменений.

```python
t = {ord(b'a'): ord(b'A'), ord(b'b'): None}  # a→A, b удалить
b'abc'.translate(t)     # b'Ac'
t = {i: i for i in range(256)}  # тождественная замена (ничего не меняет)
```

#### Граничные случаи translate и maketrans

```python
# Пустая таблица — ничего не меняется
b'hello'.translate(bytes.maketrans(b'', b''))  # b'hello'

# Только delete — замена пустая
t = bytes.maketrans(b'', b'', b'aeiou')
b'hello'.translate(t)   # b'hll' — гласные удалены

# from и to разной длины — TypeError
# bytes.maketrans(b'ab', b'A')  # TypeError: make_translation_table() ...

# Байт есть и в from, и в delete — сначала замена (по позиции в from), delete применяется к исходному байту
# Точнее: для каждого байта: если в delete — пропустить; иначе если в from — заменить; иначе оставить
t = bytes.maketrans(b'ab', b'AB', b'b')
b'ab'.translate(t)      # b'A' — b в delete, удаляется; a→A
```

#### Практическое применение translate

```python
# ROT13 (поворот алфавита на 13 позиций)
import string
rot13_from = (string.ascii_lowercase + string.ascii_uppercase).encode()
rot13_to = (string.ascii_lowercase[13:] + string.ascii_lowercase[:13] +
            string.ascii_uppercase[13:] + string.ascii_uppercase[:13]).encode()
rot13_table = bytes.maketrans(rot13_from, rot13_to)
b'hello'.translate(rot13_table)  # b'uryyb'

# Удаление управляющих символов (0x00–0x1F, кроме \t \n \r)
delete_ctrl = bytes(range(32))  # b'\x00\x01...\x1f'
# Исключаем \t(9), \n(10), \r(13)
delete_ctrl = bytes(i for i in range(32) if i not in (9, 10, 13))
t = bytes.maketrans(b'', b'', delete_ctrl)
b'hello\x01world\x02'.translate(t)  # b'helloworld'

# Замена нескольких байт на один (через dict: несколько ключей → одно значение)
t = {ord(b'\r'): ord(b'\n'), ord(b'\t'): ord(b' ')}
b'line1\rline2\t'.translate(t)  # b'line1\nline2 '
```

**hex, fromhex:**

```python
b'Hello'.hex()           # '48656c6c6f'
bytes.fromhex('48656c6c6f')  # b'Hello'
bytearray.fromhex('DEADBEEF')  # bytearray(b'\xde\xad\xbe\xef')
```

**capitalize, title, upper, lower, swapcase:**

```python
b'hello'.capitalize()   # b'Hello' — только первый символ в верхний регистр
b'HELLO'.lower()        # b'hello'
b'hello'.upper()        # b'HELLO'
b'HeLLo'.swapcase()     # b'hEllO' — инверсия регистра
b'hello world'.title()  # b'Hello World' — каждое слово с заглавной
```

**center, ljust, rjust, zfill** (выравнивание и заполнение):

```python
b'hi'.center(6)         # b'  hi  ' — по центру, по умолчанию пробелы
b'hi'.center(6, b'-')   # b'--hi--'
b'hi'.ljust(5)          # b'hi   ' — влево
b'hi'.rjust(5)          # b'   hi' — вправо
b'42'.zfill(5)          # b'00042' — слева нули (для чисел)
b'-42'.zfill(5)         # b'-0042' — минус сохраняется, нули после
```

**expandtabs(tabsize=8)** — замена табуляций пробелами (байт `\t` → tabsize пробелов; позиции табуляции как в текстовом редакторе):

```python
b' a\tb\tc '.expandtabs(4)   # b' a   b   c ' — tab = 4 пробела
b'\t'.expandtabs(8)          # b'        ' — 8 пробелов
b'a\t\tb'.expandtabs(4)      # b'a       b' — вторая табуляция на позиции 8
```

**insert(i, x)** (только bytearray) — вставить байт `x` (int 0–255) в позицию `i`:

```python
ba = bytearray(b'helo')
ba.insert(3, ord('l'))  # bytearray(b'hello') — вставка перед позицией 3
ba.insert(0, ord('!'))  # bytearray(b'!hello') — в начало
ba.insert(len(ba), ord('!'))  # в конец (как append)
```

**remove(x)** (только bytearray) — удалить первое вхождение байта `x` (int 0–255); ValueError если не найден:

```python
ba = bytearray(b'hello')
ba.remove(ord('l'))   # bytearray(b'helo') — удалено первое 'l'
ba.remove(ord('x'))   # ValueError: value not in bytearray
```

**removeprefix, removesuffix** (Python 3.9+):

```python
b'test_file.py'.removeprefix(b'test_')  # b'file.py'
b'file.py'.removesuffix(b'.py')         # b'file'
```

#### Пошагово: что происходит при b'hello'.find(b'll')

1. Интерпретатор ищет подпоследовательность байт `b'll'` (0x6C 0x6C) в последовательности `b'hello'` (0x68 0x65 0x6C 0x6C 0x6F).
2. Сравнение идёт побайтово слева направо.
3. Позиция 0: `he` ≠ `ll`; позиция 1: `el` ≠ `ll`; позиция 2: `ll` = `ll` — найдено.
4. Возвращается индекс 2.

#### Сравнение Py2 и Py3: bytes (сводная таблица)

| Аспект | Python 2.7 | Python 3 |
|--------|------------|----------|
| Литерал `b'x'` | str (синоним `'x'`) | bytes |
| `b'AB'[0]` | `'A'` (str) | `65` (int) |
| `b'AB'[0:1]` | `'A'` (str) | `b'A'` (bytes) |
| Тип для бинарных данных | str | bytes или bytearray |
| Кодировка open() по умолчанию | Системная / нет | UTF-8 (3.7+) |

#### Практические рецепты: строки и байты

**1. Чтение файла с автоопределением кодировки (упрощённо):**

```python
def read_text_auto(path, encodings=('utf-8', 'cp1251', 'cp866')):
    for enc in encodings:
        try:
            with open(path, encoding=enc) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Не удалось декодировать {path}")
```

**2. Безопасное получение строки из bytes (с fallback):**

```python
def safe_decode(data: bytes, encoding='utf-8') -> str:
    return data.decode(encoding, errors='replace')
```

**3. Round-trip произвольных байт через str (surrogateescape):**

```python
def bytes_to_str_roundtrip(data: bytes) -> str:
    return data.decode('utf-8', errors='surrogateescape')

def str_to_bytes_roundtrip(s: str) -> bytes:
    return s.encode('utf-8', errors='surrogateescape')
# str_to_bytes_roundtrip(bytes_to_str_roundtrip(b'\xff')) == b'\xff'
```

**4. Извлечение расширения и имени файла из bytes-пути (без pathlib):**

```python
def split_path_bytes(path: bytes) -> tuple[bytes, bytes]:
    """Возвращает (dirname, basename) или (путь_до_слэша, имя_файла)."""
    if b'/' in path:
        return path.rsplit(b'/', 1)[0], path.rsplit(b'/', 1)[1]
    return b'', path

def get_extension(path: bytes) -> bytes:
    if b'.' in path and path.rsplit(b'.', 1)[0]:
        return path.rsplit(b'.', 1)[1]
    return b''
```

**5. Поиск всех вхождений подстроки в bytes:**

```python
def find_all(data: bytes, sub: bytes) -> list[int]:
    result = []
    start = 0
    while True:
        pos = data.find(sub, start)
        if pos == -1:
            break
        result.append(pos)
        start = pos + 1
    return result
# find_all(b'ababab', b'ab')  # [0, 2, 4]
```

---

### 6.3.7 memoryview и Buffer Protocol

**memoryview** — объект, предоставляющий **«вид» (view)** на внутренние данные bytes, bytearray или других объектов, поддерживающих **Buffer Protocol**, без копирования. Это позволяет эффективно работать с бинарными данными: читать/писать байты через общий буфер, создавать срезы без копирования, передавать данные в C-расширения (numpy, struct) без сериализации.

#### Buffer Protocol (протокол буфера)

**Buffer Protocol** — внутренний протокол Python (C API), позволяющий объекту **экспортировать** свой внутренний буфер байт. Объекты, его поддерживающие: `bytes`, `bytearray`, `memoryview`, `array.array`, `numpy.ndarray`, модуль `struct` (для pack/unpack) и др.

Ключевая идея: вместо копирования данных при передаче между функциями/модулями объект «даёт ссылку» на свою память. `memoryview` — Python-интерфейс к этому протоколу.

#### memoryview(obj) — создание вида

```python
data = bytearray(b'hello')
mv = memoryview(data)
mv[0]     # 104 (int) — как при индексации bytearray
mv[0:3]   # <memory at 0x...> — срез memoryview (не копия данных!)
bytes(mv[0:3])  # b'hel' — при необходимости преобразовать в bytes
```

**Срезы memoryview не копируют данные** — они создают новый memoryview, указывающий на ту же память (с другим диапазоном). Изменение через срез изменяет исходный объект:

```python
ba = bytearray(b'hello')
mv = memoryview(ba)
mv[0:3][0] = ord('H')  # изменяет ba!
ba  # bytearray(b'Hello')
```

#### Основные атрибуты и методы memoryview

| Атрибут/метод | Назначение |
|---------------|------------|
| `mv.nbytes` | Размер в байтах (len × itemsize) |
| `mv.readonly` | True, если буфер только для чтения (bytes) |
| `mv.format` | Формат элемента: 'B' (unsigned char), 'b' (signed char) и др. |
| `mv.itemsize` | Размер одного элемента в байтах (для 'B' — 1) |
| `mv.ndim` | Число измерений (1 для bytes/bytearray) |
| `mv.shape` | Кортеж размеров по осям |
| `mv.strides` | Шаги в байтах для перехода к следующему элементу |
| `mv.tobytes()` | Копия данных как bytes |
| `mv.hex()` | Hex-представление |
| `mv.release()` | Освободить буфер (важно при использовании с C API) |

```python
mv = memoryview(b'AB')
mv.nbytes    # 2
mv.readonly  # True (bytes неизменяем)
mv.format    # 'B'
mv.itemsize  # 1
mv.tobytes() # b'AB'
mv.hex()     # '4142'
```

#### Когда использовать memoryview

1. **Эффективный доступ к частям большого буфера** — срезы без копирования:
   ```python
   data = bytearray(1_000_000)
   header = memoryview(data)[0:64]  # вид на первые 64 байта
   payload = memoryview(data)[64:]  # вид на остаток
   ```

2. **Интерфейс с numpy, struct, C-расширениями** — передача без копирования:
   ```python
   import struct
   data = bytearray(8)
   mv = memoryview(data)
   struct.pack_into('>HH', mv, 0, 0x1234, 0x5678)  # запись в буфер
   struct.unpack_from('>HH', mv, 0)  # (4660, 22136)
   ```

3. **Парсинг бинарных протоколов** — нулевые накладные расходы при доступе к полям:
   ```python
   packet = b'\x01\x02\x03\x04\x05\x06'
   mv = memoryview(packet)
   version = mv[0]
   length = mv[1] * 256 + mv[2]  # big-endian 16-bit
   payload = bytes(mv[3:3+length])
   ```

#### memoryview от bytes — только чтение

```python
mv = memoryview(b'hello')
mv.readonly  # True
# mv[0] = 72  # TypeError: cannot modify read-only memory
```

Для изменения создайте memoryview от **bytearray** или скопируйте в bytearray: `bytearray(mv)`.

#### Граничные случаи

- **memoryview от memoryview** — создаётся новый вид на те же данные.
- **Освобождение:** после `mv.release()` объект не должен использоваться; повторный вызов `release()` — no-op.
- **Контекстный менеджер:** `with memoryview(obj) as mv:` автоматически вызывает `release()` при выходе.

```python
with memoryview(bytearray(b'data')) as mv:
    data = mv.tobytes()
# mv освобождён
```

#### Сводка: bytes vs bytearray vs memoryview

| Тип | Изменяемость | Копирование при срезе | Использование |
|-----|--------------|------------------------|---------------|
| bytes | нет | да (новый объект) | Константные данные, ключи |
| bytearray | да | да | Накопление, изменение |
| memoryview | зависит от obj | нет (вид) | Эффективный доступ к частям, C API |

---

