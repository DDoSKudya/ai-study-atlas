[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Справочник по части 4

| Тема | Ключевые пункты |
|---|---|
| Компоненты контура | Producer публикует, broker хранит/маршрутизирует, worker исполняет, backend показывает статусы/результаты |
| Message flow | publish → routing → reserve → execute → ack → state writing (backend/events) |
| Kombu | messaging layer Celery; transport определяет возможности и семантики доставки |
| Result backend | нужен по сценариям; хранит state/result/traceback; TTL и стоимость; отдельная зона отказа |
| Events и remote control | events для наблюдения, Flower/inspect; remote control для управления; безопасность и изоляция |
| Failure domains | delivery/execution/visibility отличают причины по симптомам |

---
