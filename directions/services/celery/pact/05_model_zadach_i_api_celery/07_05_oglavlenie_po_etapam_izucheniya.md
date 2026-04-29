[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Оглавление по этапам изучения

### Этап 1. Объявление и публикация

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [5.1. Декларация задач](#51-декларация-задач) | `@app.task`, имя, опции, `bind`, базовый класс | task decorator, `bind=True`, custom `Task` |
| [5.2. Вызов задач](#52-вызов-задач) | `delay`, `apply_async`, `send_task`, ETA/expires | publish, options, remote task name |

### Этап 2. Контракт данных

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [5.3. Сигнатуры и сериализуемость](#53-сигнатуры-и-сериализуемость) | `signature`, `s`, `si`, `.set()`, payload design | immutability, serializers, pickle JSON |

### Этап 3. Контекст и контроль потока

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [5.4. Контекст задачи](#54-контекст-задачи) | `self.request`, correlation, tracing | `request.headers`, delivery_info |
| [5.5. Состояния и ошибки](#55-состояния-и-ошибки) | `PENDING`, `Ignore`, `Reject`, `Retry`, revoke | failure semantics, traceback |

### Этап 4. Поведение в production

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [5.6. Опции задач](#56-опции-задач) | acks, retry policy, time limits, rate limits | `autoretry_for`, backoff |
| [5.7. Заголовки, приоритет, routing key](#57-заголовки-приоритет-routing-key-в-apply_async) | headers, priority, exchange/queue | broker limits, `link` |

### Этап 5. Идентичность и жизненный цикл

| Раздел | Содержание | Ключевые понятия |
| --- | --- | --- |
| [5.8. Идентичность и дедупликация](#58-идентичность-и-дедупликация-на-уровне-приложения) | Стабильный `task_id`, locks в БД/Redis | races, TTL |
| [5.9. Замена задачи и отмена](#59-замена-задачи-и-отмена) | `replace`, revoke vs cancel UX | long-running jobs |
| [5.10. Локальный вызов и отладка](#510-локальный-вызов-и-отладка) | `.run()`, eager, trace | tests, dev workflow |

---
