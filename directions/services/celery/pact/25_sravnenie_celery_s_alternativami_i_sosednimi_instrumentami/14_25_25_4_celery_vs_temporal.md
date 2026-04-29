[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## 25.4 Celery vs Temporal

### Цель раздела

Понять принципиальную разницу между task queue и durable workflow engine.

### В этом разделе главное

Temporal решает класс задач, где workflow сам по себе — ключевая бизнес-сущность с длительным состоянием и надежным восстановлением.

### Теория и правила

Temporal дает:

- durable workflow state;
- replay model;
- детерминированность логики workflow (важное требование к коду).

Celery дает:

- сильный task execution и routing слой;
- гибкость для фоновых задач;
- более прямой путь для Python backend.

Тонкое место: в Temporal workflow-код подчиняется требованиям детерминизма (иначе replay может вести себя неожиданно). В Celery таких требований как у модели replay нет, но выше риск логических расхождений между задачами без явной orchestration модели.

### ASCII-схема различия

```text
Celery:
Producer -> Broker Queue -> Worker executes task -> (optional) result backend

Temporal:
Client -> Workflow history (durable log) -> Workers replay/continue workflow steps
```

### Проверь себя: модель Celery vs Temporal

1. Что в этой схеме указывает на принципиальную роль history/replay в Temporal?

<details><summary>Ответ</summary>

Центральный элемент `Workflow history (durable log)` и поведение workers через replay/continue показывают, что история процесса — первичный источник состояния.

</details>

2. Почему наличие result backend в Celery не превращает его в полноценный durable workflow engine?

<details><summary>Ответ</summary>

Result backend хранит результаты/статусы задач, но не равен полной модели workflow-истории, детерминизма и replay-семантики, как у Temporal.

</details>

### Практика

**Если бизнес-процесс длится дни/недели**, имеет много ветвлений, ожиданий внешних сигналов и строгую необходимость восстановиться шаг-в-шаг после сбоев, Temporal часто уместнее.

**Если нужны фоновые задачи, retries, batch-процессы и умеренная orchestration в Python-сервисе**, Celery обычно проще и дешевле в когнитивной стоимости.

Граничный сценарий:

- если у тебя "почти Temporal" требования, но команда и платформа не готовы к Temporal-сложности, лучше явно зафиксировать ограничения Celery-решения (какие инварианты гарантируем, а какие нет), чем делать вид, что "почти durable workflow" уже реализован.

### Типичные ошибки

- ожидать от Celery "из коробки" durable workflow уровня Temporal;
- внедрять Temporal там, где нужны просто надежные фоновые задачи.
- недооценивать требования детерминизма и операционного контура Temporal.

### Проверь себя

1. Почему Celery не прямой заменитель Temporal?

<details><summary>Ответ</summary>

Потому что Temporal строится вокруг durable workflow history и replay-модели, а Celery — вокруг доставки и исполнения задач в очередях.

</details>

2. В чем главный компромисс Temporal?

<details><summary>Ответ</summary>

Более высокий порог проектирования и эксплуатации: требования к модели workflow, детерминизму, инфраструктуре и инженерной дисциплине.

</details>

---
