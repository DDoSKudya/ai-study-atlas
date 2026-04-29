[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Карта соответствия глобальному плану

| Пункт плана | Где раскрыто |
|---|---|
| `37.1` Глобальные флаги приложения | [37.1](#371-глобальные-флаги-приложения) |
| `37.2` `celery worker` | [37.2](#372-celery-worker) |
| `37.3` `celery beat`, `celery events` | [37.3](#373-celery-beat-и-celery-events) |
| `37.4` Операционные подкоманды | [37.4](#374-операционные-подкоманды) |
| `37.5` Переменные окружения | [37.5](#375-переменные-окружения) |
| `37.6` Интеграция с process managers | [37.6](#376-интеграция-с-process-managers) |

### Контрольный список покрытия подпунктов 37.x

Этот блок нужен как "инвентаризация без слепых зон": можно быстро проверить, что в части действительно раскрыты все ключевые элементы из плана, а не только общие идеи.

| Подпункт | Что именно должно быть покрыто | Где в этой части |
|---|---|---|
| `37.1` Глобальные флаги | `-A/--app`, `--config`, `--workdir`, `--quiet`, `--no-color`, `--version`, `--skip-checks` (по версии) | [37.1](#371-глобальные-флаги-приложения) |
| `37.2` Worker: база | pool, concurrency, hostname (`-n`), queues/exclude-queues, prefetch | [37.2](#372-celery-worker) |
| `37.2` Worker: лимиты и ресурсный контур | hard/soft time limits, `max-tasks-per-child`, `max-memory-per-child`, optimization profile, autoscale | [37.2](#372-celery-worker) |
| `37.2` Worker: эксплуатация и безопасность | detach, uid/gid, umask, executable, SSL/TLS, `without gossip/mingle/heartbeat`, statedb/pid/log | [37.2](#372-celery-worker) |
| `37.3` Beat | scheduler class, schedule file, pid/log, max interval и loop-поведение | [37.3](#373-celery-beat-и-celery-events) |
| `37.3` Events | `events`, `dump`, `camera`, безопасность и стоимость event-потока | [37.3](#373-celery-beat-и-celery-events) |
| `37.4` Inspect | перечень ключевых подкоманд + аргументы `timeout`, `destination`, `json` (по версии) | [37.4](#374-операционные-подкоманды) |
| `37.4` Control и смежные команды | `control` (rate/time/pool/consumer/events), `purge`, `list bindings`, `call`, `graph`, `upgrade`, `shell`, `report`, `result`, `migrate`, `multi` | [37.4](#374-операционные-подкоманды) |
| `37.5` Env | `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND`, `CELERY_CONFIG_MODULE`, `CELERY_TIMEZONE`, паттерн `CELERY_*`, приоритеты над конфигом | [37.5](#375-переменные-окружения) |
| `37.6` Process managers | systemd (`ExecStart`, `KillSignal`, `TimeoutStopSec`, restart), supervisord/circus, минимальные чек-листы | [37.6](#376-интеграция-с-process-managers) |

#### Проверь себя: контрольный список покрытия

1. Зачем в большой учебной части нужен отдельный checklist покрытия, если уже есть оглавление?

<details><summary>Ответ</summary>

Оглавление показывает структуру чтения, а checklist — полноту соответствия плану. Он помогает быстро поймать пропуски при обновлениях и ревью.

</details>

2. Почему в таблице отмечены пометки "по версии"?

<details><summary>Ответ</summary>

Потому что часть CLI-флагов и форматов вывода может отличаться между версиями Celery. Это напоминание не копировать команды слепо, а проверять на целевой версии.

</details>

---
