[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Сквозная карта надёжности (как всё связано)

Эта схема нужна, чтобы видеть тему части 9 как единую систему, а не набор отдельных техник.

```mermaid
flowchart LR
    A["Producer<br/>формирует logical job"] --> B["Broker / Queue"]
    B --> C["Worker execution"]
    C --> D{"Класс ошибки?"}
    D -- Transient --> E["Retry policy<br/>backoff+jitter+budget"]
    E --> B
    D -- Data/Business/Config --> F["Fail-fast / Quarantine / DLQ"]
    C --> G["Side effects"]
    G --> H["Idempotency + step-state + compensation"]
    H --> I["Consistent final state"]
```

Как читать схему:

- левая часть (`Producer/Broker/Worker`) показывает технический путь задачи;
- развилка `Класс ошибки?` подчёркивает, что реакция зависит от причины, а не от факта исключения;
- нижняя ветка (`Side effects`) напоминает: главный риск - не stack trace, а неконтролируемый бизнес-эффект.

#### Проверь себя по карте надёжности

1. Почему в схеме ветка side effects выделена отдельно от ветки retry?

<details><summary>Ответ</summary>

Потому что повтор обработки и побочные эффекты - разные оси риска. Retry может восстанавливать выполнение, но без идемпотентности и step-state он увеличивает риск повторного бизнес-эффекта. Поэтому side effects требуют отдельного контроля.

</details>

2. Что будет, если всегда идти только по ветке retry и не использовать quarantine/DLQ?

<details><summary>Ответ</summary>

Система начнёт бесконечно перерабатывать нерешаемые ошибки, будет расти backlog, ухудшится throughput полезных задач и усложнится диагностика. Нужна ветка изоляции и triage.

</details>

---
