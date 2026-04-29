[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Вопросы для самопроверки

1. Почему в Celery очередь считается "памятью между релизами", и как это влияет на апгрейд?

<details><summary>Ответ</summary>

Потому что сообщения живут дольше процесса деплоя. Это требует совместимости старого и нового кода в переходном окне и явного контроля payload version.

</details>

2. Зачем совмещать canary rollout и feature flags?

<details><summary>Ответ</summary>

Canary ограничивает blast radius, а feature flag дает быстрый управляемый откат публикации нового формата без полного отката релиза.

</details>

3. Что важнее при миграции брокера: "скорость переключения" или "доказанный parity"?

<details><summary>Ответ</summary>

Доказанный parity. Быстрое, но непроверенное переключение часто приводит к скрытой деградации SLA и длительным инцидентам.

</details>

4. Почему удаление legacy-path без дренажа очереди — анти-паттерн?

<details><summary>Ответ</summary>

Потому что старые/отложенные сообщения все еще могут прийти на обработку и сломаться на новом коде.

</details>

5. Какие минимальные метрики обязательны в migration dashboard?

<details><summary>Ответ</summary>

Success/failure rate, retry rate, queue lag, p95/p99 latency, unknown task/errors by payload_version, duplicates rate.

</details>

---
