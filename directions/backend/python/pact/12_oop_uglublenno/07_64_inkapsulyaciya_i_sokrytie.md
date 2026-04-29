[← Назад к индексу части XII](index.md)


### Цель раздела

Понять, как в Python реализуется **инкапсуляция** на практике: какие соглашения приняты (`_attr`, `__attr`), что такое **name mangling** и когда использовать `property`.

### Базовые термины

- **Инкапсуляция** — скрытие деталей реализации за публичным интерфейсом.
- **Публичный атрибут** — доступен и предназначен для использования снаружи.
- **Защищённый атрибут** (`_attr`) — соглашение: «не трогать снаружи без необходимости».
- **Приватный атрибут** (`__attr`) — активирует механизм **name mangling**.

Важно: в Python инкапсуляция — это **социальный контракт**, а не «железный забор», как в языках с `private/protected/public`. Язык даёт инструмент (name mangling, соглашения об именах), но не запрещает взломать инкапсуляцию — ответственность на программистах.

### Соглашения об именах

```python
class User:
    def __init__(self, name: str, password: str):
        self.name = name            # публичный атрибут
        self._password = password   # «защищённый» (protected по соглашению)
```

- `name` — часть публичного интерфейса.
- `_password` — сигнал: «этот атрибут внутренний, не используйте его напрямую из внешнего кода».

Дополнительные соглашения:

- модульно‑внутренние объекты помечают префиксом `_` в имени: `_internal_helper`, `_SomeInternalClass`;
- в модулях можно управлять публичным API через `__all__ = ["PublicClass", "public_function"]` — всё остальное считается внутренним.

### Name mangling: `__attr`

```python
class Account:
    def __init__(self, balance: float):
        self.__balance = balance

    def get_balance(self) -> float:
        return self.__balance
```

Атрибут `__balance` при компиляции превращается в `_Account__balance`:

```python
acc = Account(100.0)
print(acc.get_balance())        # 100.0

# print(acc.__balance)          # AttributeError
print(acc._Account__balance)    # 100.0 — но так делать не надо
```

Это **не настоящая приватность**, а:

- защита от случайных конфликтов имён при наследовании;
- лёгкий барьер от неосторожного внешнего доступа.

Пример конфликта имён:

```python
class Base:
    def __init__(self):
        self.__value = 10  # превращается в _Base__value


class Child(Base):
    def __init__(self):
        super().__init__()
        self.__value = 20  # превращается в _Child__value
```

В итоге у экземпляра `Child` **два разных атрибута**: `_Base__value` и `_Child__value`. Это позволяет базовому и дочернему классу использовать «свои» приватные поля, не затирая друг друга.

### Когда использовать `property`

`property` позволяет **контролировать доступ** к атрибуту:

```python
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Невозможная температура")
        self._celsius = value
```

Снаружи:

```python
t = Temperature(25)
print(t.celsius)   # 25
t.celsius = 30     # проходит проверку
```

Мы можем:

- сохранить **интерфейс атрибута** (`obj.attr`);
- добавить **валидацию**, ленивые вычисления, кеширование и т.д.

`property` часто используют для:

- **ленивых вычислений**:

  ```python
  class User:
      def __init__(self, id_: int):
          self.id = id_
          self._profile = None

      @property
      def profile(self) -> dict:
          if self._profile is None:
              self._profile = load_profile_from_db(self.id)
          return self._profile
  ```

- **инвариантов** (нельзя присвоить недопустимое значение);
- **миграции интерфейса**: сначала был публичный атрибут `obj.value`, потом понадобилась валидация — вы превращаете его в `@property`, не ломая существующий код.

### Практические рекомендации

- Публичный API: **минимально необходимый** набор атрибутов и методов.
- Внутренние детали: прячем под `_attr` или `__attr`.
- Если нужно контролировать доступ/валидацию — используйте `property`.

### Запомните

- В Python нет жёсткой приватности, есть **соглашения** и `name mangling`.
- Ответственность за соблюдение инкапсуляции лежит на **разработчиках**, а не на языке.
- Инкапсуляция нужна не ради «секретности», а ради **простого и стабильного публичного интерфейса**.

---

## 65. Метаклассы (углублённо)
