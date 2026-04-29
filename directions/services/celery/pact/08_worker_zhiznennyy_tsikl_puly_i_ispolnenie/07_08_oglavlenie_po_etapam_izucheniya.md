[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Оглавление по этапам изучения

### Этап 1. Жизненный цикл worker

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [8.1. Жизненный цикл worker](#81-жизненный-цикл-worker) | Старт, bootsteps, подключение к broker, consumer loop, graceful shutdown | bootsteps, warm/cold shutdown, signals |

### Этап 2. Concurrency-модели

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [8.2. Concurrency модели](#82-concurrency-модели) | Сравнение `prefork`, `threads`, `gevent`, `eventlet`, `solo` | GIL, CPU-bound, I/O-bound, cooperative concurrency |

### Этап 3. Prefork углубленно

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [8.3. Prefork подробно](#83-prefork-подробно) | Fork-семантика, память, соединения после fork, re-init | copy-on-write, fork safety, child recycling |

### Этап 4. Управление ресурсами

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [8.4. Управление ресурсами worker](#84-управление-ресурсами-worker) | `--concurrency`, `autoscale`, лимиты child-процессов, saturation | max tasks/memory per child, autoscale, queue isolation |

### Этап 5. Prefetch и справедливость

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [8.5. Prefetch и fairness](#85-prefetch-и-fairness) | Как prefetch влияет на latency, throughput и redelivery | QoS, throughput vs responsiveness |

### Этап 6. Ack и потеря worker

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [8.6. Ack-семантика и потеря worker](#86-ack-семантика-и-потеря-worker) | `acks_late`, `task_reject_on_worker_lost`, поведение при `kill -9` | at-least-once, duplicates, worker lost |

### Этап 7. Управление worker-ами в реальной системе

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [8.7. Управление worker-ами в реальной системе](#87-управление-worker-ами-в-реальной-системе) | выделенные worker-ы, queue affinity, canary, blue/green | workload isolation, safe rollout |

---
