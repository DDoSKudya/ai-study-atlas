[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Типичные ошибки по части

- рассматривать ОС/контейнер как "нейтральный фон", а не как часть архитектуры Celery;
- поднимать concurrency без измерений и без пересчета лимитов;
- обновлять Python/библиотеки без матрицы совместимости;
- не тестировать graceful shutdown и rollout на staging;
- игнорировать timezone/DST и использовать naive datetime в расписаниях;
- не иметь platform-runbook и повторяемого checklist перед релизом;
- ставить `readOnlyRootFilesystem` без writable volume для `/tmp` и данных beat/schedule;
- забывать, что `celery beat` пишет schedule state в локальный файл (по умолчанию `celerybeat-schedule`) и требует writable путь (`-s`/`--schedule`) + отдельно продумывать `pidfile`, если он включен;
- при запрете **любых** локальных файлов состояния не рассматривать альтернативу **DB-backed** расписания (части `11/18`) и упираться в «ещё один PVC» без смысла для комплаенса;
- включать **Pod SecurityContext** (non-root) без **`fsGroup`/прав** на volume и списывать `Permission denied` на «Celery сломан»;
- путать `worker_max_memory_per_child` (KiB, внутренняя ротация) с OOMKilled/limits;
- путать "pip freeze зеленый" с корректностью `Requires-Python` для релизной поставки;
- считать, что "Windows dev == Linux prod contract" без Linux CI/стенда;
- в `prefork` поднимать тяжёлые I/O-клиенты на import и удивляться "рандомным" ошибкам в child-процессах;
- деплоить через `docker compose` без `stop_grace_period`/`init: true` и ожидать такой же graceful shutdown, как в зрелом k8s-контуре «из коробки».

#### Проверь себя: типичные ошибки по части

1. Почему пункт про **`pip freeze` vs `Requires-Python`** относится к поставке, а не к «чистому кодингу»?
2. Какая пара ошибок из списка чаще всего **вместе** объясняет `Permission denied` на beat при «идеально» смонтированном PVC?
3. Почему ошибка «Windows dev == Linux prod» — это в первую очередь про **процесс разработки**, а не про OS preferences?

<details><summary>Ответ</summary>

1. Потому что прод ставится из конкретного артефакта; freeze не заменяет контракт Python, который объявлен в metadata установленного пакета.
2. `readOnlyRootFilesystem` без правильного writable пути **и** `runAsNonRoot` без `fsGroup`/прав на volume — оба дают отказ записи, но с разных сторон политики.
3. Потому что без Linux CI/стенда команда систематически пропускает fork-safety, сигналы и лимиты, которые проявляются только в target-рантайме.

</details>

---

<a id="резюме-части-41"></a>
