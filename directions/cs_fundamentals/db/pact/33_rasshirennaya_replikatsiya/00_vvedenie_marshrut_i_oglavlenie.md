[← Назад к индексу части 33](index.md)

## Часть XXXIII. Расширенные темы репликации

> Цель этой части — **перестать воспринимать репликацию как «магическую галочку high availability»** и начать понимать, **как реально работают разные виды репликации (streaming, logical, binlog, replica set, Redis Sentinel/Cluster, Cassandra RF/CL)**, какие у них **ограничения по консистентности и отказоустойчивости**, как **читать лаг и метрики**, а главное — **как не сломать данные и не потерять их при сбоях**.

---

После этой части ты сможешь:

- **объяснить на пальцах, как работает streaming‑репликация в PostgreSQL**: что такое WAL‑стрим, синхронная vs асинхронная, что такое quorum commit и lag;
- **настроить и использовать logical‑репликацию PostgreSQL** для миграций, интеграций и постепенных изменений схемы;
- **понимать, как устроена binlog‑репликация и GTID в MySQL**, чем отличаются statement/row/mixed форматы и как смотреть lag;
- **разобраться в MySQL Group Replication / InnoDB Cluster**: multi‑master, консенсус, split‑brain‑защита и auto‑failover (на концептуальном уровне);
- **объяснить архитектуру репликации MongoDB (replica set + oplog)**, как работает выбор primary, read preference и write concern;
- **понимать модели репликации Redis (master‑replica, Sentinel, Cluster)** и как они влияют на надежность и поведение кэша/хранилища;
- **уверенно говорить о репликации в Cassandra**: replication factor, стратегии для нескольких дата‑центров и уровни консистентности (ONE/QUORUM/ALL и др.).

Материал опирается на:

- части про **транзакции и согласованность** (ACID, уровни изоляции, репликация и CAP‑интуиция);
- части про **хранение и WAL/лог изменений**;
- общие части по **масштабированию, отказоустойчивости и распределённым системам**.

### Уровень части: база -> advanced -> expert

- **База:** `§186–188` — streaming/logical/binlog, lag и базовая operational‑интуиция.
- **Advanced:** `§189–191` — group replication, MongoDB и Redis со своими моделями failover и consistency.
- **Expert:** `§192` — Cassandra replication factor / consistency levels и multi-DC компромиссы.

Если тема пока кажется слишком тяжёлой, сначала вернись к `part-11-scaling-and-fault-tolerance.md` и `part-25-disaster-recovery-and-dr.md`, а потом уже заходи сюда за engine-specific деталями.

### Связи с соседними частями

- Базовая лестница HA / lag / backup / failover начинается в `part-11-scaling-and-fault-tolerance.md`.
- DR-рамка и business-смысл RTO/RPO идут из `part-25-disaster-recovery-and-dr.md`.
- Monitoring lag, slots, failover time и symptom->cause мышление продолжаются в `part-39-advanced-monitoring-topics.md`.
- Deep observability и tracing вокруг distributed изменений продолжаются в `part-55-observability-apm-and-distributed-tracing.md`.
- Транзакционные последствия репликации, outbox/CDC и long txn смотри в `part-37-advanced-transaction-topics.md`.

---

### Краткая шпаргалка (термины по части)

| Термин | Что это простыми словами |
|--------|---------------------------|
| **Streaming replication (PostgreSQL)** | Реплика, которая получает изменения **потоком WAL‑записей** почти в реальном времени и воспроизводит их. |
| **Синхронная репликация** | Коммит считается успешным **только после** подтверждения применения (или хотя бы записи WAL) на одной или нескольких репликах. |
| **Асинхронная репликация** | Primary не ждёт реплику, коммит «моментальный», но при сбое можно потерять последние транзакции (replication lag). |
| **Quorum commit** | Когда для успешного коммита нужно **подтверждение нескольких реплик** (кворум), а не только primary. |
| **Logical replication (PostgreSQL)** | Репликация **на уровне строк и таблиц** (INSERT/UPDATE/DELETE по данным), а не сырого WAL; позволяет фильтровать и мигрировать. |
| **Публикация / подписка** | Модель logical‑репликации: один кластер публикует изменения, другой на них подписывается и применяет. |
| **Binlog (MySQL)** | Журнал изменений MySQL (бинарный лог), который служит основой для репликации и восстановления. |
| **GTID (MySQL)** | Глобальный идентификатор транзакции; помогает отслеживать, **какие транзакции уже применены** на реплике. |
| **Group Replication (MySQL)** | Кластер MySQL, где несколько нод образуют **группу с консенсусом**, поддерживающую multi‑master и auto‑failover. |
| **Replica set (MongoDB)** | Набор Mongo‑нод (primary + несколько secondary), где данные реплицируются через oplog. |
| **Oplog (MongoDB)** | «Журнал операций» MongoDB: последовательность операций, которые secondary воспроизводят, чтобы догнать primary. |
| **Read preference (MongoDB)** | Настройка, **с каких нод читать** (только primary, только secondary, ближайшая и т.д.). |
| **Write concern (MongoDB)** | Требуемый уровень подтверждения записи (сколько реплик должны подтвердить запись и нужно ли журналирование). |
| **Redis Sentinel** | Компонент для мониторинга Redis, который **обнаруживает падение master** и переключает репликy в новый master. |
| **Redis Cluster** | Режим Redis, в котором данные **шардируются по hash‑слотам**, при этом у каждого слота есть основная и резервные ноды. |
| **Replication factor (Cassandra)** | Сколько копий каждой записи хранится в кластере Cassandra. |
| **Consistency level (Cassandra)** | Сколько реплик должны подтвердить чтение/запись, чтобы операция считалась успешной. |
| **NetworkTopologyStrategy (Cassandra)** | Стратегия, которая распределяет копии данных по **разным дата‑центрам**. |

---

### Маршрут изучения

Рекомендуемый порядок:

1. **§186. Streaming replication (PostgreSQL)** — базовая модель: как основной сервер стримит WAL‑лог на реплики, что такое lag и синхронный/асинхронный режим.
2. **§187. Logical replication (PostgreSQL)** — когда нужна репликация «по данным», а не «по страницам», как делать миграции и интеграции.
3. **§188. Binlog‑репликация (MySQL)** — как MySQL использует binlog и GTID, какие есть форматы и их влияние на точность и нагрузку.
4. **§189. Group replication (MySQL)** — multi‑master‑кластер с консенсусом, split‑brain‑защита и автоматический failover.
5. **§190. Репликация MongoDB** — replica set, выбор primary, read preference и write concern как ручки надёжности и консистентности.
6. **§191. Репликация Redis** — как устроены master‑replica, Sentinel и Cluster, и почему Redis‑кластер — это особый зверь.
7. **§192. Репликация Cassandra** — replication factor, NetworkTopologyStrategy и уровни консистентности (ONE/QUORUM/ALL и др.).

Если у тебя пока слабое ощущение CAP‑теоремы и уровней консистентности — **не страшно**: в каждом разделе есть блоки **«Простыми словами»** и **«Картинка в голове»**, которые дадут интуицию без тяжёлой теории распределённых систем.

---

### Структура материала (что в какой группе)

| Группа разделов | Что внутри | Зачем это изучать |
|-----------------|-----------|--------------------|
| **Группа 1. PostgreSQL‑репликация** (`§186–187`) | Streaming и logical‑репликация PostgreSQL: физическая потоковая репликация WAL и логическая репликация строк/таблиц. | Чтобы уверенно настраивать реплики Postgres под high availability, чтения и миграции без догадок и «копипасты из блогов». |
| **Группа 2. MySQL‑репликация и кластеры** (`§188–189`) | Классическая binlog‑репликация с GTID и MySQL Group Replication (InnoDB Cluster). | Чтобы понимать, как «живёт» MySQL в проде: master‑slave, лаг, failover и кластеризация с консенсусом. |
| **Группа 3. Репликация NoSQL‑систем** (`§190–192`) | MongoDB replica set, Redis master‑replica/Sentinel/Cluster и Cassandra с replication factor и consistency levels. | Чтобы видеть за разными технологиями **общие идеи репликации и компромиссы** между консистентностью, доступностью и задержкой. |

---

### Как устроены разделы и оглавление

Каждый раздел (§186–192) следует единому шаблону:

- **В этом разделе главное** — 3–5 ключевых мыслей.
- **Простыми словами** — объяснение идеи без тяжёлого жаргона.
- **Теория и правила** — как это устроено в конкретной СУБД (по шагам).
- **Пошагово/Практика** — как настроить/почитать/проанализировать в реальной системе.
- **Картинка в голове** — метафора, чтобы «зацепить» образ.
- **Типичные ошибки** — реальные грабли из прод‑систем.
- **Проверь себя** — 2–3 вопроса с ответами под `<details>`.

В конце части есть:

- **Справочник по части** — краткое резюме по разделам.
- **Вопросы для самопроверки** по всей части.
- **Типичные ошибки по части и резюме** — чтобы ещё раз увидеть общие паттерны.

Оглавление ниже сгруппировано по этапам (группам разделов) — используй его как навигатор.

---
## Оглавление по этапам

### Этап 1. PostgreSQL: streaming и logical‑репликация

| §   | Раздел | Содержание | Ключевые понятия |
|-----|--------|-----------|------------------|
| 186 | [Streaming replication (PostgreSQL)](#186-streaming-replication-postgresql) | Как primary стримит WAL‑записи на standby‑узлы, чем отличаются синхронный и асинхронный режимы, что такое lag и quorum commit. | WAL, streaming replication, synchronous_commit, asynchronous replication, quorum commit, pg_stat_replication, replication lag. |
| 187 | [Logical replication (PostgreSQL)](#187-logical-replication-postgresql) | Репликация на уровне строк/таблиц: публикации и подписки, фильтрация таблиц, initial copy и типичные сценарии (миграции, интеграции). | Logical decoding, publication, subscription, initial copy, conflict, pg_stat_subscription. |

### Этап 2. MySQL: binlog‑репликация и group replication

| §   | Раздел | Содержание | Ключевые понятия |
|-----|--------|-----------|------------------|
| 188 | [Binlog‑репликация (MySQL)](#188-binlog-репликация-mysql) | Как MySQL пишет изменения в binlog, что такое форматы statement/row/mixed, GTID‑репликация и мониторинг lag. | Binlog, statement‑based, row‑based, mixed, GTID, relay log, Seconds_Behind_Master. |
| 189 | [Group replication (MySQL)](#189-group-replication-mysql) | MySQL‑кластер с консенсусом: multi‑master, защита от split‑brain, автоматический failover и ограничения на операции. | Group Replication, InnoDB Cluster, consensus, primary election, auto‑failover, conflict detection. |

### Этап 3. NoSQL: MongoDB, Redis, Cassandra

| §   | Раздел | Содержание | Ключевые понятия |
|-----|--------|-----------|------------------|
| 190 | [Репликация MongoDB](#190-репликация-mongodb) | Replica set, oplog, выбор primary (election), read preference и write concern как основные «ручки» по консистентности и доступности. | Replica set, primary, secondary, arbiter, oplog, read preference, write concern. |
| 191 | [Репликация Redis](#191-репликация-redis) | Master‑replica, Sentinel и Redis Cluster: как обеспечивается отказоустойчивость и шардирование, где возможна потеря данных. | Master‑replica, Sentinel, failover, hash slots, Redis Cluster, replicaof. |
| 192 | [Репликация Cassandra](#192-репликация-cassandra) | Replication factor, стратегии для нескольких ДЦ, уровни консистентности (ONE/QUORUM/ALL и др.) и компромиссы по CAP. | Replication factor, SimpleStrategy, NetworkTopologyStrategy, consistency level, QUORUM, LOCAL_QUORUM. |

---

---

<!-- prev-next-nav -->
*[← Индекс части](index.md) | [→ 186. Streaming replication (PostgreSQL)](01_186_streaming_replication_postgresql.md)*
