[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Оглавление по этапам изучения

| Этап | Раздел | Содержание | Ключевые понятия |
|---|---|---|---|
| **Этап 1** | [13.1. Как Celery устроен “под капотом”](#131-kak-celery-ustroen-pod-kapotom) | Карта внутренних подсистем и их границы | app, registry, loader, blueprint |
| **Этап 2** | [13.2. Task message protocol: что лежит в очереди](#132-task-message-protocol-chto-lezhit-v-ocheredi) | Структура сообщения, версии протокола, метаданные графа | headers, properties, body, root_id |
| **Этап 3** | [13.3. Consumer pipeline: от broker до pool](#133-consumer-pipeline-ot-broker-do-pool) | Путь сообщения: reserve → dispatch → ack/reject | prefetch, strategy, QoS |
| **Этап 4** | [13.4. Bootsteps: жизненный цикл worker и расширения](#134-bootsteps-zhiznennyy-cikl-worker-i-rasshireniya) | Как worker собирается при старте и как добавить свой шаг | bootstep dependencies |
| **Этап 5** | [13.5. Signals: hooks для observability и инициализации](#135-signals-hooks-dlya-observability-i-inicializacii) | Когда сигналы полезны и когда вредны | task_prerun, worker_ready |
| **Этап 6** | [13.6. Remote control internals: inspect/control/broadcast](#136-remote-control-internals-inspectcontrolbroadcast) | Команды, “рассылка”, риски безопасности | inspect, control, broadcast |
| **Этап 7** | [13.7. Chord internals: chord unlock и зависимость от backend](#137-chord-internals-chord-unlock-i-zavisimost-ot-backend) | Почему chord сложен и как он синхронизируется | group result, unlock |
| **Этап 8** | [13.8. Internal debugging: как чинить странности](#138-internal-debugging-kak-chinit-strannosti) | Чек-листы и практический подход к локализации | logs, traces, stack layers |
| **Финал** | [Справочник, сценарии, самопроверка, ошибки, резюме](#final-spravochnik-scenarii-samoproverka-oshibki-rezyume) | Конспект, кейсы, контроль | runbooks internals |

---
