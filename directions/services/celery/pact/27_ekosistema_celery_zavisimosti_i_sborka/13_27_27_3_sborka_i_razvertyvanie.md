[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## 27.3 Сборка и развёртывание

### Цель раздела

Сделать сборку Celery-контуров воспроизводимой, безопасной и удобной для эксплуатации.

### В этом разделе главное

- reproducible build снижает класс "не воспроизводится у меня";
- Docker-образ должен быть минимальным и контролируемым;
- безопасность supply chain (SBOM, vuln scan, license check) — часть стандартного pipeline;
- секреты внутри образа — критичный anti-pattern;
- multi-arch и runtime-совместимость нужно проверять заранее.

### Теория и правила

1. **Lockfiles обязательны.**  
   Используй `pip-tools`, `poetry lock` или `uv lock` для фиксации транзитивных версий.

2. **Многослойная Docker-сборка.**  
   Сначала dependencies, потом код; так ускоряется rebuild и уменьшается дрейф.

3. **Non-root runtime.**  
   Worker-процессы в контейнере не должны запускаться от root без крайней причины.

4. **SBOM + scanner + license gates.**  
   Сборка проходит только если критичные уязвимости и лицензии в рамках политики.

5. **Секреты приходят в runtime, а не baked-in.**  
   Никаких `.env` с паролями внутри image layers.

6. **Entrypoint и graceful stop hooks.**  
   Образ должен корректно обрабатывать сигналы остановки и health-проверки.

### Distroless vs slim: как выбирать

| Подход | Плюсы | Минусы | Когда уместен |
|---|---|---|---|
| **`python:slim`** | проще дебажить, привычная экосистема | больше surface area | команды с частой диагностикой в контейнере |
| **distroless** | меньше attack surface, строже runtime | сложнее интерактивная отладка | зрелый pipeline и сильные внешние инструменты наблюдаемости |

Правило: если у команды слабый observability/diagnostics контур, слишком ранний переход в distroless может замедлить расследования.

#### Проверь себя: выбор базового образа

1. Почему выбор между `slim` и `distroless` зависит от зрелости команды, а не только от security-цели?

<details><summary>Ответ</summary>

Потому что кроме attack surface важна способность быстро диагностировать инциденты. Если диагностика не зрелая, слишком “закрытый” runtime может увеличить время восстановления.

</details>

2. Когда переход на distroless особенно оправдан?

<details><summary>Ответ</summary>

Когда есть зрелые внешние observability-инструменты, стабильный CI/security pipeline и команда готова к non-interactive debugging-практике.

</details>

### Пример `requirements`-подхода (pip-tools)

```bash
# Входной файл
echo "celery[redis]==5.4.*" > requirements.in
echo "fastapi==0.115.*" >> requirements.in

# Генерация lock-подобного requirements с pinning транзитивных зависимостей
pip-compile --generate-hashes requirements.in -o requirements.txt

# Установка строго по pinned-файлу
pip install --require-hashes -r requirements.txt
```

### Альтернатива: Poetry и uv (кратко)

```bash
# Poetry
poetry add "celery[redis]@^5.4" fastapi@^0.115
poetry lock
poetry install --sync
```

```bash
# uv
uv add "celery[redis]==5.4.*" "fastapi==0.115.*"
uv lock
uv sync --frozen
```

Практическое правило: не смешивай менеджеры lock-файлов в одном проекте.  
Выбери один основной путь (`pip-tools` или `poetry` или `uv`) и стандартизируй его в CI/документации.

#### Проверь себя: менеджеры lock-файлов

1. Что ломается первым при двух источниках истины (`poetry.lock` и `requirements.txt`)?

<details><summary>Ответ</summary>

Паритет сред: локально и CI начинают ставить разные наборы зависимостей, что делает воспроизводимость и диагностику нестабильными.

</details>

2. Почему “один lock-путь” важен именно для Celery-контуров?

<details><summary>Ответ</summary>

Потому что поведение worker/runtime чувствительно к версиям транзитивных библиотек транспорта и процессов; рассинхрон версий быстро превращается в инциденты.

</details>

### Пример Dockerfile (базовый production-паттерн)

```dockerfile
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN useradd -m -u 10001 appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER appuser

ENTRYPOINT ["./docker/entrypoint-worker.sh"]
```

### Mermaid: pipeline поставки артефакта

```mermaid
flowchart LR
    A["Resolve lockfile"] --> B["Build docker image"]
    B --> C["Generate SBOM"]
    C --> D["Run vuln and license scan"]
    D --> E{"Policy passed?"}
    E -->|Yes| F["Push image"]
    E -->|No| G["Block release"]
    F --> H["Deploy worker/beat"]
```

### Sequence: жизненный цикл релиза worker-образа

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant CI as CI Pipeline
    participant Sec as Security Gates
    participant Reg as Image Registry
    participant K8s as Runtime Cluster
    Dev->>CI: commit (deps + code)
    CI->>CI: resolve lockfile and build image
    CI->>Sec: SBOM + vuln/license scan
    Sec-->>CI: pass/fail
    CI->>Reg: push signed image (if pass)
    Reg->>K8s: deploy canary worker
    K8s-->>CI: health/SLO signals
```

### Multi-arch и совместимость с worker-нодами

Если кластер смешанный (`amd64` + `arm64`), образ должен собираться и тестироваться под обе архитектуры.  
Важно проверять:
- одинаковое поведение зависимостей на разных arch;
- отсутствие скрытых бинарных wheel-конфликтов;
- валидность базового образа и security scanner policy для каждой arch.

### Health probes и graceful hooks (практический минимум)

Для Celery-контуров важно проверять не просто "процесс жив", а "воркер может безопасно брать задачи".  
Минимальный набор:

- liveness: процесс worker отвечает;
- readiness: есть доступ к брокеру и критичным зависимостям;
- graceful hook: при остановке worker перестаёт брать новые задачи и корректно завершает текущие в рамках политики.

```text
SIGTERM -> stop consuming -> finish/ack in-flight tasks -> exit
```

Если этот контракт не соблюдается, rolling update может превратиться в источник дублей и таймаутов.

### Секреты в образе: anti-pattern и правильно

```text
Плохо:
- COPY .env в образ
- ENV BROKER_URL=amqp://user:password@...
- хранить cloud keys в git и прокидывать при build

Хорошо:
- получать секреты в runtime из secret manager
- использовать короткоживущие креды/rotation
- ограничивать права по принципу least privilege
```

### Entrypoint, probes и graceful stop

`entrypoint-worker.sh` обычно делает:
1. валидацию обязательных env;
2. проверку доступности зависимостей (по политике);
3. запуск `celery worker` с нужными флагами;
4. корректное пробрасывание сигналов (SIGTERM/SIGINT) в основной процесс.

Пример "что проверить в review":

| Пункт | Что должно быть |
|---|---|
| PID 1 поведение | entrypoint не "глотает" сигналы |
| Прекращение intake | worker не берёт новые задачи при stop |
| In-flight политика | явно задокументировано, как завершаются/повторяются текущие задачи |
| Probe semantics | readiness падает до принудительного kill |

Пример каркаса entrypoint:

```bash
#!/usr/bin/env sh
set -eu

: "${CELERY_APP:?CELERY_APP is required}"
: "${BROKER_URL:?BROKER_URL is required}"

cleanup() {
  echo "Signal received, stopping worker intake..."
  # Здесь обычно используется корректная остановка процесса Celery
}

trap cleanup TERM INT

exec celery -A "$CELERY_APP" worker -l INFO
```

### Практика / реальные сценарии

- **Сценарий "собралось вчера, не собирается сегодня":**  
  причина — плавающие транзитивные зависимости без lock-файла.

- **Сценарий "в проде внезапно критичная CVE":**  
  без SBOM и vuln-scan неясно, какой образ затронут и где быстро чинить.

- **Сценарий "image работает на amd64, падает на arm64":**  
  не было multi-arch smoke-теста до выката.

- **Сценарий "poetry.lock обновили, а CI всё ещё ставит requirements.txt":**  
  в проекте фактически два источника истины, из-за чего среды рассинхронизированы.

### Типичные ошибки

- отсутствие lock-файлов;
- root-пользователь в контейнере по умолчанию;
- секреты в build layers;
- игнорирование license compliance;
- отсутствие проверки graceful stop при релизах.

### Что будет если...

Если пренебречь reproducible delivery:
- время расследования инцидентов вырастет;
- каждая пересборка может менять поведение;
- security-аудит станет реактивным и болезненным;
- релизы worker'ов будут нестабильны.

Если в проекте одновременно живут несколько несогласованных lock-механизмов:
- команда теряет доверие к артефактам сборки;
- "у меня работает" становится нормой вместо воспроизводимости;
- откаты и сравнение версий занимают непропорционально много времени.

### Проверь себя

1. Почему `python:slim` сам по себе не гарантирует безопасность образа?

<details><summary>Ответ</summary>

Потому что безопасность определяется полным набором зависимостей, конфигурацией runtime, правами процесса, наличием сканирования и политикой обновлений, а не только базовым образом.

</details>

2. Что даёт пара "SBOM + lockfile" вместе?

<details><summary>Ответ</summary>

Lockfile обеспечивает воспроизводимость, а SBOM — прозрачность состава артефакта. Вместе они дают контроль и для эксплуатации, и для безопасности.

</details>

3. Когда multi-arch особенно критичен для Celery?

<details><summary>Ответ</summary>

Когда worker-ноды в разных средах/кластерах имеют разные архитектуры CPU, и единый pipeline должен поставлять совместимые образы без сюрпризов.

</details>

4. Что опаснее: отсутствие liveness или отсутствие корректной readiness?

<details><summary>Ответ</summary>

В большинстве Celery-сценариев отсутствие корректной readiness опаснее: pod может считаться готовым и получать задачи, хотя фактически не способен их безопасно обработать.

</details>

### Запомните

Сборка — это часть надежности Celery, а не "внешняя задача DevOps".

---
