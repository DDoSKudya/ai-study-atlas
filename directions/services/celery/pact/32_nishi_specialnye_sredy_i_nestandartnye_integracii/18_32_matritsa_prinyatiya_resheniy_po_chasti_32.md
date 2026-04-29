[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Матрица принятия решений по части 32

| Вопрос | Если "да" | Если "нет" |
|---|---|---|
| Есть дефицитный GPU-ресурс? | выделить отдельную очередь и policy конкуренции | оставить CPU-контур без усложнения |
| Нужны ad-hoc операции? | заводить `adhoc.*` с guardrails и audit | не смешивать с production pipeline |
| Есть multi-region требования? | региональная маршрутизация + failover runbook | держать единый региональный контур |
| Брокер enterprise-типа через мост? | contract parity тесты и adapter layer | использовать стандартный transport-путь |
| Есть нестандартная ОС? | ограниченный support + risk register | не расширять support без бизнес-основания |

#### Проверь себя: матрица решений

1. Как пользоваться матрицей, если одновременно "да" по нескольким строкам?

<details><summary>Ответ</summary>

Приоритизировать по критичности риска: сначала контуры с высоким blast radius (например, multi-region write path), затем менее критичные. Решения должны быть согласованы между собой через общую policy-модель.

</details>

2. Почему матрица не заменяет детальные runbook-и?

<details><summary>Ответ</summary>

Матрица помогает выбрать направление решения. Runbook описывает конкретные шаги выполнения и эскалации в реальном инциденте.

</details>

### Архитектурная карта контуров (единая ментальная модель)

```mermaid
flowchart TB
    subgraph ControlPlane[Control Plane]
        CP1[Policies]
        CP2[Runbooks]
        CP3[Support Matrix]
    end

    subgraph DataPlane[Data Plane]
        D1[Standard Queues]
        D2[GPU Queues]
        D3[Ad-hoc Queues]
        D4[Region Queues]
        D5[Bridge Path]
    end

    subgraph Runtime[Execution Runtime]
        R1[Linux Production Workers]
        R2[Windows/Edge Workers]
        R3[GPU Nodes]
    end

    CP1 --> D1
    CP1 --> D2
    CP1 --> D3
    CP1 --> D4
    CP2 --> Runtime
    CP3 --> Runtime

    D1 --> R1
    D2 --> R3
    D3 --> R1
    D4 --> R1
    D5 --> R1
```

**Как читать эту схему:**  
Control Plane определяет правила и ответственность; Data Plane переносит задачи; Runtime исполняет их в конкретной среде. Большинство инцидентов части 32 — это рассинхронизация между этими тремя слоями.

---
