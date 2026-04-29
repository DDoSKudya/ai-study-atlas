[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Сквозная внутренняя схема Celery

```mermaid
flowchart LR
    P["Producer/API"] --> B["Broker"]
    B --> C["Worker Consumer"]
    C --> D["Decode + Strategy"]
    D --> E["Pool Execute"]
    E --> R["Result Backend"]
    E --> EV["Event Stream"]
    RC["Remote Control"] --> C
    S["Signals"] --> E
    BS["Bootsteps Init"] --> C
    BS --> RC
```

**Простыми словами:** Celery worker — это не "одна функция, которая берет задачу". Это набор внутренних подсистем, где каждая отвечает за свой этап. Ошибка почти всегда локализуется в одном конкретном этапе.

### Где находятся точки расширения (extension points)

```mermaid
flowchart TB
    A["Celery App"] --> B["Task Registry"]
    A --> C["Worker Blueprint"]
    C --> D["Bootsteps"]
    C --> E["Consumer Pipeline"]
    E --> F["Execution Pool"]
    F --> G["Task Signals"]
    E --> H["Remote Control"]
    F --> I["Result Backend"]
    F --> J["Events"]
```

Эта схема помогает понять, где что расширять:
- если нужна инфраструктурная инициализация worker-а -> чаще `bootsteps`;
- если нужны lifecycle hooks задачи -> чаще `signals`;
- если нужна бизнес-логика -> код задачи/canvas, а не скрытые хуки.

---
