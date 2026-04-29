[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## 19.6. Pytest и FastAPI/Flask: тестирование endpoint-ов, публикующих задачи

### Цель раздела

Научиться тестировать не "факт вызова функции", а корректность интеграционного контракта: что endpoint валидирует вход, публикует нужную задачу с нужными параметрами и корректно обрабатывает ошибки публикации.

### В этом разделе главное

- Тесты должны проверять контракт публикации и поведение API.
- Eager mode полезен, но ограничен: он не заменяет интеграционные тесты с реальным broker.
- Моки publish layer часто эффективнее, чем моки internals Celery.
- Нужны тесты негативных сценариев (broker недоступен, invalid payload, duplicate requests).

### Термины

| Термин | Определение |
|---|---|
| **Contract test** | Тест соответствия структуры и смысла передаваемого payload/headers. |
| **Integration test** | Тест взаимодействия компонентов с реальными зависимостями (или близкими к ним). |
| **Failure path** | Сценарий неуспеха (ошибка публикации, таймаут, неверный input). |

### Теория и правила

#### Три уровня полезных тестов

1. **Unit**: endpoint вызывает publish layer с ожидаемыми аргументами.
2. **Contract**: публикация содержит верные ключи, версии, маршрутизацию и метаданные.
3. **Integration**: сообщение реально доходит до broker и подхватывается worker-ом (в тестовом контуре).

#### Рекомендуемый тестовый пирамидальный баланс

- много быстрых unit/API тестов на контракт публикации;
- умеренно контрактных тестов на schema/version/headers;
- меньше, но обязательные integration smoke тесты с живым broker.

Так достигается баланс "скорость CI + реальная уверенность".

#### Что именно должно быть проверено перед production (чеклист)

| Проверка | Почему критично | Где проверять |
|---|---|---|
| Endpoint не возвращает 202 при ошибке publish | Иначе ложный успех для клиента | API tests + failure path |
| Payload имеет `contract_version` | Без этого опасны rolling deploy | Contract tests |
| Передается `correlation_id` | Без него слабая диагностика инцидентов | API + worker log assertions |
| Worker слушает нужные очереди | Иначе "зависшие" задачи | Integration smoke |
| Retry-политика не бесконечная | Иначе retry storm | Config tests / review |
| Есть idempotency стратегия | Иначе дубли side effects | Domain tests |
| Есть сценарий broker outage | Иначе неконтролируемая деградация | Chaos/smoke tests |

#### Пример минимального integration smoke контура

```text
pytest (integration marker)
  -> поднимает test broker (docker compose service)
  -> публикует одну тестовую задачу
  -> ждет ограниченное время результат/событие
  -> валидирует, что worker получил корректный payload version
```

Принципиально важно, чтобы такой smoke-тест был коротким, стабильным и запускался регулярно (например, nightly + перед релизом).

#### Почему только eager mode недостаточно

Eager mode исполняет задачу в процессе теста и скрывает классы ошибок распределенной системы:

- сетевые/брокерные сбои;
- конфигурационные ошибки очередей;
- реальные проблемы сериализации;
- рассинхрон worker-кода и API-кода.

#### FastAPI пример теста endpoint-а

```python
from fastapi.testclient import TestClient
from app.main import app

def test_build_report_publishes_task(monkeypatch):
    captured = {}

    def fake_publish_build_report(report_id: str, user_id: str, request_id: str) -> str:
        captured["report_id"] = report_id
        captured["user_id"] = user_id
        captured["request_id"] = request_id
        return "task-123"

    monkeypatch.setattr("app.api.routes_reports.publish_build_report", fake_publish_build_report)

    client = TestClient(app)
    response = client.post("/reports/r-1/build", headers={"x-request-id": "req-77"})

    assert response.status_code == 202
    assert response.json()["task_id"] == "task-123"
    assert captured == {"report_id": "r-1", "user_id": "current-user-id", "request_id": "req-77"}
```

#### Тест failure path (broker недоступен)

```python
def test_build_report_returns_503_when_broker_unavailable(monkeypatch, client):
    def failing_publish(*args, **kwargs):
        raise ConnectionError("broker unavailable")

    monkeypatch.setattr("app.api.routes_reports.publish_build_report", failing_publish)
    response = client.post("/reports/r-1/build", headers={"x-request-id": "req-77"})

    assert response.status_code == 503
    assert response.json()["detail"] == "task queue unavailable"
```

#### Контрактный тест на обратную совместимость payload

```python
def test_payload_v1_is_still_accepted_by_worker_contract():
    payload = {
        "contract_version": 1,
        "entity_id": "order_1",
        "correlation_id": "req-1",
    }
    # validate_task_payload - условный валидатор в shared module
    assert validate_task_payload(payload) is True
```

Даже такой простой тест защищает от случайного удаления полей или изменения типов, несовместимого с очередью старых сообщений.

#### Flask пример теста endpoint-а

```python
def test_invoice_endpoint_publishes_task(client, monkeypatch):
    called = {}

    def fake_publish(invoice_id: str, request_id: str) -> str:
        called["invoice_id"] = invoice_id
        called["request_id"] = request_id
        return "task-999"

    monkeypatch.setattr("app.routes.publish_invoice_task", fake_publish)
    resp = client.post("/invoices/i-5/send", headers={"X-Request-Id": "req-a1"})

    assert resp.status_code == 202
    assert called["invoice_id"] == "i-5"
```

### Пошагово

1. Вынеси публикацию задач в отдельные функции/класс.
2. В unit/API тестах мокай именно publish layer.
3. Проверяй статус-код и структуру ответа (`202`, `task_id`).
4. Проверяй обязательные поля контракта и headers.
5. Добавь отдельные integration тесты с реальным broker в CI/nightly.
6. Прогоняй негативные сценарии и проверяй graceful error handling.
7. Тестируй backward compatibility payload между версиями worker-а.

### Простыми словами

Хороший тест здесь проверяет, что "заявка оформлена правильно и отправлена по правильному каналу", а не только то, что "какая-то функция дернулась".

### Картинка в голове

```text
API Test: input -> endpoint -> publish contract -> 202 response
Integration Test: publish -> broker -> worker consume -> observable result
```

### Как запомнить

**Моки для скорости, интеграция для правды.**

### Практика / реальные сценарии

- регресс после изменения payload schema;
- смена имени очереди без обновления worker команд;
- случайная утрата correlation headers;
- переход с Flask на FastAPI с сохранением контрактов задач.

### Типичные ошибки

- тестировать только happy path;
- не проверять headers/metadata;
- использовать только eager mode и думать, что "все покрыто";
- мокать слишком глубоко internals Celery, теряя смысл бизнес-контракта.

### Что будет, если...

- **...нет контрактных тестов**: изменения payload ломают worker незаметно до продакшна.
- **...нет integration smoke тестов**: конфигурационные ошибки обнаруживаются после релиза.
- **...не тестировать failure path**: API может отвечать 200/202 даже при фактическом провале публикации.
- **...не проверять обратную совместимость payload**: rolling deploy превратится в лотерею.
- **...не отделять тесты API-публикации от тестов бизнес-логики worker-а**: диагностика падений становится долгой и дорогой.

### Мини-практика (end-to-end учебный сценарий)

Цель: руками пройти полный путь от HTTP-запроса до выполнения задачи и увидеть, как работают контракт, статусы и диагностика.

Шаги:

1. Подними API, broker и worker в локальном окружении.
2. Отправь `POST` на endpoint, публикующий задачу, и сохрани `task_id` + `correlation_id`.
3. Проверь, что статус операции перешел в `queued`.
4. Убедись по логам worker-а, что пришел тот же `correlation_id`.
5. Дождись финального статуса (`success` или `failure`) и сравни с ожиданием.
6. Повтори сценарий с искусственной ошибкой publish и проверь корректный failure path API.
7. Повтори сценарий с payload старой версии (`contract_version=1`) и проверь backward compatibility.

Ожидаемый учебный результат:

- ты увидишь, что асинхронный контракт — это наблюдаемый процесс, а не "черный ящик";
- ты проверишь не только happy path, но и эксплуатационные ветки сбоев;
- ты закрепишь связь между тестами, логами и реальной работой системы.

### Проверь себя

1. Почему полезно мокать publish layer, а не `celery.Task.apply_async` повсюду?

<details><summary>Ответ</summary>

Так тест остается ближе к бизнес-контракту API и менее хрупким к техническим изменениям внутри Celery-интеграции.

</details>

2. Какие ошибки не ловит eager mode?

<details><summary>Ответ</summary>

Реальные ошибки брокера/сети, часть сериализационных и маршрутизационных проблем, рассинхрон между отдельными процессами и окружениями.

</details>

3. Что обязательно должно проверяться в endpoint тестах, публикующих задачи?

<details><summary>Ответ</summary>

Статус ответа API, факт и корректность публикации (payload, headers, queue/routing), и обработка ошибок публикации.

</details>

### Запомните

Тестирование интеграции Celery в web API — это проверка контракта и эксплуатационного поведения, а не только "вызвали метод".

#### Дополнительная самопроверка по подпунктам 19.6

1. Почему integration smoke-тесты должны быть короткими, но обязательными?

<details><summary>Ответ</summary>

Они быстро проверяют реальную связность контура (publish -> broker -> consume), ловят инфраструктурные регрессии и при этом не делают CI чрезмерно медленным.

</details>

2. Что именно ломается, если тестировать только happy path публикации?

<details><summary>Ответ</summary>

Остаются непроверенными failure path, недоступность broker, несовместимость payload и ошибки маршрутизации. В итоге "зелёные" тесты не защищают от реальных прод-инцидентов.

</details>

---
