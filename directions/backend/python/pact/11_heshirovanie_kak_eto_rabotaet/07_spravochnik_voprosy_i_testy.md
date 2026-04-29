[← Назад к индексу части XI](index.md)


### Частые сценарии

| Задача | Решение |
|--------|---------|
| Сделать объект ключом dict / элементом set | Объект должен быть hashable: `hash(obj)` не бросает TypeError; `a==b` ⇒ `hash(a)==hash(b)` |
| Переопределить равенство и использовать в set | Определить согласованный `__hash__` (по тем же полям, что `__eq__`) или `__hash__ = None` |
| Воспроизводимые тесты с dict/set | Запуск с `PYTHONHASHSEED=0` |
| Хешировать составной ключ | `hash((a, b, c))` — tuple из hashable полей |
| Сделать класс не hashable | `__hash__ = None` в классе |
| Использовать list/dict как ключ | Преобразовать в tuple/frozenset: `tuple(lst)`, `frozenset(d.items())` |
| Кешировать результат по аргументам | `@functools.lru_cache` — аргументы должны быть hashable |
| Проверить, hashable ли объект | `try: hash(obj); return True except TypeError: return False` |
| Hashable-ключ для weakref.WeakKeyDictionary | Пользовательский класс (с `__hash__` и `__eq__`) или встроенный hashable-тип |
| Криптографический хеш (пароли, файлы) | `hashlib.sha256()`, `hashlib.blake2b()` — не `hash()` |

### Терминология (полный список)

| Термин | Краткое определение |
|--------|---------------------|
| **hash** | Целое число — «отпечаток» объекта для индексации в хеш-таблицах; вызывается `obj.__hash__()` |
| **hashable** | Объект: `hash(obj)` стабилен; `a == b` ⇒ `hash(a) == hash(b)`; можно использовать как ключ dict / элемент set |
| **контракт hashable** | Два условия: (1) `hash(a)` стабилен за время жизни; (2) `a == b` ⇒ `hash(a) == hash(b)` |
| **хеш-таблица** | Массив слотов; индекс из хеша; O(1) в среднем для get/set/delete |
| **bucket** | Один слот хеш-таблицы |
| **коллизия** | Два разных ключа дают один индекс (либо одинаковый хеш, либо совпадение `hash % size`) |
| **open addressing** | Разрешение коллизий: при занятом слоте ищем следующий свободный (probing) |
| **chaining** | Альтернатива: в каждом слоте — связный список элементов |
| **perturb** | В CPython: использование старших бит хеша при вычислении следующего индекса; уменьшает кластеризацию |
| **load factor** | Заполненность таблицы (занятые слоты / общее число); при превышении порога — resize |
| **resize** | Увеличение размера таблицы при переполнении; перехеширование всех элементов. CPython не уменьшает dict при удалении. |
| **PYTHONHASHSEED** | Переменная окружения: `random` — защита от DoS; `0` — детерминированный хеш |
| **SipHash** | Криптографически стойкая хеш-функция для str/bytes в Python (PEP 456) |
| **hash-flooding DoS** | Атака: подбор ключей с коллизиями → деградация dict до O(n²) |
| **sys.hash_info** | Параметры хеширования CPython: width, modulus, algorithm и др. |

### Вопросы для самопроверки (по разделам)

#### §52. Хеш-функция

<details>
<summary>1. В чём разница между hash(obj) и id(obj)?</summary>

`id(obj)` — уникальный идентификатор объекта (адрес в памяти), меняется между запусками. `hash(obj)` — число для хеш-таблиц; для равных объектов должен быть одинаковым; `hash` не обязан быть уникальным (коллизии допустимы).
</details>

<details>
<summary>2. В чём разница между hash() и hashlib?</summary>

`hash()` — для быстрого поиска в dict/set; возвращает int; не для криптографии; зависит от PYTHONHASHSEED (для str/bytes). `hashlib` — криптографические хеши (MD5, SHA-256, BLAKE2); принимает bytes; детерминирован; для паролей, подписей, проверки целостности.
</details>

<details>
<summary>3. Почему hash(-1) == -2 в Python?</summary>

Во внутренней структуре dict значение -1 используется как маркер «пустой слот». Чтобы ключ `-1` не конфликтовал с маркером, `hash(-1)` возвращает -2.
</details>

#### §53. Контракт hashable

<details>
<summary>1. Почему list нельзя положить в set?</summary>

list мутабельный. Хеш должен быть стабильным. Если хеш по содержимому — после изменения объект «потеряется» в set. Если по id — `a == b` при `a is not b` даст разные хеши (нарушение контракта). Поэтому list не hashable.
</details>

<details>
<summary>2. Можно ли использовать dict как ключ другого dict?</summary>

Нет. dict не hashable. Можно использовать `tuple(sorted(d.items()))` или `frozenset(d.items())` для неизменяемого представления; при изменении исходного dict представление не обновится.
</details>

<details>
<summary>3. hash((1, [2])) — что произойдёт и почему?</summary>

`TypeError: unhashable type: 'list'`. Кортеж хешируется рекурсивно по элементам; один не-hashable элемент делает весь кортеж не-hashable.
</details>

#### §54. Хеш-таблицы

<details>
<summary>1. Почему & (size-1) быстрее % size?</summary>

Когда size — степень двойки, `h % size` эквивалентно `h & (size - 1)`. Битовое AND выполняется за один такт; взятие остатка от деления — дороже. Поэтому размер таблицы dict всегда степень двойки.
</details>

<details>
<summary>2. Почему dict хранит порядок вставки, а set — нет?</summary>

dict с Python 3.6+ использует структуру indices + entries: entries — плотный массив в порядке вставки, итерация идёт по нему. set реализован аналогично, но порядок итерации зависит от хешей и истории; гарантия порядка для set не дана.
</details>

<details>
<summary>3. Что такое load factor и зачем он нужен?</summary>

Load factor — отношение занятых слотов к общему числу. При слишком высоком значении много коллизий, поиск замедляется. CPython делает resize при превышении порога (~2/3), чтобы сохранить O(1).
</details>

#### §55. Коллизии и перехеширование

<details>
<summary>1. Как CPython разрешает коллизии в dict?</summary>

Open addressing с perturb-схемой: при занятом слоте используется формула с битовым сдвигом хеша (`h >>= 5`, `i = (i*5+1+h) & mask`) для вычисления следующего индекса. Не chaining.
</details>

<details>
<summary>2. Почему при удалении слот не помечают «пусто», а «удалён»?</summary>

Иначе разорвётся цепочка проб: элементы, которые «остановились» в слоты после удалённого, стали бы невидимыми при поиске. Маркер «удалён» сохраняет цепочку, но позволяет вставить новый ключ в этот слот.
</details>

<details>
<summary>3. Уменьшает ли CPython размер dict при массовом удалении?</summary>

Нет. CPython не уменьшает размер dict при удалении элементов. Таблица остаётся прежнего размера; память не освобождается.
</details>

#### §56. Слабые ссылки и хеши

<details>
<summary>1. Почему WeakKeyDictionary требует hashable-ключи?</summary>

Внутри используется хеш-таблица для быстрого поиска по ключу. `hash(key)` нужен для индексации; без hashable ключа работа невозможна.
</details>

<details>
<summary>2. Можно ли использовать WeakKeyDictionary с классом, у которого __slots__?</summary>

Да, но в `__slots__` нужно добавить `__weakref__`. Без него объект не поддерживает слабые ссылки — `TypeError: cannot create weak reference`.
</details>

<details>
<summary>3. Почему weakref.ref(42) и weakref.ref("hello") вызывают ошибку?</summary>

Встроенные типы (int, str) не поддерживают слабые ссылки: нет слота для их хранения. Плюс мелкие int и части строк интернированы — живут вечно, слабые ссылки на них мало осмыслены.
</details>

#### §57. Кастомный __hash__

<details>
<summary>1. Когда нужно переопределять __hash__?</summary>

Когда переопределяете `__eq__` и хотите, чтобы объекты были hashable. Нужно либо определить согласованный `__hash__` (по тем же полям, что `__eq__`), либо `__hash__ = None` (объект не hashable).
</details>

<details>
<summary>2. Что будет, если __hash__ возвращает константу для всех экземпляров?</summary>

Технически контракт не нарушен (все равны по `__eq__` ⇒ один хеш). Но все разные объекты тоже получат один хеш — сплошная коллизия, поиск выродится в O(n). Так делать не нужно.
</details>

<details>
<summary>3. Как dataclass связан с __hash__?</summary>

`@dataclass` без `frozen` не даёт `__hash__` (есть `__eq__` → Python ставит `__hash__ = None`). `@dataclass(frozen=True)` автоматически генерирует `__hash__` по полям. `field(hash=False)` исключает поле из хеша.
</details>

#### §57a. PYTHONHASHSEED и детерминированность

<details>
<summary>1. Зачем нужен PYTHONHASHSEED=random?</summary>

Защита от hash-flooding DoS: атакующий не может предсказать хеши str/bytes и подобрать ключи с коллизиями. SipHash + случайный seed делают атаку нереализуемой.
</details>

<details>
<summary>2. Гарантирован ли порядок элементов в set?</summary>

Нет. Порядок set не гарантирован; зависит от хешей и истории вставок. Между запусками с разным PYTHONHASHSEED порядок может меняться.
</details>

<details>
<summary>3. Какие типы зависят от PYTHONHASHSEED?</summary>

str, bytes, datetime — да. int, float, tuple — не зависят; их хеш детерминирован в рамках одной версии CPython.
</details>

#### Практические задачи и справочник

<details>
<summary>1. Как дедуплицировать список кортежей с сохранением порядка?</summary>

`list(dict.fromkeys(pairs))` (Python 3.7+) или цикл с set: `seen = set(); [x for x in pairs if x not in seen and not seen.add(x)]`.
</details>

<details>
<summary>2. lru_cache не работает с list в аргументах — как обойти?</summary>

Преобразовать list в tuple до вызова: обёртка принимает `tuple(items)`, внутренняя функция — `list`; вызывающий передаёт `tuple(my_list)`.
</details>

<details>
<summary>3. Как проверить, hashable ли объект?</summary>

`try: hash(obj); return True` `except TypeError: return False`. Либо `isinstance(obj, collections.abc.Hashable)`.
</details>

### Отладка: пошаговый разбор типичных ошибок

#### Ошибка: `TypeError: unhashable type: 'list'`

**Что произошло:** вы попытались использовать list как ключ dict или элемент set.

**Пошагово:**
1. Вы написали `d[[1, 2]] = 3` или `s = {[1, 2], [3, 4]}`.
2. Python вызвал `hash([1, 2])`.
3. У типа `list` метод `__hash__` не определён (точнее, `list.__hash__ is None`).
4. `hash()` получил `None` или отсутствие метода → `TypeError`.

**Решение:** преобразовать в tuple: `d[tuple([1, 2])] = 3` или `s = {tuple(x) for x in [[1,2], [3,4]]}`.

**Trace при выполнении:**
```
d[[1, 2]] = 3
    → Python: d.__setitem__([1, 2], 3)
    → dict: нужно вычислить индекс для ключа [1, 2]
    → dict: index = f(hash([1, 2]), size)
    → hash([1, 2])
    → type([1, 2]).__hash__([1, 2])
    → list.__hash__ is None
    → TypeError: unhashable type: 'list'
```

#### Ошибка: равные объекты «разъехались» в set

**Симптом:** `a == b`, но `len({a, b}) == 2` (должно быть 1).

**Причина:** нарушение контракта: `__hash__` не согласован с `__eq__`. Либо хешируются не те поля, либо порядок полей в tuple другой.

**Проверка:**
```python
assert a == b
assert hash(a) == hash(b), "Нарушение контракта: __hash__ не согласован с __eq__"
```

**Решение:** переопределить `__hash__` так, чтобы хешировались те же поля, что в `__eq__`, в том же порядке.

### Типичные ошибки

| Ошибка | Почему плохо | Как правильно |
|--------|--------------|---------------|
| Переопределить `__eq__`, не трогая `__hash__` | Python 3 ставит `__hash__ = None`; равные объекты не смогут быть в set/dict | Либо `__hash__` по полям из `__eq__`, либо явно `__hash__ = None` |
| Хешировать не те поля, что в `__eq__` | `a == b` может быть True, но `hash(a) != hash(b)` — объекты «потеряются» в set | Хешировать те же поля, что в `__eq__` |
| Менять поля hashable-объекта после добавления в set | Нарушение инварианта: хеш изменился, поиск не сработает | Делать объект immutable |
| Использовать `hash()` для паролей | `hash()` не криптографический; предсказуем при PYTHONHASHSEED=0 | `hashlib`, `hmac`, `secrets` |
| Полагаться на порядок set | Порядок не гарантирован | Использовать list или dict (порядок вставки) |
| Передавать list в lru_cache | list не hashable | Преобразовать в tuple |
| Забыть `__weakref__` в `__slots__` при использовании weakref | TypeError при создании weakref | Добавить `__weakref__` в `__slots__` |

### Связь с другими частями плана

| Тема | Связь |
|------|-------|
| Часть X (§40–41) | `__eq__`, `__hash__` — магические методы; контракт hashable |
| Часть X (§51c) | Таблица оператор→метод: `hash(obj)` → `__hash__` |
| §15 hashlib | `hashlib` vs `hash()`; криптографические хеши |
| §10 dataclass | `frozen=True` → автоматический `__hash__`; `field(hash=False)` |
| §12 functools | `lru_cache` — аргументы должны быть hashable |
| §70–84 Алгоритмы | Хеш-таблицы: O-нотация, коллизии, структуры данных |
| §96 weakref | WeakKeyDictionary, WeakSet — требуют hashable |

### Диагностика и отладка

**Проверка хеша:**
```python
hash(obj)  # Вызовет TypeError, если объект не hashable
```

**Параметры хеширования:**
```python
import sys
sys.hash_info           # width, modulus, algorithm, seed_bits, ...
sys.hash_info.algorithm # 'siphash24'
sys.hash_info.width     # 64 (на 64-битной платформе)
```

**Проверка hashable:**
```python
def is_hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False
```

**Отладка «почему объект не в set/dict»:**
1. Убедиться, что объект hashable: `hash(obj)` не бросает TypeError.
2. Проверить согласованность `__eq__` и `__hash__`: если `a == b`, то `hash(a) == hash(b)`.
3. Убедиться, что поля, участвующие в `__eq__`/`__hash__`, не меняются после добавления в set/dict.
4. Для вложенных структур (tuple, frozenset): все элементы должны быть hashable; один не-hashable — весь объект не hashable.

**Воспроизводимость (для отладки):** установить `PYTHONHASHSEED=0` перед запуском. Тогда хеши str/bytes будут одинаковы между запусками.

**Типичная ошибка «unhashable type»:** объект (list, dict, set и т.д.) используется как ключ dict или элемент set. Решение: преобразовать в tuple/frozenset или использовать другой hashable-тип. Например: `tuple(my_list)`, `frozenset(my_set)`, `tuple(d.items())` для представления dict. Для dict с неупорядоченными ключами — `tuple(sorted(d.items()))` или `frozenset(d.items())` (если порядок не важен).

**Ошибка «TypeError: unhashable type» в lru_cache:** один из аргументов декорированной функции не hashable (list, dict, set). Решение: передавать tuple вместо list, frozenset вместо set; для dict — `tuple(d.items())` или создать hashable-обёртку.

### Дополнительные сценарии (расширенный список)

| Сценарий | Решение |
|----------|---------|
| Удалить дубликаты из списка кортежей с сохранением порядка | `list(dict.fromkeys(pairs))` (3.7+) или цикл с set |
| Кешировать по (a, b) где a — int, b — list | Обёртка: внутренняя функция принимает `tuple(b)` |
| Использовать объект datetime как ключ dict | OK — datetime hashable (tzinfo должен быть hashable или None) |
| Сравнить два dict по содержимому как ключ | `tuple(sorted(d1.items())) == tuple(sorted(d2.items()))` — hashable представление |
| Frozen dataclass с полем-списком | Список должен быть неизменяемым (не менять после создания); или использовать tuple |

### Резюме

**Часть XI** связывает теорию хеширования с практикой Python:

- **hash(obj)** → `obj.__hash__()`; число для индексации в хеш-таблицах; не путать с hashlib.
- **Hashable** = стабильный хеш + `a == b` ⇒ `hash(a) == hash(b)`; мутабельные типы (list, dict, set) не hashable.
- **dict, set** — хеш-таблицы с open addressing и perturb; dict хранит порядок вставки (3.7+); set — нет.
- **Коллизии** неизбежны (принцип Дирихле); разрешаются probing; при load factor > порога — resize.
- **Кастомный __hash__:** при переопределении `__eq__` — согласованный `__hash__` или `__hash__ = None`.
- **PYTHONHASHSEED:** random — защита от DoS; 0 — воспроизводимость. SipHash для str/bytes.

### Дополнительно: collections.abc.Hashable

Модуль `collections.abc` определяет абстрактный класс `Hashable`:

```python
from collections.abc import Hashable
isinstance(42, Hashable)      # True
isinstance([1, 2], Hashable)  # False
isinstance((1, 2), Hashable)  # True
```

Класс считается подтипом `Hashable`, если реализует `__hash__` и `__eq__` (и не устанавливает `__hash__ = None`). Используется для проверки типов и аннотаций: `def f(key: Hashable) -> ...`. `typing.Hashable` — алиас для `collections.abc.Hashable`.

### Ключевые выводы по разделам (краткая сводка)

| Раздел | Главный вывод |
|--------|---------------|
| §52 | `hash(obj)` → `__hash__`; число для dict/set; не путать с hashlib. int/float/str/tuple/frozenset — свои формулы. |
| §53 | Hashable = стабильный хеш + `a==b` ⇒ `hash(a)==hash(b)`. tuple — да, list — нет (immutable vs mutable). |
| §54 | dict/set — хеш-таблицы; indices + entries; perturb; порядок dict (3.7+) — порядок вставки. |
| §55 | Коллизии неизбежны; open addressing; resize при load factor; маркер «удалён» при delete. |
| §56 | WeakKeyDictionary, WeakSet — требуют hashable; при `__slots__` нужен `__weakref__`. |
| §57 | При `__eq__` — либо `__hash__` по тем же полям, либо `__hash__ = None`. |
| §57a | PYTHONHASHSEED: random — DoS-защита; 0 — воспроизводимость. SipHash для str/bytes. |
