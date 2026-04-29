[← Назад к индексу части VIII](index.md)


**Цель раздела:** понимать назначение **pyproject.toml** как единого конфигурационного файла проекта (PEP 517, 518, 621), знать секции **[build-system]** и **[project]**, задание зависимостей и опциональных зависимостей, связь с setuptools/flit/hatch и версионирование по PEP 440.

---

### Термины

| Термин | Определение |
|--------|-------------|
| **pyproject.toml** | Файл конфигурации проекта в формате TOML; стандартизирован PEP 517/518 (сборка) и PEP 621 (метаданные проекта); один файл вместо только setup.py/setup.cfg. |
| **[build-system]** | Секция, указывающая, какой бэкенд использовать для сборки пакета (setuptools, flit, hatch и т.д.) и его версию. |
| **[project]** | Секция с метаданными проекта: имя, версия, описание, зависимости, опциональные зависимости, точки входа и т.д. (PEP 621). |
| **PEP 440** | Спецификация версий пакетов: допустимые форматы (например, 1.2.3, 1.0a1, 2.0.post1), сравнение версий; используется pip и инструментами сборки. |

---

### Зачем pyproject.toml

Раньше метаданные и сборка задавались в **setup.py** (и частично в **setup.cfg**). Недостатки: setup.py — исполняемый код (риск при установке чужого пакета), разброс конфигов. **PEP 517** и **PEP 518** вводят единый файл **pyproject.toml** для указания бэкенда сборки; **PEP 621** переносит туда метаданные проекта (имя, версия, зависимости). Итог: один файл для и инструментов сборки, и для метаданных; инструменты (pip, build, twine) читают его без выполнения произвольного кода.

---

### Секция [build-system]

Указывает, чем собирать пакет:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"
```

- **requires** — зависимости, нужные только на этапе сборки (например, setuptools, wheel).
- **build-backend** — точка входа бэкенда (модуль и объект). Альтернативы: `flit_core.buildapi`, `hatchling.build` и др.

Без этой секции современные инструменты (pip, build) не знают, как строить пакет из исходников, и установка из sdist или из локального каталога с pyproject.toml может завершиться ошибкой.

**Как вызывается бэкенд (PEP 517, кратко):** при установке из sdist или `pip install .` инструмент (pip или build) читает [build-system], создаёт изолированное окружение (если не указано --no-build-isolation), устанавливает туда зависимости из `requires`, затем импортирует объект, указанный в `build-backend`, и вызывает у него методы `build_wheel` или `build_sdist` с путём к исходникам. Бэкенд возвращает путь к собранному артефакту; pip затем устанавливает wheel в site-packages. Таким образом, **код сборки выполняется в изолированном окружении** и не может произвольно менять систему.

**Популярные бэкенды:**

| build-backend | Назначение |
|---------------|------------|
| `setuptools.build_meta` | Классический бэкенд; конфиг через pyproject.toml [tool.setuptools], setup.cfg или setup.py. |
| `flit_core.buildapi` | Минималистичный бэкенд; метаданные и список файлов только в pyproject.toml. |
| `hatchling.build` | Бэкенд от Hatch; конфиг в [tool.hatch]. |

**Конфигурация setuptools в pyproject.toml (кратко):** при использовании `setuptools.build_meta` пакеты и опции задают в **[tool.setuptools]** и **[tool.setuptools.packages.find]**:

```toml
[tool.setuptools.packages.find]
where = ["src"]
include = ["mypkg*"]

[tool.setuptools.package-dir]
"" = "src"
```

Для динамической версии (например, из git tag) используют плагин **setuptools-scm**: в [project] указывают `dynamic = ["version"]`, в [tool.setuptools.dynamic] — `version = {attr = "mypkg.__version__"}` или через setuptools_scm. Тогда версия берётся из тега git при сборке.

---

### Секция [project]

Метаданные проекта по PEP 621 задаются в секции **[project]**. Ниже — полный перечень основных полей и их назначение.

**Обязательные (для публикации на PyPI) и часто используемые:**

```toml
[project]
name = "my-package"
version = "1.0.0"
description = "Short description"
readme = "README.md"
requires-python = ">=3.9"
license = { text = "MIT" }
authors = [{ name = "Author", email = "a@b.com" }]
keywords = ["cli", "tools"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
urls = { Homepage = "https://example.com", Repository = "https://github.com/user/repo" }
dependencies = [
    "requests>=2.28",
    "typing-extensions>=4.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "mypy>=1.0",
]
docs = ["sphinx>=5.0"]
```

**Классификаторы (classifiers):** полный список — на pypi.org/classifiers. Часто указывают: **Development Status** (3 — Alpha, 4 — Beta, 5 — Production/Stable), **Intended Audience**, **License**, **Programming Language :: Python :: 3.x** для каждой поддерживаемой версии, **Topic** (опционально). Классификаторы помогают пользователям находить пакет и понимать совместимость с версией Python.

**Краткое назначение полей:**

| Поле | Назначение |
|------|------------|
| **name** | Имя пакета на PyPI: только буквы, цифры, дефисы и подчёркивания; при загрузке на PyPI нормализуется (например, подчёркивания в дефисы). |
| **version** | Версия по PEP 440; используется pip и инструментами сборки для сравнения. |
| **description** | Краткое описание (одна строка); отображается в списках пакетов. |
| **readme** | Файл с длинным описанием (README.md или README.rst); отображается на странице пакета на PyPI. Можно задать как строку: `readme = "README.md"` или с типом контента: `readme = { file = "README.md", content-type = "text/markdown" }` (content-type помогает PyPI корректно отобразить разметку). |
| **requires-python** | Ограничение версий Python, например `>=3.9`, `>=3.9,<3.13`; pip не установит пакет в неподходящую версию. |
| **license** | Лицензия: `{ text = "MIT" }` или `{ file = "LICENSE" }`. |
| **authors** | Список авторов: `{ name = "...", email = "..." }`. |
| **keywords** | Ключевые слова для поиска на PyPI. |
| **classifiers** | Тропы (тропы) PyPI: статус разработки, аудитория, лицензия, версии Python и т.д.; полный список на pypi.org/classifiers. |
| **urls** | Словарь ссылок: Homepage, Documentation, Repository, Changelog и т.д. |
| **dependencies** | Список зависимостей при установке пакета; синтаксис по PEP 508 (имя, операторы сравнения версий). |
| **optional-dependencies** | Группы доп. зависимостей; установка: `pip install .[dev]`, `pip install .[dev,docs]`. |

**Динамические поля (dynamic):** если версию или другие поля задаёт инструмент (например, из git tag), их перечисляют в **dynamic** и не указывают статически в [project]:

```toml
[project]
name = "my-package"
dynamic = ["version"]
# version задаётся через [tool.setuptools.dynamic] или плагин
```

Дополнительно в [project] задают **scripts** (устаревший способ консольных команд) и **entry points** (см. §29a); для современного способа консольных команд и плагинов используется **[project.scripts]** и **[project.entry-points.***]**.

---

### Версионирование (PEP 440)

Версии пакетов в Python задаются по **PEP 440** («Version Identification and Dependency Specification»). Формат позволяет однозначно сравнивать версии и задавать ограничения в зависимостях.

**Примеры допустимых версий:**

| Формат | Пример | Назначение |
|--------|--------|------------|
| Final release | `1.0.0`, `2.1.3` | Обычный релиз. |
| Alpha | `1.0a1`, `1.0a2` | Ранняя разработка. |
| Beta | `1.0b1`, `1.0b2` | Бета-релиз. |
| Release candidate | `1.0rc1` | Кандидат в релиз. |
| Post-release | `1.0.post1` | Исправление после релиза (без изменения основного номера). |
| Dev release | `1.0.dev1` | Снимок разработки. |
| Local version | `1.0.0+local` | Локальный суффикс (не для PyPI). |

Порядок сравнения: например, `1.0a1` < `1.0b1` < `1.0rc1` < `1.0` < `1.0.post1` < `1.0.1`.

**Операторы в зависимостях (PEP 508):**

| Оператор | Пример | Значение |
|----------|--------|----------|
| `==` | `requests==2.28.0` | Ровно эта версия. |
| `!=` | `requests!=2.25.0` | Любая версия, кроме указанной. |
| `<=`, `>=`, `<`, `>` | `requests>=2.28,<3` | Диапазон версий. |
| `~=` | `requests~=2.28` | Совместимый релиз: `>=2.28, <2.29` (для 2.28.x); для 2.28 — то же, что `>=2.28, <3`. |

Несколько ограничений через запятую означают **И** (все должны выполняться): `requests>=2.28,<3` — версия от 2.28 включительно и строго меньше 3.

#### Связь с PEP 517, 518, 621

- **PEP 517** («A build-system independent format for Python packages») — определяет интерфейс сборки: как инструмент (pip, build) вызывает бэкенд (setuptools, flit и т.д.) для сборки wheel/sdist. Бэкенд указывается в [build-system].
- **PEP 518** («Specifying Minimum Build System Requirements for Python Projects») — вводит pyproject.toml и секцию [build-system] с полем `requires` (зависимости для сборки).
- **PEP 621** («Storing project metadata in pyproject.toml») — переносит метаданные проекта (имя, версия, зависимости, авторы и т.д.) в [project] вместо только setup.py/setup.cfg.

Итог: один файл pyproject.toml служит и для сборки, и для метаданных; инструменты читают его без выполнения произвольного кода из setup.py, что безопаснее и предсказуемее.

#### Граничные случаи и отладка (§29)

| Ситуация | Что проверить | Решение |
|----------|----------------|---------|
| pip install . падает: «No matching distribution» | requires-python, версия Python в окружении. | Убедиться, что версия Python удовлетворяет requires-python (например, `>=3.9`); проверить `python --version`. |
| build падает с ошибкой импорта бэкенда | [build-system] requires, версии setuptools/wheel. | Установить зависимости сборки: `pip install setuptools wheel build`; проверить версии в requires. |
| Имя пакета отклонено PyPI | Допустимы буквы, цифры, дефисы, подчёркивания. | Убрать точки и спецсимволы; подчёркивания при публикации заменяются на дефисы. |
| dynamic = ["version"] — версия не подставляется | Плагин setuptools-scm или атрибут в коде. | Установить setuptools-scm; в [tool.setuptools.dynamic] задать version; при использовании attr — атрибут должен быть в коде пакета. |
| Опциональные зависимости не подтягиваются | Синтаксис [project.optional-dependencies], имя группы. | Установить явно: `pip install .[dev,docs]`; имена групп — без пробелов. |

#### Частые вопросы (§29)

| Вопрос | Краткий ответ |
|--------|----------------|
| Где указывать зависимости для разработки (pytest, mypy)? | В [project.optional-dependencies], например группа dev; установка: `pip install .[dev]`. |
| Можно ли не указывать version в [project]? | Да, если указать dynamic = ["version"] и задать версию через плагин (setuptools-scm) или [tool.setuptools.dynamic]. |
| Чем flit/hatch отличаются от setuptools? | Flit и Hatch — минималистичные бэкенды; конфиг только в pyproject.toml; setuptools поддерживает setup.py, setup.cfg и сложные сценарии (C-расширения, плагины). |
| Нужен ли setup.py при использовании pyproject.toml? | Нет; для современного проекта достаточно pyproject.toml с [build-system] и [project]. setup.py оставляют только для legacy или особой логики. |

**Запомните:** pyproject.toml — единая точка правды для сборки ([build-system]) и метаданных ([project]); зависимости и опциональные группы задаются в [project]; версии — по PEP 440.

---

## §29a. Упаковка (packaging)
