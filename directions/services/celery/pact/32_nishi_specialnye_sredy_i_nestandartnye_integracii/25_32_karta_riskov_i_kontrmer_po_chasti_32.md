[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Карта рисков и контрмер (по части 32)

| Риск | Где проявляется | Ранний сигнал | Контрмера |
|---|---|---|---|
| Перегрузка GPU-пула | `32.1` | рост `queue_wait_p95`, OOM всплески | лимиты конкуренции, раздельные очереди, warm-pool политика |
| Невоспроизводимый ad-hoc запуск | `32.2` | нет `git_sha`/`ticket_id` в метаданных | обязательные headers, sandbox-first, запрет боевого запуска без ticket |
| Split-brain | `32.3` | регионы одновременно считают себя primary | single-writer policy, runbook активации, дедупликация и reconciliation |
| Потеря семантики через bridge | `32.4` | workflow нестабилен при "рабочем" basic task | parity-тесты, adapter contract, фиксация ограничений в SLA/runbook |
| Platform drift | `32.5` | баги только на одной ОС, не ловятся CI | support matrix, целевые smoke-тесты, запрет platform-specific hacks в бизнес-коде |

---
