[← Назад к индексу части VIII](index.md)

# Часть VIII. Инструменты и экосистема

> **Цель:** уверенно использовать виртуальные окружения, упаковку и метаданные (venv, pyproject.toml, wheel, sdist), менеджеры зависимостей и версий Python (Poetry, uv, pipx, conda, pyenv), линтеры и форматтеры (Ruff, Black, isort), проверку типов (mypy, pyright), тестирование (unittest, pytest, hypothesis) и документацию (docstrings, Sphinx); понимать PEP 668, pre-commit и практику современной экосистемы Python.

**Краткая шпаргалка (суть):**

| Область | Ключевые инструменты / концепции | Назначение |
|--------|----------------------------------|------------|
| Виртуальные окружения | `venv`, PEP 668, `pip`, `pip-tools`, `ensurepip`, `zipapp` | Изоляция зависимостей проекта от системы |
| Метаданные и сборка | `pyproject.toml`, [build-system], [project], wheel, sdist, `build`, `twine` | Описание проекта и публикация на PyPI |
| Упаковка углублённо | editable install, entry points, MANIFEST.in, src layout, py.typed | Режим разработки, плагины, типизация пакетов |
| Менеджеры | Poetry, uv, pipx, conda, pyenv | Зависимости, lock-файлы, CLI-инструменты, версии Python |
| Стиль и линтинг | Ruff, Pylint, Black, isort, pre-commit | Единый стиль и раннее обнаружение ошибок |
| Типы | mypy, pyright, typing_extensions | Статическая проверка типов и совместимость |
| Тесты | unittest, pytest, hypothesis, mutation testing | Юнит-тесты, фикстуры, property-based, качество тестов |
| Документация | docstrings (PEP 257), Sphinx, MkDocs | Описание API и генерация документации |

---

## Маршрут изучения

**Что вы изучите и в каком порядке.** Сначала — **виртуальные окружения** (§28): создание и активация venv, **PEP 668** (externally managed environment), pip и pip-tools, ensurepip, zipapp. Затем — **метаданные и сборка** (§29, §29a): pyproject.toml ([build-system], [project], зависимости), форматы wheel и sdist, команда build, twine, editable install, entry points, MANIFEST.in, src layout и py.typed. Далее — **менеджеры зависимостей и окружений** (§30): Poetry, uv, pipx, conda, pyenv. После этого — **линтеры и форматтеры** (§31, §31a): Ruff, Pylint, Black, isort, конфигурация в pyproject.toml и **pre-commit**. Затем — **проверка типов** (§32): mypy, pyright, typing_extensions. Потом — **тестирование** (§33, §33a): unittest, pytest (фикстуры, параметризация), hypothesis (property-based), mutation testing, test doubles. В конце — **документация** (§34): docstrings (PEP 257), Sphinx, type hints в docstrings. Справочник в конце части — для повторения и самопроверки.

**Что желательно знать заранее:** базовый Python (модули, импорт, пути), командная строка (Unix/Windows). Полезны Часть I (отличия Py3) и опыт установки пакетов через pip.

---

## Структура материала (что в какой группе)

| Группа | О чём раздел | Зачем это изучать |
|--------|--------------|--------------------|
| **§28 Виртуальные окружения** | venv, PEP 668, pip, pip-tools, ensurepip, zipapp | Изолировать зависимости проекта и не ломать системный Python |
| **§29 pyproject.toml** | [build-system], [project], зависимости, версионирование PEP 440 | Единый конфиг проекта и сборки (PEP 517/518/621) |
| **§29a Упаковка** | wheel, sdist, build, twine, editable, entry points, MANIFEST.in, src layout, py.typed | Собирать и публиковать пакеты, расширять приложения плагинами |
| **§30 Менеджеры** | Poetry, uv, pipx, conda, pyenv | Удобные зависимости, lock-файлы, CLI-инструменты, несколько версий Python |
| **§31 Линтеры и форматтеры** | Ruff, Pylint, Black, isort; §31a pre-commit | Единый стиль и автоматические проверки перед коммитом |
| **§32 Проверка типов** | mypy, pyright, typing_extensions | Статический анализ типов и совместимость со старыми версиями |
| **§33–33a Тестирование** | unittest, pytest, hypothesis, mutation testing, test doubles | Надёжные тесты и проверка качества тестового набора |
| **§34 Документация** | docstrings PEP 257, Sphinx, MkDocs | Описание API и генерация документации |
| **Справочник** | Сценарии, терминология, вопросы, резюме | Повторение и самопроверка |

**Связь с планом:** Часть VIII — **Шаг 5 (Инструменты)** глобального плана. Смежная тема — Часть IX (миграция Py2→Py3: 2to3, six, future).

---

## Как устроены разделы и оглавление

В каждом разделе материал идёт по шаблону: **цель** (что вы освоите) → **термины** (с кратким определением) → **правила и синтаксис** → **примеры** (код и конфиги) → **граничные случаи** → блок **«Запомните»**. Термины (venv, wheel, entry point, strict mode и т.д.) в тексте сохранены и в начале раздела расшифрованы. Оглавление сгруппировано по этапам; справочник в конце — для повторения.

---

## Оглавление

### Этап 1. Окружения и метаданные (§28–29)

| Раздел | Содержание | Ключевые понятия |
|--------|------------|------------------|
| [§28 Виртуальные окружения](01_28_virtualnye_okruzheniya.md#28-виртуальные-окружения) | venv, PEP 668, pip, pip-tools, ensurepip, zipapp | Виртуальное окружение, externally managed, pip freeze |
| [§29 pyproject.toml](02_29_pyproject_toml.md#29-pyprojecttoml) | [build-system], [project], dependencies, PEP 440 | pyproject.toml, PEP 517/518/621 |

### Этап 2. Упаковка и менеджеры (§29a, §30)

| Раздел | Содержание | Ключевые понятия |
|--------|------------|------------------|
| [§29a Упаковка](03_29a_upakovka.md#29a-упаковка-packaging) | wheel, sdist, build, twine, editable, entry points, src layout, py.typed | Wheel, sdist, editable install, entry point, src layout, py.typed |
| [§30 Менеджеры зависимостей](04_30_menedzhery_zavisimostej.md#30-менеджеры-зависимостей-и-окружений) | Poetry, uv, pipx, conda, pyenv | poetry.lock, pipx, conda env, pyenv local |

### Этап 3. Качество кода: линтинг и типы (§31–32)

| Раздел | Содержание | Ключевые понятия |
|--------|------------|------------------|
| [§31 Линтеры и форматтеры](05_31_lintery_i_formattery.md#31-линтеры-и-форматтеры) | Ruff, Pylint, Black, isort | Линтер, форматтер, Ruff rules |
| [§31a pre-commit](05_31_lintery_i_formattery.md#31a-конфигурация-и-pre-commit) | Конфиг инструментов, pre-commit хуки | pre-commit, .pre-commit-config.yaml |
| [§32 Проверка типов](06_32_proverka_tipov.md#32-проверка-типов) | mypy, pyright, typing_extensions | Статическая проверка типов, strict mode, stubs |

### Этап 4. Тестирование и документация (§33–34)

| Раздел | Содержание | Ключевые понятия |
|--------|------------|------------------|
| [§33 Тестирование](07_33_testirovanie.md#33-тестирование) | unittest, pytest, фикстуры, параметризация, mocking, coverage | TestCase, pytest.fixture, parametrize, pytest-cov |
| [§33a Тестирование углублённо](07_33_testirovanie.md#33a-тестирование-углублённо) | doctest, hypothesis, mutation testing, test doubles | Property-based testing, mutation testing, Stub/Mock/Fake |
| [§34 Документация](08_34_dokumentaciya.md#34-документация-и-документационные-строки) | docstrings PEP 257, Sphinx, MkDocs | docstring, autodoc, reStructuredText |

### Этап 5. Справочник и проверка

| Раздел | Назначение |
|--------|------------|
| [Частые сценарии](09_spravochnik_voprosy_i_testy.md#частые-сценарии-часть-viii) | Задача → решение |
| [Терминология](09_spravochnik_voprosy_i_testy.md#краткое-повторение-терминологии) | Словарь терминов |
| [Вопросы по теме](09_spravochnik_voprosy_i_testy.md#вопросы-по-теме-с-ответами) | Самопроверка |
| [Резюме](09_spravochnik_voprosy_i_testy.md#резюме-по-части-viii) | Сводка части |

---

## Как изучать эту часть (уровни)
