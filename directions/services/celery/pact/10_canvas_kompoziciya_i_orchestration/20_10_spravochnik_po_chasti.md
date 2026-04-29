[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Справочник по части

| Тема | Ключевые пункты |
| --- | --- |
| **Signature и partial** | Signature - декларация вызова; partial/immutable управляют передачей аргументов между шагами. |
| **Chain** | Последовательная зависимость; ошибка останавливает хвост; контракты входа/выхода обязательны. |
| **Group** | Fan-out независимых задач; следи за burst-нагрузкой и размером группы. |
| **Chord** | Fan-out + fan-in; backend критичен; callback должен быть идемпотентен. |
| **Map/starmap/chunks** | Инструменты batch dispatch; выбирай размер партии по замерам. |
| **Workflow design** | Гранулярность, coupling, state store, replay, compensation, correlation ID. |
| **Ограничения Canvas** | При state explosion и long-running orchestration оцени переход на специализированные решения. |
| **Ошибки/callback-и** | Классифицируй ошибки, не ретраить всё подряд, partial success должен иметь recovery-план. |

---
