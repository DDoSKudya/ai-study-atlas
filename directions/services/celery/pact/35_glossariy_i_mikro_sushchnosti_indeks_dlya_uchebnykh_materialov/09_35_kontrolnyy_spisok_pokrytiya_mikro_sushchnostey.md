[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Контрольный список покрытия микро-сущностей

Ниже — техническая "контрольная матрица", чтобы быстро увидеть: все ли термины из части `35` действительно раскрыты.

| Группа | Обязательные микро-сущности | Статус в этом файле |
|---|---|---|
| `35.1` Приложение и задачи | `Celery`, `app`, `current_app`, `shared_task`, `main`, `@app.task` опции, `Task`, `Request`, `Context`, `AsyncResult`, `EagerResult`, `ResultSet`, `GroupResult`, `Signature`, `s/si/clone/set/link/link_error`, id-поля, `headers/reply_to/delivery_mode/priority` | раскрыто в [35.1](#351-приложение-и-задачи) + [35.6](#356-результаты-и-бэкенды) |
| `35.2` Брокер и транспорт | `Connection`, `Channel`, `Producer`, `Consumer`, `Queue`, `Exchange`, `binding`, `transport`, `transport_options`, `confirm_publish`, `ssl`, durable/exclusive/auto-delete/TTL/DLX/DLQ | раскрыто в [35.2](#352-брокер-и-транспорт-kombu-уровень) |
| `35.3` Worker и исполнение | `Worker`, `Consumer`, `Bootstep`, `Timer`, `Hub`, `Pool`, `state`, пулы (`prefork/solo/threads/gevent/eventlet/custom`), команды `inspect`, команды `control` | раскрыто в [35.3](#353-worker-и-исполнение) |
| `35.4` Canvas | `chain`, `group`, `chord`, `chunks`, `map`, `starmap`, `upgrade`, `partial`, `maybe_signature`, `maybe_unroll_group`, `unlock/header/callback` | раскрыто в [35.4](#354-canvas-и-оркестрация) |
| `35.5` Beat | `beat_schedule`, `crontab`, `schedule`, `solar`, `interval`, `beat_scheduler`, `DatabaseScheduler`, `PersistentScheduler`, `celerybeat-schedule`, `beat_schedule_filename` | раскрыто в [35.5](#355-beat-и-расписание) |
| `35.6` Результаты | ключи backend, `result_extended`, `date_done`, `traceback`, `children`, групповые результаты и порядок | раскрыто в [35.6](#356-результаты-и-бэкенды) |
| `35.7` Безопасность | `json`, `pickle`, `yaml`, `msgpack`, `accept_content`, whitelist | раскрыто в [35.7](#357-сериализация-и-безопасность) |

#### Проверь себя: контрольный список покрытия

1. Зачем нужна матрица покрытия, если есть подробное оглавление?

<details><summary>Ответ</summary>

Оглавление показывает порядок изучения, а матрица — фактическую полноту терминов. Она быстрее обнаруживает пропуски после правок.

</details>

2. Как применять этот блок при обновлении версии Celery?

<details><summary>Ответ</summary>

Сверять, что обязательные микро-сущности не исчезли и не "размазались" по тексту без явного раскрытия, а ссылки на разделы остаются рабочими.

</details>

---
