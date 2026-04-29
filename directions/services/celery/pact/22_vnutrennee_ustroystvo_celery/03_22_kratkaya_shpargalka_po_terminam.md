[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Краткая шпаргалка по терминам

| Термин | Что это значит простыми словами |
|---|---|
| **Celery app** | Центральный объект конфигурации и регистрации задач. |
| **Task registry** | Таблица соответствия `task_name -> callable`, которую использует worker. |
| **Loader** | Механизм импорта модулей задач и конфигурации. |
| **Message protocol** | Формат сообщения задачи: метаданные + payload. |
| **Consumer pipeline** | Внутренний конвейер worker-а: receive -> decode -> route -> execute -> ack/reject. |
| **Bootsteps** | Модульная сборка worker-а по зависимым шагам запуска. |
| **Signals** | События жизненного цикла, на которые можно подписаться callback-ами. |
| **Remote control** | Канал команд и инспекции worker-ов (`inspect/control`). |
| **Broadcast** | Рассылка команды множеству worker-ов сразу. |
| **Chord unlock** | Логика проверки "все задачи group завершены" и запуска callback. |
| **Internal debugging** | Диагностика проблемы через внутренние слои Celery. |

---
