[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Справочник по части

| Категория | Ключевой вопрос | Минимум, который должен быть зафиксирован |
|---|---|---|
| App/discovery | Все ли задачи видны worker-у? | strategy `imports/include/autodiscover`, единая инициализация app |
| Broker/connectivity | Как система переживает сетевые сбои? | retry policy, heartbeat, TLS, transport options |
| Task policy | Какая семантика доставки и повторов? | serializer/accept, ack, limits, retry, routes |
| Worker runtime | Как контролируется производительность и стабильность? | pool, concurrency, prefetch, memory guards |
| Beat | Как исключаются дубли и временные аномалии? | single scheduler, storage, timezone policy |
| Result backend | Как хранится статус без лишней стоимости? | `result_expires`, cleanup, ignore_result strategy |
| Events/monitoring | Есть ли достаточная observability? | event flags, TTL, ключевые алерты |
| Security | Где trust boundary и кто может публиковать? | JSON-only baseline, TLS, ключи/сертификаты |
| Testing/debug | Проверяется ли distributed reality? | eager для unit + integration e2e с real broker |
| Rare/deprecated | Готовы ли к апгрейду? | реестр редких ключей, миграционный checklist |

---
