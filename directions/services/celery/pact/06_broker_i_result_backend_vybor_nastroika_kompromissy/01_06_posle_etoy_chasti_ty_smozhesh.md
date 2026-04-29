[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## После этой части ты сможешь

- объяснить разницу между **broker delivery** и **result backend visibility**;
- сравнить на уровне инженерных компромиссов **RabbitMQ**, **Redis** и **Amazon SQS** как broker’ы для Celery;
- понимать, как влияют на поведение **durable queues**, **persistent messages**, **ack/redelivery**, **prefetch/QoS**, **priorities**, **DLQ/retry топологии**, **quorum/classic queues**, **publisher confirms**, **TTL/overflow**;
- на практике описывать роль **visibility timeout** для SQS и почему без неё long-running задачи обречены на ранние redelivery;
- выбирать result backend из **Redis**, **SQL**, **RPC**, **cache-like** и осознанно управлять TTL/очисткой/стоимостью;
- объяснить, почему result backend нельзя превращать в “вечное бизнес-хранилище” и как это связано с retention/комплаенсом;
- под выбранный сценарий (внутренний маленький сервис, высокая нагрузка, облако с минимумом ops, сложная маршрутизация) сформировать обоснование выбора broker/backend;
- оценить последствия для наблюдаемости и диагностики при смене transport’а;
- понимать основные идеи про альтернативные и облачные брокеры (SNS/SQS связки, Service Bus, Pub/Sub) и где возникают ограничения переносимости (vendor lock-in).

---
