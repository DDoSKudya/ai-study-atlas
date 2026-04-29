[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Справочник по части 8

| Тема | Ключевые пункты |
| --- | --- |
| Жизненный цикл worker | Старт -> bootsteps -> broker connect -> consumer loop -> shutdown; сигналы влияют на fate задач. |
| Concurrency модели | `prefork` для изоляции и CPU, `threads` ограничены GIL, `gevent/eventlet` для I/O с проверкой совместимости, `solo` для отладки. |
| Prefork глубина | Fork-семантика, re-init соединений, copy-on-write, контроль memory drift через recycling. |
| Ресурсный тюнинг | `concurrency` + лимиты child + autoscale + разделение очередей по SLA. |
| Prefetch и fairness | Высокий prefetch повышает throughput, но может ломать responsiveness и увеличивать redelivery window. |
| Ack и worker loss | Early ack -> риск потери; late ack -> риск дублей; crash-тесты и идемпотентность обязательны. |
| Production-управление | Dedicated workers, queue affinity, canary, blue/green и runbooks с rollback. |

---
