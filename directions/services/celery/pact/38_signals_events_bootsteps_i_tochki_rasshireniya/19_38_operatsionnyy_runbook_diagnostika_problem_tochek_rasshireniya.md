[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Операционный runbook: диагностика проблем точек расширения

### Симптом -> где искать сначала

| Симптом | Первый фокус | Типичный корень проблемы |
|---|---|---|
| задачи стали медленнее после «маленькой доработки» | signal handlers и `Task` hooks | тяжелый I/O или блокировки в lifecycle |
| worker жив по heartbeat, но не обрабатывает задачи | bootsteps/pool readiness | зависший step, блокировка старта подпроцесса |
| резкий рост объема мониторинга | event stream + sampling policy | включили лишние события без лимитов |
| всплеск `task_unknown` | discovery + деплой-совместимость | version drift producer/worker |
| decode errors после релиза | serializer compatibility window | producer пишет новый формат, worker не умеет читать |
| разное поведение worker-ов в одном релизе | loader/config path | разные источники конфигурации или drift |

### Пошаговый «быстрый triage» (10-15 минут)

1. Сопоставить тайминг регрессии с моментом включения hook/step/serializer.
2. Проверить логи startup/shutdown worker и наличие ошибок в handlers.
3. Проверить event-volume и queue depth до/после изменения.
4. Временно отключить suspect-расширение feature-флагом.
5. Если метрики стабилизировались — фиксируем RCA и план безопасного возврата.

### Что обязательно записать после инцидента

- какая точка расширения была причиной (signal/event/bootstep/task class/serializer);
- какой guardrail отсутствовал (тест, лимит, rollout, observability);
- какое правило добавить в release checklist, чтобы инцидент не повторился.

### Мини-чеклист release readiness для части 38

- расширение привязано к одной явной цели и owner-команде;
- есть canary rollout и обратимый feature-flag;
- есть тесты на version compatibility (producer/worker mixed versions);
- есть fallback-режим, если extension временно отключается;
- обновлен runbook и список команд диагностики.

#### Проверь себя: runbook и readiness

1. Почему в triage сначала проверяют тайминг регрессии относительно релиза extension?
2. Какой практический смысл у feature-flag в контексте диагностируемого инцидента?
3. Почему release readiness включает mixed-version compatibility тесты, даже если «всё зелёное» в CI?

<details><summary>Ответ</summary>

1) Это самый быстрый способ связать симптом с вероятной причиной и сократить пространство гипотез.  
2) Он позволяет быстро уменьшить blast radius без полного отката релиза и проверить причинно-следственную связь.  
3) В реальной эксплуатации producer и worker могут обновляться не одновременно; без mixed-version тестов возникают скрытые несовместимости.

</details>

---
