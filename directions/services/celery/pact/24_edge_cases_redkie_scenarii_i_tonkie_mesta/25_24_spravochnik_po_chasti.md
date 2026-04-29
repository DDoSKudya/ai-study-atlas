[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Справочник по части

| Подтема | Ключевая идея | Практический ориентир |
|---|---|---|
| `24.1` Long-running tasks | Живость не равна прогрессу | checkpoints + graceful shutdown |
| `24.2` Большие payload | Broker не storage | передавать ссылки, не мегабайты |
| `24.3` Версионность | Upgrade = совместимость | matrix + canary + legacy test |
| `24.4` Timezone/DST | Локальное время коварно | UTC-first + DST policy |
| `24.5` Retry storm | Retry может усилить инцидент | backoff+jitter+circuit breaker |
| `24.6` Producer/consumer race | publish-before-commit ломает корректность | transactional outbox |
| `24.7` Hybrid | Сеть и топология меняют семантику | topology-aware routing |
| `24.8` OOM/cgroups | Контейнер убивает внезапно | memory budget + queue isolation |
| `24.9` Clock sync | Время — зависимость системы | NTP discipline + skew alerting |

---
