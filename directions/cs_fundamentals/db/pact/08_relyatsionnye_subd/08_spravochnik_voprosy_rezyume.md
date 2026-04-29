[← Назад к индексу части 8](index.md)

## Справочник по части VIII

| Тема | Ключевые понятия |
|------|------------------|
| **PostgreSQL: процессы** | postmaster, backend, background worker; один процесс на соединение |
| **PostgreSQL: память** | shared memory, shared_buffers; общая память для всех процессов |
| **PostgreSQL: расширения** | CREATE EXTENSION; pgvector, PostGIS, pg_cron, pg_stat_statements, uuid-ossp |
| **PostgreSQL: каталоги** | pg_class (relkind: r, i, v, S), pg_attribute, pg_index; pg_tables, pg_stat_*, pg_size_* |
| **PostgreSQL: конфигурация** | postgresql.conf (параметры сервера); pg_hba.conf (правила доступа); RELOAD, restart |
| **PostgreSQL: типы** | JSONB (@>, ?, ->, ->>), массивы (&&, @>, unnest), диапазоны (int4range, tstzrange), UUID, inet/cidr |
| **PostgreSQL: партиционирование** | PARTITION BY RANGE/LIST/HASH; default partition; CREATE TABLE ... PARTITION OF |
| **PostgreSQL: репликация** | схема (namespace); publication, subscription; replication slot |
| **MySQL/MariaDB** | InnoDB (транзакции, FK), MyISAM (табличные блокировки); binlog, GTID; innodb_buffer_pool_size; MariaDB (Aria, ColumnStore) |
| **SQLite** | встраиваемая; один файл / :memory:; один писатель; WAL mode; PRAGMA (journal_mode, synchronous, cache_size) |
| **Другие СУБД** | Oracle (RAC, PL/SQL), SQL Server (T-SQL, Always On); CockroachDB, TiDB, YugabyteDB (распределённый SQL) |
| **Подключение** | драйвер (psycopg2, asyncpg, JDBC); пул соединений; PgBouncer (transaction/session); prepared statements; таймауты |
| **ORM и миграции** | ORM vs raw SQL; Alembic, Flyway, Liquibase; connection string; failover в драйвере |

---

## Вопросы для самопроверки (часть VIII)

Ответы под спойлером: по 2–3 вопроса на раздел (по этапам).

### Этап 1. §42 — PostgreSQL: архитектура и системные каталоги

1. Какие процессы входят в экземпляр PostgreSQL и за что они отвечают?  
<details><summary>Ответ</summary> **postmaster** — главный процесс, слушает порт, создаёт **backend** на каждое соединение. **backend** — один процесс на одного клиента, выполняет его запросы. **background workers** — фоновые процессы (autovacuum, WAL writer, checkpointer, stats collector и др.), не привязаны к клиентам.</details>

2. Что такое shared_buffers и можно ли изменить его без перезапуска?  
<details><summary>Ответ</summary> **shared_buffers** — общий буферный кэш страниц в shared memory; все backend'ы читают и пишут страницы через него. **Без перезапуска изменить нельзя** — параметр с context = postmaster, память под буфер выделяется при старте postmaster.</details>

3. Чем postgresql.conf отличается от pg_hba.conf?  
<details><summary>Ответ</summary> **postgresql.conf** задаёт **параметры работы сервера**: память (shared_buffers, work_mem), число соединений (max_connections), WAL, логирование, таймауты. **pg_hba.conf** задаёт **правила доступа**: с каких адресов каким пользователям разрешено подключаться и каким методом аутентификации (trust, md5, scram-sha-256 и др.).</details>

### Этап 2. §43 — Типы данных, партиционирование, схемы

4. Чем оператор -> отличается от ->> в JSONB?  
<details><summary>Ответ</summary> **->** возвращает значение **как JSON** (тип jsonb) — вложенный объект или массив; с ним можно продолжать цепочку (data->'address'->>'city'). **->>** возвращает значение **как текст** (тип text) — для вывода и сравнения со строками в WHERE.</details>

5. Что такое partition pruning и зачем первичный ключ партиционированной таблицы должен включать ключ партиционирования?  
<details><summary>Ответ</summary> **Partition pruning** — планировщик отсекает партиции, не содержащие данных по условию WHERE (например, по диапазону created_at), и сканирует только нужные. **PK должен включать ключ партиционирования**, иначе одна и та же пара (id, created_at) теоретически могла бы попасть в разные партиции — нарушается уникальность.</details>

6. Чем логическая репликация в PostgreSQL отличается от streaming replication? Что такое replication slot и какой у него риск?  
<details><summary>Ответ</summary> **Streaming replication** — физическая: копируются байты WAL; реплика — побайтовая копия primary. **Логическая репликация** — на уровне строк: publication + subscription; реплика получает логические изменения (INSERT/UPDATE/DELETE). **Replication slot** — слот на primary хранит позицию потребителя; WAL не удаляется до прочтения. **Риск:** отстающий или отключённый подписчик — рост pg_wal и заполнение диска.</details>

### Этап 3. §44 — MySQL и MariaDB

7. В чём разница между InnoDB и MyISAM в MySQL?  
<details><summary>Ответ</summary> **InnoDB** — транзакционный движок по умолчанию: ACID, внешние ключи, MVCC, строковые блокировки; redo log и crash recovery. **MyISAM** — без транзакций; блокировка на уровне всей таблицы при записи; для новых проектов не рекомендуется.</details>

8. Зачем нужен GTID при репликации MySQL? Чем формат binlog ROW отличается от STATEMENT?  
<details><summary>Ответ</summary> **GTID** — глобальный идентификатор транзакции; однозначно задаёт позицию репликации и упрощает переключение между мастерами и отказоустойчивость. **ROW** — в binlog пишутся изменённые строки (значения до/после); **STATEMENT** — пишутся сами SQL-запросы. ROW предсказуем при недетерминированных выражениях и триггерах.</details>

### Этап 4. §45 — SQLite

9. Когда уместно использовать SQLite и какие у него ограничения?  
<details><summary>Ответ</summary> **SQLite** уместен для локальных приложений, тестов, прототипов, встроенных устройств, кэша. **Ограничения:** один писатель в момент времени; нет сетевого доступа «из коробки»; один файл или :memory:; не для высоконагруженного многописательного доступа с многих узлов.</details>

10. Зачем включать WAL mode в SQLite и что делает PRAGMA synchronous?  
<details><summary>Ответ</summary> **WAL mode** даёт параллельные чтение и одну запись; меньше блокировок и часто выше производительность. **PRAGMA synchronous** задаёт, когда возвращать управление после записи: FULL — после сброса на диск (надёжнее); NORMAL/OFF — быстрее, но при сбое возможна потеря данных.</details>

### Этап 5. §46 — Другие реляционные СУБД

11. Что такое Oracle RAC? Чем SQL Server Always On похож на репликацию в PostgreSQL?  
<details><summary>Ответ</summary> **Oracle RAC** — несколько экземпляров работают с одной общей БД (shared storage); отказоустойчивость и масштабирование чтения. **Always On** — группы доступности с репликацией (похоже на streaming replication в PostgreSQL): primary и одна или несколько реплик; переключение при отказе.</details>

12. В чём главное отличие NewSQL (CockroachDB, TiDB, YugabyteDB) от «обычного» PostgreSQL на одном сервере?  
<details><summary>Ответ</summary> **NewSQL** — распределённые СУБД: данные шардируются по узлам, реплицируются, поддерживается согласованность и SQL-интерфейс. Один узел PostgreSQL — одна машина (плюс реплики при необходимости). NewSQL даёт горизонтальное масштабирование и глобальное распределение при совместимости с PostgreSQL или MySQL.</details>

### Этап 6. §47 — Подключение из приложения

13. Зачем ставить PgBouncer перед PostgreSQL? В чём ограничение transaction pooling для prepared statements?  
<details><summary>Ответ</summary> **PgBouncer** ограничивает число реальных соединений к серверу и переиспользует их — меньше памяти и нагрузки (один процесс на соединение в PostgreSQL). **Transaction pooling:** соединение к серверу возвращается в пул после каждой транзакции; **именованные prepared statements** привязаны к соединению — после COMMIT они «теряются», следующий клиент получит другое соединение без этого prepared statement. Использовать анонимные prepared statements или session pooling.</details>

14. Как prepared statement защищает от SQL-инъекций?  
<details><summary>Ответ</summary> **Prepared statement** — запрос с плейсхолдерами; параметры передаются отдельно и обрабатываются СУБД как **данные**, а не как часть текста SQL. Подстановка строки с кавычками и точкой с запятой не превращается в выполнение другой команды — инъекция невозможна. Всегда использовать параметризованные запросы для пользовательского ввода.</details>

### Этап 7. §48 — ORM и миграции

15. Когда предпочтительнее raw SQL, а когда ORM? Что такое антипаттерн N+1 в контексте ORM?  
<details><summary>Ответ</summary> **ORM** — для простого CRUD, типизации, переносимости; **raw SQL** — для сложных запросов (несколько JOIN, оконные функции, специфика СУБД). **N+1:** один запрос за списком сущностей и N запросов за связями (например, заказы каждого пользователя) — вместо одного запроса с JOIN или eager loading. Решение: один запрос с JOIN или загрузка связей одним батчем.</details>

16. Зачем хранить миграции в коде и применять их при деплое? Что такое connection string и какие параметры в нём важны?  
<details><summary>Ответ</summary> **Миграции в коде** — схема версионируется вместе с приложением; при деплое применяются только неприменённые миграции — схема в dev, test и prod совпадает. **Connection string** — строка подключения к БД: хост, порт, имя базы, пользователь, пароль; часто включают таймауты (connect_timeout, statement_timeout), sslmode, параметры пула. Важно не хранить пароли в открытом виде (переменные окружения, секреты).</details>

---

## Резюме части VIII

- **PostgreSQL: архитектура** — postmaster (приём подключений), backend (один на соединение), background workers; shared memory (shared_buffers и др.). Расширения — CREATE EXTENSION (pgvector, PostGIS, pg_cron, pg_stat_statements и др.). Системные каталоги: pg_class (таблицы, индексы — relkind), pg_attribute (столбцы), pg_index; представления pg_tables, pg_stat_*, функции pg_size_*. Конфигурация: postgresql.conf (параметры сервера — память, соединения, WAL, логи); pg_hba.conf (правила доступа — кто, откуда, как аутентифицироваться); после правки — RELOAD или restart (зависит от параметра).
- **PostgreSQL: типы и партиционирование** — JSONB, массивы, диапазоны (int4range, tstzrange), UUID, inet/cidr. Партиционирование: RANGE, LIST, HASH; default partition. Схемы (namespace); логическая репликация (publication, subscription); replication slot.
- **MySQL/MariaDB** — InnoDB (транзакции, FK, по умолчанию), MyISAM (табличные блокировки). Binlog (ROW/STATEMENT/MIXED), репликация (GTID), group replication. Настройки: innodb_buffer_pool_size, изоляция REPEATABLE READ. MariaDB — форк с движками Aria, ColumnStore.
- **SQLite** — встраиваемая; один файл или :memory:; один писатель; типы (affinity). WAL mode и PRAGMA (journal_mode, synchronous, cache_size). Сценарии: приложения, тесты, прототипы.
- **Другие СУБД** — Oracle (RAC, PL/SQL), SQL Server (T-SQL, Always On); CockroachDB, TiDB, YugabyteDB (распределённый SQL, совместимость с PostgreSQL/MySQL).
- **Подключение** — драйверы (psycopg2, asyncpg, JDBC и др.); пулы соединений; PgBouncer (transaction/session); prepared statements (кэш плана, защита от инъекций); таймауты (connection, statement).
- **ORM и миграции** — ORM (удобство CRUD, переносимость) vs raw SQL (контроль, сложные запросы); миграции (Alembic, Flyway, Liquibase); connection string; failover в драйвере.

**Связь с другими частями:** Часть VII (оптимизация запросов) даёт понимание планов и статистики — применимо к любой реляционной СУБД; настройки (work_mem, shared_buffers) и расширения (pg_stat_statements) — в контексте PostgreSQL. Часть IX (NoSQL) и Часть X (векторные БД) — альтернативы и дополнения к реляционным продуктам; выбор стека (полиглот персистентности) опирается на знание реляционных продуктов из этой части.

---

---

<!-- prev-next-nav -->
*[← §48. ORM и миграции](07_48_orm_i_migratsii.md) | [→ Индекс части](index.md)*
