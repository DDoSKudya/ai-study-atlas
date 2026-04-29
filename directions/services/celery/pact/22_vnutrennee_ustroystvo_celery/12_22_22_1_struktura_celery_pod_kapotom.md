[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## 22.1 Структура Celery под капотом

### Цель раздела

Понять архитектурный "скелет" Celery и границы ответственности внутренних компонентов.

### В этом разделе главное

- Celery состоит из связанных, но независимых подсистем;
- `app` управляет конфигурацией и регистрацией задач, но не исполняет задачи сам;
- worker включает consumer-часть и execution-часть (pool);
- event/control-подсистемы отдельны от result backend.

### Термины

| Термин | Определение |
|---|---|
| **App** | Центр конфигурации Celery и реестр задач. |
| **Worker main process** | Процесс, который управляет consumer, пулом и control-channel. |
| **Execution pool** | Подсистема исполнения задач (prefork/threads/gevent/solo). |
| **Event dispatcher** | Публикация событий состояния для мониторинга. |

### Теория и правила

1. **App-layer:** отвечает за конфиг, имя приложения, импорт задач, policy.
2. **Messaging-layer:** broker + transport abstractions (через Kombu).
3. **Worker control-layer:** запуск/остановка внутренних компонентов, remote commands.
4. **Execution-layer:** запуск task callable и обработка исключений.
5. **State-layer:** запись результата и состояния, отдельно от event stream.

### Важные внутренние границы (где часто путаются)

| Пара похожих понятий | В чем различие | Почему это важно |
|---|---|---|
| **Event stream** vs **Result backend** | Events: поток телеметрии о жизни worker/task. Backend: долговременное состояние результата. | Потеря events не всегда ломает бизнес, а потеря backend state может ломать orchestration и клиентские статусы. |
| **Main process** vs **Pool child** | Main принимает и маршрутизирует задачи, child их исполняет. | Проблема может быть только в child-процессах, при живом main. |
| **Task declaration** vs **Task execution** | Декларация в коде и регистрация в app не равны успешному выполнению на worker. | Можно иметь корректный код и сломанный execution-контур из-за среды. |

### Пошагово

1. Producer формирует task message.
2. Broker сохраняет и маршрутизирует сообщение.
3. Worker consumer резервирует сообщение с учетом prefetch/QoS.
4. Strategy связывает `task_name` из сообщения с объектом из registry.
5. Задача уходит в pool.
6. После завершения происходит update state/result + ack/reject.

### Простыми словами

Представь логистический хаб:

- `app` — офис планирования и каталог маршрутов;
- broker — склад посылок;
- consumer — приемщик на складе;
- pool — бригада доставки;
- backend/events — отчетность и трекинг.

### Картинка в голове

```text
app(config+registry) -> broker(queue) -> consumer(dispatch) -> pool(execution)
                                              |                   |
                                              +-> events          +-> result backend
```

### Как запомнить

Запомни формулу: **"регистрация != доставка != исполнение != наблюдаемость"**. Это четыре разные зоны.

### Пример

```python
from celery import Celery

app = Celery("orders")
app.conf.update(
    broker_url="amqp://guest:guest@rabbitmq:5672//",
    result_backend="redis://redis:6379/1",
)

@app.task(name="orders.recalculate")
def recalculate(order_id: int) -> None:
    # Выполнение произойдет уже на execution-layer worker-а
    pass
```

### Практика / реальные сценарии

- **Сценарий:** в логах есть `Received task`, но не появляется `Task started`.
  - Что это обычно означает: consumer слой жив, а execution слой не принимает работу.
  - Что проверить: saturation пула, deadlock в child-процессе, memory/CPU limits, зависшие внешние вызовы.

- **Сценарий:** бизнес говорит "задача завершилась", а API возвращает `PENDING`.
  - Частая причина: state-layer (result backend) не обновлен или данные очищены TTL раньше времени.

### Типичные ошибки

- думать, что `app.task` автоматически гарантирует идемпотентность;
- смешивать telemetry events с business result;
- трактовать worker как монолитный "черный ящик".

### Что будет, если...

**...игнорировать разделение слоев?**  
Диагностика станет хаотичной: проблемы backend будут "лечить" масштабированием pool, а проблемы consumer — ретраями задач.

### Проверь себя

1. Чем event stream отличается от result backend?
2. Почему worker main process и execution pool нужно рассматривать отдельно?

<details><summary>Ответ</summary>

1) Event stream дает телеметрию о ходе выполнения, но не заменяет durable хранение результата.  
2) Потому что consumer/control и execution имеют разные failure modes: можно видеть "received", но не получать "started/success", если pool деградировал.

</details>

### Запомните

Разделение на внутренние слои Celery — главный инструмент инженерной диагностики.

---
