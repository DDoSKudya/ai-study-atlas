[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Типичные ошибки по части

- treating Celery как "черный ящик", а не как pipeline из слоев;
- отсутствие версионирования payload-контрактов;
- неоправданно высокий prefetch без учета SLA и fairness;
- использование signals для критичной доменной логики;
- доверие inspect/control как "абсолютной правде";
- запуск chord без проверки backend поведения под нагрузкой;
- отсутствие формализованного internal runbook после инцидентов.
- изменение сразу многих "рычагов" (`prefetch`, `acks_late`, `concurrency`) без контрольного эксперимента;
- недооценка влияния clock drift на `eta/expires` и планировочную логику.
- попытка применять одинаковые control/debug практики без поправки на конкретный transport.
- смешение ролей `signals`, `retries` и `canvas callbacks`, из-за чего оркестрация становится неявной.

---

### Симптом -> первопричина -> первое действие

| Симптом | Частая первопричина | Первое практическое действие |
|---|---|---|
| `Received` есть, `started` нет | Saturation/блокировка execution pool | Проверить `inspect active/reserved/stats`, загрузку CPU/RAM и блокирующие I/O |
| `SUCCESS` в worker-логах, но клиент видит `PENDING` | Проблемы result backend/TTL | Проверить backend latency/errors и `result_expires` |
| Chord callback не запускается | Проблемы агрегации/TTL/policy в backend | Проверить group state, unlock retries, сроки хранения результатов |
| Inspect отвечает не всем worker-ам | Control-plane latency/network/transport нюансы | Повторить с timeout+, сверить сетевой доступ и broker control path |
| После релиза `unregistered task` | Несовместимые версии registry/имени задач | Откатиться на совместимый alias и провести phased rollout |

---
