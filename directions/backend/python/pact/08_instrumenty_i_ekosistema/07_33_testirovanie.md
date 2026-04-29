[← Назад к индексу части VIII](index.md)


**Цель раздела:** писать тесты с **unittest** и **pytest**, использовать **фикстуры** и **параметризацию**, подменять зависимости через **unittest.mock** и **pytest-mock**, измерять **покрытие** (coverage, pytest-cov).

---

### Термины

| Термин | Определение |
|--------|-------------|
| **unittest** | Стандартный фреймворк тестирования: классы, наследующие TestCase, методы test_*. |
| **pytest** | Популярный фреймворк: функции test_*, фикстуры, параметризация, плагины. |
| **Фикстура (fixture)** | Подготовка данных или окружения для теста (например, временный файл, экземпляр класса); в pytest — декоратор @pytest.fixture и conftest.py. |
| **Параметризация** | Запуск одного и того же теста с разными аргументами (данные/ожидания); в pytest — @pytest.mark.parametrize. |
| **Mock** | Подмена объекта или вызова для изоляции теста и проверки взаимодействий (unittest.mock, pytest-mock). |
| **Покрытие (coverage)** | Доля кода, выполненная при запуске тестов; инструменты coverage, pytest-cov. |

---

### unittest

**unittest** — встроенный в Python фреймворк тестирования (модуль **unittest**). Тесты организуются в классы, наследующие **TestCase**; методы тестов должны начинаться с **test_**.

**Базовый пример:**

```python
import unittest

class TestMyFunc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_exception(self):
        with self.assertRaises(ValueError):
            int("x")
```

**Подготовка и очистка:** для каждого теста можно вызывать **setUp** (перед тестом) и **tearDown** (после теста). Для всего класса — **setUpClass** / **tearDownClass** (классовые методы).

```python
class TestWithSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.resource = create_heavy_resource()

    def setUp(self):
        self.data = []

    def tearDown(self):
        self.data.clear()

    def test_something(self):
        self.data.append(1)
        self.assertEqual(len(self.data), 1)
```

**Проверки (assert) — основные методы TestCase:**

| Метод | Назначение |
|-------|------------|
| `assertEqual(a, b)` | a == b |
| `assertNotEqual(a, b)` | a != b |
| `assertTrue(x)`, `assertFalse(x)` | bool(x) is True/False |
| `assertIs(a, b)`, `assertIsNot(a, b)` | a is b / a is not b |
| `assertIsNone(x)` | x is None |
| `assertIn(a, b)` | a in b |
| `assertNotIn(a, b)` | a not in b |
| `assertIsInstance(a, type)` | isinstance(a, type) |
| `assertRaises(Exc, callable, *args)` | callable(*args) выбрасывает Exc; можно использовать как контекстный менеджер: `with self.assertRaises(ValueError): ...` |
| `assertRaisesRegex(Exc, pattern, ...)` | То же + сообщение исключения должно соответствовать регулярному выражению. |
| `assertAlmostEqual(a, b, places=7)` | round(a - b, places) == 0 (для float). |
| `assertGreater(a, b)`, `assertLess(a, b)` | a > b, a < b и аналоги для >=, <=. |
| `assertListEqual(a, b)`, `assertDictEqual(a, b)` | Сравнение с понятным выводом при несовпадении. |

**Пропуск и ожидаемый провал:** `@unittest.skip("reason")` — всегда пропускать тест; `@unittest.skipIf(condition, "reason")` — пропускать, если condition истинно (удобно для пропуска на определённой платформе или версии); `@unittest.expectedFailure` — тест ожидаемо падает (помечается в отчёте). Пример:

```python
import sys
@unittest.skipIf(sys.platform == "win32", "Not supported on Windows")
def test_posix_only(self):
    ...
```

**Запуск:** `python -m unittest discover` (поиск тестов по шаблону test_*.py в текущем каталоге); `python -m unittest discover -s tests -p 'test_*.py'` (каталог tests, шаблон test_*.py); `python -m unittest test_module` (один модуль); `python -m unittest test_module.TestClass.test_method` (один тест). Опция `-v` — подробный вывод; `-f` / `--failfast` — остановиться на первом провале.

**TestLoader и TestSuite:** для программного сбора тестов используют **unittest.TestLoader()**: `loader.loadTestsFromModule(module)`, `loader.loadTestsFromTestCase(TestClass)`, `loader.discover(start_dir, pattern='test_*.py')`. Результат — **TestSuite**; запуск: `unittest.TextTestRunner().run(suite)`.

**Запомните:** unittest не требует установки зависимостей; подходит для встроенных скриптов и сред, где pytest недоступен; для новых проектов чаще выбирают pytest из‑за фикстур и параметризации.

---

### pytest

Тесты — функции с именем `test_*`:

```python
def test_add():
    assert 1 + 1 == 2

def test_exception():
    with pytest.raises(ValueError):
        int("x")
```

**Фикстуры:** общая подготовка в **conftest.py** (файл в корне тестов или в любом родительском каталоге) или в самом тестовом модуле. pytest автоматически загружает conftest.py и делает фикстуры из него доступными во всех тестах в этом каталоге и подкаталогах. **Важно:** conftest.py в подкаталоге (например, tests/integration/conftest.py) виден только тестам в этом подкаталоге и ниже; фикстуры из корневого tests/conftest.py доступны всем тестам в tests/. Имя фикстуры совпадает с именем параметра теста: если тест объявляет параметр `tmp_file`, pytest ищет фикстуру с именем `tmp_file` и вызывает её, а результат передаёт в тест.

```python
# conftest.py (в каталоге tests/ или в корне)
import pytest

@pytest.fixture
def tmp_file(tmp_path):
    f = tmp_path / "data.txt"
    f.write_text("hello")
    return f

# test_example.py
def test_read(tmp_file):
    assert tmp_file.read_text() == "hello"
```

**Фикстура с очисткой (yield):** если после теста нужно освободить ресурс (закрыть соединение, удалить файл), используйте **yield**: код до yield — setup, код после yield — teardown. Teardown выполняется после завершения теста (и при падении теста). Без yield фикстура просто возвращает значение; с yield — возвращает значение вызывающему, а после выхода из теста выполняется код после yield.

```python
@pytest.fixture
def db_connection():
    conn = create_connection()
    yield conn
    conn.close()
```

**Зависимость фикстур:** фикстура может зависеть от другой фикстуры — достаточно объявить её именем параметра. Порядок вызова: сначала вызываются фикстуры без зависимостей, затем те, что от них зависят.

```python
@pytest.fixture
def user_repo(db_connection):
    return UserRepository(db_connection)

def test_user(user_repo):
    user = user_repo.get(1)
    assert user is not None
```

Сначала вызывается `db_connection`, затем `user_repo(db_connection)`, затем тест получает `user_repo`.

**Параметризация:**

```python
@pytest.mark.parametrize("a,b,expected", [(1, 1, 2), (2, 3, 5)])
def test_sum(a, b, expected):
    assert a + b == expected
```

**Параметризация с id (удобно в отчёте):** опция **ids** задаёт подписи к наборам аргументов — в выводе pytest будет видно, какой набор провалился:

```python
@pytest.mark.parametrize("a,b,expected", [(1, 1, 2), (0, 0, 0), (-1, 1, 0)], ids=["positive", "zeros", "mixed"])
def test_sum(a, b, expected):
    assert a + b == expected
```

Без ids вывод будет `test_sum[1-1-2]`, с ids — `test_sum[positive]`, `test_sum[zeros]` и т.д. Можно передать функцию: `ids=lambda x: f"a={x[0]},b={x[1]}"`.

**Запуск:** `pytest` (по умолчанию ищет test_*.py и *_test.py); `pytest tests/` (каталог); `pytest -v` (подробный вывод); `pytest -k "test_add"` (только тесты, в имени которых есть test_add); `pytest --tb=short` (короткий traceback).

**Полезные опции запуска pytest:**

| Опция | Назначение |
|-------|------------|
| `-v` | Подробный вывод (имя каждого теста). |
| `-x`, `--exitfirst` | Остановиться на первом провале. |
| `--lf`, `--last-failed` | Запустить только тесты, провалившиеся в последний раз (удобно после исправлений). |
| `--ff`, `--failed-first` | Сначала запустить последние провалы, затем остальные. |
| `-k "expr"` | Запустить только тесты, у которых имя совпадает с выражением (например, `-k "test_add or test_sub"`). |
| `--tb=short` / `--tb=no` | Короткий traceback или без него. |
| `-n auto` | Параллельный запуск (требует pytest-xdist). |

**Маркеры:** можно помечать тесты и запускать выборочно: `@pytest.mark.slow`, затем `pytest -m slow`. Встроенные: skip, skipif, xfail, parametrize. Регистрация своих маркеров в **pyproject.toml** (чтобы избежать предупреждения о неизвестном маркере):

```toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests",
]
```

**Граничные случаи pytest:** тесты не находятся — проверьте, что имена файлов соответствуют `test_*.py` или `*_test.py`, имена функций — `test_*`, а каталог с тестами передан в аргументах (`pytest tests/`). Фикстура не находится — проверьте, что она объявлена в conftest.py в том же или родительском каталоге и имя параметра теста совпадает с именем фикстуры. Импорт тестируемого модуля падает — убедитесь, что корень проекта или путь к пакету в PYTHONPATH (при src layout обычно `pip install -e .` решает проблему).

---

### Mocking

**unittest.mock:** подмена функции или класса. **Патч по месту использования:** подменять нужно объект в том модуле, где он вызывается (где написан import), а не там, где определён.

```python
from unittest.mock import patch

with patch("mymodule.open", return_value=io.StringIO("fake")):
    result = mymodule.read_config()
```

**Патч как декоратор:** для всего теста можно использовать декоратор `@patch`; аргументы теста получают mock-объекты в том же порядке, что и декораторы (снизу вверх):

```python
@patch("mymodule.requests.get")
def test_fetch(mock_get):
    mock_get.return_value.json.return_value = {"id": 1}
    result = mymodule.fetch_user(1)
    assert result["id"] == 1
    mock_get.assert_called_once_with("https://api.example.com/users/1")
```

**patch.object** — подмена атрибута конкретного объекта (удобно для методов класса):

```python
with patch.object(MyClass, "expensive_method", return_value=42):
    obj = MyClass()
    assert obj.expensive_method() == 42
```

**pytest-mock** даёт фикстуру `mocker` (обёртка над patch и т.д.) для удобной подстановки в тестах pytest:

```python
def test_with_mock(mocker):
    fake_open = mocker.patch("builtins.open", mocker.mock_open(read_data="fake"))
    result = mymodule.read_first_line("path.txt")
    assert result == "fake"
    fake_open.assert_called_once_with("path.txt")
```

#### pytest.raises и pytest.warns

Проверка, что код выбрасывает ожидаемое исключение или предупреждение:

```python
def test_raises():
    with pytest.raises(ValueError, match="invalid"):
        int("not a number")

def test_warns():
    with pytest.warns(DeprecationWarning, match="old_api"):
        mymodule.old_api()
```

**scope фикстур:** у `@pytest.fixture` можно задать **scope**: `function` (по умолчанию — на каждый тест), `class` (один раз на класс тестов), `module` (один раз на файл), `session` (один раз на весь прогон). Фикстура с `scope="session"` создаётся один раз на весь прогон тестов (удобно для тяжёлой инициализации: БД, клиент API). Фикстура с `scope="class"` создаётся один раз на каждый тестовый класс (в unittest-стиле с классами).

```python
@pytest.fixture(scope="session")
def db():
    return create_test_db()

@pytest.fixture(scope="class")
def shared_client():
    return ApiClient()  # один экземпляр на класс

class TestAPI:
    def test_one(self, shared_client):
        assert shared_client.get("/x") is not None
    def test_two(self, shared_client):
        assert shared_client is shared_client  # тот же объект
```

**Порядок вызова:** при scope="session" фикстура создаётся до любых тестов; при scope="function" — перед каждым тестом. Если фикстура A зависит от фикстуры B (A(B)), сначала создаётся B (с учётом её scope), затем A.

---

### Покрытие

```bash
pip install pytest-cov
pytest --cov=mypkg --cov-report=html
```

В каталоге `htmlcov/` отчёт по строкам; в CI часто выводят только итог: `--cov-report=term-missing` (показывает строки, не покрытые тестами).

**coverage vs pytest-cov:** **coverage** — самостоятельная утилита: `coverage run -m pytest`, затем `coverage report` или `coverage html`. **pytest-cov** — плагин pytest, под капотом использует coverage; удобнее: один вызов `pytest --cov=mypkg --cov-report=html`. Для CI часто достаточно pytest-cov; для сложных сценариев (несколько источников, .coveragerc) можно использовать coverage напрямую.

**Опции pytest-cov (важные):**

| Опция | Назначение |
|-------|------------|
| `--cov=src` или `--cov=mypkg` | Какие пакеты/каталоги учитывать при подсчёте покрытия (по умолчанию текущий каталог). |
| `--cov-report=term-missing` | В консоли вывести процент по модулям и список непокрытых строк. |
| `--cov-report=html` | Создать каталог htmlcov/ с интерактивным отчётом (какие строки покрыты/не покрыты). |
| `--cov-report=xml` | XML-отчёт для загрузки в CI (например, Codecov, Coveralls). |
| `--cov-fail-under=80` | Завершить с ошибкой, если покрытие ниже 80% (удобно в CI). |
| `--no-cov-on-fail` | Не генерировать отчёт при падении тестов. |

**Запомните:** unittest — встроенный фреймворк; pytest — удобные фикстуры и параметризация; mock — изоляция зависимостей; coverage/pytest-cov — измерение покрытия; в CI часто используют --cov-report=term-missing и --cov-fail-under.

---

### Плагины pytest

**pytest** расширяется **плагинами**: они добавляют фикстуры, хуки, маркеры, формат вывода и т.д. Плагины устанавливаются как пакеты и подхватываются автоматически при наличии **pytest_plugins** или по entry point **pytest11**.

**Установка и использование:** установить пакет в окружение — после этого pytest подхватит плагин при запуске. Примеры:

```bash
pip install pytest-cov pytest-mock pytest-asyncio pytest-xdist
pytest  # плагины активны
```

**Типичные плагины (кратко):**

| Плагин | Назначение |
|--------|------------|
| **pytest-cov** | Покрытие кода: `--cov=src`, `--cov-report=html`, `--cov-fail-under=80`. |
| **pytest-mock** | Фикстура `mocker` — тонкая обёртка над unittest.mock; удобный `mocker.patch()`. |
| **pytest-asyncio** | Запуск async-тестов: `@pytest.mark.asyncio` на корутинах; настройка event loop. |
| **pytest-xdist** | Параллельный запуск: `-n auto` или `-n 4` (несколько воркеров). |
| **pytest-django** | Интеграция с Django: фикстуры БД, транзакции, `django_db` маркер. |
| **pytest-flask** | Фикстура `client` для тестирования Flask-приложения. |
| **pytest-timeout** | Прерывание зависших тестов: `@pytest.mark.timeout(5)`. |
| **pytest-benchmark** | Фикстура для бенчмарков; сохранение и сравнение результатов. |

**Менее распространённые, но полезные плагины:**

| Плагин | Назначение |
|--------|------------|
| **pytest-rerunfailures** | Повторный запуск упавших тестов (flaky-тесты): `pytest --reruns 3`. |
| **pytest-randomly** | Перемешивание порядка тестов, фиксирование `random.seed`; помогает находить зависимости между тестами. |
| **pytest-freezegun / freezegun** | «Заморозка» времени в тестах (datetime.now(), date.today()) через фикстуру. |
| **pytest-httpx / responses** | Тестирование HTTP-клиентов без реальных запросов (подмена ответов). |
| **pytest-mypy** | Запуск mypy как части pytest: `pytest --mypy`. |

**Подключение плагина в тестах:** обычно не требуется — достаточно установить пакет. Для **pytest-asyncio** тесты помечают маркером:

```python
import pytest

@pytest.mark.asyncio
async def test_async_fetch():
    result = await fetch_data()
    assert result is not None
```

В pyproject.toml можно зафиксировать маркеры и опции плагинов:

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
addopts = "-v --tb=short"
markers = [
    "asyncio: mark test as async",
    "slow: marks tests as slow",
]
```

**Написание своего плагина (кратко):** плагин — модуль или пакет с хуками pytest (например, `pytest_configure`, `pytest_collection_modifyitems`). Регистрация через **entry point** в pyproject.toml: `[project.entry-points.pytest11]` с именем и путём к модулю. Документация: [Writing plugins — pytest](https://docs.pytest.org/en/stable/how-to/writing_plugins.html).

**Минимальный собственный плагин с хуками:**

```python
# mypkg/pytest_plugin.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="run tests marked as slow",
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marks tests as slow")

def pytest_collection_modifyitems(config, items):
    """Переместить slow-тесты в конец и при отсутствии --run-slow пометить как xfail."""
    run_slow = config.getoption("--run-slow")
    slow_items = [i for i in items if "slow" in i.keywords]
    fast_items = [i for i in items if "slow" not in i.keywords]
    items[:] = fast_items + slow_items
    if not run_slow:
        for item in slow_items:
            item.add_marker(pytest.mark.xfail(reason="need --run-slow to run this test"))
```

Регистрация плагина через entry point в **pyproject.toml**:

```toml
[project.entry-points.pytest11]
mypkg_plugin = "mypkg.pytest_plugin"
```

После установки пакета `mypkg` pytest автоматически подхватит плагин (имя группы entry point — `pytest11` фиксировано).

#### Граничные случаи и отладка (§33)

| Ситуация | Что проверить | Решение |
|----------|----------------|---------|
| pytest не находит тесты | Имена файлов (test_*.py), имена функций (test_*), путь. | Запускать из корня проекта; проверять conftest.py и пути; `pytest --collect-only` покажет собранные тесты. |
| Фикстура не подставляется | Имя аргумента совпадает с именем фикстуры; scope. | Имя параметра теста должно совпадать с именем фикстуры; при scope=session фикстура создаётся один раз. |
| patch не срабатывает | Патчить «по месту использования», а не по месту определения. | Использовать путь к объекту в том модуле, где он импортирован: `patch("mymodule.used_func")`, а не `patch("othermodule.used_func")`. |
| coverage показывает 0% | Путь к пакету (--cov), каталог запуска. | Указать `--cov=src` или `--cov=mypkg`; запускать из корня проекта. |

#### Частые вопросы (§33)

| Вопрос | Краткий ответ |
|--------|----------------|
| unittest или pytest? | pytest удобнее (фикстуры, параметризация, плагины); unittest встроен и подходит для простых сценариев и совместимости. |
| Где хранить общие фикстуры? | В conftest.py в корне тестов или в каталоге с тестами; pytest подхватывает conftest автоматически. |
| Как пропустить тест в pytest? | `@pytest.mark.skip("reason")` или `@pytest.mark.skipif(condition, reason="...")`. |

**Запомните:** плагины расширяют pytest (покрытие, mock, asyncio, параллельность, фреймворки); устанавливаются как пакеты и подхватываются автоматически; при необходимости свой плагин регистрируют через entry point pytest11.

---

## §33a. Тестирование углублённо

**Цель подраздела:** знать **doctest**, **property-based testing** с **hypothesis**, **mutation testing** и таксономию **test doubles** (Stub, Mock, Spy, Fake, Dummy); использовать pytest.raises/warns, scope фикстур и продвинутый mock (spec, side_effect).

---

### Термины

| Термин | Определение |
|--------|-------------|
| **doctest** | Запуск примеров из docstrings как тестов; `doctest.testmod()`. |
| **Property-based testing** | Тестирование свойств (инвариантов): генератор даёт много входов, тест проверяет утверждение для всех; hypothesis — библиотека. |
| **Mutation testing** | Внесение мелких изменений в код (мутантов); если тесты не падают — мутант жив, тесты возможно недостаточны. |
| **Test double** | Заглушка вместо реального объекта: Stub (ответы), Mock (проверка вызовов), Spy (запись + проверка), Fake (упрощённая реализация), Dummy (placeholder). |

---

### doctest

В docstring пишут диалог интерпретатора:

```python
def add(a, b):
    """Return a + b.
    >>> add(1, 2)
    3
    """
    return a + b
```

**Запуск:** `python -m doctest mymodule.py` (проверяет все docstrings в модуле); или внутри кода: `doctest.testmod()` (при запуске файла как скрипта). Запуск одного модуля с подробным выводом: `python -m doctest mymodule.py -v`.

**Ограничения doctest:**

- **Чувствительность к выводу:** ожидаемый вывод должен **точно** совпадать с реальным (пробелы, переносы строк, представление чисел с плавающей точкой). Для float используют округление или не проверяют точное значение.
- **Порядок выполнения:** примеры выполняются последовательно в одном и том же глобальном пространстве имён; один пример может влиять на следующий (изменение переменных).
- **Побочные эффекты:** если пример печатает что-то случайное или зависит от времени/сети, тест нестабилен.
- **Сложная логика:** для ветвлений, циклов и больших данных предпочтительны обычные тесты (unittest/pytest); doctest лучше для коротких примеров использования в документации.

**Подавление вывода:** если вывод не важен, можно использовать директиву `# doctest: +ELLIPSIS` и заменить меняющуюся часть на `...` в ожидаемом выводе.

---

### hypothesis

**hypothesis** — библиотека для **property-based testing**: тест формулируется как **свойство** (инвариант), которое должно выполняться для **множества** входных данных. hypothesis **генерирует** входы по заданным **стратегиям** (integers, text, lists и т.д.) и многократно запускает тест; при падении выполняет **shrinking** — пытается найти минимальный контрпример.

**Установка:** `pip install hypothesis`.

**Базовый пример:**

```python
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert add(a, b) == add(b, a)
```

**Стратегии (кратко):**

| Стратегия | Назначение |
|-----------|------------|
| `st.integers()` | Целые числа; можно ограничить: `st.integers(min_value=0, max_value=100)`. |
| `st.floats()` | Числа с плавающей точкой. |
| `st.text()` | Строки (Unicode); можно ограничить алфавит: `st.text(alphabet="ab")`. |
| `st.booleans()` | True/False. |
| `st.lists(st.integers())` | Списки целых; можно ограничить длину: `min_size=0, max_size=10`. |
| `st.dictionaries(st.text(), st.integers())` | Словари с заданными ключами и значениями. |
| `st.tuples(st.integers(), st.text())` | Кортежи. |
| `st.one_of(st.integers(), st.text())` | Один из вариантов. |
| `st.sampled_from([1, 2, 3])` | Выбор из списка. |
| `st.builds(MyClass, x=st.integers())` | Построение объектов MyClass с полями из стратегий. |
| `@st.composite def custom(draw): ...` | Своя стратегия (draw для вложенных стратегий). |

**assume:** отсечь неинтересные входы без провала теста: `hypothesis.assume(x != 0)` — при x == 0 тест не считается провалом, hypothesis подберёт другой вход.

**Воспроизведение провала:** при падении hypothesis выводит в лог **reproduce_failure** с копируемым вызовом; его можно вставить в тест для воспроизведения: `@given(..., reproduce=...)`.

**Настройки hypothesis (кратко):** через декоратор **@settings** или глобально в **hypothesis.settings** можно задать: **max_examples** — сколько примеров сгенерировать (по умолчанию 100); **deadline** — максимальное время на один пример (по умолчанию 200 ms; для медленных тестов увеличить или отключить: `deadline=None`); **phases** — какие фазы выполнять (explicit, reuse, generate, shrink и т.д.). Пример: `@given(...) @settings(max_examples=500, deadline=500)` — больше примеров и дольше на каждый.

**Запомните:** property-based тесты проверяют инварианты на множестве входов; при падении shrinking даёт минимальный контрпример; стратегии задают область генерации.

---

### Mutation testing

**Mutation testing** (мутационное тестирование) оценивает **качество набора тестов**: в исходный код вносятся небольшие изменения (**мутанты**), и для каждого мутанта запускаются тесты. Если тесты **проходят** — мутант «выжил», то есть тесты не заметили изменение; если **падают** — мутант «убит», тесты достаточны для этого изменения. Цель — максимизировать долю убитых мутантов (mutation score).

**Типичные мутации (операторы):** замена `+` на `-`, `*` на `/`, константы на другую константу или 0, замена `True` на `False`, удаление вызова функции, замена условия `>` на `>=` и т.д.

**Инструменты:** **mutmut** (простой, Python), **cosmic-ray** (распределённый запуск). Запуск mutmut: `mutmut run` (в каталоге проекта); отчёт: `mutmut results`. Требует значительного времени (много мутантов × полный прогон тестов); часто используют выборочно (на критичных модулях) или в CI по расписанию (ночные прогоны).

---

### Test doubles

**Test double** — общий термин для объекта, подменяющего реальную зависимость в тесте. Таксономия (по Мезону и др.):

| Тип | Назначение | Пример |
|-----|------------|--------|
| **Stub** | Возвращает заданные ответы на вызовы; вызовы не проверяются. | Объект с методом `get_user()` всегда возвращает одного и того же пользователя. |
| **Mock** | Записывает вызовы и позволяет проверять (assert_called_once_with, call_count и т.д.). | Проверить, что `send_email` был вызван ровно один раз с нужными аргументами. |
| **Spy** | Обёртка над реальным объектом: вызовы проходят к реальной реализации и одновременно записываются для проверки. | Реальный HTTP-клиент + запись всех запросов. |
| **Fake** | Рабочая упрощённая реализация (не полная, но достаточная для тестов). | In-memory репозиторий вместо БД. |
| **Dummy** | Объект-заглушка, который не используется в тесте, но нужен для сигнатуры (например, передать в конструктор). | Передать None или пустой объект, если тест не проверяет эту зависимость. |

**В unittest.mock:** **Mock** — объект, записывающий вызовы и возвращающий по умолчанию новый Mock при доступе к атрибутам. **MagicMock** — то же, но с предопределёнными магическими методами (__len__, __iter__ и т.д.); удобно, когда подменяемый объект используется в операциях (len(obj), цикл for). **return_value** — что возвращать при вызове: `m.return_value = 42`. **side_effect** — вызываемая при вызове: если это исключение — оно выбрасывается; если итерируемый объект — при каждом вызове возвращается следующий элемент; если функция — вызывается с аргументами вызова и её результат возвращается. Пример: `m.side_effect = [1, 2, ValueError()]` — первые два вызова вернут 1 и 2, третий выбросит ValueError. **spec** (или **spec_set**) — список атрибутов или объект: только эти атрибуты разрешены; обращение к несуществующему атрибуту вызовет AttributeError (защита от опечаток). **patch.object(obj, 'attr', new=...)** подменяет атрибут объекта; **patch.dict** — подмена словаря (например, os.environ). **patch** по умолчанию подменяет объект в том модуле, где он **используется** (где делают import), а не где определён — патчить нужно «по месту использования».

#### Граничные случаи и отладка (§33a)

| Ситуация | Что проверить | Решение |
|----------|----------------|---------|
| hypothesis находит контрпример, тест падает | Условия в тесте, граничные значения. | Добавить assume() для неинтересных входов; сузить стратегии (min_value, max_value); проверить воспроизведение (reproduce_failure в логе). |
| mutation testing: много выживших мутантов | Тесты не покрывают ветки или границы. | Добавить тесты на граничные случаи и ветки; отключить мутации для части кода при необходимости. |
| Mock не проверяет вызовы | Использован return_value без assert. | Вызывать mock.assert_called_once_with(...) или assert_called_with; при side_effect проверять порядок вызовов. |

#### Частые вопросы (§33a)

| Вопрос | Краткий ответ |
|--------|----------------|
| Когда использовать hypothesis вместо обычных тестов? | Когда нужно проверить свойство на множестве входов (сортировка, инварианты, сериализация); для одного-двух примеров достаточно parametrize. |
| Stub vs Mock vs Fake? | Stub — только ответы; Mock — проверка вызовов; Fake — рабочая упрощённая реализация (например, in-memory БД). |

**Запомните:** doctest — быстрые примеры в docstrings; hypothesis — свойство для множества входов; mutation testing — проверка качества тестов; различайте Stub/Mock/Fake по цели (ответы vs проверка вызовов vs упрощённая реализация).

---

## §34. Документация и документационные строки
