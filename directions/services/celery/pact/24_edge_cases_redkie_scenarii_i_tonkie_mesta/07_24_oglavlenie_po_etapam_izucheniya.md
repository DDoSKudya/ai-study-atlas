[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Оглавление по этапам изучения

### Этап 0. Карта и общая рамка

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Карта соответствия глобальному плану](#карта-соответствия-глобальному-плану) | где закрыт каждый подпункт 24.1–24.9 | coverage, scope |
| [Сквозная модель edge-case риска](#сквозная-модель-edge-case-риска) | как редкий сбой превращается в каскадный инцидент | trigger, amplification, containment |

### Этап 1. Ресурсы, жизненный цикл и payload

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [24.1 Долгоживущие задачи](#241-долгоживущие-задачи) | liveness, shutdown, checkpointing | heartbeat, graceful stop |
| [24.2 Очень большие payload](#242-очень-большие-payload) | broker pressure, serialization overhead, object storage | payload contract |

### Этап 2. Совместимость и календарь

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [24.3 Версионные несовместимости](#243-версионные-несовместимости) | upgrade risks, feature drift, old messages | compatibility matrix |
| [24.4 Часовые пояса и календарные эффекты](#244-часовые-пояса-и-календарные-эффекты) | DST, locale calendars, UTC-first | scheduling correctness |

### Этап 3. Каскадные инциденты и гонки состояния

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [24.5 Падение внешней зависимости во время массового retry](#245-падение-внешней-зависимости-во-время-массового-retry) | retry storm, jitter, circuit breaker | load shedding |
| [24.6 Гонка producer vs consumer state](#246-гонка-producer-vs-consumer-state) | publish-before-commit, stale read, eventual consistency | outbox, consistency |

### Этап 4. Инфраструктурные крайние случаи

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [24.7 Celery в гибридных environments](#247-celery-в-гибридных-environments) | on-prem + cloud, multi-broker, geo-workers | topology-aware routing |
| [24.8 OOM, cgroups и лимиты контейнеров](#248-oom-cgroups-и-лимиты-контейнеров) | SIGKILL, memory limits, swap/disk pressure | memory governance |
| [24.9 Часы и синхронизация времени](#249-часы-и-синхронизация-времени) | NTP drift, ETA skew, early/late execution | time hygiene |

### Финал

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Справочник по части](#справочник-по-части) | краткое повторение | recap |
| [Частые сценарии](#частые-сценарии) | практические кейсы | decision patterns |
| [Вопросы для самопроверки](#вопросы-для-самопроверки) | контроль понимания | self-check |
| [Типичные ошибки по части](#типичные-ошибки-по-части) | главные ловушки | anti-patterns |
| [Резюме части 24](#резюме-части-24) | синтез и связь со следующей частью | mental model |

---
