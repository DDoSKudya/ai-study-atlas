[← Назад к индексу части VIII](index.md)


**Цель раздела:** оформлять **docstrings** по PEP 257, при необходимости генерировать документацию с **Sphinx** или **MkDocs**, указывать type hints в docstrings (Google, NumPy стили) при отсутствии аннотаций в коде.

---

### Термины

| Термин | Определение |
|--------|-------------|
| **docstring** | Строка в начале модуля, класса или функции, описывающая назначение; по PEP 257 — тройные кавычки, первая строка — краткое описание. |
| **PEP 257** | Рекомендации по оформлению документационных строк: стиль, многострочные docstrings. |
| **Sphinx** | Инструмент генерации документации (HTML, PDF); autodoc подтягивает docstrings из кода; reStructuredText. |
| **MkDocs** | Генерация документации из Markdown; проще для простых проектов. |

---

### PEP 257 — основы

**PEP 257** («Docstring Conventions») задаёт соглашения по оформлению документационных строк в Python.

**Общие правила:**

1. **Расположение:** docstring — первая строка в теле модуля, класса, функции или метода — строка в тройных кавычках `"""..."""` (или `'''...'''`).
2. **Однострочная docstring:** одна строка; закрывающие кавычки на той же строке; без пустой строки после. Подходит для короткого описания.
3. **Многострочная docstring:** первая строка — краткое резюме (как однострочная); затем пустая строка; затем абзацы с деталями. Закрывающие кавычки на отдельной строке.
4. **Для классов:** docstring описывает класс; если есть публичные атрибуты, их можно перечислить в отдельном разделе (см. стили ниже).
5. **Для скриптов:** в docstring модуля можно описать использование скрипта (например, при вызове без аргументов).

**Что не делать:** не писать docstring для приватных методов, если они очевидны; не дублировать сигнатуру в первой строке («Function that does X» лучше, чем «foo(a, b) does X» — сигнатура видна из кода).

**Docstring для класса с атрибутами (Google style):** если у класса есть важные атрибуты экземпляра или класса, их перечисляют в секции Attributes:

```python
class Config:
    """Configuration holder.

    Attributes:
        timeout: Request timeout in seconds.
        retries: Number of retries on failure.
    """
    def __init__(self, timeout: int = 30, retries: int = 3):
        self.timeout = timeout
        self.retries = retries
```

В NumPy style атрибуты описывают в секции Attributes с тем же форматом, что и Parameters.

Пример:

```python
def func(a: int, b: str) -> bool:
    """Return True if a and b satisfy the condition."""
    ...

def other():
    """First line.

    More details and examples can go here.
    """
```

---

### Type hints в docstrings

Если аннотации не используются, типы можно описать в docstring (Google, NumPy стили):

```python
def process(data, n):
    """Process data.

    Args:
        data: List of items.
        n: Number of items to process.

    Returns:
        Processed result.
    """
```

Sphinx и другие инструменты парсят такие блоки для отображения в документации.

#### Стили docstrings (Google, NumPy, reStructuredText)

Когда аннотации типов в коде не используются или нужно дублировать описание типов в документации, типы указывают в docstring. Распространённые стили:

**Google style** (кратко, читаемо):

```python
def process(data, n):
    """Process data.

    Args:
        data: List of items to process.
        n: Number of items.

    Returns:
        Processed result.

    Raises:
        ValueError: If n is negative.
    """
```

**NumPy style** (подробные секции):

```python
def process(data, n):
    """Process data.

    Parameters
    ----------
    data : list
        List of items to process.
    n : int
        Number of items.

    Returns
    -------
    result
        Processed result.

    Raises
    ------
    ValueError
        If n is negative.
    """
```

**reStructuredText** (для Sphinx: директивы типа :param, :return):

```python
def process(data, n):
    """Process data.

    :param data: List of items to process.
    :param n: Number of items.
    :returns: Processed result.
    :raises ValueError: If n is negative.
    """
```

Выбор стиля обычно фиксируют в руководстве по стилю проекта; Sphinx и MkDocs поддерживают несколько форматов через расширения.

---

### Sphinx и MkDocs

**Sphinx** — генератор документации (HTML, PDF, ePub и др.); изначально для Python-документации. Исходники — в reStructuredText (.rst); код и docstrings подтягиваются через расширение **sphinx.ext.autodoc**.

**Минимальный workflow:**

1. Создать проект: `sphinx-quickstart` (ответы на вопросы: каталог build, source, имя проекта).
2. В **conf.py** включить расширения: `extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']` (napoleon — для Google/NumPy стиля docstrings).
3. В .rst файлах использовать директивы autodoc: `.. automodule:: mypkg.module`, `.. autofunction:: mypkg.func`, `.. autoclass:: mypkg.MyClass` (с опцией `:members:` для методов класса).
4. Собрать HTML: `make html` (или `sphinx-build -b html sourcedir builddir`).

**Директивы autodoc (кратко):** `.. automodule:: mypkg.module` — документировать весь модуль (docstring модуля + при опциях — классы и функции). `.. autofunction:: mypkg.func` — одна функция. `.. autoclass:: mypkg.MyClass` — класс; опция **:members:** — включить методы; **:undoc-members:** — и без docstring; **:private-members:** — приватные. Пример в .rst: `.. autoclass:: mypkg.MyClass\n   :members:\n   :undoc-members:`.

**autodoc** импортирует модули и извлекает docstrings; **napoleon** преобразует Google/NumPy стиль в reStructuredText для красивого отображения.

**Ключевые настройки conf.py (Sphinx):**

| Настройка | Назначение |
|-----------|------------|
| `extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.viewcode']` | autodoc — docstrings из кода; napoleon — Google/NumPy; viewcode — ссылки на исходный код. |
| `autodoc_default_options = {'members': True, 'undoc-members': True}` | Включать в документацию все члены класса; undoc-members — и без docstring. |
| `napoleon_google_docstring = True` | Парсить Google-style docstrings. |
| `napoleon_numpy_docstring = True` | Парсить NumPy-style docstrings. |
| `html_theme = 'alabaster'` или `'sphinx_rtd_theme'` | Тема оформления HTML. |
| `sys.path.insert(0, os.path.abspath('..'))` | Добавить корень проекта в sys.path, чтобы Sphinx мог импортировать ваш пакет при извлечении docstrings. |

Без добавления пути к пакету в sys.path autodoc не сможет импортировать модули и извлечь из них docstrings.

**Пример добавления пути в conf.py (пошагово):** в начале conf.py (после импорта os) добавьте:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))   # корень проекта на уровень выше docs/
# если пакет в src/: sys.path.insert(0, os.path.abspath('../src'))
```

Путь зависит от структуры: если каталог документации — `docs/`, а корень проекта и пакет — на уровень выше, то `'..'`; если код в `src/mypkg`, то `os.path.abspath('../src')`. После этого директивы `.. automodule:: mypkg` смогут импортировать `mypkg`.

**intersphinx (ссылки на внешнюю документацию).** Расширение `sphinx.ext.intersphinx` позволяет делать ссылки на объекты в чужой документации (например, Python, Django). В **conf.py**:

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", {}),
    "django": ("https://docs.djangoproject.com/en/stable/", {}),
}
```

После этого можно использовать роли вида `:class:\`dict\`` (будет линк в docs.python.org) или `:mod:\`django.http\`` — Sphinx подтянет ссылки из удалённых inventories.

**autodoc_typehints (как показывать type hints).** В `conf.py` можно управлять тем, где отображаются аннотации типов:

```python
autodoc_typehints = "description"  # типы переносятся в описание параметров
```

Варианты: `"signature"` (по умолчанию, типы остаются в сигнатуре), `"description"` (переносятся в текст), `"none"` (игнорировать). В сочетании с napoleon это позволяет строить «чистые» сигнатуры и описывать типы только в секциях Args/Returns.

**MkDocs** — генератор документации из **Markdown**; конфиг **mkdocs.yml**, страницы — .md файлы. Проще для небольших проектов и документации «в стиле вики». Плагины (mkdocstrings и др.) могут подтягивать docstrings из кода в Markdown. Команда сборки: `mkdocs build`; предпросмотр: `mkdocs serve`.

**Минимальный mkdocs.yml:**

```yaml
site_name: My Project
nav:
  - Home: index.md
  - API: api.md
plugins:
  - search
  - mkdocstrings:
      handlers:
        python:
          paths: [src]
```

С плагином **mkdocstrings** в .md можно писать: `::: mypkg.module` или `::: mypkg.MyClass` — в документ подставятся docstrings из кода. Тема задаётся в **theme**: `theme: readthedocs` или установить mkdocs-material и указать `theme: name: material`.

**Продвинутая навигация и стили в MkDocs.** Навигация может быть вложенной, с группами и подстраницами:

```yaml
nav:
  - Home: index.md
  - Guides:
      - Getting started: guides/getting-started.md
      - Configuration: guides/configuration.md
  - Reference:
      - API: api.md
      - CLI: cli.md
```

Дополнительные стили и скрипты:

```yaml
extra_css:
  - css/custom.css

extra_javascript:
  - js/custom.js
```

Файлы `css/custom.css` и `js/custom.js` лежат в каталоге `docs/` (или другом, указанном в конфиге). Их можно использовать для подсветки блоков, добавления кнопок «scroll to top» и т.п. В темах вроде mkdocs-material также доступны свои настройки навигации (sidebar, tabs и др.), которые задаются под `theme:`.

#### Граничные случаи и отладка (§34)

| Ситуация | Что проверить | Решение |
|----------|----------------|---------|
| Sphinx autodoc не находит модуль | sys.path в conf.py. | В conf.py добавить `sys.path.insert(0, os.path.abspath('..'))` (или путь к корню пакета). |
| Napoleon не парсит docstring | Стиль (Google/NumPy), расширения. | В conf.py: napoleon_google_docstring = True, napoleon_numpy_docstring = True; extensions включают sphinx.ext.napoleon. |
| MkDocs mkdocstrings пустая страница | Путь к пакету (paths), установка плагина. | В mkdocs.yml в mkdocstrings указать paths: [src]; установить mkdocstrings[python]. |

#### Частые вопросы (§34)

| Вопрос | Краткий ответ |
|--------|----------------|
| Какой стиль docstrings выбрать? | Google — кратко и читаемо; NumPy — подробные секции; reST — для Sphinx и сложной разметки. |
| Sphinx или MkDocs? | Sphinx — мощнее для больших API и reST; MkDocs — проще для Markdown и небольших проектов. |

**Запомните:** docstrings по PEP 257 — стандарт описания API; Sphinx подходит для больших API-документов и reStructuredText; MkDocs — для Markdown и простых сайтов документации; типы в docstrings дополняют или заменяют аннотации для читателей и инструментов.

---

## Частые сценарии (Часть VIII)
