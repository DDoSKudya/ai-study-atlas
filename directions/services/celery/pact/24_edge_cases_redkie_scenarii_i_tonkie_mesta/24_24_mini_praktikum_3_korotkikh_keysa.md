[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Мини-практикум: 3 коротких кейса

### Кейс A: «Длинная задача часто перезапускается после деплоя»

Что сделать в первую очередь?

<details><summary>Ответ</summary>

Разбить задачу на этапы с checkpoint, добавить graceful shutdown контракт и метрики прогресса. Это сразу снижает цену рестартов и делает поведение предсказуемым.

</details>

### Кейс B: «После апгрейда часть задач стала падать на десериализации»

Какой минимальный план действий?

<details><summary>Ответ</summary>

Остановить расширение rollout, проверить compatibility matrix Celery/Kombu/Billiard, прогнать legacy-message replay, затем делать canary с явными rollback-критериями.

</details>

### Кейс C: «ETA-задачи уходят раньше в одном регионе»

Что проверять по порядку?

<details><summary>Ответ</summary>

Clock skew между producer/worker, состояние NTP/chrony, UTC timestamps по цепочке publish->receive->start, затем timezone/DST правила.

</details>

---
