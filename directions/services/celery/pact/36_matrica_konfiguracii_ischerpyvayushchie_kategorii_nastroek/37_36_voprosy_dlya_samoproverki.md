[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Вопросы для самопроверки

1. Почему матрица конфигурации должна обновляться вместе с версией Celery?

<details><summary>Ответ</summary>

Потому что часть опций меняет статус (deprecated/new), semantics и значения по умолчанию. Без актуализации команда опирается на устаревшую модель и получает неожиданные сбои после апгрейда.

</details>

2. Что важнее для надежности: "правильные значения по умолчанию" или согласованность между категориями настроек?

<details><summary>Ответ</summary>

Согласованность. Даже хорошие default-значения могут конфликтовать между собой в конкретном workload. Надежность появляется, когда policy согласована end-to-end.

</details>

3. Почему нельзя тестировать конфигурацию только в eager-режиме?

<details><summary>Ответ</summary>

Потому что eager обходит broker/worker lifecycle и не показывает реальные эффекты доставки, redelivery, reconnect, prefetch-конкуренции и поведения event/result слоев.

</details>

4. Какие три группы настроек в первую очередь проверять при инциденте "задачи застряли"?

<details><summary>Ответ</summary>

Broker/connectivity (доступность/heartbeat/retry), worker runtime (pool/prefetch/concurrency/memory), task policy (acks/retry/time limits/routes).

</details>

---
