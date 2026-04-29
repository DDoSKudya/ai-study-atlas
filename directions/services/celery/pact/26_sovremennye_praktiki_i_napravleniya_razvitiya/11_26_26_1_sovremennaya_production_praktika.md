[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## 26.1 Современная production-практика

### Цель раздела

Понять, как выглядит современный operational baseline для Celery: IaC, контейнеризация, autoscaling, единая телеметрия и безопасная работа с секретами.

### В этом разделе главное

- production-практика должна быть воспроизводимой, а не "ручной";
- autoscaling без политики качества может ускорить деградацию;
- секреты и конфиги должны управляться централизованно и безопасно;
- логирование/метрики/трейсы должны проектироваться как единая система.

### Термины

| Термин | Формально | Простыми словами |
|---|---|---|
| **IaC** | Декларативное управление инфраструктурой в коде | Все настройки среды живут в Git |
| **Immutable container** | Непересобираемый в рантайме образ | Один образ — одинаковое поведение |
| **KEDA/HPA autoscaling** | Автомасштабирование по метрикам нагрузки | Кластер сам добавляет/убирает воркеры |
| **Secret management** | Управление чувствительными данными | Пароли и ключи не хранятся "в явном виде" |
| **Central telemetry** | Единый сбор логов/метрик/трейсов | Полная картина по системе в одном месте |

### Теория и правила

1. **Everything as code.**  
   Очереди, deploy, scaling policy и observability-конфиг должны быть ревьюируемыми и версионируемыми.

2. **Container-first execution.**  
   Worker должен запускаться в предсказуемом контейнере с фиксированными зависимостями.

3. **Autoscaling c guardrails.**  
   Масштабируемся по queue lag и throughput, но с ограничителями (max replicas, cooldown, rate limits).

4. **Telemetry by default.**  
   Каждый worker/pool/queue должен иметь обязательные метрики и structured logs.

5. **Secret zero trust.**  
   Никаких токенов/паролей в образах и переменных "на вечность"; нужны rotation и минимальные права.

### Пошагово: базовая modern-ready настройка

1. Описать infra Celery в IaC (namespace, broker endpoints, deployment, autoscaler).
2. Собирать immutable-образ с фиксированными зависимостями.
3. Настроить KEDA/HPA по `queue_length`, `processing_latency`.
4. Подключить централизованный сбор логов/метрик/трейсов.
5. Вынести секреты в Vault/KMS/secret-manager и настроить rotation.
6. Зафиксировать SLO/алерты до включения autoscaling в production.

### Пример: KEDA `ScaledObject` для очереди Celery

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: celery-critical-scaler
spec:
  scaleTargetRef:
    name: celery-critical-workers
  pollingInterval: 15
  cooldownPeriod: 120
  minReplicaCount: 2
  maxReplicaCount: 30
  triggers:
    - type: rabbitmq
      metadata:
        protocol: amqp
        queueName: critical_tasks
        mode: QueueLength
        value: "50"
        hostFromEnv: RABBITMQ_CONN_STR
```

Что важно в этом примере:
- `minReplicaCount` защищает от cold-start деградации в критичной очереди;
- `cooldownPeriod` предотвращает "пиление" масштаба вверх-вниз;
- scaling-метрика соответствует конкретной очереди, а не среднему по всем потокам.

### Мини-чеклист production-ready для `26.1`

- есть ли IaC-описание worker deployment, autoscaler и broker-коннектов;
- есть ли ограничения масштаба (`min/max replicas`, cooldown);
- есть ли политика секретов (источник, ротация, аудит доступа);
- есть ли единый формат structured-логов;
- есть ли fallback-режим при деградации внешних API.

### Пример безопасной секретной конфигурации (паттерн)

```text
Нельзя:
- хранить broker URL с паролем в .env внутри образа;
- передавать секреты как "вечные" переменные без ротации;
- давать всем worker-ам одинаковые максимальные права.

Нужно:
- получать секреты из Secret Manager/Vault при старте pod;
- использовать short-lived credentials или регулярную ротацию;
- ограничивать доступ по принципу least privilege.
```

### ASCII-схема современного production-контура

```text
Git (IaC + app config)
   -> CI/CD builds container
   -> Deploy to K8s
   -> KEDA/HPA scales workers by queue metrics
   -> OTel exports traces/metrics/logs
   -> Alerting reacts to SLO burn
```

### Практика / реальные сценарии

- **Сценарий "пиковые продажи":** KEDA масштабирует только `critical` worker deployment, а не весь пул.
- **Сценарий "секреты обновились":** rolling restart подов берет новые credentials без ручного вмешательства.
- **Сценарий "новая очередь":** IaC-патч + ревью + release pipeline вместо ручных действий в проде.

### Граничные случаи

- **Слишком агрессивный autoscaling:** backlog падает, но внешние API уходят в `429/5xx`, и общая доступность ухудшается.
- **Слишком консервативный autoscaling:** система выглядит стабильной, но queue lag системно нарушает SLO.
- **Секреты меняются, но воркеры не перечитывают конфиг:** часть подов работает с просроченными credential и дает "плавающие" ошибки.

### Типичные ошибки

- включать autoscaling без верхней границы и cooldown;
- хранить broker credentials в plain env-файлах;
- считать, что только метрики достаточно, игнорируя трассировку;
- поддерживать "ручной" production-изменяемый state.

### Что будет, если...

Если оставить Celery на "полуручном" уровне:
- релизы станут непредсказуемыми;
- инциденты будут расследоваться дольше;
- autoscaling начнет усиливать проблемы вместо их решения;
- безопасность конфигурации станет слабым местом.

### Проверь себя

1. Почему autoscaling без ограничителей может ухудшить ситуацию при падении внешнего API?

<details><summary>Ответ</summary>

Потому что рост реплик увеличит число одновременных попыток к уже деградировавшей зависимости, усилив retry storm и сжигая ресурсы кластера.

</details>

2. Зачем IaC в Celery-контуре, если "и так можно задеплоить вручную"?

<details><summary>Ответ</summary>

IaC дает повторяемость, аудит изменений, peer review и безопасный rollback. Ручной деплой в сложных асинхронных системах повышает риск скрытых конфигурационных расхождений.

</details>

3. Что является минимальным security baseline для секретов?

<details><summary>Ответ</summary>

Централизованное хранение, ротация, принцип минимальных привилегий и отсутствие секретов в образах/репозитории.

</details>

### Запомните

Современная production-практика Celery — это platform engineering, а не просто запуск воркера с правильной командой.

---
