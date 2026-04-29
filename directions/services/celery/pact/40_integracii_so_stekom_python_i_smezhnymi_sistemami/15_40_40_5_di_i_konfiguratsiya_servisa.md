[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## 40.5 DI и конфигурация сервиса

### Цель раздела

Построить интеграцию задач Celery с настройками и зависимостями приложения так, чтобы код оставался тестируемым, расширяемым и прозрачным для сопровождения.

### В этом разделе главное

- задача не должна неявно зависеть от глобальных mutable singleton-объектов;
- конфигурация должна быть явной и предсказуемой;
- внешние зависимости (repo/client/cache) должны подменяться в тестах без боли;
- DI в Celery — это про контроль границ, а не про "модность архитектуры".

### Термины

| Термин | Значение |
|---|---|
| **Service wiring** | Способ собрать объектный граф зависимостей приложения. |
| **Implicit dependency** | Скрытая зависимость, не видная из сигнатуры/контракта функции. |
| **Test seam** | Точка, где можно безопасно подменить зависимость в тесте. |
| **Configuration drift** | Расхождение настроек между environments. |

### Теория и правила

1. **Антипаттерн глобального singleton**  
   Глобальный клиент/репозиторий с mutable state сложно тестировать и контролировать между задачами.

2. **Явная фабрика зависимостей**  
   Лучше держать `build_service()`/`get_dependencies()` слой, который возвращает готовый набор зависимостей для задачи.

3. **Settings injection**  
   В Django/FastAPI полезно передавать в бизнес-слой "объект настроек" или иммутабельные значения, а не читать `os.environ` глубоко в каждой функции.

4. **Тестируемость**  
   Если зависимость нельзя подменить в unit/integration-тесте без monkeypatch глубины 5 уровней — архитектура слишком скрытая.

5. **Django/FastAPI settings injection**  
   Важно не дублировать источник настроек. Один слой конфигурации должен использоваться и web/API, и worker-процессами.

### Пошагово: минимальная DI-схема для задач

1. Выдели бизнес-функцию отдельно от Celery-декоратора.
2. Создай фабрику зависимостей (`build_x_service`).
3. В задаче получи сервис через фабрику и вызови бизнес-функцию.
4. В тестах подмени фабрику/провайдер на fake/mock.
5. Внедри конфигурацию через централизованный settings-объект.

### Простыми словами

DI — это когда ты не прячешь "провода" внутри стены. Все подключения видны, и в тесте можно временно подсоединить безопасный стенд вместо боевой системы.

### Картинка в голове

```text
Task wrapper -> build dependencies -> call pure business service
                    ^ test can replace this seam
```

### Как запомнить

**Явная зависимость лучше скрытой магии.**

### Примеры

```python
from celery import shared_task

def process_refund(refund_id: str, refund_service):
    return refund_service.process(refund_id)

def build_refund_service():
    # construct repositories/clients/settings here
    return RefundService(...)

@shared_task
def process_refund_task(refund_id: str):
    service = build_refund_service()
    return process_refund(refund_id, refund_service=service)
```

Тест:

```python
def test_process_refund_task(monkeypatch):
    class FakeService:
        def process(self, refund_id):
            return {"refund_id": refund_id, "status": "ok"}

    monkeypatch.setattr("myapp.tasks.build_refund_service", lambda: FakeService())
    result = process_refund_task("r_1")
    assert result["status"] == "ok"
```

FastAPI-style settings provider:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    payment_api_base_url: str
    payment_api_timeout_sec: float = 2.0

def get_settings() -> Settings:
    return Settings()
```

### Практика / реальные сценарии

- **FastAPI + Celery:** настройки API и worker расходятся, потому что worker читает env иначе. Решение — единый settings слой и явная инъекция.
- **Django monolith:** задача напрямую импортирует "толстые" сервисы с побочными init-эффектами, запуск worker тормозит и падает на старте.
- **Multi-tenant SaaS:** без явной передачи `tenant_id` и tenant-aware dependency factory можно случайно смешать данные арендаторов.

### Типичные ошибки

- хранить mutable глобальные клиенты без явного lifecycle;
- прятать критичные настройки в глубине call stack;
- писать задачи, которые невозможно протестировать без реальных внешних систем.

### Что будет, если...

- **...оставить неявные зависимости?**  
  Любой рефакторинг превращается в рискованный "черный ящик", а тесты дают ложное чувство безопасности.

- **...не синхронизировать конфиг web/worker?**  
  Возникают расхождения поведения: "в API работает, в Celery падает".

### Проверь себя

1. Почему DI в Celery напрямую влияет на скорость диагностики инцидентов?
2. Что лучше подменять в тесте: низкоуровневый HTTP-клиент или бизнес-сервис целиком?
3. Как понять, что задача слишком связана с инфраструктурой?

<details><summary>Ответ</summary>

1) Потому что явные зависимости сразу показывают, где искать проблему и что можно мокнуть/изолировать.  
2) Обычно бизнес-сервис на test seam уровне; низкоуровневый мок часто делает тесты хрупкими.  
3) Если её нельзя выполнить в тесте без десятка внешних компонентов и сложных monkeypatch.

</details>

### Запомните

Celery-задача должна быть тонкой оболочкой вокруг явного бизнес-сервиса и явных зависимостей.

---
