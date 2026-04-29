[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Что желательно знать заранее

Желательно, чтобы ты уже уверенно понимал:

- базовую архитектуру Celery (producer/broker/worker/result backend) и message flow из предыдущих частей;
- семантику доставки “как минимум один раз” (at-least-once), `ack`, `prefetch`, redelivery;
- основы `worker`-пула (prefork/threads/gevent) и почему процесс может падать независимо от master;
- базовую идею orchestration через `group/chord` и роль result backend.

Если что-то из этого ещё “шатается” — не беда: в этой части мы будем повторять ключевые идеи, но уровень будет **экспертный**.

---
