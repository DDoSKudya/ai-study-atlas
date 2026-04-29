[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Сквозная модель observability-слоя

```mermaid
flowchart LR
    A[Celery Producers] --> B[(Broker)]
    B --> C[Workers]
    C --> D[Business side effects]
    C --> E[Logs JSON]
    C --> F[Metrics]
    C --> G[Traces/APM]
    B --> H[Broker exporters]
    E --> I[Loki/ELK/OpenSearch]
    F --> J[Prometheus/Datadog]
    G --> K[OTel collector/APM]
    J --> L[Grafana/APM UI]
    I --> L
    K --> L
    C --> M[Flower]
```

**Простыми словами:** Celery сам исполняет задачи, но "видимость" системы создаётся отдельным слоем наблюдаемости. Если этот слой неполный, команда работает вслепую.

---
