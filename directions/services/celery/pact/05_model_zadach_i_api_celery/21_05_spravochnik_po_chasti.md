[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Справочник по части

| Тема | Что держать в голове |
| --- | --- |
| Декларация | имя = контракт; `bind` = контекст; `base` = общие правила |
| Вызов | `delay` простой; `apply_async` полный; `send_task` по имени |
| Сигнатуры | `s` / `si` / `signature`; `.set()` для опций доставки; small payload |
| Контекст | `self.request` + headers для корреляции |
| Ошибки | Ignore vs Retry vs business fail |
| Опции | backoff+jitter, лимиты, `ignore_result`, `acks_late`, `rate_limit` |
| Routing | очередь/ключ/headers по месту |
| Идентичность | БД/Redis + идемпотентность |
| Отмена | флаги продукта + revoke как вспомогательное |
| Отладка | `.run`/eager с пониманием границ |
| `signature()` | Имя строкой + args/kwargs/options |
| `Reject` | Отказ от сообщения (requeue/drop), не путать с `Ignore` |
| Сериализация | `serializer` + `compression` + `accept_content` |
| Payload | маленький / стабильный / воспроизводимый + `schema_version` |
| `link` / `link_error` | Колбэк после успеха/ошибки **новой** задачей в очереди; проектируй идемпотентно; тяжёлую оркестрацию — в canvas |

---
