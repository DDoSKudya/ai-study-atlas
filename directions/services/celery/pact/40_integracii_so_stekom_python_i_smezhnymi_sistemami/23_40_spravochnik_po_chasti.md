[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Справочник по части

| Тема | Ключевые опорные пункты |
|---|---|
| ORM и транзакции | `on_commit`, session lifecycle, per-task scope, no ORM objects in payload |
| Схемы данных | payload contract, validation, schema evolution, compact JSON |
| HTTP/gRPC | timeout budget, retry layering, correlation id, per-process clients |
| Async-модели | Celery vs asyncio roles, bridge limits, pool compatibility |
| DI и конфиг | explicit dependencies, test seams, unified settings |
| ML/ETL | chunking, checkpointing, resource isolation, idempotent stages |

#### Проверь себя: справочник

1. Как использовать этот справочник при разборе инцидента?
2. Почему он не заменяет полный материал разделов?

<details><summary>Ответ</summary>

1) Быстро выбрать слой проблемы и перейти в нужный раздел за подробной процедурой действий.  
2) Он дает опорные тезисы, но не содержит полной причинно-следственной логики и примеров.

</details>

---

### Анти-путаница: где проблема интеграции, а где проблема Celery

| Наблюдаемый симптом | Частая неверная интерпретация | Более вероятный реальный слой | Что проверить первым |
|---|---|---|---|
| `DoesNotExist` сразу после публикации | "Celery теряет сообщения" | транзакционные границы ORM | publish до commit, наличие `on_commit` |
| Массовые retries при деградации API | "Worker сломан" | retry layering + timeout budget | ретраи в HTTP-клиенте и Celery одновременно |
| Случайные сетевые ошибки после деплоя | "Брокер нестабилен" | fork-unsafe клиент/канал | lifecycle клиента per process |
| Падения после релиза с новыми полями | "Сломался transport" | несовместимость payload-схемы | backward compatibility и `schema_version` |
| Редкие cross-tenant инциденты | "Проблема очередей" | DI/конфигурация и tenant context | явная передача `tenant_id`, tenant-aware dependencies |

Ключевой принцип: сначала ищи причину на **границе интеграции**, и только потом подозревай внутренности Celery.

#### Проверь себя: анти-путаница

1. Почему “Celery теряет сообщения” часто оказывается неверной гипотезой?
2. Что проверять первым при всплеске retries: worker-код или policy-слой?

<details><summary>Ответ</summary>

1) Потому что похожие симптомы часто вызываются транзакциями, payload-контрактом или сетевыми деградациями.  
2) Policy-слой (timeout/retry budget и классификацию ошибок), затем уже детали кода worker.

</details>

---

### Сравнение подходов: Django vs SQLAlchemy в Celery-задачах

| Аспект | Django ORM | SQLAlchemy |
|---|---|---|
| Публикация после commit | `transaction.on_commit(...)` встроен и очевиден | обычно делается через явный application-layer хук после commit |
| Очистка соединений в worker | `close_old_connections()` + сигналы `task_prerun/postrun` | `Session.remove()`/`session.close()` в `finally` |
| Риск утечек в prefork | высокий без дисциплины закрытия соединений | высокий при глобальной Session или неочищенном `scoped_session` |
| Типичный антипаттерн | передача model instance в payload | использование одной глобальной Session на процесс |
| Рекомендуемая единица работы | id в payload + ORM-read внутри задачи | per-task Session scope + явный commit/rollback |

Практический вывод: фреймворк меняется, но инвариант один — **publish после commit, lifecycle соединений в границах задачи**.

#### Проверь себя: Django vs SQLAlchemy

1. Что в этом сравнении является инвариантом, независимо от ORM?
2. Какой типичный антипаттерн уникален для каждой стороны таблицы?

<details><summary>Ответ</summary>

1) Связка publish-after-commit и короткий, управляемый lifecycle соединений/сессий.  
2) Django: передача model instance в payload; SQLAlchemy: глобальная Session на процесс.

</details>

---
