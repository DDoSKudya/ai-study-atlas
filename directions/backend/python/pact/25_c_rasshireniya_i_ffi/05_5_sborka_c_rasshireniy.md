[← Назад к индексу части XXV](index.md)

## 5. Сборка C‑расширений (§148)

### 5.0. Исторически и по‑современному

Исторический путь:

- писать `setup.py` с `distutils`/`setuptools`;
- запускать `python setup.py build_ext --inplace`.

Современный путь:

- использовать `setuptools` через `pyproject.toml`;
- собирать пакет `python -m build` или `pip install .`.

В этой части мы покажем **минимальные рабочие примеры**,  
не углубляясь в тонкости публикации на PyPI.

Чтобы не запутаться, держите в голове две основные картинки:

- **«Локальная разработка»** — вы хотите просто собрать расширение рядом с кодом и импортировать его:
  - достаточно `setup.py` + `build_ext --inplace`;
  - файл `.so`/`.pyd` появится в текущей директории.
- **«Пакет для установки»** — вы хотите, чтобы модуль можно было ставить через `pip`:
  - заводите `pyproject.toml` с описанием зависимостей сборки;
  - собираете `wheel`/`sdist` и устанавливаете их как обычный пакет.

### 5.1. Минимальный `setup.py` с C‑расширением

Допустим, у нас есть простой C‑файл:

```c
// file: hello.c

#include <Python.h>

static PyObject *hello(PyObject *self, PyObject *args) {
    const char *name = "world";
    if (!PyArg_ParseTuple(args, "|s", &name)) {
        return NULL;
    }

    char buffer[256];
    snprintf(buffer, sizeof(buffer), "Hello, %s!", name);

    return PyUnicode_FromString(buffer);
}

static PyMethodDef HelloMethods[] = {
    {"hello", hello, METH_VARARGS, "Сказать привет"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "hello_ext",
    "Простой C-модуль",
    -1,
    HelloMethods
};

PyMODINIT_FUNC PyInit_hello_ext(void) {
    return PyModule_Create(&hellomodule);
}
```

`setup.py`:

```python
from setuptools import setup, Extension

hello_ext = Extension(
    "hello_ext",
    sources=["hello.c"],
)

setup(
    name="hello-ext",
    version="0.1.0",
    ext_modules=[hello_ext],
)
```

Сборка «на месте»:

```bash
python setup.py build_ext --inplace
```

После этого в каталоге появится файл вроде `hello_ext.cpython-312-x86_64-linux-gnu.so`,  
который можно импортировать:

```python
import hello_ext

print(hello_ext.hello())          # Hello, world!
print(hello_ext.hello("Python"))  # Hello, Python!
```

Минус этого подхода:

- `setup.py` — исполняемый сценарий;
- современные инструменты рекомендуют описывать сборку в `pyproject.toml`.

### 5.1.1. Разбор `hello.c` и `setup.py` «по буквам»

Чтобы пример не казался «магией», разберём его ещё медленнее.

`hello.c`:

- `#include <Python.h>` — подключаем заголовок C‑API Python:
  - без него компилятор не узнает, что такое `PyObject`, `PyModuleDef` и т.д.
- `static PyObject *hello(PyObject *self, PyObject *args)`:
  - сигнатура функции, которую Python будет видеть как `hello_ext.hello`;
  - `self` — указатель на модуль или объект (здесь можно его игнорировать);
  - `args` — кортеж аргументов в терминах C‑API.
- `PyArg_ParseTuple(args, "|s", &name)`:
  - разбирает Python‑кортеж аргументов в C‑переменные;
  - формат `|s` значит: «необязательная строка (`const char *`)»;
  - если аргументы не подошли под формат — возвращаем `NULL` (Python увидит исключение).
- `snprintf(...)` + `PyUnicode_FromString(buffer)`:
  - готовим C‑строку `"Hello, %s!"`;
  - упаковываем её обратно в Python‑строку.
- `HelloMethods` и `hellomodule`:
  - описывают, какие функции есть в модуле и как он называется;
  - это стандартный шаблон для модулей C‑API.
- `PyMODINIT_FUNC PyInit_hello_ext(void)`:
  - точка входа: Python вызывает эту функцию при `import hello_ext`;
  - она должна вернуть новый модуль (`PyModule_Create`).

`setup.py`:

- `Extension("hello_ext", sources=["hello.c"])`:
  - говорит setuptools: «есть расширение с именем `hello_ext`, собираем его из файла `hello.c`»;
- `setup(..., ext_modules=[hello_ext])`:
  - регистрирует расширение в метаданных пакета;
  - при `build_ext` setuptools вызовет компилятор:
    - подставит пути до заголовков/библиотек Python;
    - соберёт `.so`/`.pyd`.

### 5.1.2. Типичные ошибки при сборке через `setup.py`

- **Нет установленного компилятора.**
  - На Linux нужно установить `build-essential` (Debian/Ubuntu) или аналог;
  - На Windows нужен MSVC (обычно через «Build Tools for Visual Studio»).

- **Не найден `Python.h`.**
  - Ошибка вида `Python.h: No such file or directory` значит, что не установлены dev‑заголовки Python;
  - на Linux это пакеты вроде `python3-dev`, `python3.12-dev` и т.п.

- **Несоответствие версий Python.**
  - Если вы собираете модуль под одну версию Python, а запускаете под другой, файл `.so` может не подойти;
  - лучше собирать расширение тем же интерпретатором, под которым вы его будете использовать (тем же `python` в виртуальном окружении).

### 5.2. `pyproject.toml` с `setuptools`

Минимальный пример (упрощённо):

`pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "hello-ext"
version = "0.1.0"
description = "Простой пример C-расширения"
requires-python = ">=3.10"

[tool.setuptools.ext_modules]
hello_ext = { sources = ["hello.c"] }
```

Далее:

```bash
pip install build
python -m build
```

Появятся `wheel` и `sdist`, которые можно:

- установить локально (`pip install dist/hello_ext-0.1.0-...whl`);
- выкладывать на внутренний индекс.

### 5.2.1. Когда имеет смысл переходить на `pyproject.toml`

Для учебных примеров маленького размера достаточно:

- `setup.py` + `build_ext --inplace`.

Когда проект растёт и вы:

- хотите публиковать пакет (даже во внутреннем репозитории);
- хотите, чтобы другой человек мог просто сделать `pip install .` без знания о деталях сборки;

— лучше описать сборку в `pyproject.toml`:

- это современный стандарт;
- многие инструменты (poetry, pip, build) ожидают его наличие;
- зависимости сборки (например, `setuptools`, `wheel`, `pybind11`, `Cython`) будут явно указаны в одном месте.

### 5.3. Cython: промежуточный путь

Иногда:

- вам не хочется писать C‑код вручную;
- но вы готовы:
  - немного «аннотировать» Python‑код типами;
  - компилировать его в C.

Здесь на сцену выходит **Cython**:

- вы пишете `.pyx`:
  - почти как Python;
  - с типами: `cdef int`, `cdef double[:]` и т.п.;
- Cython генерирует C‑файл;
- `setuptools` собирает его как расширение.

Минимальный пример:

`fast_sum.pyx`:

```cython
cpdef double fast_sum(double[:] values):
    cdef Py_ssize_t i, n = values.shape[0]
    cdef double s = 0
    for i in range(n):
        s += values[i]
    return s
```

`setup.py`:

```python
from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension("fast_sum", sources=["fast_sum.pyx"])

setup(
    name="fast-sum",
    ext_modules=cythonize([ext]),
)
```

Сборка:

```bash
python setup.py build_ext --inplace
```

После этого:

```python
import numpy as np
import fast_sum

arr = np.array([1.0, 2.0, 3.0])
print(fast_sum.fast_sum(arr))  # 6.0
```

Ключевая идея:

- Cython позволяет писать **почти Python**, но с производительностью C;
- подходит, когда:
  - нужно ускорить существующий Python‑код;
  - нет желания руками писать C/С++‑биндинги.

### 5.4. NumPy и `numpy.distutils` (историческая справка)

Раньше для расширений, тесно работающих с NumPy, часто использовали:

- `numpy.distutils` — надстройку над `distutils`, упрощающую подключение заголовков/библиотек NumPy.

Сейчас:

- `numpy.distutils` считается **устаревшим**;
- рекомендовано:
  - использовать обычный `setuptools`;
  - подключать заголовки через `numpy.get_include()`;
  - или использовать `pybind11`/Cython с поддержкой NumPy.

---

