[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Оглавление по этапам изучения

### Этап 0. Карта и рамка

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Карта соответствия глобальному плану](#карта-соответствия-глобальному-плану) | Где раскрыт каждый подпункт | coverage, scope |
| [Сквозная внутренняя схема Celery](#сквозная-внутренняя-схема-celery) | Общий поток исполнения | pipeline, layers |

### Этап 1. База internals

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [22.1 Структура Celery под капотом](#221-структура-celery-под-капотом) | Внутренние подсистемы и границы | app, registry, loader |
| [22.2 Task message protocol](#222-task-message-protocol) | Формат сообщения и совместимость | headers, properties, body |

### Этап 2. Исполнение worker

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [22.3 Consumer pipeline](#223-consumer-pipeline) | Путь от брокера до пула и ack | qos, dispatch, acknowledge |
| [22.4 Bootsteps и расширение worker](#224-bootsteps-и-расширение-worker) | Модульная сборка worker-а | blueprint, dependency graph |
| [22.5 Signals](#225-signals) | Hooks жизненного цикла | task_prerun, task_postrun |

### Этап 3. Операционный и orchestration internals

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [22.6 Remote control internals](#226-remote-control-internals) | Inspect/control и broadcast | pidbox, replies, timeout |
| [22.7 Chord internals и backend dependence](#227-chord-internals-и-backend-dependence) | Почему chord сложен | unlock, group result, backend |
| [22.8 Internal debugging](#228-internal-debugging) | Диагностика и runbook подход | symptom mapping |

### Финал

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Справочник по части](#справочник-по-части) | Короткий повтор | recap |
| [Частые сценарии](#частые-сценарии) | Практические кейсы | troubleshooting |
| [Вопросы для самопроверки](#вопросы-для-самопроверки) | Проверка понимания | self-check |
| [Типичные ошибки по части](#типичные-ошибки-по-части) | Распространенные ловушки | anti-patterns |
| [Резюме части 22](#резюме-части-22) | Синтез ключевых идей | mental model |

---
