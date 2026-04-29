[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Чеклист production-ready перед релизом

Используй как короткий gate перед выкладкой новой версии worker-ов/producer-ов.

- **Совместимость сообщений:** новая версия читает старые payload/имена задач (dual-read при необходимости).
- **Rollout-план:** есть canary, rollback и понятное graceful окно.
- **Наблюдаемость:** метрики/алерты для lag, retries, failures, heartbeat включены и проверены.
- **Runbook-пакет:** актуальны сценарии broker/backend outage, stuck workers, backlog, scheduler duplication.
- **DR-готовность:** известны критичные очереди, есть replay-процедура и проверенный recovery drill.
- **Ограничители:** autoscaling guardrails и лимиты downstream-зависимостей зафиксированы.

Если хотя бы один пункт не выполнен, релиз лучше считать повышенным риском и заранее усилить мониторинг/дежурство.

---
