[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Вопросы для самопроверки по части 4

1. Чем failure symptoms broker’а отличаются от failure symptoms result backend’а?

<details><summary>Ответ</summary>

Падение broker влияет на доставку (publish/reserve/queue behavior), а падение backend влияет на видимость статусов/результата (client не видит обновления, но execution может идти).

</details>

2. Какая часть message flow отвечает за “куда именно попадет сообщение”?

<details><summary>Ответ</summary>

Routing в broker: обменник/очередь/bindings и routing key определяют, в какую очередь сообщение будет помещено.

</details>

3. Как различить ситуацию “задача еще не стартовала” и “задача стартовала, но backend не записал”?

<details><summary>Ответ</summary>

Проверить evidence execution: логи worker и/или events. Если в worker видно started/succeeded/failed, а backend не обновляется — проблема в visibility.

</details>

4. Почему Kombu нельзя считать чисто “внутренним импортом”?

<details><summary>Ответ</summary>

Потому что через Kombu реализуются transport-операции. А transport определяет семантики и возможности доставки, значит влияет на гарантию и retry.

</details>

5. Назови две причины, почему result backend может стать узким местом.

<details><summary>Ответ</summary>

Write/load amplification при записи статусов и массовом polling чтении статусов; плюс стоимость хранения и риск отказов/TTL.

</details>

6. Чем события отличаются от хранения результата?

<details><summary>Ответ</summary>

События — поток телеметрии “что происходило сейчас”, который потребляют наблюдатели. Storage результата — хранилище состояний/результатов для чтения по `task_id` (часто с TTL).

</details>

7. Почему remote control требует сетевой изоляции?

<details><summary>Ответ</summary>

Remote control дает управление и inspect команды. Если контроль доступен извне, им может злоупотребить третья сторона: отмена задач, ограничения rate, утечки данных.

</details>

8. Какую формулу можно использовать для первичной локализации проблемы?

<details><summary>Ответ</summary>

Delivery / Execution / Visibility. Сначала определяем плоскость отказа по симптомам, затем проверяем компоненты доказательствами.

</details>

---
