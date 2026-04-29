[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## FINAL. Справочник, сценарии, самопроверка, ошибки, резюме

### Справочник по части 18

| Тема | Коротко |
|------|---------|
| План §18 | Таблица [«Карта соответствия»](#карта-соответствия-глобальному-плану-часть-18) — все подпункты 18.1–18.7 |
| Каркас | `celery.py`, импорт в `__init__.py`, `CELERY_*`, **`CELERY_TASK_ROUTES` / `-Q`**, **`ignore_result`**, **`django.setup()`** в утилитах/cron, `autodiscover_tasks` (**`related_name`** для `jobs.py`), `CELERY_IMPORTS`, `AppConfig.ready` |
| Beat | Статическое `CELERY_BEAT_SCHEDULE` или `django-celery-beat` + `DatabaseScheduler` |
| Транзакции | `on_commit`; **mermaid on_commit vs outbox**; **`ATOMIC_REQUESTS`** не отменяет `on_commit`; **`bulk_create`** без сигналов; **IntegrityError** как идемпотентность; **soft time limit** → `close_old_connections`; replica lag; outbox |
| ORM | **id**/UUID (**str** в JSON, единый контракт); **GFK** = `content_type_id` + `object_id`; N+1; stale/`updated_at`; prefork + БД; пулы **solo/threads/gevent** |
| Нагрузки | Email (`EMAIL_BACKEND`, Anymail, батчи); PDF/Excel стеки; **static** для рендера в worker; экспорт: **iterator**, JSONL, **Job+storage**, не result backend; агрегаты: **`F()`**, **`select_for_update`**, debounce |
| Admin / API | **sequenceDiagram** staff→admin→Job/Audit→broker→worker; **`get_task_logger`**, `extra=` / JSON‑логи, **sequenceDiagram корреляции HTTP→worker**, связка с trace id (ч. 14); модель `Job` + прогресс; `BackgroundActionAudit`; action с `MAX_N` и `on_commit`; **DRF** `perform_create` + `on_commit` |
| Миграции | expand/contract; K8s rolling; **redelivery при `acks_late` + новый код**; **удалённая схема + старые сообщения** |
| Settings | **Наследование `base` → web/worker**; `DATABASES` (`CONN_MAX_AGE`, `CONN_HEALTH_CHECKS`); **UTC/`CELERY_TIMEZONE`**; ASGI: **async view → sync сервис (`sync_to_async`) → atomic/on_commit/delay** |
| Кэш / фронт | **Redis** для общего кэша; polling API к **модели Job**; не отдавать Flower в браузер |
| Локально | 3 процесса: runserver + worker + beat; `inspect ping`; один `SECRET_KEY` |

---

### Частые сценарии

| Задача | Как рассуждать |
|--------|----------------|
| «После создания объекта отправить письмо» | `on_commit` + задача по `pk` + guard идемпотентности |
| «Долгий отчёт для админки» | Модель `ReportJob`, статус, файл в S3/storage, права |
| «Инцидент после миграции» | Совместимость версий кода и схемы, poison в очереди, drain |
| «DatabaseError в worker ночью» | `CONN_MAX_AGE`, балансировщик БД, `close_old_connections` |
| «Инвалидация кэша не доходит до задачи» | Убрать **LocMem** для общих флагов; **Redis** + явный TTL/ключ |
| «SPA не видит прогресс отчёта» | REST **GET** по `job_id` к **БД**, не к брокеру; при необходимости SSE |
| «Экспорт 500k строк — worker умер по RAM» | **`iterator`**, **лимит строк**, запись **потоком** в файл/storage, не держать всё в списке |
| «Счётчик заказов «теряет» при concurrency» | **`F()` + update`** или **`select_for_update`**, не read‑modify‑write в Python без блокировки |
| «Подпись Django валидна в web, ломается в worker» | Один **`SECRET_KEY`** и окружение на всех процессах |
| «Задачи лежат в `jobs.py`, worker их не регистрирует» | **`autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name="jobs")`** и/или **`CELERY_IMPORTS`** |
| «async view: предупреждения про async unsafe / блокировка loop» | БД + **`on_commit`** + **`delay`** в **sync** функции, вызов через **`sync_to_async`** (§18.7) |
| «В логах worker не видно, какой заказ падал» | В задачах **`get_task_logger`** + **`extra`** / JSON с **`order_id`**, **`celery_task_id`** (§18.5, ч. 14) |
| «Задачи в очереди есть, worker молчит» | Проверить **имя очереди** в **`apply_async`**/`TASK_ROUTES` и аргумент **`-Q`** у `celery worker` (§18.1) |
| «Redis забит, а статус и так в БД» | **`ignore_result=True`** на задачах без **`AsyncResult`**; **TTL**/чистка result backend (ч. 6) |
| «`AppRegistryNotReady` в cron-скрипте» | **`DJANGO_SETTINGS_MODULE` + `django.setup()`** до импорта моделей и `delay` (§18.1) |
| «Уведомление по связи GenericForeignKey» | В сообщении **`content_type_id` + `object_id`**, в задаче `ContentType` → `model_class()` → `get` |
| «Пачка через `bulk_create`, задачи не ставятся» | Сигналы **`post_save` не сработали**; явная постановка после пачки или отдельная задача «обработать id» |
| «Дубликаты в логе при retry» | **Unique** + **`IntegrityError`** как успех идемпотентности |

---

### Вопросы из глобального плана (часть 18, блок самопроверки)

*В исходном плане блок помечен как «18.5», но вопросы по смыслу относятся к транзакциям и ORM — здесь даны ответы в терминах §18.2–18.3.*

1. Почему **`transaction.on_commit`** критичен для многих Celery‑задач в Django?

<details><summary>Ответ</summary>

Потому что публикация в брокер **не откатывается** вместе с транзакцией БД, а worker может начать читать данные **до** фиксации изменений. `on_commit` привязывает постановку задачи к **успешному commit** и убирает класс ошибок **rollback + фантомная задача** и **гонка видимости**.

</details>

2. Почему передача **`model instance`** в задачу — плохая идея?

<details><summary>Ответ</summary>

Риск **тяжёлой/опасной** сериализации, **устаревшего** состояния к моменту исполнения, утечки **лишних полей/PII** в брокер, непредсказуемости с **lazy** связями. Идентификатор + **новый SELECT** в worker — контролируемый контракт.

</details>

3. Какие **симптомы** у проблемы «задача стартовала раньше, чем данные стали видимыми»?

<details><summary>Ответ</summary>

`DoesNotExist`, интермиттирующие ошибки под нагрузкой, «**первый** retry проходит», логи с **отсутствующим** `pk` при том что web «успешно создал» объект. Лечение: **`on_commit`**, корректная изоляция, и повторное чтение по `pk` в задаче.

</details>

---

### Вопросы для самопроверки (сквозные)

1. Опиши **минимальный** корректный способ поставить задачу после успешного создания заказа в `atomic()`.

<details><summary>Ответ</summary>

Внутри `atomic()` после `Order.objects.create(...)` зарегистрировать `transaction.on_commit(lambda: process_order.delay(order.id))`, а в задаче выполнить свежий `Order.objects.get(pk=...)`.

</details>

2. Почему **outbox** сильнее `on_commit` с точки зрения **потери события**?

<details><summary>Ответ</summary>

`on_commit` гарантирует момент вызова хука после commit, но **публикация в брокер** может упасть **после** commit без автоматического отката БД. Outbox пишет намерение **в БД атомарно с бизнес‑данными**, и отдельный процесс **повторяет** отправку до успеха (с идемпотентностью на приёмнике).

</details>

3. Назови **три** причины не передавать `User` instance в `delay`.

<details><summary>Ответ</summary>

Риск **большой/опасной** сериализации, **устаревшие** поля к моменту исполнения, лишние **PII** в брокере; правильнее **`user_id`** и выборка в worker‑е.

</details>

---

### Типичные ошибки (сводка)

- `delay` **внутри** `atomic()` **без** `on_commit`.
- Думать, что **`ATOMIC_REQUESTS`** «уже всё оборачивает» и **`on_commit`** не нужен.
- Ожидать **`post_save`** после **`bulk_create`** для постановки задач.
- Передача **ORM‑объектов** и **queryset** в задачи.
- **Один** `settings` для web/worker с неудачным **`CONN_MAX_AGE`**.
- **Ломающие** миграции без **двухфазности** при живых worker‑ах; игнорировать **повторную доставку** задач при смене версии кода и схемы.
- Admin **actions** без **лимитов** и **аудита**; **`delay` в action без `on_commit`** при транзакционном сохранении.
- **LocMemCache** для данных, которые должны совпадать между **web** и **worker**.
- Открывать **Flower** или **broker** из **публичного** фронтенда для статуса джобы.
- Передавать **GFK** как «объект в JSON» вместо пары **`content_type_id` + `object_id`**.
- **`fail_silently=True`** в почтовых задачах без альтернативной диагностики.
- Считать **read‑modify‑write** счётчика в Python «достаточно безопасным» при высокой конкуренции без **`F()`** или **`select_for_update`**.
- В **`async def` view** вызывать **ORM / `on_commit` / `delay`** без **`sync_to_async`** (или эквивалента), блокируя loop и нарушая рекомендации Django.
- Диагностировать задачи только через **`print`** или логи **без** доменных id / **`celery_task_id`** — инциденты не сшиваются с HTTP и Flower.
- Ставить задачи в очередь **`reports`/`exports`**, не подняв worker с **`-Q`**, включающим эти имена.
- Держать **`CELERY_RESULT_BACKEND`** и писать результаты **всех** задач, хотя продуктовый статус уже в **`Job`** и **`AsyncResult` не используется**.
- Вызывать **`delay`** из **cron** или утилиты без **`django.setup()`** и без **`DJANGO_SETTINGS_MODULE`**.

---

### Резюме части

Django и Celery отлично сочетаются, если ты явно проектируешь **границу процессов**: **транзакции** фиксируют данные, **`on_commit`/outbox** синхронизируют публикацию, **идентификаторы** едут в очередь, **ORM** в worker‑е загружает **актуальное** состояние с **дисциплиной соединений**, а **деплой** учитывает **расхождение версий** кода и схемы. Админка и отчёты — это **продуктовый слой** поверх тех же правил: статусы в БД, аудит, лимиты. Следующая логическая часть глобального плана — **часть 19: интеграция с FastAPI/Flask**, где нет Django ORM и `transaction.on_commit`, и те же идеи приходится воплощать **вручную**.

### Ключевые тезисы из плана (часть 18)

- Django + Celery — частый стек; важны **интеграционные ловушки**, не только установка.
- **`transaction.on_commit`** — базовая защита от **rollback** и **гонок видимости**.
- В сообщения — **`pk`**, в worker — **явное чтение**; следи за **соединениями** и **миграциями**.

### Полнота относительно плана

Все буллеты **18.1–18.7** из `mastery_plan.md` разобраны в основных разделах и блоках «Дополнение»; сводная **карта ссылок** — в разделе [«Карта соответствия глобальному плану (часть 18)»](#карта-соответствия-глобальному-плану-часть-18). Дополнительно закрыты типичные **сквозные** дыры стека: **кэш между процессами**, **опрос статуса из SPA**, **локальный запуск**, **таймзоны**, **SECRET_KEY**, **middleware vs задачи**, **тесты `on_commit`**, **сравнение гарантий `on_commit` и outbox (mermaid)**, **`ATOMIC_REQUESTS` + постановка задач**, **`bulk_create`/сигналы**, **идемпотентность через `IntegrityError`**, **пулы worker vs Django ORM**, **DRF `perform_create`**, **soft time limit и соединения к БД**, **поток экспорта web→worker→storage (sequenceDiagram)**, **агрегаты: `F()` и `select_for_update`**, **конвейер пост‑обработки файлов (flowchart)**, **sequenceDiagram админка→worker (§18.5)**, **наследование settings base/web/worker (§18.7)**, **UUID в сообщениях + `on_commit`**, **`autodiscover_tasks` + `related_name`**, **миграции и redelivery/`acks_late` (§18.6)**, **ASGI/async views + `sync_to_async` для atomic/on_commit/delay (§18.7)**, **логирование задач через `get_task_logger` (§18.5)**, **очереди брокера и `CELERY_TASK_ROUTES` (§18.1)**, **`ignore_result` / разгрузка result backend (§18.1)**, **`django.setup()` для скриптов вне worker (§18.1)**. Детали синтаксиса Celery/Django, зависящие от **конкретных версий** библиотек, намеренно отсылаются к официальной документации (эволюция имён настроек и сигналов).

**Оценка полноты относительно плана §18 (для самопроверки автора материала):** ~**98–99%**; оставшийся хвост — вариативность прод‑стека (конкретный UI, SSO, нестандартный broker, vendor‑специфика PDF, выбор антивирусного контура) и версионные отличия API тестов Django / опций `bulk_create`.

---

*Конец части 18.*
