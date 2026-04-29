[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Decision flow: как выбрать направление настройки

```mermaid
flowchart TD
    A[Новый Celery workload] --> B{Есть строгий SLA по latency?}
    B -- Да --> C{Задачи короткие и частые?}
    B -- Нет --> D{Главная цель: cost/throughput?}
    C -- Да --> E[Оптимизируй worker runtime\nprefetch/concurrency/routes]
    C -- Нет --> F[Оптимизируй fairness\nprefetch=1, изоляция длинных задач]
    D -- Да --> G[Batch профиль\nочереди bulk + result TTL]
    D -- Нет --> H[Универсальный baseline]
    E --> I{Есть внешние API лимиты?}
    F --> I
    I -- Да --> J[Добавь rate limit + backoff/jitter]
    I -- Нет --> K[Фокус на memory/retries/observability]
    G --> L[Проверка cost и queue lag]
    H --> L
    J --> L
    K --> L
    L --> M[Canary -> staged rollout -> rollback readiness]
```

#### Проверь себя: decision flow

1. Почему дерево завершается canary/rollback readiness, а не “выбран профиль”?
2. Где в decision flow чаще всего появляется ошибка новичков?

<details><summary>Ответ</summary>

1) Выбор профиля — гипотеза, которая подтверждается только метриками в безопасном rollout.  
2) На ветке throughput: забывают про fairness/idempotency и получают скрытую деградацию.

</details>

---
