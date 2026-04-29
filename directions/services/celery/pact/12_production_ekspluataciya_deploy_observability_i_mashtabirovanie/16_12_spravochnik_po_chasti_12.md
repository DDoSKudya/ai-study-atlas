[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Справочник по части 12

| Тема | Ключевые пункты |
|---|---|
| **Deployment** | разделяй роли, планируй stateful компоненты, учитывай platform-реальность (OOM/SIGKILL) |
| **Rolling update** | in-queue совместимость + in-flight завершение, деплой партиями, throughput падает во время drain |
| **Graceful shutdown** | SIGTERM ≠ гарантия, нужны корректные grace periods и дизайн задач |
| **Observability** | lag важнее depth, корреляция обязательна, Flower — UI, не система наблюдаемости |
| **Инциденты** | triage: broker → lag → throughput → errors, runbooks + алерты |
| **Autoscaling** | скейлим по lag/SLO, cooldown и анти-thrashing, защищаем внешние зависимости |
| **DR и совместимость** | очередь длиннее деплоя, phased rollout, идемпотентность = основа recovery |

---
