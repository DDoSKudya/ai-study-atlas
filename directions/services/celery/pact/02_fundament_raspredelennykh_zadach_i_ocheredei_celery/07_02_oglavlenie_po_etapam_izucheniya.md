[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Оглавление по этапам изучения

### Этап 1. Модель очередей

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [2.1. Базовые концепции систем очередей](#21-базовые-концепции-систем-очередей) | Producer/consumer, decoupling, message как единица работы, метрики очереди | producer, consumer, queue depth, lag, throughput, service time |
| [2.2. Семантика доставки](#22-семантика-доставки) | at-most-once/at-least-once, дубликаты как норма, видимость сообщения и redelivery, ack/commit | at-most-once, at-least-once, ack, redelivery |

### Этап 2. Брокер и failure modes

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [2.3. Виды очередей и брокеров](#23-виды-очередей-и-брокеров) | RabbitMQ/Redis/SQS и их отличия по устойчивости, latency, visibility timeout, ordering, priority | RabbitMQ, Redis, SQS, persistence, visibility timeout, ordering |
| [2.4. Модели отказов](#24-модели-отказов) | Где падает: worker до/после ack, broker/backend недоступны, зависания, storm повторов, backlog и SLA | failure modes, ack point, backlog, retry storm |

### Этап 3. Надёжность и контроль

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [2.5. Паттерны надёжной фоновой обработки](#25-паттерны-надежной-фоновой-обработки) | idempotency key, дедупликация, transactional outbox, saga/compensation, retry/backoff, circuit breaker, rate limiting/backpressure | idempotency, outbox, saga, backoff, breaker, backpressure |
| [2.6. Упорядочивание и детерминизм](#26-упорядочивание-и-детерминизм) | почему порядок не гарантируется, псевдо-порядок через single consumer/partition key/dedicated queue | ordering, partition key, dedicated queue |
| [2.7. Backpressure и ограничение входа](#27-backpressure-и-ограничение-входа) | publish быстрее consume => рост очереди, стратегии throttle/отдельные очереди/отказ в приёме, связь с SLA | backpressure, throttle, queue growth, SLA |

### Этап 4. Сравнение и выбор

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [2.8. Сравнительная матрица брокеров](#28-сравнительная-матрица-брокеров) | Matrix: persistence, ordering, priorities, DLQ, ops complexity, latency, cost model | comparison matrix, trade-offs |

### Финал

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [Справочник по части 2](#справочник-по-части-2) | Быстрое повторение ключевых идей | summary |
| [Частые сценарии](#частые-сценарии) | Как распознавать проблемы по симптомам | diagnosis |
| [Вопросы для самопроверки по части 2](#вопросы-для-самопроверки-по-части-2) | Сводная проверка понимания | self-check |
| [Типичные ошибки и антипаттерны](#типичные-ошибки-и-антипаттерны) | Наиболее опасные ошибки применения | anti-patterns |
| [Резюме части 2](#резюме-части-2) | Главные выводы и связь со следующими частями | recap |

---
