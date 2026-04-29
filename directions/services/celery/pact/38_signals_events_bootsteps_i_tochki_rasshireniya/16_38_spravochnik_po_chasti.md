[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Справочник по части

| Тема | Ключевые пункты | Что проверять в проде |
|---|---|---|
| Signals | разделение publish/task/worker сигналов | latency handler-ов, идемпотентность, coverage тестов |
| Event protocol | worker/task events, мониторинг, sampling | объём event traffic, backlog event consumer-а, retention |
| Bootsteps | порядок и зависимости шагов | startup/shutdown время, restart-loop, health readiness |
| task_annotations | централизованная policy-настройка задач | неожиданные override, влияние на SLA |
| Custom Task class | lifecycle hooks `before_start`...`after_return` | корректность лог-контекста и ошибки финализации |
| Serializer/backend/loader | глубинная кастомизация инфраструктуры | совместимость версий, decode errors, rollback path |

---
