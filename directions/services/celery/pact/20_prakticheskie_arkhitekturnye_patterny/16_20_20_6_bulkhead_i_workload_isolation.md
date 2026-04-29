[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## 20.6 Bulkhead и workload isolation

### Цель раздела

Понять, как изолировать разные классы нагрузки в Celery, чтобы перегрузка одной очереди не уничтожала весь фоновый контур.

### В этом разделе главное

- критичные и некритичные задачи должны иметь разные очереди и worker-пулы;
- ресурсные квоты и приоритеты нужны не "для красоты", а для защиты SLA;
- isolation надо проектировать вместе с мониторингом и capacity planning.

### Термины

| Термин | Определение |
|---|---|
| **Critical lane** | Контур задач с высоким бизнес-приоритетом и жестким SLA. |
| **Best-effort lane** | Контур вторичных задач, допускающих задержку. |
| **Quota** | Ограничение ресурса (concurrency, rate, queue depth budget) для домена/команды. |

### Теория и правила

Bulkhead — аналог водонепроницаемых отсеков в корабле: если один отсек затоплен, корабль не тонет целиком.

В Celery это реализуется через:

- отдельные очереди;
- отдельные worker-ы или worker-пулы;
- разные политики retry, prefetch и rate limits;
- при необходимости — разные брокеры/виртуальные хосты.

Подпункт плана **quota per team/domain** обычно реализуют минимум в трех уровнях:

1. лимит `concurrency` на отдельные worker-пулы;
2. rate limit на типы задач (`task_annotations` / policy layer);
3. лимиты запуска batch-кампаний через platform API (governance-контур).

#### ASCII-схема

```text
                     +------------------+
Critical API events -> queue.critical   -> workers.critical (reserved capacity)
                     +------------------+

                     +------------------+
Analytics batch ----> queue.analytics   -> workers.analytics (elastic/best effort)
                     +------------------+
```

### Пошагово

1. Раздели workload по критичности и профилю ресурса (CPU/I/O).
2. Назначь отдельные очереди и task routes.
3. Выдели worker-ы с изолированными лимитами.
4. Настрой отдельные alert thresholds.
5. Регулярно проверяй, что "вторичный" контур не перетекает в critical lane.

### Пример квотной матрицы

| Домен | Очередь | Worker pool | Квота |
|---|---|---|---|
| Billing | `critical.billing` | `workers-billing` | min 10 concurrency, приоритет высокий |
| Product notifications | `best_effort.notifications` | `workers-notify` | max 30 rps, допустима задержка |
| Analytics | `batch.analytics` | `workers-analytics` | запуск по расписанию, ограниченный window |

### Как запомнить

Изоляция настоящая только тогда, когда разделены **и очередь, и ресурсы, и алерты**.

### Пример маршрутизации

```python
task_routes = {
    "billing.tasks.*": {"queue": "critical.billing"},
    "notifications.tasks.*": {"queue": "best_effort.notifications"},
    "analytics.tasks.*": {"queue": "batch.analytics"},
}
```

### Пример запуска worker-пулов под изоляцию

```bash
celery -A proj worker -n billing@%h -Q critical.billing --concurrency=10 --prefetch-multiplier=1
celery -A proj worker -n notify@%h -Q best_effort.notifications --concurrency=6
celery -A proj worker -n analytics@%h -Q batch.analytics --concurrency=4
```

### Практика / реальные сценарии

- защита платежного контура от всплеска маркетинговых рассылок;
- изоляция тяжелого ML batch от пользовательских job API;
- квоты по командам в multi-team платформе.

### Типичные ошибки

- "одна очередь на все" в надежде на fair scheduling;
- отсутствуют квоты, одна команда может "съесть" весь кластер;
- нет отдельного дашборда по critical lane.

### Что будет, если...

- **...нет bulkhead, а аналитика внезапно запустила огромный батч?**  
  Критичные задачи начнут ждать в общей очереди, SLA пользовательских операций будет сорван.

- **...очереди разделили, но worker-ы все равно слушают все очереди?**  
  Формальная изоляция есть, фактической нет: contention останется.

- **...нет domain quota и одна команда запускает "тяжелый эксперимент"?**  
  Остальные команды теряют ресурс, а платформа превращается в "кто первый захватил capacity".

### Проверь себя

1. Почему разделение только по queue без разделения capacity часто недостаточно?

<details><summary>Ответ</summary>

Потому что если одни и те же worker-ы конкурируют за все очереди, тяжелые задачи все равно могут вытеснить критичные по ресурсам CPU/RAM/IO.

</details>

2. Какой минимальный набор для работающего bulkhead-подхода?

<details><summary>Ответ</summary>

Отдельные очереди, отдельные worker-capacity профили и отдельные метрики/алерты по каждому lane.

</details>

### Запомните

Bulkhead — основной инструмент управления blast radius в Celery-архитектуре.

---
