[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## 19.2. Flask + Celery

### Цель раздела

Научиться корректно встраивать Celery в Flask-приложения (включая app factory pattern), сохраняя чистые границы между Flask context и worker execution.

### В этом разделе главное

- Flask context не существует автоматически внутри Celery worker-а.
- Нужно явно инициализировать Celery вместе с Flask app-конфигом.
- Для легаси-систем особенно важны единые правила импортов и точки инициализации.
- `current_app` в задаче без подготовленного контекста часто приводит к трудноуловимым ошибкам.

### Термины

| Термин | Определение |
|---|---|
| **Application Factory** | Паттерн Flask, где app создается функцией `create_app()`. |
| **App Context** | Контекст Flask-приложения, дающий доступ к `current_app`, конфигу и расширениям. |
| **Request Context** | Контекст текущего запроса (`request`, `g`), живет только в HTTP-потоке. |

### Теория и правила

#### Интуиция

Во Flask многие вещи берутся "из контекста". Celery-задача запускается не в HTTP-запросе, поэтому контекст нужно готовить явно, иначе код может работать "иногда" и падать "иногда".

#### Точная формулировка

Интеграция Flask + Celery корректна, если:

1. Celery и Flask используют согласованный конфиг;
2. задачи не зависят от request context;
3. app context создается там, где это действительно нужно;
4. бизнес-логика по возможности не привязана к Flask globals.

#### Пример app factory интеграции

```python
# app/extensions.py
from celery import Celery

celery_ext = Celery(__name__)
```

```python
# app/factory.py
from flask import Flask
from app.extensions import celery_ext

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY_BROKER_URL="redis://localhost:6379/0",
        CELERY_RESULT_BACKEND="redis://localhost:6379/1",
    )
    _init_celery(app)
    return app

def _init_celery(app: Flask) -> None:
    celery_ext.conf.update(
        broker_url=app.config["CELERY_BROKER_URL"],
        result_backend=app.config["CELERY_RESULT_BACKEND"],
        task_serializer="json",
        accept_content=["json"],
    )
```

```python
# app/tasks.py
from app.extensions import celery_ext
from app.factory import create_app

@celery_ext.task(bind=True)
def send_invoice_email(self, invoice_id: str):
    app = create_app()
    with app.app_context():
        # здесь можно безопасно использовать Flask extensions
        # но лучше вызывать чистый сервисный слой
        return {"invoice_id": invoice_id, "status": "sent"}
```

#### Production-нюанс: custom Task с app context

Чтобы не открывать `app_context()` вручную в каждой задаче, часто делают базовый Task-класс:

```python
from celery import Task
from app.factory import create_app

flask_app = create_app()

class FlaskContextTask(Task):
    def __call__(self, *args, **kwargs):
        with flask_app.app_context():
            return self.run(*args, **kwargs)
```

И регистрируют Celery с `task_cls=FlaskContextTask`. Это снижает дублирование, но не отменяет правило: payload должен быть независим от request context.

### Пошагово

1. Вынеси Celery instance в отдельный модуль (`extensions.py`).
2. Инициализируй его из Flask config в factory.
3. Убедись, что задачи не тянут `request`/`g` напрямую.
4. Если нужен app context, открывай его явно и локально.
5. Сложную логику держи в сервисах, не во Flask globals.
6. Избегай создания нового Flask app внутри каждой задачи: создай один раз на старте worker-процесса.
7. Зафиксируй единый импортный путь для worker startup, чтобы исключить расхождения конфигурации.

### Простыми словами

Flask-контекст — как "кабинет, где лежат нужные бумаги". Worker приходит в другое здание. Если ему нужны бумаги из кабинета, он должен открыть кабинет специально, а не надеяться, что дверь уже открыта.

### Картинка в голове

```text
HTTP request thread (Flask)      Celery worker process
---------------------------      ---------------------
request + app context            no request context by default
current_app available            current_app unavailable unless app_context opened
```

### Как запомнить

**Flask context не телепортируется в Celery.**

### Примеры

Пример плохой практики:

```python
# Плохо: task зависит от request context
from flask import request

@celery_ext.task
def bad_task():
    return request.headers["X-User"]  # вне request context упадет
```

Пример правильной идеи:

```python
@celery_ext.task
def good_task(user_id: str):
    # все нужное передано явно
    return {"processed_for_user": user_id}
```

### Практика / реальные сценарии

- Flask-монолиты с legacy blueprint-ами;
- API + админка на Flask, где фоновые задачи отправляют уведомления;
- старые ERP/CRM системы, где Celery вводят постепенно, без большого рефакторинга.

#### Команды запуска и проверки базового контура

```bash
# 1) Запустить Flask API
flask --app app.factory:create_app run --port 8000

# 2) Запустить Celery worker
celery -A app.extensions.celery_ext worker -l INFO -Q default,reports

# 3) (Опционально) запустить beat для периодики
celery -A app.extensions.celery_ext beat -l INFO
```

```bash
# Быстрая проверка "жив ли worker"
celery -A app.extensions.celery_ext inspect ping
```

Эти команды полезны в учебной практике: сначала убедиться, что контур живой, и только потом отлаживать payload/бизнес-логику.

### Типичные ошибки

- считать, что `current_app` безопасно доступен всегда;
- инициализировать Celery в нескольких местах разными конфигами;
- смешивать инфраструктурную и бизнес-логику в task-функции;
- делать import циклы между `factory`, `tasks`, `routes`.
- создавать Flask app на каждый task call (лишние накладные расходы и риск рассинхрона конфигурации).

### Что будет, если...

- **...держать heavy logic внутри task декоратора без сервисного слоя**: сложно тестировать и переиспользовать.
- **...инициализировать Celery лениво и непредсказуемо**: "работает локально, падает в worker контейнере".
- **...не контролировать import graph**: циклические импорты, проблемы autodiscovery.

### Проверь себя

1. Почему request context нельзя считать доступным внутри Celery-задачи?

<details><summary>Ответ</summary>

Потому что задача исполняется в другом процессе и в другое время, вне исходного HTTP-запроса. Request context живет ограниченно и не переносится через broker.

</details>

2. Что дает app factory в интеграции с Celery?

<details><summary>Ответ</summary>

Единый способ создания и конфигурирования приложения, меньше глобального состояния и более предсказуемая инициализация расширений, включая Celery.

</details>

3. Почему важно отделять сервисный слой от Flask globals?

<details><summary>Ответ</summary>

Это снижает связность, упрощает тесты и делает код переносимым между Flask, FastAPI и чистыми worker-процессами.

</details>

### Запомните

Flask + Celery стабильны, когда контекст приложения включается осознанно, а контракт задачи не зависит от request-магии.

#### Дополнительная самопроверка по подпунктам 19.2

1. Почему создание Flask app "на каждый task" считается плохой практикой?

<details><summary>Ответ</summary>

Это повышает накладные расходы, усложняет конфигурационную предсказуемость и может приводить к расхождениям окружения между вызовами. Обычно лучше единая инициализация и контролируемый app context.

</details>

2. Как app factory помогает в тестировании Celery-интеграции Flask?

<details><summary>Ответ</summary>

Позволяет создавать предсказуемые тестовые экземпляры приложения с явной конфигурацией и изоляцией зависимостей, уменьшая влияние глобального состояния.

</details>

---
