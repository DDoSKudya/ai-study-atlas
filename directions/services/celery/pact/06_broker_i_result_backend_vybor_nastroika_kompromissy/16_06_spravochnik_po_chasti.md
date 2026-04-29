[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Справочник по части

| Тема | Что держать в голове |
|---|---|
| Broker vs backend | Broker = delivery, backend = видимость статусов/результата. |
| RabbitMQ | exchange/binding = routing, durable/persistent = надежность, ack/redelivery = семантика, prefetch/QoS = дубликаты при падениях, DLX/TTL = retry топологии, quorum/classic = надежность очереди. |
| RabbitMQ priorities | Полезно для локальных приоритетов, но не заменяет topology для strict ordering. |
| Publisher confirms | Делает “publish принят” более доказуемым, но может влиять на latency/блокировки. |
| Redis broker | Быстро, но надежность упирается в persistence и риск потери при рестартах; редelivery требует идемпотентности; приоритеты/ordering обычно ограничены. |
| Redis visibility_timeout | Настраивай под worst-case длительность обработки. |
| SQS managed | delivery связана с visibility timeout и polling; повторы реальны всегда, нужна идемпотентность; FIFO — порядок внутри message group и ограничение параллелизма. |
| Result backend | TTL и cost profile важнее “выбрать что быстрее”. |
| Result backend safety | tracebacks/meta могут быть чувствительными: retention и комплаенс. |
| chord/group | Композиции могут зависеть от backend механики сбора результатов. |
| Выбор под scenario | Переводи требования в критерии: delivery, TTL, diagnosability, cost, ops maturity. |
| Альтернативы | bridge меняет семантики и runbooks; vendor lock-in часто семантический. |

---
