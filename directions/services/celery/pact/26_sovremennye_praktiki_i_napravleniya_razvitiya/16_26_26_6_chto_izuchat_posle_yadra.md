[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## 26.6 Что изучать после ядра

### Цель раздела

Сформировать практический roadmap развития после освоения Celery-базы, чтобы выйти на уровень платформенного инженера/архитектора асинхронных систем.

### В этом разделе главное

- Celery mastery не заканчивается на API задач;
- рост идет через соседние инженерные дисциплины;
- важно учиться в правильной последовательности: от транспорта к reliability и архитектуре;
- roadmap должен включать и теорию, и практику production-инцидентов.

### Теория и правила

План развития после ядра:

1. **RabbitMQ deeply** — модель очередей, routing, HA, quorum, recovery.
2. **Distributed systems reliability** — delivery semantics, failure modes, consistency.
3. **SRE для async systems** — SLO, error budgets, incident response, capacity planning.
4. **Workflow engines** — Temporal/Prefect/Airflow как отдельный класс решений.
5. **Event-driven architecture** — event contracts, stream processing, replay.
6. **Transactional messaging patterns** — outbox/inbox, dedup, exactly-once trade-offs.

### Таблица "что и зачем"

| Область | Что изучать | Что это даст в Celery-практике |
|---|---|---|
| RabbitMQ deep dive | quorum queues, flow control, clustering | меньше broker-инцидентов и лучше HA-дизайн |
| Reliability | CAP, retries, idempotency, consistency | корректные решения в авариях и race-сценариях |
| SRE async | SLI/SLO, burn-rate, runbooks | управляемое качество фоновых сервисов |
| Workflow engines | durable workflows, replay model | понимание границ Celery и осознанный гибрид |
| Event-driven | Kafka/streams, schema registry | правильное разделение команд и событий |
| Messaging patterns | outbox/inbox, dedup keys | консистентность между DB и асинхронными контурами |

### Пошагово: roadmap на 3 этапа

1. **Этап A (1-2 месяца):**  
   RabbitMQ internals + SLO/observability усиление текущего Celery-контура.
2. **Этап B (2-4 месяца):**  
   reliability patterns + outbox/dedup стандарты команды.
3. **Этап C (4-6 месяцев):**  
   workflow/event-driven инструменты и пилот гибридной архитектуры.

### Рекомендованный формат обучения после части 26

| Формат | Что делать | Какой результат |
|---|---|---|
| **Теория** | читать RFC/доки по broker/OTel/SRE | формируется точная терминология и модель |
| **Практика** | проводить нагрузочные и failover drills | появляется уверенность в инцидентах |
| **Ревью решений** | писать mini-RFC на каждое значимое изменение | повышается архитектурная дисциплина |
| **Ретроспектива инцидентов** | связывать сбои с пробелами в знаниях | обучение становится прикладным |

### Личная карта компетенций (самооценка)

Оцени себя по шкале 0-3:
- `0` — не умею;
- `1` — знаю теорию;
- `2` — делал под руководством;
- `3` — внедрял самостоятельно и защищал решение.

| Компетенция | Балл (0-3) | Что подтянуть следующим шагом |
|---|---:|---|
| Проектирование autoscaling для Celery |  | KEDA/HPA практикум |
| SLO и burn-rate для фоновых систем |  | построить живой SLO dashboard |
| Broker failover/restart drills |  | провести drill и обновить runbook |
| K8s lifecycle и probes |  | лабораторный rolling update test |
| Hybrid architecture contracts |  | mini-RFC на один гибридный кейс |
| Outbox/idempotency patterns |  | внедрить стандарт команды |

Цель таблицы: сделать обучение измеримым, а не "кажется, я уже разобрался".

---
