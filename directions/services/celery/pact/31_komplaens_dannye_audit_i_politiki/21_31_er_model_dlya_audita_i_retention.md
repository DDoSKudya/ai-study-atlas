[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## ER-модель для аудита и retention

Эта схема нужна, чтобы визуально отделить "операционные" и "доказательные" сущности и понять, как legal hold влияет на удаление.

```mermaid
erDiagram
    TASK_MESSAGE ||--o{ TASK_EVENT : generates
    TASK_EVENT }o--|| AUDIT_RECORD : mirrored_as
    TASK_EVENT }o--|| RETENTION_CLASS : governed_by
    AUDIT_RECORD }o--o{ LEGAL_HOLD : frozen_by

    TASK_MESSAGE {
      string task_id
      string task_name
      string payload_version
      string tenant_region
    }
    TASK_EVENT {
      string event_id
      string task_id
      string request_id
      string actor_id
      string status
      datetime created_at
    }
    AUDIT_RECORD {
      string audit_id
      string event_id
      string business_outcome
      datetime stored_at
      bool immutable
    }
    RETENTION_CLASS {
      string class_name
      int ttl_days
      string owner_team
    }
    LEGAL_HOLD {
      string hold_id
      string reason
      datetime activated_at
      string scope
    }
```

Как читать схему:

1. `TASK_MESSAGE` и `TASK_EVENT` отражают operational-поток Celery.
2. `AUDIT_RECORD` отделен, потому что его требования к неизменяемости и срокам иные.
3. `RETENTION_CLASS` управляет удалением по правилам.
4. `LEGAL_HOLD` может временно "замораживать" удаление даже при истекшем TTL.

#### Проверь себя: ER-модель

1. Почему `LEGAL_HOLD` логически связан с `AUDIT_RECORD`, а не только с `TASK_MESSAGE`?

<details><summary>Ответ</summary>

Потому что legal hold обычно касается доказательной и расследовательной информации: нужно сохранять не только сообщение, но и контекст принятых решений и событий.

</details>

2. Что потеряет модель, если убрать `RETENTION_CLASS` как отдельную сущность?

<details><summary>Ответ</summary>

Исчезнет явная управляемость сроками хранения по категориям; удаление станет неформальным и зависимым от ручных решений.

</details>

---
