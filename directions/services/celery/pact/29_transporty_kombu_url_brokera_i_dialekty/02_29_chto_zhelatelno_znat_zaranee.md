[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Что желательно знать заранее

- части 6, 8, 9, 14, 21 и 27 текущего курса;
- базовую модель Celery: producer -> broker -> worker -> result backend;
- разницу между at-least-once delivery и exactly-once processing;
- основы сетей: DNS, TCP keepalive, TLS, private endpoints.

#### Проверь себя: входные знания

1. Почему тема транспорта критична именно после разделов про надежность и worker lifecycle?

<details><summary>Ответ</summary>

Потому что надежность Celery формируется на стыке логики задач и поведения брокера. Без понимания ack/retry/prefetch на уровне worker вы не сможете правильно интерпретировать ограничения транспорта.

</details>

2. Что полезнее для production: «любой рабочий URL брокера» или «URL + явные операционные параметры»?

<details><summary>Ответ</summary>

Второе. Базовый URL может работать в happy path, но без явных параметров (таймауты, heartbeat, TLS, failover) система часто разваливается в деградации сети и при пиках нагрузки.

</details>

---
