[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Карта соответствия глобальному плану

| Пункт плана | Где раскрыто |
|---|---|
| `38.1` Сигналы Celery | [38.1](#381-сигналы-celery) |
| `38.2` События (event protocol) | [38.2](#382-события-event-protocol) |
| `38.3` Bootsteps и кастомизация worker | [38.3](#383-bootsteps-и-кастомизация-worker) |
| `38.4` Другие hooks | [38.4](#384-другие-hooks) |

### Контрольный список покрытия подпунктов 38.x

| Подпункт | Что именно покрыто | Где в части |
|---|---|---|
| `38.1` publish signals | `before_task_publish`, `after_task_publish`, типичные поля и риски | [38.1](#381-сигналы-celery) |
| `38.1` task lifecycle signals | `task_prerun`, `task_postrun`, `task_success`, `task_failure`, `task_retry`, `task_revoked` | [38.1](#381-сигналы-celery) |
| `38.1` receive/reject/unknown | `task_received`, `task_rejected`, `task_unknown` | [38.1](#381-сигналы-celery) |
| `38.1` worker/process lifecycle | `worker_init`, `worker_ready`, `worker_shutdown`, `worker_process_init`, `worker_process_shutdown`, `heartbeat_sent`, `setup_logging`, `celeryd_after_setup` | [38.1](#381-сигналы-celery) |
| `38.2` event protocol | worker/task event types, включение событий, совместимость с Flower/monitoring | [38.2](#382-события-event-protocol) |
| `38.2` стоимость и sampling | нагрузка, фильтрация, sampling-подходы при high load | [38.2](#382-события-event-protocol) |
| `38.3` bootsteps chain | идея chain, порядок и зависимости инициализации | [38.3](#383-bootsteps-и-кастомизация-worker) |
| `38.3` custom consumer steps | безопасная кастомизация consumer-контура | [38.3](#383-bootsteps-и-кастомизация-worker) |
| `38.4` task annotations | `task_annotations` как функция и policy-слой | [38.4](#384-другие-hooks) |
| `38.4` custom Task class | `__call__`, `before_start`, `on_success`, `on_failure`, `on_retry`, `after_return` | [38.4](#384-другие-hooks) |
| `38.4` custom serializer/backend/loader | когда применять, риски совместимости и тестирование | [38.4](#384-другие-hooks) |

#### Проверь себя: полнота покрытия плана

1. Зачем в учебной части держать отдельный checklist покрытия подпунктов, если уже есть оглавление?
2. Что делать, если подпункт вроде «упомянут», но без практического сценария и ограничений?

<details><summary>Ответ</summary>

1) Оглавление показывает маршрут, а checklist — полноту и проверяемость соответствия master-плану.  
2) Считать подпункт неполным и дополнять: теория, ограничения, примеры, ошибки и применение.

</details>

---
