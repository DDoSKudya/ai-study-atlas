[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Справочник по части 19

| Тема | Короткая суть | Практический вывод |
|---|---|---|
| FastAPI + Celery | ASGI-вход и worker-выход разделены | Держи publish layer и явный контракт |
| Flask + Celery | Контексты Flask не переносятся автоматически | Не завязывай задачи на request context |
| Общее ядро | Contract/version/correlation/idempotency обязательны | Стандартизируй публикацию на уровне команды |
| Async boundary | Async API не делает task-слой async сам по себе | Явно проектируй sync/async переходы |
| ASGI context | middleware-контекст переносится только явно | Передавай correlation id через headers |
| Тестирование | Нужны unit + contract + integration | Eager mode полезен, но не исчерпывающий |

#### Проверь себя по справочнику

1. Какой пункт справочника сильнее всего влияет на скорость расследования инцидентов и почему?

<details><summary>Ответ</summary>

ASGI context + correlation id: без сквозной корреляции сложно связать API-событие с конкретной задачей в worker и быстро локализовать проблему.

</details>

2. Какой пункт справочника чаще всего игнорируют на старте и чем это заканчивается?

<details><summary>Ответ</summary>

Versioning/contract discipline. Итог — несовместимые payload при релизах, массовые падения задач и сложные rollback-сценарии.

</details>

---
