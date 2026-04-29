[← Назад к индексу части VIII](index.md)


**Цель раздела:** запускать **mypy** и при необходимости **pyright** (Pylance в VS Code), настраивать strict mode и игнор модулей; использовать **typing_extensions** для обратной совместимости типов (Self, ParamSpec и др.) в библиотеках.

---

### Термины

| Термин | Определение |
|--------|-------------|
| **Статическая проверка типов** | Анализ аннотаций типов без запуска кода; находит несоответствия типов до выполнения. |
| **mypy** | Эталонный статический анализатор типов для Python; читает аннотации и typing. |
| **pyright / Pylance** | Альтернативный анализатор (от Microsoft); Pylance — расширение VS Code. |
| **typing_extensions** | Пакет с бэкпортами типов из новых версий Python (Self, TypeAlias, ParamSpec и т.д.) для поддержки старых версий. |
| **Stub-пакеты (types-*)** | Пакеты только с аннотациями для библиотек без встроенных типов (например, types-requests). |

**Stub-пакеты (types-*):** многие библиотеки не поставляют аннотации типов (или поставляют неполные). Сообщество ведёт пакеты **types-PackageName** на PyPI (например, **types-requests**, **types-PyYAML**). При установке `pip install types-requests` mypy и pyright подхватывают эти аннотации для пакета `requests`. Если сама библиотека добавила типы (и маркер py.typed), types-* пакет обычно помечают как устаревший; для своих пакетов типы лучше указывать в коде и добавлять py.typed.

---

### mypy

**mypy** — статический анализатор типов для Python; читает аннотации типов (PEP 484) и проверяет соответствие вызовов и присваиваний без запуска кода.

**Запуск:** `mypy mypkg`, `mypy src/` или `mypy .` (проверяет все модули в указанном пути). Выход с ненулевым кодом при обнаружении ошибок типов.

**Конфигурация в pyproject.toml (подробно):**

```toml
[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
no_implicit_optional = true
show_error_codes = true
show_column_numbers = true

[[tool.mypy.overrides]]
module = "legacy.*"
ignore_errors = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

**Что включает strict:** при `strict = true` включаются, в частности: no_implicit_optional (None должен быть явно в Union/Optional), warn_return_any, disallow_untyped_defs (все функции с аннотациями), disallow_incomplete_defs и др. Полный список — в документации mypy.

**Ослабление по модулям:** через [[tool.mypy.overrides]] для отдельных путей (например, legacy.*, tests.*) можно отключить строгие проверки или ignore_errors = true, чтобы постепенно приводить код к типизации.

**Типичные сообщения и что делать:**

| Сообщение | Причина | Решение |
|-----------|---------|---------|
| `Incompatible return value type` | Функция возвращает тип, не совместимый с аннотацией. | Исправить возвращаемое значение или аннотацию. |
| `Argument has type "X"; expected "Y"` | Передан аргумент не того типа. | Привести тип или расширить аннотацию (Union, overload). |
| `Missing return statement` | Функция объявлена с возвращаемым типом, но не все ветки возвращают значение. | Добавить return во все ветки или изменить аннотацию (Optional, NoReturn). |
| `Need type annotation for ...` | mypy не может вывести тип. | Добавить явную аннотацию. |
| `Unused "ignore" comment` | В коде есть # type: ignore, но mypy ошибки не выдаёт. | Удалить лишний комментарий или обновить опцию. |
| `Cannot determine type of "x"` | Переменная используется до присваивания или тип не выводится. | Присвоить начальное значение с явным типом или добавить аннотацию. |
| `Incompatible types in assignment` | Присваивание значения несовместимого типа переменной. | Исправить тип правой части или аннотацию переменной; при необходимости cast(). |

**Кеш и инкрементальная проверка:** mypy по умолчанию кеширует результаты в каталоге .mypy_cache; при повторном запуске проверяются только изменённые файлы (если не указано --no-incremental).

**Запомните:** strict mode рекомендуется для новых проектов; для legacy-модулей используйте overrides с ослаблением или ignore_errors; типичные ошибки исправляют по сообщениям mypy.

---

### pyright

**pyright** — статический анализатор типов от Microsoft; по возможностям близок к mypy. В VS Code используется через расширение **Pylance** (Pylance включает pyright). Конфигурация: **pyrightconfig.json** в корне проекта или секция [tool.pyright] в pyproject.toml (если инструмент её читает).

**Уровни строгости (typeCheckingMode):** basic, standard, strict. В strict проверки ближе к mypy strict. Выбор между mypy и pyright часто сводится к интеграции с IDE (Pylance в VS Code удобен с pyright) и к привычке команды.

---

### typing_extensions

В библиотеках, поддерживающих Python 3.9 или 3.10, типы вроде **Self** (3.11) или **TypeAlias** (3.10) можно импортировать из **typing_extensions**:

```python
from typing_extensions import Self

class C:
    def copy(self) -> Self:
        return type(self)()
```

Установка: `pip install typing_extensions`. Зависимость для пакетов: `typing_extensions>=4.0` (в [project] или requirements).

**Что есть в typing_extensions (кратко):** бэкпорты типов и утилит из новых версий Python, чтобы библиотеки могли использовать их при поддержке старых версий. Примеры: **Self** (3.11), **TypeAlias** (3.10), **ParamSpec**, **Concatenate**, **TypeVarTuple** (3.10), **TypedDict** с Required/NotRequired (3.11), **NamedTuple** с default (3.10), **assert_never** (3.11), **Literal**, **Final**, **Protocol** и др. Импорт: `from typing_extensions import Self` — в Python 3.11 можно также `from typing import Self`; для кода, поддерживающего 3.9–3.10, используют только typing_extensions.

#### Граничные случаи и отладка (§32)

| Ситуация | Что проверить | Решение |
|----------|----------------|---------|
| mypy не находит модуль (third-party) | Установлен ли пакет; есть ли types-* или py.typed. | Установить пакет и при необходимости types-requests и т.д.; для своего пакета добавить py.typed. |
| mypy падает на legacy-коде | Строгие опции (disallow_untyped_defs и т.д.). | Добавить [[tool.mypy.overrides]] для модуля с ignore_errors = true или ослабить проверки. |
| pyright не видит venv в VS Code | Интерпретатор выбран не тот. | Выбрать интерпретатор из venv (Command Palette → Python: Select Interpreter). |
| Incompatible return value / Argument has type | Несоответствие аннотации и фактического типа. | Исправить тип возврата/аргумента или использовать cast/overload; проверить Union и Optional. |

#### Частые вопросы (§32)

| Вопрос | Краткий ответ |
|--------|----------------|
| Нужно ли типизировать весь проект сразу? | Нет; можно включать strict по модулям и ослаблять через overrides для legacy; постепенная типизация допустима. |
| Чем mypy отличается от pyright? | Оба проверяют типы; pyright/Pylance удобен в VS Code; mypy — эталон в экосистеме; выбор часто по привычке команды. |
| Когда использовать typing_extensions? | В библиотеках, поддерживающих Python 3.9/3.10: импорт Self, TypeAlias и др. из typing_extensions вместо typing. |

**Запомните:** mypy и pyright — основные инструменты проверки типов; strict mode рекомендуется для новых проектов; typing_extensions — для использования новых типов в коде, рассчитанном на старые версии Python.

---

## §33. Тестирование
