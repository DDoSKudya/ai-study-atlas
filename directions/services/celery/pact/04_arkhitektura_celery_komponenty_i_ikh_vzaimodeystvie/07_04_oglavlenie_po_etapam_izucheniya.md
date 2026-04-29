[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Оглавление по этапам изучения

### Этап 1. Контур и путь сообщения

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [4.1. Producer, broker, worker, result backend](#41-producer-broker-worker-result-backend) | Кто что делает в контуре; почему broker и backend могут быть разными системами; когда backend можно отключить | producer, broker, worker, result backend, failure boundaries |
| [4.2. Message flow end-to-end](#42-message-flow-end-to-end) | Как формируется task message, как идет routing, как worker reserve/ack, как пишутся состояния | headers, body, properties, routing, reserve, ack, state writing |

### Этап 2. Подсистемы транспорта и результатов

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [4.3. Роль Kombu](#43-роль-kombu) | Kombu как messaging layer; транспортная абстракция; почему транспорт определяет возможности и поведение | Kombu, transport abstraction, AMQP vs Redis/SQS |
| [4.4. Result backend как отдельная подсистема](#44-result-backend-как-отдельная-подсистема) | Зачем backend нужен; где хранятся метаданные; TTL и стоимость хранения | task states, traceback, TTL, storage cost |

### Этап 3. Наблюдаемость и удаленное управление

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [4.5. Event system и remote control](#45-event-system-и-remote-control) | Events и наблюдатели (Flower); broadcast команды; inspect/control; безопасность remote control | events, Flower, inspect/control, network safety |

### Этап 4. Границы отказов

| Раздел | Содержание | Ключевые понятия |
|---|---|---|
| [4.6. Разделение зон отказа](#46-разделение-зон-отказа) | Отдельные сбои broker/result backend/worker; что видит клиент; стратегии деградации при недоступном backend | failure domains, timeouts, caching, degradation |

---
