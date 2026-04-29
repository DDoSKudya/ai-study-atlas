[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Справочник по части

| Тема | Короткое правило |
|---|---|
| Выбор транспорта | Сначала требования и failure modes, потом «удобство» |
| `broker_url` | Это инженерный контракт подключения, а не просто адрес |
| Таймауты/heartbeat | Баланс между быстрым обнаружением сбоев и стабильностью соединения |
| Failover | Должен быть не только в конфиге, но и в протестированном runbook |
| Redis/AMQP/SQS | API похож, семантика и ограничения различаются |
| Idempotency | Обязательна при at-least-once и re-delivery |
| Тестовые транспорты | Только для fast feedback, не для proof production behavior |

### Карманный runbook: симптом -> вероятная причина -> что проверить первым

| Симптом | Вероятная причина | Первая проверка |
|---|---|---|
| Задачи «теряются» после publish | окно между приложением и устойчивой фиксацией в broker | publish logs + broker ingress метрики |
| Дубли задач на длинных job | timeout/visibility/re-delivery | runtime p95/p99 vs visibility/ack-профиль |
| Медленный старт worker | DNS/endpoint/network path | резолв endpoint и connect-time |
| Failover «есть», но не срабатывает | сетевой блок/нерабочий резервный endpoint | controlled-failure primary + route/ACL проверка |
| Зеленые тесты, проблемы в проде | тесты только на memory/file | наличие real-broker integration/failure tests |

---
