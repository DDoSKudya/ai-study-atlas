[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Сквозная карта микро-сущностей в потоке задачи

```mermaid
flowchart LR
    A[Producer code\napp.task/app.send_task] --> B[Signature/options\nargs kwargs headers]
    B --> C[Broker layer\nExchange Queue Binding]
    C --> D[Worker consumer\nPool Request Task]
    D --> E[Execution\nstate retry events]
    E --> F[Result backend\nAsyncResult GroupResult metadata]
    G[Beat schedule] --> B
    H[Security policy\nserializer + accept_content] --> B
    H --> D
```

Простая интерпретация схемы:

- **слева** мы формируем задание (`Task` + `Signature`);
- **в центре** брокер решает, куда это сообщение попадет;
- **справа** worker исполняет и публикует состояние/результат;
- `beat` периодически генерирует новые вызовы;
- политика безопасности ограничивает допустимые форматы и payload.

#### Проверь себя: сквозная карта

1. Почему политика безопасности в схеме влияет сразу на две точки потока?

<details><summary>Ответ</summary>

Формат и допустимость контента проверяются и при публикации, и при приеме/десериализации. Ошибка на любом конце рвет целостность потока.

</details>

2. Какой переход в схеме чаще всего объясняет симптом "задача отправлена, но не выполняется"?

<details><summary>Ответ</summary>

Переход между broker layer и worker consumer: routing, подписка на очередь, transport-параметры и доступность consumer-ов.

</details>

---
