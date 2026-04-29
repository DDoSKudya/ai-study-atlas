[← Назад к индексу части VIII](index.md)


**Цель раздела:** ориентироваться в **Poetry** (pyproject.toml + poetry.lock), **uv** (быстрый менеджер на Rust), **pipx** (установка CLI-инструментов в изолированные окружения), **conda/mamba** (альтернатива для data science) и **pyenv/asdf** (несколько версий Python в системе).

---

### Термины

| Термин | Определение |
|--------|-------------|
| **Poetry** | Менеджер зависимостей и сборки: свой pyproject.toml и poetry.lock; команды poetry add/install/run; lock-файл фиксирует все версии. |
| **uv** | Быстрый менеджер пакетов и окружений (на Rust); совместим с pip и pyproject.toml, может заменять pip/venv в рабочих процессах. |
| **pipx** | Устанавливает CLI-приложения (пакеты с console_scripts) в отдельные виртуальные окружения и добавляет их в PATH; глобально не засоряет один общий venv. |
| **conda** | Менеджер пакетов и окружений от Anaconda; свои репозитории, поддержка бинарных пакетов и нескольких версий Python; часто используется в data science. |
| **pyenv** | Менеджер версий Python: установка нескольких интерпретаторов (3.9, 3.12 и т.д.), переключение глобально или локально (.python-version). |

---

### Poetry

**Poetry** — менеджер зависимостей и сборки, использующий **pyproject.toml** для метаданных и зависимостей и **poetry.lock** для фиксации точных версий всех пакетов (включая транзитивные). Один инструмент заменяет связку pip + pip-tools + setuptools для типичного проекта.

**Установка:** официальный установщик — `curl -sSL https://install.python-poetry.org | python3 -`; или через pip (в изолированном окружении): `pip install poetry`.

**Основные команды (пошагово):**

| Команда | Назначение |
|---------|------------|
| `poetry init` | Интерактивное создание pyproject.toml в текущем каталоге (имя, версия, зависимости). |
| `poetry add requests` | Добавить зависимость в [tool.poetry.dependencies] и установить её; обновить lock. |
| `poetry add --group dev pytest` | Добавить зависимость в группу dev (аналог optional-dependencies). |
| `poetry add -D mypy` | То же для dev-зависимости (-D = --group dev). |
| `poetry remove requests` | Удалить зависимость и обновить lock. |
| `poetry lock` | Создать или обновить poetry.lock по текущему pyproject.toml (разрешить все версии). |
| `poetry install` | Установить зависимости из poetry.lock (если lock нет — создать и установить). |
| `poetry install --no-root` | Установить только зависимости, не сам проект (удобно в CI). |
| `poetry run python script.py` | Запустить команду в виртуальном окружении Poetry. |
| `poetry run pytest` | Запустить pytest в окружении проекта. |
| `poetry shell` | Активировать виртуальное окружение Poetry в текущей оболочке. |
| `poetry env info` | Показать путь к виртуальному окружению и версию Python. |
| `poetry export -f requirements.txt --output requirements.txt` | Экспорт зависимостей в формате requirements.txt (для CI без Poetry). |

**Структура pyproject.toml с Poetry:** Poetry использует секцию **[tool.poetry]** для метаданных и зависимостей; при сборке пакета эти данные можно маппить в [project] (PEP 621) через плагин или вручную. Пример минимального [tool.poetry]:

```toml
[tool.poetry]
name = "my-package"
version = "1.0.0"
description = "Short description"
authors = ["Author <a@b.com>"]

[tool.poetry.dependencies]
python = "^3.9"
requests = ">=2.28"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
```

**Спецификаторы версий в Poetry (кратко):** Poetry использует свои обозначения для диапазонов версий. **`^3.9`** — «совместимая» версия: `>=3.9, <4.0` (по умолчанию для python). **`~3.9.0`** — «приближённая»: `>=3.9.0, <3.10.0`. **`*`** — любая версия. **`>=2.28,<3`** — явный диапазон (как в PEP 508). При `poetry add requests` Poetry подберёт последнюю версию, удовлетворяющую ограничениям, и зафиксирует её в poetry.lock.

**Lock-файл:** `poetry.lock` фиксирует точные версии всех пакетов (включая транзитивные). В репозиторий **нужно** коммитить poetry.lock, чтобы у всех разработчиков и в CI была одинаковая среда. При изменении pyproject.toml (добавление/удаление зависимостей) выполняют `poetry lock`, затем `poetry install`. Если lock устарел (изменён вручную или из другого ветки), `poetry install` предупредит; обновить lock под текущий pyproject.toml: `poetry lock --no-update` (без обновления версий) или `poetry update` (обновить зависимости в рамках ограничений и пересобрать lock).

**Дополнительные команды Poetry:**

| Команда | Назначение |
|---------|------------|
| `poetry show` | Список установленных пакетов с версиями. |
| `poetry show --tree` | Дерево зависимостей. |
| `poetry config --list` | Показать настройки Poetry (виртуальное окружение по умолчанию, репозитории и т.д.). |
| `poetry config virtualenvs.in-project true` | Создавать .venv внутри проекта (удобно для единообразия с venv). |
| `poetry source add --priority=primary myrepo https://my-index/simple/` | Добавить альтернативный индекс (например, приватный). |

**Пошаговый сценарий: новый проект с Poetry.** 1) `poetry init` (интерактивно) или создать pyproject.toml вручную с [tool.poetry]. 2) `poetry add requests` — добавить зависимость и установить. 3) `poetry add -D pytest mypy` — dev-зависимости. 4) Писать код и тесты. 5) `poetry run pytest` или `poetry shell` и затем `pytest`. 6) Перед коммитом убедиться, что poetry.lock закоммичен. В CI: `poetry install --no-root` (или `poetry install`) и `poetry run pytest`.

**Запомните:** Poetry даёт воспроизводимые окружения через poetry.lock; зависимости и скрипты хранятся в pyproject.toml; для запуска кода в окружении используйте `poetry run` или `poetry shell`.

---

### uv

**uv** — быстрый менеджер пакетов и виртуальных окружений (реализован на Rust, от Astral — тех же авторов Ruff). Совместим с pip и pyproject.toml: понимает requirements.txt, pyproject.toml, может заменять pip и venv в рабочих процессах.

**Установка:** `curl -LsSf https://astral.sh/uv/install.sh | sh` (Unix) или через pip: `pip install uv`.

**Основные команды:**

| Команда | Назначение |
|---------|------------|
| `uv venv` | Создать виртуальное окружение в текущем каталоге (.venv по умолчанию). |
| `uv pip install -r requirements.txt` | Установить зависимости из requirements.txt в текущее окружение (быстрее pip). |
| `uv pip install .` | Установить текущий проект (из pyproject.toml). |
| `uv pip compile pyproject.toml -o requirements.txt` | Сгенерировать lock-подобный requirements.txt из pyproject.toml. |
| `uv run python script.py` | Создать venv при необходимости и запустить скрипт в нём. |
| `uv run pytest` | Запустить pytest в окружении проекта. |

**Практика:** в CI и локально можно заменить `pip install -r requirements.txt` на `uv pip install -r requirements.txt` для ускорения; для новых проектов можно использовать `uv pip compile` вместо pip-tools. uv не заменяет Poetry (нет своего lock-формата и UI), но дополняет или заменяет pip/venv.

**Пошаговый сценарий с uv (без Poetry):** 1) Создать venv: `uv venv` (по умолчанию .venv). 2) Активировать: `source .venv/bin/activate` (Unix). 3) Установить зависимости: `uv pip install -r requirements.txt` (быстрее pip) или при наличии pyproject.toml: `uv pip install -e .`. 4) Сгенерировать lock-подобный requirements.txt из pyproject.toml: `uv pip compile pyproject.toml -o requirements.txt`. 5) Запуск без активации: `uv run pytest` — uv создаст venv при необходимости и запустит pytest в нём.

---

### pipx

**pipx** устанавливает CLI-приложения (пакеты с **console_scripts** в entry points) в **отдельные виртуальные окружения** и добавляет только бинары в PATH. Таким образом, black, ruff, pytest, mypy и т.д. не засоряют один общий venv и не конфликтуют друг с другом по версиям.

**Установка:** `pip install pipx` (желательно в изолированном окружении или через ensurepath: `pipx ensurepath` — добавить каталог с бинарами в PATH).

**Основные команды:**

| Команда | Назначение |
|---------|------------|
| `pipx install black` | Установить black в отдельное окружение и добавить команду black в PATH. |
| `pipx install --force black` | Переустановить black. |
| `pipx run black .` | Запустить black без установки (временное окружение, затем удаление). |
| `pipx run --spec "ruff>=0.1" ruff check .` | Запустить конкретную версию ruff без установки. |
| `pipx inject black colorama` | Добавить пакет в окружение уже установленного black. |
| `pipx list` | Список установленных приложений и их окружений. |
| `pipx uninstall black` | Удалить black и его окружение. |

**Когда использовать:** для глобальных CLI-инструментов (форматтеры, линтеры, утилиты), которые нужны в любом проекте. Для зависимостей конкретного проекта по-прежнему используют venv + pip или Poetry.

---

### conda и mamba

**conda** — менеджер пакетов и окружений от Anaconda. Управляет не только Python-пакетами, но и бинарными пакетами (компиляторы, библиотеки C), поэтому часто используется в data science и научном стеке, где нужны NumPy, SciPy, PyTorch и т.д. в виде готовых бинарников.

**Основные команды conda:**

| Команда | Назначение |
|---------|------------|
| `conda create -n myenv python=3.11` | Создать окружение с именем myenv и Python 3.11. |
| `conda activate myenv` | Активировать окружение (в Windows: `activate myenv` в cmd). |
| `conda deactivate` | Деактивировать. |
| `conda install numpy pandas` | Установить пакеты в активное окружение. |
| `conda install -c conda-forge package` | Установить из канала conda-forge. |
| `conda env export > environment.yml` | Экспорт окружения в файл (аналог requirements.txt). |
| `conda env create -f environment.yml` | Создать окружение из файла. |
| `conda list` | Список установленных пакетов. |

**Каналы:** по умолчанию используются репозитории Anaconda; **conda-forge** — сообщественный канал с большим числом пакетов. Установка из другого канала: `-c conda-forge`. Приоритет каналов задаётся в `~/.condarc` или в `conda config --add channels conda-forge`.

**environment.yml** — аналог requirements.txt для conda: описание окружения в YAML. Пример:

```yaml
name: myenv
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy>=1.24
  - pip
  - pip:
    - requests>=2.28
```

Создание окружения из файла: `conda env create -f environment.yml`. Экспорт текущего окружения: `conda env export > environment.yml` (точные версии всех пакетов, включая транзитивные — максимальная воспроизводимость) или **`conda env export --from-history`** (только пакеты, которые вы явно устанавливали; транзитивные не включаются — файл короче и проще править вручную; при создании окружения из такого файла conda сам разрешит зависимости). Для CI обычно используют полный экспорт без --from-history.

#### Продвинутые темы: каналы, pinning и locking

**.condarc и приоритет каналов.** Глобальная конфигурация conda хранится в файле **`~/.condarc`** (или в системном аналоге). В нём можно задать:

```yaml
channels:
  - conda-forge
  - defaults
channel_priority: strict
```

- **channels** — порядок каналов (conda-forge, затем defaults).
- **channel_priority=strict** — пакеты предпочитаются из канала, идущего раньше; это уменьшает «мешанину» версий из разных каналов.

**Pinning версий (конкретные версии и диапазоны).** В **environment.yml** можно задавать не только `python=3.11`, но и более жёсткие ограничения: `numpy=1.26.*`, `pandas>=2,<3`. Внутренний механизм pinning (файл `conda-meta/pinned`) чаще нужен в «системных» окружениях; в проектах обычно достаточно явных версий в dependencies. Для «жёсткой заморозки» окружения используют environment-lock файлы.

**environment locking и conda-lock.** Инструмент **conda-lock** генерирует lock-файлы с точными версиями пакетов для разных платформ (linux-64, win-64, osx-64 и т.д.), аналогично poetry.lock или requirements.txt от pip-tools.

Типичный workflow:

1. Установить conda-lock (в базовое окружение или отдельное): `conda install -c conda-forge conda-lock` или `pip install conda-lock`.
2. Иметь базовый **environment.yml** (как выше).
3. Сгенерировать lock-файлы:

   ```bash
   conda-lock -f environment.yml -p linux-64 -p win-64 -p osx-64
   ```

   В результате появятся файлы вида `conda-lock.yml` или по одному файлу на платформу (в зависимости от версии conda-lock).

4. Создать окружение по lock-файлу:

   ```bash
   conda-lock install -n myenv conda-lock.yml
   ```

   или с указанием платформы/файла: `conda-lock install -n myenv conda-linux-64.lock`.

**Когда использовать conda-lock:** если проект должен воспроизводимо собираться на разных платформах (CI на Linux, разработка на macOS, деплой на Windows), и важна точная фиксация версий conda‑пакетов. Для простых сценариев внутри одной платформы часто достаточно обычного environment.yml.

**mamba** — замена консольного клиента conda (тот же CLI), написанная на C++; разрешение зависимостей и установка значительно быстрее. Установка: `conda install mamba`; затем вместо `conda install` можно вызывать `mamba install`.

---

### pyenv и asdf

**pyenv** — менеджер **версий Python**: установка нескольких интерпретаторов (3.9, 3.10, 3.11, 3.12 и т.д.) и переключение между ними глобально или по каталогу.

**Установка:** см. официальную документацию (curl-скрипт или git clone); после установки нужно добавить инициализацию в shell (eval "$(pyenv init -)" и т.д.).

**Основные команды:**

| Команда | Назначение |
|---------|------------|
| `pyenv install --list` | Список доступных версий для установки. |
| `pyenv install 3.12.0` | Установить Python 3.12.0. |
| `pyenv global 3.12.0` | Установить версию по умолчанию для всей системы. |
| `pyenv local 3.12.0` | Установить версию для текущего каталога (создаётся файл .python-version). |
| `pyenv version` | Текущая активная версия. |
| `pyenv versions` | Список установленных версий. |
| `pyenv which python` | Путь к исполняемому файлу python для текущей версии. |

При входе в каталог с файлом **.python-version** pyenv автоматически подставляет указанную там версию (если настроен shell hook). Это удобно для проектов с разными требованиями к версии Python.

**Как работает pyenv (shims):** pyenv создаёт каталог **shims** (прокси для команд python, pip и т.д.). При вызове `python` выполняется shim, который смотрит на текущую директорию (и на .python-version, если есть) и запускает реальный интерпретатор выбранной версии. Команда **`pyenv rehash`** обновляет shims после установки новой версии Python или после установки исполняемых файлов в окружения (например, после `pip install` в одном из окружений). Обычно rehash вызывается автоматически; при сбоях — вызвать вручную.

**asdf** — универсальный менеджер версий (Ruby, Node, Python, Go и др.). Для Python используется плагин **asdf-python**; команды похожи: `asdf install python 3.12.0`, `asdf local python 3.12.0` (создаётся файл .tool-versions). Выбор между pyenv и asdf часто сводится к тому, нужен ли только Python или несколько языков в одном инструменте.

#### Граничные случаи и отладка (§30)

| Ситуация | Что проверить | Решение |
|----------|----------------|---------|
| poetry install падает с конфликтом зависимостей | Ограничения в [tool.poetry.dependencies] несовместимы. | Ослабить ограничения версий или обновить lock: `poetry update`; при необходимости удалить poetry.lock и выполнить `poetry lock` заново. |
| poetry run не находит команду | Окружение не создано или пакет не установлен. | Выполнить `poetry install`; проверить `poetry env info` (путь к venv). |
| pipx: команда не в PATH | Каталог с бинарами pipx не в PATH. | Выполнить `pipx ensurepath` и перезапустить терминал; или добавить в PATH вручную (pipx dir показывает каталог). |
| conda activate не работает в shell | Инициализация conda не добавлена в .bashrc/.zshrc. | Выполнить `conda init bash` или `conda init zsh`, перезапустить терминал. |
| pyenv: python всё ещё системный | Shims не в начале PATH или shell hook не загружен. | Проверить `pyenv which python`; в .bashrc/.zshrc добавить eval "$(pyenv init -)" и перезапустить shell. |
| uv pip install в CI падает | Окружение не активировано или путь к venv не задан. | Создать venv: `uv venv`, активировать или указать путь: `uv pip install --python .venv/bin/python -r requirements.txt`. |

#### Частые вопросы (§30)

| Вопрос | Краткий ответ |
|--------|----------------|
| Нужно ли коммитить poetry.lock? | Да. Lock фиксирует версии для воспроизводимости; все разработчики и CI используют один и тот же lock. |
| Чем uv отличается от pip? | uv написан на Rust, быстрее pip; понимает pyproject.toml и requirements.txt; может создавать venv и компилировать зависимости (uv pip compile). |
| Когда использовать conda вместо pip/venv? | Когда нужны бинарные пакеты (NumPy, SciPy, PyTorch) из репозиториев conda или несколько версий Python в одном менеджере; для обычных PyPI-пакетов достаточно venv + pip. |
| pipx vs pip install --user? | pipx ставит каждое приложение в отдельное venv и не засоряет пользовательский site-packages; изоляция и отсутствие конфликтов версий. |

**Запомните:** Poetry — зависимости + lock в одном инструменте; uv — быстрый pip/venv; pipx — CLI-инструменты без глобального venv; conda — data science и бинарные пакеты; pyenv/asdf — несколько версий интерпретатора в системе.

---

## §31. Линтеры и форматтеры
