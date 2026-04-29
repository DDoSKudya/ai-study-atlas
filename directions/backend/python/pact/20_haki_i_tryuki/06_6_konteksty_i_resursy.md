[← Назад к индексу части XX](index.md)

## 6. Контексты и ресурсы (§114)

### 6.0. Главная идея §114 (на пальцах)

Контекстный менеджер (`with`) нужен для одной простой цели:

> **гарантировать уборку** (закрыть файл, освободить ресурс), даже если случилась ошибка.

Если объяснить совсем просто, `with` — это «делай работу» + «в любом случае прибери за собой».

### 6.1. Несколько ресурсов в одном `with`

Python позволяет открывать несколько ресурсов в **одном** `with`:

```python
with open('input.txt', 'r', encoding='utf-8') as src, \
     open('output.txt', 'w', encoding='utf-8') as dst:
    for line in src:
        dst.write(line.upper())
```

Особенности:

- оба файла будут закрыты **корректно**, даже если внутри возникнет исключение;
- второй `open` не выполнится, если первый уже упал.

---

### 6.1a. Как `with` работает «под капотом» (упрощённо)

Конструкция:

```python
with open('x.txt', 'w', encoding='utf-8') as f:
    f.write("hi")
```

По смыслу похожа на:

```python
f = open('x.txt', 'w', encoding='utf-8')
try:
    f.write("hi")
finally:
    f.close()
```

То есть `finally` гарантирует закрытие файла **в любом случае**:

- даже если `write` упал с исключением,
- даже если вы сделали `return`,
- даже если вы сделали `break` из цикла.

### 6.2. `contextlib.suppress` и `nullcontext`

**`suppress`** — контекстный менеджер, который **игнорирует указанные исключения**:

```python
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove('temp.txt')  # если файла нет — просто ничего не произойдёт
```

Это лучше, чем голый `try/except FileNotFoundError: pass`, потому что:

- явно показывает **намерение** «тихо игнорировать отсутствие файла»;
- локализует обработку в аккуратный блок.

Но помните правило безопасности:

- `suppress` хорош только для **ожидаемых** исключений, которые действительно можно игнорировать;
- если вы сомневаетесь — лучше залогировать ситуацию или обработать явно.

Например, игнорировать `FileNotFoundError` при удалении временного файла — ок.  
Игнорировать `PermissionError` — обычно **не** ок, потому что это уже «реальная проблема».

**`nullcontext`** — «пустой» контекстный менеджер:

```python
from contextlib import nullcontext

debug = True

cm = open('log.txt', 'w') if debug else nullcontext()
with cm as f:
    if debug:
        f.write("Debug info\n")
```

Полезно, когда:

- иногда ресурс нужен, иногда нет;
- вы хотите, чтобы остальной код **не знал** об этой разнице.

---

### 6.3. `contextlib.ExitStack` — динамический набор контекстов

Когда количество ресурсов заранее **неизвестно**:

```python
from contextlib import ExitStack

filenames = ['a.txt', 'b.txt', 'c.txt']

with ExitStack() as stack:
    files = [stack.enter_context(open(name, 'r', encoding='utf-8'))
             for name in filenames]
    # здесь все файлы открыты
    for f in files:
        print(f.readline())
# при выходе из блока все файлы закрываются
```

`ExitStack`:

- позволяет добавлять контексты **в цикле**;
- гарантирует, что все они будут закрыты в обратном порядке.

---

### 6.3a. Ещё одна фишка `ExitStack`: `callback` (когда нет контекстного менеджера)

Иногда у вас есть ресурс, который нужно «убрать», но у него нет `with`.
Тогда можно вручную зарегистрировать функцию очистки:

```python
from contextlib import ExitStack

def acquire():
    print("acquire")
    return {"resource": "R"}

def release(res):
    print("release", res)

with ExitStack() as stack:
    res = acquire()
    stack.callback(release, res)  # release(res) вызовется при выходе
    print("work with", res)
```

Это помогает писать безопасный код даже с «неудобными» API.

### 6.4. Запомните по §114

- Несколько ресурсов в одном `with` делают код компактнее и безопаснее.
- `contextlib.suppress` — аккуратный способ «заглушить» ожидаемое исключение.
- `nullcontext` и `ExitStack` нужны, когда структура ресурсов становится динамической и зависит от условий.

---

