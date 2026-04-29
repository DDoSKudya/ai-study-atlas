[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Справочник по части

| Подтема | Ключевая идея | Практический ориентир |
|---|---|---|
| `26.1` Modern production | Platform-first: IaC, autoscaling, secrets, telemetry | все изменения через код и controlled rollout |
| `26.2` Observability | OTel + correlation + SLO + burn-rate | измеряй путь `HTTP -> task -> dependency` |
| `26.3` Broker evolution | quorum/HA/restart resilience/managed trade-offs | регулярно тестируй failover и recovery |
| `26.4` Kubernetes | pod lifecycle, probes, scaling per queue | разделяй worker deployment-ы по SLA и нагрузке |
| `26.5` Hybrid | Celery как execution layer в смешанных схемах | четко фиксируй границы инструментов |
| `26.6` Learning path | развитие через reliability/SRE/workflow/event patterns | строй roadmap на месяцы, а не "читай хаотично" |

#### Проверь себя: справочник

1. Как использовать справочник в момент инцидента, когда времени мало?

<details><summary>Ответ</summary>

Определить тип симптома, перейти к соответствующему подпункту и применить его runbook/чеклисты вместо хаотичного перебора гипотез.

</details>

2. Почему справочник не заменяет основной текст части?

<details><summary>Ответ</summary>

Справочник дает сжатую карту, но не содержит всей глубины: обоснований, ограничений, граничных случаев и детальных шагов внедрения.

</details>

---
