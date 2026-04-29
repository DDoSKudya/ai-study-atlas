[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Сквозная модель транспорта в Celery

```mermaid
flowchart LR
    A[Producer app] -->|publish via Kombu| B[(Transport Driver)]
    B --> C[(Broker)]
    C -->|deliver| D[Worker Consumer]
    D -->|ack/reject/requeue| C
    D --> E[Task Execution]
    E --> F[(Result Backend)]
```

### Визуальная схема границ ответственности (где искать корень проблемы)

```mermaid
flowchart LR
    A[Celery app layer] --> B[Kombu transport layer] --> C[Broker layer] --> D[Network/Infra layer]
    A -. task code/retry/idempotency .-> A
    B -. dialect mapping/parity .-> B
    C -. ack routing dlq semantics .-> C
    D -. DNS TLS ACL latency .-> D
```

Если сбой в `DNS/TLS/маршрутизации`, его не исправить только флагами Celery.  
Если проблема в semantics очереди, ее не исправить только «больше ретраев» в коде задачи.

**Интуиция.**  
Celery похож на «универсальный пульт», а transport — как «переходник под конкретную розетку». Пульт один, но электрические характеристики и ограничения розетки разные.

**Точная формулировка.**  
Kombu абстрагирует transport API, но не устраняет различия между брокерами. Поэтому корректный дизайн Celery-системы всегда включает явное проектирование транспорта, URL и transport options.

**Картинка в голове.**  
Представь логистику: у тебя одинаковые коробки (tasks), но часть едет самолетом (SQS), часть поездом (AMQP), часть грузовиком (Redis). Накладная похожа, но сроки, риски и правила передачи груза разные.

#### Проверь себя: сквозная модель

1. Где в схеме появляется риск «приняли в producer, но потеряли до устойчивой фиксации»?

<details><summary>Ответ</summary>

На пути публикации от producer через transport к брокеру, особенно при сетевых сбоях и неочевидной семантике подтверждения publish. Риск зависит от транспорта и настроек confirms/acks.

</details>

2. Почему нельзя обсуждать idempotency отдельно от транспорта?

<details><summary>Ответ</summary>

Потому что транспорт определяет частоту и условия повторной доставки. Idempotency нужна именно для компенсации реальных re-delivery сценариев конкретного брокера.

</details>

---
