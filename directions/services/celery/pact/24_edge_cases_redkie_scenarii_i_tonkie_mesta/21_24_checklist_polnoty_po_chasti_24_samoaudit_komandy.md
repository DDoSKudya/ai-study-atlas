[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Checklist полноты по части 24 (самоаудит команды)

Используйте перед крупными релизами и после инцидентов:

- [ ] Для long-running задач есть checkpoints и сценарии graceful shutdown.
- [ ] Для больших payload действует pointer-подход с TTL/checksum/cleanup.
- [ ] Для апгрейдов есть compatibility matrix и replay legacy сообщений.
- [ ] Для расписаний зафиксированы DST/UTC правила.
- [ ] Для внешних зависимостей готовы backoff+jitter+circuit breaker+disable path.
- [ ] Для producer/consumer консистентности есть outbox (или эквивалентная гарантия).
- [ ] Для hybrid маршрутов есть latency budget и failover drills.
- [ ] Для контейнеров есть memory budget и мониторинг node pressure.
- [ ] Для времени есть мониторинг clock skew и runbook при drift.

#### Проверь себя: checklist

1. Как использовать checklist так, чтобы он не стал «галочками ради отчета»?

<details><summary>Ответ</summary>

Каждый пункт должен быть связан с конкретным артефактом: тестом, дашбордом, runbook, владельцем и проверяемым процессом. Если артефакта нет, пункт фактически не закрыт.

</details>

2. Почему checklist нужно проходить и перед релизом, и после инцидента?

<details><summary>Ответ</summary>

Перед релизом он предотвращает занос новых рисков, а после инцидента фиксирует постоянные улучшения, чтобы сценарий не повторился.

</details>

---
