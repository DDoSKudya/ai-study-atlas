[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## End-to-end поток: клиент -> API -> Celery -> внешние системы

```mermaid
sequenceDiagram
    participant U as Frontend/User
    participant API as Backend API
    participant DB as DB/ORM
    participant BR as Broker
    participant WK as Celery Worker
    participant EXT as External API
    participant CH as Checkpoint Store

    U->>API: POST /operation
    API->>DB: BEGIN + write domain data
    API->>DB: COMMIT
    API->>BR: publish task (on_commit)
    BR->>WK: deliver message
    WK->>DB: read by id (fresh session)
    WK->>EXT: call with timeout + idempotency key
    alt success
        EXT-->>WK: 2xx
        WK->>CH: update progress/status
    else transient failure
        EXT-->>WK: timeout/5xx
        WK->>WK: retry with backoff+jitter
    else permanent failure
        EXT-->>WK: 4xx contract/data issue
        WK->>CH: mark failed stage (no blind retry)
    end
```

Зачем этот сценарий нужен: он показывает, где именно находятся контрактные границы и какие ошибки типичны на каждой из них.

#### Проверь себя: end-to-end поток

1. Где в E2E-схеме проходит критичная граница консистентности данных?
2. Почему ветка permanent failure не должна автоматически уходить в бесконечный retry?

<details><summary>Ответ</summary>

1) Между commit в БД и publish в broker — именно здесь решается, что увидит worker.  
2) Потому что при контрактной/валидационной ошибке повтор без изменения данных не исправляет причину.

</details>

---
