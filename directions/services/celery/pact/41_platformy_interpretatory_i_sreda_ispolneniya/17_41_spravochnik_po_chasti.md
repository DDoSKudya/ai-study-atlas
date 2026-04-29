[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Справочник по части

| Тема           | Ключевые пункты                                                                                                                                                           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ОС             | Linux baseline, `SIGTERM` vs `SIGKILL`, `ulimit`, dev-ловушки macOS                                                                                                       |
| Windows        | официальная FAQ-позиция, пулы/пути; production → Linux/WSL2/Docker                                                                                                        |
| Интерпретатор  | `Requires-Python` из metadata, PyPy trade-offs, осторожность с free-threading, `prefork`+fork-safety (глобальные клиенты/пулы)                                            |
| Контейнеры     | `tini`/`dumb-init` или Compose `init: true`, `stop_grace_period`, writable `/tmp`, beat: файл `-s` на volume **или** DB-backed schedule (части `11/18`), read-only rootfs |
| K8s            | requests/limits, throttling vs OOMKilled, grace period, rollout, SecurityContext non-root + `fsGroup` ↔ writable volume                                                   |
| Лимиты         | fd/pids, `worker_max_memory_per_child` (KiB), NUMA/pinning как ниша                                                                                                       |
| Время и локали | `TZ` vs Celery/Django time, `tzdata`, DST, NTP drift                                                                                                                      |

#### Проверь себя: справочник по части

1. Как по таблице быстро выбрать **первый** раздел для triage при `OOMKilled` на worker?
2. Почему в одной строке «Контейнеры» перечислены и **Compose `init`**, и **beat `-s`**?
3. Чем строка «Интерпретатор» в справочнике связана с инцидентом **read-only rootfs** (если связь неочевидна)?

<details><summary>Ответ</summary>

1. Смотреть строку **K8s** (limits/throttle vs OOM) и **Лимиты** (`worker_max_memory_per_child` vs cgroup), затем уточнять по метрикам.
2. Потому что это один чеклист platform-ready деплоя: корректный PID1/signals **и** предсказуемый file IO для beat в жёстком FS-контракте.
3. Напрямую мало; зато «Интерпретатор» напоминает проверить образ/ABI **до** того, как списать симптом на платформу — иногда OOM следствие нативной утечки, а не cgroup.

</details>

---

<a id="частые-сценарии"></a>
