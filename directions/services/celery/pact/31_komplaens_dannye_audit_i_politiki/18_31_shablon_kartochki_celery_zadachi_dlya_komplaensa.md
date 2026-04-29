[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Шаблон карточки Celery-задачи для комплаенса

Этот шаблон нужен, чтобы каждая значимая задача имела одинаково понятный профиль риска и не зависела от памяти конкретного разработчика.

```markdown
### Task Compliance Card

- task_name:
- owner_team:
- business_purpose:
- data_class: (low-risk / PII / PHI / PCI)
- allowed_payload_fields:
- forbidden_payload_fields:
- tokenization_strategy:
- audit_required_fields: (task_id, request_id, actor_id, ...)
- retention_class:
- result_backend_policy: (ignore/store errors/TTL)
- legal_hold_handling:
- region_policy: (EU-only / US-only / multi-region with constraints)
- dependencies_risk_level:
- last_security_review_date:
- rollback_plan_reference:
```

### Как использовать шаблон

1. Заполнять при создании новой задачи и при каждом существенном изменении payload.
2. Хранить рядом с кодом (например, в docs/adr/task-cards) и ссылаться из PR.
3. Проверять на релизном review: если карточка устарела — релиз блокируется.

#### Проверь себя: шаблон карточки

1. Почему task card должна обновляться при изменении payload, даже если код "почти не менялся"?

<details><summary>Ответ</summary>

Даже небольшое изменение полей может поменять data class, требования к retention, аудиту и региональности. Устаревшая карточка создает ложное чувство контроля.

</details>

2. Что произойдет, если держать task card отдельно от процесса PR/release?

<details><summary>Ответ</summary>

Карточка быстро устареет и перестанет быть рабочим инструментом. Она должна быть встроена в инженерный процесс проверки изменений.

</details>

---
