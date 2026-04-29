[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Операционный мини-runbook (часть 19)

Ниже короткий диагностический маршрут для инцидента "задача не доходит/не исполняется":

1. Проверить API-лог публикации: сформирован ли `task_id`, какой `queue`, какой `correlation_id`.
2. Проверить broker: есть ли сообщение в очереди, не истек ли `expires`, нет ли TTL-удаления.
3. Проверить worker startup: слушает ли правильные очереди (`-Q`), нет ли crash-loop.
4. Проверить сериализацию: совместим ли payload по `contract_version`.
5. Проверить task retries: нет ли бесконечного цикла или poison payload.
6. Проверить статусную модель: обновляется ли `queued -> running -> success/failure`.
7. Проверить алерты и метрики: backlog, error rate, latency p95/p99, retry rate.

Мини-правило: расследование всегда идет по цепочке  
`request -> publish -> broker -> consume -> side effect -> status`.

### Быстрая таблица "симптом -> проверка -> действие"

| Симптом | Первая проверка | Действие |
|---|---|---|
| Клиент получил `202`, но статус вечно `queued` | Слушает ли worker нужную очередь | Исправить `-Q`/routing, проверить деплой worker |
| Много `failure` сразу после релиза | Совместимость `contract_version` | Включить backward-compatible ветку, откатить несовместимый payload |
| Резкий рост retry | Класс ошибок transient или permanent | Разделить retry-policy, quarantine для permanent |
| Дубли побочного эффекта | Есть ли idempotency key и доменная защита | Внедрить dedup/idempotent handlers |
| Нельзя связать инцидент между API и worker | Есть ли единый correlation id | Протянуть id в headers и structured logs |

### Чеклист "готово к production" для части 19

- есть единый publish layer и запрещён прямой `.delay()` в endpoint-ах;
- у payload есть `contract_version`, есть политика backward compatibility;
- correlation id проходит через API, broker headers и worker-логи;
- есть тесты failure path (broker down/queue misroute);
- есть integration smoke контур с реальным broker;
- есть idempotency стратегия для критичных side effects;
- есть операционная диагностика по цепочке `request -> publish -> consume`.

### Карта рисков и контрмер

| Риск | Как проявляется | Контрмера |
|---|---|---|
| Потеря публикации | API ответил успехом, но задачи нет в очереди | Явный publish error handling, outbox для критичных сценариев |
| Несовместимый payload | Всплеск падений после релиза | `contract_version`, backward-compatible обработка, контрактные тесты |
| Retry storm | Рост нагрузки и повторов без прогресса | Ограниченные retry, backoff/jitter, quarantine permanent ошибок |
| Дубли side effects | Повторные списания/уведомления | Idempotency key + доменная дедупликация |
| Непрозрачная диагностика | Нельзя быстро собрать цепочку инцидента | Единый correlation id и structured logs в API/worker |

#### Проверь себя по runbook и рискам

1. Какой риск карта помогает предотвратить в первую очередь: технический или организационный?

<details><summary>Ответ</summary>

Оба. Технически — снижает вероятность сбоев (retry storm, несовместимость), организационно — ускоряет совместную диагностику и делает реакцию команды предсказуемой.

</details>

2. Почему runbook должен идти по цепочке `request -> publish -> broker -> consume -> status`, а не "с конца"?

<details><summary>Ответ</summary>

Это минимизирует время поиска причины: шаги идут по реальному пути данных и быстро локализуют точку сбоя без хаотичных проверок.

</details>

---
