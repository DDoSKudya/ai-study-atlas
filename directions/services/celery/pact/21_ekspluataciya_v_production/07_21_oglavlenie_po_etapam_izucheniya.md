[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Оглавление по этапам изучения

### Этап 0. Карта соответствия плану

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Карта соответствия глобальному плану (часть 21)](#карта-соответствия-глобальному-плану-часть-21) | Где раскрыт каждый пункт | scope, coverage |
| [Сквозная картина эксплуатации](#сквозная-картина-эксплуатации) | Цепочка прохождения задачи через контур | data flow, failure points |

### Этап 1. Deployment и обновления

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [21.1 Deployment модели](#211-deployment-модели) | systemd, Compose, K8s, stateful/stateless, sidecar | deployment topology |
| [21.2 Rolling updates и graceful shutdown](#212-rolling-updates-и-graceful-shutdown) | drain, ожидание задач, long-running, revoke/terminate | rolling, drain, restart safety |

### Этап 2. Масштабирование и размещение

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [21.3 Autoscaling](#213-autoscaling) | HPA/KEDA, queue depth, lag, cooldown, anti-thrashing | autoscaling policy |
| [21.4 Ресурсы Kubernetes и размещение worker](#214-ресурсы-kubernetes-и-размещение-worker) | requests/limits, PDB, affinity, выделенные ноды | scheduling, resilience |

### Этап 3. Инциденты и восстановление

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [21.5 Инциденты и runbooks](#215-инциденты-и-runbooks) | типовые аварии и алгоритмы действий | incident response |
| [21.6 Disaster recovery](#216-disaster-recovery) | что хранить, что терять нельзя, replay, тестирование DR | RTO/RPO, replay |

### Этап 4. Совместимость и эволюция

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [21.7 Версионирование задач и backward compatibility](#217-версионирование-задач-и-backward-compatibility) | эволюция payload, phased rollout, deprecations | compatibility, rollout |

### Финал

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Справочник по части 21](#справочник-по-части-21) | Быстрый повтор | recap |
| [Чеклист production-ready перед релизом](#чеклист-production-ready-перед-релизом) | Предрелизная проверка готовности | release gate |
| [Частые сценарии](#частые-сценарии) | Практика решений | runbook mindset |
| [Вопросы для самопроверки по части 21](#вопросы-для-самопроверки-по-части-21) | Проверка понимания | self-check |
| [Типичные ошибки по части](#типичные-ошибки-по-части) | Что ломает production чаще всего | anti-patterns |
| [Резюме части 21](#резюме-части-21) | Главные выводы | synthesis |

---
