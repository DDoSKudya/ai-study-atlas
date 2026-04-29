[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## 36.2 Брокер и соединения

### Цель раздела

Разобрать, как Celery управляет соединениями с брокером и что означает каждая группа параметров надежности подключения.

### В этом разделе главное

- `broker_url` — только начало; реальная устойчивость задается retry/pool/heartbeat/SSL;
- split `broker_read_url`/`broker_write_url` полезен для сложных топологий;
- `broker_transport_options` нужно проектировать вместе с конкретным transport.

### Термины

| Термин | Формально | Простыми словами |
|---|---|---|
| `broker_url` | Строка подключения к брокеру | Куда подключаться за сообщениями |
| `broker_read_url` / `broker_write_url` | Раздельные endpoint-ы для consume/publish | Читать и писать можно в разные точки |
| `broker_connection_retry` | Повтор подключения при временных ошибках | "Пробуй снова, если сеть мигнула" |
| `broker_pool_limit` | Размер пула брокерных соединений | Сколько соединений держим одновременно |
| `broker_heartbeat` | Механизм проверки живости соединения | Пульс канала, чтобы вовремя замечать обрывы |
| `broker_use_ssl` | TLS-параметры подключения | Шифрование и валидация сертификата |

### Теория и правила

1. **Read/write split нужен не всегда.**  
   Полезен, когда у брокера разная инфраструктура для producer и consumer (например, разные endpoint-ы/маршруты).
2. **Retry не отменяет архитектурные ошибки.**  
   Если брокер системно недоступен, бесконечные retry создадут storm логов и нагрузку на сеть.
3. **Heartbeat связан с failover latency.**  
   Слишком редкий heartbeat -> долго замечаем обрыв; слишком частый -> лишняя нагрузка.
4. **Transport options — это контракт с конкретным драйвером.**  
   У Redis, RabbitMQ, SQS разные ключи и semantics.

### Пошагово

1. Зафиксируй основной `broker_url` и требования к failover.
2. Настрой retry-политику для startup и runtime отдельно.
3. Подбери heartbeat и pool_limit под нагрузку.
4. Включи TLS и проверь валидацию сертификата.
5. Настрой transport-specific options и протестируй на реальных отказах.

### Простыми словами

Broker-конфигурация — это "правила выживания на плохой сети". С хорошей сетью почти любые значения работают. С плохой — только продуманные.

### Картинка в голове

Это как логистика склада: адрес склада (`broker_url`), резервные дороги (`retry`), число грузовиков (`pool_limit`), рация водителя (`heartbeat`), охрана на воротах (`SSL`).

### Как запомнить

**URL подключает, но policy стабилизирует.**

### Примеры

```python
broker_url = "amqp://celery:secret@rabbitmq:5672/prod"
broker_read_url = "amqp://celery:secret@rabbitmq-read:5672/prod"
broker_write_url = "amqp://celery:secret@rabbitmq-write:5672/prod"

broker_connection_retry = True
broker_connection_retry_on_startup = True
broker_connection_max_retries = 100
broker_pool_limit = 20
broker_heartbeat = 30
broker_use_ssl = {
    "ca_certs": "/etc/ssl/ca.pem",
    "cert_reqs": "required",
}
```

```python
# Пример transport options для Redis (примерный набор, сверять с версией)
broker_transport_options = {
    "visibility_timeout": 3600,
    "fanout_prefix": True,
    "fanout_patterns": True,
}
```

### Практика / реальные сценарии

- **Kubernetes + RabbitMQ:** heartbeat и retry-настройки под network blips во время rolling update.
- **Hybrid cloud:** read/write split для минимизации межзонных задержек.
- **Redis broker:** контроль `visibility_timeout` совместно с `task_time_limit`.

### Типичные ошибки

- включить retry без ограничения и без алертов по длительной деградации;
- выставить большой `broker_pool_limit` на маленьком инстансе и получить file descriptor pressure;
- считать SSL "включенным", но не проверять `cert_reqs`.

### Что будет, если...

- **...heartbeat слишком редкий:** worker долго не замечает разрыв и задачи "замирают" в переходном состоянии.
- **...retry policy агрессивная:** получишь шум, перегруз и плохую диагностику первопричины.

### Проверь себя

1. Зачем разделять `broker_connection_retry_on_startup` и runtime retry?
2. Почему `broker_transport_options` нельзя копировать между Redis и RabbitMQ?
3. Какая связь между `task_time_limit` и `visibility_timeout` у Redis/SQS-подобных сценариев?

<details><summary>Ответ</summary>

1) Startup retry определяет, поднимется ли сервис при временной недоступности инфраструктуры; runtime retry влияет на поведение уже работающих worker-ов.  
2) Потому что это разные драйверы и разные semantics ключей; одинаковое имя не гарантирует одинаковое поведение.  
3) Если `visibility_timeout` меньше реального времени задачи, сообщение может быть выдано повторно до завершения первого исполнения.

</details>

### Запомните

Надежность подключения определяется не строкой URL, а сочетанием retry, heartbeat, pool и transport-опций.

### Сравнение transport options: RabbitMQ vs Redis vs SQS (практический минимум)

| Транспорт | Что обычно настраивают в `broker_transport_options` | Где чаще ломается | Что проверять в первую очередь |
|---|---|---|---|
| **RabbitMQ (AMQP)** | heartbeat/reconnect/failover, иногда confirm-подобные паттерны на уровне publish-политики | connection churn, очереди с неверной durability/policy | стабильность соединения, redelivery-поведение, broker alarms |
| **Redis** | `visibility_timeout`, fanout-параметры, retry-поведение | повторная доставка при длинных задачах и коротком timeout | соотношение `visibility_timeout` и реальной длительности задач |
| **SQS** | visibility timeout, polling-параметры, batch receive/delete, региональные/IAM настройки | latency polling, стоимость запросов, дубли после timeout | hit-rate polling, стоимость API calls, идемпотентность |

**Практический вывод:** один и тот же Celery-код задач может вести себя по-разному из-за transport semantics. Поэтому профиль transport-опций должен быть отдельным артефактом, а не "копипастой".

#### Проверь себя: transport comparison

1. Почему одинаковый `visibility_timeout` в Redis и SQS не означает одинаковое поведение?
2. Какой ранний симптом указывает на ошибочный transport-профиль?

<details><summary>Ответ</summary>

1) Потому что transport различаются моделью доставки/поллинга и подтверждений, а значит одинаковые значения дают разные эффекты.  
2) Рост lag/дублей/стоимости при стабильном коде и сопоставимой нагрузке.

</details>

---
