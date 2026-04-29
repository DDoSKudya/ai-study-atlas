[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Частая путаница (и как не ошибаться)

| Путают | Правильное различие | Практический критерий |
|---|---|---|
| **Autoscaling** vs **устойчивость** | Autoscaling добавляет ресурсы, но не гарантирует корректность retries/idempotency | если растут дубли/ошибки, дело не только в масштабе |
| **Liveness** vs **Readiness** | Liveness: "жив ли процесс"; Readiness: "готов ли брать задачи" | под может быть жив, но не ready |
| **Event** vs **Task command** | Event описывает факт, command требует действие | event хранится и может replay; command должен быть исполнен |
| **Metrics** vs **Observability** | Метрики — часть картины; observability = метрики + логи + traces + контекст | можно ли восстановить цепочку причины по одному инциденту |
| **Broker HA** vs **end-to-end reliability** | HA брокера не отменяет бизнес-идемпотентность и outbox-контракты | при failover не должно быть неконтролируемых повторов |
| **Roadmap чтения** vs **roadmap внедрения** | Прочитать тему и внедрить практику — разные вещи | есть ли артефакт (runbook, dashboard, RFC, drill report) |

### Как запомнить

```text
Scale != Reliability
Alive != Ready
Event != Command
Metrics != Observability
HA Broker != End-to-end correctness
Read != Implemented
```

#### Проверь себя: частая путаница

1. Как на практике проверить, что команда не путает `Alive` и `Ready` в Kubernetes-контуре Celery?

<details><summary>Ответ</summary>

Нужно отдельно валидировать liveness и readiness в сценариях деградации: процесс может быть жив, но readiness обязана стать false, если worker не может безопасно брать задачи.

</details>

2. Почему формула `Metrics != Observability` критична именно для части 26?

<details><summary>Ответ</summary>

Потому что часть 26 про современную эксплуатацию: без трассировки и контекста метрики не дают причинности, а значит не позволяют быстро и корректно устранять инциденты.

</details>

---
