[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Что желательно знать заранее

- части `09`, `14`, `22`, `23`, `36`, `37`;
- базовую модель `producer -> broker -> worker -> result backend`;
- различие между `at-least-once` и «логически exactly-once через идемпотентность»;
- как работают retries, prefetch, ack и worker pools;
- базовые практики наблюдаемости: метрики, structured logs, trace correlation.

#### Проверь себя: входные знания

1. Почему без модели ack/retry сложно корректно использовать `task_failure` и `task_retry`?
2. Зачем перед bootsteps полезно понимать внутренний consumer lifecycle?

<details><summary>Ответ</summary>

1) Потому что сигнал сам по себе не описывает гарантию доставки; без модели ack/retry легко сделать неверный вывод о финальном состоянии задачи.  
2) Bootsteps встроены в жизненный цикл инициализации worker/consumer, и без этой модели легко сломать запуск, graceful shutdown или поток сообщений.

</details>

---
