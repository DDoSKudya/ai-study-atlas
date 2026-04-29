[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Оглавление по этапам изучения

### Этап 1. RabbitMQ как broker

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [6.1. RabbitMQ как broker](#61-rabbitmq-как-broker) | Как broker-топология и настройки влияют на delivery, retry/DLQ и performance | AMQP, exchange, binding, durable/persistent, ack/redelivery, prefetch/QoS, priorities, DLQ, quorum |

### Этап 2. Redis и SQS

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [6.2. Redis как broker](#62-redis-как-broker) | Почему Redis прост, где он ограничен, как работает persistence и как не ожидать AMQP-гарантий | persistence, memory limits, restart risk, visibility-like семантика, priorities/DLQ ограничения |
| [6.3. SQS и managed brokers](#63-sqs-и-managed-brokers) | Managed очереди, `visibility timeout`, polling/cost и когда FIFO реально помогает | visibility timeout, polling, FIFO vs standard, idempotency |

### Этап 3. Result backend

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [6.4. Result backend варианты](#64-result-backend-варианты) | Redis/SQL/RPC/cache-like backends, TTL/очистка, стоимость, безопасность traceback/meta | TTL, consistency expectations, write amplification, chord dependency |

### Этап 4. Выбор и альтернативы

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [6.5. Как выбирать broker/backend под сценарий](#65-как-выбирать-broker-backend-под-сценарий) | Обоснование выбора под workload и зрелость команды, чеклист диагностики | scenario mapping, cost model, diagnosability |
| [6.6. Облачные и альтернативные брокеры](#66-облачные-и-альтернативные-брокеры) | SNS/SQS, Service Bus, Pub/Sub, переносимость и vendor lock-in | managed trade-offs, portability limits |

---
