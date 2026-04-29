[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Карта соответствия глобальному плану

<a id="карта-соответствия-глобальному-плану"></a>

| Пункт плана                                                                                                 | Где раскрыто                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `41.1` Linux как основной target; `signal handling` (SIGTERM/SIGKILL)                                       | [41.1 — Linux, сигналы, отличия от Windows/macOS](#linux-сигналы-отличия-windowsmacos)                                                     |
| `41.1` Windows: ограничения пулов, сигналы, пути — что **официально** про поддержку                         | [41.1 — Windows: пулы, пути, песочница, рекомендации](#windows-пулы-пути-песочница-и-что-официально)                                       |
| `41.1` macOS: dev-особенности (сигналы, пути, perf vs Linux)                                                | [41.1 — macOS dev-особенности](#macos-dev-особенности)                                                                                     |
| `41.2` CPython: минимальная версия для конкретного релиза `celery` (проверка из packaging metadata)         | [41.2 — Минимальная версия Python: как читать из фактов, а не "на ухо"](#минимальная-версия-python-как-читать-из-фактов-а-не-на-ухо)       |
| `41.2` PyPy: совместимость, perf trade-offs, edge cases                                                     | [41.2 — PyPy: когда это может быть выгодно](#pypy-когда-это-может-быть-выгодно)                                                            |
| `41.2` Free-threading / subinterpreters: риск смешивать с "просто Celery"                                   | [41.2 — Free-threading / subinterpreters: риск и правило безопасности](#free-threading--subinterpreters-риск-и-правило-безопасности)       |
| `41.2` (углубление) `prefork` + **fork-safety** глобальных клиентов/пулов (ORM, gRPC, TLS)                  | [41.2 — Prefork и fork-safety: что наследует child после fork()](#prefork-и-fork-safety-глобальные-объекты-после-fork)                     |
| `41.3` PID 1, zombie reaping, `tini` / `dumb-init`                                                          | [41.3 — PID1, reaping, init-wrapper](#pid1-reaping-init-wrapper)                                                                           |
| `41.3` Docker / `docker compose` без k8s: `init`, `stop_grace_period`, healthcheck                          | [41.3 — Docker и Compose (без Kubernetes)](#docker-i-compose-bez-kubernetes)                                                               |
| `41.3` Read-only filesystem, tmp, `statedb`/`celerybeat-schedule`                                           | [41.3 — Read-only rootfs, tmp и файлы schedule](#read-only-rootfs-tmp-и-файлы-schedule)                                                    |
| `41.3` (углубление) read-only: **DB-backed** расписание вместо файла (`django-celery-beat` / части `11/18`) | [41.3 — Read-only rootfs, tmp и файлы schedule](#read-only-rootfs-tmp-и-файлы-schedule)                                                    |
| `41.3` K8s: CPU limits, throttling, OOMKilled vs Celery child restart                                       | [41.3 — Throttling, OOMKilled, restart-политика vs `max_memory_per_child`](#throttling-oomkilled-restart-политика-vs-max_memory_per_child) |
| `41.3` (углубление) **Pod SecurityContext**: non-root, `fsGroup`, read-only rootfs ↔ writable volume        | [41.3 — Pod SecurityContext и запись в volume](#pod-securitycontext-и-запись-в-volume)                                                     |
| `41.4` `ulimit`, file descriptors, `worker_max_memory_per_child`                                            | [41.4 — ulimits, fd, `worker_max_memory_per_child` vs OOMKilled](#ulimits-fd-worker_max_memory_per_child-vs-oomkilled)                     |
| `41.4` NUMA, CPU pinning (нишево)                                                                           | [41.4 — NUMA / CPU pinning (когда и зачем)](#numa--cpu-pinning-когда-и-зачем)                                                              |
| `41.5` `TZ` env vs `timezone` в приложении, DST + beat (связь с частью 11)                                  | [41.5 — `TZ` и `LC_*`: как не "переопределить" самого себя](#tz-и-lc_как-не-переопределить-самого-себя)                                    |
| `41.5` Time sync, DST, стабильность расписаний                                                              | [41.5 — NTP, drift, “плавающие” расписания](#ntp-drift-плавающие-расписания)                                                               |

#### Проверь себя: карта соответствия плану

1. Почему карта покрытия нужна даже при подробном оглавлении?
2. Что именно карта ускоряет при обновлении материала под новую платформу?
3. Как по строке карты понять, что инцидент с beat на read-only **связан** с частями `11/18`, а не только с `41.3`?

<details><summary>Ответ</summary>

1. Оглавление дает навигацию, а карта подтверждает полноту закрытия пунктов master-плана.
2. Позволяет быстро определить, какие разделы пересматривать при изменении платформенных требований.
3. В карте явно стоят мосты: read-only + файловый schedule ↔ DB-backed расписание и ссылки на `11/18`; это подсказывает, что лечить нужно **контракт планировщика и хранения state**, а не только volume mount.

</details>

---

<a id="сквозная-схема-среды-исполнения"></a>
