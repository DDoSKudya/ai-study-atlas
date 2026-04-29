[← Назад к индексу части II](index.md)

## Краткое повторение терминологии

| Термин | Определение |
|--------|-------------|
| **Code point** | Целое число 0–1 114 111, идентифицирующее символ в Unicode |
| **Character** | В контексте str — один code point |
| **Grapheme cluster** | Видимая единица текста (может состоять из нескольких code points) |
| **Encoding** | Правило преобразования code points ↔ байты (UTF-8, UTF-16, Latin-1 и т.д.) |
| **Decoding** | Преобразование байт → str (code points) |
| **UTF-8** | Кодировка переменной длины (1–4 байта); self-synchronizing; стандарт по умолчанию |
| **Latin-1** | 1 байт на символ, 0–255; round-trip любых байт без потерь |
| **ord(c)** | Code point символа c (str длиной 1) → int |
| **chr(i)** | Символ с code point i → str длиной 1 |
| **str.encode()** | str → bytes; параметры encoding, errors |
| **bytes.decode()** | bytes → str; параметры encoding, errors |
| **errors** | Поведение при ошибках: strict, ignore, replace, surrogateescape, backslashreplace и др. |
| **surrogateescape** | Round-trip произвольных байт через str (U+DC00+b ↔ байт b) |
| **bytes** | Неизменяемая последовательность байт (0–255); индексация → int; срез → bytes |
| **bytearray** | Изменяемая последовательность байт; мутирующие методы append, extend, pop и т.д. |
| **memoryview** | «Вид» на буфер без копирования; Buffer Protocol |
| **Buffer Protocol** | Протокол экспорта буфера байт (bytes, bytearray, array, numpy) |
| **BMP** | Basic Multilingual Plane; U+0000–U+FFFF |
| **BOM** | Byte Order Mark; для UTF-16/UTF-32 указывает порядок байт |

---

## Миграция с Python 2 на Python 3: строки и байты

При переходе с Python 2 на Python 3 модель строк — одна из самых важных областей изменений. Ниже — краткий чеклист.

- **`str` в Py2 — байты; в Py3 — Unicode.** Везде, где Py2-код предполагал байты, используйте **bytes** или **bytearray**.
- **Литералы:** `b'hello'` в Py3 — bytes; `'hello'` в Py3 — str (Unicode). В Py2 `b'hello'` и `'hello'` были синонимами.
- **Индексация bytes:** `b'AB'[0]` в Py3 возвращает **65** (int), а не `b'A'`. Для однобайтового объекта используйте срез `b'AB'[0:1]`.
- **open():** везде указывайте **encoding** при работе с текстом; в Py3 по умолчанию UTF-8.
- **Проверки типов:** `isinstance(s, str)` в Py3 — Unicode; для байт — `isinstance(s, bytes)`. Тип **unicode** в Py3 удалён; **basestring** удалён — используйте `(str, bytes)`.

## Частые сценарии и решения

#### Сценарий 1: Чтение файла с неизвестной кодировкой

**Задача:** файл может быть в UTF-8, CP1251 или CP866. Нужно попробовать декодировать.

```python
def read_text_auto(path: str, encodings=('utf-8', 'cp1251', 'cp866', 'latin-1')) -> str:
    with open(path, 'rb') as f:
        raw = f.read()
    for enc in encodings:
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Не удалось декодировать {path} ни одной из кодировок: {encodings}")
```

#### Сценарий 2: Запись CSV с кириллицей для Excel (Windows)

Excel ожидает BOM в UTF-8 файлах для корректного распознавания кириллицы:

```python
with open("report.csv", "w", encoding="utf-8-sig", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Имя", "Сумма"])
```
`utf-8-sig` добавляет BOM при записи; `newline=''` — обязательно для csv.writer.

#### Сценарий 3: Передача bytes через API, ожидающее str (JSON)

JSON не поддерживает bytes напрямую. Варианты: (1) base64 — `base64.b64encode(data).decode('ascii')`; (2) hex — `data.hex()`. Обратное: `bytes.fromhex(s)` или `base64.b64decode(s)`.

#### Сценарий 4: Сравнение строк с разной нормализацией (é vs e+accent)

```python
import unicodedata
def strings_equal_nfc(a: str, b: str) -> bool:
    return unicodedata.normalize('NFC', a) == unicodedata.normalize('NFC', b)
```

#### Сценарий 5: Безопасное логирование строк с возможными невалидными символами

```python
def safe_repr(s: str) -> str:
    return s.encode('utf-8', errors='replace').decode('utf-8')
# Или для логов: repr(s) — покажет escape для непечатаемых
```

#### Сценарий 6: Чтение строк из бинарного потока (фиксированная длина)

```python
def read_c_string(data: bytes, offset: int) -> tuple[str, int]:
    """Читает C-строку (до null) из data начиная с offset. Возвращает (строка, новый offset)."""
    end = data.find(b'\x00', offset)
    if end == -1:
        end = len(data)
    return data[offset:end].decode('utf-8'), end + 1
```

#### Сценарий 7: Проверка, что файл — валидный UTF-8 (без чтения в память целиком)

```python
def is_valid_utf8(path: str) -> bool:
    try:
        with open(path, encoding='utf-8', errors='strict') as f:
            for _ in f:  # итерация по строкам — ленивое чтение
                pass
        return True
    except UnicodeDecodeError:
        return False
```

---

## Сквозной пример: от чтения файла до вывода

Полный цикл: чтение текстового файла в одной кодировке → обработка в памяти (str) → запись в другой файл → вывод в консоль.

```python
# input.txt — файл в CP1251 с содержимым "Привет, мир!"
# Задача: прочитать, преобразовать в верхний регистр, сохранить в UTF-8, вывести

def process_and_convert(src_path: str, dst_path: str) -> None:
    # 1. Чтение: байты из файла → декодирование → str
    with open(src_path, encoding='cp1251') as f:
        text = f.read()  # str: "Привет, мир!"
    
    # 2. Обработка: работа только с str (Unicode)
    text_upper = text.upper()  # "ПРИВЕТ, МИР!"
    
    # 3. Запись: str → кодирование → байты в файл
    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(text_upper)
    
    # 4. Вывод в консоль: str → кодирование по sys.stdout.encoding → байты в терминал
    print(text_upper)  # на экране: ПРИВЕТ, МИР!

# Вызов
process_and_convert("input.txt", "output.txt")
```

**Что происходит на каждом шаге:**

| Шаг | Операция | Типы | Кодировка |
|-----|----------|------|-----------|
| 1 | `f.read()` | bytes (из ОС) → decode → str | CP1251 |
| 2 | `text.upper()` | str → str | — |
| 3 | `f.write(text_upper)` | str → encode → bytes (в ОС) | UTF-8 |
| 4 | `print(text_upper)` | str → encode → bytes (в stdout) | sys.stdout.encoding |

**Правило:** внутри приложения — только `str`; на границах (файл, сеть, консоль) — явные `encode`/`decode`.

---

## Схемы преобразований

#### Схема 1: Преобразование str ↔ bytes

```
     ┌─────────────────────────────────────────────────────────────┐
     │                    ТЕКСТ (в памяти Python)                  │
     │                         str                                 │
     │              последовательность code points                 │
     └─────────────────────────────────────────────────────────────┘
         │ encode(encoding, errors)          decode(encoding, errors)
         ▼                                              ▲
     ┌─────────────────────────────────────────────────────────────┐
     │                    БАЙТЫ (на границах)                      │
     │                        bytes                                │
     │            последовательность байт 0–255                    │
     └─────────────────────────────────────────────────────────────┘
         │                                              ▲
         │  запись в файл / сеть         чтение из файла / сети
         ▼                                              │
     ┌─────────────────────────────────────────────────────────────┐
     │              ФАЙЛ, СЕТЬ, КОНСОЛЬ (внешний мир)              │
     └─────────────────────────────────────────────────────────────┘
```

#### Схема 2: Чтение текстового файла (open с encoding)

```
  Файл на диске          BufferedReader           TextIOWrapper            Программа
  (байты)                (буфер байт)             (decode)                 (str)
      │                        │                        │                       │
      │  read()                 │                        │                       │
      │ ──────────────────────► │   байты                │                       │
      │                         │ ──────────────────────►│  decode(encoding)     │
      │                         │                        │ ─────────────────────►│
      │                         │                        │         str          │
```

#### Схема 3: Запись текстового файла

```
  Программа              TextIOWrapper             BufferedWriter           Файл на диске
  (str)                  (encode)                  (буфер байт)             (байты)
      │                        │                        │                       │
      │  write(str)             │                        │                       │
      │ ──────────────────────► │  encode(encoding)      │                       │
      │                         │ ──────────────────────►│   байты               │
      │                         │                        │ ─────────────────────►│
```

#### Схема 4: UTF-8 — длина последовательности по первому байту

<a id="схема-длины-utf-8-последовательности-по-первому-байту"></a>

```
  Первый байт       Диапазон           Длина        Пример
  0xxxxxxx          0x00–0x7F          1 байт       'A' → 0x41
  110xxxxx          0xC0–0xDF          2 байта      'П' → 0xD0 0x9F
  1110xxxx          0xE0–0xEF          3 байта      '€' → 0xE2 0x82 0xAC
  11110xxx          0xF0–0xF7          4 байта      '😀' → 0xF0 0x9F 0x98 0x80
  10xxxxxx          continuation       (часть)      второй/третий/четвёртый байт
```

---

## Отладка и диагностика: строки и байты

**Проверка типа и содержимого:**
```python
type(s)        # str или bytes
repr(s)        # показывает escape для непечатаемых символов: '\n', '\xd0\x9f'
s.encode('utf-8').hex()   # hex-дамп байт строки
bytes.fromhex('...').decode('utf-8')  # обратно
```

**Проверка кодировки файла (эвристика):**
```python
# Попытка декодирования с разными кодировками
for enc in ('utf-8', 'cp1251', 'cp866', 'latin-1'):
    try:
        with open(path, encoding=enc) as f:
            text = f.read()
        print(f"Похоже на {enc}: {text[:50]}...")
        break
    except UnicodeDecodeError:
        continue
```

**repr vs print:** `print(s)` выводит «человекочитаемое» представление; `repr(s)` показывает escape-последовательности и тип. Для отладки «кракозябр» полезно смотреть `repr(text)` и hex байт файла.

---

## Типичные ошибки при работе со строками и байтами

1. **Сложение str и bytes:** `"x" + b"y"` → `TypeError`. Явно преобразуйте: `"x" + b"y".decode()` или `"x".encode() + b"y"`.
2. **Индексация bytes ожидает str:** `b'AB'[0]` возвращает int; для однобайтового bytes используйте срез `b[i:i+1]`.
3. **ord() от int:** `ord(b'A'[0])` → `TypeError`; `b'A'[0]` уже int, `chr(b'A'[0])` — правильно.
4. **Кодировка по умолчанию:** не полагайтесь на системную кодировку при открытии файлов — явно указывайте `encoding`.
5. **ignore при decode:** тихо теряет данные; для отладки предпочтите `replace`, для round-trip — `surrogateescape`.
6. **Сравнение str и bytes:** `"a" == b"a"` → `False`; типы разные. Привести к одному: `"a" == b"a".decode()`.
7. **Форматирование с bytes:** `f"{b'x'}"` даёт `"b'x'"` (repr); для текста — `b'x'.decode()`.
8. **in с разными типами:** `b'a' in "abc"` → `TypeError`; `"a" in b"abc"` → `TypeError`. Подстрока и контейнер должны быть одного типа.
9. **Путь с не-ASCII и open:** на Windows пути в UTF-16; Python 3 корректно обрабатывает. Явно `Path` или `os.fsdecode` при необходимости.
10. **Бинарный режим и encoding:** `open(path, 'rb', encoding='utf-8')` — encoding игнорируется; в бинарном режиме decode не выполняется.
11. **split() с пустым разделителем:** `"a".split("")` — `ValueError`; split не принимает пустую строку как sep.
12. **bytes и hash:** bytes хешируем (hashable), можно использовать как ключ dict; bytearray — нет (изменяемый).

---

## Вопросы для самопроверки

1. Что возвращает `b'AB'[0]` в Python 3 и почему?
2. В чём разница между `str` и `bytes`?
3. Какая кодировка по умолчанию в `open()` для текстового режима (Python 3.7+)?
4. Когда использовать `errors='surrogateescape'`?
5. Почему `''.join(parts)` предпочтительнее цикла `s = ''; for x in parts: s += x`?
6. Чем `chr(ord(c))` отличается от `c` для произвольного символа?
7. Сколько байт занимает символ 'П' в UTF-8? А в UTF-16?
8. Что делает `bytes.fromhex('41')`?
9. Какие escape-последовательности допустимы в bytes-литералах?
10. Как получить однобайтовый bytes из байта по индексу `i`?
11. Чем отличается `bytes(3)` от `bytes([3])`?
12. Что произойдёт при `b'\xff\xfe'.decode('utf-8', errors='strict')`?
13. Как записать строку в файл в кодировке CP1251?
14. Что такое BOM и зачем он нужен в UTF-16?
15. Почему `bytes(5)` и `bytes([5])` дают разный результат? Объясните оба вызова.
16. Что вернёт `"café".encode("ascii", errors="xmlcharrefreplace")`?
17. Зачем при работе с csv.writer указывать newline='' при открытии файла?
18. Чем отличается split() от splitlines() для bytes?
19. Почему bytes хешируем, а bytearray — нет?
20. Что вернёт `"".join([chr(i) for i in range(256)])` при encode('latin-1')?

<details>
<summary>Показать ответы</summary>

1. **`65` (int)** — в Python 3 индексация bytes возвращает целое число (код байта). См. [§6.3.1 Индексация и срезы](#631-индексация-и-срезы).  
2. **str** — последовательность Unicode code points (текст); **bytes** — последовательность байт (0–255), сырые данные. См. [§6.1.1](#611-unicode-code-points-и-представление-в-памяти).  
3. **UTF-8** (на всех платформах с Python 3.7+). См. [§6.2.1](#621-open-и-encoding).  
4. Когда нужно round-trip произвольных байт через текстовый интерфейс (имена файлов в POSIX, legacy-данные). См. [§6.2.3 surrogateescape](#623-параметр-errors).  
5. **join** — линейная сложность, один проход; конкатенация в цикле — квадратичная, много аллокаций. См. [§6.3.4 str.join()](#634-strjoin--эффективная-конкатенация).  
6. Для одного code point: `chr(ord(c)) == c`. См. [§6.1.3 ord() и chr()](#613-ord-и-chr--код-и-символ).  
7. 'П' (U+041F): UTF-8 — 2 байта; UTF-16 — 2 байта (в BMP). См. [§6.1.2 UTF-8, UTF-16](#612-utf-8-utf-16-utf-32-latin-1).  
8. **`b'A'`** — один байт 0x41. См. [§6.3.2 fromhex](#632-создание-bytes-и-bytearray).  
9. `\xHH`, `\n`, `\r`, `\t`, `\\`, `\'`, `\"` и др. — только то, что даёт один байт; `\u`, `\U` недопустимы. См. [§6.1.4 bytes-литералы](#614-escape-последовательности-nname-uhhhh-uhhhhhhhh).  
10. **`b[i:i+1]`** — срез; `bytes([b[i]])` — через конструктор. См. [§6.3.1](#631-индексация-и-срезы).  
11. `bytes(3)` — bytes длины 3 из нулевых байт: `b'\x00\x00\x00'`. `bytes([3])` — один байт со значением 3: `b'\x03'`. См. [§6.3.2 Конструкторы bytes](#632-создание-bytes-и-bytearray).  
12. **`UnicodeDecodeError`** — байты `0xFF 0xFE` не являются корректной UTF-8 последовательностью. См. [§6.1.2 Примеры невалидных UTF-8](#612-utf-8-utf-16-utf-32-latin-1).  
13. **`open(path, 'w', encoding='cp1251').write(s)`** — явно указать encoding при записи. См. [§6.2.1](#621-open-и-encoding).  
14. **BOM (Byte Order Mark)** — служебные байты в начале файла (U+FEFF); указывают порядок байт в UTF-16. См. [§6.1.2 BOM](#612-utf-8-utf-16-utf-32-latin-1).
15. **`bytes(5)`** — конструктор с одним целым: 5 нулевых байт. **`bytes([5])`** — с итерабельным: один байт 0x05. См. [§6.3.2](#632-создание-bytes-и-bytearray).  
16. **`b'caf&#233;'`** — é заменён на XML-сущность `&#233;`. См. [§6.3.3 encode, errors](#633-encode-и-decode--преобразование-strbytes).  
17. Без `newline=''` на Windows `\n` при записи станет `\r\n`, что ломает CSV. См. [§6.2.2 newline](#622-текстовый-и-бинарный-режим).  
18. **split()** — по пробельным или sep; **splitlines()** — только по границам строк. См. [§6.3.6 split, splitlines](#636-методы-bytes-и-bytearray).  
19. **bytes** — неизменяемый, hashable; **bytearray** — изменяемый, не hashable. См. [§6.3.5 bytearray](#635-bytearray--изменяемая-последовательность-байт).  
20. Строка из 256 символов (U+0000..U+00FF). При encode('latin-1') → `bytes(range(256))`. См. [§6.1.2 Latin-1](#612-utf-8-utf-16-utf-32-latin-1).
</details>

---

## Тестовые задания

**Задание 1.** Напишите функцию `to_hex(s: str) -> str`, которая возвращает строку с hex-представлением байт строки `s` в UTF-8 (например, `"A"` → `"41"`).

<details>
<summary>Показать ответ</summary>

```python
def to_hex(s: str) -> str:
    return s.encode('utf-8').hex()
```
См. [§6.3.3 encode](#633-encode-и-decode--преобразование-strbytes), [§6.3.6 hex](#636-методы-bytes-и-bytearray).
</details>

**Задание 2.** Напишите функцию, которая читает файл в кодировке CP1251 и записывает его в новый файл в UTF-8.

<details>
<summary>Показать ответ</summary>

```python
def convert_cp1251_to_utf8(src: str, dst: str) -> None:
    with open(src, encoding='cp1251') as f:
        text = f.read()
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(text)
```
См. [§6.2.1 open и encoding](#621-open-и-encoding).
</details>

**Задание 3.** Что выведет `print(bytes([72, 101, 108, 108, 111]).decode())`? Объясните пошагово.

<details>
<summary>Показать ответ</summary>

`Hello`. `bytes([72, 101, 108, 108, 111])` создаёт `b'Hello'`. Метод `decode()` без аргументов использует кодировку по умолчанию (UTF-8); последовательность байт `b'Hello'` в UTF-8 — это ASCII, декодируется в строку `'Hello'`.  
См. [§6.3.2 Создание bytes](#632-создание-bytes-и-bytearray), [§6.3.3 decode](#633-encode-и-decode--преобразование-strbytes).
</details>

**Задание 4.** Получите строку `'Привет'` тремя способами: литералом, через `chr()` и через escape `\u`.

<details>
<summary>Показать ответ</summary>

```python
s1 = "Привет"
s2 = "".join(chr(c) for c in [1055, 1088, 1080, 1074, 1077, 1090])
s3 = "\u041f\u0440\u0438\u0432\u0435\u0442"
assert s1 == s2 == s3
```
См. [§6.1.3 ord и chr](#613-ord-и-chr--код-и-символ), [§6.1.4 escape \uHHHH](#614-escape-последовательности-nname-uhhhh-uhhhhhhhh).
</details>

**Задание 5.** Напишите функцию `safe_decode(data: bytes) -> str`, которая декодирует байты в UTF-8, заменяя невалидные байты на символ U+FFFD.

<details>
<summary>Показать ответ</summary>

```python
def safe_decode(data: bytes) -> str:
    return data.decode('utf-8', errors='replace')
```
См. [§6.2.3 errors](#623-параметр-errors), [§6.3.3 decode](#633-encode-и-decode--преобразование-strbytes).
</details>

**Задание 6.** Объясните пошагово, как `'П'` кодируется в UTF-8 (code point U+041F, два байта).

<details>
<summary>Показать ответ</summary>

U+041F = 1055 (дес.) = 0x041F (hex). В диапазоне U+0080–U+07FF (2 байта). Формат UTF-8: 110xxxxx 10xxxxxx. 1055 в двоичном: 100 0001 1111 (11 бит). Заполняем: 11010000 10011111 → 0xD0 0x9F. Результат: `b'\xd0\x9f'`.  
См. [§6.1.2 UTF-8](#612-utf-8-utf-16-utf-32-latin-1), [Схема длины UTF-8](#схема-длины-utf-8-последовательности-по-первому-байту).
</details>

**Задание 7.** Напишите функцию, которая принимает bytes и возвращает str, заменяя невалидные UTF-8 байты на символ замены (U+FFFD). Без использования decode — только ord, chr и цикл (упрощённо: считать каждый байт Latin-1).

<details>
<summary>Показать ответ (Задание 7)</summary>

Это учебная задача; на практике используйте `data.decode('utf-8', errors='replace')`. Упрощённый вариант (Latin-1 для каждого байта): `''.join(chr(b) if b < 128 else '\ufffd' for b in data)` — некорректен для полноценного UTF-8, т.к. не учитывает многобайтовые последовательности. Полная ручная реализация требует парсинга UTF-8 по битам. Практический вывод: всегда используйте встроенные encode/decode с параметром errors.  
См. [§6.2.3 errors](#623-параметр-errors), [§6.1.2 UTF-8](#612-utf-8-utf-16-utf-32-latin-1).
</details>

**Задание 8.** Объясните пошагово, почему `b'\xff\xfe'` не является валидной UTF-8 последовательностью. Какие байты могли бы следовать за 0xFF, если бы он был первым байтом 4-байтовой последовательности?

<details>
<summary>Показать ответ (Задание 8)</summary>

Байт 0xFF в бинарном виде: 11111111. В UTF-8 первый байт с префиксом 11111 (5 единиц) не определён — допустимы только 0, 110, 1110, 11110. Байт 0xFF не является ни валидным однобайтовым (0xxxxxxx), ни началом 2/3/4-байтовой последовательности. Следовательно, он невалиден. Второй байт 0xFE (11111110) — continuation byte должен иметь вид 10xxxxxx; 0xFE начинается с 10, но сам по себе как continuation после невалидного 0xFF не даёт корректной последовательности. Если бы 0xFF теоретически мог быть первым байтом 4-байтовой последовательности (формат 11110xxx), то следующие 3 байта должны быть 10xxxxxx. Но 0xFF — не 11110xxx (он 11111111), поэтому вопрос гипотетичен. Итог: 0xFF — невалидный байт в UTF-8.  
См. [§6.1.2 UTF-8](#612-utf-8-utf-16-utf-32-latin-1), [Схема длины UTF-8](#схема-длины-utf-8-последовательности-по-первому-байту).
</details>

**Задание 9.** Напишите функцию `normalize_for_compare(s: str) -> str`, которая приводит строку к форме NFC для корректного сравнения (импорт `unicodedata` разрешён).

<details>
<summary>Показать ответ (Задание 9)</summary>

```python
import unicodedata

def normalize_for_compare(s: str) -> str:
    return unicodedata.normalize('NFC', s)

# Использование:
# normalize_for_compare("e\u0301") == normalize_for_compare("é")  # True
```
См. §15d (unicodedata, NFC/NFD) — материал выходит за рамки текущей темы.
</details>

**Задание 10.** Создайте bytes из списка целых `[72, 101, 108, 108, 111]` тремя разными способами. Декодируйте результат в строку и убедитесь, что получилось "Hello".

<details>
<summary>Показать ответ (Задание 10)</summary>

```python
data = [72, 101, 108, 108, 111]

# Способ 1: bytes(iterable_of_ints)
b1 = bytes(data)
assert b1.decode() == "Hello"

# Способ 2: bytes.fromhex после hex-представления
hex_str = ''.join(f'{x:02x}' for x in data)  # '48656c6c6f'
b2 = bytes.fromhex(hex_str)
assert b2.decode() == "Hello"

# Способ 3: bytearray с последующим преобразованием
b3 = bytes(bytearray(data))
assert b3.decode() == "Hello"
```
См. [§6.3.2 Создание bytes и bytearray](#632-создание-bytes-и-bytearray), [§6.3.6 fromhex](#636-методы-bytes-и-bytearray).
</details>

**Задание 11.** Что выведет `print(b'AB'[0] + 1)` и почему? Как получить строку `'B'` из `b'AB'` с использованием этого результата?

<details>
<summary>Показать ответ (Задание 11)</summary>

`print(b'AB'[0] + 1)` выведет `66` — `b'AB'[0]` это 65 (int), 65+1=66. Для получения строки `'B'`: `chr(b'AB'[1])` или `chr(66)` или `b'AB'[1:2].decode()`.  
См. [§6.3.1 Индексация bytes[i]](#631-индексация-и-срезы).
</details>

<details>
<summary>Вопрос: в чём разница между <code>bytes(n)</code> и <code>bytes([n])</code>?</summary>

**bytes(n)** — создаёт последовательность из **n нулевых байт** (n — целое >= 0). Результат: `b'\x00\x00...'` длиной n. **bytes([n])** — создаёт последовательность из **одного байта** со значением n (0–255). Результат: `bytes([65])` → `b'A'`. Для n=5: `bytes(5)` → `b'\x00\x00\x00\x00\x00'`; `bytes([5])` → `b'\x05'`.  
См. [§6.3.2 Создание bytes](#632-создание-bytes-и-bytearray).
</details>

---

## Вопросы на проверку

Дополнительные вопросы для самопроверки. Ответы в раскрывающихся блоках; ссылки ведут к соответствующему разделу.

**1.** Что вернёт `b'hello'[1:4].decode()` и почему?

<details>
<summary>Показать ответ</summary>

**`'ell'`** — срез `b'hello'[1:4]` даёт `b'ell'`; метод `decode()` без аргументов использует UTF-8 по умолчанию; `b'ell'` — валидный ASCII/UTF-8.  
См. [§6.3.1 Срезы](#631-индексация-и-срезы), [§6.3.3 decode](#633-encode-и-decode--преобразование-strbytes).
</details>

**2.** Чем `ba.insert(0, x)` отличается от `ba = bytearray([x]) + ba`?

<details>
<summary>Показать ответ</summary>

**insert** — мутация на месте, возвращает `None`; **bytearray([x]) + ba** — создаёт новый объект. По результату эквивалентны, но insert не создаёт промежуточных объектов.  
См. [§6.3.5 bytearray, insert](#635-bytearray--изменяемая-последовательность-байт).
</details>

**3.** Что выведет `print('\u041f\u0440\u0438\u0432\u0435\u0442')`?

<details>
<summary>Показать ответ</summary>

**Привет** — escape `\uHHHH` интерпретируется как Unicode code point; шесть escape дают шесть символов кириллицы.  
См. [§6.1.4 \uHHHH](#614-escape-последовательности-nname-uhhhh-uhhhhhhhh).
</details>

**4.** Почему `open("file.txt", "rb").read()` возвращает bytes, а не str?

<details>
<summary>Показать ответ</summary>

Режим **`'rb'`** — бинарный; декодирование не выполняется. Байты возвращаются как есть. Для str нужен текстовый режим (`'r'`) с `encoding`.  
См. [§6.2.2 Текстовый и бинарный режим](#622-текстовый-и-бинарный-режим).
</details>

**5.** Что произойдёт при `"Привет".encode("ascii")`? Как исправить?

<details>
<summary>Показать ответ</summary>

**UnicodeEncodeError** — ASCII не содержит кириллицу. Исправить: использовать `encoding='utf-8'` или `errors='replace'` / `errors='ignore'`.  
См. [§6.3.3 encode](#633-encode-и-decode--преобразование-strbytes).
</details>

**6.** Зачем нужен параметр `newline=''` при `open(..., newline='')` для CSV?

<details>
<summary>Показать ответ</summary>

Без него на Windows `\n` при записи превращается в `\r\n`, что создаёт лишние переводы строк в полях CSV. `newline=''` отключает нормализацию.  
См. [§6.2.2 newline](#622-текстовый-и-бинарный-режим).
</details>

**7.** Как получить строку из bytes с заменой невалидных байт на `?` при декодировании?

<details>
<summary>Показать ответ</summary>

**`data.decode('utf-8', errors='replace')`** — символ U+FFFD (); для `?` (ASCII): `data.decode('utf-8', errors='replace').encode('ascii', errors='replace').decode()` или проще — `errors='replace'` даёт U+FFFD, визуально похожий.  
См. [§6.2.3 errors](#623-параметр-errors).
</details>

**8.** В чём разница между `b'AB'[0]` в Python 2 и Python 3?

<details>
<summary>Показать ответ</summary>

**Python 2:** `'A'` (str, однобайтовая строка). **Python 3:** `65` (int, код байта).  
См. [§6.3.1 Индексация](#631-индексация-и-срезы), [Сводная таблица Py2 vs Py3](#611-unicode-code-points-и-представление-в-памяти).
</details>

---

## Резюме по Части II

- **str** — последовательность Unicode code points; **bytes** — последовательность байт (0–255); **bytearray** — изменяемый bytes.
- **ord(c)** и **chr(i)** — мост между символом и code point; взаимно обратные: `chr(ord(c)) == c`.
- **UTF-8** — кодировка по умолчанию; переменная длина 1–4 байта; self-synchronizing; Latin-1 — round-trip любых байт; surrogateescape — round-trip произвольных байт через str.
- **open(encoding='utf-8')** — текстовый режим; **open('rb')** — бинарный, bytes; параметр **newline** управляет переводами строк.
- **encode** / **decode** — преобразование str ↔ bytes; параметр **errors** (strict, ignore, replace, surrogateescape) управляет поведением при ошибках.
- Индексация **bytes[i]** возвращает **int**; срез **bytes[i:j]** возвращает **bytes**; для однобайтового объекта используйте срез.
- **str.join(iterable)** — эффективная конкатенация (O(N)); конкатенация в цикле — O(N²).
- Escape: `\uHHHH`, `\UHHHHHHHH`, `\N{NAME}` для указания символов по коду или имени; в bytes допустимы только `\xHH` и др., не `\u`/`\U`.
- CP1251, CP866 — кодировки для legacy-русского текста; для новых проектов — UTF-8.
- `bytes` хешируем (ключ dict); `bytearray` — нет. `split()` vs `splitlines()` — разные разделители.
- **Потоковая обработка:** `for line in f:` — текстовые файлы; `while True: chunk = f.read(size); if not chunk: break` — бинарные. Избегайте `f.read()` для больших файлов.
- **memoryview** — вид на bytes/bytearray без копирования; Buffer Protocol для эффективной работы с буферами.

---

### Дополнительные задания (углублённые)

**Задание 12.** Напишите функцию, которая определяет, является ли строка валидным UTF-8 без использования decode (проверка битовых масок первых байт).

<details>
<summary>Показать ответ</summary>

Упрощённая проверка: первый байт определяет длину последовательности (0x00–0x7F → 1; 0xC0–0xDF → 2; и т.д.); последующие байты должны быть 0x80–0xBF. Полная реализация должна проверять overlong, surrogate, диапазоны code points.  
См. [§6.1.2 UTF-8](#612-utf-8-utf-16-utf-32-latin-1), [Схема длины UTF-8](#схема-длины-utf-8-последовательности-по-первому-байту).
</details>

**Задание 13.** Реализуйте простой парсер «key=value» из bytes, возвращающий dict[str, str]. Пары разделены `\n`, кодировка UTF-8.

<details>
<summary>Показать ответ</summary>

`dict(line.decode('utf-8').split('=', 1) for line in data.split(b'\n') if b'=' in line)` — упрощённо; нужна обработка пустых строк и ошибок.  
См. [§6.3.6 split, splitlines](#636-методы-bytes-и-bytearray), [§6.3.3 decode](#633-encode-и-decode--преобразование-strbytes).
</details>

**Задание 14.** Что выведет `print(bytes([0]).decode('utf-8') == chr(0))`? Объясните.

<details>
<summary>Показать ответ</summary>

**True**. `bytes([0])` = `b'\x00'` — валидный UTF-8 (ASCII null). `chr(0)` = `'\x00'`. Оба — строка из одного символа U+0000. Сравнение даёт True.  
См. [§6.3.2 Создание bytes](#632-создание-bytes-и-bytearray), [§6.1.3 chr](#613-ord-и-chr--код-и-символ).
</details>

---

*Этот документ соответствует Части II глобального плана (§6) и служит основой для дальнейших тем (stdlib, pathlib, dataclasses и т.д.). Продвинутые темы Unicode — unicodedata, NFC/NFD, grapheme clusters — см. §15d. Связанные PEP: PEP 393 (flexible string representation), PEP 358 (bytes type), PEP 540 (UTF-8 mode), PEP 3120 (source encoding UTF-8).*
