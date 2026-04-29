[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Справочник по части 2

| Тема | Что обязательно помнить |
| --- | --- |
| `2.1` Концепции очередей | Очередь = буфер; метрики depth/lag/throughput/service time показывают разрыв скоростей. |
| `2.2` Семантика доставки | Часто реалистична `at-least-once`; дубликаты нормальны при идемпотентности; ack — точка ответственности. |
| `2.3` Виды брокеров | RabbitMQ/Redis/SQS отличаются persistence, latency, visibility timeout, ordering и приоритетами. |
| `2.4` Failure modes | Классифицируй сбой: worker до/после ack, broker down, backend down, зависания, backlog, retry storm. |
| `2.5` Паттерны надёжности | Идемпотентность + outbox + saga + retry/backoff + circuit breaker + rate limit/backpressure. |
| `2.6` Упорядочивание | Порядок не гарантируется по умолчанию; псевдо-порядок достигается single consumer/partition key/dedicated queue. |
| `2.7` Backpressure | Управляй входом, когда publish быстрее consume: throttle, отдельные очереди, отказ в приёме. |
| `2.8` Сравнение брокеров | Смотри на semantics и ops, а не только на скорость: persistence/ordering/priorities/DLQ/latency/cost. |

---
