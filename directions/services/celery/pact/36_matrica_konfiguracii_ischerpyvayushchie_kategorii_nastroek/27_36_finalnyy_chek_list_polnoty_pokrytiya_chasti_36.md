[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Финальный чек-лист полноты покрытия части 36

Эта таблица — контроль того, что материал действительно закрыл план не "по ощущениям", а по пунктам.

| Подпункт плана | Статус покрытия | Где смотреть |
|---|---|---|
| `36.1` App/discovery + timezone/UTC | Полностью | раздел `36.1` + исчерпывающая матрица |
| `36.2` Broker URLs/read-write/retry/pool/heartbeat/SSL/failover | Полностью | раздел `36.2` + transport comparison + матрица |
| `36.3` Task policy (serializer/protocol/ack/retry/routes/queues/priority/annotations) | Полностью | раздел `36.3` + конфликты опций + матрица |
| `36.4` Worker runtime/logging/events/remote control/rare worker keys | Полностью | раздел `36.4` + ASCII fairness + матрица |
| `36.5` Beat scheduler/sync/deadlines/init callback | Полностью | раздел `36.5` + recovery sequence + матрица |
| `36.6` Result backend/retry/extended/chord/cache/compression | Полностью | раздел `36.6` + edge cases + матрица |
| `36.7` Events/TTL/prefix/persistence/sent events | Полностью | раздел `36.7` + operational metrics + матрица |
| `36.8` Security keys/certs/digest + payload trust | Полностью | раздел `36.8` + hardening checklist + матрица |
| `36.9` Test/debug eager profile | Полностью | раздел `36.9` + test coverage matrix |
| `36.10` Misc/rare/control queues/backend SSL/deprecated | Полностью | раздел `36.10` + исчерпывающая матрица |

#### Проверь себя: финальный чек

1. Зачем нужен отдельный "чек полноты", если уже есть оглавление?
2. Как использовать эту таблицу при ревью нового `celeryconfig.py`?
3. Что делать, если пункт формально "есть", но практически не протестирован?

<details><summary>Ответ</summary>

1) Оглавление показывает структуру чтения, а чек полноты — факт закрытия требований плана и эксплуатационной готовности.  
2) Проходить по строкам: у каждой категории должно быть обоснование, метрика проверки и сценарий отката.  
3) Считать пункт незавершенным: добавить тест-кейс/канареечную проверку и только после этого фиксировать как покрытый.

</details>

---
