[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Справочник по части

| Тема | Ключевые пункты |
|---|---|
| Состояния | `PENDING` читать только в контексте backend; `RETRY` не финал; `REVOKED/REJECTED` требуют анализа политики |
| Исключения | `Retry/Ignore/Reject` — управляющие механизмы; таймауты/worker loss — operational сигнал |
| Payload/протокол | минимальный payload, явный serializer, проверка `task_protocol`, контроль размера |
| Дедупликация | idempotency key + атомарный dedupe-store + метрики конфликтов |

---
