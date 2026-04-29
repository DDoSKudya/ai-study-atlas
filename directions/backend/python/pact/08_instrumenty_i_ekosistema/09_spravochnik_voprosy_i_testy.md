[← Назад к индексу части VIII](index.md)


| Задача | Решение |
|--------|---------|
| Начать новый проект с изоляцией | `python3 -m venv .venv`, `source .venv/bin/activate`, `pip install -r requirements.txt` |
| Ошибка «externally-managed-environment» | Создать и активировать venv, не использовать системный pip |
| Воспроизводимые зависимости | pip-tools: requirements.in → pip-compile → requirements.txt; pip-sync |
| Офлайн-установка пакетов | На машине с сетью: `pip download -r requirements.txt -d ./wheels`; на целевой: `pip install --no-index --find-links ./wheels -r requirements.txt` |
| Описать проект и зависимости | pyproject.toml: [build-system], [project], dependencies |
| Собрать только wheel или только sdist | `python -m build --wheel` или `python -m build --sdist` |
| Собрать и опубликовать пакет | `python -m build`, `twine check dist/*`, `twine upload dist/*` |
| Разработка без переустановки пакета | `pip install -e .` (editable); при src layout импорт идёт из src/ |
| Добавить консольную команду из пакета | [project.scripts] в pyproject.toml, entry point типа `app = app.cli:main` |
| Обнаружить плагины в приложении | `from importlib.metadata import entry_points`; `entry_points(group="myapp.plugins")` |
| Единый стиль и проверки перед коммитом | Ruff (check + format) или Black + isort; pre-commit с хуками ruff, mypy |
| Включить только нужные правила Ruff | [tool.ruff.lint] select = ["E", "F", "I"]; ignore = ["E501"] |
| Проверить типы | `mypy mypkg` или pyright; strict в pyproject.toml; для legacy — overrides с ignore_errors |
| Запустить тесты с покрытием | `pytest --cov=mypkg --cov-report=term-missing` или `--cov-report=html` |
| Тесты на свойства с произвольными входами | hypothesis: @given и strategies (st.integers(), st.text() и т.д.) |
| Пропустить тест в unittest | `@unittest.skip("reason")` или `@unittest.skipIf(condition, "reason")` |
| Запустить один тест в pytest | `pytest path/to/test_file.py::test_name` или `pytest -k "test_name"` |
| Подменить зависимость в тесте | unittest.mock: `with patch("mymodule.attr", return_value=...)` или pytest-mock: `mocker.patch(...)` |
| Описать API в коде | docstrings по PEP 257; типы в docstrings (Google/NumPy) при отсутствии аннотаций |
| Сгенерировать документацию из docstrings | Sphinx + sphinx.ext.autodoc (+ napoleon для Google/NumPy); или MkDocs + mkdocstrings |
| Разделить зависимости prod и dev (pip-tools) | requirements.in — prod; requirements-dev.in с `-r requirements.in` и доп. пакетами; pip-compile оба; pip-sync requirements-dev.txt в CI |
| Установить CLI-инструмент глобально без засорения venv | pipx install black (или ruff, mypy); pipx run black . — без установки |
| Переключить версию Python в каталоге | pyenv local 3.12; в каталоге создаётся .python-version; при входе в каталог pyenv подставит эту версию |
| Экспорт зависимостей Poetry в requirements.txt | poetry export -f requirements.txt --output requirements.txt (для CI без Poetry) |
| Игнорировать правило Ruff в одном файле | [tool.ruff.lint.per-file-ignores] "path/to/file.py" = ["E501"] |
| Проверить типы только в одном модуле | mypy src/mypkg/module.py; или в overrides указать только этот модуль |
| Запустить только помеченные тесты в pytest | pytest -m "slow" (маркер slow зарегистрирован в pyproject.toml) |
| Воспроизвести падение hypothesis | В логе скопировать reproduce_failure и вставить в декоратор @given(..., reproduce=...) |
| Пропустить тест по условию (unittest) | @unittest.skipIf(condition, "reason") на методе или классе |
| Пропустить тест по условию (pytest) | @pytest.mark.skipif(condition, reason="...") |
| Патчить метод класса в тесте | patch.object(MyClass, "method", return_value=...) или mocker.patch.object(...) |
| Собрать только sdist для проверки MANIFEST.in | python -m build --sdist; распаковать .tar.gz и проверить список файлов |

---

## Краткое повторение терминологии

| Термин | Кратко |
|--------|--------|
| venv | Виртуальное окружение (stdlib); изоляция пакетов проекта |
| PEP 668 | Externally managed environment; запрет pip в системный Python |
| wheel / sdist | Бинарный формат установки / исходный дистрибутив |
| pyproject.toml | Единый конфиг сборки и метаданных (PEP 517/518/621) |
| Editable install | Установка «в режиме разработки», импорт из исходников |
| Entry point | Точка входа (CLI или плагин), объявленная в метаданных пакета |
| src layout | Код пакета в каталоге src/; рекомендуемая структура |
| py.typed | Маркер PEP 561: пакет предоставляет типы |
| Ruff / Black / isort | Линтер+форматтер / форматтер / сортировка импортов |
| pre-commit | Хуки Git для запуска проверок перед коммитом |
| mypy / pyright | Статическая проверка типов |
| typing_extensions | Бэкпорты типов для старых версий Python |
| pytest fixture / parametrize | Подготовка данных для теста / запуск с разными аргументами |
| hypothesis | Property-based testing: генерация входов по стратегиям |
| mutation testing | Проверка качества тестов через мутации кода |
| docstring (PEP 257) | Документационная строка в начале модуля/класса/функции |

---

## Вопросы по теме (с ответами)

<details>
<summary><strong>1.</strong> Зачем нужен venv, если можно ставить пакеты в систему?</summary>

Виртуальное окружение изолирует зависимости проекта от системного Python и от других проектов. Разные проекты могут требовать разные версии одних и тех же пакетов; в системе один общий site-packages. Кроме того, на многих дистрибутивах PEP 668 запрещает установку в системный Python (externally managed environment).
</details>

<details>
<summary><strong>2.</strong> Что такое PEP 668 и что делать при ошибке «externally-managed-environment»?</summary>

PEP 668 помечает среду как управляемую извне (например, пакетным менеджером ОС). pip отказывается устанавливать пакеты в такой среде. Решение: использовать venv или conda и не устанавливать пакеты в системный Python.
</details>

<details>
<summary><strong>3.</strong> Чем wheel отличается от sdist?</summary>

Wheel — готовый к установке бинарный (или универсальный) формат; установка быстрая. sdist — архив исходников; при установке из sdist вызывается бэкенд сборки (pyproject.toml [build-system]), который может собрать wheel и затем установить его.
</details>

<details>
<summary><strong>4.</strong> Что даёт editable install?</summary>

Установка пакета в режиме разработки: импорт идёт из исходников в репозитории. Изменения в коде видны сразу без переустановки пакета. Команда: <code>pip install -e .</code>
</details>

<details>
<summary><strong>5.</strong> Для чего нужен py.typed?</summary>

Пустой файл <code>package_name/py.typed</code> — маркер PEP 561: пакет поддерживает типизацию. mypy и pyright тогда используют аннотации из пакета (и не ищут отдельные stub-пакеты types-* по умолчанию).
</details>

<details>
<summary><strong>6.</strong> Зачем pre-commit?</summary>

Чтобы перед каждым коммитом автоматически запускались проверки (линтер, форматтер, типы, тесты). В репозиторий не попадёт код, не проходящий эти проверки (если хуки настроены и не обходятся принудительно).
</details>

<details>
<summary><strong>7.</strong> В чём разница между Stub и Mock в тестах?</summary>

Stub — заглушка, которая только возвращает заданные ответы; вызовы не проверяются. Mock — подмена, которая записывает вызовы и позволяет проверять (assert_called_once_with и т.д.). Stub для поведения, Mock для проверки взаимодействий.
</details>

<details>
<summary><strong>8.</strong> Что такое property-based testing в hypothesis?</summary>

Тест формулируется как свойство (инвариант), которое должно выполняться для множества входов. hypothesis генерирует входы по стратегиям (integers(), lists(), и т.д.) и многократно запускает тест. При падении выполняет shrinking к минимальному контрпримеру.
</details>

<details>
<summary><strong>9.</strong> Зачем нужен src layout и чем он лучше «пакета в корне»?</summary>

При src layout код пакета лежит в каталоге <code>src/</code>. Тесты и скрипты в корне не смешиваются с пакетом; при установке (в т.ч. editable) импорт идёт только из src/, поэтому тесты не «затеняют» модули пакета при импорте из текущей директории. Так тесты проверяют именно установленный пакет, а не локальные файлы в корне.
</details>

<details>
<summary><strong>10.</strong> В чём разница между <code>pip install -r requirements.txt</code> и <code>pip-sync requirements.txt</code>?</summary>

<code>pip install -r requirements.txt</code> устанавливает/обновляет пакеты из файла, но не удаляет лишние пакеты, уже установленные в окружении. <code>pip-sync requirements.txt</code> (pip-tools) приводит окружение в точное соответствие с файлом: устанавливает недостающее и удаляет всё, чего нет в requirements.txt.
</details>

<details>
<summary><strong>11.</strong> Когда использовать Poetry, а когда venv + pip + pip-tools?</summary>

Poetry даёт единый инструмент (зависимости + lock + сборка) и удобный CLI (poetry add, poetry run). venv + pip + pip-tools проще по стеку (только stdlib venv и pip), не требует Poetry в CI; lock — это requirements.txt от pip-compile. Выбор часто сводится к предпочтениям команды и к тому, нужна ли сборка пакетов через Poetry.
</details>

<details>
<summary><strong>12.</strong> Что такое «patch по месту использования» в unittest.mock?</summary>

Подменять нужно объект в том модуле, где он используется (где делают <code>import</code> или откуда вызывают), а не там, где он определён. Например, если в <code>mymodule.py</code> написано <code>from requests import get</code> и вызывается <code>get(...)</code>, патчить нужно <code>mymodule.get</code>, а не <code>requests.get</code>, иначе подмена не попадёт в mymodule.
</details>

<details>
<summary><strong>13.</strong> Зачем в pre-commit фиксировать ревизию (rev) репозитория хука?</summary>

Фиксация <code>rev</code> (тег или коммит) гарантирует, что у всех разработчиков и в CI запускается одна и та же версия инструмента (ruff, mypy и т.д.). Без фиксации при обновлении хука могут измениться правила и проверки — коммиты начнут падать по-другому. Обновлять ревизии осознанно: <code>pre-commit autoupdate</code>, затем прогнать тесты и линтер.
</details>

<details>
<summary><strong>14.</strong> В чём разница между <code>pip install -e .</code> и обычным <code>pip install .</code>?</summary>

<code>pip install .</code> копирует (или собирает и устанавливает) пакет в site-packages; изменения в исходниках не видны до повторной установки. <code>pip install -e .</code> (editable) не копирует пакет, а добавляет путь к исходникам в sys.path (через .pth или метаданные); импорт идёт из вашего дерева исходников, поэтому правки видны сразу без переустановки.
</details>

<details>
<summary><strong>15.</strong> Что такое Poetry-спецификаторы <code>^</code> и <code>~</code>?</summary>

<code>^3.9</code> — «совместимая» версия: <code>>=3.9, &lt;4.0</code> (для python). <code>~3.9.0</code> — «приближённая»: <code>>=3.9.0, &lt;3.10.0</code>. При <code>poetry add</code> Poetry выбирает последнюю версию в этом диапазоне и фиксирует её в poetry.lock.
</details>

<details>
<summary><strong>16.</strong> Зачем в pytest регистрировать маркеры в pyproject.toml?</summary>

Без регистрации при использовании <code>@pytest.mark.slow</code> pytest выведет предупреждение о неизвестном маркере (возможная опечатка). В <code>[tool.pytest.ini_options] markers</code> перечисляют допустимые маркеры и их описание; предупреждение исчезает, а <code>pytest --markers</code> покажет список маркеров.
</details>

<details>
<summary><strong>17.</strong> В чём разница между Mock и MagicMock в unittest.mock?</summary>

<strong>Mock</strong> — базовая заглушка; при обращении к атрибуту создаётся новый Mock. <strong>MagicMock</strong> — то же, но с предопределёнными магическими методами (__len__, __iter__, __str__ и т.д.). Если подменяемый объект используется в <code>len(obj)</code>, цикле <code>for x in obj</code> или в форматировании, удобнее MagicMock; для простых вызовов достаточно Mock.
</details>

<details>
<summary><strong>18.</strong> Зачем в фикстуре pytest использовать yield вместо return?</summary>

При <strong>yield</strong> код после yield выполняется после завершения теста (teardown) — в том числе при падении теста или исключении. Так можно гарантированно закрыть соединение, удалить файл, снять блокировку. При <strong>return</strong> фикстура просто возвращает значение; очистки после теста нет. Для ресурсов с явным освобождением используют yield.
</details>

<details>
<summary><strong>19.</strong> Когда использовать uv вместо pip?</summary>

uv быстрее pip (реализован на Rust); понимает pyproject.toml и requirements.txt; может создавать venv (uv venv) и компилировать зависимости (uv pip compile). В CI и локально можно заменить <code>pip install -r requirements.txt</code> на <code>uv pip install -r requirements.txt</code> для ускорения. Для полного lock-файла и UI как у Poetry — Poetry; для быстрого pip-совместимого workflow — uv.
</details>

<details>
<summary><strong>20.</strong> Зачем в pyproject.toml указывать requires-python?</summary>

Ограничение версий интерпретатора (например, <code>>=3.9</code>): pip не установит пакет в окружение с неподходящей версией Python. Это защищает пользователей от несовместимых установок и отображается на странице пакета на PyPI.
</details>

<details>
<summary><strong>21.</strong> Что такое MANIFEST.in и когда он нужен?</summary>

Файл в корне проекта, который указывает, какие файлы включить в sdist (исходный дистрибутив). По умолчанию бэкенд (setuptools) включает не всё (например, тесты или скрипты в корне могут не попасть). MANIFEST.in дополняет или переопределяет набор файлов для sdist. Директивы: include, exclude, recursive-include, recursive-exclude, graft, prune и др.
</details>

<details>
<summary><strong>22.</strong> Чем pytest.raises отличается от assertRaises в unittest?</summary>

Оба проверяют, что в блоке кода выбрасывается ожидаемое исключение. <code>pytest.raises</code> — контекстный менеджер: <code>with pytest.raises(ValueError): ...</code>; можно проверить сообщение: <code>pytest.raises(ValueError, match="regex")</code>. <code>assertRaises</code> в unittest вызывается как метод TestCase: <code>self.assertRaises(ValueError, func, arg)</code> или как контекстный менеджер. По смыслу эквивалентны; синтаксис разный.
</details>

<details>
<summary><strong>23.</strong> Зачем в conda environment.yml секция pip: и что такое conda env export --from-history?</summary>

В <code>dependencies</code> можно перечислить пакеты из репозиториев conda; пакеты, которых нет в conda (или нужна конкретная версия с PyPI), указывают в подсекции <code>pip:</code> — conda установит их через pip в то же окружение. <code>conda env export --from-history</code> экспортирует только те пакеты, которые вы явно устанавливали (<code>conda install ...</code>); транзитивные зависимости не попадают в файл. Удобно для минимального environment.yml; при <code>conda env create -f environment.yml</code> conda сам подтянет зависимости. Для полной воспроизводимости используют экспорт без --from-history.
</details>

<details>
<summary><strong>24.</strong> Чем black --check отличается от black . и black --diff?</summary>

<code>black .</code> переформатирует файлы на месте. <code>black --check .</code> не меняет файлы, только проверяет соответствие стилю; при несоответствии выходит с ненулевым кодом (удобно в CI). <code>black --diff .</code> выводит diff между текущим кодом и отформатированным, без записи в файлы.
</details>

---

### Типичные ошибки (Часть VIII)

| Ошибка | Почему плохо | Как правильно |
|--------|---------------|---------------|
| Устанавливать пакеты в системный Python на Linux | Конфликт с пакетами ОС, PEP 668 блокирует | Всегда venv или conda |
| Не фиксировать версии в requirements.txt | Разные окружения получают разные версии, невоспроизводимые баги | pip freeze или pip-tools (pip-compile) |
| Игнорировать py.typed в типизированном пакете | mypy/pyright не используют типы из пакета | Добавить пустой файл package/py.typed |
| Писать тесты без изоляции (реальная БД, сеть) | Тесты хрупкие, медленные, зависят от окружения | Mock/fixture для внешних зависимостей |
| Не настраивать pre-commit | В репозиторий попадает код, не проходящий линтер/типы | .pre-commit-config.yaml + pre-commit install |
| Docstring без первой строки-резюме | Сложнее ориентироваться в API | PEP 257: первая строка — краткое описание |
| Патчить не то место в mock | Подмена не срабатывает в тесте | Патчить по месту использования: модуль, где вызывают, а не где определяют |
| Забыть закоммитить poetry.lock / requirements.txt | Разные версии у разработчиков и в CI | Всегда коммитить lock-файл и пересобирать при изменении зависимостей |
| Патчить requests.get вместо mymodule.get | Подмена не срабатывает | Патчить по месту использования: модуль, где импортируют и вызывают |
| Фикстура без yield при ресурсе с очисткой | Ресурс не освобождается при падении теста | Использовать yield: код после yield — teardown, выполняется всегда |
| Не указывать --cov при нескольких пакетах | Покрытие считается по всему дереву или не тому пакету | Явно задать --cov=src или --cov=mypkg |
| Забыть pipx ensurepath | Команды установленных через pipx приложений не в PATH | Выполнить pipx ensurepath и перезапустить терминал |
| Указывать пароль PyPI вместо токена в twine | Загрузка может быть отклонена или небезопасна | В .pypirc и TWINE_PASSWORD использовать API-токен (pypi-...) |
| Не добавлять sys.path в conf.py для Sphinx | autodoc не импортирует пакет, docstrings не извлекаются | sys.path.insert(0, os.path.abspath('..')) в conf.py |
| Игнорировать poetry.lock при merge | Разные версии зависимостей у разработчиков | После merge выполнить poetry lock и закоммитить обновлённый lock |

---

### Отладка и диагностика (Часть VIII)

| Проблема | Что проверить |
|----------|----------------|
| venv: пакеты не находятся при импорте | Активно ли окружение (`echo $VIRTUAL_ENV`); путь к site-packages в `python -c "import site; print(site.getsitepackages())"`. |
| build/twine: ошибка при сборке или загрузке | Вывод `python -m build` и `twine check dist/*`; соответствие имени пакета и версии в pyproject.toml и имени файлов в dist/. |
| mypy: много ошибок после включения strict | Включить strict по модулям через overrides; исправлять по одному модулю; для legacy — временно ignore_errors. |
| pytest: тесты не находятся | Имена файлов test_*.py или *_test.py; имена функций test_*; каталог в аргументах pytest. |
| pre-commit не запускается | Выполнено ли `pre-commit install`; наличие .pre-commit-config.yaml; права на исполнение хуков. |
| pip install из sdist долго или падает | Нет подходящего wheel; сборка требует компилятора/заголовков. | Установить build-зависимости (gcc, python3-dev); или использовать готовый wheel с другой машины. |
| Poetry lock конфликтует при merge | Два разработчика обновили зависимости по-разному. | Оставить одну версию pyproject.toml, выполнить `poetry lock` заново, закоммитить обновлённый poetry.lock. |
| Sphinx не находит модули при make html | Пакет не в sys.path при сборке. | В conf.py добавить `sys.path.insert(0, os.path.abspath('..'))` (или путь к src/). |
| Ruff не находит конфиг при запуске из подкаталога | Поиск конфига идёт вверх по дереву. | Запускать из корня проекта или указать --config ../pyproject.toml. |
| pip-sync удалил нужный пакет | В requirements.txt его не было (забыли добавить в .in и пересобрать). | Добавить пакет в requirements.in, pip-compile, затем pip-sync. |
| coverage показывает 0% для части модулей | --cov указывает не на тот каталог или модули не импортируются в тестах. | Указать --cov=src и --cov=mypkg явно; убедиться, что тесты импортируют код (при src layout — pip install -e .). |
| Entry point не загружается в приложении | Пакет с entry point установлен в другое окружение. | Установить пакет в то же venv, что и приложение; проверить group и name. |
| hypothesis тест нестабильно падает | Случайные входы каждый раз разные. | Использовать reproduce= из лога для воспроизведения; сузить стратегии. |

---

### Вопросы и задания для самопроверки

1. Создайте venv, активируйте его и установите пакет `requests`; сохраните вывод `pip freeze` в файл и восстановите окружение в новом venv по этому файлу.
2. Напишите минимальный `pyproject.toml` с [build-system] (setuptools) и [project] (имя, версия, одна зависимость).
3. Объясните разницу между wheel и sdist и когда pip выбирает тот или иной формат при установке.
4. Настройте Ruff в pyproject.toml (line-length 88, выбор правил E, F, I) и запустите `ruff check .` и `ruff format .`; добавьте per-file-ignores для каталога tests.
5. Включите strict mode для mypy в pyproject.toml и исправьте типы в одном модуле; для другого модуля настройте overrides с ignore_errors.
6. Напишите pytest-тест с фикстурой (например, временный файл через tmp_path) и параметризацией по двум наборам аргументов; добавьте тест с pytest.raises.
7. Оформите docstring функции по PEP 257 (однострочный и многострочный вариант); добавьте типы в стиле Google (Args, Returns).
8. Настройте pre-commit с хуками ruff и ruff-format; выполните `pre-commit run --all-files`.
9. Напишите hypothesis-тест для функции, принимающей два целых числа (стратегия st.integers()); проверьте свойство коммутативности или ассоциативности.
10. Объясните разницу между Stub, Mock и Fake в тестах и приведите пример использования Mock с assert_called_once_with.

11. Создайте минимальный .pre-commit-config.yaml с одним хуком (ruff) и выполните `pre-commit run --all-files`; объясните, зачем фиксировать rev.

12. Опишите по шагам, как загрузить пакет на Test PyPI и установить его оттуда через pip.

13. Напишите pytest-тест с фикстурой scope="class" и двумя методами теста в одном классе; убедитесь, что фикстура создаётся один раз на класс.

14. Подмените в тесте функцию из другого модуля через patch (декоратор и контекстный менеджер); проверьте вызов через assert_called_once_with.

15. Напишите hypothesis-тест с @settings(max_examples=50) и стратегией st.lists(st.integers(), max_size=5); проверьте инвариант (например, что sorted(lst) == sorted(lst)[::-1][::-1]).

---

## Резюме по Части VIII

**Часть VIII** охватывает инструменты и экосистему Python:

- **§28** — виртуальные окружения: venv, PEP 668 (externally managed), pip, pip-tools, ensurepip, zipapp.
- **§29** — pyproject.toml: [build-system], [project], зависимости, PEP 440.
- **§29a** — упаковка: wheel, sdist, build, twine, editable install, entry points, MANIFEST.in, src layout, py.typed.
- **§30** — менеджеры: Poetry, uv, pipx, conda, pyenv.
- **§31–31a** — линтеры и форматтеры (Ruff, Pylint, Black, isort), конфигурация и pre-commit.
- **§32** — проверка типов: mypy, pyright, typing_extensions.
- **§33–33a** — тестирование: unittest, pytest (фикстуры, параметризация), mocking, coverage, doctest, hypothesis, mutation testing, test doubles.
- **§34** — документация: docstrings (PEP 257), Sphinx, MkDocs.

Практика: всегда использовать venv (или conda) на системах с PEP 668; держать метаданные и сборку в pyproject.toml; применять линтер/форматтер и проверку типов (в т.ч. через pre-commit); писать тесты (pytest + при необходимости hypothesis) и документировать API (docstrings).

**Версии Python (Часть VIII):**

| Версия / PEP | Нововведения, затронутые в Части VIII |
|--------------|---------------------------------------|
| **3.3** | venv в stdlib |
| **3.4** | ensurepip в stdlib |
| **PEP 517/518** | pyproject.toml, [build-system] |
| **PEP 621** | [project] в pyproject.toml |
| **PEP 561** | py.typed для типизированных пакетов |
| **PEP 668** | Externally managed environment (защита системного Python) |
| **3.10+** | importlib.metadata.entry_points() — новый API (возврат EntryPoints) |

---

### Примеры из практики (Часть VIII)

| Сценарий | Что сделать по шагам |
|----------|----------------------|
| **Новый проект с нуля** | 1) `python3 -m venv .venv`; 2) `source .venv/bin/activate`; 3) `pip install --upgrade pip`; 4) создать requirements.in с верхнеуровневыми зависимостями; 5) `pip-compile requirements.in`; 6) `pip-sync requirements.txt`; 7) добавить pyproject.toml с [build-system] и [project] при необходимости упаковки. |
| **Клонировали репозиторий** | 1) `python3 -m venv .venv`; 2) активировать venv; 3) `pip install -r requirements.txt` (или `poetry install` при Poetry); 4) запустить тесты: `pytest`. |
| **Публикация пакета на PyPI** | 1) Проверить pyproject.toml ([build-system], [project], версия); 2) `python -m build`; 3) `twine check dist/*`; 4) `twine upload dist/*` (токен PyPI). |
| **Добавить линтер и pre-commit в старый проект** | 1) Добавить [tool.ruff] в pyproject.toml; 2) `pip install ruff pre-commit`; 3) создать .pre-commit-config.yaml с ruff и ruff-format; 4) `pre-commit install`; 5) `pre-commit run --all-files` и исправить нарушения. |
| **Включить mypy в существующем коде** | 1) Добавить [tool.mypy] с strict = false или выборочными опциями; 2) Запустить mypy, исправить критические ошибки; 3) Для legacy-модулей добавить [[tool.mypy.overrides]] с ignore_errors = true; 4) Постепенно включать strict по модулям. |
| **Использовать приватный PyPI или зеркало** | В requirements.txt первой строкой: `--extra-index-url https://my-index/simple/` или при установке: `pip install --index-url https://... mypackage`. В CI задать переменные PIP_INDEX_URL / PIP_EXTRA_INDEX_URL. |
| **Очистить кеш pip** | `pip cache purge` — удалить весь кеш; `pip cache dir` — путь к кешу; при невоспроизводимых установках в CI часто используют `pip install --no-cache-dir`. |
| **Установить несколько версий Python и переключаться** | 1) Установить pyenv (или asdf); 2) `pyenv install 3.12.0`; 3) `pyenv local 3.12.0` в каталоге проекта (создаётся .python-version); 4) создать venv: `python -m venv .venv` (будет использована выбранная версия). |
| **Добавить консольную команду в свой пакет** | 1) В pyproject.toml: [project.scripts] с записью `cmd = mypkg.cli:main`; 2) Реализовать функцию main() в mypkg/cli.py; 3) После `pip install -e .` команда `cmd` будет в PATH. |
| **Запустить тесты с покрытием и порогом в CI** | `pytest --cov=src --cov-report=term-missing --cov-fail-under=80`; при покрытии ниже 80% выход с ошибкой. |
| **Подменить зависимость в pytest-тесте** | Использовать pytest-mock: в тест передаётся фикстура mocker; `mocker.patch("mymodule.external_api", return_value=...)`; проверить вызов: `mymodule.external_api.assert_called_once_with(...)`. |
| **Запустить проверки pre-commit только при push** | В .pre-commit-config.yaml для хука указать `stages: [push]` (по умолчанию stages: [commit]). |
| **Увеличить число примеров в hypothesis** | Декоратор @settings(max_examples=500) или глобально hypothesis.settings(max_examples=500). |

---

### Когда что использовать (краткая сводка)

| Задача | Рекомендация |
|--------|--------------|
| Изоляция зависимостей проекта | Всегда venv (или conda); на Linux с PEP 668 — обязательно. |
| Воспроизводимые версии зависимостей | pip-tools (requirements.in → pip-compile → requirements.txt) или Poetry (poetry.lock). |
| Один конфиг проекта и сборки | pyproject.toml с [build-system] и [project] (PEP 517/518/621). |
| Разработка пакета без переустановки | `pip install -e .` (editable); желательно src layout. |
| Линтинг и форматирование | Ruff (check + format) — один инструмент; при необходимости Black + isort отдельно. |
| Проверки перед коммитом | pre-commit с хуками ruff, mypy (и при необходимости pytest). |
| Проверка типов | mypy или pyright; для новых проектов — strict; для библиотек с поддержкой старых Python — typing_extensions. |
| Тесты | pytest (фикстуры, параметризация); unittest — если нужна совместимость со stdlib без зависимостей. |
| Property-based тесты | hypothesis с @given и стратегиями. |
| Документация API | docstrings по PEP 257; генерация — Sphinx (autodoc) или MkDocs (mkdocstrings). |
| CLI-инструменты глобально (black, ruff, mypy) | pipx install; не ставить в каждый venv. |
| Быстрая установка в CI | uv pip install -r requirements.txt (быстрее pip). |
| Data science / научный стек (NumPy, PyTorch из бинарников) | conda или mamba; канал conda-forge. |
| Legacy-проект без pyproject.toml | venv + pip-tools; .flake8 или setup.cfg для линтера; mypy.ini при необходимости. |
| Типизированная библиотека для Python 3.9+ | typing_extensions для Self, TypeAlias и др.; py.typed в пакете. |

---

**Связь с другими частями плана:** Часть IX — миграция Py2→Py3 (2to3, six, future). Часть III — модули stdlib (argparse, logging, json и др.), используемые в приложениях и тестах.
