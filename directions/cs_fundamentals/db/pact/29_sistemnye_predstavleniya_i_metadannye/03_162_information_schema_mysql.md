[← Назад к индексу части 29](index.md)

## 162. `INFORMATION_SCHEMA` (MySQL)

#### В этом разделе главное

- В MySQL метаданные хранятся в базе/схеме `INFORMATION_SCHEMA` (плюс `performance_schema`, `sys` для статистики).
- Основные таблицы похожи на стандарт: `TABLES`, `COLUMNS`, `KEY_COLUMN_USAGE`, `TABLE_CONSTRAINTS`, но есть и специфичные — например, статистика, привилегии, процессы.
- Как и в PostgreSQL, **важно фильтровать по схеме/базе** и понимать, что часть информации доступна только через другие схемы (`performance_schema`).

#### Простыми словами

Для MySQL `INFORMATION_SCHEMA` — это тоже каталог по базе, только:

- с классическими SQL‑таблицами в верхнем регистре (`TABLES`, `COLUMNS`, …);
- с рядом расширений (привилегии, статистика, процессы);
- и с нюансами реализации в разных версиях (некоторые вещи переезжают в `performance_schema`).

#### Основные таблицы

**`INFORMATION_SCHEMA.TABLES`**

- Описание таблиц/представлений:
  - `TABLE_SCHEMA`, `TABLE_NAME`, `TABLE_TYPE`;
  - `ENGINE` — движок (`InnoDB`, `MyISAM` и т.п.);
  - `TABLE_ROWS` — приблизительное число строк;
  - `DATA_LENGTH`, `INDEX_LENGTH` — размеры данных и индексов (в байтах).

**`INFORMATION_SCHEMA.COLUMNS`**

- Столбцы таблиц:
  - `TABLE_SCHEMA`, `TABLE_NAME`, `COLUMN_NAME`;
  - `ORDINAL_POSITION`;
  - `COLUMN_TYPE` (с размером), `DATA_TYPE` (общий тип);
  - `IS_NULLABLE`, `COLUMN_DEFAULT`;
  - `COLUMN_KEY` (`PRI`, `UNI`, `MUL`).

**`INFORMATION_SCHEMA.TABLE_CONSTRAINTS` + `KEY_COLUMN_USAGE`**

- Аналогично стандарту: информация об ограничениях и столбцах, которые в них участвуют.

**`TABLE_STATISTICS` и `INDEX_STATISTICS` (MariaDB / некоторые системы)**

- Эти таблицы есть, например, в MariaDB как часть функции **User Statistics** (включается отдельно).
- Они помогают понять, **как часто реально читают таблицы и индексы**.

`TABLE_STATISTICS` (упрощённо):

- `TABLE_SCHEMA` — имя базы;
- `TABLE_NAME` — имя таблицы;
- `ROWS_READ` — сколько строк прочитали из этой таблицы;
- `ROWS_CHANGED` — сколько строк изменили (`INSERT/UPDATE/DELETE`);
- `ROWS_CHANGED_X_INDEXES` — изменения с учётом числа затронутых индексов (чем больше индексов, тем дороже запись).

`INDEX_STATISTICS`:

- `TABLE_SCHEMA`, `TABLE_NAME` — к чему относится индекс;
- `INDEX_NAME` — имя индекса;
- `ROWS_READ` — сколько строк прочитали из этого индекса;
- в новых версиях — счётчик `QUERIES` и другие поля, помогающие оценить полезность индекса.

Примеры:

```sql
-- Часто читаемые таблицы (по количеству прочитанных строк)
SELECT
    table_schema,
    table_name,
    rows_read,
    rows_changed
FROM INFORMATION_SCHEMA.TABLE_STATISTICS
WHERE table_schema = 'app_db'
ORDER BY rows_read DESC
LIMIT 10;

-- Индексы, которые почти не читают (кандидаты на пересмотр)
SELECT
    table_schema,
    table_name,
    index_name,
    rows_read
FROM INFORMATION_SCHEMA.INDEX_STATISTICS
WHERE table_schema = 'app_db'
  AND rows_read < 100  -- порог подбирается под проект
ORDER BY rows_read, table_name, index_name;
```

> Важно: эти таблицы **не входят в «голый» MySQL 8.0**, они характерны именно для MariaDB и некоторых сборок.  
> Но идея полезна сама по себе: иметь отдельный слой статистики, привязанный к таблицам и индексам.

**Привилегии и процессы (MySQL‑специфичное):**

- `USER_PRIVILEGES`, `SCHEMA_PRIVILEGES`, `TABLE_PRIVILEGES` — кто какие права имеет;
- `PROCESSLIST` — активные соединения (аналог `SHOW PROCESSLIST`).

#### Примеры запросов

**Список таблиц в базе `app_db` с размером:**

```sql
SELECT
    table_schema,
    table_name,
    table_rows,
    data_length,
    index_length,
    data_length + index_length AS total_bytes
FROM INFORMATION_SCHEMA.TABLES
WHERE table_schema = 'app_db'
ORDER BY total_bytes DESC;
```

**Описание столбцов таблицы `orders`:**

```sql
SELECT
    column_name,
    column_type,
    is_nullable,
    column_default,
    column_key
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_schema = 'app_db'
  AND table_name   = 'orders'
ORDER BY ordinal_position;
```

**Поиск всех внешних ключей, ведущих в таблицу `users`:**

```sql
SELECT
    kcu.TABLE_SCHEMA,
    kcu.TABLE_NAME,
    kcu.COLUMN_NAME,
    kcu.CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS kcu
JOIN INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS AS rc
  ON rc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME
 AND rc.CONSTRAINT_SCHEMA = kcu.CONSTRAINT_SCHEMA
WHERE rc.REFERENCED_TABLE_SCHEMA = 'app_db'
  AND rc.REFERENCED_TABLE_NAME   = 'users';
```

#### Картинка в голове

`INFORMATION_SCHEMA` в MySQL — это:

- примерно тот же набор **«таблицы о таблицах»**, что и в стандарте;
- с бонусом в виде **размеров и статистики** прямо в `TABLES`;
- плюс сводка по **правам и процессам**, чтобы не ходить по разным командами `SHOW`.

#### Типичные ошибки

- «`TABLE_ROWS` — точное число строк» — нет, это **оценка**, особенно для InnoDB (может сильно отличаться от реальности).
- «Привилегии лучше смотреть только командами `SHOW`» — `INFORMATION_SCHEMA` даёт те же данные в табличном виде, с которым проще работать программно.
- «Всё про статистику есть в `INFORMATION_SCHEMA`» — часть метрик переехала в `performance_schema` и `sys`.

#### Как запомнить

- Запомни, что в MySQL `INFORMATION_SCHEMA` — **база**, а не только схема, и всё в верхнем регистре (`TABLES`, `COLUMNS`).
- Минимально полезная комбинация: `TABLES` (включая размеры), `COLUMNS`, `KEY_COLUMN_USAGE`, `TABLE_CONSTRAINTS`, `SCHEMA_PRIVILEGES` / `TABLE_PRIVILEGES`.

#### Как учить, если считаешь себя «тупым»

1. **Сделай одно простое упражнение.**

   - Подключись к своей тестовой MySQL‑базе.
   - Выполни:
     ```sql
     SELECT table_name, table_rows
     FROM INFORMATION_SCHEMA.TABLES
     WHERE table_schema = DATABASE();
     ```
   - Убедись, что видишь знакомые таблицы и примерное число строк.

2. **Свяжи `TABLES` и `COLUMNS`.**

   - Выбери одну таблицу из результата (например, `orders`).
   - Запроси её столбцы через `INFORMATION_SCHEMA.COLUMNS`.
   - Сравни с тем, что показывает любимый клиент (DBeaver, DataGrip и т.п.).

3. **Посмотри на размеры.**

   - В тот же запрос к `TABLES` добавь `data_length`, `index_length`, `total_bytes`.
   - Отсортируй по размеру и посмотри, какие таблицы самые тяжёлые.

4. **Не пытайся сразу понять все таблицы `INFORMATION_SCHEMA`.**  
   Для начала достаточно: `TABLES`, `COLUMNS`, `KEY_COLUMN_USAGE`, `TABLE_CONSTRAINTS`. Остальные пригодятся позже.

5. **Периодически возвращайся к этому разделу.**  
   После каждой новой фичи в проекте можешь задать себе вопрос: «Как бы я описал эту таблицу/ограничение через `INFORMATION_SCHEMA`?».

#### Проверь себя

<details>
<summary>1. Почему нельзя слепо доверять полю <code>TABLE_ROWS</code> в <code>INFORMATION_SCHEMA.TABLES</code>?</summary>

Потому что для движков вроде InnoDB это **оценка**, основанная на статистике, а не точный счётчик.  
Для точных значений нужно либо делать `COUNT(*)`, либо использовать специализированные инструменты/метрики.

</details>

<details>
<summary>2. Чем <code>INFORMATION_SCHEMA</code> в MySQL отличается от <code>information_schema</code> в PostgreSQL с точки зрения размеров объектов?</summary>

В MySQL в `INFORMATION_SCHEMA.TABLES` есть поля `DATA_LENGTH` и `INDEX_LENGTH`, дающие размер данных и индексов таблицы в байтах.  
В PostgreSQL для этого используют функции (`pg_table_size`, `pg_indexes_size`, `pg_total_relation_size`), а в `information_schema` таких числовых полей нет.

</details>

---

---

<!-- prev-next-nav -->
*[← 161. `pg_catalog` (PostgreSQL)](02_161_pg_catalog_postgresql.md) | [→ 163. Метаданные схемы](04_163_metadannye_shemy.md)*
