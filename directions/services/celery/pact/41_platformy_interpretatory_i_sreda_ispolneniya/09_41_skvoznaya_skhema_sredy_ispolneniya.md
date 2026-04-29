[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Сквозная схема среды исполнения

```mermaid
flowchart LR
    A[Producer app] --> B[Broker]
    B --> C[Celery Worker Pod/VM]
    C --> D[Python Interpreter]
    D --> E[Task Runtime]
    E --> F[(DB/API/Storage)]
    C --> G[cgroups limits]
    C --> H[OS signals]
    C --> I[TZ/Locale settings]
    H --> E
    G --> E
    I --> E
```

ASCII-образ "что реально влияет на задачу":

```text
Task code
  inside Python runtime
    inside worker process model
      inside container/VM limits
        inside OS scheduling + time settings
          inside orchestration lifecycle
```

Дополнительная "слоистая" карта (удобно для triage): где заканчивается прикладной код и начинается платформа.

```mermaid
flowchart TB
  subgraph App[Application layer]
    T[Task business logic]
  end
  subgraph Celery[Celery runtime]
    W[Worker / pool / prefetch / ack policy]
  end
  subgraph Py[Python runtime]
    I[Interpreter + stdlib + site-packages]
  end
  subgraph OS[OS / host]
    S[Signals, ulimit, clocks, filesystem]
  end
  subgraph Orc[Container / orchestrator]
    C[cgroups: CPU/mem/pids + probes + rollout]
  end
  T --> W --> I --> S
  C --> S
  C --> W
```

Ключевая идея схемы: проблема редко живет в одном слое. Обычно инцидент — это пересечение нескольких факторов (например, CPU throttle + длинный I/O timeout + aggressive prefetch).

#### Проверь себя: сквозная модель

1. Почему "исправить код задачи" не всегда лечит operational-инцидент?
2. Какие два внешних слоя чаще всего делают код "медленным" без изменений в коде?
3. Почему на ASCII-схеме **orchestration lifecycle** стоит на самом нижнем уровне, хотя «логика задачи» кажется главной?

<details><summary>Ответ</summary>

1. Потому что корень может быть в лимитах, сигналах, сети, scheduler-е или времени, а не в логике задачи.
2. cgroup-лимиты CPU/memory и оркестрационная политика (rollout, reschedule, node pressure).
3. Потому что оркестратор может в любой момент остановить/пересоздать pod и тем самым оборвать исполнение; без учёта этого даже идеальный task-код не выполнит контракт доставки.

</details>

---

<a id="411-ос"></a>
