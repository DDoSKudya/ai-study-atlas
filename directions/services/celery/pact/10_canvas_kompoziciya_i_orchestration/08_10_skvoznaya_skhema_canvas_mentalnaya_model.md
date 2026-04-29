[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Сквозная схема Canvas (ментальная модель)

```mermaid
flowchart LR
    A[Producer<br/>Создаёт logical job] --> B[Canvas Graph]
    B --> C1[chain]
    B --> C2[group]
    C2 --> C3[chord callback]
    B --> C4[map/starmap/chunks]
    C1 --> D[Broker]
    C2 --> D
    C3 --> D
    C4 --> D
    D --> E[Workers]
    E --> F[Result backend]
    F --> G[Aggregation / status / diagnostics]
```

Прочтение схемы:

- Canvas находится "сверху" как декларация графа, но исполняется через обычные сообщения в broker.
- `group/chord` дополнительно нагружают result backend, потому что нужно отслеживать много дочерних результатов.
- Чем богаче граф, тем важнее correlation ID и наблюдаемость в каждом узле.

---
