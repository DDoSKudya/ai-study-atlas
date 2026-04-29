[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Вопросы для самопроверки по части 19

1. В чем ключевое архитектурное отличие FastAPI `BackgroundTasks` от Celery worker-а?

<details><summary>Ответ</summary>

`BackgroundTasks` локальны процессу API и не дают распределенную очередь/масштабирование/устойчивую доставку. Celery — отдельная распределенная подсистема с broker-ом и worker-ами.

</details>

2. Зачем выделять publish layer между endpoint-ами и Celery API?

<details><summary>Ответ</summary>

Чтобы централизовать правила публикации: payload schema, versioning, headers, queue routing, аудит и обработку ошибок публикации.

</details>

3. Почему без versioning payload сложно делать безопасные релизы?

<details><summary>Ответ</summary>

Потому что в очереди могут быть старые сообщения, а разные версии кода API/worker могут работать одновременно. Без версии невозможно надежно поддерживать совместимость.

</details>

4. Что является минимальным набором наблюдаемости для интеграции web backend + Celery?

<details><summary>Ответ</summary>

Структурированные логи API и worker с общим correlation id, базовые метрики очередей/времени выполнения/ошибок и возможность проследить путь request -> publish -> consume -> outcome.

</details>

5. Какой подход к тестам самый устойчивый?

<details><summary>Ответ</summary>

Комбинация: быстрые unit/API тесты с моками publish layer + контрактные тесты payload + интеграционные smoke тесты с реальным broker/worker.

</details>

6. Почему наличие `task_id` в ответе API недостаточно для качественной эксплуатации?

<details><summary>Ответ</summary>

Потому что нужен не только идентификатор, но и вся операционная обвязка: статусная модель (`queued/running/success/failure/retrying`), correlation id, обработка failure path, мониторинг очередей и понятная диагностика для поддержки.

</details>

7. В чём ключевая разница между "задача поставлена" и "бизнес-операция завершена"?

<details><summary>Ответ</summary>

"Задача поставлена" — это событие уровня инфраструктуры (message accepted/published), а "бизнес-операция завершена" — доменный результат (успешный side effect, подтверждённый статус). Между ними могут быть retries, задержки и ошибки.

</details>

---
