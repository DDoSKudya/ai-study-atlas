[← Назад к индексу части 26](index.md)

## 142. Условные функции

### Цель раздела

Научиться **описывать ветвящуюся логику прямо в SQL**, используя `CASE`, `COALESCE`, `NULLIF`, а также диалектные `IF`/`IIF`, и правильно обрабатывать `NULL`.

### В этом разделе главное

- `CASE` — это **`if/else` внутри SQL**, который можно использовать где угодно: в `SELECT`, `WHERE`, `ORDER BY`.
- `COALESCE` и `NULLIF` помогают **управлять `NULL`**: подставлять значения по умолчанию или превращать «особые значения» в `NULL`.
- Условные функции тесно связаны с **трёхзначной логикой SQL** (`TRUE`, `FALSE`, `UNKNOWN`).

### Термины

- **Простой `CASE`** — сравнение одного выражения с несколькими значениями.
- **Поисковый `CASE`** — набор произвольных условий `WHEN condition`.
- **Значение по умолчанию** — то, что подставляется, если все условия не сработали или значение `NULL`.

### Теория и правила

- **Простой `CASE`**:

```sql
CASE status
  WHEN 'NEW' THEN 'Новый'
  WHEN 'PAID' THEN 'Оплачен'
  ELSE 'Другое'
END
```

- **Поисковый `CASE`**:

```sql
CASE
  WHEN amount < 1000 THEN 'small'
  WHEN amount < 10000 THEN 'medium'
  ELSE 'large'
END
```

- **`COALESCE`**:
  - `COALESCE(a, b, c)` возвращает **первое не‑`NULL` значение**.  
  - Часто используется для значений по умолчанию: `COALESCE(discount, 0)`.

- **`NULLIF`**:
  - `NULLIF(a, b)` возвращает `NULL`, если `a = b`, иначе `a`.  
  - Например, чтобы избежать деления на ноль:

    ```sql
    SELECT amount / NULLIF(count, 0)
    ```

- **Диалектные `IF`/`IIF`**:
  - В MySQL: `IF(condition, true_value, false_value)`.  
  - В SQL Server: `IIF(condition, true_value, false_value)`.  
  - По сути, это короткая форма поискового `CASE`.

- **`GREATEST/LEAST` как условные**:
  - В строке из плана: они повторно упомянуты здесь, так как часто используются **вместо громоздких `CASE`** для выбора максимума/минимума.

### Разбор условных конструкций по одной

#### Простой CASE — «одно значение против списка вариантов»

Структура:

```sql
CASE выражение
  WHEN значение1 THEN результат1
  WHEN значение2 THEN результат2
  ...
  ELSE результат_по_умолчанию
END
```

Пример:

```sql
CASE status
  WHEN 'NEW'   THEN 'Новый'
  WHEN 'PAID'  THEN 'Оплачен'
  WHEN 'CANCELED' THEN 'Отменён'
  ELSE 'Неизвестен'
END
```

**Когда использовать:** когда у тебя есть одно поле (например, `status`) и **фиксированный список вариантов**, которые нужно красиво переименовать или сгруппировать.

#### Поисковый CASE — «набор условий»

Структура:

```sql
CASE
  WHEN условие1 THEN результат1
  WHEN условие2 THEN результат2
  ...
  ELSE результат_по_умолчанию
END
```

Пример разбиения заказов по корзинам:

```sql
CASE
  WHEN amount < 1000 THEN 'small'
  WHEN amount < 5000 THEN 'medium'
  ELSE 'large'
END
```

**Особенность:** условия проверяются **по порядку**, как `if / else if / else`. Как только одно `WHEN` срабатывает, остальные **не проверяются**.

#### COALESCE — «первое непустое»

- **Что делает:** возвращает **первое аргумент, который не `NULL`**.

```sql
COALESCE(a, b, c, ...)
```

Примеры:

```sql
SELECT COALESCE(NULL, 10, 20);    -- 10
SELECT COALESCE(NULL, NULL, 30);  -- 30
```

Типичные применения:

- подставлять **значение по умолчанию**:

  ```sql
  COALESCE(discount_percent, 0)
  ```

- объединять несколько возможных источников данных:

  ```sql
  COALESCE(phone_mobile, phone_home, phone_work)
  ```

#### NULLIF — «сделать NULL, если равно»

- **Что делает:** возвращает `NULL`, если два значения равны, иначе возвращает первое.

```sql
NULLIF(a, b)
```

Примеры:

```sql
SELECT NULLIF(10, 0);   -- 10
SELECT NULLIF(0, 0);    -- NULL
```

Классический приём — **избежать деления на ноль**:

```sql
SELECT total / NULLIF(count, 0) AS avg_value
FROM stats;
```

Если `count = 0`, выражение превратится в `total / NULL`, что даёт `NULL` вместо ошибки деления на ноль.

#### IF / IIF — короткая форма для одного условия

- В MySQL:

  ```sql
  IF(condition, true_value, false_value)
  ```

- В SQL Server:

  ```sql
  IIF(condition, true_value, false_value)
  ```

Эквивалентно:

```sql
CASE WHEN condition THEN true_value ELSE false_value END
```

Пример:

```sql
SELECT
  user_id,
  IF(is_active = 1, 'active', 'inactive') AS status_label
FROM users;
```

### Примеры

**1. Сгруппировать заказы по «корзинам» суммы:**

```sql
SELECT
  order_id,
  amount,
  CASE
    WHEN amount < 1000 THEN 'small'
    WHEN amount < 5000 THEN 'medium'
    ELSE 'large'
  END AS bucket
FROM orders;
```

**2. Подставить 0 вместо отсутствующей скидки:**

```sql
SELECT
  order_id,
  COALESCE(discount_percent, 0) AS discount_percent_safe
FROM orders;
```

**3. Избежать деления на ноль с помощью `NULLIF`:**

```sql
SELECT
  product_id,
  total_revenue / NULLIF(units_sold, 0) AS avg_price
FROM stats;
```

**4. Пример `IF` в MySQL:**

```sql
SELECT
  user_id,
  IF(is_active = 1, 'active', 'inactive') AS status_label
FROM users;
```

### Простыми словами

Условные функции — это **маленький кусочек «if/else»**, который живёт прямо в SQL‑выражении. Вместо того чтобы сначала выбрать данные, а потом в коде на языке приложения разруливать все случаи, ты можешь сразу сказать БД: «если так — верни X, иначе — Y».

### Картинка в голове

Представь **развилку дороги**: входящий поток строк доходит до `CASE`, и в зависимости от условий каждая строка уходит по своей дорожке (значению). `COALESCE` — это как табличка «если поле пустое — подставь вот это значение».

### Как запомнить

**`CASE` — универсальный «if/else», `COALESCE` — «первое непустое», `NULLIF` — «сделать NULL, если совпало», `IF/IIF` — короткая запись для одного условия.**

### Типичные ошибки

- Забыть `ELSE` в `CASE` и не обрабатывать неожиданные значения (получаешь `NULL`).
- Использовать `COALESCE` без понимания, что он **останавливается на первом не‑`NULL`** — порядок аргументов важен.
- Путать простой и поисковый `CASE` и пытаться писать условия в первом виде.

### Проверь себя

1. Как переписать `IF(condition, a, b)` в виде `CASE`?  
2. Чем отличается `COALESCE(a, b, c)` от `CASE WHEN a IS NOT NULL THEN a WHEN b IS NOT NULL THEN b ELSE c END`?  
3. Как с помощью `NULLIF` избежать деления на ноль, но при этом явно увидеть строки, где деление невозможно?

<details>
<summary>Ответы</summary>

1. `CASE WHEN condition THEN a ELSE b END`.  
2. Ничем — это эквивалентная запись, `COALESCE` просто короче и читабельнее.  
3. Можно вычислить два поля: одно с делением через `NULLIF`, второе — флаг проблемной строки:  
   ```sql
   SELECT
     value / NULLIF(denom, 0) AS result,
     CASE WHEN denom = 0 THEN 1 ELSE 0 END AS is_division_by_zero
   FROM t;
   ```
</details>

### Запомните

Условные функции позволяют **держать бизнес‑логику ближе к данным**, там, где её проще проверить и оптимизировать. Чем лучше ты владеешь `CASE` и друзьями, тем реже тебе нужно будет переписывать одну и ту же логику в разных слоях приложения.

---

---

<!-- prev-next-nav -->
*[← 141. Функции даты и времени](03_141_funktsii_daty_i_vremeni.md) | [→ 143. Преобразование типов](05_143_preobrazovanie_tipov.md)*
