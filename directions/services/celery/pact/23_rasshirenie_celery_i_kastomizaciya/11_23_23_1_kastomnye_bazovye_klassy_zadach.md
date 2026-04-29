[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## 23.1 Кастомные базовые классы задач

### Цель раздела

Научиться строить единый базовый класс задач, который стандартизирует логирование, retry-логику, трассировку и валидацию аргументов без нарушения принципа "задача должна оставаться простой".

### В этом разделе главное

- base class нужен для **унификации** и **снижения повторяемости**, а не для бизнес-магии;
- правильный base class делает поведение задач предсказуемым;
- retry, logging, tracing и validation лучше реализовывать как маленькие, независимые блоки;
- базовый класс должен быть хорошо протестирован контрактно.

### Термины

| Термин | Формальное значение | Простыми словами |
|---|---|---|
| **Task subclassing** | Наследование от `celery.Task` | Создаем "родителя" для всех задач |
| **`bind=True`** | Передача `self` в функцию задачи | Получаем доступ к `self.request`, `self.retry` |
| **Retry policy** | Формальные правила повторов | Когда, как часто и до какого предела повторять |
| **Validation layer** | Проверка входных параметров | "Не пускаем мусор в задачу" |
| **Structured logging** | Логи с полями вместо свободного текста | Легко фильтровать и анализировать |

### Теория и правила

#### Зачем вообще нужен кастомный base class

Если в проекте десятки задач, появляются повторяющиеся требования:
- единый формат логов;
- единые правила retry;
- единый tracing context;
- единый подход к валидации payload.

Если это дублировать в каждой задаче вручную — получится разнобой.

#### Что **можно** выносить в базовый класс

- инфраструктурные вещи (логирование, retry helpers, метрики, tracing);
- техническую валидацию аргументов;
- небольшие утилиты для единообразия.

#### Что **нельзя** выносить в базовый класс

- бизнес-правила конкретного домена;
- сетевые вызовы, которые нужны только части задач;
- тяжелую магию, которая скрывает поведение от разработчика.

### Пошагово: проектируем устойчивый BaseTask

1. Определи минимальный обязательный набор общих функций.
2. Зафиксируй контракт: что должен получить разработчик "из коробки".
3. Реализуй простые методы-хелперы (`log_start`, `log_success`, `retry_transient`).
4. Добавь безопасную валидацию входа (без перегрузки).
5. Пропиши unit + integration тесты на поведение базового класса.
6. Документируй base class как внутренний framework проекта.

### Простыми словами

Базовый класс задач — это "корпоративный стандарт" поведения. Он нужен, чтобы каждая новая задача автоматически вела себя правильно по техническим требованиям.

### Картинка в голове

Представь фабрику, где все детали проходят через общий контроль качества. BaseTask — это такой контроль: он не делает продукт за вас, но гарантирует, что базовые стандарты соблюдены.

### Как запомнить

**BaseTask = стабильная оболочка, а не скрытая бизнес-логика.**

### Пример: базовый класс с логированием, retry helper и валидацией

```python
from __future__ import annotations

from typing import Any, Iterable

from celery import Task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


class AppBaseTask(Task):
    autoretry_for = ()
    retry_backoff = False
    retry_jitter = True
    retry_kwargs = {"max_retries": 5}

    def validate_required(self, kwargs: dict[str, Any], required: Iterable[str]) -> None:
        missing = [key for key in required if key not in kwargs or kwargs[key] is None]
        if missing:
            raise ValueError(f"Missing required args: {missing}")

    def log_start(self) -> None:
        logger.info(
            "task_started",
            extra={
                "task_name": self.name,
                "task_id": self.request.id,
                "retries": self.request.retries,
            },
        )

    def log_success(self, result: Any) -> None:
        logger.info(
            "task_finished",
            extra={
                "task_name": self.name,
                "task_id": self.request.id,
                "result_type": type(result).__name__,
            },
        )

    def retry_transient(self, exc: Exception, countdown: int = 30):
        logger.warning(
            "task_retry_scheduled",
            extra={
                "task_name": self.name,
                "task_id": self.request.id,
                "error": repr(exc),
                "countdown": countdown,
            },
        )
        raise self.retry(exc=exc, countdown=countdown)
```

```python
from celery import shared_task


@shared_task(bind=True, base=AppBaseTask, name="billing.charge_invoice")
def charge_invoice(self, invoice_id: str, amount_cents: int):
    self.validate_required(
        kwargs={"invoice_id": invoice_id, "amount_cents": amount_cents},
        required=["invoice_id", "amount_cents"],
    )
    self.log_start()
    try:
        # ... business logic ...
        result = {"status": "ok", "invoice_id": invoice_id}
        self.log_success(result)
        return result
    except TimeoutError as exc:
        self.retry_transient(exc, countdown=60)
```

### Дополнение: normalization аргументов до бизнес-логики

Иногда задачи получают данные из разных источников (API, legacy producer, ручной requeue), и формат полей "плавает". Без нормализации это быстро превращается в нестабильность.

```python
from datetime import datetime, timezone


class AppBaseTask(Task):
    # ... остальной код ...
    def normalize_common(self, kwargs: dict[str, Any]) -> dict[str, Any]:
        normalized = dict(kwargs)

        # Нормализация строковых идентификаторов
        if "user_id" in normalized and isinstance(normalized["user_id"], str):
            normalized["user_id"] = normalized["user_id"].strip().lower()

        # Нормализация времени к UTC
        if "event_ts" in normalized and isinstance(normalized["event_ts"], str):
            dt = datetime.fromisoformat(normalized["event_ts"].replace("Z", "+00:00"))
            normalized["event_ts"] = dt.astimezone(timezone.utc).isoformat()

        return normalized
```

```python
@shared_task(bind=True, base=AppBaseTask, name="audit.process_event")
def process_event(self, **kwargs):
    data = self.normalize_common(kwargs)
    self.validate_required(data, required=["user_id", "event_ts"])
    self.log_start()
    # ... далее уже предсказуемый формат payload ...
```

### Чеклист тестов для BaseTask

- проверка, что `retry_transient` действительно выбрасывает `Retry`;
- проверка, что лог-поля (`task_id`, `task_name`) присутствуют в каждом хелпере;
- проверка нормализации граничных входов (пустые строки, timezone offsets, `None`);
- проверка, что валидация не "съедает" ошибки, а явно сигнализирует проблему;
- проверка обратной совместимости BaseTask при добавлении новых helper-методов.

### Пример: tracing hook в BaseTask (OpenTelemetry-подход)

```python
from opentelemetry import trace

tracer = trace.get_tracer("celery.tasks")


class AppBaseTask(Task):
    # ... остальной код ...
    def traced_run(self, fn, *args, **kwargs):
        with tracer.start_as_current_span(self.name) as span:
            span.set_attribute("celery.task_id", self.request.id)
            span.set_attribute("celery.retries", self.request.retries)
            try:
                result = fn(*args, **kwargs)
                span.set_attribute("celery.state", "SUCCESS")
                return result
            except Exception as exc:
                span.record_exception(exc)
                span.set_attribute("celery.state", "FAILURE")
                raise
```

**Почему это полезно:** tracing hook дает сквозную видимость "API -> Celery -> внешняя зависимость" и особенно помогает в сложных инцидентах с деградацией latency.

### Практика / реальные сценарии

1. **Единое логирование в платформенной команде**
   - Проблема: разные команды логировали задачи в разном формате.
   - Решение: общий BaseTask с обязательными ключами (`task_name`, `task_id`, `tenant`, `trace_id`).
   - Эффект: время диагностики упало, потому что поиск в логах стал предсказуемым.

2. **Retry-политика для временных ошибок внешнего API**
   - Проблема: часть задач делала бесконтрольные retry, перегружая поставщика.
   - Решение: `retry_transient` + backoff + jitter в BaseTask.
   - Эффект: снизили retry storm и стабилизировали интеграцию.

### Типичные ошибки

- делать BaseTask слишком "умным" (он начинает управлять бизнесом);
- скрывать сайд-эффекты внутри магических хуков;
- не тестировать поведение при `retry` и `max_retries`;
- ломать обратную совместимость без migration notes.

### Что будет, если...

- **если** положить в BaseTask бизнес-логику,  
  **то** зависимость между задачами станет неявной и отладка усложнится;
- **если** не задокументировать контракт BaseTask,  
  **то** разработчики будут использовать его по-разному и снова появится разнобой;
- **если** делать silent catch в BaseTask,  
  **то** ошибки будут "исчезать", а инциденты — всплывать поздно.

### Проверь себя

1. Почему инфраструктурная логика в BaseTask полезна, а бизнес-логика — риск?

<details><summary>Ответ</summary>

Инфраструктурная логика повторяется почти во всех задачах и должна быть единообразной. Бизнес-логика зависит от контекста домена и в базовом классе обычно превращается в скрытую связанность.

</details>

2. Что важнее: "умный" BaseTask или предсказуемый BaseTask?

<details><summary>Ответ</summary>

Предсказуемый. Умный, но непрозрачный BaseTask усложняет сопровождение и повышает риск регрессий.

</details>

3. Зачем тестировать BaseTask отдельно от бизнес-задач?

<details><summary>Ответ</summary>

Потому что он влияет на поведение всех задач сразу. Ошибка в нем масштабируется на всю систему.

</details>

### Запомните

- BaseTask — это инструмент стандартизации, а не место для бизнес-правил.
- Каждый добавленный хук должен иметь понятную ценность и тесты.
- Хороший BaseTask снижает когнитивную нагрузку, плохой — увеличивает.

### Вопросы по подблокам 23.1

1. Как связаны между собой подблоки "что можно выносить", "normalization", "чеклист тестов" и "типичные ошибки"?

<details><summary>Ответ</summary>

Это единая цепочка качества: сначала определяем границы ответственности BaseTask, затем приводим вход к стабильному формату (normalization), потом закрепляем поведение тестами и отслеживаем анти-паттерны, чтобы не скатиться в скрытую бизнес-логику.

</details>

2. Когда нормализация аргументов в BaseTask улучшает систему, а когда становится вредной?

<details><summary>Ответ</summary>

Полезна, когда устраняет технический шум (регистр, формат времени, пустые поля). Вредна, когда начинает менять доменный смысл данных или скрывать ошибки producer-а вместо явной валидации и фикса на источнике.

</details>

3. Почему tracing hook в BaseTask не должен заменять бизнес-логирование в задачах?

<details><summary>Ответ</summary>

Tracing hook отвечает за инфраструктурную наблюдаемость (latency, retries, exception-path), а бизнес-логирование фиксирует доменные события. Смешение ролей создает шум и делает обе формы телеметрии менее полезными.

</details>

---
