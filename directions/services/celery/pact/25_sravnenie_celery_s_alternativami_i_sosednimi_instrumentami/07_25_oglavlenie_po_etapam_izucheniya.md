[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Оглавление по этапам изучения

### Этап 0. Карта и рамка выбора

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Карта соответствия глобальному плану](#карта-соответствия-глобальному-плану) | где закрыт каждый подпункт 25.1-25.9 | coverage, scope |
| [Сквозная модель выбора инструмента](#сквозная-модель-выбора-инструмента) | как не ошибиться классом решения | problem-class fit |

### Этап 1. Близкие альтернативы

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [25.1 Celery vs cron/systemd timers](#251-celery-vs-cronsystemd-timers) | простота, периодичность, ограничения локального планирования | scheduler vs queue |
| [25.2 Celery vs RQ/Huey/Dramatiq/Arq](#252-celery-vs-rqhueydramatiqarq) | API, зрелость, эксплуатация, компромиссы | ecosystem trade-off |

### Этап 2. Инструменты другого уровня

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [25.3 Celery vs Airflow/Prefect](#253-celery-vs-airflowprefect) | orchestration level, scheduling semantics, observability | pipeline orchestration |
| [25.4 Celery vs Temporal](#254-celery-vs-temporal) | durable workflows, replay model, сложность | workflow durability |
| [25.6 Celery vs Luigi/Dagster и ETL-оркестраторы](#256-celery-vs-luigidagster-и-oblegchyonnye-etl-orkestratory) | canvas vs data lineage | data workflow |

### Этап 3. Потоки и managed-платформы

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [25.5 Celery vs Kafka consumers / stream processing](#255-celery-vs-kafka-consumers--stream-processing) | очередь задач против потока событий | event stream |
| [25.7 Celery vs managed workers](#257-celery-vs-oblachnye-managed-workers-cloud-run-jobs-batch-step-functions) | стоимость, cold start, гибрид | managed trade-off |

### Этап 4. Критерии архитектурного решения

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [25.8 Когда Celery - лучший выбор](#258-kogda-celery---luchshiy-vybor) | признаки хорошего fit | positive criteria |
| [25.9 Когда Celery - спорный выбор](#259-kogda-celery---spornyy-vybor) | красные флаги и альтернативы | negative criteria |

### Финал

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [Справочник по части](#справочник-по-части) | краткий конспект решений | recap |
| [Частые сценарии](#частые-сценарии) | реальные кейсы выбора | decision patterns |
| [Вопросы для самопроверки](#вопросы-для-самопроверки) | контроль понимания | self-check |
| [Типичные ошибки по части](#типичные-ошибки-по-части) | анти-паттерны выбора | anti-patterns |
| [Резюме части 25](#резюме-части-25) | итоговая ментальная модель | mental model |

---
