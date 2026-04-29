[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Карта соответствия глобальному плану (часть 18)

Ниже — **пункты из `mastery_plan.md`** и где они раскрываются в этом файле (можно использовать как чек‑лист при повторении).

| Пункт плана | Где в материале |
|-------------|-----------------|
| **18.1** `celery.py`, автозагрузка из `settings`, `autodiscover_tasks`, запуск worker/beat | [§18.1](#181-базовая-интеграция), **`CELERY_TASK_ROUTES` / очереди**, **`ignore_result`**, **`django.setup()` в скриптах/cron**, дополнения + **ленивые импорты моделей внутри задачи** |
| **18.2** `on_commit`, нельзя до коммита, чтение «свежих» строк, outbox | [§18.2](#182-транзакции-и-публикация-задач), дополнения про автокоммит, вложенный `atomic`, сигналы, **видимость/replica lag**, **схема on_commit vs outbox**, **`ATOMIC_REQUESTS` + on_commit**, **`bulk_create`/сигналы**, **`IntegrityError`/идемпотентность**, **`SoftTimeLimitExceeded` + БД** |
| **18.3** только `id`, stale, N+1/lazy, соединения в child процессах | [§18.3](#183-orm-и-задачи), prefork + БД, N+1, **GFK/`content_type_id`**, **UUID в JSON + `on_commit`**, PgBouncer, multi‑db, **пулы worker (`prefork`/`solo`/threads/gevent)** |
| **18.4** email, отчёты, экспорт, агрегаты, файлы | [§18.4](#184-django-специфичные-сценарии), **18.4.1–18.4.5** + `EMAIL_BACKEND`/Anymail, PDF‑стеки, **static в worker**, **sequenceDiagram экспорта**, **`F()`/`select_for_update` для агрегатов** |
| **18.5** статусы в UI, безопасные кнопки, audit trail | [§18.5](#185-django-admin-и-observability), **sequenceDiagram админка→broker→worker**, Flower, **`get_task_logger` + доменные id в логах**, модель аудита, admin action, **DRF + `on_commit` в `perform_create`** |
| **18.6** порядок миграций vs задачи; чтение удалённой схемы | [§18.6](#186-миграции-django-и-celery), **timeline R1→R3**, **acks_late / redelivery + смена кода**, удалённые таблицы/очередь |
| **18.7** `DATABASES`, `CONN_MAX_AGE`, health checks, web vs worker settings | [§18.7](#187-настройки-django-влияющие-на-worker), **flowchart base/web/worker settings**, **`async` views + `sync_to_async` + on_commit**, пример `DATABASES`, **таймзоны**, диаграмма **middleware vs worker** |
| **Сквозные темы** (кэш, фронт→статус, локальный dev, `SECRET_KEY`) | Дополнения в §18.1, §18.3–18.5, §18.7 и шпаргалка; **сравнение гарантий on_commit/outbox** — §18.2 |

---
