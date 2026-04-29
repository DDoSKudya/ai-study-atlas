[← Назад к индексу части 26](index.md)

## 145. Операторы SQL

### Цель раздела

Научиться уверенно пользоваться **операторами SQL**: арифметическими, сравнений, логическими, строковыми, а также операторами для массивов, JSON и диапазонов, понимать приоритет и типичные ловушки.

### В этом разделе главное

- Операторы задают **структуру логики**: что с чем складывается, сравнивается и как комбинируются условия.
- Приоритет операторов (`NOT` > `AND` > `OR`) критичен — лучше **лишний раз ставить скобки**, чем ловить неожиданные результаты.
- Операторы для массивов, JSON и диапазонов позволяют в одну строку выразить то, что иначе пришлось бы писать сложными JOIN и подзапросами.

### Термины

- **Арифметический оператор** — `+`, `-`, `*`, `/`, `%`.
- **Оператор сравнения** — `=`, `<>`, `<`, `>`, `<=`, `>=`, а также `IS [NOT] NULL`.
- **Логический оператор** — `AND`, `OR`, `NOT`.
- **Строковый оператор** — `||`, `LIKE`, `ILIKE`, `SIMILAR TO`, `~` (регулярки).
- **Операторы массивов/JSON/диапазонов** — специальные символы для проверки вхождения/пересечения и извлечения частей.

### Теория и правила

- **Арифметические операторы**:
  - `+`, `-`, `*`, `/`, `%` (остаток).  
  - Деление целых чисел может давать целый результат (обрезание дроби) — зависит от типов.

- **Операторы сравнения**:
  - `=`, `<>` (или `!=`), `<`, `>`, `<=`, `>=`.  
  - Любое сравнение с `NULL` даёт `UNKNOWN`, а не `TRUE`/`FALSE`. Поэтому `IS NULL` и `IS NOT NULL` — отдельные операторы.

- **Логические операторы и приоритет**:
  - `NOT` выполняется раньше `AND`, который выполняется раньше `OR`.  
  - Для читаемости и безопасности **ставь скобки**: `WHERE (cond1 OR cond2) AND cond3`.

- **Строковые операторы**:
  - Конкатенация: `||` (в PostgreSQL и др.).  
  - `LIKE` — шаблоны с `%` (произвольная последовательность) и `_` (один символ).  
  - `ILIKE` (PostgreSQL) — `LIKE` без учёта регистра.  
  - `SIMILAR TO` и `~` — регулярные выражения (диалект‑зависимо).

- **Операторы массивов (PostgreSQL)**:
  - `&&` — массивы пересекаются.  
  - `@>` — левый массив содержит правый.  
  - `<@` — левый массив содержится в правом.  
  - `[]` — индекс: `arr[1]`.

- **Операторы JSON (PostgreSQL)**:
  - `->` — получить JSON‑значение (объект/массив).  
  - `->>` — получить текстовое значение (извлечь строку/число как текст).  
  - `@>` — левый JSON содержит правый (по структуре).  
  - `?`, `?&`, `?|` — наличие ключей.  
  - `#>`, `#>>` — доступ по пути.

- **Операторы диапазонов (PostgreSQL)**:
  - `&&` — диапазоны пересекаются.  
  - `@>` — диапазон содержит значение/диапазон.  
  - `<@` — значение/диапазон содержится в диапазоне.  
  - `-`, `+` — разность/объединение (для некоторых типов диапазонов).

### Разбор операторов по группам

#### Арифметические операторы: +, -, *, /, %

- **`+`** — сложение.
- **`-`** — вычитание.
- **`*`** — умножение.
- **`/`** — деление.
- **`%` или `MOD`** — остаток от деления (в выражениях чаще встречается функция `MOD`, см. числовые функции).

Важный момент: при делении целых чисел часть СУБД **обрезает дробную часть**, если оба операнда — целые. Чтобы получить дробный результат, хотя бы один операнд должен быть с плавающей точкой или `numeric`.

Пример:

```sql
SELECT 5 / 2;       -- может дать 2 (целое деление)
SELECT 5.0 / 2;     -- 2.5
SELECT 5 / 2.0;     -- 2.5
```

#### Операторы сравнения: =, <>, !=, <, >, <=, >=, IS NULL

- `=` — равно.
- `<>` или `!=` — не равно.
- `<`, `>`, `<=`, `>=` — меньше, больше, нестрогое меньше/больше.
- **Особый случай:** `IS NULL`, `IS NOT NULL`.

Правило:  
**Любое сравнение с `NULL` (`=`, `<`, `>`, `<>`) не даёт `TRUE` или `FALSE`, а даёт `UNKNOWN`.**  
Поэтому для проверки на отсутствие значения нужны отдельные операторы:

```sql
WHERE value IS NULL
WHERE value IS NOT NULL
```

#### Логические операторы: NOT, AND, OR

- `NOT` — логическое отрицание.
- `AND` — логическое «и».
- `OR` — логическое «или».

**Приоритет:** `NOT` > `AND` > `OR`.  
То есть без скобок:

```sql
a OR b AND c
```

будет трактоваться как:

```sql
a OR (b AND c)
```

Чтобы получить `(a OR b) AND c`, нужно явно поставить скобки:

```sql
(a OR b) AND c
```

#### Строковые операторы: ||, LIKE, ILIKE, SIMILAR TO, ~

- `||` — конкатенация (см. строковые функции).
- `LIKE` — простые шаблоны:  
  - `%` — «любая последовательность символов»,  
  - `_` — «один любой символ».

Примеры:

```sql
WHERE name LIKE 'A%'      -- начинается с 'A'
WHERE name LIKE '%son'    -- заканчивается на 'son'
WHERE code LIKE 'A_3'     -- 'A', любой символ, '3'
```

- `ILIKE` — как `LIKE`, но без учёта регистра (PostgreSQL).
- `SIMILAR TO` и `~` — регулярные выражения (диалект‑зависимо).

#### Операторы массивов (PostgreSQL): &&, @>, <@, []

- `&&` — массивы **пересекаются** (есть хотя бы один общий элемент).
- `@>` — левый массив **содержит** правый.
- `<@` — левый массив **содержится** в правом.
- `[]` — индекс элемента.

Примеры:

```sql
-- статьи, у которых в массиве тегов есть 'postgres'
WHERE tags @> ARRAY['postgres']

-- пользователь подписан хотя бы на один из указанных каналов
WHERE subscriptions && ARRAY['news', 'offers']
```

#### Операторы JSON (PostgreSQL): ->, ->>, @>, ?, ?&, ?|, #>, #>>

- `->` — получить JSON‑значение (объект/массив).
- `->>` — получить текстовое значение.
- `@>` — левый JSON **содержит** правый (по структуре).
- `?` — проверить наличие ключа.
- `?&`, `?|` — проверить наличие **всех** / **хотя бы одного** ключа из списка.
- `#>`, `#>>` — доступ по пути.

Пример:

```sql
-- событие определённого типа
WHERE payload->>'event_type' = 'signup'

-- payload содержит поле {"plan": "pro"}
WHERE payload @> '{"plan": "pro"}'
```

#### Операторы диапазонов: &&, @>, <@

Для типов `daterange`, `int4range` и др. (PostgreSQL):

- `&&` — диапазоны пересекаются;
- `@>` — диапазон содержит значение или другой диапазон;
- `<@` — значение или диапазон содержится в диапазоне.

Пример — акция, действительная на текущую дату:

```sql
WHERE active_period @> CURRENT_DATE
```

### Примеры

**1. Корректное комбинирование условий с `AND` и `OR`:**

```sql
SELECT *
FROM orders
WHERE (status = 'NEW' OR status = 'PENDING')
  AND created_at >= CURRENT_DATE - INTERVAL '7 days';
```

**2. Поиск строк по шаблону (email на `@example.com`):**

```sql
SELECT *
FROM users
WHERE email LIKE '%@example.com';
```

**3. Проверить, содержит ли массив тегов нужный тег (PostgreSQL):**

```sql
SELECT *
FROM articles
WHERE tags @> ARRAY['postgres'];
```

**4. Достать поле из JSON и отфильтровать по нему:**

```sql
SELECT *
FROM events
WHERE payload->>'event_type' = 'signup';
```

**5. Проверить, попадает ли дата в рабочий диапазон (диапазоны date):**

```sql
SELECT *
FROM promotions
WHERE active_period @> CURRENT_DATE;
```

### Простыми словами

Операторы — это **знаки препинания и союзы** в предложении SQL: они связывают части выражений и определяют, как читать условие. Неправильно поставленный оператор — как «не там поставленная запятая», смысл может радикально поменяться.

### Картинка в голове

Представь, что каждое условие (`status = 'PAID'`, `amount > 1000`) — это **лампочка**. Операторы `AND`, `OR`, `NOT` — это логические схемы, которые соединяют лампочки: «горит только если обе», «горит, если хотя бы одна», «перевёрнуть сигнал». Массивы/JSON/диапазоны — это более сложные блоки, но принципы те же.

### Как запомнить

**Приоритет: сначала `NOT`, потом `AND`, потом `OR`. Если сомневаешься — ставь скобки.** Для специальных типов запомни пары: массивы/диапазоны — `@>` (содержит), `<@` (содержится), `&&` (пересечение).

### Типичные ошибки

- Писать `WHERE a = 1 OR b = 2 AND c = 3` и ожидать «(a = 1 OR b = 2) AND c = 3» — без скобок получится другое.  
- Забывать, что `NULL` в сравнениях даёт `UNKNOWN`, и использовать `=` вместо `IS NULL`.  
- Путать операторы массивов/диапазонов и пытаться применять их к неподдерживаемым типам.

### Проверь себя

1. Как переписать условие `WHERE a = 1 OR b = 2 AND c = 3` так, чтобы сначала применялось `OR`?  
2. Почему `WHERE value = NULL` никогда не вернёт строк?  
3. Как проверить, что дата `CURRENT_DATE` входит в диапазон `daterange`?

<details>
<summary>Ответы</summary>

1. Нужно явно расставить скобки: `WHERE (a = 1 OR b = 2) AND c = 3`.  
2. Любое сравнение с `NULL` (`=`, `<>` и т.п.) даёт `UNKNOWN`, а не `TRUE`; фильтр `WHERE` пропускает только строки с `TRUE`, поэтому ничего не пройдёт. Нужно писать `WHERE value IS NULL`.  
3. В PostgreSQL: `WHERE my_range @> CURRENT_DATE` — оператор `@>` проверяет, содержит ли диапазон значение.
</details>

### Запомните

Операторы — это **скелет SQL‑логики**. Если ты уверен в приоритете и поведении операторов для разных типов (строк, массивов, JSON, диапазонов), то сложные условия становятся читаемыми и предсказуемыми, а не загадками «почему тут не так отфильтровалось».

---

## Диалектные отличия: PostgreSQL, MySQL, SQL Server

В этом разделе собраны **ключевые отличия трёх популярных СУБД** по тем же темам, что и в части: строковые/числовые/временные функции, условные конструкции, преобразование типов, системные функции и операторы.

### Базовые принципы

- **Синтаксис может отличаться**, но идея обычно одна и та же.  
- **Типы и поведение с `NULL` и временем** иногда заметно разные — это важно для продакшена.  
- Здесь мы не перечисляем все возможности, а даём **карту отличий по основным функциям и операторам**.

### Строковые функции: отличия

- **Конкатенация строк**
  - PostgreSQL: `CONCAT(a, b, ...)` и оператор `||`.  
  - MySQL: `CONCAT(a, b, ...)`, оператор `||` по умолчанию — это **логическое OR**, а не конкатенация.  
  - SQL Server: конкатенация через оператор `+`, функции `CONCAT`, `CONCAT_WS`.

- **Длина строки**
  - PostgreSQL:  
    - `LENGTH(str)` — длина в **байтах**;  
    - `CHAR_LENGTH(str)` / `CHARACTER_LENGTH(str)` — длина в **символах**.
  - MySQL:  
    - `LENGTH(str)` — байты;  
    - `CHAR_LENGTH(str)` — символы.
  - SQL Server:  
    - `LEN(str)` — длина в символах (без завершающих пробелов);  
    - `DATALENGTH(str)` — длина в байтах.

- **Поиск подстроки**
  - PostgreSQL: `POSITION(substr IN str)`, `STRPOS(str, substr)`.  
  - MySQL: `LOCATE(substr, str)`, `INSTR(str, substr)`.  
  - SQL Server: `CHARINDEX(substr, str)`, `PATINDEX(pattern, str)`.

- **Регулярные выражения**
  - PostgreSQL: богатая поддержка через `~`, `~*`, `!~`, `!~*`, `REGEXP_REPLACE`, `REGEXP_MATCHES`.  
  - MySQL: оператор `REGEXP`/`RLIKE`, функция `REGEXP_REPLACE` (в новых версиях).  
  - SQL Server: полноценного встроенного regexp‑движка нет; часто используют `LIKE`, `PATINDEX`, CLR или внешние средства.

### Числовые функции: отличия

- **Округление**
  - PostgreSQL: `ROUND`, `TRUNC`, `CEIL`/`CEILING`, `FLOOR`.  
  - MySQL: `ROUND`, `TRUNCATE`, `CEILING`, `FLOOR`.  
  - SQL Server: `ROUND`, `CEILING`, `FLOOR`; аналога `TRUNC` нет, но можно использовать `ROUND(num, digits, 1)` для усечения.

- **Случайные числа**
  - PostgreSQL: `RANDOM()` → `double precision` `[0, 1)`.  
  - MySQL: `RAND([seed])`.  
  - SQL Server: `RAND([seed])` (один генератор на сессию, вызовы без seed дают последовательность).

### Дата и время: отличия

- **Текущее время**
  - PostgreSQL: `NOW()`, `CURRENT_TIMESTAMP`, `CURRENT_DATE`, `CURRENT_TIME`.  
  - MySQL: `NOW()`, `CURRENT_TIMESTAMP`, `CURDATE()`, `CURTIME()`.  
  - SQL Server: `GETDATE()` (локальное время сервера), `SYSDATETIME()`, `CURRENT_TIMESTAMP`.

- **Разница дат и работа с интервалами**
  - PostgreSQL: тип `INTERVAL`, функции `AGE`, простое вычитание `ts1 - ts2`.  
  - MySQL: функции `DATEDIFF(date1, date2)`, `TIMESTAMPDIFF(unit, dt1, dt2)`, `DATE_ADD`, `DATE_SUB`, нет отдельного типа `INTERVAL`.  
  - SQL Server: `DATEDIFF(part, start, end)`, `DATEADD(part, value, date)`, `DATEDIFF_BIG` для больших диапазонов.

- **Округление и извлечение**
  - PostgreSQL: `DATE_TRUNC('unit', ts)`, `EXTRACT(field FROM ts)`.  
  - MySQL: `DATE_FORMAT(date, format)` (форматирование), `EXTRACT(part FROM date)`. Аналога `DATE_TRUNC` нет, но многие сценарии решаются через `DATE_FORMAT` + `CAST`.  
  - SQL Server: использует `DATEPART`, `DATENAME`, `FORMAT`, `EOMONTH`; явного аналога `DATE_TRUNC` нет.

### Условные функции и логика

- **CASE**
  - Во всех трёх СУБД синтаксис `CASE ... WHEN ... THEN ... ELSE ... END` по стандарту поддерживается.

- **IF / IIF**
  - PostgreSQL: только `CASE`, нет `IF` в чистом SQL (но есть в PL/pgSQL).  
  - MySQL: `IF(condition, true_value, false_value)` как обычная функция.  
  - SQL Server: `IIF(condition, true_value, false_value)` начиная с SQL Server 2012.

- **COALESCE / ISNULL / IFNULL**
  - PostgreSQL: `COALESCE`.  
  - MySQL: `COALESCE`, `IFNULL(expr1, expr2)`.  
  - SQL Server: `COALESCE`, `ISNULL(expr, replacement)`.

### Преобразование типов

- **Явное приведение**
  - PostgreSQL: `CAST(expr AS type)` и `expr::type`.  
  - MySQL / SQL Server: только `CAST`/`CONVERT`, синтаксиса `::` нет.

- **Форматирование дат/чисел**
  - PostgreSQL: `TO_CHAR`, `TO_DATE`, `TO_TIMESTAMP`, `TO_NUMBER`.  
  - MySQL: `DATE_FORMAT`, `STR_TO_DATE`, `FORMAT` (для чисел).  
  - SQL Server: `FORMAT`, `CONVERT` с `style`, `TRY_CONVERT`, `TRY_CAST` для безопасного приведения.

### JSON, массивы, диапазоны

- **PostgreSQL**
  - Массивы как отдельный тип (`text[]`, `int[]` и т.п.), операторы `@>`, `<@`, `&&`, индексирование `arr[1]`.  
  - JSON/JSONB с богатым набором операторов (`->`, `->>`, `@>`, `?`, `?|`, `?&`, `#>`, `#>>`) и индексами.  
  - Диапазонные типы (`int4range`, `numrange`, `daterange` и др.) с операторами `@>`, `<@`, `&&`.

- **MySQL**
  - Массивов как отдельного типа нет, но JSON‑массивы (`JSON`) активно используются с функциями `JSON_EXTRACT`, `JSON_CONTAINS`, `JSON_ARRAY`, `JSON_OBJECT`.  
  - Нет встроенных диапазонных типов как в PostgreSQL — диапазоны обычно моделируют двумя колонками `from`/`to`.

- **SQL Server**
  - JSON хранится в `NVARCHAR`, с функциями `JSON_VALUE`, `JSON_QUERY`, `OPENJSON`.  
  - Массивов и диапазонных типов тоже нет; используют таблицы связей и обычные типы.

### Операторы

- **Конкатенация**
  - PostgreSQL: `||`.  
  - MySQL: `CONCAT`, оператор `||` по умолчанию не используется для конкатенации.  
  - SQL Server: `+` (строковый плюс), `CONCAT`.

- **Регистронезависимый поиск**
  - PostgreSQL: `ILIKE`, регулярки с `~*`.  
  - MySQL: `LIKE` чувствителен к колlation; часто делают `LOWER(col) LIKE LOWER(pattern)`.  
  - SQL Server: чувствительность/нечувствительность задаётся collation; `LIKE` может быть чувствителен/нет в зависимости от настроек.

### Проверь себя (диалекты)

1. Какой оператор используется для конкатенации строк в PostgreSQL и в SQL Server?  
2. Чем отличается работа с интервалами/разницей дат в PostgreSQL и MySQL?  
3. Как в MySQL и SQL Server получить текущее время (по одной функции на каждую СУБД)?

<details>
<summary>Ответы</summary>

1. В PostgreSQL для конкатенации можно использовать `CONCAT(...)` и оператор `||`, в SQL Server — оператор `+` (для строк) и функцию `CONCAT(...)`.  
2. В PostgreSQL есть отдельный тип `INTERVAL`, можно прямо вычитать timestamps и работать с интервалами (`AGE`, `ts1 - ts2`). В MySQL интервал — это часть синтаксиса (`INTERVAL n unit`), а разницу считают функциями `DATEDIFF`, `TIMESTAMPDIFF`, отдельного типа `INTERVAL` нет.  
3. В MySQL — `NOW()` или `CURRENT_TIMESTAMP`, в SQL Server — `GETDATE()` (или более точный `SYSDATETIME()`).
</details>

---

## Дополнительные функции и операторы вне плана

Ниже — **неполный, но полезный список** функций и операторов, которые часто встречаются на практике, хотя прямо не перечислены в глобальном плане. Они помогут тебе лучше ориентироваться в чужом SQL‑коде.

### Строки

- PostgreSQL:
  - `LEFT(str, n)`, `RIGHT(str, n)` — взять первые/последние `n` символов.  
  - `OVERLAY(str PLACING replacement FROM start FOR length)` — заменить часть строки в середине.  
  - `STRING_AGG(str, delimiter)` — агрегат: склеить строки по группам.

- MySQL:
  - `LEFT`, `RIGHT`, `SUBSTRING_INDEX(str, delim, count)` — вытащить часть до/после N‑го разделителя.  
  - `REVERSE`, `FIELD`, `ELT` — часто встречаются в репортах.  
  - `GROUP_CONCAT(expr SEPARATOR ',')` — аналог `STRING_AGG`.

- SQL Server:
  - `LEFT`, `RIGHT`, `SUBSTRING`, `STUFF` (вставка/удаление внутри строки).  
  - `STRING_AGG(expr, ',')` (в новых версиях) — агрегатное склеивание.

### Даты и время

- PostgreSQL:
  - `JUSTIFY_DAYS/MONTHS/INTERVAL` — нормализация интервалов.  
  - `CLOCK_TIMESTAMP()`, `STATEMENT_TIMESTAMP()` — разные виды текущего времени.

- MySQL:
  - `DATE_ADD(date, INTERVAL n unit)`, `DATE_SUB`, `ADDDATE`, `SUBDATE`.  
  - `LAST_DAY(date)` — последняя дата месяца.  
  - `TIMESTAMPADD`, `TIMESTAMPDIFF`.

- SQL Server:
  - `DATEADD`, `DATEDIFF`, `DATEDIFF_BIG`, `EOMONTH`.  
  - `SWITCHOFFSET`, `TODATETIMEOFFSET` — работа с зонами.

### Преобразования и безопасность приведения

- **PostgreSQL**: `TRY_CAST` нет, но можно использовать `NULLIF` + проверку формата или писать пользовательские функции.  
- **MySQL**: многие приведения «молча» обрезают значения — в продакшене лучше сначала фильтровать строки регулярками.  
- **SQL Server**: `TRY_CAST`, `TRY_CONVERT`, `TRY_PARSE` — «мягкие» преобразования, которые возвращают `NULL` вместо ошибки.

### JSON‑функции

- PostgreSQL (`jsonb`):
  - `jsonb_path_query`, `jsonb_path_exists`, `jsonb_set`, `jsonb_insert`.  
  - Поддержка JSONPath, индексирование по путям.

- MySQL:
  - `JSON_SET`, `JSON_REPLACE`, `JSON_REMOVE`, `JSON_ARRAY_APPEND`.  
  - `JSON_UNQUOTE(JSON_EXTRACT(...))` — типичный паттерн.

- SQL Server:
  - `JSON_VALUE`, `JSON_QUERY`, `OPENJSON` с `WITH` — разворачивание JSON в таблицу.

### Проверь себя (дополнительные функции)

1. Чем `STRING_AGG` в PostgreSQL отличается от `GROUP_CONCAT` в MySQL и `STRING_AGG` в SQL Server по идее использования?  
2. Какое главное отличие между хранением JSON в PostgreSQL (`jsonb`) и в SQL Server (через `NVARCHAR`)?  
3. Какой безопасный способ приведения типов есть в SQL Server, если обычный `CAST` может выбросить ошибку?

<details>
<summary>Ответы</summary>

1. Все три функции служат одной идее — агрегировать несколько строк в одну строку с разделителем. Отличия в синтаксисе и опциях (`SEPARATOR` у `GROUP_CONCAT`, порядок/доп. параметры у `STRING_AGG`), но концептуально это один и тот же приём.  
2. В PostgreSQL существует тип `jsonb` с внутренним бинарным форматом, индексами и богатыми операторами; в SQL Server JSON хранится как текст (`NVARCHAR`) и обрабатывается функциями `JSON_VALUE`/`OPENJSON`, индексация делается опосредованно.  
3. В SQL Server есть функции `TRY_CAST`, `TRY_CONVERT`, `TRY_PARSE`, которые при невозможности приведения возвращают `NULL`, а не ошибку выполнения.
</details>

---

## Практический тренажёр по части

Ниже — блок **практических упражнений**. Идея простая:

- читаешь теорию по разделу;
- берёшь 1–2 упражнения;
- пробуешь написать запрос **без подсмотра в ответы**;
- затем раскрываешь `<details>` и сверяешься.

Не пытайся сделать всё сразу. Лучше качественно пройти по одному упражнению, чем пробежать все по диагонали.

### Упражнения по 139. Строковые функции

1. **Нормализация email‑адресов.**  
   В таблице `users(email_raw text)` есть email‑ы с лишними пробелами и разным регистром.  
   - Задача: написать запрос, который вернёт `email_normalized` в виде «обрезать пробелы по краям + перевести в нижний регистр».  
   - Подумай, какие функции нужно составить в «конвейер».

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  email_raw,
  LOWER(TRIM(email_raw)) AS email_normalized
FROM users;
```
</details>

2. **Вытащить домен из email.**  
   - Есть колонка `email`, формат строго `имя@домен`.  
   - Задача: получить только домен (`example.com`).

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  email,
  SPLIT_PART(email, '@', 2) AS domain
FROM users;
```
</details>

3. **Оставить только цифры в номере телефона.**  
   В таблице `contacts(phone_raw text)` номера вида `"+7 (999) 123-45-67"`.  
   - Задача: получить `phone_digits` только с цифрами, без пробелов, скобок и `+`.

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  phone_raw,
  REGEXP_REPLACE(phone_raw, '[^0-9]', '', 'g') AS phone_digits
FROM contacts;
```
</details>

### Упражнения по 140. Числовые функции

1. **Округление цены.**  
   В таблице `products(price_raw numeric)` цены с большим количеством знаков после запятой.  
   - Задача: вывести цену, округлённую до 2 знаков, и цену, просто усечённую (без округления).

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  price_raw,
  ROUND(price_raw, 2) AS price_rounded,
  TRUNC(price_raw, 2) AS price_truncated
FROM products;
```
</details>

2. **Разложить пользователей по корзинам.**  
   В таблице `users(id integer)` ты хочешь разложить пользователей по 4 группам для A/B‑тестов.  
   - Задача: на основе `id` получить `bucket` со значениями 1–4, распределёнными как можно равномернее.

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  id,
  MOD(id, 4) + 1 AS bucket
FROM users;
```
</details>

3. **Определить тренд метрики.**  
   Таблица `metrics(name text, value_today numeric, value_yesterday numeric)`.  
   - Задача: добавить колонку `trend`, где `'up'`, `'down'` или `'flat'` в зависимости от того, растёт значение, падает или не меняется.

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  name,
  value_today,
  value_yesterday,
  CASE SIGN(value_today - value_yesterday)
    WHEN 1  THEN 'up'
    WHEN -1 THEN 'down'
    ELSE 'flat'
  END AS trend
FROM metrics;
```
</details>

### Упражнения по 141. Даты и время

1. **Заказы по дням.**  
   Таблица `orders(id, created_at timestamp)`.  
   - Задача: посчитать, сколько заказов было каждый день.

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  DATE_TRUNC('day', created_at) AS day,
  COUNT(*) AS orders_count
FROM orders
GROUP BY DATE_TRUNC('day', created_at)
ORDER BY day;
```
</details>

2. **Проверка совершеннолетия.**  
   Таблица `users(id, birth_date date)`.  
   - Задача: выбрать только пользователей старше или равных 18 лет на текущую дату.

<details>
<summary>Возможное решение</summary>

```sql
SELECT *
FROM users
WHERE AGE(CURRENT_DATE, birth_date) >= INTERVAL '18 years';
```
</details>

3. **Сдвиг времени события.**  
   Таблица `events(id, occurred_at timestamptz)` хранит время в UTC.  
   - Задача: вывести время события в часовом поясе `Europe/Moscow`.

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  id,
  occurred_at,
  occurred_at AT TIME ZONE 'Europe/Moscow' AS occurred_at_msk
FROM events;
```
</details>

### Упражнения по 142. Условные функции

1. **Разбор статусов заказов.**  
   Таблица `orders(id, status text)`, статусы: `'NEW'`, `'PAID'`, `'CANCELED'`, другие возможны.  
   - Задача: вывести человекочитаемый статус (`'Новый'`, `'Оплачен'`, `'Отменён'`, `'Неизвестен'`).

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  id,
  status,
  CASE status
    WHEN 'NEW'      THEN 'Новый'
    WHEN 'PAID'     THEN 'Оплачен'
    WHEN 'CANCELED' THEN 'Отменён'
    ELSE 'Неизвестен'
  END AS status_label
FROM orders;
```
</details>

2. **Защита от деления на ноль.**  
   Таблица `stats(id, total numeric, count integer)`.  
   - Задача: посчитать `avg_value = total / count`, но так, чтобы при `count = 0` не падать с ошибкой, а получать `NULL`.

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  id,
  total,
  count,
  total / NULLIF(count, 0) AS avg_value
FROM stats;
```
</details>

3. **Значения по умолчанию для nullable‑полей.**  
   Таблица `orders(id, discount_percent numeric NULL)`.  
   - Задача: вывести колонку `discount_percent_safe`, где вместо `NULL` подставлено `0`.

<details>
<summary>Возможное решение</summary>

```sql
SELECT
  id,
  COALESCE(discount_percent, 0) AS discount_percent_safe
FROM orders;
```
</details>

### Упражнения по 143. Преобразование типов

1. **Строки → числа.**  
   Таблица `uploads(raw_id text)`, где `raw_id` — строка, но в ней лежат числа.  
   - Задача: безопасно привести `raw_id` к `integer` и отфильтровать строки, где это невозможно.

<details>
<summary>Возможное решение (PostgreSQL)</summary>

Идея: попробовать привести и отловить ошибки через `WHERE raw_id ~ '^[0-9]+$'`:

```sql
SELECT
  raw_id,
  CAST(raw_id AS integer) AS id
FROM uploads
WHERE raw_id ~ '^[0-9]+$';
```
</details>

2. **Форматирование дат.**  
   Таблица `sales(id, sale_date timestamp)`.  
   - Задача: вывести `sale_date` в строковом формате `ДД.ММ.ГГГГ ЧЧ:ММ`.

<details>
<summary>Возможное решение (PostgreSQL)</summary>

```sql
SELECT
  id,
  TO_CHAR(sale_date, 'DD.MM.YYYY HH24:MI') AS sale_date_str
FROM sales;
```
</details>

3. **Парсинг строковой даты.**  
   Таблица `raw_data(raw_date text)` вида `'31-12-2024'`.  
   - Задача: получить нормальную дату типа `date`.

<details>
<summary>Возможное решение (PostgreSQL)</summary>

```sql
SELECT
  raw_date,
  TO_DATE(raw_date, 'DD-MM-YYYY') AS parsed_date
FROM raw_data;
```
</details>

### Упражнения по 144. Системные функции

1. **Размер текущей базы.**  
   - Задача: узнать размер текущей БД в читаемом виде.

<details>
<summary>Возможное решение (PostgreSQL)</summary>

```sql
SELECT pg_size_pretty(pg_database_size(current_database()));
```
</details>

2. **Топ‑5 таблиц по размеру.**  
   - Задача: вывести 5 самых больших таблиц с их размером.

<details>
<summary>Возможное решение (PostgreSQL)</summary>

```sql
SELECT
  relname AS table_name,
  pg_size_pretty(pg_total_relation_size(relid)) AS total_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 5;
```
</details>

3. **Снять «снимок» настроек.**  
   - Задача: получить значения `max_connections`, `shared_buffers`, `work_mem`.

<details>
<summary>Возможное решение (PostgreSQL)</summary>

```sql
SELECT
  current_setting('max_connections') AS max_connections,
  current_setting('shared_buffers')  AS shared_buffers,
  current_setting('work_mem')        AS work_mem;
```
</details>

### Упражнения по 145. Операторы

1. **Сложное условие с AND/OR.**  
   Таблица `orders(id, status, amount, created_at)`.  
   - Задача: выбрать заказы:
     - со статусом `'NEW'` или `'PENDING'`,  
     - и суммой `amount > 1000`,  
     - и созданные за последние 7 дней.  
   - Важно: правильно расставить скобки.

<details>
<summary>Возможное решение</summary>

```sql
SELECT *
FROM orders
WHERE (status = 'NEW' OR status = 'PENDING')
  AND amount > 1000
  AND created_at >= CURRENT_DATE - INTERVAL '7 days';
```
</details>

2. **LIKE и ILIKE.**  
   Таблица `users(id, email)`.  
   - Задача: найти всех пользователей с доменом `@example.com`, игнорируя регистр.

<details>
<summary>Возможное решение (PostgreSQL)</summary>

```sql
SELECT *
FROM users
WHERE email ILIKE '%@example.com';
```
</details>

3. **Массивы и JSON.**  
   Таблица `articles(id, tags text[], meta jsonb)`.  
   - Задача:
     - выбрать статьи, у которых среди тегов есть `'postgres'`;  
     - и у которых в `meta` указано `"published": true`.

<details>
<summary>Возможное решение (PostgreSQL)</summary>

```sql
SELECT *
FROM articles
WHERE tags @> ARRAY['postgres']
  AND meta->>'published' = 'true';
```
</details>

---

---

<!-- prev-next-nav -->
*[← 144. Системные функции](06_144_sistemnye_funktsii.md) | [→ Справочник по части (ключевые пункты)](08_spravochnik_voprosy_rezyume.md)*
