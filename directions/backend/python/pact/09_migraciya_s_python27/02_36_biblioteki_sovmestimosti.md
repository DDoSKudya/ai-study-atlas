[← Назад к индексу части IX](index.md)


**Цель раздела:** научиться применять `six` и `future` как временные «швы» совместимости между Py2 и Py3, понимать, какие именно различия они закрывают, и иметь план удаления этих швов после завершения миграции.

---

### Термины

| Термин | Определение |
|--------|-------------|
| **Compatibility layer** | Слой совместимости: небольшой набор функций/обёрток, скрывающий отличия платформ. |
| **Shim** | «Прокладка» между API: тонкая обёртка, которая подставляет нужную реализацию. |
| **Backport** | Перенос функциональности из новой версии в старую (например, из Py3 в Py2). |
| **Vendor** | «Вендорить» — включить копию зависимости в свой репозиторий (обычно нежелательно). |

---

### 36.1. `six`: минимальный шов для dual-support

#### Зачем нужен six

`six` — это **маленькая библиотека**, которая помогает писать один код для Py2 и Py3 без тяжёлых зависимостей:

- типы строк и чисел (`six.text_type`, `six.binary_type`, `six.string_types`, `six.integer_types`)
- переносы модулей stdlib (`six.moves`)
- удобные итераторы `six.iteritems(d)` вместо `d.iteritems()` (которого нет в Py3)
- инструменты для метаклассов (`six.with_metaclass`, `six.add_metaclass`)

#### Типовой набор «проблем → решение» через six

**1) Проверка «строка это текст или байты»**

```python
import six

def ensure_text(x):
    if isinstance(x, six.text_type):
        return x
    if isinstance(x, six.binary_type):
        return x.decode("utf-8", errors="strict")
    raise TypeError("expected text or bytes")
```

**2) Итерация по dict в Py2 и Py3**

```python
import six

def iter_items(d):
    for k, v in six.iteritems(d):
        yield k, v
```

В Py2 `six.iteritems(d)` вернёт iterator, а в Py3 — эквивалент `d.items()` (view-итерация).

**3) Перенос stdlib модулей**

```python
from six.moves.urllib.parse import urlparse
from six.moves.urllib.request import urlopen
```

Это один из самых практичных способов скрыть факт, что в Py2 были `urllib`, `urllib2`, а в Py3 всё переехало в `urllib.parse`, `urllib.request`.

#### `six.moves`: «карта переездов» стандартной библиотеки (самое нужное)

Когда вы видите в коде `try: import X; except ImportError: import Y`, это почти всегда следствие переезда stdlib между Py2 и Py3. `six.moves` позволяет писать один импорт.

| Что вы хотите | Py2 | Py3 | Через `six.moves` |
|--------------|-----|-----|-------------------|
| Очередь | `Queue` | `queue` | `from six.moves import queue` |
| Конфиги INI | `ConfigParser` | `configparser` | `from six.moves import configparser` |
| URL‑парсинг | `urlparse` | `urllib.parse` | `from six.moves.urllib.parse import urlparse` |
| HTTP запросы (низкоур.) | `urllib2` | `urllib.request` | `from six.moves.urllib.request import urlopen` |
| Итерация по диапазону | `xrange` | `range` | `from six.moves import range` (или просто `range` после 2to3) |
| Перенос reduce | builtin | `functools` | `from six.moves import reduce` |
| Перенос input | `raw_input` | `input` | `from six.moves import input` |

> Важно: `six.moves` — это именно «мост» на период dual-support. После перехода на чистый Py3 импорты лучше сделать прямыми (понятнее и меньше зависимостей).

#### Шаблон: централизованный модуль совместимости (`compat.py`)

Одна из лучших практик dual-support периода: **не разбрасывать совместимость по всему проекту**, а держать её в одном месте.

Пример (идея; адаптируйте под проект):

```python
# compat.py
import six

text_type = six.text_type
binary_type = six.binary_type
string_types = six.string_types
integer_types = six.integer_types

def is_text(x):
    return isinstance(x, text_type)

def is_bytes(x):
    return isinstance(x, binary_type)

def to_text(x, encoding="utf-8", errors="strict"):
    if x is None:
        return None
    if is_text(x):
        return x
    if is_bytes(x):
        return x.decode(encoding, errors)
    return text_type(x)

def to_bytes(x, encoding="utf-8", errors="strict"):
    if x is None:
        return None
    if is_bytes(x):
        return x
    if is_text(x):
        return x.encode(encoding, errors)
    return text_type(x).encode(encoding, errors)
```

Плюсы:
- меньше «условных веток по версии» в бизнес‑коде;
- проще удалить совместимость в конце миграции (чистите один модуль);
- проще тестировать преобразования строк/байтов (тестируете `compat.py`, а не «всё подряд»).

#### Важная практика: избегайте `if six.PY2` везде

Иногда без ветвления не обойтись, но как правило лучше:

- использовать `six.moves` и функции `six` (`iteritems`, типы, метаклассы);
- либо вынести ветвление в `compat.py`.

Почему: чем больше `if PY2` размазано по коду, тем дороже поддержка и тем сложнее финальная очистка.

#### Метаклассы: аккуратный пример

В Py2 метакласс задавался через `__metaclass__`, в Py3 — `metaclass=` в заголовке класса.

С `six`:

```python
import six

class Meta(type):
    pass

class Base(six.with_metaclass(Meta, object)):
    pass
```

#### Когда six — хорошая идея

- вам **нужен dual-support** (2.7 и 3.x одновременно);
- вы хотите **минимальный** слой совместимости и максимально «обычный» код вокруг.

#### Когда six — плохая идея

- если Py2 уже можно выключить: `six` только мешает и усложняет код;
- если вы начинаете писать новый код в стиле «везде six, даже где не нужно».

**Запомните:** `six` — это «временный адаптер». Его цель — пережить переход, а не стать стандартом проекта.

---

### 36.2. `future`: «сделать Py2 похожим на Py3»

`future` — более «тяжёлый» подход, чем `six`.

Если `six` пытается быть тонким набором функций, то `future` часто:

- подменяет/добавляет **builtins**, чтобы Py2-код выглядел как Py3;
- может ставить алиасы стандартной библиотеки через `future.standard_library.install_aliases()`.

#### Пример: builtins из future

```python
from builtins import str, range
```

Смысл: в Py2 `range` создавал список, а `xrange` был ленивым; `future` может дать вам поведение ближе к Py3.

#### Что обычно «приносит» `future` в проект (что вы увидите в коде)

В проектах на `future` часто встречаются такие элементы:

- `from builtins import ...` — подмена/добавление Py3‑подобных builtins в Py2 (например, `str`, `range`, `object`, `bytes` и т.д.).
- `from future import standard_library; standard_library.install_aliases()` — алиасы для stdlib переездов (см. §35.2).
- иногда — `from past.builtins import ...` (если нужно поведение «как в Py2» при запуске под Py3, но это уже отдельный и более редкий сценарий).

Эта «шумность» — цена за то, что Py2 начинает вести себя ближе к Py3 без ручного `try/except ImportError` и без постоянных ветвлений.

#### Практический критерий выбора: `six` или `future`

Сформулируем максимально прагматично:

- Если вам нужен **тонкий мост** и вы готовы чинить конкретные переезды руками — чаще выбирают `six`.
- Если вам нужно **быстро унифицировать** большую кодовую базу и вы готовы к «магии алиасов» — иногда выбирают `future` + futurize.

Нельзя сказать «future всегда хуже» или «six всегда лучше». Но важно помнить: **удалять `future` обычно сложнее**, потому что он меняет и импортный ландшафт, и ожидания по поведению builtins.

#### Риски future

- **Скрытие проблем:** вы можете «замазать» отличие, а потом оно проявится в неожиданном месте.
- **Шум в коде:** появляется много импортов и установок алиасов.
- **Сложнее удалять:** чем больше вы опираетесь на `future`, тем больше работы при переходе на чистый Py3.

Используйте `future` тогда, когда он даёт реальный выигрыш (например, большая база кода, строгий dual-support, ограниченные ресурсы на ручную переписку).

---

### 36.3. Когда отказываться от six/future и как это делать системно

#### Принцип

Совместимость — это **временная стоимость**. Если её не ограничить, она становится вечной.

#### Практический критерий «пора выкидывать»

Вы готовы удалять `six`/`future`, когда:

- вы официально подняли минимальную версию до Python 3 (и Py2 больше не поддерживается);
- CI больше не запускает тесты на Py2;
- зависимости не требуют Py2.

#### Как удалять без боли (пошагово)

1) Уберите «центральные» точки: например, `standard_library.install_aliases()` и подобные глобальные вещи.
2) Замените `six`-хелперы на Py3-эквиваленты:
   - `six.text_type` → `str`
   - `six.binary_type` → `bytes`
   - `six.string_types` → `str` (а если нужно принимать и bytes — используйте `(str, bytes)` осознанно)
   - `six.iteritems(d)` → `d.items()`
3) Перепишите `six.moves` на прямые Py3 импорты (`urllib.parse`, `urllib.request`, `queue`, `configparser` и т.д.).
4) Прогоните тесты, затем удалите зависимость из зависимостей проекта.

**Запомните:** выкидывать совместимость нужно не «в один день в панике», а как последнюю фазу миграции, когда Py3 уже стабилен.

---

## §37. Стратегии миграции
