[← Назад к индексу части XXII](index.md)

## 6. CI/CD и тестирование инфраструктуры (§133)

### 6.0. Общая идея: автоматизируйте всё, что повторяется

Без CI/CD:

- тесты запускаются «иногда руками»;
- проверки стиля забываются;
- деплой — это человек, который заходит на сервер и что‑то делает.

С CI/CD:

- каждый push/PR:
  - запускает тесты;
  - проверяет формат/линтеры;
  - (опционально) собирает образ и выкатывает на staging/prod.

#### 6.0a. Аналогия: ручной тест против автотеста

Как в жизни:

- можно каждый раз вручную проверять, закрыта ли дверь (тесты руками);
- а можно повесить доводчик и сигнализацию (автоматический контроль).

CI/CD — это «доводчик и сигнализация» для кода:

- любая правка автоматически прогоняет проверки;
- если что‑то сломалось — вы видите это **сразу**, а не через неделю.

---

### 6.1. GitHub Actions: минимальный workflow

Файл `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest -q
```

Что здесь происходит:

- триггер — пуш или PR в `main`;
- поднимается виртуальная машина;
- ставится нужная версия Python;
- ставятся зависимости;
- запускаются тесты.

#### 6.1a. Как читать этот workflow «по‑людски»

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

- говорит: «запускай этот workflow при любом push или pull request в ветку `main`».

```yaml
jobs:
  tests:
    runs-on: ubuntu-latest
```

- описывает задание `tests`, которое будет выполняться на виртуальной машине с Linux (ubuntu‑latest).

```yaml
steps:
  - uses: actions/checkout@v4
```

- шаг, который:
  - скачивает ваш репозиторий в файловую систему виртуальной машины (git clone).

```yaml
  - name: Set up Python
    uses: actions/setup-python@v5
    with:
      python-version: "3.12"
```

- ставит нужную версию Python (3.12);
- дальше все команды `python`/`pip` будут использовать её.

```yaml
  - name: Install dependencies
    run: |
      python -m pip install --upgrade pip
      pip install -r requirements.txt
```

- устанавливает ваши зависимости;
- обычно `requirements.txt` уже зафиксирован в репозитории.

```yaml
  - name: Run tests
    run: |
      pytest -q
```

- запускает тесты;
- если какая‑то тестовая команда завершится с ненулевым кодом — job упадёт, и в интерфейсе Actions вы увидите «красный» статус.

Дальше можно добавлять шаги:

- `ruff`, `black`, `mypy`;
- сборка Docker‑образа и пуш в registry;
- деплой на staging/prod.

---

### 6.2. GitLab CI: аналогичный pipeline

Файл `.gitlab-ci.yml`:

```yaml
stages:
  - test

tests:
  stage: test
  image: python:3.12-slim
  script:
    - pip install -r requirements.txt
    - pytest -q
```

Идея та же: при каждом пуше GitLab стартует контейнер с Python, ставит зависимости и гоняет тесты.

---

### 6.3. tox и nox: тесты в разных окружениях

**tox**:

- позволяет описать, как гонять тесты/линтеры в разных версиях Python и с разными наборами зависимостей.

Пример `tox.ini`:

```ini
[tox]
envlist = py310, py311, py312

[testenv]
deps = -rrequirements.txt
commands =
    pytest -q
```

Запуск:

```bash
tox
```

GitHub Actions/GitLab CI могут просто вызывать `tox`, а вся логика окружений будет описана в одном месте.

#### 6.3a. Зачем нужен tox, если есть CI

tox решает задачу:

- «как **локально** и в CI одинаково запускать одни и те же сценарии в разных версиях Python и с разными зависимостями».

Например:

- у вас есть:
  - `py310`, `py311`, `py312`;
  - для каждого окружения нужно:
    - установить зависимости;
    - запустить тесты и линтеры.

Вместо того, чтобы дублировать команды в:

- локальных скриптах;
- GitHub Actions;
- GitLab CI;

вы описываете всё в одном `tox.ini`, а внешние системы просто вызывают одну команду `tox`.

**nox** — похожий инструмент, но конфиг на Python (`noxfile.py`), что даёт больше гибкости.

---

### 6.4. pre‑commit: хуки и авто‑починка

`pre-commit` позволяет автоматически запускать:

- форматер (`black/ruff format`);
- линтер (`ruff`);
- статический анализ (`mypy`);
- собственные скрипты

при каждом `git commit`.

Файл `.pre-commit-config.yaml` (упрощённый пример):

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.0
    hooks:
      - id: black
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
        args: [--fix]
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.0
    hooks:
      - id: mypy
```

Установка:

```bash
pip install pre-commit
pre-commit install
```

Теперь при `git commit`:

- файлы автоматически форматируются;
- базовые нарушения стиля фиксируются;
- mypy прогоняется по изменённым файлам.

---

### 6.5. mypy в CI

Пример отдельного шага в GitHub Actions:

```yaml
  type-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Install deps
        run: |
          pip install -r requirements.txt
          pip install mypy
      - name: Run mypy
        run: mypy src
```

mypy позволяет:

- отловить несоответствия типов ещё до запуска кода;
- постепенно ужесточать проект (режим `--strict`).

---

### 6.6. Запомните по §133

- CI/CD — это не «дополнительная опция», а **страховка** от человеческих ошибок и регрессий.
- GitHub Actions/GitLab CI + tox/nox позволяют выстроить проверку в нескольких окружениях и с разными наборами проверок.
- pre‑commit и mypy помогают поймать много проблем **до** того, как код попадёт в репозиторий или продакшн.

---

