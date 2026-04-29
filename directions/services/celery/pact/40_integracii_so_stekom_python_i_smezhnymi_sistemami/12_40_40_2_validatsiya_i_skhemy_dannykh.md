[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## 40.2 Валидация и схемы данных

### Цель раздела

Научиться формализовывать payload задач так, чтобы сообщения оставались совместимыми, компактными и проверяемыми между релизами.

### В этом разделе главное

- task payload — это публичный контракт, почти как API между сервисами;
- сериализуем только JSON-совместимые типы (или строго оговоренный сериализатор);
- перед выполнением валидируем входные данные и нормализуем типы;
- модель данных должна быть устойчива к эволюции схемы.

### Термины

| Термин | Значение |
|---|---|
| **Schema evolution** | Изменение структуры payload без поломки старых сообщений. |
| **Backward compatibility** | Новая версия обработчика может читать старые сообщения. |
| **`TypeAdapter`** | В Pydantic v2 валидирует/сериализует произвольные типы вне `BaseModel`. |
| **Message bloat** | Перегруженный payload, который замедляет broker/worker и повышает риск ошибок. |

### Теория и правила

1. **Pydantic v1/v2**  
   v2 быстрее и гибче, но в обеих версиях идея одна: явно описываем структуру данных задачи.

2. **`dataclasses`, `attrs`, `msgspec`**  
   Это варианты "описать структуру". Критерий выбора: скорость, удобство валидации, совместимость команды и инфраструктуры.

3. **Что передавать в `args/kwargs`**  
   Передавай примитивы, UUID/строки, числа, компактные словари. Не передавай сокеты, ORM-объекты, открытые файлы, клиентские экземпляры.

4. **Версионирование payload**  
   Для критичных задач добавляй поле `schema_version` или поддерживай tolerant reader (новые поля опциональны, старые читаются с default).

5. **Валидация на границе worker-а**  
   Ошибка валидации — это отдельный класс ошибки. Ее не всегда нужно retry-ить (часто это permanent failure, а не transient).

### Сравнение подходов к схемам данных

| Инструмент | Плюсы | Минусы | Когда выбирать |
|---|---|---|---|
| Pydantic v2 | мощная валидация, удобные ошибки, экосистема | накладные расходы на очень горячем пути | default для большинства бизнес-задач |
| `dataclasses` | минимум магии, stdlib | валидацию надо писать отдельно | простые внутренние payload |
| `attrs` | гибкая модель, валидаторы, mature API | команде нужно договориться о стиле | сложные доменные объекты |
| `msgspec` | высокая скорость encode/decode | более строгая модель, меньше "магии" | high-throughput и большие потоки |

### Пошагово: минимальный контракт payload

1. Определи структуру входа через Pydantic/dataclass.
2. На producer-стороне сериализуй в чистый dict.
3. В задаче сделай валидацию входа перед business logic.
4. Ошибки валидации логируй отдельно от transport/runtime-ошибок.
5. При изменении схемы сохрани backward compatibility минимум на период drain старых сообщений.

### Простыми словами

Payload — это "посылка", которая может ехать долго и попасть к обработчику другой версии кода. Если не подписал коробку стандартом, получатель не поймет, что внутри.

### Картинка в голове

```text
Producer code v1 ----message----> Worker code v2
      |                              |
  contract needed                tolerant parser needed
```

### Как запомнить

**Task payload = API-контракт, а не "случайный словарь".**

### Примеры

Pydantic v2:

```python
from pydantic import BaseModel, TypeAdapter
from uuid import UUID

class PaymentTaskPayload(BaseModel):
    payment_id: UUID
    amount_minor: int
    currency: str
    schema_version: int = 1

payload_adapter = TypeAdapter(PaymentTaskPayload)

@app.task
def process_payment(payload: dict):
    data = payload_adapter.validate_python(payload)
    # data is validated and normalized
    return {"payment_id": str(data.payment_id), "status": "processed"}
```

`dataclass` как промежуточный слой:

```python
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class ExportChunk:
    job_id: str
    offset: int
    limit: int

def enqueue_chunk(job_id: str, offset: int, limit: int):
    chunk = ExportChunk(job_id=job_id, offset=offset, limit=limit)
    export_chunk.delay(asdict(chunk))
```

`attrs` и `msgspec` (концептуальный пример):

```python
import attrs
import msgspec

@attrs.define(frozen=True)
class AuditEvent:
    event_id: str
    tenant_id: str
    action: str

class AuditEventMsg(msgspec.Struct):
    event_id: str
    tenant_id: str
    action: str
```

### Практика / реальные сценарии

- **Миграция релиза:** старые задачи уже в очереди, новый код их потребляет через tolerant schema.
- **Multi-team контур:** одна команда публикует задачи, другая обрабатывает; контракт валидации предотвращает "тихие" несовместимости.
- **Drain очереди после релиза:** старые сообщения с прошлой схемой должны обрабатываться безопасно, пока очередь полностью не опустеет.

### Типичные ошибки

- передавать "всё что есть в объекте" вместо минимального набора полей;
- не различать validation-error и transient network-error;
- добавлять обязательные поля без fallback на drain-период.

### Что будет, если...

- **...делать payload без контракта?**  
  После релиза часть задач начнет падать "случайно", диагностика будет дорогой и долгой.

- **...retry-ить validation ошибки?**  
  Получишь бесполезный retry storm без шанса на успех.

### Проверь себя

1. Чем полезно поле `schema_version`, если есть git history?
2. Почему "толстый payload" вреден даже при быстром брокере?
3. В каком случае validation ошибку можно считать retryable?

<details><summary>Ответ</summary>

1) Сообщение живет в runtime, а не в git; worker должен понять формат на лету.  
2) Он увеличивает I/O, задержку, потребление памяти и риск десериализационных проблем.  
3) Редко: когда ошибка вызвана внешней transient-нормализацией, а не постоянным дефектом структуры.

</details>

### Запомните

Схема payload — это договор между producer и worker. Формализуй его так же строго, как публичный HTTP API.

---
