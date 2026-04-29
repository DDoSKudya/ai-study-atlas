[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Базовые конфигурационные профили (готовые стартовые шаблоны)

Этот блок нужен, чтобы перейти от "теоретически понимаю" к "могу быстро стартовать без грубых ошибок".

### Профиль A: Надежный универсальный baseline (большинство backend-команд)

**Когда применять:** обычные веб-бэкенды с фоновыми задачами, умеренная нагрузка, высокий приоритет предсказуемости.

```python
# serializer/security baseline
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]

# delivery/reliability baseline
task_acks_late = True
task_reject_on_worker_lost = True
task_publish_retry = True
task_publish_retry_policy = {"max_retries": 5, "interval_start": 0, "interval_step": 0.5, "interval_max": 5}

# limits
task_soft_time_limit = 270
task_time_limit = 300

# worker
worker_pool = "prefork"
worker_concurrency = 4
worker_prefetch_multiplier = 1
worker_max_tasks_per_child = 1000

# observability
worker_send_task_events = True
task_send_sent_event = True

# result backend
result_expires = 86400
result_backend_always_retry = True
```

### Профиль B: I/O-heavy интеграции (много внешних API)

**Когда применять:** сервисы-оркестраторы интеграций, где главная боль — rate limit и нестабильные внешние системы.

- ниже `worker_prefetch_multiplier` (часто `1`) для fairness;
- обязательный `task_default_rate_limit` и per-task overrides через `task_annotations`;
- более мягкие retry с jitter/backoff;
- строгая маршрутизация в отдельные очереди интеграций.

### Профиль C: Batch/throughput контур

**Когда применять:** массовая обработка, где допустима задержка, но важна стоимость и устойчивость при длинных очередях.

- отдельные `bulk`-очереди и worker-пулы;
- повышенный контроль памяти (`worker_max_memory_per_child`);
- ограниченные события (только нужные для SLO);
- агрессивный `result_expires` и `task_ignore_result=True` для промежуточных шагов.

### Что проверить перед выбором профиля

1. Тип задач: CPU, I/O, mixed.
2. Требование к latency (p95/p99) и к стоимости.
3. Критичность дублей и наличие идемпотентности.
4. Наличие/отсутствие chord/group зависимостей.

#### Проверь себя: выбор профиля

1. Почему наличие chord/group меняет требования к result policy?
2. Как cost-ограничения влияют на выбор между `result_expires` и `task_ignore_result`?

<details><summary>Ответ</summary>

1) Потому что fan-in сценарии завязаны на корректное и своевременное хранение результатов.  
2) Эти параметры напрямую управляют объемом хранения и частотой операций с backend.

</details>

---
