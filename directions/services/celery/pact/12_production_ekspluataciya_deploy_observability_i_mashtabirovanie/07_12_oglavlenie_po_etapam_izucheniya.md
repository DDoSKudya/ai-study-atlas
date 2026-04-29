[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Оглавление по этапам изучения

### Этап 1. Deployment модели

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [12.1. Deployment-модели Celery](#121-deployment-модели-celery) | systemd/Docker/K8s, stateless vs stateful, конфиги/секреты, sidecar/agents | systemd, Docker, Kubernetes, requests/limits, secrets, sidecar |

### Этап 2. Rolling update и graceful shutdown

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [12.2. Rolling updates и graceful shutdown](#122-rolling-updates-и-graceful-shutdown) | drain, остановка без потери задач, long-running, revoke/terminate | drain, SIGTERM, termination grace, ack, revoke, long-running |

### Этап 3. Observability (логи, метрики, трейсы)

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [12.3. Observability Celery в production](#123-observability-celery-в-production) | какие метрики нужны, как связать логи/трейсы/таски, Flower и ограничения | metrics, traces, correlation id, events, Flower, exporters |

### Этап 4. Инциденты и runbooks

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [12.4. Инциденты: диагностика и runbooks](#124-инциденты-диагностика-и-runbooks) | backlog, stuck workers, retry storm, outage, duplication, hot queue | backlog, lag, retry storm, broker outage, runbook |

### Этап 5. Масштабирование

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [12.5. Autoscaling и capacity planning](#125-autoscaling-и-capacity-planning) | стратегии скейла, KEDA/HPA, сигналы, cooldown, anti-thrashing | autoscaling, KEDA, HPA, lag-based scaling, cooldown |

### Этап 6. DR и совместимость при деплое

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [12.6. DR и совместимость: очередь не пуста](#126-dr-и-совместимость-очередь-не-пуста) | что сохраняем, replay, идемпотентность, evolve payload schema | DR, replay, idempotency, schema evolution, backward compatibility |

### Финал

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Справочник по части 12](#справочник-по-части-12) | краткое повторение | summary |
| [Частые сценарии](#частые-сценарии) | “что делать если…” | runbooks |
| [Вопросы для самопроверки по части 12](#вопросы-для-самопроверки-по-части-12) | сводная проверка | self-check |
| [Типичные ошибки](#типичные-ошибки) | список граблей | pitfalls |
| [Резюме части](#резюме-части) | итоги и связь с соседними темами | next steps |

---
