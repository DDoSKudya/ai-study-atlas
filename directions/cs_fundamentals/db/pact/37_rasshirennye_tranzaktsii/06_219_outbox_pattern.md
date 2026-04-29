[← Назад к индексу части 37](index.md)

## §219. Outbox pattern

### Цель раздела

Понять, как гарантировать связку “**изменение в БД** + **публикация события**” без 2PC: через **outbox table** и отдельного публикующего воркера (polling) или через **CDC**; научиться проектировать схему outbox, обработку повторов, порядок событий и мониторинг.

### В этом разделе главное

1) Outbox решает проблему “обновил БД, но не отправил событие” (или наоборот) при падениях.  
2) Почти всегда получится **at-least-once**, значит **дедуп** на потребителе обязателен.  
3) Publisher должен уметь безопасно забирать пачки (`SKIP LOCKED`), ретраить и быть наблюдаемым (метрики).  
4) Polling проще, CDC сложнее. Начинай с polling, CDC подключай, когда реально нужно.

### Термины

| Термин | Определение |
|---|---|
| **Outbox** | Таблица в той же БД, куда в одной транзакции пишут бизнес-изменение и событие для публикации. |
| **Publisher** | Процесс, который читает outbox и публикует события в брокер/шину/HTTP. |
| **Polling** | Публикация через периодический опрос таблицы outbox. |
| **CDC-based outbox** | Публикация через чтение лога изменений (WAL/binlog) и извлечение outbox-событий. |
| **At-least-once delivery** | Доставка “как минимум один раз”: возможны дубликаты, требуется дедупликация. |
| **Deduplication** | Устранение дублей на стороне потребителя (обычно по `event_id`). |

### Теория и правила

#### 1) Проблема, которую решает outbox

Наивный код:

1) `UPDATE` в БД  
2) `publish(event)` в брокер

Если между (1) и (2) приложение упадёт, изменения уже в БД, а событие не ушло → подписчики “не узнают”.

Если сделать наоборот:

1) publish  
2) UPDATE

Тоже плохо: событие ушло, а данных ещё нет.

Outbox решает так:

- в **одной транзакции** пишем и изменения, и запись события в outbox.
- публикация делается отдельно, повторяемо.

#### 1.1) “Псевдо‑точность”: чего outbox НЕ обещает

Outbox не обещает “ровно один раз” автоматически. Он обещает другое:

- **не потерять событие** при падениях;
- иметь возможность **доставить позже**;
- позволить системе жить с повторами через дедуп.

Если ты ожидаешь “exactly once” без дедуп — почти наверняка получишь баги.

#### 2) Схема outbox-таблицы (практичный минимум)

Типичный минимум:

- `event_id` (UUID/ULID) — уникальный идентификатор события
- `aggregate_type`, `aggregate_id` — к чему относится событие
- `event_type` — тип события
- `payload` (JSON) — данные события
- `created_at`
- `published_at` (nullable)
- `attempts`, `last_error` (опционально)

#### 3) Как писать в outbox “в одной транзакции”

Пример (идея, SQL условный):

```sql
BEGIN;

UPDATE orders
SET status = 'PAID'
WHERE id = :order_id;

INSERT INTO outbox(event_id, aggregate_type, aggregate_id, event_type, payload, created_at)
VALUES (:event_id, 'order', :order_id, 'OrderPaid', :payload_json, now());

COMMIT;
```

Если `COMMIT` не случился — не будет ни изменения, ни события.

#### 3.1) Практичная DDL‑заготовка (PostgreSQL‑стиль)

Пример структуры (адаптируй под себя):

```sql
CREATE TABLE outbox (
  event_id uuid PRIMARY KEY,
  aggregate_type text NOT NULL,
  aggregate_id text NOT NULL,
  event_type text NOT NULL,
  payload jsonb NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  published_at timestamptz NULL,
  attempts int NOT NULL DEFAULT 0,
  last_error text NULL
);

CREATE INDEX ix_outbox_unpublished_created
ON outbox (created_at)
WHERE published_at IS NULL;
```

Смысл индекса: быстро находить “неотправленные” в правильном порядке.

#### 4) Публикация: polling-вариант (без CDC)

Публикующий воркер обычно делает:

- взять пачку “не опубликованных” событий,
- пометить как “в обработке” или захватить блокировкой,
- опубликовать,
- отметить `published_at`.

Чтобы несколько воркеров не взяли одно и то же — часто используют блокировки строк:

```sql
-- Идея для PostgreSQL: “захватить” пачку строк
SELECT *
FROM outbox
WHERE published_at IS NULL
ORDER BY created_at
FOR UPDATE SKIP LOCKED
LIMIT 100;
```

После успешной публикации:

```sql
UPDATE outbox
SET published_at = now()
WHERE event_id = :event_id;
```

#### 4.1) Надёжный цикл publisher’а (псевдокод)

```text
loop:
  begin tx
    rows = select ... for update skip locked limit N
    mark attempts = attempts + 1 for rows (optional)
  commit tx

  for each row in rows:
    try publish(row)
      update outbox set published_at = now(), last_error = null where event_id = ...
    catch error:
      update outbox set last_error = ..., attempts = attempts + 1 where event_id = ...
      maybe sleep/backoff
```

Тут две важные идеи:

- захват строк (`FOR UPDATE SKIP LOCKED`) делает работу параллельной без гонок;
- публикация и отметка `published_at` разделены, поэтому повторы неизбежны → потребителю нужен dedup.

#### 4.2) Вариант “mark as processing”

Иногда добавляют поля:

- `locked_by`, `locked_at`

Это помогает:

- видеть “зависшие” в обработке;
- возвращать их обратно, если воркер умер.

Но в PostgreSQL часто достаточно `SKIP LOCKED` + корректных ретраев.

#### 5) Публикация через CDC

CDC читает WAL/binlog и “видит” вставку в outbox как факт.  
Плюсы:

- меньше нагрузки от polling;
- публикация ближе к “реальному времени”.

Минусы:

- сложнее инфраструктура;
- нужно аккуратно настроить консистентность, порядок и ровно-однократность обработки (которая всё равно обычно превращается в at-least-once + дедуп).

#### 6) Важное: outbox почти всегда = at-least-once

Даже если publisher “старается”, в реальности:

- publish мог случиться, а подтверждение publisher’у — нет;
- publisher упал после публикации, но до `UPDATE published_at`.

Поэтому:

- публикация может быть повторной;
- потребители должны делать **dedup** (обычно по `event_id`).

#### 6.1) Как сделать dedup у потребителя (минимальная схема)

Идея таблицы:

```sql
CREATE TABLE processed_events (
  event_id uuid PRIMARY KEY,
  processed_at timestamptz NOT NULL DEFAULT now()
);
```

В обработчике:

1) `BEGIN;`
2) `INSERT INTO processed_events(event_id) VALUES (:event_id);`
   - если вставка упала по PK → это дубль → `ROLLBACK;` и “ok”
3) применить изменения доменных таблиц
4) `COMMIT;`

Это самый простой способ “сделать эффект как будто один раз”.

#### 7) План внедрения outbox в существующий сервис (по шагам)

Если у тебя уже есть сервис, который “обновляет БД и шлёт события”, можно двигаться так:

1. **Найти места, где сейчас есть риск несогласованности.**  
   Ищи паттерн: “сначала `UPDATE/INSERT/DELETE`, потом publish в брокер/HTTP”.

2. **Спроектировать таблицу outbox.**  
   Минимум: `event_id` (PK), `aggregate_type`, `aggregate_id`, `event_type`, `payload`, `created_at`, `published_at`. Часто добавляют индекс по `published_at` и `created_at`.

3. **Изменить код бизнес‑операции.**  
   Вместо “обновили БД, а потом publish” делаем:
   - внутри транзакции меняем доменную таблицу;
   - в той же транзакции вставляем запись в outbox.

4. **Написать publisher‑воркер.**  
   - периодически (каждые N миллисекунд) делать `SELECT ... FOR UPDATE SKIP LOCKED` пачкой;
   - публиковать события в брокер;
   - отмечать `published_at` после успешной отправки;
   - логировать ошибки и увеличивать `attempts`.

5. **Обновить потребителей событий.**  
   - добавить дедупликацию по `event_id` (таблица “обработанные события” или встроенный механизм брокера, если есть);
   - сделать обработку идемпотентной (повтор обработки одного и того же события не ломает данные).

6. **Добавить мониторинг.**  
   - количество неотправленных событий;
   - самая старая запись без `published_at` (age);
   - количество ошибок/ретраев.

7. **При необходимости перейти с polling на CDC.**  
   Это не обязательно: для начала достаточно polling‑подхода. CDC имеет смысл, когда нагрузка растёт или когда хочется минимальных задержек.

#### 8) Мониторинг outbox (что мерить, чтобы не “взорвалось” тихо)

Минимальные метрики:

- **outbox backlog**: сколько строк `published_at IS NULL`
- **oldest unpublished age**: `now() - min(created_at)` среди неопубликованных
- **publish errors rate**: сколько ошибок публикации в минуту
- **attempts distribution**: сколько событий с attempts > 3 (подозрительно)

Практический запрос “возраст самого старого события”:

```sql
SELECT now() - MIN(created_at) AS oldest_unpublished_age
FROM outbox
WHERE published_at IS NULL;
```

Если возраст растёт — publisher не справляется или брокер/сеть сломаны.

#### 9) Очистка outbox (ретеншн): как не потерять события

Правило безопасной очистки:

- удаляем **только опубликованные** (`published_at IS NOT NULL`);
- держим “хвост” по времени (например, 7–30 дней) на случай расследований и повторной доставки.

Пример:

```sql
DELETE FROM outbox
WHERE published_at IS NOT NULL
  AND published_at < now() - interval '14 days';
```

Ошибка, которую делают часто: чистят “по created_at” без учёта `published_at`. Это может удалить ещё не доставленные события.

#### 10) Порядок событий: “в целом” vs “по агрегату”

Частая тонкость: тебе может быть не нужен глобальный порядок (между всеми заказами), но нужен порядок **внутри одного заказа**.

Тогда удобно хранить:

- `aggregate_id`
- `aggregate_version` (монотонно растущая версия)

И consumer делает:

- если пришла версия меньше/равна последней применённой → игнорировать (дубль/старое)
- если пришла версия = last+1 → применить
- если пришла версия “с дыркой” → положить в буфер/подождать/запросить реплей

Это уже продвинутый слой, но он часто нужен, чтобы не ловить “события пришли в другом порядке”.

### Outbox ordering глубже: aggregate_version и “дедуп + порядок” вместе

Если события по агрегату должны применяться строго по порядку, то одного `event_id` мало.

Практичная модель:

- у агрегата есть `aggregate_id`
- у события есть `aggregate_version` (1,2,3,…)

Consumer хранит “последнюю применённую версию”:

```sql
CREATE TABLE aggregate_offsets (
  aggregate_type text NOT NULL,
  aggregate_id uuid NOT NULL,
  last_version bigint NOT NULL,
  PRIMARY KEY (aggregate_type, aggregate_id)
);
```

Алгоритм:

- пришло событие version = v
- если v <= last_version → дубль/старое → игнорировать
- если v == last_version + 1 → применить и обновить last_version
- если v > last_version + 1 → “дырка” → буфер/ретраи/реплей

Это убирает класс проблем “пришло не по порядку”.

---

### Типичные ошибки

- **Ошибка: не делать dedup у потребителя.**  
  Тогда ровно в тот день, когда publisher упадёт “после publish, но до отметки published_at”, ты получишь двойные эффекты.

- **Ошибка: чистить outbox “DELETE старше 1 дня” без уверенности, что всё доставлено.**  
  Это может привести к потере событий. Чистить можно только опубликованные (`published_at IS NOT NULL`) и с запасом.

### Что будет, если…

- **Что будет, если publisher читает без `SKIP LOCKED` и у тебя несколько воркеров?**  
  Возможны гонки и дубликаты публикации. Дубликаты и так возможны, но так ты сделаешь их намного больше.

### Мини‑лаборатория §219: `FOR UPDATE SKIP LOCKED` двумя воркерами

Цель: почувствовать, что два воркера могут безопасно “делить” outbox.

1) Подготовка:

```sql
DROP TABLE IF EXISTS outbox;
CREATE TABLE outbox (
  event_id uuid PRIMARY KEY,
  created_at timestamptz NOT NULL DEFAULT now(),
  published_at timestamptz NULL
);

INSERT INTO outbox(event_id) VALUES
('00000000-0000-0000-0000-000000000001'),
('00000000-0000-0000-0000-000000000002'),
('00000000-0000-0000-0000-000000000003');
```

2) **Сеанс A**:

```sql
BEGIN;
SELECT event_id
FROM outbox
WHERE published_at IS NULL
ORDER BY created_at
FOR UPDATE SKIP LOCKED
LIMIT 2;
-- НЕ КОММИТЬ сразу
```

3) **Сеанс B** (параллельно):

```sql
BEGIN;
SELECT event_id
FROM outbox
WHERE published_at IS NULL
ORDER BY created_at
FOR UPDATE SKIP LOCKED
LIMIT 2;
COMMIT;
```

Сеанс B не возьмёт строки, которые уже залочил сеанс A — он “перепрыгнет” их. Это и есть смысл `SKIP LOCKED`.

### Мини‑лаборатория §219.2: end‑to‑end Outbox → Publisher → Consumer (dedup)

Цель: собрать в голове весь конвейер “без магии”.

#### Шаг 0. Таблицы (outbox + processed_events)

```sql
DROP TABLE IF EXISTS processed_events;
DROP TABLE IF EXISTS outbox;
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
  id uuid PRIMARY KEY,
  status text NOT NULL
);

CREATE TABLE outbox (
  event_id uuid PRIMARY KEY,
  aggregate_type text NOT NULL,
  aggregate_id uuid NOT NULL,
  event_type text NOT NULL,
  payload jsonb NOT NULL,
  created_at timestamptz NOT NULL DEFAULT now(),
  published_at timestamptz NULL
);

CREATE TABLE processed_events (
  event_id uuid PRIMARY KEY,
  processed_at timestamptz NOT NULL DEFAULT now()
);
```

#### Шаг 1. “Бизнес‑операция”: меняем доменную таблицу + пишем outbox (одна транзакция)

```sql
BEGIN;

INSERT INTO orders(id, status)
VALUES ('00000000-0000-0000-0000-000000000010', 'PAID');

INSERT INTO outbox(event_id, aggregate_type, aggregate_id, event_type, payload)
VALUES (
  '00000000-0000-0000-0000-000000000100',
  'order',
  '00000000-0000-0000-0000-000000000010',
  'OrderPaid',
  jsonb_build_object('order_id', '00000000-0000-0000-0000-000000000010')
);

COMMIT;
```

Теперь факт “заказ оплачен” и событие “OrderPaid” неразрывны.

#### Шаг 2. “Publisher”: забрал outbox и “отправил” (мы имитируем отправку)

В реальности это Kafka/Rabbit/HTTP. В лаборатории просто сделаем “отметку опубликовано”:

```sql
BEGIN;
SELECT event_id
FROM outbox
WHERE published_at IS NULL
ORDER BY created_at
FOR UPDATE SKIP LOCKED
LIMIT 1;
-- допустим, publisher отправил событие в брокер
UPDATE outbox
SET published_at = now()
WHERE event_id = '00000000-0000-0000-0000-000000000100';
COMMIT;
```

#### Шаг 3. “Consumer”: обработал событие + dedup (от дублей)

Первый раз:

```sql
BEGIN;
INSERT INTO processed_events(event_id)
VALUES ('00000000-0000-0000-0000-000000000100');
-- применяем эффект (для примера просто читаем заказ)
SELECT * FROM orders WHERE id = '00000000-0000-0000-0000-000000000010';
COMMIT;
```

Второй раз (дубль того же события):

```sql
BEGIN;
INSERT INTO processed_events(event_id)
VALUES ('00000000-0000-0000-0000-000000000100');
COMMIT;
```

Вторая вставка упадёт по PK → consumer должен воспринимать это как “уже обработано, ок”.

**Главное ощущение:** outbox решает “не потерять”, dedup решает “не задвоить”.

### Простыми словами

Outbox — это “черновик сообщений” внутри БД: сначала ты надёжно записываешь и факт, и сообщение о факте в одном месте. А уже потом отдельный доставщик сообщений гарантированно разносит это наружу, пусть даже с повторами.

### Картинка в голове

Ты кладёшь письмо в “исходящие” (outbox) в офисе. Даже если курьер сегодня не пришёл, письмо не потеряется. Когда курьер придёт — он заберёт письма и доставит. Если курьер случайно возьмёт письмо дважды — получатель должен уметь распознавать “это уже было”.

### Как запомнить

- Связка “изменение + событие” делается **в одной транзакции** через outbox.
- Доставка почти всегда **at-least-once** → **dedup на потребителе**.
- Polling проще, CDC сложнее, но масштабнее.

### Проверь себя

1) Какую конкретную проблему решает outbox?  
<details><summary>Ответ</summary>
Проблему “обновили БД, но не опубликовали событие” (или наоборот) из-за падения между двумя операциями. Outbox делает обе записи атомарно в одной транзакции БД.
</details>

2) Почему даже с outbox возможны дубликаты событий?  
<details><summary>Ответ</summary>
Потому что публикация и отметка `published_at` — две разные операции. Publisher мог упасть/потерять подтверждение после публикации, но до отметки в БД; при повторе он опубликует снова.
</details>

3) Зачем `FOR UPDATE SKIP LOCKED` в polling?  
<details><summary>Ответ</summary>
Чтобы несколько воркеров могли параллельно брать разные события без гонки за одну строку: строки, уже захваченные другим воркером, пропускаются.
</details>

### Запомните

Outbox — базовый строительный блок надёжной интеграции. Он превращает “публикацию” из непредсказуемого побочного эффекта в управляемый, наблюдаемый процесс.

---

---

<!-- prev-next-nav -->
*[← §218. Saga паттерн](05_218_saga_pattern.md) | [→ §220. Длинные транзакции](07_220_dlinnye_tranzaktsii.md)*
