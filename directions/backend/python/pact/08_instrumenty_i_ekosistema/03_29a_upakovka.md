[← Назад к индексу части VIII](index.md)


**Цель раздела:** различать форматы **wheel** и **sdist**, собирать пакет командой **build**, публиковать через **twine**, использовать **editable install**, настраивать **entry points** (в т.ч. console_scripts), знать **MANIFEST.in**, **src layout** и маркер **py.typed** для типизированных пакетов.

---

### Термины

| Термин | Определение |
|--------|-------------|
| **wheel (.whl)** | Бинарный (или универсальный) формат распространения пакета; установка из wheel быстрая, без этапа сборки. |
| **sdist** | Source distribution — архив исходников (.tar.gz или .zip); при установке из sdist pip запускает бэкенд сборки и может собирать wheel на лету. |
| **build** | Стандартная команда `python -m build` для сборки wheel и sdist по pyproject.toml (PEP 517). |
| **twine** | Утилита для загрузки собранных артефактов на PyPI (проверка перед загрузкой). |
| **Editable install** | Установка пакета в режиме разработки: импорт идёт из исходников в репозитории, правки сразу видны без переустановки. |
| **Entry point** | Точка входа, объявленная в метаданных пакета; используется для консольных команд (console_scripts) и плагинов; discovery через importlib.metadata.entry_points(). |
| **src layout** | Структура проекта, в которой код пакета лежит в подкаталоге `src/`; изоляция от тестов и скриптов в корне, корректное поведение editable. |
| **py.typed** | Маркер PEP 561: пустой файл `package_name/py.typed` сообщает типам (mypy, pyright), что пакет поддерживает типизацию и предоставляет стабы/аннотации. |

---

### Форматы: wheel и sdist

**Wheel (.whl)** — это ZIP-архив с **фиксированной структурой** каталогов, соответствующей layout в site-packages. При установке pip распаковывает архив в site-packages; компиляции и запуска кода сборки нет. Поэтому установка из wheel **быстрая** и **предсказуемая**.

- **Универсальный wheel** (`py3-none-any.whl`) — подходит для любого Python 3 и любой платформы; так собирают пакеты без C-расширений.
- **Платформо-специфичный wheel** (`cp311-cp311-linux_x86_64.whl`) — содержит скомпилированные расширения под конкретную версию Python и ОС; pip выбирает подходящий wheel при установке.

**Имя файла wheel (формат):** `{distribution}-{version}-{python tag}-{abi tag}-{platform tag}.whl`. Примеры: `mypkg-1.0.0-py3-none-any.whl` (универсальный: py3, none, any); `mypkg-1.0.0-cp311-cp311-win_amd64.whl` (Python 3.11, Windows x64). **python tag** — версия Python (py3, cp311); **abi tag** — ABI (none для чистого Python, cp311 для CPython 3.11); **platform tag** — ОС и архитектура (any, linux_x86_64, win_amd64, macosx_10_9_x86_64). Pip при установке выбирает wheel, совместимый с текущим интерпретатором и платформой.

**sdist (source distribution)** — архив исходников (обычно `.tar.gz` или `.zip`). В него входят файлы, перечисленные в MANIFEST.in (или по умолчанию бэкенда). При установке **из sdist** pip не может просто распаковать архив: он вызывает **бэкенд сборки** из [build-system] (например, setuptools), который собирает wheel (или напрямую устанавливает файлы). То есть установка из sdist **требует** этапа сборки и может зависеть от окружения (компилятор, заголовки и т.д.). sdist нужен, когда пользователь ставит пакет из исходников (например, нет подходящего wheel для его платформы) или когда вы публикуете пакет на PyPI (PyPI принимает и wheel, и sdist).

**Когда pip выбирает wheel, а когда sdist:** при `pip install my-package` pip сначала ищет подходящий wheel в индексе; если находит — ставит из wheel. Если подходящего wheel нет (например, пакет только в sdist или платформа не совпадает), pip скачивает sdist и запускает сборку через бэкенд из [build-system].

**Сборка (команда build):**

В каталоге проекта с pyproject.toml:

```bash
pip install build
python -m build
```

По умолчанию создаются **и** sdist, **и** wheel. Результат попадает в каталог **`dist/`**: например, `my_package-1.0.0.tar.gz` (sdist) и `my_package-1.0.0-py3-none-any.whl` (wheel).

**Опции build:**

| Опция | Назначение |
|-------|------------|
| `python -m build --sdist` | Собрать только sdist. |
| `python -m build --wheel` | Собрать только wheel. |
| `python -m build --outdir output/` | Положить артефакты в указанный каталог вместо `dist/`. |
| `python -m build --no-isolation` | Сборка в текущем окружении (использовать уже установленные зависимости сборки); быстрее, но менее изолированно. |

**Когда использовать --no-isolation:** по умолчанию `python -m build` создаёт изолированное окружение и ставит туда только зависимости из [build-system] requires — воспроизводимость максимальна. С `--no-isolation` сборка идёт в текущем venv; удобно, если setuptools/wheel уже установлены и нужно ускорить повторную сборку. В CI обычно используют изоляцию по умолчанию.

---

### Twine — загрузка на PyPI

**Twine** — утилита для **загрузки** собранных артефактов (wheel и sdist) на PyPI (или другой индекс). Рекомендуется использовать twine вместо устаревшего `python setup.py upload`, так как twine загружает по HTTPS и проверяет артефакты перед отправкой.

**Проверка артефактов перед загрузкой:**

```bash
pip install twine
twine check dist/*
```

Проверяется соответствие метаданных (имя, версия, описание и т.д.) стандартам; при ошибках загрузка на PyPI может быть отклонена, поэтому проверку делают всегда.

**Загрузка на PyPI:**

```bash
twine upload dist/*
```

Требуется **учётная запись PyPI** и **API-токен** (создаётся в настройках аккаунта на pypi.org: Account settings → API tokens → Add API token). Twine запросит имя пользователя и пароль; в качестве пароля указывают **токен** (не пароль от аккаунта). Можно задать учётные данные через переменные окружения: **TWINE_USERNAME** и **TWINE_PASSWORD** (в CI удобно задавать секретами); или через конфиг **~/.pypirc**:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-...

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-...
```

Для PyPI в качестве username указывают `__token__`, в password — токен с префиксом `pypi-`. Тогда `twine upload dist/*` не будет запрашивать ввод. Файл .pypirc не коммитят в репозиторий (добавить в .gitignore).

**Загрузка на Test PyPI** (тестовый индекс для проверки перед публикацией):

```bash
twine upload --repository testpypi dist/*
```

Учётная запись на test.pypi.org отдельная; установка с Test PyPI: `pip install --index-url https://test.pypi.org/simple/ my-package`.

**Опции twine upload:**

| Опция | Назначение |
|-------|------------|
| `--repository pypi` | Репозиторий по умолчанию (PyPI). |
| `--repository testpypi` | Test PyPI. |
| `--skip-existing` | Не перезаписывать уже загруженные версии (удобно при повторной загрузке того же dist/). |
| `--verbose` | Подробный вывод. |

**Типичные ошибки twine и что делать:**

| Ошибка / сообщение | Причина | Решение |
|--------------------|---------|---------|
| `400 Invalid or non-existent authentication` | Неверный токен или username не `__token__`. | В .pypirc: username = `__token__`, password = токен с префиксом `pypi-`; проверить TWINE_USERNAME и TWINE_PASSWORD в CI. |
| `403 Forbidden` / `Invalid credentials` | Токен отозван или нет прав на пакет. | Создать новый API-токен на pypi.org; для организации проверить права на пакет. |
| `File already exists` | Версия уже загружена на PyPI (версии неизменяемы). | Увеличить версию в pyproject.toml, пересобрать (`python -m build`), загрузить заново; или использовать `--skip-existing` для уже загруженных файлов. |
| `twine check` ругается на long_description | README не найден или не в UTF-8. | Указать в [project] readme = "README.md" (или readme = {file = "README.md", content-type = "text/markdown"}); проверить кодировку файла. |

**Загрузка в приватный индекс (пошагово):** 1) В .pypirc добавить секцию с repository = URL индекса; 2) Указать username/password или токен для этого индекса; 3) Вызвать `twine upload --repository myprivate dist/*`. В CI задать TWINE_REPOSITORY_URL и учётные данные.

---

### Editable install

Установка пакета в режиме разработки: изменения в исходниках сразу видны при импорте, переустанавливать пакет не нужно.

```bash
pip install -e .
```

С опциональными зависимостями:

```bash
pip install -e ".[dev]"
```

**Как устроен editable install (setuptools):** при `pip install -e .` setuptools не копирует пакет в site-packages целиком. Вместо этого он создаёт в site-packages **.pth-файл** (или, в новом режиме, метаданные с путём к исходникам), в котором записан путь к корню проекта (или к каталогу `src/` при src layout). При импорте интерпретатор читает .pth и добавляет этот путь в **sys.path**, поэтому импорт `import mypkg` находит модули в вашем дереве исходников, а не в копии. Любое изменение в коде сразу отражается при следующем импорте — переустанавливать пакет не нужно.

**Режимы editable в setuptools:** в старом режиме (legacy) используется только .pth. В режиме **strict** (рекомендуется с PEP 660) создаётся специальная структура в site-packages с ссылкой на исходники. Режим задаётся в pyproject.toml: `[tool.setuptools.packages.find]` и настройками setuptools. При **src layout** в sys.path попадает путь к `src/`, поэтому импорт всегда идёт из src/, а не из корня — тесты и скрипты в корне не «затеняют» пакет.

**Запомните:** editable — это не копия пакета в site-packages, а добавление пути к исходникам в sys.path; при src layout путь указывает на src/, что изолирует пакет от корня проекта.

---

### Entry points

**Console scripts** — команды в консоли при установке пакета. В pyproject.toml (setuptools):

```toml
[project.scripts]
myapp = myapp.cli:main
```

После `pip install .` в PATH появляется команда `myapp`, вызывающая функцию `main` в модуле `myapp.cli`.

**Плагины** — объявление групп entry points:

```toml
[project.entry-points."myapp.plugins"]
foo = myapp_plugin_foo:plugin
```

В коде приложения (Python 3.10+):

```python
from importlib.metadata import entry_points

eps = entry_points(group="myapp.plugins")
for ep in eps:
    plugin = ep.load()  # загружает объект (функцию/класс), указанный в entry point
    plugin.run()
```

В **Python 3.9 и раньше** API другой: `entry_points()` возвращает объект с методом **.get(group_name, default)**. Группа — ключ, значение — список EntryPoint. Пример:

```python
from importlib.metadata import entry_points

eps = entry_points().get("myapp.plugins", [])
for ep in eps:
    plugin = ep.load()  # ep.name — имя entry point, ep.value — "module:attr"
    plugin.run()
```

Если группы нет, .get возвращает пустой список; итерация тогда не выполняется. В Python 3.10+ можно вызывать `entry_points(group="myapp.plugins")` — возвращается только список для этой группы (или пустой).

**Полный пример загрузки плагинов с обработкой ошибок:**

```python
from importlib.metadata import entry_points

def load_plugins():
    loaded = []
    try:
        eps = entry_points(group="myapp.plugins")
    except TypeError:
        eps = entry_points().get("myapp.plugins", [])
    for ep in eps:
        try:
            plugin = ep.load()
            loaded.append((ep.name, plugin))
        except (ImportError, AttributeError) as e:
            # плагин объявлен, но не загружается (нет модуля или атрибута)
            logging.warning("Plugin %s failed to load: %s", ep.name, e)
    return loaded
```

Так реализуется **расширяемость без жёсткой зависимости** от всех плагинов в коде: приложение объявляет группу entry points, сторонние пакеты регистрируют в ней свои плагины; при установке пакета плагин становится виден через `entry_points()`.

---

### MANIFEST.in и src layout

**MANIFEST.in** — файл в корне проекта, который указывает, **какие файлы включить** в sdist (исходный дистрибутив). По умолчанию бэкенд (setuptools и др.) включает не всё: например, тесты или скрипты в корне могут не попасть. MANIFEST.in дополняет или переопределяет этот набор.

**Основные директивы MANIFEST.in:**

| Директива | Назначение |
|-----------|------------|
| `include file1 file2` | Включить указанные файлы. |
| `exclude file1` | Исключить файлы (часто после recursive-include). |
| `recursive-include dir pattern` | Включить все файлы в каталоге и подкаталогах, совпадающие с glob-шаблоном. |
| `recursive-exclude dir pattern` | Исключить файлы по шаблону в каталоге. |
| `global-include pattern` | Включить файлы по шаблону во всём дереве. |
| `global-exclude pattern` | Исключить по шаблону во всём дереве. |
| `graft dir` | Включить весь каталог. |
| `prune dir` | Исключить весь каталог. |

Пример:

```
include README.md LICENSE pyproject.toml
include mypkg/py.typed
recursive-include mypkg *.py
recursive-exclude mypkg __pycache__
global-exclude *.pyc
```

**Пояснение директив на примере:** `include` — явно добавить файлы в sdist. `recursive-include mypkg *.py` — все .py в каталоге mypkg и подкаталогах. `recursive-exclude` и `global-exclude` убирают лишнее (кэш, байткод). Без MANIFEST.in setuptools по умолчанию включает не всё (например, тесты в корне или данные в пакете могут не попасть); при сомнении после сборки проверить содержимое sdist: распаковать .tar.gz и посмотреть список файлов.

**Src layout** — рекомендуемая структура проекта, при которой **исходный код пакета** лежит в подкаталоге **`src/`**:

```
project/
  pyproject.toml
  README.md
  src/
    mypkg/
      __init__.py
      module.py
      py.typed
  tests/
    test_module.py
  scripts/
    run.py
```

**Зачем src layout:**

1. **Изоляция от корня:** тесты, скрипты, конфиги в корне не смешиваются с кодом пакета; при установке в site-packages попадает только то, что в `src/`.
2. **Корректный editable install:** при `pip install -e .` импорт идёт из `src/mypkg`, а не из корня; тесты в корне не «затеняют» модули пакета при импорте из текущей директории.
3. **Тесты против установленного пакета:** при запуске тестов из корня пакет импортируется как установленный (из src/), а не как локальные файлы в корне — так ловятся ошибки упаковки.

В pyproject.toml (setuptools) указывают поиск пакетов в `src/`:

```toml
[tool.setuptools.packages.find]
where = ["src"]
# опционально: include = ["mypkg*"], exclude = []
```

Без этой настройки setuptools ищет пакеты в корне; при src layout пакетов там нет, поэтому их нужно явно указать или задать `where = ["src"]`.

#### Legacy-сборка (setup.py, setup.cfg)

Раньше метаданные и сборка задавались в **setup.py** (исполняемый Python) и **setup.cfg** (INI-формат). Сейчас рекомендуются **pyproject.toml** и **`python -m build`** (PEP 517/518/621); legacy-подход всё ещё встречается в старых пакетах и в части документации.

**setup.py** — скрипт, вызывающий **setuptools.setup()** с именем пакета, версией, зависимостями, пакетами и т.д.:

```python
from setuptools import setup, find_packages

setup(
    name="mypkg",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests>=2.0"],
    extras_require={"dev": ["pytest", "mypy"]},
    entry_points={"console_scripts": ["mycli=mypkg.cli:main"]},
)
```

**Поля setuptools.setup() (кратко):** **packages** — список пакетов или `find_packages()`; **package_dir** — отображение имён пакетов на каталоги (например, `{"": "src"}` для src layout); **install_requires** — зависимости при установке; **extras_require** — дополнительные группы (dev, docs); **entry_points** — console_scripts и плагины. Полный список — документация setuptools.

**Legacy-команды сборки (не рекомендуются для новых проектов):**

| Команда | Назначение |
|---------|------------|
| `python setup.py sdist` | Собрать source distribution (.tar.gz) — аналог `python -m build --sdist`. |
| `python setup.py bdist_wheel` | Собрать wheel — аналог `python -m build --wheel`. |
| `python setup.py install` | Установить пакет в окружение (лучше использовать `pip install .`). |
| `python setup.py develop` | Установить в режиме разработки (устарело; использовать `pip install -e .`). |
| `python setup.py upload` | Загрузить на PyPI (устарело, небезопасно; использовать **twine upload**). |

**setup.cfg** — INI-файл, в котором можно задать часть опций setuptools без кода в setup.py (например, `[metadata]`, `[options]`, `[options.packages.find]`). При наличии и setup.py, и pyproject.toml современные инструменты (pip, build) читают **pyproject.toml**; setup.py может оставаться минимальным (только `setuptools.setup()`) или использоваться для динамической логики (версия из git, условные зависимости).

**Запомните:** для новых проектов — pyproject.toml + `python -m build`; setup.py/setup.cfg — для поддержки старых репозиториев; загрузку на PyPI делать только через **twine**, не через `python setup.py upload`.

#### C-расширения в сборке (setuptools.Extension)

Пакеты с **C/C++ расширениями** (модули, компилируемые в .so/.pyd) собираются через **setuptools.Extension**. В pyproject.toml расширения задают в **[tool.setuptools.package-dir]** и **[tool.setuptools.packages]** или через **setup.py** в секции **ext_modules**; для чисто декларативного подхода в pyproject.toml используют **[tool.setuptools.packages]** и **[tool.setuptools.ext_modules]** (в зависимости от версии setuptools и бэкенда).

**Классический способ (setup.py):**

```python
from setuptools import setup, Extension

setup(
    name="mypkg",
    version="1.0.0",
    ext_modules=[
        Extension(
            "mypkg._native",
            sources=["src/mypkg/_native.c"],
            include_dirs=["/usr/include"],
            library_dirs=["/usr/lib"],
            libraries=["m"],
        )
    ],
)
```

**Параметры setuptools.Extension (основные):**

| Параметр | Назначение |
|----------|------------|
| **name** | Имя модуля (как при import: `mypkg._native`). |
| **sources** | Список исходных файлов (.c, .cpp и т.д.). |
| **include_dirs** | Каталоги с заголовками для компилятора. |
| **library_dirs** | Каталоги с библиотеками для линкера. |
| **libraries** | Имена библиотек для линковки (например, `["m"]` для libm). |
| **define_macros** | Макросы для препроцессора: `[("DEBUG", "1")]`. |
| **extra_compile_args** | Доп. флаги компилятора (например, `["-O2"]`). |
| **extra_link_args** | Доп. флаги линкера. |

При сборке **wheel** для платформы (Linux/Windows/macOS) создаётся бинарный wheel с скомпилированным расширением; **универсальный** wheel (py3-none-any) для пакетов с C-расширениями не подходит — нужны отдельные wheel’ы под платформу или установка из sdist на целевой машине. Подробности сборки C-расширений (pybind11, cffi, C API) — в материалах по Части XXV (C-расширения).

**Запомните:** C-расширения задаются через setuptools.Extension (или аналог в pyproject.toml); include_dirs и library_dirs — пути к заголовкам и библиотекам; распространение — платформо-специфичные wheel’ы или sdist.

#### Граничные случаи и отладка (§29a)

| Ситуация | Что проверить | Решение |
|----------|----------------|---------|
| build падает с ошибкой импорта | Зависимости сборки в [build-system] requires; версия Python. | Установить setuptools/wheel в окружении; проверить `python -m build --no-isolation` с уже установленными зависимостями. |
| twine upload отклоняет артефакт | Метаданные (имя, версия, описание). | Запустить `twine check dist/*`; исправить имя пакета (только буквы, цифры, дефисы), версию по PEP 440, длинное описание в readme. |
| После editable install импорт не находит пакет | Путь в .pth; src layout. | Проверить `pip show -f mypkg` (файлы установки); при src layout убедиться, что в sys.path попадает путь к src/. |
| Entry point не находится в приложении | Группа и имя; установлен ли пакет. | Проверить `python -c "from importlib.metadata import entry_points; print(entry_points(group='...'))"`; убедиться, что пакет с entry point установлен в то же окружение, что и приложение. |
| wheel не устанавливается на другой платформе | Универсальный vs платформо-специфичный. | Универсальный wheel (py3-none-any) ставится везде; для C-расширений нужны платформенные wheel’ы или установка из sdist на целевой машине. |
| twine upload: 400 Invalid or non-existent authentication | Токен PyPI, .pypirc, TWINE_*. | Username для PyPI должен быть __token__; password — токен с префиксом pypi-; проверить TWINE_USERNAME/TWINE_PASSWORD в CI. |
| editable install: импорт не находит пакет | Путь в .pth, src layout, package_dir. | Проверить `pip show -f mypkg` (файлы установки); при src layout в [tool.setuptools.packages.find] указать where = ["src"]. |
| entry_points не загружаются в приложении | Группа и имя совпадают, пакет установлен в то же окружение. | Проверить `python -c "from importlib.metadata import entry_points; print(list(entry_points(group='myapp.plugins')))"`. |

#### Частые вопросы (§29a)

| Вопрос | Краткий ответ |
|--------|----------------|
| Загружать на PyPI wheel, sdist или оба? | Рекомендуется оба: wheel — быстрая установка; sdist — для платформ без готового wheel и для аудита исходников. |
| Чем pip install -e . отличается от pip install .? | -e (editable) — импорт из исходников в репозитории, правки сразу видны; без -e — копия в site-packages, правки требуют переустановки. |
| Как добавить консольную команду в пакет? | В pyproject.toml: [project.scripts] с записью `cmd = pkg.module:func`; после установки команда `cmd` вызовет func. |
| Что такое py.typed и зачем он? | Пустой файл в пакете; маркер PEP 561 — типы (mypy, pyright) используют аннотации из пакета; без него типы могут игнорировать пакет. |

---

### py.typed (PEP 561)

Чтобы типы (mypy, pyright) использовали аннотации из вашего пакета, добавьте в пакет пустой файл:

```
mypkg/py.typed
```

Без него типы могут игнорировать ваш пакет или искать отдельные stub-пакеты (types-*).

**Запомните:** wheel — быстрая установка; sdist — исходники для сборки; build + twine — современный цикл сборки и публикации; editable — разработка без переустановки; entry points — CLI и плагины; src layout и py.typed — рекомендуемая структура и поддержка типизации.

---

## §30. Менеджеры зависимостей и окружений
