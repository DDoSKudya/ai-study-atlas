[← Назад к индексу части 26](index.md)

## 144. Системные функции

### Цель раздела

Научиться использовать **системные функции для диагностики и introspection**: узнавать версию БД, активного пользователя, размеры баз/таблиц и текущие настройки.

### В этом разделе главное

- Системные функции помогают **«заглянуть под капот»** БД без доступа к консоли сервера.
- Знание функций размера (`pg_database_size`, `pg_relation_size`, `pg_total_relation_size`, `pg_size_pretty`) критично для оценки потребления диска.
- `current_setting` и подобные функции позволяют **читать конфигурацию в рантайме**.

### Термины

- **Интроспекция** — способность системы предоставлять информацию о самой себе.
- **Бэкенд‑процесс** — отдельный серверный процесс, обслуживающий соединение (в PostgreSQL).

### Теория и правила (на примере PostgreSQL)

- **VERSION()**:

```sql
SELECT version();
```

Возвращает строку с информацией о версии PostgreSQL, параметрах сборки и ОС.

- **CURRENT_USER / SESSION_USER**:
  - `CURRENT_USER` — текущий пользователь (может отличаться при `SET ROLE`).  
  - `SESSION_USER` — пользователь, под которым установлено соединение.

- **DATABASE(), SCHEMA()** (или аналоги):
  - `CURRENT_DATABASE()` в PostgreSQL, `DATABASE()` в MySQL — текущее имя БД.  
  - `current_schema()` — текущая схема поиска объектов.

- **Размеры**:

```sql
SELECT
  pg_size_pretty(pg_database_size(current_database())) AS db_size;
```

```sql
SELECT
  relname,
  pg_size_pretty(pg_total_relation_size(relid)) AS total_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 10;
```

- **PID текущего бэкенда**:

```sql
SELECT pg_backend_pid();
```

Это помогает связать сессии с записями в системных вьюхах (`pg_stat_activity`).

- **Чтение настроек**:

```sql
SELECT current_setting('work_mem');
SELECT current_setting('shared_buffers');
```

### Примеры

**1. Узнать, сколько веса занимают самые большие таблицы:**

```sql
SELECT
  relname AS table_name,
  pg_size_pretty(pg_total_relation_size(relid)) AS total_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 5;
```

**2. В логах запросов выводить PID и пользователя:**

```sql
SELECT
  pg_backend_pid()   AS pid,
  current_user       AS user_name,
  now()              AS ts,
  query
FROM pg_stat_activity
WHERE pid = pg_backend_pid();
```

### Простыми словами

Системные функции — это **панель приборов твоей БД**: они показывают, какая версия сейчас работает, сколько места занимают данные, кто подключён и с какими настройками.

### Картинка в голове

Представь, что БД — это **автомобиль**, а системные функции — это датчики и индикаторы на приборной панели: скорость, обороты, температура, остаток топлива. Без них машина вроде едет, но ты не знаешь, когда закончится бензин или перегреется двигатель.

### Как запомнить

**`version()` — «кто я», `current_user` — «кто сейчас за рулём», `pg_*size*` — «сколько весит», `current_setting` — «какие настройки сейчас включены».**

### Типичные ошибки

- Не использовать системные функции и пытаться «на глаз» оценивать размер БД и таблиц.
- Путать `CURRENT_USER` и `SESSION_USER`, особенно при работе с `SET ROLE`.
- Игнорировать возможности чтения настроек из SQL и держать всю информацию только в внешних конфигурационных файлах.

### Проверь себя

1. Как узнать размер текущей базы данных в читаемом виде?  
2. Зачем может понадобиться `pg_backend_pid()`?  
3. Как посмотреть текущее значение `work_mem` из SQL?

<details>
<summary>Ответы</summary>

1. В PostgreSQL:  
   ```sql
   SELECT pg_size_pretty(pg_database_size(current_database()));
   ```  
2. Чтобы связать свою сессию с записью в `pg_stat_activity`, диагностировать блокировки, логировать информацию по конкретному соединению.  
3. Через `current_setting('work_mem')`:  
  ```sql
  SELECT current_setting('work_mem');
  ```
</details>

### Дополнительные практические приёмы с системными функциями

#### Список самых «тяжёлых» таблиц

```sql
SELECT
  relname AS table_name,
  pg_size_pretty(pg_total_relation_size(relid)) AS total_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 10;
```

Такой запрос помогает быстро понять, какие таблицы больше всего занимают место и с чем нужно работать (архивировать, чистить, партиционировать).

#### Проверка ключевых настроек

```sql
SELECT
  current_setting('max_connections')   AS max_connections,
  current_setting('shared_buffers')    AS shared_buffers,
  current_setting('work_mem')          AS work_mem;
```

Это быстрый способ «сфотографировать» важные параметры окружения прямо из SQL.

### Запомните

Системные функции — это **обязательный инструмент любого, кто пускает SQL в продакшен**. Они позволяют быстро понять состояние БД, не заходя на сервер руками и не глядя в конфиги.

---

---

<!-- prev-next-nav -->
*[← 143. Преобразование типов](05_143_preobrazovanie_tipov.md) | [→ 145. Операторы SQL](07_145_operatory_sql.md)*
