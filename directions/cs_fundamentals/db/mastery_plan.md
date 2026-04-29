# Глобальный план освоения баз данных

> Цель: знать всё о базах данных — как они работают, что умеют, как хранят данные и используют память (SQL, NoSQL, векторные, графовые, временные ряды и другие).

---

## Быстрая навигация по частям

### Базовое ядро (Шаги 0–15)

| Шаг | Часть | Ссылка |
|-----|-------|--------|
| 0 | Философия, границы и ментальные модели | [→ Навигация](pact/00_filosofiya_granitsy_mentalnye_modeli/index.md) |
| 1 | Теория и модели данных | [→ Навигация](pact/01_teoriya_i_modeli_dannyh/index.md) |
| 2 | SQL — основы | [→ Навигация](pact/02_sql_osnovy/index.md) |
| 3 | SQL — средний уровень | [→ Навигация](pact/03_sql_sredny_uroven/index.md) |
| 4 | Транзакции и согласованность | [→ Навигация](pact/04_tranzaktsii_i_soglasovannost/index.md) |
| 5 | Хранение и память | [→ Навигация](pact/05_hranenie_i_pamyat/index.md) |
| 6 | Индексы | [→ Навигация](pact/06_indeksy/index.md) |
| 7 | Оптимизация запросов | [→ Навигация](pact/07_optimizatsiya_zaprosov/index.md) |
| 8 | Реляционные СУБД | [→ Навигация](pact/08_relyatsionnye_subd/index.md) |
| 9 | SQL углублённо: типы, представления, процедуры | [→ Навигация](pact/13_sql_uglublenno_tipy_predstavleniya_protsedury/index.md) |
| 10 | Партиционирование и внутренности хранилища | [→ Навигация](pact/14_partitsionirovanie_i_vnutrennosti_hraneniya/index.md) |
| 11 | NoSQL и альтернативные модели | [→ Навигация](pact/09_nosql_i_alternativnye_modeli/index.md) |
| 12 | Векторные базы данных | [→ Навигация](pact/10_vektornye_bd/index.md) |
| 13 | Масштабирование и отказоустойчивость | [→ Навигация](pact/11_masshtabirovanie_i_otkazoustojchivost/index.md) |
| 14 | Аналитика и хранилища данных | [→ Навигация](pact/16_analitika_i_hranilishcha_dannyh/index.md) |
| 15 | Операционная часть и безопасность | [→ Навигация](pact/12_operatsii_i_bezopasnost/index.md) |

### Профессиональное углубление (Шаги 16–49)

| Шаг | Часть | Ссылка |
|-----|-------|--------|
| 16 | PostgreSQL: детали и расширения | [→ Навигация](pact/17_postgresql_detali_i_rasshireniya/index.md) |
| 17 | MySQL: детали и оптимизация | [→ Навигация](pact/18_mysql_detali_i_optimizatsiya/index.md) |
| 18 | Геопространственные данные | [→ Навигация](pact/19_geodannye/index.md) |
| 19–20 | Администрирование и тюнинг | [→ Навигация](pact/20_administrirovanie_i_tyuning/index.md) |
| 21 | Разработка и паттерны | [→ Навигация](pact/21_razrabotka_i_patterny/index.md) |
| 22 | Интеграции и инструменты | [→ Навигация](pact/22_integratsii_i_instrumenty/index.md) |
| 23 | Инфраструктура и облака | [→ Навигация](pact/23_infrastruktura_i_oblaka/index.md) |
| 24 | Тестирование и документация | [→ Навигация](pact/24_testirovanie_i_dokumentatsiya/index.md) |
| 25 | Disaster Recovery | [→ Навигация](pact/25_disaster_recovery/index.md) |
| 26 | SQL: функции и операторы | [→ Навигация](pact/26_sql_funktsii_i_operatory/index.md) |
| 27 | Troubleshooting и диагностика | [→ Навигация](pact/27_troubleshooting_i_diagnostika/index.md) |
| 28 | Расширенная безопасность | [→ Навигация](pact/28_rasshirennaya_bezopasnost/index.md) |
| 29 | Системные представления и метаданные | [→ Навигация](pact/29_sistemnye_predstavleniya_i_metadannye/index.md) |
| 30 | Расширенные темы NoSQL | [→ Навигация](pact/30_rasshirennye_nosql_temy/index.md) |
| 31 | Расширенные темы: векторные БД | [→ Навигация](pact/31_rasshirennye_vektornye_bd/index.md) |
| 32 | Расширенное партиционирование | [→ Навигация](pact/32_rasshirennoe_partitsionirovanie/index.md) |
| 33 | Расширенная репликация | [→ Навигация](pact/33_rasshirennaya_replikatsiya/index.md) |
| 34 | Расширенный шардинг | [→ Навигация](pact/34_rasshirennyj_sharding/index.md) |
| 35 | Расширенные индексы | [→ Навигация](pact/35_rasshirennye_indeksy/index.md) |
| 36 | Расширенная оптимизация | [→ Навигация](pact/36_rasshirennaya_optimizatsiya/index.md) |
| 37 | Расширенные транзакции | [→ Навигация](pact/37_rasshirennye_tranzaktsii/index.md) |
| 38 | Расширенные типы данных | [→ Навигация](pact/38_rasshirennye_tipy_dannyh/index.md) |
| 39 | Расширенный мониторинг | [→ Навигация](pact/39_rasshirennyj_monitoring/index.md) |
| 40 | Расширенные бэкапы | [→ Навигация](pact/40_rasshirennye_bekopy/index.md) |
| 41 | Oracle и SQL Server: расширенные темы | [→ Навигация](pact/41_oracle_i_sql_server/index.md) |
| 42 | Алгоритмы и структуры данных в СУБД | [→ Навигация](pact/42_algoritmy_i_struktury_dannyh_v_subd/index.md) |
| 43 | Теория транзакций и согласованность | [→ Навигация](pact/43_teoriya_tranzaktsij_i_soglasovannost/index.md) |
| 44 | LSM-деревья и записно-оптимизированное хранение | [→ Навигация](pact/44_lsm_derevya_i_zapisno_optimizirovannoe_hranenie/index.md) |
| 45 | Аппаратная настройка и архитектура | [→ Навигация](pact/45_apparatnaya_nastrojka_i_arhitektura/index.md) |
| 46 | Колоночные движки: внутренности | [→ Навигация](pact/46_kolonochnye_dvigateli_vnutrennosti/index.md) |
| 47 | Big Data и SQL над Data Lake | [→ Навигация](pact/47_big_data_i_sql_nad_data_lake/index.md) |
| 48 | Формальная теория баз данных | [→ Навигация](pact/48_formalnaya_teoriya_bd/index.md) |
| 49 | Исследовательские темы и современная литература | [→ Навигация](pact/49_issledovatelskie_temy/index.md) |

### Дополнительные современные модули

| Модуль | Часть | Ссылка |
|--------|-------|--------|
| 50 | Инциденты и постмортемы | [→ Навигация](pact/50_incidenty_i_postmortery/index.md) |
| 51 | База данных как код и DevOps-практики | [→ Навигация](pact/51_bd_kak_kod_i_devops/index.md) |
| 52 | Качество данных и governance | [→ Навигация](pact/52_kachestvo_dannyh_i_governance/index.md) |
| 53 | Современные архитектуры: федерация, mesh, multi-cloud, serverless | [→ Навигация](pact/53_sovremennye_arhitektury/index.md) |
| 54 | Расширенное кэширование и performance | [→ Навигация](pact/54_rasshirennoe_keshirovanie_i_performance/index.md) |
| 55 | Observability, APM и распределённая трассировка | [→ Навигация](pact/55_observability_apm_i_treysing/index.md) |
| 56 | Рефакторинг и работа с legacy-базами | [→ Навигация](pact/56_refaktoring_i_legacy_bd/index.md) |

---

## Как читать этот план (если кажется сложно)

**План большой. Чтобы не потеряться и всё уложить в голову — читай так.**

1. **Одна мысль — несколько раз.** В подробных учебных частях в папке `pact/` одна и та же идея обычно повторяется несколько раз: в теории, потом «Простыми словами», потом «Картинка в голове», в конце «Запомните» и «Проверь себя». Это относится не только к [Часть 0](pact/00_filosofiya_granitsy_mentalnye_modeli/index.md) … [Часть 5](pact/05_hranenie_i_pamyat/index.md), но и к поздним специализированным частям курса. Не учи наизусть с первого абзаца — дочитай до «Запомните», к тому моменту мысль обычно уже будет объяснена несколькими способами.

2. **Двигайся по шагам по порядку.** В этом файле — основной маршрут: Шаг 0 → Шаг 1 → … → Шаг 49. После него есть ещё специализированные части курса ([Часть 51](pact/51_bd_kak_kod_i_devops/index.md) … [Часть 56](pact/56_refaktoring_i_legacy_bd/index.md)), которые разумно читать уже после ядра. Лучше пройти один шаг и честно ответить на «Проверь себя» в соответствующей части, чем пробежать десять шагов поверхностно.

3. **Где «максимально подробно».** Подробные тексты с «Пошагово», «Простыми словами», «Картинка в голове», «Проверь себя» лежат во **всех полноценных учебных частях** в папке `pact/`, а не только в первых главах. Этот файл — карта: что в каком порядке изучать и как темы связаны. Открывай нужную часть по шагу (например, Шаг 5 → [→ Часть 5](pact/05_hranenie_i_pamyat/index.md), Шаг 27 → [→ Часть 28](pact/28_rasshirennaya_bezopasnost/index.md)).

4. **Не гонись за скоростью.** «Проверил — добавил — и так 100 раз» значит: после каждого блока проверяй себя (вопросы «Проверь себя»), возвращайся к непонятному, перечитывай «Простыми словами» и «Картинка в голове». Так даже сложное уляжется.

5. **Шпаргалка в начале.** Ниже есть блок **«Одной фразой по шагам»** — одна строка на каждый шаг. Если забыл, «что такое Шаг 4» — глянь туда. Это не замена изучению, а якорь для памяти.

**Итог:** план — это маршрут. Подробность, примеры, повторения и самопроверка — в частях `pact`. Используй «Как читать», «Одной фразой по шагам» и карту файлов ниже, чтобы не теряться и быстро находить нужную учебную часть.

---

## Одной фразой по шагам (шпаргалка)

| Шаг | Одной фразой |
|-----|----------------|
| **0** | Введение: что такое БД, классификация, ментальные модели (таблицы, документы, графы). |
| **1** | Теория: реляционная модель, нормализация, алгебра, другие модели и ER. |
| **2** | SQL основы: DDL, ограничения, DML, SELECT, агрегация. |
| **3** | SQL средний: JOIN, подзапросы, оконные, CTE, множества, NULL. |
| **4** | Транзакции: ACID, уровни изоляции, блокировки, MVCC, 2PC, длинные транзакции. |
| **5** | Хранение и память: страницы, буфер, WAL, формат строк, undo/visibility/FSM, память, I/O. |
| **6** | Индексы: назначение, B-tree, Hash/GiST/GIN/BRIN, частичные, создание, bitmap/index-only, мониторинг. |
| **7** | Оптимизация запросов: EXPLAIN, статистика, cost-based оптимизатор, параллелизм, антипаттерны. |
| **8** | Реляционные СУБД: PostgreSQL, MySQL, SQLite, Oracle/SQL Server, подключение, ORM, миграции. |
| **9** | SQL углублённо: типы, JSON, полнотекст, представления, триггеры, процедуры, последовательности. |
| **10** | Партиционирование, WAL/VACUUM, репликация PostgreSQL, бэкапы. |
| **11** | NoSQL: документы, ключ–значение, широкостолбцовые, графы, временные ряды, поиск, многомодельные. |
| **12** | Векторные БД: эмбеддинги, индексы векторов, продукты, RAG, масштабирование. |
| **13** | Масштабирование: репликация, шардирование, CAP, консенсус, распределённые транзакции, бэкапы, NewSQL. |
| **14** | Аналитика: OLAP, колоночное хранение, ClickHouse, хранилища данных, ETL, data lake. |
| **15** | Операционка и безопасность: мониторинг, миграции, аутентификация, шифрование, инъекции, аудит, тесты. |
| **16–49** | Детали PostgreSQL/MySQL, гео, тюнинг, паттерны, интеграции, облака, тесты, DR, справочники, диагностика, безопасность, метаданные, расширенные NoSQL/вектор/партиции/репликация/шарды/индексы/оптимизация/транзакции/типы/мониторинг/бэкапы/Oracle-SQL Server, алгоритмы, теория транзакций, LSM, железо, колонки, data lake, формальная теория, исследования, инциденты. |

*(Шаги 16–49 в таблице сжаты; в плане ниже каждый шаг расписан по темам.)*

---

## Актуальная карта файлов `pact`

Ниже — быстрый ответ на вопрос **«какой шаг каким файлом закрывается на практике»**. Это полезно, потому что курс уже вырос дальше первоначального набора частей, и по одним только номерам шагов ориентироваться неудобно.

### Базовое ядро: пройти последовательно

| Шаг | Смысл шага | Основной файл |
|-----|------------|---------------|
| 0 | Что вообще такое БД, где её границы, как о ней думать | [→ Часть 0](pact/00_filosofiya_granitsy_mentalnye_modeli/index.md) |
| 1 | Реляционная теория и модели данных | [→ Часть 1](pact/01_teoriya_i_modeli_dannyh/index.md) |
| 2 | SQL: базовые команды и чтение/запись данных | [→ Часть 2](pact/02_sql_osnovy/index.md) |
| 3 | SQL: JOIN, окна, CTE, NULL, множества | [→ Часть 3](pact/03_sql_sredny_uroven/index.md) |
| 4 | Транзакции, изоляция, блокировки, MVCC | [→ Часть 4](pact/04_tranzaktsii_i_soglasovannost/index.md) |
| 5 | Хранение, буферы, WAL, память, I/O | [→ Часть 5](pact/05_hranenie_i_pamyat/index.md) |
| 6 | Индексы и их поведение | [→ Часть 6](pact/06_indeksy/index.md) |
| 7 | Планы выполнения и оптимизация запросов | [→ Часть 7](pact/07_optimizatsiya_zaprosov/index.md) |
| 8 | Продукты реляционных СУБД и подключение из приложений | [→ Часть 8](pact/08_relyatsionnye_subd/index.md) |
| 9 | Типы, JSON, представления, триггеры, процедуры | [→ Часть 13](pact/13_sql_uglublenno_tipy_predstavleniya_protsedury/index.md) |
| 10 | Партиционирование, VACUUM, WAL, PITR, детали хранения | [→ Часть 14](pact/14_partitsionirovanie_i_vnutrennosti_hraneniya/index.md) |
| 11 | NoSQL и альтернативные модели | [→ Часть 9](pact/09_nosql_i_alternativnye_modeli/index.md) |
| 12 | Векторные БД и RAG‑база | [→ Часть 10](pact/10_vektornye_bd/index.md) |
| 13 | Масштабирование и отказоустойчивость | [→ Часть 11](pact/11_masshtabirovanie_i_otkazoustojchivost/index.md) |
| 14 | Аналитика и хранилища данных | [→ Часть 16](pact/16_analitika_i_hranilishcha_dannyh/index.md) |
| 15 | Операционная часть и безопасность | [→ Часть 12](pact/12_operatsii_i_bezopasnost/index.md) |

### Профессиональное углубление: после ядра

| Шаги | Фокус | Основные файлы |
|------|-------|----------------|
| 16–20 | PostgreSQL, MySQL, гео, тюнинг, администрирование | [→ Часть 17](pact/17_postgresql_detali_i_rasshireniya/index.md), [→ Часть 18](pact/18_mysql_detali_i_optimizatsiya/index.md), [→ Часть 19](pact/19_geodannye/index.md), [→ Часть 20](pact/20_administrirovanie_i_tyuning/index.md) |
| 21–25 | Паттерны разработки, интеграции, облака, тестирование, DR | [→ Часть 21](pact/21_razrabotka_i_patterny/index.md) … [→ Часть 25](pact/25_disaster_recovery/index.md) |
| 26–31 | SQL‑справочник, troubleshooting, безопасность, метаданные, advanced NoSQL/vector | [→ Часть 26](pact/26_sql_funktsii_i_operatory/index.md) … [→ Часть 31](pact/31_rasshirennye_vektornye_bd/index.md) |
| 32–40 | Репликация, шардинг, индексы, оптимизация, транзакции, типы, мониторинг, бэкапы, Oracle/SQL Server | [→ Часть 32](pact/32_rasshirennoe_partitsionirovanie/index.md) … [→ Часть 41](pact/41_oracle_i_sql_server/index.md) |
| 41–49 | Алгоритмы, теория транзакций, LSM, железо, колоночные движки, data lake, формальная теория, research, инциденты | [→ Часть 42](pact/42_algoritmy_i_struktury_dannyh_v_subd/index.md) … [→ Часть 50](pact/50_incidenty_i_postmortery/index.md) |

### Дополнительные современные модули после основного плана

Эти части **не были отражены в старой версии плана как отдельные шаги**, но фактически являются полноценными учебными модулями и логично идут после ядра:

| Модуль | Что закрывает | Файл |
|--------|---------------|------|
| 50+ | Database as Code, DevOps‑практики | [→ Часть 51](pact/51_bd_kak_kod_i_devops/index.md) |
| 51+ | Качество данных и governance | [→ Часть 52](pact/52_kachestvo_dannyh_i_governance/index.md) |
| 52+ | Federation, mesh, multi-cloud, serverless DB | [→ Часть 53](pact/53_sovremennye_arhitektury/index.md) |
| 53+ | Расширенное кэширование и performance‑паттерны | [→ Часть 54](pact/54_rasshirennoe_keshirovanie_i_performance/index.md) |
| 54+ | Observability, APM, distributed tracing | [→ Часть 55](pact/55_observability_apm_i_treysing/index.md) |
| 55+ | Refactoring и работа с legacy‑базами | [→ Часть 56](pact/56_refaktoring_i_legacy_bd/index.md) |

### Как не потеряться

- Если ты новичок, сначала честно пройди **Шаги 0–15**.
- Если ты разработчик приложений, после ядра особенно важны **Шаги 20–28** и части [Часть 51](pact/51_bd_kak_kod_i_devops/index.md), [Часть 54](pact/54_rasshirennoe_keshirovanie_i_performance/index.md), [Часть 55](pact/55_observability_apm_i_treysing/index.md), [Часть 56](pact/56_refaktoring_i_legacy_bd/index.md).
- Если тебе ближе data/analytics направление, после ядра особенно важны **Шаг 14**, затем [Часть 47](pact/47_big_data_i_sql_nad_data_lake/index.md), [Часть 52](pact/52_kachestvo_dannyh_i_governance/index.md), [Часть 53](pact/53_sovremennye_arhitektury/index.md).
- Если ты идёшь в сторону DBA / DB engineer, после ядра особенно важны **Шаги 16–20**, потом **26–40**, затем [Часть 55](pact/55_observability_apm_i_treysing/index.md) и [Часть 56](pact/56_refaktoring_i_legacy_bd/index.md).

### Уровни глубины: база -> advanced -> expert

- **База**: не просто диапазон файлов, а именно **Шаги 0-15 целиком**. Это ядро курса: [Часть 0](pact/00_filosofiya_granitsy_mentalnye_modeli/index.md) -> [Часть 12](pact/12_operatsii_i_bezopasnost/index.md), **плюс** [Часть 13](pact/13_sql_uglublenno_tipy_predstavleniya_protsedury/index.md), [Часть 14](pact/14_partitsionirovanie_i_vnutrennosti_hraneniya/index.md) и [Часть 16](pact/16_analitika_i_hranilishcha_dannyh/index.md) в тех шагах, где они стоят в маршруте.
- **Advanced**: [Часть 16](pact/16_analitika_i_hranilishcha_dannyh/index.md) -> [Часть 40](pact/40_rasshirennye_bekopy/index.md). Это профессиональное углубление после ядра, а не “обязательный хвост” для каждого.
- **Expert**: [Часть 41](pact/41_oracle_i_sql_server/index.md) -> [Часть 56](pact/56_refaktoring_i_legacy_bd/index.md). Это слой для архитекторов, platform/data/DB engineers и тех, кто регулярно живёт в проде.

Если поздняя часть кажется слишком тяжёлой, это не сигнал “курс сломан”. Обычно это значит, что ты подошёл к **следующему уровню глубины раньше времени** и стоит вернуться на предыдущий слой.

### Поперечные маршруты по зонам перекрытия

- **Security**: [Часть 12](pact/12_operatsii_i_bezopasnost/index.md) -> [Часть 28](pact/28_rasshirennaya_bezopasnost/index.md) -> [Часть 51](pact/51_bd_kak_kod_i_devops/index.md) -> [Часть 56](pact/56_refaktoring_i_legacy_bd/index.md).
- **Observability / monitoring**: [Часть 12](pact/12_operatsii_i_bezopasnost/index.md) -> [Часть 27](pact/27_troubleshooting_i_diagnostika/index.md) -> [Часть 39](pact/39_rasshirennyj_monitoring/index.md) -> [Часть 55](pact/55_observability_apm_i_treysing/index.md).
- **Replication / DR**: [Часть 11](pact/11_masshtabirovanie_i_otkazoustojchivost/index.md) -> [Часть 25](pact/25_disaster_recovery/index.md) -> [Часть 33](pact/33_rasshirennaya_replikatsiya/index.md) -> [Часть 40](pact/40_rasshirennye_bekopy/index.md).
- **Analytics / warehouses**: [Часть 16](pact/16_analitika_i_hranilishcha_dannyh/index.md) -> [Часть 47](pact/47_big_data_i_sql_nad_data_lake/index.md) -> [Часть 45](pact/45_apparatnaya_nastrojka_i_arhitektura/index.md) -> [Часть 52](pact/52_kachestvo_dannyh_i_governance/index.md).
- **Schema / metadata / documentation**: [Часть 24](pact/24_testirovanie_i_dokumentatsiya/index.md) -> [Часть 29](pact/29_sistemnye_predstavleniya_i_metadannye/index.md) -> [Часть 51](pact/51_bd_kak_kod_i_devops/index.md) -> [Часть 56](pact/56_refaktoring_i_legacy_bd/index.md).

---

## Последовательность изучения (от простого к сложному)

**Изучай по этой последовательности — от основ к специализациям.** Используй при создании md-файлов по темам.

> Важно: римские номера частей соответствуют исторической эволюции курса и именам файлов `pact`. Для маршрута чтения ориентируйся прежде всего на **шаги** и на деление **база / advanced / expert**. Внутренние номера подпунктов ниже выровнены настолько, насколько это помогает чтению, но не являются главным ориентиром маршрута.

### Шаг 0 — Введение *(параллельно с шагом 1)*
**Часть 0** — Философия, границы, ментальные модели
- 0.1 Что такое база данных: определение, СУБД, данные vs информация, персистентность, OLTP vs OLAP
- 0.2 Классификация БД: реляционные, NoSQL, векторные, графовые, временные ряды, поисковые, in-memory, встраиваемые, распределённые, колоночные, NewSQL
- 0.3 Ментальные модели: таблицы vs документы vs графы vs ключ–значение; полиглот персистентности; когда что выбирать

### Шаг 1 — Теория и модели данных
**Часть I (§1–4)**
- §1 Реляционная модель: отношения, атрибуты, домены, ключи (PK, FK, кандидаты, суперключ), целостность (сущности, ссылочная, по домену)
- §2 Нормализация: 1NF–5NF, BCNF, функциональные и многозначные зависимости, денормализация, когда нарушать
- §3 Реляционная алгебра: выборка, проекция, объединение, разность, пересечение, декартово произведение, соединения, переименование, деление
- §4 Другие модели: иерархическая, сетевая (CODASYL), документная, графовая, ключ–значение, широкостолбцовые, векторная; ER-модель, концептуальное vs логическое vs физическое проектирование

### Шаг 2 — SQL: основы
**Часть II (§5–9)**
- §5 DDL: CREATE TABLE, все типы данных (числа, строки, даты, JSON, массивы, диапазоны, UUID, ENUM), ALTER, DROP, TRUNCATE, временные таблицы
- §6 Ограничения: PRIMARY KEY, UNIQUE, NOT NULL, CHECK, FOREIGN KEY (каскады), DEFERRABLE, EXCLUDE
- §7 DML: INSERT, UPDATE, DELETE, MERGE/UPSERT, RETURNING; COPY, BULK; последовательности, IDENTITY
- §8 SELECT: список столбцов, WHERE, ORDER BY (NULLS FIRST/LAST), LIMIT/OFFSET, DISTINCT/DISTINCT ON, псевдонимы, выражения
- §9 Агрегация: GROUP BY, HAVING, COUNT/SUM/AVG/MIN/MAX, FILTER в агрегатах, GROUPING SETS/CUBE/ROLLUP, строковые агрегаты (string_agg)

### Шаг 3 — SQL: средний уровень
**Часть III (§10–15)**
- §10 JOIN: INNER, LEFT/RIGHT/FULL OUTER, CROSS, self-join, LATERAL, USING, составные ключи
- §11 Подзапросы: скалярные, в FROM, IN/EXISTS/ANY/ALL, коррелированные; замена на JOIN
- §12 Оконные функции: OVER, PARTITION BY, ORDER BY, рамка (ROWS/RANGE, UNBOUNDED), ROW_NUMBER/RANK/DENSE_RANK, LAG/LEAD, FIRST_VALUE/LAST_VALUE, NTH_VALUE, агрегаты как окно
- §13 CTE (WITH): обычные и рекурсивные, иерархии, MATERIALIZED/NOT MATERIALIZED
- §14 Множества: UNION/UNION ALL, INTERSECT, EXCEPT; пагинация (OFFSET vs keyset)
- §15 NULL и трёхзначная логика: IS NULL, COALESCE, NULLIF, IS DISTINCT FROM; NULL в сортировке и группировке

### Шаг 4 — Транзакции и согласованность
**Часть IV (§16–21)**
- §16 ACID: атомарность, согласованность, изоляция, долговечность; BEGIN/COMMIT/ROLLBACK, SAVEPOINT
- §17 Уровни изоляции: READ UNCOMMITTED/COMMITTED, REPEATABLE READ, SERIALIZABLE; аномалии (грязное, неповторяющееся, фантом)
- §18 Блокировки: строки, таблицы (SHARE/EXCLUSIVE), SELECT FOR UPDATE/SHARE, SKIP LOCKED, advisory locks, deadlock
- §19 MVCC: версии строк (xmin/xmax), видимость, snapshot isolation, SSI (serializable snapshot isolation)
- §20 Двухфазный коммит, XA; длинные транзакции и их влияние (bloat, репликация)
- §21 Оптимистичная и пессимистичная блокировка; lost update; идемпотентность

### Шаг 5 — Хранение и память
**Часть V (§22–28)**
- §22 Физическое хранение: страницы, блоки, файлы данных, табличные пространства, row-oriented vs columnar
- §23 Буферный пул: кэш страниц, LRU/clock-sweep, dirty pages, checkpoint, read-ahead
- §24 WAL/redo: запись до сброса страниц, сегменты, LSN, full page write, восстановление; doublewrite (InnoDB)
- §25 Формат строк: heap, заголовок строки, NULL bitmap, TOAST, HOT (Heap Only Tuple), fillfactor
- §26 Undo log (InnoDB); visibility map, FSM (free space map); сжатие страниц
- §27 Память: оценка размера таблицы/индекса, shared_buffers, work_mem, maintenance_work_mem; OOM
- §28 Дисковый I/O: последовательное vs случайное, random_page_cost, SSD, очереди I/O

### Шаг 6 — Индексы
**Часть VI (§29–35)**
- §29 Назначение индексов: ускорение поиска/сортировки/группировки; замедление DML; когда не индексировать
- §30 B-tree: структура, листья, диапазоны, составные ключи, порядок столбцов, INCLUDE (покрывающий)
- §31 Hash, GiST, GIN (posting list/tree, fast update), BRIN (min-max), пространственные (R-tree), полнотекст
- §32 Частичный индекс (WHERE), индекс по выражению; уникальный частичный
- §33 Создание/перестроение: CREATE INDEX CONCURRENTLY, REINDEX CONCURRENTLY; bloat, CLUSTER
- §34 Bitmap index scan, index-only scan (visibility map); корреляция физического и логического порядка
- §35 Мониторинг использования индексов; неиспользуемые и избыточные индексы

### Шаг 7 — Оптимизация запросов
**Часть VII (§36–41)**
- §36 EXPLAIN/EXPLAIN ANALYZE: узлы (Seq Scan, Index Scan, Bitmap, Nested Loop, Hash/Merge Join, Sort, Aggregate)
- §37 Статистика: ANALYZE, гистограммы, pg_stats, селективность, correlation; устаревшая статистика
- §38 Cost-based optimizer: стоимость (seq_page_cost, random_page_cost, cpu_tuple_cost), порядок JOIN
- §39 Параллельное выполнение: Gather, workers; JIT; подплан (subplan), initplan
- §40 Антипаттерны: N+1, отсутствие индексов, SELECT *, большие IN, несоответствие типов
- §41 Настройка: work_mem, effective_cache_size, parallel workers; pg_stat_statements, auto_explain

### Шаг 8 — Реляционные СУБД: продукты
**Часть VIII (§42–48)**
- §42 PostgreSQL: архитектура (процессы, shared memory), расширения, системные каталоги (pg_class, pg_attribute)
- §43 PostgreSQL: типы (JSONB, массивы, диапазоны, inet, uuid), партиционирование (range/list/hash), схемы
- §44 MySQL/MariaDB: InnoDB/MyISAM, binlog, репликация (GTID), настройки
- §45 SQLite: один файл, WAL, PRAGMA, ограничения, когда использовать
- §46 Oracle, SQL Server, CockroachDB, TiDB, YugabyteDB: обзор и отличия
- §47 Подключение: драйверы, пулы (PgBouncer: transaction/session), prepared statements, таймауты
- §48 ORM vs raw SQL; миграции (Alembic, Flyway); connection string, failover в драйвере

### Шаг 9 — SQL углублённо: типы, представления, процедуры
**Часть XIII (§66–72)**
- §66 Типы данных углублённо: точность (DECIMAL), коллации, кодировки; дата/время (таймзоны, INTERVAL, extract)
- §67 JSON/JSONB: операторы (@>, ?, ->, ->>, #>, path), индексы (GIN), jsonpath; XML
- §68 Полнотекст: tsvector, tsquery, словари, rank, headline; массивы и диапазоны (операторы, индексы)
- §69 Представления: обычные, материализованные (REFRESH CONCURRENTLY), WITH CHECK OPTION; правила vs триггеры
- §70 Триггеры: BEFORE/AFTER, FOR EACH ROW/STATEMENT, INSTEAD OF; триггерные функции
- §71 Хранимые процедуры и функции: PL/pgSQL, volatile/stable/immutable, SECURITY DEFINER; курсоры; динамический SQL
- §72 Последовательности: nextval, currval, setval; IDENTITY; разрывы в нумерации

### Шаг 10 — Партиционирование и внутренности хранилища
**Часть XIV–XV (§73–78)**
- §73 Партиционирование: range, list, hash; default partition; создание/присоединение/отсоединение партиций
- §74 Partition pruning (статический/динамический); partition-wise join; уникальность и FK при партиционировании
- §75 WAL: структура записей, LSN, архивирование, restore_command; PITR
- §76 VACUUM: обычный и FULL; autovacuum (naptime, threshold); freeze, transaction ID wraparound
- §77 Репликация PostgreSQL: streaming (sync/async), слоты, logical replication (публикация/подписка, конфликты)
- §78 Бэкап и восстановление: pg_basebackup, pg_dump/restore; recovery_target_time, standby

### Шаг 11 — NoSQL и альтернативные модели
**Часть IX (§49–56)**
- §49 NoSQL обзор: CAP, BASE, eventual consistency; когда выбирать NoSQL
- §50 Документные: MongoDB (документ, коллекция, embedded vs reference), агрегация ($match, $lookup, $group), индексы, replica set, sharding
- §51 Ключ–значение: Redis (строки, списки, множества, хеши, zset, streams), RDB/AOF, кластер, Sentinel, Lua, MULTI/EXEC
- §52 Широкостолбцовые: Cassandra (partition key, clustering, consistency levels), compaction, tombstones; ScyllaDB
- §53 Графовые: Neo4j (Cypher, узлы/рёбра), индексы, кратчайший путь; Neptune, JanusGraph
- §54 Временные ряды: InfluxDB, TimescaleDB (hypertable, chunks), retention, continuous aggregates; Prometheus/PromQL
- §55 Поисковые: Elasticsearch (mapping, analyzers, BM25, агрегации), OpenSearch; ILM, reindex
- §56 Многомодельные (ArangoDB), DynamoDB, HBase; выбор стека

### Шаг 12 — Векторные базы данных
**Часть X (§57–61)**
- §57 Эмбеддинги: вектор представления, косинус/L2/dot product; модели (OpenAI, sentence-transformers)
- §58 Индексы векторов: brute force, HNSW, IVF, LSH; квантизация (PQ, SQ); recall vs скорость
- §59 Продукты: pgvector, Pinecone, Weaviate, Chroma, Qdrant, Milvus, LanceDB, Vald; сравнение
- §60 RAG: чанкинг, гибридный поиск (вектор + полнотекст), фильтры, переранжирование
- §61 Масштабирование векторных БД: память, шардирование, обновление/удаление

### Шаг 13 — Масштабирование и отказоустойчивость
**Часть XI (§62–68)**
- §62 Репликация: физическая vs логическая, синхронная vs асинхронная; чтение из реплик, lag
- §63 Шардирование: ключ шардирования, горячие ключи; Citus, Vitess; cross-shard запросы
- §64 CAP, PACELC; консенсус (Raft, Paxos); split-brain, кворум
- §65 Лидерство и кворум: выбор primary, split-brain, координация кластера
- §66 Бэкап: полный, инкрементальный, WAL-архив; стратегии, RTO/RPO; реплика не заменяет бэкап
- §67 Продолжение по теме: distributed transactions / saga / outbox / CDC раскрываются глубже в [Часть 37](pact/37_rasshirennye_tranzaktsii/index.md) и [Часть 22](pact/22_integratsii_i_instrumenty/index.md)
- §68 Продолжение по теме: NewSQL, geo-distributed и event/log-подходы уходят в [Часть 25](pact/25_disaster_recovery/index.md), [Часть 41](pact/41_oracle_i_sql_server/index.md), [Часть 53](pact/53_sovremennye_arhitektury/index.md)

### Шаг 14 — Аналитика и хранилища данных
**Часть XVI (§69–72)**
- §69 OLAP vs OLTP; колоночное хранение, сжатие, векторное выполнение
- §70 ClickHouse: MergeTree, order by, partition by; материализованные представления; Snowflake, BigQuery, Redshift — обзор
- §71 Хранилище данных: звёздная схема, снежинка; факты и измерения; SCD (типы 1–3)
- §72 ETL/ELT; data lake (Delta, Iceberg); CDC для загрузки в хранилище

### Шаг 15 — Операционная часть и безопасность
**Часть XII (§73–80)**
- §73 Мониторинг: метрики (QPS, задержка, CPU, RAM, диск), pg_stat_*, pg_stat_activity, алерты, Grafana
- §74 Миграции: версионирование, zero-downtime ALTER, откат; блокировки при DDL
- §75 Безопасность: аутентификация (SCRAM, сертификаты, LDAP), авторизация (роли, GRANT), RLS (политики)
- §76 Шифрование: at rest (TDE), in transit (TLS); управление ключами
- §77 SQL-инъекции: типы (classic, blind, time-based); подготовленные выражения, экранирование
- §78 Аудит: pgaudit, логирование; маскирование; GDPR, PCI DSS, HIPAA
- §79 Продолжение по теме: тестирование, документация и database-as-code вынесены в [Часть 24](pact/24_testirovanie_i_dokumentatsiya/index.md) и [Часть 51](pact/51_bd_kak_kod_i_devops/index.md)
- §80 Продолжение по теме: advanced monitoring / observability / security углубляются в [Часть 28](pact/28_rasshirennaya_bezopasnost/index.md), [Часть 39](pact/39_rasshirennyj_monitoring/index.md), [Часть 55](pact/55_observability_apm_i_treysing/index.md)

### Шаг 16 — PostgreSQL: детали и расширения
**Часть XVII (§81–87)**
- §81 Расширения PostgreSQL: установка (CREATE EXTENSION), популярные (pg_stat_statements, pg_trgm, pgcrypto, pg_partman)
- §82 Системные каталоги: pg_class, pg_attribute, pg_index, pg_constraint, pg_depend; полезные представления (pg_tables, pg_indexes)
- §83 Конфигурация: postgresql.conf, pg_hba.conf; ALTER SYSTEM, pg_reload_conf(); параметры памяти, WAL, autovacuum
- §84 Расширенные типы: ltree (иерархии), hstore (ключ–значение), citext (case-insensitive), pg_trgm (триграммы)
- §85 Расширенные функции: generate_series, unnest, array_agg, jsonb_agg; агрегатные функции (custom aggregates)
- §86 Расширения для партиционирования: pg_partman (автоматическое управление партициями), pg_pathman
- §87 Расширения для репликации: pglogical, bucardo (multi-master); расширения для мониторинга (pg_stat_monitor)

### Шаг 17 — MySQL: детали и оптимизация
**Часть XVIII (§88–94)**
- §88 Движки хранения: InnoDB (транзакции, внешние ключи), MyISAM (табличные блокировки), Aria, ColumnStore
- §89 InnoDB: структура (tablespace, segment, extent, page); doublewrite buffer; undo tablespace; buffer pool
- §90 Binlog: формат (statement, row, mixed); GTID; репликация на основе binlog; binary log rotation
- §91 Настройки MySQL: my.cnf; innodb_buffer_pool_size, innodb_log_file_size, max_connections; query cache (deprecated)
- §92 Оптимизация MySQL: EXPLAIN FORMAT=JSON; индексы (covering, prefix); оптимизация JOIN; slow query log
- §93 Репликация MySQL: master-slave, master-master; GTID; group replication (multi-master); semi-sync replication
- §94 Инструменты: mysqldump, mysqlbinlog, pt-query-digest (Percona Toolkit), MySQL Workbench

### Шаг 18 — Геопространственные данные
**Часть XIX (§95–98)**
- §95 PostGIS: установка и типы (geometry, geography); координатные системы (SRID); преобразование координат
- §96 Пространственные типы: POINT, LINESTRING, POLYGON, MULTIPOINT; создание и вставка геометрий
- §97 Пространственные запросы: ST_Distance, ST_Within, ST_Intersects, ST_Contains; ST_Buffer, ST_Union
- §98 Пространственные индексы: GiST, SP-GiST; использование в запросах; оптимизация пространственных запросов

### Шаг 19 — Администрирование и тюнинг
**Часть XX (§99–105)**
- §99 Настройка ОС для БД: huge pages, vm.swappiness, I/O scheduler (deadline, noop); файловая система (XFS, ext4)
- §100 Профилирование: pg_stat_statements, pg_stat_monitor; slow query log; pt-query-digest; профилирование CPU (perf)
- §101 Бенчмаркинг: pgbench (TPC-B), sysbench; TPC-C, TPC-H; интерпретация результатов; нагрузочное тестирование
- §102 Мониторинг производительности: wait events (pg_stat_activity.wait_event_type); блокировки (pg_locks); temp files
- §103 Тюнинг памяти: shared_buffers, work_mem, maintenance_work_mem; effective_cache_size; OOM killer
- §104 Тюнинг I/O: random_page_cost для SSD; effective_io_concurrency; checkpoint настройки; read-ahead
- §105 Тюнинг параллелизма: max_parallel_workers, max_parallel_workers_per_gather; parallel tuple cost; JIT настройки

### Шаг 20 — Разработка и паттерны работы с БД
**Часть XXI (§106–112)**
- §106 Паттерны доступа к данным: Repository, Unit of Work, Active Record, Data Mapper; выбор паттерна
- §107 Паттерны работы с транзакциями: транзакционный скрипт, доменная модель; управление транзакциями в приложении
- §108 Паттерны масштабирования: read replicas, write-through cache, write-behind cache, CQRS, event sourcing
- §109 Антипаттерны разработки: N+1 запросы, избыточные запросы, игнорирование транзакций, отсутствие индексов
- §110 Best practices: подготовленные выражения, пулы соединений, таймауты, retry логика, circuit breaker
- §111 Версионирование данных: оптимистичная блокировка (version), пессимистичная (SELECT FOR UPDATE); soft delete
- §112 Идемпотентность: идемпотентные ключи; повторная обработка; idempotency key в API; обработка дублей

### Шаг 21 — Интеграции и инструменты
**Часть XXII (§113–119)**
- §113 CDC инструменты: Debezium (Kafka Connect), Maxwell, Bottled Water; логирование изменений для интеграций
- §114 ETL инструменты: Apache Airflow, dbt (data build tool), Pentaho, Talend; оркестрация ETL пайплайнов
- §115 Коннекторы: JDBC, ODBC, ADO.NET; специфичные (psycopg2, asyncpg); connection string параметры
- §116 Kafka и БД: Kafka как persistent log; Kafka Connect для интеграции БД; ksqlDB (SQL поверх Kafka)
- §117 Message queues и БД: RabbitMQ, Apache Pulsar; паттерн outbox для гарантии доставки; транзакционные outbox
- §118 GraphQL и БД: GraphQL resolvers с БД; N+1 проблема в GraphQL; DataLoader паттерн; Prisma, Hasura
- §119 REST API и БД: проектирование API для БД; пагинация, фильтрация, сортировка; rate limiting; API версионирование

### Шаг 22 — Инфраструктура и облака
**Часть XXIII (§120–126)**
- §120 Docker и БД: образы БД (postgres, mysql); docker-compose для разработки; volumes для персистентности
- §121 Kubernetes и БД: StatefulSets для БД; PersistentVolumes; операторы (PostgreSQL Operator, MySQL Operator)
- §122 Managed БД: AWS RDS (PostgreSQL, MySQL, Aurora), Azure Database, Google Cloud SQL; преимущества и ограничения
- §123 Облачные NoSQL: AWS DynamoDB, DocumentDB; Azure Cosmos DB; Google Firestore; сравнение с self-hosted
- §124 Облачные аналитические: AWS Redshift, Azure Synapse, Google BigQuery; serverless аналитика
- §125 Backup и restore в облаке: автоматические бэкапы; point-in-time recovery; cross-region репликация
- §126 Multi-cloud стратегии: репликация между облаками; disaster recovery; vendor lock-in; гибридные решения

### Шаг 23 — Тестирование и документация
**Часть XXIV (§127–132)**
- §127 Unit тесты БД: мокирование БД; тестирование репозиториев; изоляция тестов
- §128 Integration тесты: testcontainers (Docker); фикстуры данных; транзакционный rollback между тестами
- §129 Performance тесты: нагрузочное тестирование БД; профилирование медленных запросов; тестирование под нагрузкой
- §130 ER диаграммы: инструменты (dbdiagram.io, pgAdmin, MySQL Workbench, DBeaver); нотация (Crow's Foot, IDEF1X)
- §131 Документация схемы: комментарии к таблицам и столбцам (COMMENT ON); генерация документации; версионирование схемы
- §132 Миграции данных: перенос между БД (pg_dump → restore, mysqldump); конвертация схем; ETL для миграции

### Шаг 24 — Катастрофоустойчивость и DR
**Часть XXV (§133–138)**
- §133 Disaster Recovery планы: RTO (Recovery Time Objective), RPO (Recovery Point Objective); стратегии восстановления
- §134 Multi-region репликация: синхронная vs асинхронная между регионами; задержка; выбор primary региона
- §135 Failover стратегии: автоматический failover (Patroni, Stolon); ручной failover; тестирование failover
- §136 Backup стратегии: полный, инкрементальный, дифференциальный; хранение бэкапов (локально, S3, архив)
- §137 Тестирование восстановления: регулярное тестирование восстановления; проверка целостности после restore
- §138 Географическое распределение: CockroachDB multi-region; Spanner global; репликация между дата-центрами

### Шаг 25 — SQL функции и операторы: полный справочник
**Часть XXVI (§139–145)**
- §139 Строковые функции: CONCAT, SUBSTRING, TRIM, LOWER/UPPER, LENGTH, POSITION, REPLACE, SPLIT_PART, REGEXP_REPLACE
- §140 Числовые функции: ABS, ROUND, FLOOR/CEIL, MOD, POWER, SQRT, RANDOM, GREATEST/LEAST, SIGN
- §141 Функции даты и времени: NOW, CURRENT_DATE/TIME, EXTRACT, DATE_TRUNC, AGE, INTERVAL арифметика, AT TIME ZONE
- §142 Условные функции: CASE (простой и поисковый), COALESCE, NULLIF, GREATEST/LEAST, IF (MySQL)
- §143 Преобразование типов: CAST, :: (PostgreSQL), CONVERT (SQL Server), типы преобразований, безопасное преобразование
- §144 Системные функции: VERSION, CURRENT_USER, SESSION_USER, DATABASE(), SCHEMA(), pg_size_pretty, pg_database_size
- §145 Операторы SQL: арифметические (+, -, *, /, %), сравнения (=, <>, <, >, <=, >=), логические (AND, OR, NOT), строковые (||, LIKE, ILIKE, SIMILAR TO, ~)

### Шаг 26 — Troubleshooting и диагностика
**Часть XXVII (§146–152)**
- §146 Диагностика медленных запросов: идентификация проблемных запросов; анализ планов; профилирование
- §147 Диагностика блокировок: pg_locks анализ; deadlock detection; блокирующие запросы; kill блокирующих
- §148 Диагностика репликации: lag анализ; причины отставания; синхронная репликация — ожидание; слоты
- §149 Диагностика памяти: OOM причины; использование shared_buffers; temp files; memory leaks
- §150 Диагностика I/O: медленный диск; очередь I/O; wait events; оптимизация I/O
- §151 Диагностика bloat: раздувание таблиц и индексов; pg_stat_user_tables; VACUUM анализ; решение
- §152 Логи и диагностика: анализ логов (PostgreSQL, MySQL); error codes; stack traces; диагностические запросы

### Шаг 27 — Расширенные темы безопасности
**Часть XXVIII (§153–159)**
- §153 Типы SQL-инъекций: классическая, blind, time-based, second-order, union-based, error-based; примеры атак
- §154 Защита от инъекций: подготовленные выражения (все языки); параметризованные запросы; валидация; allowlist
- §155 Атаки на БД: SQL injection, NoSQL injection, command injection через функции; защита
- §156 Шифрование данных: column-level encryption; application-level encryption; TDE (Transparent Data Encryption)
- §157 Управление ключами: KMS (Key Management Service); ротация ключей; безопасное хранение ключей
- §158 Аудит и compliance: детальное логирование; pgaudit конфигурация; соответствие стандартам (GDPR, PCI DSS, HIPAA, SOX)
- §159 Маскирование данных: PII (Personally Identifiable Information); маскирование в тестовых окружениях; динамическое маскирование

### Шаг 28 — Системные представления и метаданные
**Часть XXIX (§160–166)**
- §160 information_schema: стандартные представления; таблицы, столбцы, ограничения, индексы; переносимость
- §161 pg_catalog (PostgreSQL): системные каталоги; pg_class, pg_attribute, pg_index, pg_constraint, pg_depend
- §162 INFORMATION_SCHEMA (MySQL): таблицы, столбцы, ключи, статистика; совместимость со стандартом
- §163 Метаданные схемы: получение списка таблиц, столбцов, индексов; типы данных; ограничения
- §164 Статистика использования: pg_stat_user_tables, pg_stat_user_indexes; анализ использования объектов
- §165 Размеры объектов: pg_size_pretty, pg_total_relation_size, pg_table_size, pg_indexes_size; мониторинг роста
- §166 Версионирование схемы: отслеживание изменений; сравнение схем; миграции как история

### Шаг 29 — Расширенные темы NoSQL
**Часть XXX (§167–173)**
- §167 MongoDB детали: aggregation pipeline ($match, $group, $project, $lookup, $unwind, $sort, $limit, $facet); change streams; transactions
- §168 Redis детали: все структуры данных (strings, lists, sets, hashes, sorted sets, streams, bitmaps, hyperloglog); Lua scripting; pub/sub; Redis Modules
- §169 Cassandra детали: CQL (CREATE TABLE, INSERT, SELECT, UPDATE, DELETE); materialized views; secondary indexes; lightweight transactions; batch
- §170 Elasticsearch детали: mapping (dynamic, explicit); analyzers (standard, keyword, custom); query DSL (bool, match, term, range, nested); aggregations (metric, bucket, pipeline)
- §171 Neo4j детали: Cypher (MATCH, WHERE, RETURN, CREATE, MERGE, DELETE, SET, REMOVE); переменная длина пути; shortest path; APOC процедуры
- §172 InfluxDB детали: Flux язык; retention policies; continuous queries; downsampling; tags vs fields; series
- §173 DynamoDB: таблицы, items, attributes; partition key и sort key; GSI и LSI; streams; TTL; on-demand vs provisioned

### Шаг 30 — Расширенные темы векторных БД
**Часть XXXI (§174–179)**
- §174 pgvector детали: типы vector(n); операторы (<->, <#>, <=>); индексы (ivfflat, hnsw); параметры индексов
- §175 Pinecone детали: managed векторная БД; API; namespaces; metadata filtering; hybrid search
- §176 Weaviate детали: схема (classes, properties); модули (text2vec, img2vec); GraphQL API; batch operations
- §177 Milvus детали: collections; partitions; segments; индексы (FLAT, IVF_FLAT, IVF_SQ8, HNSW); load и release
- §178 Qdrant детали: collections; points; payload (metadata); фильтры; sparse vectors; sharding
- §179 Оптимизация векторного поиска: выбор метрики; настройка индексов (ef_construction, m для HNSW); квантизация; фильтрация

### Шаг 31 — Расширенные темы партиционирования
**Часть XXXII (§180–185)**
- §180 Стратегии партиционирования: по времени (месяц, год, неделя); по диапазону значений; по списку; по хешу; composite
- §181 Управление партициями: автоматическое создание (pg_partman); удаление старых (retention); архивирование; split/merge
- §182 Partition pruning: статический (при планировании); динамический (при выполнении); prepared statements
- §183 Partition-wise операции: partition-wise join; partition-wise aggregate; параллелизм по партициям
- §184 Уникальность и FK: ограничения при партиционировании; локальные vs глобальные индексы; foreign keys
- §185 Мониторинг партиций: размер партиций; использование; статистика по партициям; неравномерное распределение

### Шаг 32 — Расширенные темы репликации
**Часть XXXIII (§186–192)**
- §186 Streaming replication (PostgreSQL): настройка; синхронная vs асинхронная; multiple standbys; quorum commit
- §187 Logical replication (PostgreSQL): публикация и подписка; фильтрация; конфликты и их разрешение; initial copy
- §188 Binlog репликация (MySQL): формат (statement, row, mixed); GTID; настройка; мониторинг lag
- §189 Group replication (MySQL): multi-master; консенсус; split-brain защита; автоматический failover
- §190 Репликация MongoDB: replica set; oplog; выбор primary; read preference; write concern
- §191 Репликация Redis: master-replica; Sentinel для HA; Cluster для шардирования; репликация слотов
- §192 Репликация Cassandra: replication factor; стратегии (SimpleStrategy, NetworkTopologyStrategy); consistency levels

### Шаг 33 — Расширенные темы шардирования
**Часть XXXIV (§193–199)**
- §193 Стратегии шардирования: range sharding; hash sharding; directory-based; consistent hashing
- §194 Citus детали: distributed tables; reference tables; colocation; rebalance; cross-shard queries
- §195 Vitess детали: keyspace; shard; vindex (hash, lookup, unicode_lookup); resharding; vreplication
- §196 Cross-shard операции: scatter-gather; агрегация; сортировка; JOIN между шардами; ограничения
- §197 Решардинг: изменение числа шардов; перенос данных; downtime; online resharding
- §198 Мониторинг шардирования: распределение данных; горячие ключи; неравномерность; rebalance triggers
- §199 Роутинг запросов: application-level routing; proxy routing (ProxySQL, PgBouncer); middleware routing

### Шаг 34 — Расширенные темы индексов
**Часть XXXV (§200–206)**
- §200 B-tree детали: структура узлов; page split; fill factor; bloat причины; перестроение
- §201 GIN детали: posting list и posting tree; fast update (pending list); vacuum merge; использование для массивов и JSONB
- §202 GiST детали: tree structure; penalty function; picksplit; consistent function; использование для диапазонов и геометрии
- §203 BRIN детали: block range; min-max summary; autosummarize; эффективность для упорядоченных данных
- §204 Составные индексы: порядок столбцов; left-prefix rule; covering indexes; INCLUDE columns
- §205 Частичные индексы: WHERE clause; использование для фильтрации; уникальные частичные индексы
- §206 Индексы по выражениям: функциональные индексы; immutable функции; использование LOWER, UPPER, выражения

### Шаг 35 — Расширенные темы оптимизации
**Часть XXXVI (§207–213)**
- §207 Чтение планов выполнения: cost, rows, actual time; узлы плана; поддеревья; initplan vs subplan
- §208 Статистика и селективность: гистограммы; MCV (most common values); correlation; влияние на планы
- §209 Параллельное выполнение: Gather узел; workers; parallel seq scan, hash join, aggregate; ограничения
- §210 JIT компиляция: когда используется; jit_above_cost; компиляция выражений и WHERE; влияние на производительность
- §211 Подсказки (hints): USE INDEX, FORCE INDEX (MySQL); ограничения в PostgreSQL; когда использовать
- §212 Оптимизация JOIN: порядок таблиц; nested loop vs hash join vs merge join; выбор оптимизатором
- §213 Оптимизация подзапросов: развертывание в JOIN; материализация; коррелированные подзапросы; EXISTS vs IN

### Шаг 36 — Расширенные темы транзакций
**Часть XXXVII (§214–220)**
- §214 Snapshot isolation: как работает; видимость версий; snapshot на начало транзакции
- §215 Serializable snapshot isolation (SSI): rw-conflict detection; serialization failure; retry логика
- §216 Двухфазный коммит: PREPARE TRANSACTION; COMMIT PREPARED; распределённые транзакции; координатор
- §217 XA транзакции: внешний координатор; начало, подготовка, коммит/откат; поддержка в СУБД
- §218 Saga паттерн: компенсирующие транзакции; choreography vs orchestration; идемпотентность
- §219 Outbox pattern: транзакционная гарантия публикации; таблица outbox; CDC для публикации
- §220 Длинные транзакции: влияние на bloat; влияние на репликацию; влияние на блокировки; решения

### Шаг 37 — Расширенные темы типов данных
**Часть XXXVIII (§221–227)**
- §221 Числовые типы: точность DECIMAL/NUMERIC; масштаб; округление; float vs decimal для денег
- §222 Строковые типы: VARCHAR vs TEXT; кодировка (UTF-8, Latin1); коллации; байтовая vs символьная длина
- §223 Дата и время: TIMESTAMP WITH TIME ZONE vs WITHOUT; таймзоны; DST (Daylight Saving Time); INTERVAL
- §224 JSON и JSONB: различия; операторы (@>, ?, ->, ->>, #>, #>>); индексы GIN; jsonpath
- §225 Массивы: создание; операторы (&&, @>, <@, []); индексы GIN; unnest для JOIN
- §226 Диапазоны: int4range, tstzrange; операторы (&&, @>, <@); индексы GiST; использование для периодов
- §227 UUID и ENUM: генерация UUID; использование как PK; ENUM типы; добавление значений; порядок

### Шаг 38 — Расширенные темы мониторинга
**Часть XXXIX (§228–234)**
- §228 Метрики производительности: QPS, TPS, latency (p50, p95, p99, p999); throughput; error rate
- §229 Метрики ресурсов: CPU usage; memory (shared_buffers, work_mem, temp); disk I/O; network
- §230 Метрики репликации: lag (bytes, time); replication slots; sync standby; failover time
- §231 Метрики блокировок: lock wait time; deadlocks; blocking queries; lock contention
- §232 Метрики кэша: buffer pool hit ratio; index hit ratio; query cache hit ratio (MySQL)
- §233 Метрики роста: размер БД, таблиц, индексов; скорость роста; прогнозирование; capacity planning
- §234 Алертинг: пороги для алертов; escalation policies; интеграция с PagerDuty, Opsgenie; runbooks

### Шаг 39 — Расширенные темы бэкапов
**Часть XL (§235–241)**
- §235 Стратегии бэкапов: полный, инкрементальный, дифференциальный; комбинации; retention policies
- §236 Физические бэкапы: pg_basebackup; file-level backup; snapshot на уровне ОС; быстрее восстановление
- §237 Логические бэкапы: pg_dump; mysqldump; переносимость; выборочный бэкап; восстановление части данных
- §238 WAL архивирование: непрерывное архивирование; archive_command; restore_command; основа PITR
- §239 Point-in-Time Recovery: восстановление до момента; recovery_target_time; recovery_target_lsn; тестирование
- §240 Бэкапы в облаке: автоматические бэкапы managed БД; cross-region backup; lifecycle policies; восстановление
- §241 Валидация бэкапов: проверка целостности; тестирование восстановления; автоматизация проверок

### Шаг 40 — Расширенные темы Oracle и SQL Server
**Часть XLI (§242–248)**
- §242 Oracle детали: RAC (Real Application Clusters); ASM (Automatic Storage Management); PL/SQL; материализованные представления
- §243 Oracle: партиционирование (range, list, hash, composite, interval, reference); индексы (B-tree, bitmap, function-based)
- §244 SQL Server детали: Always On Availability Groups; Columnstore indexes; In-Memory OLTP; T-SQL специфика
- §245 SQL Server: партиционирование; индексы (clustered, non-clustered, filtered); statistics; query hints
- §246 Сравнение СУБД: PostgreSQL vs MySQL vs Oracle vs SQL Server; лицензии; экосистема; когда что выбирать
- §247 Миграция между СУБД: различия в типах данных; различия в SQL; инструменты миграции; тестирование
- §248 Управляемые версии: AWS RDS для Oracle/SQL Server; Azure SQL; ограничения; преимущества

### Шаг 41 — Алгоритмы и структуры данных внутри СУБД
**Часть XLII (§249–255)**
- §249 Алгоритмы JOIN: nested loop (простой, с индексом, блокированный), hash join (build/probe фазы, spilling на диск), merge join, adaptive join
- §250 Алгоритмы сортировки: external sort (multi-way merge), in-memory sort; spilling на диск при нехватке work_mem
- §251 Алгоритмы агрегации: hash aggregate (build hash table, probe), sort+aggregate (сортировка затем группировка), spilling
- §252 LSM-деревья: memtable (in-memory), SSTable (on-disk), уровни L0-Ln; compaction стратегии (STCS, LCS, TWCS); write amplification
- §253 Альтернативные индексные структуры: fractal tree, Bε-tree, learned indexes (Kraska et al.); bitmap индексы (Oracle, DWH)
- §254 Inverted index: структура для полнотекстового поиска; posting list; термы и документы; использование в Elasticsearch
- §255 Буферный менеджер: алгоритмы замены (LRU, LRU-K, 2Q, ARC, clock-sweep); eviction policy; prefetch (sequential, random)

### Шаг 42 — Теория транзакций и согласованности углублённо
**Часть XLIII (§256–262)**
- §256 Формальные модели изоляции: serializability (conflict serializability, view serializability); snapshot isolation формально; read committed и др.
- §257 Модели согласованности распределённых БД: linearizability, sequential consistency, causal consistency, PRAM, eventual, strong eventual consistency
- §258 Two-phase locking (2PL): basic 2PL, strict 2PL; wound-wait, wait-die протоколы; deadlock prevention
- §259 Timestamp ordering: basic TO, multiversion TO (MVTO); конфликты и откаты; сравнение с 2PL
- §260 CAP теорема формально: доказательство интуитивно; примеры систем (CP, AP, CA компромиссы); PACELC расширение
- §261 Реализация изоляции: как СУБД обеспечивают уровни; PostgreSQL (snapshot isolation), MySQL (gap locks), Oracle (MVCC)
- §262 Слабая согласованность: eventual consistency модели; CRDT (Conflict-free Replicated Data Types); векторные часы; logical clocks

### Шаг 43 — LSM-деревья и write-optimized storage
**Часть XLIV (§263–269)**
- §263 LSM структура: уровни L0 (memtable flush), L1-Ln (SSTable уровни); размер уровней; соотношение размеров
- §264 Compaction стратегии: Size-Tiered (STCS), Leveled (LCS), Time-Window (TWCS); выбор стратегии; компромиссы
- §265 Tombstones: маркеры удаления; необходимость для LSM; cleanup при compaction; влияние на read amplification
- §266 Write и read amplification: write amplification (множественные записи при compaction); read amplification (чтение нескольких уровней)
- §267 RocksDB: Facebook LSM; варианты compaction; настройки; использование в MySQL (MyRocks), TiKV
- §268 LevelDB, WiredTiger, Cassandra/HBase: различия в реализации LSM; compaction; производительность
- §269 Event sourcing и commit log: append-only лог как основа; event store; Kafka log; использование в СУБД

### Шаг 44 — Железо-ориентированный тюнинг и архитектура
**Часть XLV (§270–276)**
- §270 Cache-friendly алгоритмы: cache line alignment; row-oriented vs column-oriented layout; cache-oblivious структуры
- §271 NUMA: Non-Uniform Memory Access; pinning процессов к NUMA узлам; распределение буферных пулов; numa_maps анализ
- §272 Contention и spinlocks: contention по shared структурам; spinlocks vs mutex; latches в СУБД; измерение contention
- §273 NVMe/SSD vs HDD: различия в характеристиках; random vs sequential I/O; write barriers, FUA (Force Unit Access), fsync семантика
- §274 RDMA: Remote Direct Memory Access; использование в распределённых БД; низкая задержка; примеры систем
- §275 In-Memory DBMS: VoltDB (in-memory, snapshot на диск); MemSQL (hybrid); Hekaton (SQL Server In-Memory OLTP); архитектуры
- §276 Оптимизация под железо: CPU cache optimization; memory bandwidth; I/O patterns; профилирование на уровне железа

### Шаг 45 — Колончатые движки: внутренняя кухня
**Часть XLVI (§277–283)**
- §277 Кодировки и сжатие: RLE (Run-Length Encoding), dictionary encoding, delta encoding, bit-packing, frame-of-reference; выбор кодировки
- §278 Vectorized execution: batch processing (обработка векторов значений); SIMD инструкции; late materialization (отложенная материализация)
- §279 Storage layout: сегменты (segments), stripe'ы; zone maps (min/max значения); min/max pruning для отсечения данных
- §280 ClickHouse внутренности: MergeTree структура; primary key и order by; партиции; материализованные представления; сжатие
- §281 Snowflake внутренности: micro-partitions; clustering keys; automatic clustering; storage и compute разделение
- §282 Columnar индексы: columnstore indexes в SQL Server; использование для аналитики; compression; batch mode
- §283 Оптимизация колончатых БД: выбор кодировок; настройка сжатия; vectorized execution; параллелизм

### Шаг 46 — Большие данные и SQL поверх data lake
**Часть XLVII (§284–290)**
- §284 Presto/Trino: распределённый SQL движок; connector архитектура; execution model; оптимизация запросов
- §285 Spark SQL: SQL поверх Spark; Catalyst optimizer; DataFrame API; интеграция с data lake
- §286 Hive: SQL поверх Hadoop; MapReduce execution; Tez engine; LLAP (Live Long and Process); metastore
- §287 Impala: MPP SQL движок; in-memory execution; интеграция с HDFS; производительность
- §288 Parquet формат: columnar формат; структура файла (row groups, column chunks, pages); сжатие; статистика (min/max)
- §289 ORC и Avro: ORC (Optimized Row Columnar) — структура, индексы; Avro — row-based, schema evolution
- §290 Lakehouse детали: Delta Lake (ACID, time travel, schema evolution); Iceberg (hidden partitioning, schema evolution); Hudi (incremental processing)

### Шаг 47 — Формальная теория баз данных
**Часть XLVIII (§291–297)**
- §291 Реляционное исчисление: tuple calculus, domain calculus; связь с реляционной алгеброй; выразительная мощность; связь с SQL
- §292 Volcano/Cascades framework: архитектура оптимизатора запросов; search space; cost model; transformation rules
- §293 Heuristic vs cost-based оптимизация: rule-based оптимизация; cost-based оптимизация; гибридные подходы; ограничения
- §294 Теория типов в SQL: NULL как bottom type; three-valued logic формально; partial functions; constraints как логические формулы
- §295 Query optimization как поиск: search space планов; dynamic programming; greedy алгоритмы; ограничения перебора
- §296 Cardinality estimation: статистика для оценки; гистограммы; sampling; ошибки оценки и влияние на планы
- §297 Теоретические основы: реляционная модель формально; ACID формально; транзакции как истории; serializability формально

### Шаг 48 — Исследовательские темы и современная литература
**Часть XLIX (§298–304)**
- §298 NewSQL/HTAP архитектуры: TiDB (HTAP), Spanner (TrueTime), CockroachDB (глобальное распределение); исследования и реализации
- §299 Learned indexes: Kraska et al. "The Case for Learned Index Structures"; ML модели вместо B-tree; компромиссы
- §300 Learned cardinality estimation: ML для оценки кардинальности; улучшение планов; исследования
- §301 CRDT: Conflict-free Replicated Data Types; математические основы; использование в распределённых системах; примеры
- §302 Классические papers: System R (1970s), Spanner (Google), F1 (Google), Calvin (Yale), FaRM (Microsoft); чтение и понимание
- §303 Классические книги: "Readings in Database Systems" (Red Book), "Designing Data-Intensive Applications" (Kleppmann); изучение
- §304 Современные исследования: SIGMOD, VLDB, ICDE конференции; темы исследований; как следить за исследованиями

### Шаг 49 — Инциденты и пост-мортемы
**Часть L (§305–310)**
- §305 Real-world инциденты: разбор публичных postmortem'ов; отказ репликации; потеря данных; lock storm; примеры
- §306 Шаблон post-mortem: timeline событий; root cause analysis; remediation (что сделано); action items (что будет сделано)
- §307 Типичные инциденты: репликация lag; OOM; deadlock storms; corruption данных; network partitions
- §308 Анализ инцидентов: сбор данных (логи, метрики); анализ причин; предотвращение повторения; документация
- §309 Runbooks: процедуры обработки инцидентов; автоматизация; обучение команды; регулярное обновление
- §310 Культура надежности: blameless postmortems; learning from failures; continuous improvement; SRE принципы

---

**Справочники:** типы данных по СУБД, функции агрегации и оконные по диалектам, параметры настройки (PostgreSQL/MySQL).

**Навигация:** [Краткий обзор структуры](#краткий-обзор-структуры-плана-для-навигации) — в конце документа.

---

## Часть 0. Философия, границы и ментальные модели

> Концептуальная основа: *что* такое база данных и *когда* какую модель выбирать. Изучать можно параллельно с Частью I.

### 0.1 Что такое база данных

- [ ] **Определение**: упорядоченное хранилище данных с возможностью добавления, изменения, удаления и поиска
- [ ] **СУБД** (система управления БД): программное обеспечение, обеспечивающее хранение, целостность, безопасность, параллельный доступ
- [ ] **Данные vs информация**: данные — факты; информация — интерпретированные данные; БД хранит данные, приложение порождает информацию
- [ ] **Персистентность**: данные переживают перезапуск процесса; отличие от кэша (кэш может быть потерей)
- [ ] **Критичность**: надёжность, бэкапы, восстановление — часть концепции БД
- [ ] **OLTP vs OLAP**: транзакционная нагрузка (много коротких запросов) vs аналитическая (сложные агрегации, сканы); разные требования к хранению и индексам
- [ ] **Консистентность vs доступность**: строгая консистентность (всегда актуальные данные) vs eventual consistency (в итоге сойдётся)
- [ ] **Масштабирование**: вертикальное (больше ресурсов узла) vs горизонтальное (больше узлов); шардирование, репликация

#### Простыми словами

**База данных** — это место, где данные лежат постоянно и упорядоченно: их можно добавлять, менять, удалять и искать. **СУБД** — программа, которая это место организует (без неё «база» сама по себе не умеет гарантировать целостность и доступ). Важно: данные **переживают** перезапуск (персистентность); для аналитики (OLAP) и для операционных транзакций (OLTP) требования к БД разные.

#### Картинка в голове

БД — **архив с ящиками**: в ящиках лежат данные (факты). СУБД — **архивариус**: знает, куда что положить, как найти, как не дать испортить и как обслуживать несколько читателей сразу. Кэш — временная полка «под рукой»: выключили свет — полка пустая, а архив (БД) остался. OLTP — много людей быстро берут/кладут по одной бумажке; OLAP — один человек перелопачивает целые ящики и считает итоги.

#### Проверь себя (0.1)

Чем база данных отличается от кэша в памяти приложения с точки зрения персистентности?  
<details><summary>Ответ</summary> **База данных** рассчитана на **персистентность**: данные должны пережить перезапуск процесса, сбой питания, перезагрузку сервера. После восстановления СУБД данные с диска (или реплики) снова доступны. **Кэш в памяти** приложения обычно **не персистентный**: при перезапуске процесса или падении сервера содержимое кэша может быть потеряно. Кэш ускоряет доступ к данным; БД гарантирует, что данные никуда не денутся (при правильной настройке бэкапов и восстановления).</details>

#### Запомните

- **БД** — упорядоченное хранилище с добавлением, изменением, удалением и поиском; **СУБД** — программа, которая им управляет.
- **Персистентность** — данные переживают перезапуск; кэш — часто нет.
- **OLTP** — много коротких транзакций; **OLAP** — тяжёлая аналитика; требования к хранению и индексам разные.

### 0.2 Классификация баз данных

- [ ] **Реляционные (SQL)**: таблицы, строки, столбцы; схема; ACID; SQL как язык запросов; PostgreSQL, MySQL, Oracle, SQL Server
- [ ] **NoSQL**: общий термин для нереляционных; документные, ключ–значение, широкостолбцовые, графовые
- [ ] **Векторные**: хранение векторов (эмбеддингов), поиск по сходству; для ML и RAG; pgvector, Pinecone, Weaviate
- [ ] **Графовые**: узлы и рёбра; связи первого класса; Neo4j, Neptune
- [ ] **Временные ряды**: оптимизация под метрики и события во времени; InfluxDB, TimescaleDB, QuestDB
- [ ] **Поисковые**: полнотекстовый поиск, ранжирование; Elasticsearch, OpenSearch; часто вместе с основной БД
- [ ] **In-memory**: данные в RAM; Redis, Memcached, KeyDB; персистентность опциональна
- [ ] **Встраиваемые**: библиотека в процессе приложения (SQLite, DuckDB); без отдельного сервера
- [ ] **Распределённые**: данные на нескольких узлах; репликация, шардирование; CockroachDB, Cassandra
- [ ] **Колоночные (columnar)**: хранение по столбцам; сжатие, аналитика; ClickHouse, Snowflake, Vertica
- [ ] **NewSQL**: распределённые SQL с ACID; CockroachDB, TiDB, YugabyteDB, Spanner
- [ ] **Многомодельные**: одна СУБД — несколько моделей (документы + граф и т.д.); ArangoDB, OrientDB
- [ ] **Очереди и логи**: Kafka как persisted log; не классическая БД, но персистентность и запросы (ksqlDB)

#### Простыми словами

**Классификация** — это «кто как хранит и что умеет». Реляционные — таблицы и SQL. NoSQL — документы, ключ–значение, графы, широкие столбцы. Векторные — для поиска «похожего» (эмбеддинги). Временные ряды — под метрики во времени. Поисковые — полнотекст и ранжирование. In-memory — всё в RAM, скорость важнее долговечности. Колоночные — по столбцам, для аналитики. Один тип БД не закрывает все задачи — выбирают под задачу.

#### Картинка в голове

**Реляционная** — таблица Excel с жёсткой схемой. **Документная** — папки с JSON-файлами. **Графовая** — соцсеть: узлы и связи между ними. **Ключ–значение** — ящик с полками: по ключу достал значение. **Векторная** — «похожие картинки/тексты» по вектору. **Временные ряды** — лента показаний счётчика по времени. **Колоночная** — не «строка за строкой», а «столбец за столбцом» — удобно считать суммы по одному полю.

#### Проверь себя (0.2)

Когда логичнее выбрать документную БД, а когда реляционную?  
<details><summary>Ответ</summary> **Документная** уместна, когда: структура записей **разная** или часто меняется; данные естественно укладываются в **документ** (профиль пользователя, конфиг, лог события); не нужны сложные связи между сущностями и жёсткие JOIN. **Реляционная** уместна, когда: много **связей** между сущностями (таблицы, внешние ключи); нужна **целостность**, транзакции, жёсткая схема; типичные запросы — агрегации, JOIN по нескольким таблицам. Часто «полиглот персистентности»: основная БД реляционная, кэш или поиск — Redis/Elasticsearch.</details>

#### Запомните

- **Реляционные** — таблицы, схема, SQL, ACID. **NoSQL** — документы, ключ–значение, графы, широкие столбцы; у каждого типа своя ниша.
- **Векторные** — для поиска по сходству (эмбеддинги). **Колоночные** — для аналитики (хранение по столбцам, сжатие).
- Один тип БД не решает все задачи — выбирают **под задачу** (полиглот персистентности).

### 0.3 Ментальные модели

- [ ] **Таблицы (реляционная модель)**: строки и столбцы, схема, связи через ключи; мысленная картина — Excel с жёсткой структурой и связями между листами
- [ ] **Документы**: самодостаточные записи (JSON и т.п.); мысленная картина — папка с файлами, у каждого файла своя структура
- [ ] **Графы**: узлы и рёбра; связи — объекты первого класса; мысленная картина — соцсеть, граф зависимостей
- [ ] **Ключ–значение**: по ключу достаётся значение; мысленная картина — ящик с полками или словарь
- [ ] **Полиглот персистентности**: в одной системе — несколько типов хранилищ под разные задачи (например, PostgreSQL + Redis + Elasticsearch)
- [ ] **Когда что выбирать**: реляционная — связи, целостность, транзакции; документная — гибкая структура, документ как единица; графовая — обход связей; ключ–значение — кэш, сессии; векторная — поиск по сходству

#### Простыми словами

**Ментальная модель** — как ты представляешь данные в голове. **Таблицы** — строки и столбцы, связи по ключам. **Документы** — «один объект — один документ», структура может отличаться. **Графы** — «кто с кем связан», связи так же важны, как узлы. **Ключ–значение** — «по ключу получил значение», без сложной структуры. В реальных проектах часто **полиглот**: основная БД + кэш + поисковик — у каждой своя модель.

#### Картинка в голове

**Таблицы** — блокнот с разлинованными листами: каждая строка — запись, связи — «см. лист 2, строку 5». **Документы** — стопка открыток: на каждой что-то своё (текст, фото, адрес), без единой сетки. **Граф** — карта знакомств: кружочки — люди, стрелки — «знает», «друг». **Ключ–значение** — адресная книжка: имя (ключ) → телефон (значение). **Полиглот** — в столе и блокнот (таблицы), и открытки (документы), и адресная книжка (кэш): каждая вещь для своей задачи.

#### Проверь себя (0.3)

Что значит «полиглот персистентности» и зачем он нужен?  
<details><summary>Ответ</summary> **Полиглот персистентности** — использование **нескольких типов хранилищ** в одной системе под разные задачи. Например: **PostgreSQL** — основные данные, связи, транзакции; **Redis** — кэш, сессии, очереди; **Elasticsearch** — полнотекстовый поиск и ранжирование. Зачем: каждая БД лучше решает свою задачу; одна реляционная СУБД не даст ни скорости кэша, ни возможностей поисковика. Компромисс — сложность: несколько систем нужно проектировать, разворачивать и поддерживать.</details>

#### Запомните

- **Ментальная модель** — как представлять данные: таблицы (строки/столбцы/связи), документы (самодостаточные записи), графы (узлы и рёбра), ключ–значение (ключ → значение).
- **Полиглот персистентности** — несколько хранилищ в одной системе (реляционная + кэш + поиск и т.д.); выбирают **под задачу**.

---

## Часть I. Теория и модели данных

### 1. Реляционная модель

#### 1.1 Основные понятия
- [ ] **Отношение (relation)**: таблица; множество кортежей одной структуры
- [ ] **Кортеж (tuple)**: строка таблицы
- [ ] **Атрибут**: столбец; имя и домен (тип)
- [ ] **Домен**: множество допустимых значений (тип данных)
- [ ] **Степень отношения**: число атрибутов
- [ ] **Кардинальность**: число кортежей (мощность)

#### 1.2 Ключи
- [ ] **Суперключ**: множество атрибутов, уникально идентифицирующее кортеж
- [ ] **Кандидат ключа**: минимальный суперключ (нет подмножества-суперключа)
- [ ] **Первичный ключ (PK)**: выбранный кандидат ключа; не NULL, уникальный
- [ ] **Внешний ключ (FK)**: атрибут(ы), ссылающиеся на PK другой таблицы; ссылочная целостность
- [ ] **Альтернативный ключ**: кандидат, не выбранный первичным
- [ ] **Составной ключ**: ключ из нескольких атрибутов

#### 1.3 Целостность
- [ ] **Целостность сущности**: первичный ключ не NULL, уникален
- [ ] **Ссылочная целостность**: значение FK либо NULL, либо существует в целевой таблице
- [ ] **Целостность по домену**: значения в пределах домена (типы, CHECK)
- [ ] **Каскадное обновление/удаление**: при изменении PK или удалении строки — что делать с FK

### 2. Нормализация

#### 2.1 Нормальные формы
- [ ] **1NF**: атомарность значений; нет повторяющихся групп; каждый атрибут — одно значение
- [ ] **2NF**: 1NF + каждый неключевой атрибут полностью зависит от всего первичного ключа (нет частичной зависимости)
- [ ] **3NF**: 2NF + нет транзитивных зависимостей (неключевой атрибут не зависит от другого неключевого)
- [ ] **BCNF (Бойса–Кодда)**: каждый детерминант — кандидат ключа; устранение аномалий при нескольких кандидатах
- [ ] **4NF**: 3NF + нет многозначных зависимостей (MVD); разбиение на два отношения по MVD
- [ ] **5NF (PJ/NF)**: соединение без потерь; нет зависимостей соединения
- [ ] **Функциональные зависимости**: A → B; замыкание множества атрибутов; ключ как минимальное множество с полным замыканием
- [ ] **Многозначные зависимости**: A →→ B; независимые атрибуты при одном значении A
- [ ] **Детерминант**: атрибут(ы), от которых функционально зависит другой атрибут

#### 2.2 Денормализация
- [ ] Когда намеренно нарушать нормальные формы: производительность чтения, отчёты, дублирование для скорости
- [ ] Компромисс: дублирование vs аномалии обновления; контроль в приложении или триггеры
- [ ] Материализованные представления как управляемая денормализация
- [ ] Денормализация для отчётов: сводные таблицы, кэш агрегатов

### 3. Реляционная алгебра

- [ ] **Выборка (σ)**: подмножество строк по условию; аналог WHERE
- [ ] **Проекция (π)**: подмножество столбцов; аналог выбора столбцов в SELECT
- [ ] **Объединение (∪)**: множество строк из двух отношений (одинаковая схема)
- [ ] **Разность (−)**: строки из первого отношения, которых нет во втором
- [ ] **Пересечение (∩)**: строки, присутствующие в обоих отношениях
- [ ] **Декартово произведение (×)**: каждая строка первого с каждой строкой второго
- [ ] **Соединение (⋈)**: декартово произведение + условие (часто равенство ключей); эквивалент JOIN
- [ ] **Деление**: реляционное деление — обзорно
- [ ] Связь алгебры с SQL: каждый оператор алгебры выражается в SQL

### 4. Другие модели данных

- [ ] **Иерархическая**: дерево; родитель–потомок; ограниченная гибкость; IMS
- [ ] **Сетевая**: граф; обобщение иерархии; CODASYL; наборы (sets)
- [ ] **Документная**: документ (JSON/BSON) как единица; вложенность; гибкая схема; embedded vs reference
- [ ] **Графовая**: узлы (сущности), рёбра (связи), свойства; обход графа; property graph vs RDF
- [ ] **Ключ–значение**: ключ → значение; минимальная семантика; возможны структуры (список, хеш)
- [ ] **Широкостолбцовые**: ключ строки + семейства столбцов + временные метки; разреженная таблица; partition key + clustering
- [ ] **Векторная**: объект + вектор эмбеддинга; поиск по сходству (L2, косинус)
- [ ] **ER-модель**: сущности, атрибуты, связи (1:1, 1:N, N:M); преобразование в реляционную схему
- [ ] **Концептуальное vs логическое vs физическое проектирование**: от требований к схеме и к физическому хранению
- [ ] **Паттерны моделирования**: звёздная схема, снежинка (хранилище данных); агрегат (DDD)
- [ ] Сравнение: когда какая модель удобнее; гибридные решения

---

## Часть II. SQL — основы

### 5. DDL — определение данных

#### 5.1 CREATE TABLE
- [ ] Синтаксис: имя таблицы, список столбцов с типами
- [ ] Числовые: INT, BIGINT, SMALLINT; DECIMAL(p,s)/NUMERIC; FLOAT/REAL/DOUBLE; точность и масштаб
- [ ] Строковые: VARCHAR(n), TEXT, CHAR(n); кодировка, коллация (COLLATE)
- [ ] Типы дат и времени: DATE, TIME, TIMESTAMP, TIMESTAMPTZ, INTERVAL; таймзоны (AT TIME ZONE)
- [ ] Булевы: BOOLEAN (TRUE/FALSE/NULL)
- [ ] Бинарные: BLOB, BYTEA (PostgreSQL)
- [ ] Специальные: JSON, JSONB (PostgreSQL); массивы ARRAY[]; UUID; перечисления ENUM; диапазоны (int4range, tstzrange)
- [ ] DEFAULT (литерал, выражение, nextval(sequence)); GENERATED ALWAYS AS (STORED/VIRTUAL)
- [ ] IF NOT EXISTS; временные таблицы (TEMP/TEMPORARY); ON COMMIT DROP/PRESERVE ROWS
- [ ] CREATE TABLE AS (CTAS); CREATE TABLE ... LIKE; табличные пространства (TABLESPACE)
- [ ] Unlogged таблицы (PostgreSQL): быстрее запись, нет WAL; потеря при сбое

#### 5.2 ALTER и DROP
- [ ] ALTER TABLE ADD COLUMN (с DEFAULT: перезапись в старых PG vs быстрая в 11+); DROP COLUMN
- [ ] ALTER COLUMN: тип (часто перезапись), SET/DROP NOT NULL, SET DEFAULT
- [ ] ADD CONSTRAINT, DROP CONSTRAINT; переименование таблицы и столбцов (RENAME)
- [ ] DROP TABLE, CASCADE (зависимые объекты); TRUNCATE TABLE (CASCADE, RESTART IDENTITY)
- [ ] Блокировки при ALTER: уровень блокировки (ACCESS EXCLUSIVE и др.); ALTER без блокировки (CONCURRENTLY где поддерживается)

### 6. Ограничения (constraints)

- [ ] PRIMARY KEY: уникальность + NOT NULL; один на таблицу; кластерный индекс во многих СУБД; составной PK
- [ ] UNIQUE: уникальность; NULL в PostgreSQL — несколько NULL допустимы (в других СУБД по-разному)
- [ ] NOT NULL: запрет NULL; DEFAULT не отменяет NOT NULL при явной вставке NULL
- [ ] CHECK (условие): проверка на уровне строки; CHECK (col > 0); именованные vs анонимные
- [ ] FOREIGN KEY: ссылка на другую таблицу; ON DELETE / ON UPDATE (CASCADE, SET NULL, RESTRICT, NO ACTION, SET DEFAULT)
- [ ] FK и индекс: на целевой таблице — индекс по PK; на ссылающейся — индекс по FK для JOIN и каскадов
- [ ] DEFERRABLE INITIALLY DEFERRED / IMMEDIATE: проверка в конце транзакции (SET CONSTRAINTS)
- [ ] EXCLUDE (PostgreSQL): ограничение-исключение (GiST, btree_gist); например, непересекающиеся диапазоны
- [ ] NOT VALID (PostgreSQL): ограничение не проверяет существующие строки; VALIDATE CONSTRAINT — проверка позже

### 7. DML — изменение данных

- [ ] INSERT INTO table (col1, col2, ...) VALUES (v1, v2, ...); несколько строк через VALUES (...), (...)
- [ ] INSERT ... SELECT: вставка результата запроса
- [ ] INSERT ... ON CONFLICT (PostgreSQL UPSERT): DO UPDATE / DO NOTHING
- [ ] UPDATE table SET col = expr WHERE condition; несколько столбцов
- [ ] DELETE FROM table WHERE condition; без WHERE — осторожно (очистка)
- [ ] MERGE (SQL стандарт): вставка или обновление в зависимости от условия
- [ ] RETURNING (PostgreSQL): возврат вставленных/обновлённых/удалённых строк

### 8. SELECT — выборка

- [ ] SELECT col1, col2, * FROM table
- [ ] WHERE condition: сравнения, AND, OR, NOT, IN, BETWEEN, LIKE, IS NULL
- [ ] ORDER BY col [ASC|DESC], col2; NULLS FIRST / NULLS LAST
- [ ] LIMIT n OFFSET m (или FETCH FIRST n ROWS ONLY, OFFSET m ROWS)
- [ ] DISTINCT, DISTINCT ON (PostgreSQL)
- [ ] Псевдонимы столбцов (AS) и таблиц
- [ ] Выражения в SELECT: вычисления, вызовы функций, подзапросы-скаляры

### 9. Агрегация

- [ ] GROUP BY: группировка по одному или нескольким столбцам; GROUP BY с выражениями
- [ ] Агрегатные функции: COUNT(*), COUNT(col), SUM, AVG, MIN, MAX; COUNT(DISTINCT col)
- [ ] HAVING: фильтр по результатам агрегации (после GROUP BY); различие WHERE (до группировки) и HAVING (после)
- [ ] Фильтрация NULL в агрегатах: COUNT(col) не считает NULL; SUM/AVG игнорируют NULL
- [ ] FILTER (WHERE ...) в агрегатах: COUNT(*) FILTER (WHERE condition); условная агрегация без подзапроса
- [ ] GROUPING SETS: несколько группировок в одном запросе; CUBE, ROLLUP
- [ ] GROUPING(col): признак «свёрнутой» группы в CUBE/ROLLUP
- [ ] Строковые агрегаты: string_agg (PostgreSQL), GROUP_CONCAT (MySQL) — объединение значений в строку
- [ ] Упорядочение в агрегате: array_agg(... ORDER BY ...); порядок элементов в массиве
- [ ] Ordered-set агрегаты: mode(), percentile_cont(), percentile_disc()

---

## Часть III. SQL — средний уровень

### 10. JOIN

- [ ] INNER JOIN: только совпадающие строки; синтаксис ON condition
- [ ] LEFT [OUTER] JOIN: все строки слева + совпадения справа; NULL при отсутствии
- [ ] RIGHT JOIN, FULL [OUTER] JOIN
- [ ] CROSS JOIN: декартово произведение
- [ ] Self-join: таблица с самой собой (алиасы)
- [ ] Составные ключи в ON: несколько условий равенства
- [ ] JOIN по неравенству (диапазоны, анти-join) — осторожно с производительностью
- [ ] USING (col): если имена столбцов совпадают
- [ ] NATURAL JOIN: автоматическое совпадение по именам — обычно не рекомендуется

### 11. Подзапросы

- [ ] Скалярный подзапрос: один столбец, одна строка; в SELECT, WHERE, HAVING
- [ ] Подзапрос в FROM: FROM (SELECT ...) AS alias; обязательный алиас в большинстве СУБД
- [ ] IN (subquery): проверка вхождения в множество
- [ ] EXISTS (subquery): истина, если подзапрос возвращает хотя бы одну строку; часто с корреляцией
- [ ] ANY / SOME, ALL: сравнение с множеством
- [ ] Коррелированные подзапросы: ссылка на внешний запрос; влияние на производительность
- [ ] Замена подзапросов на JOIN где возможно

### 12. Оконные функции

- [ ] OVER(): окно по всей таблице (или партиции)
- [ ] PARTITION BY col: разбиение на группы без свёртки в одну строку
- [ ] ORDER BY в окне: порядок внутри партиции для накопительных и ранжирующих
- [ ] ROW_NUMBER(): уникальный номер строки в партиции
- [ ] RANK(), DENSE_RANK(): ранги с пропусками и без
- [ ] LAG(col, n), LEAD(col, n): значение из предыдущей/следующей строки
- [ ] Агрегаты как окно: SUM() OVER (PARTITION BY ... ORDER BY ...) — нарастающий итог
- [ ] Рамка окна: ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW; RANGE vs ROWS
- [ ] FIRST_VALUE, LAST_VALUE, NTH_VALUE

### 13. CTE (обобщённые табличные выражения)

- [ ] WITH cte_name AS (SELECT ...) SELECT * FROM cte_name
- [ ] Несколько CTE: WITH a AS (...), b AS (...) SELECT ...
- [ ] Рекурсивные CTE: WITH RECURSIVE ... UNION ALL; базовый член + рекурсивный член
- [ ] Иерархии (дерево): вывод поддерева от заданного узла
- [ ] Ограничение глубины рекурсии; циклы в графе
- [ ] CTE для читаемости и повторного использования в одном запросе
- [ ] Материализация CTE в PostgreSQL (NOT MATERIALIZED / MATERIALIZED)

### 14. Множества и пагинация

- [ ] UNION: объединение результатов (без дубликатов); UNION ALL (с дубликатами, быстрее)
- [ ] INTERSECT: строки, присутствующие в обоих результатах; EXCEPT: разность множеств
- [ ] Порядок столбцов и типы: одинаковое число и совместимые типы столбцов; ORDER BY по позиции или алиасу
- [ ] Пагинация через OFFSET/LIMIT: простота; проблема при больших OFFSET (полное сканирование до OFFSET)
- [ ] Keyset (cursor) пагинация: WHERE id > last_seen_id ORDER BY id LIMIT n; стабильная производительность
- [ ] Пагинация в приложении: передача последнего ключа; не передавать OFFSET для больших страниц

### 15. NULL и трёхзначная логика

- [ ] NULL: отсутствие значения; не равен ничему, в том числе NULL; сравнение с NULL даёт UNKNOWN
- [ ] Трёхзначная логика: TRUE, FALSE, UNKNOWN; AND/OR/NOT с UNKNOWN; WHERE отбрасывает FALSE и UNKNOWN
- [ ] IS NULL, IS NOT NULL: единственный корректный способ проверки на NULL
- [ ] COALESCE(x, y, ...): первое не-NULL значение; NULLIF(a, b): NULL если a = b
- [ ] IS DISTINCT FROM, IS NOT DISTINCT FROM: сравнение с учётом NULL (NULL IS DISTINCT FROM NULL → FALSE)
- [ ] NULL в сортировке: NULLS FIRST / NULLS LAST в ORDER BY
- [ ] NULL в GROUP BY: все NULL в одном значении группы; в UNIQUE (PostgreSQL: несколько NULL допустимы)
- [ ] NULL в агрегатах: COUNT(*) считает строки, COUNT(col) не считает NULL; SUM/AVG/MIN/MAX игнорируют NULL

### 16. Массовые операции и особенности DML

- [ ] Пакетная вставка: много INSERT в одной транзакции; COPY (PostgreSQL), LOAD DATA (MySQL), BULK INSERT
- [ ] COPY: форматы (text, csv, binary); заголовок; разделители; COPY FROM PROGRAM
- [ ] Транзакция вокруг DML: атомарность нескольких операций
- [ ] RETURNING в пакетах; выходные таблицы (INSERT ... RETURNING * INTO)
- [ ] Ограничения размера пакета; таймауты и блокировки при больших объёмах
- [ ] Вставка без индексов (временное DROP INDEX) и пересоздание после загрузки; отключение триггеров (осторожно)

---

## Часть IV. Транзакции и согласованность

### 16. ACID

- [ ] **Атомарность**: транзакция выполняется целиком или не выполняется; откат при ошибке
- [ ] **Согласованность**: переход из одного корректного состояния в другое; ограничения и инварианты
- [ ] **Изоляция**: параллельные транзакции не «видят» незавершённые изменения друг друга (в зависимости от уровня)
- [ ] **Долговечность**: после COMMIT данные сохранены на диске (через WAL) и не теряются при сбое
- [ ] BEGIN / START TRANSACTION; COMMIT; ROLLBACK; SAVEPOINT, ROLLBACK TO SAVEPOINT
- [ ] Автокоммит; неявное начало транзакции

### 17. Уровни изоляции

- [ ] **READ UNCOMMITTED**: грязное чтение возможно; редко используется
- [ ] **READ COMMITTED**: только закоммиченные данные; неповторяющееся чтение возможно (другая транзакция изменила строку между чтениями)
- [ ] **REPEATABLE READ**: снимок данных на начало транзакции; фантомное чтение возможно в некоторых СУБД
- [ ] **SERIALIZABLE**: полная изоляция; результат как при последовательном выполнении; блокировки или SSI (serializable snapshot isolation)
- [ ] Аномалии: грязное чтение, неповторяющееся чтение, фантом
- [ ] Установка уровня в сессии; отличия между PostgreSQL и MySQL по реализации

### 18. Блокировки

- [ ] Блокировки строк: при UPDATE, DELETE; блокировка до COMMIT/ROLLBACK
- [ ] SELECT FOR UPDATE: явная блокировка строк для обновления позже; FOR UPDATE SKIP LOCKED
- [ ] Блокировки таблиц: SHARE, EXCLUSIVE; LOCK TABLE
- [ ] Deadlock: две транзакции ждут друг друга; обнаружение, откат одной из них
- [ ] Ожидание блокировки: таймаут, nowait; стратегии уменьшения блокировок (короткие транзакции, порядок блокировок)
- [ ] Блокировки метаданных: при DDL (ALTER TABLE) в разных СУБД

### 19. MVCC

- [ ] Идея: хранить несколько версий строки; каждая транзакция видит снимок на свой момент
- [ ] Версионирование строк: xmin/xmax (PostgreSQL), номера транзакций; видимость по правилам
- [ ] Отсутствие блокировок при чтении: читатели не блокируют писателей и наоборот (в типичной реализации)
- [ ] Мёртвые строки: версии, которые больше никто не видит; необходимо удалять
- [ ] VACUUM (PostgreSQL): удаление мёртвых строк, возврат места; VACUUM FULL — перезапись таблицы
- [ ] Autovacuum: настройки (naptime, threshold, scale_factor), мониторинг; bloat (раздувание) таблиц и индексов
- [ ] Snapshot isolation и SERIALIZABLE через SSI (PostgreSQL); serialization failure и retry
- [ ] Transaction ID wraparound: риск исчерпания номера транзакции; autovacuum и freeze

### 20. Двухфазный коммит и длинные транзакции

- [ ] Двухфазный коммит (2PC): PREPARE TRANSACTION, COMMIT PREPARED; распределённые транзакции
- [ ] XA (внешний координатор): начало, подготовка, коммит/откат; поддержка в СУБД и драйверах
- [ ] Длинные транзакции: влияние на bloat (мёртвые строки не удаляются), репликацию (lag), блокировки
- [ ] Idle in transaction: транзакция открыта без активности; таймаут (idle_in_transaction_session_timeout)
- [ ] Рекомендации: короткие транзакции; не держать соединение с открытой транзакцией без дела

### 21. Оптимистичная и пессимистичная блокировка

- [ ] Пессимистичная: SELECT FOR UPDATE; блокировка строк до COMMIT; защита от одновременного изменения
- [ ] Оптимистичная: версионирование (version/timestamp); проверка при UPDATE (WHERE version = ?); конфликт при изменении
- [ ] Lost update: две транзакции читают и обновляют одну строку; вторая перезаписывает первую; решения (FOR UPDATE, версия)
- [ ] Идемпотентность: повторный вызов даёт тот же результат; идемпотентный ключ (UNIQUE), повторная вставка (ON CONFLICT DO NOTHING)
- [ ] SELECT FOR UPDATE SKIP LOCKED: пропуск заблокированных строк; очереди задач без ожидания

---

## Часть V. Хранение и память

### 22. Физическое хранение

- [ ] **Страница (page, block)**: единица хранения; обычно 8 KB (PostgreSQL), 16 KB (InnoDB по умолчанию)
- [ ] Файлы данных: таблицы и индексы в файлах; один или несколько файлов на таблицу
- [ ] Табличные пространства (tablespaces): размещение на разных дисках; CREATE TABLESPACE; default tablespace
- [ ] Сегменты и экстенты (некоторые СУБД): группы страниц
- [ ] Row-oriented: строки хранятся подряд; колоночное хранение (columnar) — отдельная тема для аналитики
- [ ] Размер страницы: влияние на размер строки, I/O; изменение (некоторые СУБД) при создании кластера

### 23. Буферный пул

- [ ] Кэш страниц в оперативной памяти: buffer pool (InnoDB), shared_buffers (PostgreSQL)
- [ ] Чтение: сначала из буфера; при промахе — с диска, страница помещается в буфер
- [ ] Запись: изменение в буфере; грязная (dirty) страница сбрасывается на диск позже
- [ ] Замена страниц: LRU (Least Recently Used) или варианты (clock-sweep в PostgreSQL)
- [ ] Read-ahead: предзагрузка следующих страниц при последовательном чтении
- [ ] Checkpoint: периодический сброс грязных страниц на диск; checkpoint_timeout, checkpoint_completion_target
- [ ] Настройка размера: доля RAM (25% и т.д.); слишком большой буфер — риск OOM, слишком маленький — лишний I/O

### 24. Журнал (WAL / redo)

- [ ] Write-ahead: запись изменений в журнал до сброса страниц на диск
- [ ] При сбое: восстановление путём воспроизведения WAL (redo)
- [ ] LSN (Log Sequence Number): позиция в WAL; порядок записей
- [ ] Full page write: первая модификация страницы после checkpoint записывает полную страницу в WAL (защита от частичной записи)
- [ ] Сегменты WAL, ротация (recycle); архивирование (archive_command) для PITR
- [ ] Синхронная vs асинхронная запись: synchronous_commit; fsync; компромисс надёжность/скорость
- [ ] Redo log в MySQL/InnoDB: аналогичная роль; doublewrite buffer (защита от partial page write)
- [ ] Undo log (InnoDB): откат транзакции и MVCC; отдельно от redo

### 25. Формат хранения строк

- [ ] Heap: строка в куче; указатели из индексов на строку (TID)
- [ ] Заголовок строки: метаданные (visibility, xmin/xmax, количество столбцов, битовая карта NULL)
- [ ] NULL: битовая карта или маски; экономия места; NULL не хранится как значение
- [ ] TOAST (PostgreSQL): большие значения (>2KB) выносятся в отдельное хранилище; PLAIN/EXTENDED/EXTERNAL/MAIN
- [ ] HOT (Heap Only Tuple): обновление без изменения индексов, если изменяемые столбцы не в индексах; fillfactor
- [ ] Сжатие: сжатие страниц или строк (в зависимости от СУБД); компромисс CPU/место
- [ ] Размер строки: ограничения (например, ~1.6TB в PostgreSQL); влияние на размер таблицы и индексов

### 26. Память: оценка и настройка

- [ ] Оценка размера таблицы: число строк × средний размер строки; выравнивание, заголовки страниц
- [ ] Размер индекса: B-tree примерно (ключ + указатель) × число записей + накладные расходы
- [ ] shared_buffers (PostgreSQL): рекомендации (25% RAM и т.д.); work_mem, maintenance_work_mem
- [ ] InnoDB buffer_pool_size: основной потребитель памяти у MySQL
- [ ] Кэш запросов, план запросов: ещё потребители памяти
- [ ] Риск исчерпания памяти при больших сортировках/хеш-соединениях (work_mem)

### 27. Дисковый I/O

- [ ] Последовательное чтение vs случайное: диски и SSD; случайное медленнее на HDD
- [ ] Влияние на производительность: полное сканирование таблицы (sequential) vs много точечных чтений (random)
- [ ] Параметр random_page_cost (PostgreSQL): отношение стоимости случайной к последовательной; для SSD уменьшать
- [ ] Очереди I/O, планировщики; NVMe, дисковые массивы
- [ ] Мониторинг: статистика I/O, ожидание на диск

### 28. Практическая оценка хранения и памяти

- [ ] Прикидка размера таблицы/индекса до запуска: число строк, средний размер, накладные расходы
- [ ] Проверка “влезет ли рабочий набор в память” и что случится, если не влезет
- [ ] Как связаны формат строки, WAL, буферный пул и I/O в реальной производительности
- [ ] Почему оценка хранения нужна до миграций, before-load и capacity planning

---

## Часть VI. Индексы

### 29. Назначение индексов

- [ ] Ускорение поиска по условию (WHERE), сортировки (ORDER BY), группировки (GROUP BY), JOIN
- [ ] Замедление INSERT/UPDATE/DELETE: обновление каждого индекса; HOT-обновление (без изменения индексов)
- [ ] Когда не индексировать: маленькие таблицы, столбцы с низкой селективностью, редко используемые в условиях
- [ ] Баланс: сколько индексов на таблицу; мониторинг использования (pg_stat_user_indexes.idx_scan)
- [ ] Неиспользуемые индексы: idx_scan = 0; осторожно — редкие запросы; избыточные индексы (подмножество другого)
- [ ] Дублирующие индексы: одинаковое определение; лишние затраты на запись

### 30. B-tree

- [ ] Сбалансированное дерево: все листья на одном уровне
- [ ] Узлы: ключи и указатели на дочерние узлы или на строки (листья)
- [ ] Поиск: O(log N); диапазонные запросы (BETWEEN, >, <) эффективны за счёт порядка
- [ ] Сортировка по ключу: листья связаны; index-only scan если все нужные столбцы в индексе
- [ ] Уникальный vs неуникальный индекс; включение столбцов (INCLUDE) для покрывающего индекса
- [ ] Порядок сортировки: ASC/DESC; влияние на запросы с ORDER BY

### 31. Hash-индекс

- [ ] Хеш-функция от ключа → номер корзины; точечный поиск по равенству
- [ ] Нет поддержки диапазонов и сортировки
- [ ] В PostgreSQL hash-индекс (улучшен в 10+); в MySQL InnoDB — нет hash по умолчанию (есть адаптивный hash для внутренних целей)
- [ ] Когда уместен: только WHERE key = constant

### 32. Специализированные индексы

- [ ] **GiST**: обобщённое дерево поиска; диапазоны, полнотекст, геометрия, разнообразные типы
- [ ] **GIN**: инвертированный индекс; полнотекст, массивы, JSONB (содержание, ключи)
- [ ] **BRIN**: блоки диапазонов; минимальный размер; подходит для данных, упорядоченных по столбцу (время)
- [ ] **Пространственные**: PostGIS, R-tree; поиск по геометрии
- [ ] **Полнотекстовый**: токены, стемминг, ранжирование; GIN/GiST в PostgreSQL
- [ ] **Частичный индекс**: только строки, удовлетворяющие условию; меньше размер, быстрее обновление
- [ ] **Индекс по выражению**: индекс на выражение (например, LOWER(email))

### 33. Составные индексы

- [ ] Порядок столбцов важен: (a, b) полезен для WHERE a = ? AND b = ?, для WHERE a = ?, но не для одного WHERE b = ?
- [ ] Правило «левого префикса»: использование первых столбцов индекса
- [ ] Покрывающий индекс (covering): все нужные столбцы в индексе (INCLUDE в PostgreSQL); index-only scan
- [ ] Составной уникальный индекс: уникальность по комбинации

### 34. Обслуживание индексов

- [ ] Создание: CREATE INDEX; CONCURRENTLY в PostgreSQL (без блокировки записи)
- [ ] Перестроение: REINDEX; когда индекс раздут или повреждён
- [ ] Фрагментация: заполненность страниц; VACUUM, перестроение
- [ ] Анализ использования: какие индексы не используются; осторожно с выводом (редкие запросы)
- [ ] Партиционирование и индексы: локальные индексы по партициям

### 35. Мониторинг использования индексов

- [ ] Проверка `idx_scan`, чтений и записей по индексам; поиск неиспользуемых и дублирующих индексов
- [ ] Связь индексов с планами выполнения: почему “индекс есть” не означает “он будет выбран”
- [ ] Индексы как цена записи: как отслеживать, когда ускорение чтения уже не окупает запись

---

## Часть VII. Оптимизация запросов

### 31. Планы выполнения

- [ ] EXPLAIN: вывод плана без выполнения
- [ ] EXPLAIN ANALYZE: выполнение и фактические времена и числа строк
- [ ] Узлы плана: Seq Scan (полное сканирование), Index Scan, Index Only Scan
- [ ] Join: Nested Loop, Hash Join, Merge Join; когда какой
- [ ] Sort, Aggregate, Limit; подузлы (план дерева)
- [ ] Оценка cost: условные единицы; сравнение альтернатив оптимизатором
- [ ] Буферы: EXPLAIN (ANALYZE, BUFFERS) — чтение из кэша vs диск

### 32. Статистика

- [ ] Сбор статистики: ANALYZE (или автоматический автоанализатор); гистограммы по столбцам
- [ ] Cardinality: оценка числа строк; влияет на выбор плана
- [ ] Селективность: доля строк, удовлетворяющих условию; оценка по гистограмме
- [ ] Устаревшая статистика: после массовых изменений; неверные планы
- [ ] Ручная настройка: увеличение статистики по столбцам для сложных столбцов (ALTER TABLE ... SET STATISTICS)

### 33. Выбор плана оптимизатором

- [ ] Cost-based optimizer: оценка стоимости каждого варианта (последовательное чтение, случайное, CPU)
- [ ] Порядок JOIN: перебор вариантов; динамическое программирование, жадные стратегии
- [ ] Подзапросы: развертывание в JOIN, материализация
- [ ] Ограничения оптимизатора: не все планы перебираются; подсказки (hints) в некоторых СУБД
- [ ] Планы с параметрами: подготовленные запросы; возможная неоптимальность при первом наборе параметров

### 34. Антипаттерны запросов

- [ ] N+1: много запросов в цикле вместо одного с JOIN или IN
- [ ] Отсутствие индекса на условиях WHERE и JOIN
- [ ] SELECT *: лишние данные, невозможность index-only scan
- [ ] Избыточные подзапросы: повторяющийся подзапрос вместо CTE/временной таблицы
- [ ] Неоптимальные типы: несоответствие типов в JOIN (приведение, отказ от индекса)
- [ ] Слишком большие IN-списки; ограничение и батчинг
- [ ] Игнорирование блокировок: длинные транзакции, блокировка многих строк

### 35. Настройка СУБД

- [ ] work_mem / sort_buffer_size: память на сортировку и хеш; слишком мало — сброс на диск
- [ ] random_page_cost, seq_page_cost: для SSD уменьшать random_page_cost
- [ ] effective_cache_size: оценка кэша ОС для планировщика
- [ ] Параллельное выполнение: max_parallel_workers, parallel tuple cost
- [ ] JIT-компиляция (PostgreSQL 11+): для сложных запросов
- [ ] Логирование медленных запросов: log_min_duration_statement, slow query log

---

## Часть XIV. Партиционирование и внутренности хранилища

### 73. Партиционирование таблиц

- [ ] Declarative partitioning (PostgreSQL 10+): PARTITION BY RANGE/LIST/HASH
- [ ] Создание партиций: CREATE TABLE ... PARTITION OF; диапазон/список для RANGE/LIST
- [ ] Default partition: партиция «по умолчанию» для значений вне заданных диапазонов
- [ ] Присоединение и отсоединение: ATTACH PARTITION, DETACH PARTITION; архивирование старых данных
- [ ] Уникальность и FK: первичный ключ и уникальные индексы должны включать ключ партиционирования
- [ ] Индексы: создание на родительской таблице — создаётся на каждой партиции (локальные индексы)

### 74. Partition pruning и partition-wise операции

- [ ] Partition pruning: отсечение партиций по условию WHERE; статический (при планировании) и динамический (при выполнении)
- [ ] Подготовленные запросы: возможная неоптимальность при первом наборе параметров (все партиции)
- [ ] Partition-wise join: соединение партиционированных таблиц по партициям; меньше памяти
- [ ] Partition-wise aggregate: агрегация по партициям с последующим объединением
- [ ] Субпартиционирование: партиция внутри партиции (например, по диапазону и по списку)

### 75. WAL, восстановление и PITR

- [ ] Сегменты WAL: размер (16 MB по умолчанию); ротация при заполнении
- [ ] archive_command: копирование сегментов в архив (например, в S3); restore_command при восстановлении
- [ ] recovery_target_time, recovery_target_lsn: восстановление до момента или до LSN
- [ ] standby.signal / recovery.conf: режим standby (реплика); promote для переключения на primary
- [ ] PITR (Point-in-Time Recovery): полный бэкап + WAL до нужного момента

### 76. VACUUM и autovacuum

- [ ] VACUUM: удаление мёртвых строк; возврат места в таблицу (не в ОС без FULL); обновление visibility map
- [ ] VACUUM FULL: перезапись таблицы; эксклюзивная блокировка; сжатие
- [ ] VACUUM FREEZE: заморозка старых версий строк; защита от transaction ID wraparound
- [ ] Autovacuum: настройки (autovacuum_naptime, autovacuum_vacuum_threshold, scale_factor)
- [ ] Мониторинг: pg_stat_user_tables (n_dead_tup, last_vacuum, last_autovacuum)
- [ ] Ручной ANALYZE после массовых изменений; autovacuum_analyze_*

### 77. Репликация PostgreSQL (детали)

- [ ] Streaming replication: поток WAL от primary к replica; синхронная (synchronous_commit, synchronous_standby_names) vs асинхронная
- [ ] Репликационные слоты: сохранение WAL для подписчика; риск накопления WAL при отстающей реплике
- [ ] Логическая репликация: публикация (CREATE PUBLICATION) и подписка (CREATE SUBSCRIPTION)
- [ ] Конфликты при логической репликации: replica identity (FULL, DEFAULT, INDEX); разрешение конфликтов (error, apply, skip)
- [ ] Декодирование: pgoutput, test_decoding, wal2json; логирование изменений для CDC

### 78. Резервное копирование и восстановление (детали)

- [ ] pg_basebackup: полная копия кластера (tar, plain); для создания реплики или бэкапа
- [ ] pg_dump: логический дамп (plain, custom, directory); выбор объектов (таблицы, схема)
- [ ] pg_dump -j: параллельный дамп; pg_restore -j: параллельное восстановление
- [ ] Инкрементальный бэкап: только изменённые файлы (файловый уровень); WAL между полными бэкапами
- [ ] Проверка восстановления: регулярный тест восстановления; RTO, RPO
- [ ] Реплика не заменяет бэкап: случайное удаление/повреждение реплицируется на все узлы

---

## Часть VIII. Реляционные СУБД: продукты

### 36. PostgreSQL

- [ ] Архитектура: процессы (postmaster, backend, background workers), shared memory
- [ ] Расширения: pgvector, PostGIS, pg_cron, и др.; установка и использование
- [ ] Типы: JSONB, массивы, диапазоны (int4range, tstzrange), UUID, сетевые (inet, cidr)
- [ ] Партиционирование: по диапазону, списку, хешу; партиции по умолчанию
- [ ] Логическая репликация; слоты репликации
- [ ] Конфигурация: postgresql.conf, pg_hba.conf
- [ ] Системные каталоги: pg_class, pg_attribute, pg_index; полезные представления (pg_stat_*, pg_size_*)

### 37. MySQL / MariaDB

- [ ] Движки хранения: InnoDB (транзакционный, по умолчанию), MyISAM (табличные блокировки, без транзакций)
- [ ] Отличия от PostgreSQL: диалект SQL, автоинкремент, репликация на основе бинарного лога
- [ ] Репликация: мастер–реплика, GTID; группировка (group replication)
- [ ] Настройки: innodb_buffer_pool_size, изоляция по умолчанию (REPEATABLE READ)
- [ ] MariaDB: движки (Aria, ColumnStore), совместимость с MySQL

### 38. SQLite

- [ ] Встраиваемая: один файл или in-memory; без отдельного сервера
- [ ] Один писатель: запись последовательна; чтений много
- [ ] Ограничения: ограниченный параллелизм записи, нет сетевого доступа «из коробки»
- [ ] Типы: гибкая типизация (affinity); INTEGER, TEXT, BLOB, REAL
- [ ] Когда использовать: приложения, тесты, встроенные устройства, прототипы
- [ ] WAL mode: улучшение параллелизма чтения/записи
- [ ] PRAGMA: настройки (journal_mode, synchronous, cache_size)

### 39. Другие реляционные СУБД

- [ ] Oracle: RAC, PL/SQL, лицензии; обзор отличий
- [ ] SQL Server: T-SQL, интеграция с экосистемой Microsoft; Always On
- [ ] CockroachDB: распределённая SQL, совместимость с PostgreSQL; глобальное распределение
- [ ] Сравнение: лицензии, возможности, экосистема, когда что выбирать

### 40. Подключение из приложения

- [ ] Драйверы: psycopg2, asyncpg (Python); JDBC, Hibernate (Java); и др.
- [ ] Пул соединений: ограничение числа соединений, переиспользование; PgBouncer, эквиваленты
- [ ] Подготовленные выражения (prepared statements): план кэшируется; защита от SQL-инъекций
- [ ] ORM vs raw SQL: плюсы ORM (безопасность, переносимость), минусы (сложные запросы, контроль)
- [ ] Миграции схемы: Alembic, Flyway, Liquibase; версионирование DDL

---

## Часть XIII. SQL углублённо: типы, представления, процедуры

### 66. Типы данных углублённо

- [ ] Точность числовых: DECIMAL(10,2); округление при переполнении; float vs decimal для денег
- [ ] Коллации (COLLATE): порядок сортировки строк; locale (lc_collate, lc_ctype); case-sensitive vs insensitive
- [ ] Кодировки: UTF-8, client_encoding; байтовая vs символьная длина (octet_length vs char_length)
- [ ] Дата и время: TIMESTAMP WITH TIME ZONE vs WITHOUT; AT TIME ZONE; INTERVAL; extract(), date_trunc()
- [ ] Таймзоны: имена (Europe/Moscow), смещение; хранение в UTC; вывод в локальной зоне
- [ ] Перечисления (ENUM): CREATE TYPE ... AS ENUM; добавление значений; порядок
- [ ] Домены (CREATE DOMAIN): тип с ограничением (CHECK); переиспользование
- [ ] Составные типы (CREATE TYPE): тип как набор полей; использование в таблицах

### 67. JSON, XML, массивы, диапазоны

- [ ] JSON vs JSONB (PostgreSQL): JSONB — бинарный, индексируемый; операторы @>, ?, ->, ->>, #>, #>>
- [ ] jsonpath: SQL/JSON path; фильтрация и извлечение; индексы по выражению
- [ ] Массивы: ARRAY[], операторы &&, @>, <@, [] (индекс); unnest(); индексы GIN
- [ ] Диапазоны: int4range, tstzrange; операторы &&, @>, <@; индексы GiST
- [ ] XML: тип xml; xpath(), xmlagg(); редко в приложениях
- [ ] Сетевые типы: inet, cidr; операторы <<, >>, &&; маски подсети

### 68. Полнотекстовый поиск в SQL

- [ ] tsvector: лексемы с позициями; to_tsvector('english', text); конфигурации (simple, english)
- [ ] tsquery: to_tsquery, plainto_tsquery, websearch_to_tsquery; AND, OR, NOT
- [ ] Операторы: @@ (соответствие), ts_rank(), ts_headline(); ранжирование и подсветка
- [ ] Индексы: GIN по tsvector; полнотекстовый индекс (GIN/GiST)
- [ ] Словари: стемминг, стоп-слова; кастомные словари; thesaurus
- [ ] Триграммы (pg_trgm): similarity(), % ; LIKE/ILIKE через GIN; нечёткий поиск

### 69. Представления и материализованные представления

- [ ] VIEW: виртуальная таблица; определение как запрос; WITH CHECK OPTION (LOCAL/CASCADED)
- [ ] Обновляемые представления: простые (одна таблица, без агрегатов); INSTEAD OF триггер для сложных
- [ ] Материализованное представление: CREATE MATERIALIZED VIEW; хранение результата на диске
- [ ] REFRESH MATERIALIZED VIEW; REFRESH CONCURRENTLY (без блокировки чтения)
- [ ] WITH NO DATA: создание без начальных данных; затем REFRESH
- [ ] Правила (rules) vs триггеры: правила переписывают запрос; триггеры выполняют код

### 70. Триггеры

- [ ] BEFORE/AFTER: момент срабатывания; FOR EACH ROW vs FOR EACH STATEMENT
- [ ] Триггерная функция: NEW, OLD (для row); RETURN NEW/OLD/NULL
- [ ] INSTEAD OF: для представлений; одна строка за раз
- [ ] Условные триггеры: WHEN (condition); только при выполнении условия
- [ ] Порядок триггеров: несколько триггеров на одно событие; имя и порядок
- [ ] Constraint trigger: отложенное срабатывание (DEFERRED)
- [ ] Event trigger (DDL): ddl_command_start, ddl_command_end, sql_drop; отмена DDL

### 71. Хранимые процедуры и функции

- [ ] Функция: RETURNS тип; VOLATILE/STABLE/IMMUTABLE; влияние на кэширование и оптимизатор
- [ ] Параметры: IN, OUT, INOUT; значения по умолчанию; VARIADIC (массив аргументов)
- [ ] PL/pgSQL: объявление переменных, IF/LOOP/RETURN; EXCEPTION блок
- [ ] Курсор: DECLARE, OPEN, FETCH, CLOSE; курсор в процедуре для постраничной обработки
- [ ] Динамический SQL: EXECUTE format(); опасность инъекций; использование %s для параметров
- [ ] SECURITY DEFINER vs INVOKER: выполнение с правами владельца или вызывающего
- [ ] Процедура (PROCEDURE): без возврата; CALL; COMMIT внутри (некоторые СУБД)
- [ ] Параллельное выполнение: PARALLEL SAFE/UNSAFE/RESTRICTED

### 72. Последовательности и IDENTITY

- [ ] CREATE SEQUENCE; nextval(), currval(), setval(); использование в DEFAULT
- [ ] Свойства: START, INCREMENT, MINVALUE, MAXVALUE, CYCLE, CACHE
- [ ] Разрывы в нумерации: CACHE, откат транзакции, nextval() коммитится сразу
- [ ] GENERATED ALWAYS AS IDENTITY / BY DEFAULT: автоинкремент в стандарте SQL
- [ ] SERIAL, BIGSERIAL: обёртка над sequence в PostgreSQL
- [ ] Репликация и последовательности: логическая репликация — синхронизация sequence; слоты

---

## Часть IX. NoSQL и альтернативные модели

### 49. NoSQL обзор

- [ ] Причины появления: масштаб, гибкая схема, распределённость, специализированные модели
- [ ] CAP-теорема: из трёх (Consistency, Availability, Partition tolerance) при разделении сети можно гарантировать только два
- [ ] Eventual consistency: в итоге все реплики сойдутся; чтение может быть «устаревшим»
- [ ] Когда выбирать NoSQL: большие объёмы, горизонтальное масштабирование, документы/граф/кэш по модели данных
- [ ] Когда оставаться на SQL: сложные связи, транзакции, отчётность, целостность

### 50. Документные БД (MongoDB и др.)

- [ ] Документ: единица хранения (JSON/BSON); вложенные объекты и массивы; размер лимит (16 MB в MongoDB)
- [ ] Коллекции: аналог таблицы; без жёсткой схемы; валидация схемы опциональна
- [ ] Запросы: find(), по полям, вложенным (dot notation), массивам ($elemMatch); проекция, сортировка, skip/limit
- [ ] Агрегация: pipeline ($match, $group, $project, $lookup — аналог JOIN, $unwind, $sort, $limit)
- [ ] Индексы: одиночные, составные, мультиключевые (массивы), полнотекстовые, геопространственные, TTL, hashed (для шардирования)
- [ ] Read concern: local, available, majority, linearizable, snapshot
- [ ] Write concern: w:1, majority; journal; таймауты
- [ ] Транзакции: многодокументные (multi-document); снимок на начало транзакции
- [ ] Replica set: primary, secondary, arbiter; выбор primary (election); чтение из secondary (read preference)
- [ ] Sharding: shard key; chunks; balancer; выбор ключа (cardinality, равномерность)
- [ ] Change streams: подписка на изменения в коллекции; для CDC и кэширования
- [ ] CouchDB, Couchbase, RavenDB: отличия от MongoDB; CouchDB — multi-master, конфликты

### 51. Ключ–значение (Redis и др.)

- [ ] Модель: key → value; ключ — строка; значение — строка или структура (list, set, hash, zset, stream)
- [ ] Redis: строки (GET/SET), списки (LPUSH/RPOP — очереди), множества (SADD/SINTER), хеши (HGET/HSET), sorted sets (ZADD/ZRANGE по score), streams (consumer groups)
- [ ] TTL: EXPIRE, PTTL; кэш с истечением; ключи без TTL — постоянные
- [ ] Персистентность: RDB (снимки по расписанию), AOF (append-only, fsync always/everysec/no); гибрид RDB+AOF
- [ ] Однопоточность: одна команда за раз; блокирующие команды (BLPOP); pipeline (batch без round-trip)
- [ ] Транзакции: MULTI/EXEC; атомарность набора команд; WATCH — оптимистичная блокировка
- [ ] Lua: EVAL для атомарных скриптов; ограничения (время, память)
- [ ] Pub/Sub: PUBLISH/SUBSCRIBE; нет персистентности сообщений; для уведомлений
- [ ] Streams: XADD, XREADGROUP; consumer groups; персистентность; аналог Kafka-lite
- [ ] Кластер Redis: 16384 слота; шардирование по хешу ключа; репликация слотов; MOVED/ASK
- [ ] Sentinel: мониторинг; автоматический failover; кворум
- [ ] Memcached: только строки; без персистентности; проще; когда достаточно кэша
- [ ] KeyDB, Dragonfly: совместимость с Redis; многопоточность; большая пропускная способность

### 52. Широкостолбцовые (Cassandra, ScyllaDB)

- [ ] Модель: partition key → множество строк (clustering columns + столбцы); разреженная таблица
- [ ] Партиционирование: по partition key; данные распределены по узлам
- [ ] Запись: запись очень быстрая (append-oriented); чтение по ключу партиции
- [ ] QUORUM: согласованность при записи/чтении; настройка уровня консистентности
- [ ] CQL: SQL-подобный язык; ограничения по сравнению с реляционными (нет JOIN, ограниченные запросы)
- [ ] Когда использовать: большие объёмы записей, распределённость, отказоустойчивость; временные ряды, события
- [ ] ScyllaDB: совместимость с Cassandra, переписан на C++; меньшая задержка

### 53. Графовые БД (Neo4j и др.)

- [ ] Модель: узлы (сущности), рёбра (связи), свойства у обоих
- [ ] Cypher: декларативный язык запросов; MATCH (a)-[:REL]->(b) WHERE ...
- [ ] Обход графа: переменная длина пути, кратчайший путь
- [ ] Когда реляционная модель неудобна: много связей «многие ко многим», иерархии с переменной глубиной, рекомендации, соцграфы
- [ ] Индексы: по свойствам узлов и рёбер
- [ ] Другие: Amazon Neptune, граф в PostgreSQL (расширения), в памяти (NetworkX — не БД)
- [ ] Память: граф часто держат в RAM для скорости обхода

### 54. Временные ряды (InfluxDB, TimescaleDB)

- [ ] Данные: метрики/события с временной меткой; теги и поля
- [ ] InfluxDB: запись высокопроизводительная; сжатие по времени; запросы на своем языке и SQL-like
- [ ] TimescaleDB: расширение PostgreSQL; гибрид SQL + временные ряды; партиции по времени
- [ ] Агрегация по времени: downsampling, окна (1m, 1h); хранение сырых и агрегатов
- [ ] Сжатие: эффективное хранение за счёт упорядоченности по времени
- [ ] Retention: политики удаления старых данных
- [ ] Prometheus + PromQL: метрики, не универсальная БД; Thanos, VictoriaMetrics

### 55. Поисковые движки (Elasticsearch, OpenSearch)

- [ ] Назначение: полнотекстовый поиск, аналитика логов; не замена основной БД для транзакций
- [ ] Индексы: инвертированный индекс по токенам; анализ текста (анализаторы)
- [ ] Запросы: match, term, bool, агрегации; подсветка, подсказки
- [ ] Масштабирование: шарды и реплики; распределённый поиск
- [ ] Логи и метрики: типичный сценарий (ELK/Loki); хранение и ротация
- [ ] Синхронизация с основной БД: логирование изменений, ETL, CDC

### 56. Многомодельные и выбор стека

- [ ] Многомодельные СУБД: одна система — документы + граф или ключ–значение + документы (ArangoDB, OrientDB и др.)
- [ ] Гибридный стек: PostgreSQL (основные данные) + Redis (кэш/сессии) + Elasticsearch (поиск) + векторная БД (RAG)
- [ ] Критерии выбора: модель данных, объём, согласованность, операционная сложность, команда
- [ ] Антипаттерны: использование NoSQL «потому что модно»; отказ от реляционной БД без веской причины

---

## Часть X. Векторные базы данных

### 57. Эмбеддинги и векторный поиск

- [ ] Эмбеддинг: вектор чисел (часто 384–1536 размерности), представляющий смысл текста/изображения
- [ ] Поиск по сходству: найти k ближайших векторов (k-NN); косинусное сходство, L2 (евклидово), скалярное произведение
- [ ] Нормализация: для косинуса векторы нормируют; тогда косинус = скалярное произведение; единичная сфера
- [ ] Метрики расстояния: L2 (евклидово), косинус (1 - cosine_similarity), dot product (для нормированных)
- [ ] Применения: семантический поиск, рекомендации, дедупликация, RAG (поиск релевантных чанков), кластеризация
- [ ] Модели эмбеддингов: OpenAI (text-embedding-ada-002, размерность 1536), sentence-transformers (all-MiniLM-L6-v2 и др.), Cohere
- [ ] Размерность: больше — потенциально точнее, но больше памяти и медленнее; компромисс

### 58. Индексы для векторов

- [ ] Точный поиск (brute force): перебор всех векторов; O(N); приемлемо для малых коллекций
- [ ] Приближённый поиск (ANN): быстрее, с потерей точности
- [ ] HNSW (Hierarchical Navigable Small World): граф; высокая точность, хорошая скорость; память
- [ ] IVF (Inverted File Index): кластеризация (k-means), поиск по ближайшим центроидам; параметр nlist, nprobe
- [ ] LSH (Locality Sensitive Hashing): хеширование, сохраняющее близость; вероятностный поиск
- [ ] Квантизация: сжатие векторов (PQ, SQ); экономия памяти и ускорение при небольшой потере точности
- [ ] Сравнение: recall vs скорость vs память; настройка под задачу

### 59. Продукты векторных БД

- [ ] **pgvector** (PostgreSQL): расширение; типы vector, индексы ivfflat, hnsw; интеграция с обычным SQL
- [ ] **Pinecone**: managed; простое API; под RAG и рекомендации
- [ ] **Weaviate**: векторная + объектная модель; фильтрация по метаданным; модули (текст, изображения)
- [ ] **Chroma**: открытая; встраиваемая; для разработки и небольших проектов
- [ ] **Qdrant**: фильтры, полезные нагрузки; Rust
- [ ] **Milvus**: масштабируемая; несколько типов индексов; для больших объёмов
- [ ] Сравнение: managed vs self-hosted, размерность, фильтры, экосистема

### 60. RAG и гибридный поиск

- [ ] RAG: поиск релевантных фрагментов по запросу (векторный поиск) + передача в LLM
- [ ] Гибридный поиск: векторный + ключевой/полнотекстовый; комбинирование рангов (RRF и др.)
- [ ] Метаданные и фильтрация: отбор по полям (категория, дата) до или после векторного поиска
- [ ] Чанкинг: разбиение документов на чанки; перекрытие; влияние на качество RAG
- [ ] Переранжирование: быстрый векторный отбор → точная модель переранжирования (cross-encoder)

### 61. Память и масштабирование векторных БД

- [ ] Размер индекса: число векторов × размерность × размер числа (4/8 байт); квантизация уменьшает
- [ ] RAM: многие индексы загружаются в память для скорости; ограничение по размеру датасета
- [ ] Шардирование: разбиение по метаданным или по диапазонам векторов; распределённый поиск
- [ ] Горизонтальное масштабирование: добавление узлов; репликация для отказоустойчивости
- [ ] Обновление и удаление: поддержка в продуктах; перестроение индекса при больших изменениях

---

## Часть XI. Масштабирование и отказоустойчивость

### 62. Репликация

- [ ] Мастер–реплика (primary–replica): один узел принимает запись, реплики копируют данные
- [ ] Логическая репликация: поток изменений (логических записей); возможность фильтрации и преобразований
- [ ] Физическая репликация: копирование блоков/страниц; реплика — точная копия
- [ ] Синхронная vs асинхронная: синхронная — запись подтверждается после записи на реплику; задержка и доступность
- [ ] Реплика только для чтения: разгрузка мастера; задержка репликации (lag)
- [ ] Каскадная репликация: реплика от реплики

### 63. Чтение из реплик

- [ ] Балансировка: направление части запросов на реплики
- [ ] Задержка репликации: риск чтения устаревших данных; допустимость для сценария
- [ ] Консистентное чтение: чтение только после синхронной реплики или с ожиданием применения
- [ ] Распределение по репликам: round-robin, по задержке, по региону

### 64. Шардирование

- [ ] Горизонтальное разбиение: данные распределены по узлам (шардам); ключ шардирования определяет шард
- [ ] Ключ шардирования: выбор столбца/выражения; равномерность (hash); диапазон (range) — риск горячих границ
- [ ] Горячие ключи (hot spots): один ключ — много трафика; перебалансировка, разделение ключа, соль
- [ ] Запросы: запрос в один шард по ключу; cross-shard — scatter-gather (все шарды), агрегация, сортировка
- [ ] JOIN между шардами: colocation (одинаковый ключ шардирования); broadcast (малая таблица); shuffle (перераспределение)
- [ ] Транзакции: single-shard — локально; cross-shard — 2PC или избегать
- [ ] Партиционирование внутри СУБД vs шардирование между инстансами (разные серверы)
- [ ] Citus (PostgreSQL): distributed table, reference table (реплика на все узлы), colocation; rebalance
- [ ] Vitess: keyspace, shard, vindex (various index); маршрутизация запросов; resharding
- [ ] Обратная сторона: сложность JOIN между шардами, транзакции, миграции, resharding

### 65. CAP и PACELC

- [ ] CAP: при разделении сети (Partition) — либо Consistency, либо Availability
- [ ] Практика: разделения редки; часто выбирают отказ от строгой консистентности (eventual) ради доступности
- [ ] PACELC: при Partition — A или C; иначе (E — Else) — Latency или Consistency
- [ ] Выбор при проектировании: что критичнее — консистентность или доступность/задержка; примеры (банк vs лайки)

### 66. Лидерство и кворум

- [ ] Выбор лидера: при отказе мастера — кто станет новым; ручной или автоматический (consensus)
- [ ] Split-brain: два узла считают себя лидерами при разделении сети; предотвращение через кворум
- [ ] Кворум: решение принимается при согласии большинства узлов (или взвешенного большинства)
- [ ] Raft, Paxos: алгоритмы консенсуса — упрощённое понимание; лидер, лог, коммит
- [ ] Практика: etcd, Consul для координации; встроенный консенсус в CockroachDB, MongoDB replica set

### 67. Резервное копирование и восстановление

- [ ] Полный бэкап: копия всех данных на момент времени; долго, много места
- [ ] Инкрементальный: только изменения с последнего бэкапа; быстрее восстановление при комбинации
- [ ] WAL-архивирование: непрерывная передача сегментов WAL; основа PITR
- [ ] PITR (Point-in-Time Recovery): восстановление до произвольного момента в прошлом
- [ ] Стратегии: частота полного/инкрементального; хранение копий; проверка восстановления
- [ ] Реплика не заменяет бэкап: случайное удаление/повреждение реплицируется

### 68. Мост к следующим advanced-темам

- [ ] Distributed transactions, saga, outbox и CDC углубляются в частях `XXXVII` и `XXII`
- [ ] NewSQL, geo-distributed и глобальная консистентность продолжаются в частях `XXV` и `XLI`
- [ ] Event log, Kafka, CQRS и event sourcing как соседняя архитектурная тема продолжаются после ядра, а не внутри одной части XI

---

## Часть XII. Операционная часть и безопасность

### 73. Мониторинг

- [ ] Метрики: QPS (запросов в секунду), задержка (p50, p95, p99), ошибки, таймауты
- [ ] Ресурсы: использование CPU, RAM (shared_buffers, work_mem, кэш ОС), диска; очередь I/O; temp files
- [ ] Репликация: lag реплики (в байтах, секундах); pg_stat_replication; синхронная реплика — ожидание
- [ ] Соединения: pg_stat_activity; idle in transaction; блокировки (pg_locks); long-running queries
- [ ] Кэш: hit ratio буферного пула; effective_cache_size для планировщика
- [ ] pg_stat_statements: запросы по времени выполнения, количеству вызовов; нормализация запроса (queryid)
- [ ] auto_explain: автоматическое логирование планов медленных запросов
- [ ] Алерты: пороги по задержке, ошибкам, заполнению диска, lag, deadlocks
- [ ] Дашборды: Grafana; экспортёры (postgres_exporter, node_exporter); pgAdmin, PMM
- [ ] Логи: log_min_duration_statement, log_connections, log_disconnections; централизованный сбор (ELK, Loki)
- [ ] pg_stat_progress_*: прогресс VACUUM, CREATE INDEX; мониторинг длительных операций

### 74. Миграции схемы

- [ ] Версионирование DDL: миграции как скрипты с номерами/именами; применение по порядку; таблица версий (schema_migrations)
- [ ] Обратная миграция (rollback): откат последней миграции; не всегда возможен (потеря данных при DROP)
- [ ] Блокировки при ALTER: ADD COLUMN с DEFAULT в PostgreSQL 11+ — без перезаписи; ALTER типа/ADD NOT NULL — полная перезапись или блокировка
- [ ] CREATE INDEX CONCURRENTLY: создание индекса без блокировки записи; два прохода; нельзя в транзакции
- [ ] Zero-downtime: добавление столбца без NOT NULL → заполнение в фоне → ADD NOT NULL; переключение приложения на новую таблицу (blue-green)
- [ ] Разделение миграций: данные и схема отдельно; обратная совместимость (старая и новая версия приложения работают со схемой)
- [ ] Инструменты: Alembic (Python), Flyway (Java), Liquibase, golang-migrate; сравнение (язык, откат, транзакции)
- [ ] Миграции в CI/CD: применение при деплое; проверка перед мержем; тестовое окружение с теми же миграциями

### 75. Безопасность

- [ ] Аутентификация: пароль (SCRAM-SHA-256 в PG), сертификаты (clientcert=verify-full), LDAP, GSSAPI/Kerberos
- [ ] pg_hba.conf: host, user, database, method (md5, scram-sha-256, cert, ldap); порядок правил
- [ ] Авторизация: роли (CREATE ROLE); наследование ролей (GRANT role TO role); привилегии (GRANT/REVOKE)
- [ ] Привилегии: SELECT, INSERT, UPDATE, DELETE; на таблицу, столбец, схему; DEFAULT PRIVILEGES
- [ ] Минимальные привилегии: отдельный пользователь для приложения; не суперпользователь; только нужные объекты
- [ ] RLS (Row Level Security): политики (USING — кто видит, WITH CHECK — кто пишет); принудительная RLS
- [ ] SECURITY DEFINER: функция выполняется с правами владельца; осторожность с search_path и инъекциями
- [ ] Шифрование at rest: шифрование диска (LUKS) или TDE (прозрачное шифрование табличных пространств)
- [ ] Шифрование in transit: TLS (sslmode=verify-full); сертификаты сервера и клиента
- [ ] Секреты: пароли не в коде; переменные окружения, секрет-менеджеры (HashiCorp Vault)
- [ ] Аудит: pgaudit (расширение); логирование SELECT/INSERT/...; таблицы аудита в приложении

### 76. SQL-инъекции

- [ ] Суть: подстановка пользовательского ввода в SQL без экранирования; выполнение произвольного SQL
- [ ] Защита: подготовленные выражения (prepared statements) — параметры не интерпретируются как SQL
- [ ] Экранирование: если подготовленные выражения недоступны — осторожное экранирование; предпочтительно всё же параметры
- [ ] Ограничение прав пользователя БД: только нужные операции; снижение ущерба при инъекции
- [ ] Валидация ввода: тип, длина, формат; не полагаться только на неё для защиты от инъекций

### 77. Аудит и соответствие

- [ ] Логирование доступа: кто, когда, какая операция (SELECT/INSERT/...); таблицы аудита или логи СУБД
- [ ] Маскирование данных: сокрытие чувствительных полей в логах и дампах; маскирование в тестовых копиях
- [ ] GDPR-аспекты: право на удаление, переносимость данных; хранение персональных данных, сроки
- [ ] Соответствие отраслевым стандартам: PCI DSS, HIPAA — обзор требований к БД

### 78. Резюме: выбор БД и антипаттерны

- [ ] Сводка по типам: реляционная — структура и целостность; документная — гибкость; ключ–значение — кэш и скорость; граф — связи; векторная — сходство; временные ряды — метрики
- [ ] Полиглот персистентности: комбинация БД в одном проекте под разные задачи
- [ ] Антипаттерны: одна БД «на всё» без обоснования; отказ от реляционной БД ради моды; игнорирование операционной сложности
- [ ] Критерии выбора: модель данных, объём, консистентность, команда, экосистема, лицензии
- [ ] Эволюция: начать с простого (например, PostgreSQL + Redis); добавлять специализированные БД по мере необходимости

### 79. Продолжение: testing, documentation, database-as-code

- [ ] Тестирование БД, фикстуры, testcontainers, performance-tests, ER-диаграммы и миграции данных вынесены в [Часть 24](pact/24_testirovanie_i_dokumentatsiya/index.md)
- [ ] Database-as-Code, GitOps, CI/CD и infrastructure-подход к схемам продолжаются в [Часть 51](pact/51_bd_kak_kod_i_devops/index.md)
- [ ] Это вынесено специально, чтобы базовая operational-часть не перегружалась раньше времени

### 80. Продолжение: observability, advanced monitoring, advanced security

- [ ] Продвинутый мониторинг и symptom -> cause -> action раскрываются в [Часть 39](pact/39_rasshirennyj_monitoring/index.md)
- [ ] Глубокая безопасность, key management, masking и compliance продолжаются в [Часть 28](pact/28_rasshirennaya_bezopasnost/index.md)
- [ ] End-to-end observability, APM и distributed tracing раскрываются в [Часть 55](pact/55_observability_apm_i_treysing/index.md)

---

## Часть XVI. Аналитика и хранилища данных

### 69. OLAP и колоночное хранение

- [ ] OLAP vs OLTP: аналитические запросы (агрегации, сканы) vs транзакционные (точечные чтения/записи)
- [ ] Колоночное хранение: данные по столбцам; сжатие (одинаковые значения в столбце); векторное выполнение
- [ ] Сжатие в колоночных БД: кодирование (dictionary, run-length); тип данных влияет на степень сжатия
- [ ] MPP (Massively Parallel Processing): запрос выполняется на многих узлах параллельно; распределённые агрегации
- [ ] HTAP (Hybrid): OLTP + OLAP в одной системе; TiDB, Oracle, SQL Server; компромиссы

### 70. ClickHouse и колоночные СУБД

- [ ] ClickHouse: MergeTree — движок по умолчанию; ORDER BY (сортировка при вставке); PARTITION BY
- [ ] Primary key в ClickHouse: не уникален; определяет порядок и сегментацию
- [ ] Материализованные представления в ClickHouse: срабатывают при INSERT (агрегация «на лету»)
- [ ] Snowflake: разделение хранения и вычислений; виртуальные склады (warehouses); масштабирование
- [ ] BigQuery: серверный колоночный; оплата за объём запроса; интеграция с GCP
- [ ] Redshift: колоночный; Spectrum для запросов к S3; сравнение с Snowflake
- [ ] DuckDB: встраиваемая аналитическая БД; SQL поверх файлов (Parquet, CSV)

### 71. Хранилище данных: схемы и модели

- [ ] Звёздная схема: центральная таблица фактов + таблицы измерений (dimension); денормализация измерений
- [ ] Снежинка: нормализованные измерения (иерархии в отдельных таблицах)
- [ ] Факты и измерения: факт — события/метрики (объёмы, суммы); измерение — атрибуты (продукт, время, клиент)
- [ ] Slowly Changing Dimension (SCD): тип 1 (перезапись), тип 2 (история версий), тип 3 (предыдущее значение)
- [ ] Surrogate key: искусственный ключ в измерении; независимость от источников
- [ ] Дата-измерение: таблица дат с атрибутами (день недели, месяц, квартал); предрасчёт для JOIN

### 72. ETL, CDC и загрузка в хранилище

- [ ] ETL: Extract, Transform, Load; извлечение из источников, преобразование, загрузка в хранилище
- [ ] ELT: загрузка сырых данных, преобразование в хранилище (на мощностях БД)
- [ ] CDC (Change Data Capture): логирование изменений в источнике; Debezium, Kafka Connect
- [ ] Логическая репликация и декодирование WAL как источник CDC для PostgreSQL
- [ ] Инкрементальная загрузка: по временной метке или ключу; полная перезагрузка vs дельта
- [ ] Data lake: сырые данные в объектном хранилище (S3); Delta Lake, Apache Iceberg — табличные форматы поверх файлов
- [ ] ACID в data lake: Iceberg, Delta — транзакции и версионность на уровне таблицы

---

## Часть XVII. PostgreSQL: детали и расширения

### 81. Расширения PostgreSQL

- [ ] CREATE EXTENSION: установка расширения; pg_available_extensions — список доступных
- [ ] Популярные расширения: pg_stat_statements (статистика запросов), pg_trgm (триграммы), pgcrypto (шифрование)
- [ ] Расширения для партиционирования: pg_partman (автоматическое создание/удаление партиций), pg_pathman
- [ ] Расширения для репликации: pglogical (логическая репликация), bucardo (multi-master)
- [ ] Расширения для мониторинга: pg_stat_monitor (расширенная статистика), pg_wait_sampling
- [ ] Расширения для данных: PostGIS (геопространственные), pgvector (векторные), hstore (ключ–значение)
- [ ] Управление расширениями: ALTER EXTENSION UPDATE; удаление (DROP EXTENSION CASCADE)

### 82. Системные каталоги PostgreSQL

- [ ] pg_class: таблицы, индексы, последовательности; relkind (r=table, i=index, S=sequence)
- [ ] pg_attribute: столбцы таблиц; attnum, attname, atttypid (тип), attnotnull
- [ ] pg_index: индексы; indrelid (таблица), indkey (столбцы), indisunique, indisprimary
- [ ] pg_constraint: ограничения; contype (p=primary, u=unique, f=foreign, c=check), conkey (столбцы)
- [ ] pg_depend: зависимости объектов; удаление с CASCADE
- [ ] Полезные представления: pg_tables, pg_indexes, pg_views, pg_stat_user_tables, pg_stat_user_indexes
- [ ] pg_stat_*: статистика использования; pg_stat_database, pg_stat_bgwriter, pg_stat_archiver

### 83. Конфигурация PostgreSQL

- [ ] postgresql.conf: основные параметры; ALTER SYSTEM SET; pg_reload_conf() для применения без перезапуска
- [ ] Параметры памяти: shared_buffers, work_mem, maintenance_work_mem, effective_cache_size
- [ ] Параметры WAL: wal_level, max_wal_size, min_wal_size, checkpoint_timeout, checkpoint_completion_target
- [ ] Параметры autovacuum: autovacuum_naptime, autovacuum_vacuum_threshold, autovacuum_analyze_threshold
- [ ] Параметры параллелизма: max_parallel_workers, max_parallel_workers_per_gather, parallel_tuple_cost
- [ ] pg_hba.conf: правила доступа; host, user, database, method (md5, scram-sha-256, cert, ldap)
- [ ] Логирование: log_destination, logging_collector, log_min_duration_statement, log_connections

### 84. Расширенные типы PostgreSQL

- [ ] ltree: иерархические данные (пути); операторы (@>, <@, ~); индексы GiST
- [ ] hstore: ключ–значение в столбце; операторы (->, ->>, ?); индексы GIN
- [ ] citext: case-insensitive текст; сравнения без LOWER(); индексы
- [ ] pg_trgm: триграммы для нечёткого поиска; similarity(), %; индексы GIN
- [ ] uuid-ossp: генерация UUID; uuid_generate_v4(), uuid_generate_v1()
- [ ] intarray: операции с массивами целых; пересечение, объединение; индексы GIN

### 85. Расширенные функции PostgreSQL

- [ ] generate_series: генерация последовательностей чисел/дат; для тестовых данных, временных рядов
- [ ] unnest: разворачивание массивов в строки; LATERAL unnest(); для JOIN с массивами
- [ ] array_agg: агрегация в массив; ORDER BY в агрегате; array_agg(DISTINCT ...)
- [ ] jsonb_agg: агрегация в JSON массив; jsonb_build_object для объектов
- [ ] Кастомные агрегаты: CREATE AGGREGATE; state function, final function; для специфичных вычислений
- [ ] Оконные функции: расширенные (percentile_cont, mode, array_agg как окно)

### 86. Расширения для партиционирования

- [ ] pg_partman: автоматическое управление партициями; создание по расписанию; удаление старых партиций
- [ ] pg_pathman: альтернативный менеджер партиций; быстрее для некоторых сценариев
- [ ] Стратегии партиционирования: по времени (месяц, год); по диапазону значений; по хешу
- [ ] Управление партициями: создание новых, отсоединение старых (архивирование); автоматизация через cron

### 87. Расширения для репликации и мониторинга

- [ ] pglogical: логическая репликация с фильтрацией; публикация/подписка; конфликты
- [ ] bucardo: multi-master репликация; разрешение конфликтов; ограничения
- [ ] pg_stat_monitor: расширенная статистика запросов; группировка по приложению, пользователю
- [ ] pg_wait_sampling: профилирование wait events; какие операции ждут

---

## Часть XVIII. MySQL: детали и оптимизация

### 88. Движки хранения MySQL

- [ ] InnoDB: транзакционный движок по умолчанию; ACID; внешние ключи; row-level locking
- [ ] MyISAM: табличные блокировки; без транзакций; быстрее для read-heavy; deprecated
- [ ] Aria (MariaDB): улучшенный MyISAM; crash-safe; для временных таблиц
- [ ] ColumnStore (MariaDB): колоночное хранение; для аналитики; сжатие
- [ ] Memory/HEAP: in-memory таблицы; для временных данных; потеря при перезапуске
- [ ] Выбор движка: InnoDB для большинства случаев; специфичные движки для особых задач

### 89. InnoDB: структура и внутренности

- [ ] Tablespace: файл .ibd; системный tablespace (ibdata1); file-per-table (innodb_file_per_table)
- [ ] Структура: tablespace → segment → extent → page (16 KB); doublewrite buffer
- [ ] Undo tablespace: откат транзакций; MVCC; настройка размера
- [ ] Buffer pool: кэш страниц; innodb_buffer_pool_size (основной параметр); LRU
- [ ] Redo log: ib_logfile0, ib_logfile1; циклическая запись; innodb_log_file_size
- [ ] Doublewrite buffer: защита от partial page write; запись полной страницы перед изменением

### 90. Binlog и репликация MySQL

- [ ] Binlog: бинарный лог изменений; statement-based, row-based, mixed формат
- [ ] GTID: Global Transaction Identifier; уникальный ID транзакции; упрощает репликацию
- [ ] Репликация: master → slave; чтение binlog на master, применение на slave
- [ ] Binary log rotation: автоматическая ротация; expire_logs_days; ручная очистка (PURGE BINARY LOGS)
- [ ] Semi-sync replication: ожидание подтверждения от хотя бы одной реплики; компромисс надёжность/скорость
- [ ] Group replication: multi-master; консенсус; автоматический failover

### 91. Настройки MySQL

- [ ] my.cnf / my.ini: конфигурационный файл; секции [mysqld], [client]
- [ ] Память: innodb_buffer_pool_size (70-80% RAM), innodb_log_file_size, max_connections
- [ ] Query cache: deprecated в MySQL 8.0; кэширование результатов запросов; проблемы с инвалидацией
- [ ] InnoDB настройки: innodb_flush_log_at_trx_commit (1=sync, 2=OS buffer, 0=async)
- [ ] Логирование: slow_query_log, long_query_time; general_log; binary_log
- [ ] Оптимизация: innodb_io_capacity, innodb_read_io_threads, innodb_write_io_threads

### 92. Оптимизация MySQL

- [ ] EXPLAIN: формат (traditional, JSON, TREE); чтение плана выполнения
- [ ] EXPLAIN FORMAT=JSON: детальная информация; cost, rows, filtered
- [ ] Индексы: covering index (все столбцы в индексе); prefix index (первые N символов)
- [ ] Оптимизация JOIN: порядок таблиц; использование индексов; STRAIGHT_JOIN для принудительного порядка
- [ ] Slow query log: логирование медленных запросов; pt-query-digest для анализа
- [ ] Оптимизатор: cost-based; hints (USE INDEX, FORCE INDEX); ограничения оптимизатора

### 93. Репликация MySQL (детали)

- [ ] Master-slave: классическая репликация; один master, несколько slaves
- [ ] Master-master: двунаправленная репликация; конфликты; auto-increment offset
- [ ] GTID репликация: упрощение управления; автоматическое определение позиции
- [ ] Group replication: multi-master через консенсус; автоматический failover; split-brain защита
- [ ] Чтение из реплик: балансировка нагрузки; read-only на репликах; lag мониторинг
- [ ] Failover: автоматический (MHA, Orchestrator); ручной; тестирование процедуры

### 94. Инструменты MySQL

- [ ] mysqldump: логический дамп; --single-transaction для консистентности; --master-data для репликации
- [ ] mysqlbinlog: чтение binlog; восстановление транзакций; фильтрация по времени/позиции
- [ ] Percona Toolkit: pt-query-digest (анализ slow log), pt-online-schema-change (ALTER без блокировки)
- [ ] MySQL Workbench: GUI инструмент; моделирование схемы; администрирование
- [ ] phpMyAdmin, Adminer: веб-интерфейсы; для простого администрирования
- [ ] Monitoring: PMM (Percona Monitoring and Management), MySQL Enterprise Monitor

---

## Часть XIX. Геопространственные данные

### 95. PostGIS: основы

- [ ] Установка: CREATE EXTENSION postgis; версии (PostGIS 2.x, 3.x)
- [ ] Типы: geometry (плоская геометрия), geography (сферическая, на эллипсоиде)
- [ ] SRID: Spatial Reference System Identifier; EPSG коды (4326=WGS84, 3857=Web Mercator)
- [ ] Преобразование координат: ST_Transform(geom, target_srid); перепроецирование
- [ ] Создание геометрий: ST_GeomFromText, ST_MakePoint, ST_MakePolygon; WKT, WKB форматы

### 96. Пространственные типы данных

- [ ] POINT: точка (широта, долгота); ST_MakePoint(x, y); ST_X(), ST_Y()
- [ ] LINESTRING: линия (последовательность точек); маршруты, границы
- [ ] POLYGON: полигон (замкнутая область); многоугольники, зоны
- [ ] MULTIPOINT, MULTILINESTRING, MULTIPOLYGON: коллекции геометрий
- [ ] GEOMETRYCOLLECTION: смешанная коллекция; различные типы геометрий вместе

### 97. Пространственные запросы

- [ ] ST_Distance: расстояние между геометриями; ST_Distance_Sphere для geography
- [ ] ST_Within: одна геометрия внутри другой; ST_Contains (обратное)
- [ ] ST_Intersects: пересечение геометрий; ST_Overlaps (частичное пересечение)
- [ ] ST_Buffer: буфер вокруг геометрии; радиус; для поиска в радиусе
- [ ] ST_Union: объединение геометрий; ST_Intersection (пересечение)
- [ ] ST_Envelope: ограничивающий прямоугольник; для быстрой фильтрации

### 98. Пространственные индексы

- [ ] GiST индекс: для пространственных данных; CREATE INDEX ... USING GIST (geom)
- [ ] SP-GiST: альтернативный индекс; для некоторых типов запросов быстрее
- [ ] Использование индекса: WHERE ST_Intersects(geom, ST_MakeEnvelope(...)); автоматическое использование
- [ ] Оптимизация: ST_Envelope для предварительной фильтрации; затем точная проверка
- [ ] Пространственные агрегаты: ST_Collect, ST_Union для группировки геометрий

---

## Часть XX. Администрирование и тюнинг

### 99. Настройка ОС для БД

- [ ] Huge pages: большие страницы памяти; меньше TLB misses; настройка в ОС и PostgreSQL
- [ ] vm.swappiness: баланс RAM/SWAP; для БД — низкое значение (1-10); избегать swap
- [ ] I/O scheduler: deadline, noop для SSD; cfq для HDD; настройка в Linux
- [ ] Файловая система: XFS предпочтительнее для больших файлов; ext4 тоже хорошо; настройки монтирования (noatime)
- [ ] NUMA: Non-Uniform Memory Access; настройка для БД; numactl для привязки процессов
- [ ] Limits: ulimit для файловых дескрипторов; увеличение для БД (65535+)

### 100. Профилирование производительности

- [ ] pg_stat_statements: статистика запросов; queryid, calls, total_time, mean_time; нормализация запросов
- [ ] pg_stat_monitor: расширенная статистика; группировка по приложению, пользователю, базе
- [ ] Slow query log: логирование медленных запросов; анализ через pt-query-digest (MySQL), pgBadger (PostgreSQL)
- [ ] Профилирование CPU: perf (Linux); профилирование времени выполнения; flame graphs
- [ ] Профилирование памяти: valgrind, tracemalloc (Python); утечки памяти
- [ ] Мониторинг wait events: pg_stat_activity.wait_event_type; какие операции ждут

### 101. Бенчмаркинг

- [ ] pgbench: встроенный бенчмарк PostgreSQL; TPC-B like; настройка масштаба, клиентов, времени
- [ ] sysbench: универсальный бенчмарк; для MySQL, PostgreSQL; различные тесты (CPU, I/O, OLTP)
- [ ] TPC-C: стандартный бенчмарк OLTP; сложная схема; транзакционная нагрузка
- [ ] TPC-H: стандартный бенчмарк OLAP; аналитические запросы; большие объёмы данных
- [ ] Интерпретация результатов: TPS (transactions per second), latency (p50, p95, p99); сравнение конфигураций
- [ ] Нагрузочное тестирование: реалистичная нагрузка; постепенное увеличение; поиск узких мест

### 102. Мониторинг производительности

- [ ] Wait events: pg_stat_activity.wait_event_type; I/O, Lock, LWLock, BufferPin; анализ узких мест
- [ ] Блокировки: pg_locks; blocked и blocking запросы; deadlock detection
- [ ] Temp files: создание временных файлов при нехватке work_mem; мониторинг (pg_stat_database.temp_files)
- [ ] Кэш hit ratio: pg_stat_database.blks_hit / (blks_hit + blks_read); цель > 99%
- [ ] Репликация lag: pg_stat_replication; lag в байтах и секундах; синхронная репликация — ожидание
- [ ] Длительные запросы: pg_stat_activity.query_start, state; идентификация проблемных запросов

### 103. Тюнинг памяти

- [ ] shared_buffers: кэш страниц; рекомендации (25% RAM для PostgreSQL); слишком большой — OOM риск
- [ ] work_mem: память на сортировку и хеш; слишком мало — temp files; слишком много — OOM
- [ ] maintenance_work_mem: память на VACUUM, CREATE INDEX; можно больше чем work_mem
- [ ] effective_cache_size: оценка кэша ОС для планировщика; влияет на выбор плана
- [ ] OOM killer: исчерпание памяти; мониторинг использования; настройка лимитов
- [ ] Баланс параметров: не все параметры памяти можно увеличить одновременно; компромиссы

### 104. Тюнинг I/O

- [ ] random_page_cost: стоимость случайного чтения; для SSD уменьшать (1.1-1.5 вместо 4.0)
- [ ] seq_page_cost: стоимость последовательного чтения; обычно оставлять 1.0
- [ ] effective_io_concurrency: параллельные I/O операции; для SSD увеличивать (200+)
- [ ] Checkpoint настройки: checkpoint_timeout, max_wal_size; баланс между частотой и размером WAL
- [ ] Read-ahead: предзагрузка следующих страниц; настройка в ОС и СУБД
- [ ] Файловая система: noatime для уменьшения записи; настройки монтирования

### 105. Тюнинг параллелизма

- [ ] max_parallel_workers: общее число параллельных воркеров; ограничение ресурсов
- [ ] max_parallel_workers_per_gather: воркеры на один запрос; зависит от сложности запроса
- [ ] parallel_tuple_cost: стоимость передачи данных между процессами; влияет на выбор параллельного плана
- [ ] JIT компиляция: для сложных запросов; jit_above_cost; компиляция выражений и WHERE
- [ ] Параллельные операции: параллельный Seq Scan, Hash Join, Aggregate; Gather узел
- [ ] Ограничения: не все операции параллелизуются; зависимость от данных и запроса

---

## Часть XXI. Разработка и паттерны работы с БД

### 106. Паттерны доступа к данным

- [ ] Repository: абстракция доступа к данным; скрытие деталей БД; тестируемость
- [ ] Unit of Work: отслеживание изменений; коммит всех изменений вместе; транзакционность
- [ ] Active Record: объект = строка таблицы; методы сохранения в объекте; простота, но связь с БД
- [ ] Data Mapper: разделение объекта и БД; mapper преобразует; более гибко
- [ ] Выбор паттерна: зависит от сложности, требований к тестированию, команды

### 107. Паттерны работы с транзакциями

- [ ] Транзакционный скрипт: одна транзакция = один скрипт/метод; простота; для простых операций
- [ ] Доменная модель: бизнес-логика в объектах; транзакции на границах; для сложной логики
- [ ] Управление транзакциями: явное (BEGIN/COMMIT) vs неявное (декораторы, AOP); границы транзакций
- [ ] Транзакции в веб-приложении: один запрос = одна транзакция; длинные транзакции — проблема
- [ ] Распределённые транзакции: 2PC, saga; компромиссы; когда избегать

### 108. Паттерны масштабирования

- [ ] Read replicas: чтение из реплик; разгрузка master; eventual consistency
- [ ] Write-through cache: запись в кэш и БД одновременно; консистентность
- [ ] Write-behind cache: запись в кэш, асинхронная запись в БД; риск потери
- [ ] CQRS: Command Query Responsibility Segregation; отдельные модели для чтения и записи
- [ ] Event sourcing: хранение событий вместо состояния; восстановление состояния из событий
- [ ] Выбор паттерна: зависит от требований к консистентности, сложности, команды

### 109. Антипаттерны разработки

- [ ] N+1 запросы: один запрос + N запросов в цикле; решение: JOIN или batch loading
- [ ] Избыточные запросы: повторяющиеся запросы; кэширование, мемоизация
- [ ] Игнорирование транзакций: авто-коммит везде; потеря атомарности; явные транзакции
- [ ] Отсутствие индексов: медленные запросы; анализ и добавление индексов
- [ ] SELECT *: лишние данные; невозможность index-only scan; явное указание столбцов
- [ ] Длинные транзакции: блокировки, bloat; короткие транзакции; batch processing

### 110. Best practices разработки

- [ ] Подготовленные выражения: защита от SQL-инъекций; кэширование плана; всегда использовать
- [ ] Пулы соединений: ограничение соединений; переиспользование; настройка размера пула
- [ ] Таймауты: connection timeout, query timeout; избежание зависаний; graceful degradation
- [ ] Retry логика: повтор при временных ошибках; exponential backoff; идемпотентность
- [ ] Circuit breaker: отключение при множественных ошибках; защита БД от перегрузки
- [ ] Логирование: логирование запросов (осторожно с данными); метрики; трассировка

### 111. Версионирование данных

- [ ] Оптимистичная блокировка: версия в строке; проверка при UPDATE; конфликт при изменении
- [ ] Пессимистичная блокировка: SELECT FOR UPDATE; блокировка до изменения; deadlock риск
- [ ] Soft delete: deleted_at вместо физического удаления; возможность восстановления; фильтрация
- [ ] Аудит: created_at, updated_at, created_by, updated_by; отслеживание изменений
- [ ] Версионирование записей: хранение истории изменений; temporal tables (SQL:2011)

### 112. Идемпотентность

- [ ] Идемпотентные ключи: уникальный ключ для операции; повторная обработка безопасна
- [ ] Повторная обработка: обработка сообщений/событий; идемпотентность операций
- [ ] Idempotency key в API: клиент передаёт ключ; сервер проверяет; повторный запрос — тот же результат
- [ ] Обработка дублей: дедупликация на уровне БД (UNIQUE constraint) или приложения
- [ ] Транзакции и идемпотентность: откат не делает операцию неидемпотентной; повтор после отката

---

## Часть XXII. Интеграции и инструменты

### 113. CDC инструменты

- [ ] Debezium: Kafka Connect connector; логирование изменений из БД в Kafka; поддержка PostgreSQL, MySQL, MongoDB
- [ ] Maxwell: MySQL binlog → JSON → Kafka; простота; только MySQL
- [ ] Bottled Water: PostgreSQL logical decoding → Avro → Kafka; устаревший
- [ ] Логирование изменений: для интеграций, кэширования, аналитики; поток изменений в реальном времени
- [ ] Схема изменений: формат событий (before/after); обработка DDL; snapshot mode для начальной загрузки

### 114. ETL инструменты

- [ ] Apache Airflow: оркестрация ETL пайплайнов; DAG (Directed Acyclic Graph); Python-based
- [ ] dbt (data build tool): трансформации в SQL; версионирование; тестирование данных
- [ ] Pentaho, Talend: GUI ETL инструменты; визуальное проектирование; enterprise решения
- [ ] Apache NiFi: потоковая обработка данных; визуальный интерфейс; интеграции
- [ ] Выбор инструмента: зависит от сложности, команды, требований к визуализации

### 115. Коннекторы и драйверы

- [ ] JDBC: Java Database Connectivity; стандартный интерфейс; пулы соединений (HikariCP, C3P0)
- [ ] ODBC: Open Database Connectivity; кроссплатформенный; для различных языков
- [ ] Специфичные драйверы: psycopg2, asyncpg (Python); pgx (Go); специфичные возможности
- [ ] Connection string: параметры подключения; sslmode, connect_timeout, application_name
- [ ] Failover в драйвере: multi-host connection string; автоматический failover; load balancing

### 116. Kafka и БД

- [ ] Kafka как persistent log: хранение сообщений; репликация; персистентность
- [ ] Kafka Connect: интеграция БД с Kafka; source connectors (БД → Kafka), sink connectors (Kafka → БД)
- [ ] ksqlDB: SQL поверх Kafka; потоковая обработка; запросы в реальном времени
- [ ] Паттерн outbox: транзакционная гарантия публикации в Kafka; таблица outbox + CDC
- [ ] Exactly-once семантика: идемпотентные продюсеры; транзакции Kafka; компромиссы

### 117. Message queues и БД

- [ ] RabbitMQ: классическая очередь сообщений; персистентность; routing
- [ ] Apache Pulsar: распределённая очередь; персистентность; multi-tenancy
- [ ] Паттерн outbox: гарантия доставки; запись в БД и очередь в одной транзакции; CDC для публикации
- [ ] Транзакционные outbox: таблица outbox в БД; CDC читает и публикует; гарантия доставки
- [ ] Saga и очереди: координация распределённых транзакций через сообщения; компенсирующие транзакции

### 118. GraphQL и БД

- [ ] GraphQL resolvers с БД: запросы к БД в резолверах; N+1 проблема
- [ ] DataLoader паттерн: батчинг и кэширование запросов; решение N+1
- [ ] Prisma: ORM для GraphQL; генерация типов; миграции
- [ ] Hasura: автоматическая GraphQL API поверх PostgreSQL; реальное время (subscriptions)
- [ ] Оптимизация: батчинг запросов; кэширование; ограничение глубины запросов

### 119. REST API и БД

- [ ] Проектирование API: ресурсы, методы HTTP; RESTful принципы
- [ ] Пагинация: offset-based, cursor-based; параметры limit, offset или cursor
- [ ] Фильтрация и сортировка: query параметры; безопасность (SQL injection); валидация
- [ ] Rate limiting: ограничение запросов; защита БД от перегрузки; токены, IP-based
- [ ] API версионирование: URL версионирование (/v1/), header версионирование; обратная совместимость

---

## Часть XXIII. Инфраструктура и облака

### 120. Docker и БД

- [ ] Образы БД: официальные образы (postgres, mysql); версионирование тегов
- [ ] docker-compose: оркестрация контейнеров; сети, volumes; для разработки
- [ ] Volumes для персистентности: named volumes, bind mounts; сохранение данных между перезапусками
- [ ] Окружения: development, testing, production; разные конфигурации
- [ ] Миграции в контейнерах: запуск миграций при старте; init scripts; health checks

### 121. Kubernetes и БД

- [ ] StatefulSets: для stateful приложений (БД); стабильные имена, persistent volumes
- [ ] PersistentVolumes: хранение данных; динамическое выделение; классы storage
- [ ] Операторы: PostgreSQL Operator, MySQL Operator; автоматизация управления; бэкапы, репликация
- [ ] ConfigMaps и Secrets: конфигурация и секреты; отделение от образа
- [ ] Headless Services: для прямого доступа к подам; StatefulSet discovery
- [ ] Ограничения: БД в K8s сложнее; персистентность, производительность, бэкапы

### 122. Managed БД в облаке

- [ ] AWS RDS: PostgreSQL, MySQL, MariaDB, Oracle, SQL Server; автоматические бэкапы, патчинг
- [ ] AWS Aurora: совместимость с MySQL/PostgreSQL; масштабирование; автоматический failover
- [ ] Azure Database: PostgreSQL, MySQL, SQL Server; интеграция с Azure сервисами
- [ ] Google Cloud SQL: PostgreSQL, MySQL, SQL Server; автоматические бэкапы, репликация
- [ ] Преимущества: управление, бэкапы, патчинг, мониторинг; ограничения: меньше контроля, vendor lock-in

### 123. Облачные NoSQL

- [ ] AWS DynamoDB: managed key-value/document; автоматическое масштабирование; pay-per-use
- [ ] AWS DocumentDB: MongoDB совместимый; managed; автоматические бэкапы
- [ ] Azure Cosmos DB: multi-model (document, graph, key-value); глобальное распределение; несколько API
- [ ] Google Firestore: document БД; real-time синхронизация; интеграция с Firebase
- [ ] Сравнение: managed vs self-hosted; стоимость, контроль, vendor lock-in

### 124. Облачные аналитические БД

- [ ] AWS Redshift: колоночное хранилище; масштабирование; интеграция с S3 (Spectrum)
- [ ] Azure Synapse Analytics: аналитика; интеграция с Azure сервисами; serverless опции
- [ ] Google BigQuery: serverless аналитика; оплата за объём запроса; интеграция с GCP
- [ ] Snowflake: multi-cloud; разделение storage и compute; масштабирование независимо
- [ ] Serverless аналитика: оплата за использование; автоматическое масштабирование; простота

### 125. Backup и restore в облаке

- [ ] Автоматические бэкапы: scheduled backups; retention policies; управление жизненным циклом
- [ ] Point-in-time recovery: восстановление до момента; непрерывное логирование изменений
- [ ] Cross-region репликация: репликация между регионами; disaster recovery; задержка
- [ ] Snapshot: моментальные снимки; быстрое восстановление; хранение в объектном хранилище
- [ ] Экспорт/импорт: экспорт в S3/Azure Blob/GCS; импорт из облачного хранилища

### 126. Multi-cloud стратегии

- [ ] Репликация между облаками: данные в нескольких облаках; отказоустойчивость
- [ ] Disaster recovery: план восстановления; тестирование; RTO, RPO
- [ ] Vendor lock-in: зависимость от провайдера; стратегии снижения (стандарты, портабельность)
- [ ] Гибридные решения: часть в облаке, часть on-premise; сложность управления
- [ ] Стоимость: сравнение провайдеров; оптимизация расходов; резервирование

---

## Часть XXIV. Тестирование и документация

### 127. Unit тесты БД

- [ ] Мокирование БД: mock объекты для репозиториев; изоляция от БД; быстрые тесты
- [ ] Тестирование репозиториев: in-memory БД (H2, SQLite); тестирование SQL логики
- [ ] Изоляция тестов: каждый тест в своей транзакции; rollback после теста; чистые данные
- [ ] Фикстуры: предопределённые данные; загрузка перед тестами; очистка после
- [ ] Тестирование миграций: применение и откат миграций; проверка схемы

### 128. Integration тесты

- [ ] testcontainers: Docker контейнеры для тестов; реальная БД в тестах; изоляция
- [ ] Фикстуры данных: загрузка тестовых данных; реалистичные данные; генерация (Faker)
- [ ] Транзакционный rollback: каждый тест в транзакции; автоматический rollback; чистые данные
- [ ] Параллельные тесты: изоляция между тестами; разные схемы/базы; порядок выполнения
- [ ] Тестирование производительности: измерение времени запросов; выявление регрессий

### 129. Performance тесты

- [ ] Нагрузочное тестирование: симуляция нагрузки; инструменты (JMeter, Gatling, k6)
- [ ] Профилирование медленных запросов: идентификация узких мест; оптимизация
- [ ] Тестирование под нагрузкой: длительная нагрузка; стабильность; утечки памяти
- [ ] Бенчмарки: сравнение производительности; до и после изменений; метрики
- [ ] Continuous performance testing: автоматические тесты производительности; CI/CD интеграция

### 130. ER диаграммы

- [ ] Инструменты: dbdiagram.io (DSL), pgAdmin (визуальный), MySQL Workbench, DBeaver, ER/Studio
- [ ] Нотация: Crow's Foot (популярная), IDEF1X, UML; выбор нотации
- [ ] Создание диаграмм: из существующей схемы (reverse engineering); проектирование новой схемы
- [ ] Версионирование: диаграммы в Git; изменения схемы; документация эволюции
- [ ] Автоматизация: генерация диаграмм из схемы; обновление при изменении схемы

### 131. Документация схемы

- [ ] COMMENT ON: комментарии к таблицам, столбцам; документация в БД
- [ ] Генерация документации: инструменты (SchemaSpy, DataGrip); HTML/PDF документация
- [ ] Версионирование схемы: миграции как документация; история изменений
- [ ] Метаданные: описание назначения таблиц; примеры данных; бизнес-правила
- [ ] Живая документация: автоматическая генерация; синхронизация с кодом

### 132. Миграции данных

- [ ] Перенос между БД: pg_dump → restore; mysqldump → import; конвертация форматов
- [ ] Конвертация схем: различия между СУБД; типы данных; ограничения
- [ ] ETL для миграции: извлечение, трансформация, загрузка; валидация данных
- [ ] Стратегии миграции: big bang vs incremental; downtime; тестирование
- [ ] Валидация: проверка целостности; сравнение данных; регрессионное тестирование

---

## Часть XXV. Катастрофоустойчивость и DR

### 133. Disaster Recovery планы

- [ ] RTO (Recovery Time Objective): целевое время восстановления; максимально допустимый downtime
- [ ] RPO (Recovery Point Objective): целевая точка восстановления; максимальная потеря данных
- [ ] Стратегии восстановления: hot standby (минимальный RTO), cold standby (экономия), warm standby
- [ ] Документация DR плана: процедуры восстановления; контакты; тестирование плана
- [ ] Регулярное тестирование: проверка процедур; выявление проблем; обновление плана

### 134. Multi-region репликация

- [ ] Синхронная между регионами: строгая консистентность; высокая задержка; ограниченная доступность
- [ ] Асинхронная между регионами: меньшая задержка; eventual consistency; риск потери данных
- [ ] Задержка: географическое расстояние; компромисс консистентность/задержка
- [ ] Выбор primary региона: ближе к пользователям; автоматический failover; ручное переключение
- [ ] Региональные требования: GDPR (данные в регионе); compliance; юридические ограничения

### 135. Failover стратегии

- [ ] Автоматический failover: Patroni (PostgreSQL), Stolon; автоматическое переключение при сбое
- [ ] Ручной failover: контроль над процессом; проверка перед переключением; меньше рисков
- [ ] Тестирование failover: регулярное тестирование; проверка процедур; обучение команды
- [ ] Split-brain защита: предотвращение двух primary; кворум; fencing
- [ ] Время восстановления: мониторинг времени failover; оптимизация процедур

### 136. Backup стратегии

- [ ] Полный бэкап: полная копия данных; основа восстановления; долго, много места
- [ ] Инкрементальный: только изменения; быстрее; требует полного для восстановления
- [ ] Дифференциальный: изменения с последнего полного; компромисс между полным и инкрементальным
- [ ] Хранение бэкапов: локально, S3/Azure Blob/GCS, архив (Glacier); lifecycle policies
- [ ] Retention: политики хранения; соответствие требованиям; автоматическое удаление старых

### 137. Тестирование восстановления

- [ ] Регулярное тестирование: проверка восстановления; выявление проблем; обновление процедур
- [ ] Проверка целостности: валидация данных после restore; сравнение с оригиналом
- [ ] Время восстановления: измерение RTO; оптимизация процедур; документация
- [ ] Автоматизация: автоматическое тестирование восстановления; CI/CD интеграция
- [ ] Документация результатов: отчёты о тестировании; улучшения; обучение команды

### 138. Географическое распределение

- [ ] CockroachDB multi-region: автоматическое распределение; глобальная консистентность; низкая задержка
- [ ] Spanner global: TrueTime для глобальной консистентности; автоматическое распределение
- [ ] Репликация между дата-центрами: синхронная/асинхронная; выбор стратегии
- [ ] Локальность данных: данные ближе к пользователям; снижение задержки; compliance
- [ ] Стоимость: межрегиональный трафик; репликация; компромиссы

---

## Часть XXVI. SQL функции и операторы: полный справочник

### 139. Строковые функции

- [ ] CONCAT: объединение строк; CONCAT(str1, str2, ...); NULL обрабатывается как пустая строка
- [ ] SUBSTRING: извлечение подстроки; SUBSTRING(str FROM start FOR length); индексация с 1
- [ ] TRIM: удаление пробелов; TRIM([LEADING|TRAILING|BOTH] [chars] FROM str); LTRIM, RTRIM
- [ ] LOWER, UPPER: преобразование регистра; для сравнения без учета регистра
- [ ] LENGTH, CHAR_LENGTH: длина строки; LENGTH в байтах, CHAR_LENGTH в символах (UTF-8)
- [ ] POSITION, STRPOS: позиция подстроки; POSITION(substr IN str); возвращает 0 если не найдено
- [ ] REPLACE: замена подстроки; REPLACE(str, old, new); все вхождения
- [ ] SPLIT_PART: разбиение строки; SPLIT_PART(str, delimiter, field_num); для парсинга
- [ ] REGEXP_REPLACE: замена по регулярному выражению; REGEXP_REPLACE(str, pattern, replacement, flags)
- [ ] REGEXP_MATCH: поиск по регулярному выражению; возвращает массив совпадений
- [ ] LPAD, RPAD: дополнение строки; LPAD(str, length, pad); выравнивание

### 140. Числовые функции

- [ ] ABS: абсолютное значение; ABS(-5) = 5
- [ ] ROUND: округление; ROUND(num, digits); банковское округление для .5
- [ ] FLOOR, CEIL: округление вниз/вверх; FLOOR(3.7) = 3, CEIL(3.2) = 4
- [ ] MOD: остаток от деления; MOD(a, b) = a % b
- [ ] POWER, SQRT: степень и квадратный корень; POWER(2, 3) = 8, SQRT(16) = 4
- [ ] RANDOM: случайное число; RANDOM() в [0, 1); для выборки случайных строк
- [ ] GREATEST, LEAST: максимум/минимум из списка; GREATEST(a, b, c); работает и со строками
- [ ] SIGN: знак числа; SIGN(-5) = -1, SIGN(0) = 0, SIGN(5) = 1
- [ ] TRUNC: усечение; TRUNC(num, digits); отбрасывание дробной части

### 141. Функции даты и времени

- [ ] NOW, CURRENT_TIMESTAMP: текущее время; с таймзоной; точность (микросекунды)
- [ ] CURRENT_DATE, CURRENT_TIME: текущая дата и время отдельно; без таймзоны для TIME
- [ ] EXTRACT: извлечение части даты; EXTRACT(YEAR FROM date), EXTRACT(EPOCH FROM timestamp)
- [ ] DATE_TRUNC: округление до единицы времени; DATE_TRUNC('month', date); для группировки
- [ ] AGE: разница между датами; AGE(timestamp1, timestamp2); возвращает INTERVAL
- [ ] INTERVAL арифметика: timestamp + INTERVAL '1 day'; INTERVAL '1 month'; сложение/вычитание
- [ ] AT TIME ZONE: преобразование таймзоны; timestamp AT TIME ZONE 'UTC'; работа с таймзонами
- [ ] TO_TIMESTAMP, TO_DATE: преобразование строки в дату/время; форматирование; локализация

### 142. Условные функции

- [ ] CASE простой: CASE expr WHEN val1 THEN res1 WHEN val2 THEN res2 ELSE default END
- [ ] CASE поисковый: CASE WHEN condition1 THEN res1 WHEN condition2 THEN res2 ELSE default END
- [ ] COALESCE: первое не-NULL значение; COALESCE(a, b, c); для значений по умолчанию
- [ ] NULLIF: NULL если равны; NULLIF(a, b) эквивалентно CASE WHEN a = b THEN NULL ELSE a END
- [ ] GREATEST, LEAST: максимум/минимум с учётом NULL; NULL игнорируется или делает результат NULL
- [ ] IF (MySQL): IF(condition, true_value, false_value); простая альтернатива CASE
- [ ] IIF (SQL Server): IIF(condition, true_value, false_value); аналогично IF

### 143. Преобразование типов

- [ ] CAST: стандартное преобразование; CAST(expr AS type); CAST('123' AS INTEGER)
- [ ] :: (PostgreSQL): краткая форма; '123'::INTEGER; удобнее для простых случаев
- [ ] CONVERT (SQL Server): CONVERT(type, expr, style); стили для дат
- [ ] Типы преобразований: явное vs неявное; безопасное преобразование; ошибки при несовместимости
- [ ] TO_CHAR, TO_NUMBER, TO_DATE: преобразование в строку/число/дату; форматирование
- [ ] Опасные преобразования: потеря точности; переполнение; неявные преобразования

### 144. Системные функции

- [ ] VERSION: версия СУБД; VERSION(); детальная информация о версии
- [ ] CURRENT_USER, SESSION_USER: текущий пользователь; различие между ними
- [ ] DATABASE(), SCHEMA(): текущая база данных/схема; для динамических запросов
- [ ] pg_size_pretty: форматирование размера; pg_size_pretty(1024) = '1 kB'; читаемый формат
- [ ] pg_database_size, pg_relation_size: размер БД/таблицы; pg_total_relation_size (с индексами)
- [ ] pg_backend_pid: PID процесса; для идентификации соединения
- [ ] current_setting: получение параметра конфигурации; current_setting('work_mem')

### 145. Операторы SQL

- [ ] Арифметические: +, -, *, /, % (modulo); приоритет операций; деление на ноль
- [ ] Сравнения: =, <>, !=, <, >, <=, >=; с NULL даёт UNKNOWN; IS NULL, IS NOT NULL
- [ ] Логические: AND, OR, NOT; приоритет (NOT > AND > OR); короткое замыкание
- [ ] Строковые: || (конкатенация), LIKE (с %, _), ILIKE (case-insensitive), SIMILAR TO, ~ (regexp)
- [ ] Массивы: && (пересечение), @> (содержит), <@ (содержится в), [] (индекс)
- [ ] JSON: ->, ->>, @>, ?, ?&, ?|, #>, #>>; операторы для работы с JSON
- [ ] Диапазоны: && (пересечение), @> (содержит), <@ (содержится в), - (разность), + (объединение)

---

## Часть XXVII. Troubleshooting и диагностика

### 146. Диагностика медленных запросов

- [ ] Идентификация проблемных запросов: pg_stat_statements по total_time; slow query log; pg_stat_activity
- [ ] Анализ планов: EXPLAIN ANALYZE; чтение cost, rows, actual time; поиск узких мест
- [ ] Профилирование: pg_stat_statements детали; нормализация запросов; анализ паттернов
- [ ] Инструменты: pgBadger (анализ логов), pg_stat_monitor; pt-query-digest (MySQL)
- [ ] Типичные проблемы: отсутствие индексов; неоптимальные планы; блокировки; недостаток памяти
- [ ] Решения: добавление индексов; переписывание запросов; настройка параметров; увеличение ресурсов

### 147. Диагностика блокировок

- [ ] pg_locks анализ: blocked и blocking запросы; типы блокировок; ожидание
- [ ] Deadlock detection: автоматическое обнаружение; откат одной транзакции; логирование
- [ ] Блокирующие запросы: идентификация; pg_blocking_pids(); анализ причин блокировки
- [ ] Kill блокирующих: pg_terminate_backend(); pg_cancel_backend(); осторожность
- [ ] Предотвращение: короткие транзакции; правильный порядок блокировок; таймауты
- [ ] Мониторинг: pg_stat_activity с wait_event_type; алерты на длительные блокировки

### 148. Диагностика репликации

- [ ] Lag анализ: pg_stat_replication; lag в байтах и секундах; причины отставания
- [ ] Причины отставания: медленная сеть; медленный диск на реплике; большие транзакции; конфликты
- [ ] Синхронная репликация: ожидание применения на реплике; влияние на производительность; таймауты
- [ ] Слоты репликации: накопление WAL при отстающей реплике; max_slot_wal_keep_size; мониторинг
- [ ] Решение проблем: оптимизация сети; оптимизация реплики; настройка синхронной репликации
- [ ] Логическая репликация: конфликты; разрешение конфликтов; мониторинг подписок

### 149. Диагностика памяти

- [ ] OOM причины: исчерпание памяти; анализ использования; shared_buffers, work_mem, temp files
- [ ] Использование shared_buffers: мониторинг hit ratio; влияние на производительность; настройка размера
- [ ] Temp files: создание при нехватке work_mem; pg_stat_database.temp_files; решение — увеличение work_mem
- [ ] Memory leaks: утечки памяти в расширениях; профилирование; valgrind, tracemalloc
- [ ] Мониторинг: pg_stat_database; использование памяти процессами; системные метрики
- [ ] Решения: оптимизация запросов; увеличение памяти; настройка параметров; ограничение параллелизма

### 150. Диагностика I/O

- [ ] Медленный диск: анализ wait events (I/O); очередь I/O; использование диска
- [ ] Очередь I/O: мониторинг глубины очереди; влияние на задержку; оптимизация
- [ ] Wait events: анализ pg_stat_activity.wait_event_type; I/O wait events; оптимизация
- [ ] Оптимизация I/O: random_page_cost для SSD; effective_io_concurrency; read-ahead
- [ ] Файловая система: настройки монтирования (noatime); выбор ФС (XFS, ext4); оптимизация
- [ ] RAID: влияние на производительность; выбор уровня RAID; SSD vs HDD

### 151. Диагностика bloat

- [ ] Раздувание таблиц: pg_stat_user_tables.n_dead_tup; причины (UPDATE, DELETE); влияние на производительность
- [ ] Раздувание индексов: pg_stat_user_indexes; причины; влияние на размер и производительность
- [ ] pg_stat_user_tables: анализ bloat; отношение dead_tup к live_tup; пороги для VACUUM
- [ ] VACUUM анализ: необходимость VACUUM; влияние autovacuum; ручной VACUUM
- [ ] Решение: настройка autovacuum; ручной VACUUM; VACUUM FULL (осторожно); оптимизация запросов
- [ ] Мониторинг: регулярная проверка bloat; алерты; автоматизация VACUUM

### 152. Логи и диагностика

- [ ] Анализ логов PostgreSQL: postgresql.log; уровни логирования; фильтрация по уровню
- [ ] Анализ логов MySQL: error log, slow query log, general log; ротация логов
- [ ] Error codes: коды ошибок СУБД; классификация ошибок; обработка в приложении
- [ ] Stack traces: трассировка стека при ошибках; отладка; символическая информация
- [ ] Диагностические запросы: проверка состояния; анализ проблем; системные представления
- [ ] Инструменты: pgBadger (анализ логов PostgreSQL); pt-query-digest (MySQL); централизованное логирование

---

## Часть XXVIII. Расширенные темы безопасности

### 153. Типы SQL-инъекций

- [ ] Классическая SQL-инъекция: подстановка в запрос; UNION-based; примеры атак
- [ ] Blind SQL injection: слепая инъекция; определение результата по времени/ошибкам; time-based
- [ ] Time-based injection: SLEEP(), BENCHMARK(); определение данных по времени ответа
- [ ] Second-order injection: инъекция через сохранённые данные; опасность при выводе
- [ ] Union-based injection: использование UNION; определение структуры таблиц; извлечение данных
- [ ] Error-based injection: использование ошибок для извлечения данных; информативные ошибки
- [ ] Защита: подготовленные выражения; валидация; принцип наименьших привилегий

### 154. Защита от инъекций

- [ ] Подготовленные выражения: параметризованные запросы; все языки программирования; защита
- [ ] Параметризованные запросы: использование параметров вместо конкатенации; безопасность
- [ ] Валидация: проверка входных данных; тип, длина, формат; не полагаться только на валидацию
- [ ] Allowlist: белый список допустимых значений; для ограниченных наборов значений
- [ ] Экранирование: когда подготовленные выражения недоступны; осторожность; предпочтительно параметры
- [ ] Ограничение прав: минимальные привилегии пользователя БД; снижение ущерба при инъекции

### 155. Атаки на БД

- [ ] SQL injection: классическая атака; защита подготовленными выражениями
- [ ] NoSQL injection: инъекция в MongoDB, Elasticsearch; $where, выражения; защита
- [ ] Command injection: выполнение команд через функции БД; COPY FROM PROGRAM; ограничения
- [ ] DoS атаки: перегрузка БД запросами; rate limiting; connection limits
- [ ] Brute force: подбор паролей; защита блокировкой; сложные пароли
- [ ] Защита: многоуровневая защита; мониторинг; алерты на подозрительную активность

### 156. Шифрование данных

- [ ] Column-level encryption: шифрование отдельных столбцов; application-level; ключи
- [ ] Application-level encryption: шифрование в приложении; контроль над ключами; производительность
- [ ] TDE (Transparent Data Encryption): прозрачное шифрование; на уровне табличных пространств; производительность
- [ ] Шифрование в PostgreSQL: pgcrypto расширение; функции encrypt/decrypt; хранение ключей
- [ ] Шифрование в MySQL: encryption functions; TDE в Enterprise версии
- [ ] Компромиссы: производительность; сложность управления ключами; выбор стратегии

### 157. Управление ключами

- [ ] KMS (Key Management Service): централизованное управление ключами; AWS KMS, Azure Key Vault, HashiCorp Vault
- [ ] Ротация ключей: регулярная смена ключей; процедуры ротации; влияние на шифрованные данные
- [ ] Безопасное хранение ключей: не в коде; переменные окружения; секрет-менеджеры
- [ ] Разделение ключей: разные ключи для разных данных; изоляция; снижение риска
- [ ] Аудит доступа к ключам: логирование использования ключей; мониторинг; алерты

### 158. Аудит и compliance

- [ ] Детальное логирование: кто, когда, что; pgaudit расширение; настройка аудита
- [ ] pgaudit конфигурация: что логировать (READ, WRITE, DDL); фильтрация; производительность
- [ ] GDPR соответствие: право на удаление; право на портативность; минимизация данных; сроки хранения
- [ ] PCI DSS: требования к хранению карточных данных; шифрование; аудит доступа
- [ ] HIPAA: требования к медицинским данным; шифрование; контроль доступа; аудит
- [ ] SOX: требования к финансовым данным; контроль изменений; аудит транзакций

### 159. Маскирование данных

- [ ] PII (Personally Identifiable Information): идентификация чувствительных данных; классификация
- [ ] Маскирование в тестовых окружениях: сокрытие реальных данных; генерация тестовых данных; Faker
- [ ] Динамическое маскирование: маскирование при запросе; политики маскирования; прозрачность
- [ ] Методы маскирования: частичное скрытие (***1234); хеширование; генерация похожих данных
- [ ] Сохранение формата: маскирование с сохранением формата; для тестирования; валидация

---

## Часть XXIX. Системные представления и метаданные

### 160. information_schema

- [ ] Стандартные представления: tables, columns, key_column_usage, table_constraints; переносимость
- [ ] tables: список таблиц; table_schema, table_name, table_type; фильтрация по схеме
- [ ] columns: список столбцов; column_name, data_type, is_nullable, column_default; порядок
- [ ] key_column_usage: использование столбцов в ключах; primary keys, foreign keys
- [ ] table_constraints: ограничения таблиц; constraint_type, constraint_name; primary, foreign, unique, check
- [ ] Использование: получение метаданных схемы; динамические запросы; документация

### 161. pg_catalog (PostgreSQL)

- [ ] Системные каталоги: низкоуровневые таблицы; структура БД; для администраторов
- [ ] pg_class: таблицы, индексы, последовательности; relkind (r=table, i=index, S=sequence); relname, relnamespace
- [ ] pg_attribute: столбцы таблиц; attrelid (таблица), attname, atttypid (тип), attnotnull, attnum
- [ ] pg_index: индексы; indrelid (таблица), indkey (столбцы), indisunique, indisprimary, indisexclusion
- [ ] pg_constraint: ограничения; contype (p=primary, u=unique, f=foreign, c=check), conkey (столбцы), confkey (FK столбцы)
- [ ] pg_depend: зависимости объектов; удаление с CASCADE; отслеживание зависимостей

### 162. INFORMATION_SCHEMA (MySQL)

- [ ] Таблицы: TABLES, COLUMNS, KEY_COLUMN_USAGE, TABLE_CONSTRAINTS; совместимость со стандартом
- [ ] Статистика: TABLE_STATISTICS, INDEX_STATISTICS; использование индексов; оптимизация
- [ ] Привилегии: USER_PRIVILEGES, SCHEMA_PRIVILEGES, TABLE_PRIVILEGES; управление доступом
- [ ] Процессы: PROCESSLIST; активные соединения; анализ запросов
- [ ] Использование: получение метаданных; динамические запросы; администрирование

### 163. Метаданные схемы

- [ ] Получение списка таблиц: SELECT FROM information_schema.tables; фильтрация по схеме
- [ ] Получение столбцов: SELECT FROM information_schema.columns; типы данных; ограничения
- [ ] Получение индексов: SELECT FROM pg_indexes (PostgreSQL); анализ использования
- [ ] Получение ограничений: SELECT FROM information_schema.table_constraints; типы ограничений
- [ ] Типы данных: mapping типов СУБД на стандартные; различия между СУБД
- [ ] Автоматизация: генерация кода из схемы; валидация схемы; документация

### 164. Статистика использования

- [ ] pg_stat_user_tables: статистика таблиц; n_tup_ins, n_tup_upd, n_tup_del, n_live_tup, n_dead_tup
- [ ] pg_stat_user_indexes: статистика индексов; idx_scan (использование), idx_tup_read, idx_tup_fetch
- [ ] Анализ использования: какие таблицы/индексы используются; неиспользуемые объекты; оптимизация
- [ ] pg_stat_statements: статистика запросов; queryid, calls, total_time, mean_time; нормализация
- [ ] Мониторинг: регулярный анализ статистики; выявление проблем; оптимизация

### 165. Размеры объектов

- [ ] pg_size_pretty: форматирование размера; читаемый формат (kB, MB, GB); удобство
- [ ] pg_total_relation_size: полный размер (таблица + индексы + TOAST); для оценки места
- [ ] pg_table_size: размер таблицы (без индексов); pg_indexes_size — размер индексов
- [ ] pg_database_size: размер базы данных; все таблицы и индексы
- [ ] Мониторинг роста: отслеживание изменения размеров; прогнозирование; capacity planning
- [ ] Анализ: выявление больших таблиц/индексов; оптимизация; очистка

### 166. Версионирование схемы

- [ ] Отслеживание изменений: миграции как история; версионирование DDL; контроль изменений
- [ ] Сравнение схем: инструменты сравнения; diff схем; выявление различий
- [ ] Миграции как история: эволюция схемы; документация изменений; откат
- [ ] Автоматизация: генерация миграций из изменений; валидация миграций; тестирование

---

## Часть XXX. Расширенные темы NoSQL

### 167. MongoDB детали

- [ ] Aggregation pipeline: $match (фильтр), $group (группировка), $project (проекция), $lookup (JOIN), $unwind (разворачивание массива), $sort, $limit, $facet (несколько пайплайнов)
- [ ] Change streams: подписка на изменения; для кэширования, интеграций; фильтрация изменений
- [ ] Transactions: multi-document transactions; снимок на начало; ограничения; использование
- [ ] Индексы: single, compound, multikey (массивы), text, geospatial, hashed, TTL; использование
- [ ] Read concern: local, available, majority, linearizable, snapshot; выбор уровня
- [ ] Write concern: w (число подтверждений), j (journal), wtimeout; гарантии записи

### 168. Redis детали

- [ ] Все структуры данных: strings (GET/SET), lists (LPUSH/RPOP — очереди), sets (SADD/SINTER), hashes (HGET/HSET), sorted sets (ZADD/ZRANGE), streams (consumer groups), bitmaps, hyperloglog (приблизительный подсчёт уникальных)
- [ ] Lua scripting: атомарные скрипты; EVAL, EVALSHA; ограничения (время, память); использование
- [ ] Pub/Sub: PUBLISH/SUBSCRIBE; нет персистентности; для уведомлений; паттерны
- [ ] Redis Modules: расширения функциональности; RediSearch, RedisGraph, RedisTimeSeries; установка
- [ ] Транзакции: MULTI/EXEC; атомарность набора команд; WATCH — оптимистичная блокировка
- [ ] Pipeline: batch команд без round-trip; уменьшение задержки; атомарность не гарантируется

### 169. Cassandra детали

- [ ] CQL: CREATE TABLE, INSERT, SELECT, UPDATE, DELETE; синтаксис; ограничения
- [ ] Materialized views: предвычисленные представления; для запросов по другим ключам; обновление
- [ ] Secondary indexes: локальные индексы; ограничения; когда использовать; SASI индексы
- [ ] Lightweight transactions: compare-and-set; IF условия; консистентность; производительность
- [ ] Batch: logged batch (гарантия атомарности), unlogged batch (быстрее); ограничения
- [ ] Consistency levels: ONE, TWO, THREE, QUORUM, ALL, LOCAL_QUORUM; выбор уровня

### 170. Elasticsearch детали

- [ ] Mapping: dynamic mapping (автоматическое), explicit mapping (ручное); типы полей; nested объекты
- [ ] Analyzers: standard, keyword, custom; tokenizers, token filters; для полнотекстового поиска
- [ ] Query DSL: bool (AND/OR/NOT), match (full-text), term (точное), range, nested (вложенные объекты)
- [ ] Aggregations: metric (avg, sum, min, max), bucket (terms, date_histogram), pipeline (derivative)
- [ ] Relevance: BM25 алгоритм; boosting; function_score; настройка релевантности
- [ ] ILM (Index Lifecycle Management): hot, warm, cold, delete; автоматическое управление индексами

### 171. Neo4j детали

- [ ] Cypher: MATCH (поиск), WHERE (фильтр), RETURN (проекция), CREATE (создание), MERGE (upsert), DELETE, SET, REMOVE
- [ ] Переменная длина пути: MATCH (a)-[*1..5]->(b); кратчайший путь; обход графа
- [ ] Shortest path: алгоритм кратчайшего пути; SHORTEST PATH; использование
- [ ] APOC процедуры: библиотека процедур; обход графа; алгоритмы; утилиты
- [ ] Индексы: single property, composite, full-text; использование в запросах
- [ ] Constraints: unique, existence; обеспечение целостности

### 172. InfluxDB детали

- [ ] Flux язык: функциональный язык запросов; pipe оператор; трансформации данных
- [ ] Retention policies: политики хранения; автоматическое удаление старых данных; downsampling
- [ ] Continuous queries: предвычисленные агрегаты; автоматическое выполнение; экономия места
- [ ] Downsampling: агрегация по времени; хранение агрегатов вместо сырых данных; компромиссы
- [ ] Tags vs fields: tags (индексируются, для фильтрации), fields (значения, для агрегации); выбор
- [ ] Series: уникальная комбинация measurement + tags; кардинальность; влияние на производительность

### 173. DynamoDB

- [ ] Таблицы, items, attributes: структура данных; partition key и sort key; типы атрибутов
- [ ] Partition key и sort key: составной первичный ключ; распределение данных; запросы
- [ ] GSI и LSI: Global Secondary Index, Local Secondary Index; альтернативные ключи запросов
- [ ] Streams: поток изменений; для интеграций; обработка событий
- [ ] TTL: Time To Live; автоматическое удаление; использование для временных данных
- [ ] On-demand vs provisioned: оплата за использование vs резервирование capacity; выбор модели

---

## Часть XXXI. Расширенные темы векторных БД

### 174. pgvector детали

- [ ] Типы vector(n): размерность вектора; ограничения; хранение; индексы
- [ ] Операторы: <-> (L2 расстояние), <#> (отрицательное скалярное произведение), <=> (косинусное расстояние)
- [ ] Индексы ivfflat: Inverted File Index; параметры (lists, probes); точность vs скорость
- [ ] Индексы hnsw: Hierarchical Navigable Small World; параметры (m, ef_construction, ef_search); высокая точность
- [ ] Параметры индексов: настройка для баланса точность/скорость; влияние на память
- [ ] Использование: поиск ближайших соседей; фильтрация по метаданным; гибридный поиск

### 175. Pinecone детали

- [ ] Managed векторная БД: полностью управляемая; простота использования; масштабирование
- [ ] API: REST API; Python SDK; операции (upsert, query, delete); простота
- [ ] Namespaces: изоляция данных; организация данных; мультитенантность
- [ ] Metadata filtering: фильтрация по метаданным; до или после векторного поиска; гибридный поиск
- [ ] Hybrid search: векторный + ключевой поиск; комбинирование результатов; RRF (Reciprocal Rank Fusion)
- [ ] Масштабирование: автоматическое масштабирование; управление индексами; производительность

### 176. Weaviate детали

- [ ] Схема: classes (таблицы), properties (столбцы); типы свойств; модули
- [ ] Модули: text2vec (текст), img2vec (изображения); векторизация; интеграция
- [ ] GraphQL API: запросы через GraphQL; фильтрация; агрегации; гибкость
- [ ] Batch operations: массовая вставка; эффективность; ограничения
- [ ] Гибридный поиск: векторный + BM25; комбинирование; настройка весов
- [ ] Версионирование: версии схемы; миграции; совместимость

### 177. Milvus детали

- [ ] Collections: коллекции векторов; схема; создание и управление
- [ ] Partitions: разделение коллекций; логическая организация; фильтрация
- [ ] Segments: физическое хранение; сегментация данных; оптимизация
- [ ] Индексы: FLAT (точный), IVF_FLAT, IVF_SQ8 (квантизация), HNSW; выбор индекса
- [ ] Load и release: загрузка коллекций в память; release для освобождения; управление памятью
- [ ] Масштабирование: горизонтальное масштабирование; распределённое хранение; производительность

### 178. Qdrant детали

- [ ] Collections: коллекции векторов; создание; настройка; удаление
- [ ] Points: точки (векторы + payload); вставка; обновление; удаление
- [ ] Payload (metadata): метаданные точек; фильтрация; индексация payload
- [ ] Фильтры: фильтрация по payload; до или после векторного поиска; комбинирование условий
- [ ] Sparse vectors: разреженные векторы; эффективное хранение; использование
- [ ] Sharding: шардирование коллекций; распределённое хранение; масштабирование

### 179. Оптимизация векторного поиска

- [ ] Выбор метрики: L2, косинус, dot product; влияние на результаты; нормализация
- [ ] Настройка индексов: ef_construction, m для HNSW; lists, probes для IVF; баланс точность/скорость
- [ ] Квантизация: скалярная (SQ), product (PQ); сжатие векторов; экономия памяти; потеря точности
- [ ] Фильтрация: pre-filter vs post-filter; влияние на производительность; выбор стратегии
- [ ] Гибридный поиск: комбинирование векторного и ключевого поиска; веса; RRF; оптимизация

---

## Часть XXXII. Расширенные темы партиционирования

### 180. Стратегии партиционирования

- [ ] По времени: месяц, год, неделя; для временных рядов; автоматическое удаление старых
- [ ] По диапазону значений: RANGE partitioning; для упорядоченных данных; границы диапазонов
- [ ] По списку: LIST partitioning; для категорий; явное указание значений
- [ ] По хешу: HASH partitioning; равномерное распределение; для балансировки нагрузки
- [ ] Composite: комбинирование стратегий; например, сначала по диапазону, потом по хешу
- [ ] Выбор стратегии: зависит от паттернов запросов; распределение данных; требования

### 181. Управление партициями

- [ ] Автоматическое создание: pg_partman расширение; создание по расписанию; настройка
- [ ] Удаление старых: retention policies; автоматическое удаление; архивирование перед удалением
- [ ] Архивирование: отсоединение партиций; сжатие; перемещение в холодное хранилище
- [ ] Split: разделение партиции; для ребалансировки; изменение границ
- [ ] Merge: объединение партиций; для консолидации; оптимизация
- [ ] Мониторинг: размер партиций; использование; неравномерное распределение

### 182. Partition pruning

- [ ] Статический pruning: при планировании запроса; анализ WHERE условий; отсечение партиций
- [ ] Динамический pruning: при выполнении запроса; для prepared statements; параметры
- [ ] Prepared statements: возможная неоптимальность; все партиции при первом выполнении; решение
- [ ] Условия для pruning: равенство по ключу партиционирования; диапазоны; IN списки
- [ ] Оптимизация: правильные условия WHERE; использование ключа партиционирования в запросах

### 183. Partition-wise операции

- [ ] Partition-wise join: соединение партиционированных таблиц по партициям; параллелизм; эффективность
- [ ] Partition-wise aggregate: агрегация по партициям с последующим объединением; меньше памяти
- [ ] Параллелизм по партициям: выполнение операций на партициях параллельно; масштабирование
- [ ] Ограничения: одинаковое партиционирование; совместимые ключи; условия для использования
- [ ] Оптимизация: правильное партиционирование; использование в запросах; настройка

### 184. Уникальность и FK при партиционировании

- [ ] Ограничения: первичный ключ и уникальные индексы должны включать ключ партиционирования
- [ ] Локальные vs глобальные индексы: локальные (на каждой партиции), глобальные (на всей таблице)
- [ ] Foreign keys: ограничения при партиционировании; ссылки на партиционированные таблицы; сложность
- [ ] Решения: компромиссы; использование приложения для обеспечения целостности; ограничения

### 185. Мониторинг партиций

- [ ] Размер партиций: отслеживание роста; неравномерное распределение; оптимизация
- [ ] Использование: статистика по партициям; какие партиции используются; оптимизация
- [ ] Статистика по партициям: отдельная статистика для каждой партиции; ANALYZE по партициям
- [ ] Неравномерное распределение: горячие партиции; причины; решения (rebalance, split)
- [ ] Автоматизация: мониторинг и алерты; автоматическое управление; оптимизация

---

## Часть XXXIII. Расширенные темы репликации

### 186. Streaming replication (PostgreSQL)

- [ ] Настройка: конфигурация primary и standby; pg_hba.conf; recovery.conf / standby.signal
- [ ] Синхронная vs асинхронная: синхронная — ожидание применения; асинхронная — без ожидания
- [ ] Multiple standbys: несколько реплик; выбор синхронной реплики; quorum commit
- [ ] Quorum commit: ожидание применения на нескольких репликах; majority; отказоустойчивость
- [ ] Мониторинг: pg_stat_replication; lag; состояние реплик; синхронность
- [ ] Оптимизация: настройка сети; оптимизация реплики; балансировка нагрузки

### 187. Logical replication (PostgreSQL)

- [ ] Публикация и подписка: CREATE PUBLICATION, CREATE SUBSCRIPTION; настройка; управление
- [ ] Фильтрация: фильтрация таблиц в публикации; выбор данных для репликации
- [ ] Конфликты: причины конфликтов; разрешение (error, apply, skip); настройка
- [ ] Initial copy: начальная копия данных; copy_data опция; синхронизация
- [ ] Мониторинг: pg_stat_subscription; lag; ошибки; состояние подписок
- [ ] Использование: для миграций; для интеграций; для масштабирования чтения

### 188. Binlog репликация (MySQL)

- [ ] Формат binlog: statement-based (SQL команды), row-based (изменения строк), mixed (комбинация)
- [ ] GTID: Global Transaction Identifier; уникальный ID транзакции; упрощение репликации
- [ ] Настройка: конфигурация master и slave; подключение; начало репликации
- [ ] Мониторинг lag: SHOW SLAVE STATUS; Seconds_Behind_Master; анализ отставания
- [ ] Оптимизация: настройка binlog; ротация; сжатие; производительность

### 189. Group replication (MySQL)

- [ ] Multi-master: несколько master узлов; запись на любой узел; консистентность
- [ ] Консенсус: алгоритм консенсуса; выбор primary; координация записей
- [ ] Split-brain защита: предотвращение разделения; кворум; автоматическое разрешение
- [ ] Автоматический failover: выбор нового primary при сбое; автоматическое переключение
- [ ] Ограничения: ограничения на операции; конфликты; производительность

### 190. Репликация MongoDB

- [ ] Replica set: набор реплик; primary и secondary; выбор primary (election)
- [ ] Oplog: операционный лог; репликация изменений; размер oplog
- [ ] Выбор primary: автоматический выбор; приоритеты; ручной выбор
- [ ] Read preference: чтение из primary, secondary, nearest; выбор стратегии
- [ ] Write concern: гарантии записи; w (число подтверждений), j (journal); настройка

### 191. Репликация Redis

- [ ] Master-replica: классическая репликация; один master, несколько replicas; асинхронная
- [ ] Sentinel: мониторинг; автоматический failover; выбор нового master; кворум
- [ ] Cluster: шардирование; hash slots; репликация слотов; распределённое хранение
- [ ] Репликация слотов: каждый слот реплицируется; отказоустойчивость; масштабирование

### 192. Репликация Cassandra

- [ ] Replication factor: число копий данных; настройка; отказоустойчивость
- [ ] Стратегии: SimpleStrategy (один дата-центр), NetworkTopologyStrategy (несколько дата-центров)
- [ ] Consistency levels: ONE, TWO, THREE, QUORUM, ALL, LOCAL_QUORUM; выбор уровня
- [ ] Quorum: большинство реплик; баланс консистентности и доступности; настройка

---

## Часть XXXIV. Расширенные темы шардирования

### 193. Стратегии шардирования

- [ ] Range sharding: по диапазону значений; простота; риск горячих границ
- [ ] Hash sharding: по хешу ключа; равномерное распределение; отсутствие диапазонных запросов
- [ ] Directory-based: таблица маршрутизации; гибкость; overhead на маршрутизацию
- [ ] Consistent hashing: равномерное распределение; минимизация перебалансировки; использование
- [ ] Выбор стратегии: зависит от паттернов запросов; распределение данных; требования

### 194. Citus детали

- [ ] Distributed tables: распределённые таблицы; автоматическое шардирование; прозрачность
- [ ] Reference tables: реплицируемые таблицы; копия на каждом узле; для малых таблиц
- [ ] Colocation: совместное размещение связанных данных; эффективные JOIN; настройка
- [ ] Rebalance: перебалансировка данных; перемещение данных между узлами; автоматизация
- [ ] Cross-shard queries: запросы между шардами; scatter-gather; ограничения

### 195. Vitess детали

- [ ] Keyspace: логическая база данных; шардирование; управление
- [ ] Shard: физический шард; данные; репликация
- [ ] Vindex: виртуальный индекс; hash, lookup, unicode_lookup; маршрутизация
- [ ] Resharding: изменение числа шардов; перенос данных; процедура
- [ ] VReplication: репликация между шардами; для resharding; синхронизация

### 196. Cross-shard операции

- [ ] Scatter-gather: запрос на все шарды; объединение результатов; overhead
- [ ] Агрегация: агрегация по шардам; объединение результатов; точность
- [ ] Сортировка: сортировка по шардам; merge sort; ограничения
- [ ] JOIN между шардами: сложность; colocation; broadcast; shuffle; ограничения
- [ ] Ограничения: производительность; сложность; компромиссы

### 197. Решардинг

- [ ] Изменение числа шардов: увеличение или уменьшение; необходимость; процедура
- [ ] Перенос данных: копирование данных; синхронизация; переключение
- [ ] Downtime: возможный downtime; минимизация; online resharding
- [ ] Online resharding: resharding без downtime; сложность; инструменты

### 198. Мониторинг шардирования

- [ ] Распределение данных: анализ распределения; неравномерность; горячие ключи
- [ ] Горячие ключи: один ключ — много трафика; выявление; решения
- [ ] Неравномерность: неравномерное распределение; причины; rebalance triggers
- [ ] Rebalance triggers: автоматический rebalance; пороги; настройка

### 199. Роутинг запросов

- [ ] Application-level routing: роутинг в приложении; знание шардов; простота
- [ ] Proxy routing: ProxySQL, PgBouncer; прозрачность; централизация
- [ ] Middleware routing: Citus, Vitess; автоматический роутинг; сложность
- [ ] Выбор стратегии: зависит от архитектуры; требования; компромиссы

---

## Часть XXXV. Расширенные темы индексов

### 200. B-tree детали

- [ ] Структура узлов: внутренние узлы (ключи + указатели), листовые узлы (ключи + данные)
- [ ] Page split: разделение страницы при переполнении; балансировка; производительность
- [ ] Fill factor: заполненность страниц; настройка; влияние на UPDATE
- [ ] Bloat причины: UPDATE создаёт новые версии; DELETE оставляет пустое место; VACUUM
- [ ] Перестроение: REINDEX; когда необходимо; влияние на производительность; CONCURRENTLY

### 201. GIN детали

- [ ] Posting list и posting tree: структура индекса; эффективное хранение множеств значений
- [ ] Fast update: pending list для быстрых обновлений; отложенная индексация; производительность
- [ ] Vacuum merge: объединение pending list в основной индекс; автоматическое; настройка
- [ ] Использование для массивов: индексация элементов массивов; операторы @>, <@, &&
- [ ] Использование для JSONB: индексация ключей и значений; операторы @>, ?, ?&, ?|

### 202. GiST детали

- [ ] Tree structure: обобщённое дерево поиска; гибкость; различные типы данных
- [ ] Penalty function: оценка расширения при вставке; выбор поддерева; оптимизация
- [ ] Picksplit: разделение узла; распределение ключей; эффективность
- [ ] Consistent function: проверка соответствия запросу; использование индекса; фильтрация
- [ ] Использование для диапазонов: индексация диапазонов; операторы &&, @>, <@
- [ ] Использование для геометрии: пространственные индексы; PostGIS; операторы

### 203. BRIN детали

- [ ] Block range: диапазон блоков; минимальный размер индекса; эффективность
- [ ] Min-max summary: минимум и максимум значений в диапазоне; фильтрация; точность
- [ ] Autosummarize: автоматическое обновление summary; настройка; производительность
- [ ] Эффективность для упорядоченных данных: данные упорядочены по индексируемому столбцу; использование
- [ ] Ограничения: только для упорядоченных данных; точность; компромиссы

### 204. Составные индексы

- [ ] Порядок столбцов: важен для использования индекса; left-prefix rule; оптимизация
- [ ] Left-prefix rule: использование первых столбцов индекса; влияние на запросы
- [ ] Covering indexes: все нужные столбцы в индексе; index-only scan; INCLUDE columns
- [ ] INCLUDE columns: дополнительные столбцы в индексе; для covering; не для поиска

### 205. Частичные индексы

- [ ] WHERE clause: условие для индексации; только часть строк; эффективность
- [ ] Использование для фильтрации: индексация только нужных строк; уменьшение размера
- [ ] Уникальные частичные индексы: уникальность среди отфильтрованных строк; использование
- [ ] Примеры: индексация активных записей; индексация по статусу; оптимизация

### 206. Индексы по выражениям

- [ ] Функциональные индексы: индекс на выражение; LOWER(email), UPPER(name); использование
- [ ] Immutable функции: функции должны быть immutable; влияние на использование индекса
- [ ] Использование: для запросов с функциями; оптимизация; ограничения
- [ ] Примеры: индексация по LOWER(); индексация по выражениям; оптимизация запросов

---

## Часть XXXVI. Расширенные темы оптимизации

### 207. Чтение планов выполнения

- [ ] Cost: оценка стоимости; условные единицы; сравнение планов
- [ ] Rows: оценка числа строк; влияние на выбор плана; точность
- [ ] Actual time: фактическое время выполнения; сравнение с оценкой; анализ
- [ ] Узлы плана: типы узлов; чтение дерева; понимание выполнения
- [ ] Поддеревья: вложенные планы; анализ частей; оптимизация
- [ ] Initplan vs subplan: однократное выполнение vs многократное; влияние на производительность

### 208. Статистика и селективность

- [ ] Гистограммы: распределение значений; оценка селективности; точность
- [ ] MCV (most common values): наиболее частые значения; оценка для частых значений
- [ ] Correlation: корреляция физического и логического порядка; влияние на оценку
- [ ] Влияние на планы: неверная статистика — неверные планы; обновление статистики
- [ ] Настройка: увеличение статистики для сложных столбцов; точность оценок

### 209. Параллельное выполнение

- [ ] Gather узел: сбор результатов от workers; координация; overhead
- [ ] Workers: параллельные процессы; выполнение частей запроса; ограничения
- [ ] Parallel seq scan: параллельное сканирование; разделение работы; эффективность
- [ ] Parallel hash join: параллельное соединение; распределение данных; масштабирование
- [ ] Parallel aggregate: параллельная агрегация; объединение результатов; эффективность
- [ ] Ограничения: не все операции параллелизуются; зависимость от данных; настройка

### 210. JIT компиляция

- [ ] Когда используется: для сложных запросов; jit_above_cost; настройка
- [ ] Компиляция выражений: компиляция WHERE условий; ускорение выполнения
- [ ] Компиляция агрегатов: компиляция агрегатных функций; оптимизация
- [ ] Влияние на производительность: ускорение сложных запросов; overhead компиляции
- [ ] Настройка: jit_above_cost, jit_inline_above_cost; баланс компиляции и выполнения

### 211. Подсказки (hints)

- [ ] USE INDEX, FORCE INDEX (MySQL): принудительное использование индекса; ограничения оптимизатора
- [ ] Ограничения в PostgreSQL: нет hints; влияние на портабельность; альтернативы
- [ ] Когда использовать: неоптимальные планы; временное решение; оптимизация
- [ ] Альтернативы: настройка статистики; переписывание запросов; настройка параметров

### 212. Оптимизация JOIN

- [ ] Порядок таблиц: влияет на план; оптимизатор выбирает; можно влиять
- [ ] Nested loop: для малых таблиц; эффективность; ограничения
- [ ] Hash join: для больших таблиц; эффективность; память
- [ ] Merge join: для отсортированных данных; эффективность; ограничения
- [ ] Выбор оптимизатором: анализ стоимости; выбор оптимального; влияние статистики

### 213. Оптимизация подзапросов

- [ ] Развертывание в JOIN: преобразование подзапроса в JOIN; оптимизатор делает автоматически
- [ ] Материализация: создание временной таблицы; для сложных подзапросов; эффективность
- [ ] Коррелированные подзапросы: ссылка на внешний запрос; влияние на производительность; оптимизация
- [ ] EXISTS vs IN: когда эквивалентны; когда различаются; выбор; производительность

---

## Часть XXXVII. Расширенные темы транзакций

### 214. Snapshot isolation

- [ ] Как работает: снимок данных на начало транзакции; видимость версий; изоляция
- [ ] Видимость версий: правила видимости; xmin/xmax; транзакционные снимки
- [ ] Snapshot на начало транзакции: фиксация видимости; консистентность чтения
- [ ] Преимущества: отсутствие блокировок при чтении; высокая производительность; параллелизм

### 215. Serializable snapshot isolation (SSI)

- [ ] rw-conflict detection: обнаружение конфликтов чтения-записи; сериализуемость
- [ ] Serialization failure: ошибка при конфликте; retry логика; обработка
- [ ] Retry логика: повтор транзакции при serialization failure; идемпотентность; реализация
- [ ] Преимущества: истинная сериализуемость; без блокировок; производительность

### 216. Двухфазный коммит

- [ ] PREPARE TRANSACTION: подготовка транзакции; блокировка ресурсов; координация
- [ ] COMMIT PREPARED: коммит подготовленной транзакции; финальное подтверждение
- [ ] Распределённые транзакции: транзакции на нескольких БД; координатор; сложность
- [ ] Координатор: управление 2PC; координация участников; отказоустойчивость

### 217. XA транзакции

- [ ] Внешний координатор: координация транзакций; управление; сложность
- [ ] Начало, подготовка, коммит/откат: фазы транзакции; координация; надёжность
- [ ] Поддержка в СУБД: PostgreSQL, MySQL, Oracle; ограничения; использование
- [ ] Ограничения: сложность; производительность; отказоустойчивость

### 218. Saga паттерн

- [ ] Компенсирующие транзакции: откат через компенсацию; распределённые транзакции; надёжность
- [ ] Choreography vs orchestration: децентрализованная vs централизованная координация; выбор
- [ ] Идемпотентность: повторная обработка безопасна; гарантии; реализация
- [ ] Использование: микросервисы; распределённые системы; компромиссы

### 219. Outbox pattern

- [ ] Транзакционная гарантия публикации: запись в БД и очередь в одной транзакции; надёжность
- [ ] Таблица outbox: хранение событий для публикации; транзакционность; гарантии
- [ ] CDC для публикации: чтение outbox через CDC; публикация в очередь; надёжность
- [ ] Использование: гарантия доставки; интеграции; микросервисы

### 220. Длинные транзакции

- [ ] Влияние на bloat: мёртвые строки не удаляются; накопление; проблемы
- [ ] Влияние на репликацию: lag репликации; накопление WAL; проблемы
- [ ] Влияние на блокировки: длительные блокировки; блокирование других транзакций; проблемы
- [ ] Решения: короткие транзакции; batch processing; оптимизация; мониторинг

---

## Часть XXXVIII. Расширенные темы типов данных

### 221. Числовые типы

- [ ] Точность DECIMAL/NUMERIC: точное представление; точность и масштаб; использование для денег
- [ ] Масштаб: число знаков после запятой; влияние на хранение; округление
- [ ] Округление: правила округления; банковское округление; точность
- [ ] Float vs decimal для денег: float — неточность; decimal — точность; выбор
- [ ] Переполнение: обработка переполнения; ошибки; защита

### 222. Строковые типы

- [ ] VARCHAR vs TEXT: ограничение длины vs без ограничения; использование; производительность
- [ ] Кодировка: UTF-8, Latin1; влияние на размер; совместимость
- [ ] Коллации: порядок сортировки; case-sensitive vs insensitive; выбор
- [ ] Байтовая vs символьная длина: LENGTH (байты) vs CHAR_LENGTH (символы); UTF-8 различия
- [ ] Оптимизация: выбор типа; влияние на индексы; производительность

### 223. Дата и время

- [ ] TIMESTAMP WITH TIME ZONE vs WITHOUT: хранение таймзоны; преобразование; использование
- [ ] Таймзоны: работа с таймзонами; преобразование; локальность
- [ ] DST (Daylight Saving Time): переход на летнее время; обработка; проблемы
- [ ] INTERVAL: интервалы времени; арифметика; использование
- [ ] Точность: микросекунды; настройка точности; использование

### 224. JSON и JSONB

- [ ] Различия: JSON (текстовый), JSONB (бинарный); производительность; использование
- [ ] Операторы: @> (содержит), ? (ключ существует), -> (объект), ->> (текст), #> (путь), #>> (текст по пути)
- [ ] Индексы GIN: индексация ключей и значений; использование операторов; производительность
- [ ] jsonpath: SQL/JSON path; фильтрация и извлечение; использование
- [ ] Оптимизация: выбор JSON vs JSONB; использование индексов; производительность

### 225. Массивы

- [ ] Создание: ARRAY[]; типы элементов; использование
- [ ] Операторы: && (пересечение), @> (содержит), <@ (содержится в), [] (индекс)
- [ ] Индексы GIN: индексация элементов массивов; использование операторов; производительность
- [ ] Unnest для JOIN: разворачивание массивов; JOIN с другими таблицами; использование
- [ ] Ограничения: размер массивов; производительность; использование

### 226. Диапазоны

- [ ] int4range, tstzrange: диапазоны целых и временных меток; создание; использование
- [ ] Операторы: && (пересечение), @> (содержит), <@ (содержится в); использование
- [ ] Индексы GiST: индексация диапазонов; использование операторов; производительность
- [ ] Использование для периодов: хранение периодов; запросы по периодам; оптимизация
- [ ] Ограничения: типы диапазонов; производительность; использование

### 227. UUID и ENUM

- [ ] Генерация UUID: uuid_generate_v4(), gen_random_uuid(); уникальность; использование
- [ ] Использование как PK: преимущества (распределённость), недостатки (размер, фрагментация)
- [ ] ENUM типы: перечисления; создание; добавление значений; порядок
- [ ] Ограничения ENUM: сложность изменения; порядок значений; использование
- [ ] Альтернативы: CHECK constraints; справочные таблицы; выбор

---

## Часть XXXIX. Расширенные темы мониторинга

### 228. Метрики производительности

- [ ] QPS, TPS: запросов/транзакций в секунду; throughput; мониторинг
- [ ] Latency: задержка; p50, p95, p99, p999; анализ распределения
- [ ] Throughput: пропускная способность; измерение; оптимизация
- [ ] Error rate: частота ошибок; мониторинг; алерты
- [ ] Анализ: тренды; сравнение; оптимизация

### 229. Метрики ресурсов

- [ ] CPU usage: использование процессора; анализ; оптимизация
- [ ] Memory: shared_buffers, work_mem, temp; использование; оптимизация
- [ ] Disk I/O: чтение/запись; очередь; оптимизация
- [ ] Network: сетевой трафик; задержка; оптимизация
- [ ] Мониторинг: регулярный анализ; алерты; оптимизация

### 230. Метрики репликации

- [ ] Lag: отставание реплики; байты и секунды; анализ
- [ ] Replication slots: использование слотов; накопление WAL; мониторинг
- [ ] Sync standby: синхронная репликация; ожидание; производительность
- [ ] Failover time: время переключения; измерение; оптимизация
- [ ] Мониторинг: регулярная проверка; алерты; оптимизация

### 231. Метрики блокировок

- [ ] Lock wait time: время ожидания блокировки; анализ; оптимизация
- [ ] Deadlocks: количество deadlocks; анализ; предотвращение
- [ ] Blocking queries: блокирующие запросы; идентификация; решение
- [ ] Lock contention: конкуренция за блокировки; анализ; оптимизация
- [ ] Мониторинг: регулярная проверка; алерты; оптимизация

### 232. Метрики кэша

- [ ] Buffer pool hit ratio: процент попаданий в кэш; цель > 99%; оптимизация
- [ ] Index hit ratio: процент попаданий в индекс; анализ; оптимизация
- [ ] Query cache hit ratio (MySQL): процент попаданий в query cache; deprecated; альтернативы
- [ ] Анализ: тренды; оптимизация; настройка

### 233. Метрики роста

- [ ] Размер БД, таблиц, индексов: отслеживание роста; анализ; прогнозирование
- [ ] Скорость роста: анализ трендов; прогнозирование; планирование
- [ ] Прогнозирование: экстраполяция; capacity planning; планирование
- [ ] Capacity planning: планирование ресурсов; масштабирование; оптимизация

### 234. Алертинг

- [ ] Пороги для алертов: настройка порогов; чувствительность; баланс
- [ ] Escalation policies: эскалация алертов; уведомления; обработка
- [ ] Интеграция: PagerDuty, Opsgenie; уведомления; автоматизация
- [ ] Runbooks: процедуры обработки; документация; обучение

---

## Часть XL. Расширенные темы бэкапов

### 235. Стратегии бэкапов

- [ ] Полный бэкап: полная копия данных; основа восстановления; частота
- [ ] Инкрементальный: только изменения; быстрее; требует полного
- [ ] Дифференциальный: изменения с последнего полного; компромисс
- [ ] Комбинации: полный + инкрементальные; оптимизация; восстановление
- [ ] Retention policies: политики хранения; соответствие требованиям; автоматизация

### 236. Физические бэкапы

- [ ] pg_basebackup: полная копия кластера PostgreSQL; для реплик и бэкапов
- [ ] File-level backup: копирование файлов данных; быстрее; требует остановки или snapshot
- [ ] Snapshot на уровне ОС: моментальный снимок; LVM snapshots; быстрое восстановление
- [ ] Быстрее восстановление: физические бэкапы быстрее логических; использование

### 237. Логические бэкапы

- [ ] pg_dump: логический дамп PostgreSQL; переносимость; выборочный бэкап
- [ ] mysqldump: логический дамп MySQL; переносимость; выборочный бэкап
- [ ] Переносимость: восстановление на другой версии/платформе; использование
- [ ] Выборочный бэкап: выбор объектов; таблицы, схемы; гибкость
- [ ] Восстановление части данных: восстановление отдельных таблиц; использование

### 238. WAL архивирование

- [ ] Непрерывное архивирование: копирование сегментов WAL; основа PITR
- [ ] archive_command: команда архивирования; настройка; автоматизация
- [ ] restore_command: команда восстановления; настройка; использование
- [ ] Основа PITR: восстановление до момента; использование WAL; точность

### 239. Point-in-Time Recovery

- [ ] Восстановление до момента: recovery_target_time; точное восстановление; использование
- [ ] Recovery_target_lsn: восстановление до LSN; точное восстановление; использование
- [ ] Тестирование: регулярное тестирование; проверка процедур; обучение
- [ ] Автоматизация: автоматическое тестирование; CI/CD интеграция; надёжность

### 240. Бэкапы в облаке

- [ ] Автоматические бэкапы managed БД: AWS RDS, Azure, GCP; автоматизация; надёжность
- [ ] Cross-region backup: бэкапы в другом регионе; отказоустойчивость; использование
- [ ] Lifecycle policies: автоматическое управление жизненным циклом; архивирование; удаление
- [ ] Восстановление: процедуры восстановления; тестирование; документация

### 241. Валидация бэкапов

- [ ] Проверка целостности: валидация бэкапов; проверка данных; использование
- [ ] Тестирование восстановления: регулярное тестирование; проверка процедур; обучение
- [ ] Автоматизация проверок: автоматическая валидация; CI/CD интеграция; надёжность
- [ ] Документация: процедуры валидации; результаты; улучшения

---

## Часть XLI. Расширенные темы Oracle и SQL Server

### 242. Oracle детали

- [ ] RAC (Real Application Clusters): кластеризация; несколько узлов; общее хранилище
- [ ] ASM (Automatic Storage Management): управление хранилищем; автоматизация; оптимизация
- [ ] PL/SQL: процедурный язык; расширенный SQL; использование
- [ ] Материализованные представления: предвычисленные представления; обновление; использование
- [ ] Партиционирование: range, list, hash, composite, interval, reference; гибкость

### 243. Oracle партиционирование и индексы

- [ ] Партиционирование: range, list, hash, composite, interval, reference; стратегии
- [ ] Индексы: B-tree, bitmap, function-based; использование; оптимизация
- [ ] Глобальные vs локальные индексы: глобальные (на всю таблицу), локальные (на партицию); выбор
- [ ] Оптимизация: использование партиционирования; индексы; производительность

### 244. SQL Server детали

- [ ] Always On Availability Groups: высокую доступность; автоматический failover; репликация
- [ ] Columnstore indexes: колоночные индексы; для аналитики; сжатие
- [ ] In-Memory OLTP: in-memory таблицы; высокая производительность; ограничения
- [ ] T-SQL специфика: расширения SQL; процедуры; функции; использование

### 245. SQL Server партиционирование и оптимизация

- [ ] Партиционирование: range, list; стратегии; использование
- [ ] Индексы: clustered, non-clustered, filtered; использование; оптимизация
- [ ] Statistics: статистика; обновление; влияние на планы
- [ ] Query hints: подсказки оптимизатору; использование; ограничения

### 246. Сравнение СУБД

- [ ] PostgreSQL vs MySQL vs Oracle vs SQL Server: сравнение возможностей; лицензии; экосистема
- [ ] Лицензии: открытые vs коммерческие; стоимость; ограничения
- [ ] Экосистема: инструменты; сообщество; поддержка
- [ ] Когда что выбирать: критерии выбора; требования; компромиссы

### 247. Миграция между СУБД

- [ ] Различия в типах данных: mapping типов; преобразование; тестирование
- [ ] Различия в SQL: диалекты SQL; совместимость; адаптация
- [ ] Инструменты миграции: автоматизация миграции; проверка; тестирование
- [ ] Тестирование: валидация миграции; проверка данных; производительность

### 248. Управляемые версии

- [ ] AWS RDS для Oracle/SQL Server: managed версии; преимущества; ограничения
- [ ] Azure SQL: managed SQL Server; преимущества; ограничения
- [ ] Ограничения: меньше контроля; зависимость от провайдера; стоимость
- [ ] Преимущества: управление; бэкапы; патчинг; масштабирование

---

## Часть XLII. Алгоритмы и структуры данных внутри СУБД

### 249. Алгоритмы JOIN

- [ ] Nested Loop простой: внешний цикл по одной таблице, внутренний по другой; O(N*M); для малых таблиц
- [ ] Nested Loop с индексом: внутренний цикл использует индекс; O(N*log(M)); эффективнее
- [ ] Block Nested Loop: блокирование внешней таблицы; уменьшение I/O; компромисс память/скорость
- [ ] Hash Join: build фаза (построение хеш-таблицы из меньшей таблицы), probe фаза (поиск в хеш-таблице); O(N+M)
- [ ] Hash Join spilling: при нехватке памяти — сброс части на диск; recursive hash join; влияние на производительность
- [ ] Merge Join: сортированные входы; слияние двух отсортированных последовательностей; O(N+M); требует сортировки
- [ ] Adaptive Join: выбор алгоритма во время выполнения; начало с nested loop, переключение на hash при необходимости
- [ ] Выбор алгоритма: размер таблиц, наличие индексов, доступная память; влияние оптимизатора

### 250. Алгоритмы сортировки

- [ ] In-memory sort: быстрая сортировка в памяти (quicksort, timsort); ограничение work_mem
- [ ] External sort: сортировка больших данных; разбиение на runs; multi-way merge; spilling на диск
- [ ] Multi-way merge: слияние нескольких отсортированных runs; использование памяти; оптимизация
- [ ] Spilling на диск: при нехватке work_mem; создание временных файлов; влияние на производительность
- [ ] Оптимизация: увеличение work_mem; предварительная сортировка индексами; избежание сортировки

### 251. Алгоритмы агрегации

- [ ] Hash Aggregate: построение хеш-таблицы групп; агрегация при вставке; O(N); эффективно
- [ ] Sort + Aggregate: сортировка по группирующим столбцам; затем агрегация; требует сортировки
- [ ] Выбор алгоритма: размер групп; доступная память; наличие сортировки для ORDER BY
- [ ] Spilling: при нехватке памяти — сброс части на диск; recursive hash aggregate; влияние
- [ ] Оптимизация: увеличение work_mem; использование индексов для сортировки; предварительная группировка

### 252. LSM-деревья: структура и основы

- [ ] Memtable: in-memory структура данных; быстрая запись; при заполнении — flush на диск
- [ ] SSTable (Sorted String Table): отсортированные данные на диске; immutable; уровни L0-Ln
- [ ] Уровни LSM: L0 (memtable flush), L1-Ln (компактированные уровни); экспоненциальный рост размеров
- [ ] Compaction: объединение SSTable с разных уровней; удаление дубликатов и удалённых записей
- [ ] Write amplification: множественные записи одной логической записи; влияние compaction; измерение
- [ ] Read amplification: чтение нескольких уровней для поиска; влияние на производительность чтения

### 253. LSM compaction стратегии

- [ ] Size-Tiered Compaction (STCS): объединение SSTable похожего размера; простота; высокий write amplification
- [ ] Leveled Compaction (LCS): каждый уровень в 10 раз больше предыдущего; низкий write amplification; больше I/O
- [ ] Time-Window Compaction (TWCS): группировка по времени; для временных рядов; эффективность
- [ ] Выбор стратегии: паттерн записи; требования к чтению; компромиссы; настройка
- [ ] Tombstones: маркеры удаления; необходимость для LSM; cleanup при compaction; влияние на read amplification

### 254. Альтернативные индексные структуры

- [ ] Fractal Tree: структура с буферами в узлах; амортизация операций; TokuDB; write optimization
- [ ] Bε-tree: вариант B-tree с буферами; компромисс read/write; исследования
- [ ] Learned indexes: ML модели вместо традиционных структур; Kraska et al.; компромиссы точность/скорость
- [ ] Bitmap индексы: битовая карта для каждого значения; эффективны для низкой кардинальности; Oracle, DWH
- [ ] Использование: выбор структуры под паттерн доступа; компромиссы; реализация в СУБД

### 255. Inverted index и буферный менеджер

- [ ] Inverted index: терм → список документов (posting list); структура для полнотекстового поиска
- [ ] Posting list: список документов с термом; сжатие (delta encoding); использование в Elasticsearch
- [ ] Буферный менеджер: управление страницами в памяти; алгоритмы замены страниц
- [ ] LRU: Least Recently Used; простота; проблемы с sequential scan
- [ ] LRU-K: учитывает K последних обращений; улучшение для sequential access
- [ ] 2Q: two queues (hot и cold); разделение частого и редкого доступа
- [ ] ARC: Adaptive Replacement Cache; адаптация к паттернам доступа; эффективность
- [ ] Clock-sweep: вариант LRU; циклический обход; используется в PostgreSQL
- [ ] Prefetch: предзагрузка следующих страниц; sequential prefetch; random prefetch; оптимизация

---

## Часть XLIII. Теория транзакций и согласованности углублённо

### 256. Формальные модели изоляции

- [ ] Conflict serializability: эквивалентность по конфликтам операций; граф конфликтов; ацикличность
- [ ] View serializability: эквивалентность по виду данных; более слабое условие; сложность проверки
- [ ] Snapshot isolation формально: определение через snapshots; гарантии; аномалии (write skew)
- [ ] Read committed формально: только committed данные видны; определение; аномалии
- [ ] Repeatable read формально: snapshot на начало транзакции; определение; различия между СУБД
- [ ] Serializable формально: эквивалентность последовательному выполнению; строгое определение

### 257. Модели согласованности распределённых БД

- [ ] Linearizability: сильнейшая модель; глобальный порядок операций; примеры систем
- [ ] Sequential consistency: порядок операций каждого процесса сохраняется; слабее linearizability
- [ ] Causal consistency: сохранение причинно-следственных связей; векторные часы; использование
- [ ] PRAM: Pipelined RAM; асинхронная репликация; слабая модель; примеры
- [ ] Eventual consistency: в итоге все реплики сойдутся; определение; использование
- [ ] Strong eventual consistency: eventual + конфликт-свободная репликация; CRDT; гарантии

### 258. Two-phase locking (2PL)

- [ ] Basic 2PL: фаза роста (acquire locks), фаза сокращения (release locks); гарантия serializability
- [ ] Strict 2PL: блокировки удерживаются до конца транзакции; предотвращение каскадных откатов
- [ ] Wound-wait протокол: старшая транзакция "ранит" младшую; предотвращение deadlock; реализация
- [ ] Wait-die протокол: младшая транзакция ждёт или умирает; предотвращение deadlock; реализация
- [ ] Deadlock prevention: предотвращение вместо обнаружения; протоколы; компромиссы
- [ ] Сравнение с MVCC: блокировки vs версионирование; производительность; компромиссы

### 259. Timestamp ordering

- [ ] Basic TO: присвоение timestamp транзакции; проверка конфликтов; откат при конфликте
- [ ] Multiversion TO (MVTO): несколько версий строк; timestamp для версий; чтение подходящей версии
- [ ] Конфликты и откаты: обнаружение конфликтов; стратегии отката; производительность
- [ ] Сравнение с 2PL: отсутствие блокировок; больше откатов; компромиссы
- [ ] Реализация: timestamp assignment; conflict detection; rollback strategies

### 260. CAP теорема формально

- [ ] Доказательство интуитивно: при partition — выбор между C и A; формальное доказательство
- [ ] CP системы: консистентность и partition tolerance; примеры (HBase, MongoDB с majority)
- [ ] AP системы: доступность и partition tolerance; примеры (Cassandra, DynamoDB)
- [ ] CA системы: консистентность и доступность; только без partition; примеры (single node)
- [ ] PACELC расширение: при отсутствии partition — Latency vs Consistency; примеры систем
- [ ] Практика: реальные системы выбирают компромиссы; настройка уровней консистентности

### 261. Реализация изоляции в СУБД

- [ ] PostgreSQL: snapshot isolation; версионирование строк; видимость; SSI для serializable
- [ ] MySQL InnoDB: gap locks для repeatable read; next-key locks; предотвращение фантомов
- [ ] Oracle: MVCC; undo segments; read consistency; serializable через блокировки
- [ ] SQL Server: row versioning; snapshot isolation; read committed snapshot; различия
- [ ] Сравнение: как разные СУБД обеспечивают уровни; различия в реализации; компромиссы

### 262. Слабая согласованность и CRDT

- [ ] Eventual consistency модели: определение; использование; компромиссы
- [ ] CRDT: Conflict-free Replicated Data Types; математические основы; гарантии
- [ ] Типы CRDT: state-based (convergent), operation-based (commutative); примеры
- [ ] Векторные часы: отслеживание причинно-следственных связей; использование; ограничения
- [ ] Logical clocks: Lamport clocks, vector clocks; использование в распределённых системах
- [ ] Применение: распределённые системы; репликация; конфликт-свободная репликация

---

## Часть XLIV. LSM-деревья и write-optimized storage

### 263. LSM структура уровней

- [ ] L0: memtable flush; множество маленьких SSTable; overlap между файлами; необходимость compaction
- [ ] L1-Ln: компактированные уровни; экспоненциальный рост размеров (×10); меньше overlap
- [ ] Соотношение размеров: L1 = 10×L0, L2 = 10×L1 и т.д.; настройка; влияние на compaction
- [ ] Memtable: in-memory структура; быстрая запись; при заполнении — flush; размер
- [ ] SSTable структура: отсортированные данные; индекс; bloom filter; immutable

### 264. Compaction стратегии LSM

- [ ] Size-Tiered (STCS): объединение SSTable похожего размера; простота реализации; высокий write amplification
- [ ] Leveled (LCS): каждый уровень в 10 раз больше; SSTable не перекрываются; низкий write amplification; больше I/O
- [ ] Time-Window (TWCS): группировка по времени; для временных рядов; эффективность для TTL
- [ ] Выбор стратегии: паттерн записи (random vs sequential); требования к чтению; компромиссы
- [ ] Настройка: параметры compaction; влияние на производительность; мониторинг

### 265. Tombstones и amplification

- [ ] Tombstones: маркеры удаления в LSM; необходимость для удаления; влияние на read
- [ ] Cleanup: удаление tombstones при compaction; когда можно удалить; политики
- [ ] Write amplification: множественные записи одной логической записи; измерение; оптимизация
- [ ] Read amplification: чтение нескольких уровней для поиска; влияние на производительность; оптимизация
- [ ] Space amplification: дублирование данных на разных уровнях; влияние; компромиссы

### 266. RocksDB и варианты LSM

- [ ] RocksDB: Facebook LSM; варианты compaction (universal, leveled); настройки; производительность
- [ ] Использование: MySQL MyRocks, TiKV, MongoDB WiredTiger (вариант); распространённость
- [ ] LevelDB: базовая LSM; Google; простота; ограничения
- [ ] WiredTiger: LSM вариант; MongoDB; настройки; производительность
- [ ] Cassandra/HBase: LSM реализация; compaction стратегии; особенности

### 267. Event sourcing и commit log

- [ ] Append-only лог: основа event sourcing; неизменяемость; история изменений
- [ ] Event store: хранилище событий; append-only; восстановление состояния; snapshots
- [ ] Kafka log: persistent log; репликация; использование как event store
- [ ] Commit log в СУБД: WAL как commit log; использование для репликации; CDC
- [ ] Event sourcing паттерн: события как источник истины; восстановление состояния; использование

---

## Часть XLV. Железо-ориентированный тюнинг и архитектура

### 270. Cache-friendly алгоритмы

- [ ] Cache line alignment: выравнивание данных по границам cache line (64 bytes); уменьшение false sharing
- [ ] Row-oriented layout: данные построчно; cache-friendly для сканирования строк; традиционный подход
- [ ] Column-oriented layout: данные постолбцово; cache-friendly для агрегаций; аналитика
- [ ] Cache-oblivious структуры: эффективны независимо от размера кэша; алгоритмы; использование
- [ ] Оптимизация: выбор layout под паттерн доступа; измерение cache misses; профилирование

### 271. NUMA и многопроцессорность

- [ ] NUMA: Non-Uniform Memory Access; локальная vs удалённая память; влияние на производительность
- [ ] Pinning процессов: привязка к NUMA узлам; numactl; оптимизация доступа к памяти
- [ ] Распределение буферных пулов: по NUMA узлам; локальность данных; оптимизация
- [ ] numa_maps анализ: анализ использования памяти по NUMA узлам; выявление проблем; оптимизация
- [ ] Многопроцессорность: использование нескольких CPU; параллелизм; contention

### 272. Contention и spinlocks

- [ ] Contention: конкуренция за shared ресурсы; влияние на производительность; измерение
- [ ] Spinlocks: активное ожидание блокировки; для коротких критических секций; CPU циклы
- [ ] Mutex: блокирующее ожидание; для длительных операций; переключение контекста
- [ ] Latches в СУБД: кратковременные блокировки; защита внутренних структур; contention
- [ ] Измерение contention: профилирование; wait events; оптимизация; уменьшение contention

### 273. NVMe/SSD vs HDD и durability

- [ ] NVMe/SSD: низкая задержка random I/O; высокая пропускная способность; характеристики
- [ ] HDD: высокая задержка random I/O; последовательный I/O быстрее; характеристики
- [ ] Write barriers: гарантия порядка записи; fsync семантика; влияние на производительность
- [ ] FUA (Force Unit Access): принудительная запись на диск; bypass кэша; durability
- [ ] fsync семантика: гарантия записи на диск; влияние на производительность; компромиссы
- [ ] Durability: гарантия сохранности данных; настройки; компромиссы надёжность/скорость

### 274. RDMA и In-Memory DBMS

- [ ] RDMA: Remote Direct Memory Access; низкая задержка; обход CPU; использование в распределённых БД
- [ ] VoltDB: in-memory DBMS; snapshot на диск; высокая производительность; ограничения
- [ ] MemSQL: hybrid (in-memory + disk); columnstore; высокая производительность; использование
- [ ] Hekaton: SQL Server In-Memory OLTP; компиляция в native code; высокая производительность
- [ ] Архитектуры: in-memory подходы; компромиссы; использование; ограничения

### 275. Оптимизация под железо

- [ ] CPU cache optimization: использование кэша процессора; cache-friendly алгоритмы; измерение
- [ ] Memory bandwidth: пропускная способность памяти; влияние на производительность; оптимизация
- [ ] I/O patterns: последовательный vs случайный; оптимизация под устройство; измерение
- [ ] Профилирование на уровне железа: perf, VTune; анализ производительности; оптимизация
- [ ] Компромиссы: производительность vs сложность; оптимизация под конкретное железо

---

## Часть XLVI. Колончатые движки: внутренняя кухня

### 277. Кодировки и сжатие в колончатых БД

- [ ] RLE (Run-Length Encoding): кодирование последовательностей одинаковых значений; эффективность для повторяющихся значений
- [ ] Dictionary encoding: словарь уникальных значений; индексы вместо значений; эффективность для низкой кардинальности
- [ ] Delta encoding: хранение разностей между значениями; эффективность для упорядоченных данных
- [ ] Bit-packing: упаковка значений в биты; эффективность для малых значений
- [ ] Frame-of-reference: базовая точка + отклонения; эффективность для близких значений
- [ ] Выбор кодировки: зависит от данных; автоматический выбор; влияние на сжатие и скорость

### 278. Vectorized execution

- [ ] Batch processing: обработка векторов значений за раз; эффективность; использование SIMD
- [ ] SIMD: Single Instruction Multiple Data; параллельная обработка; использование в колончатых БД
- [ ] Late materialization: отложенная материализация строк; работа с колонками; эффективность
- [ ] Оптимизация: использование векторных инструкций; batch size; влияние на производительность
- [ ] Реализация: как СУБД используют vectorization; примеры; измерение эффекта

### 279. Storage layout колончатых БД

- [ ] Сегменты: единицы хранения; организация данных; размеры
- [ ] Stripe'ы: полосы данных; распределение; параллелизм
- [ ] Zone maps: min/max значения для сегментов; отсечение данных; эффективность
- [ ] Min/max pruning: использование zone maps для отсечения; уменьшение I/O; оптимизация
- [ ] Организация: как данные организованы на диске; влияние на производительность; оптимизация

### 280. ClickHouse внутренности

- [ ] MergeTree структура: основа ClickHouse; сортировка данных; эффективность
- [ ] Primary key и order by: определяют сортировку; влияние на запросы; оптимизация
- [ ] Партиции: разделение данных; по времени; автоматическое управление
- [ ] Материализованные представления: предвычисленные агрегаты; обновление при вставке; использование
- [ ] Сжатие: эффективное сжатие; кодировки; влияние на производительность

### 281. Snowflake внутренности

- [ ] Micro-partitions: маленькие партиции; автоматическое управление; эффективность
- [ ] Clustering keys: ключи кластеризации; автоматическая кластеризация; оптимизация
- [ ] Automatic clustering: автоматическая рекластеризация; поддержание порядка; эффективность
- [ ] Storage и compute разделение: независимое масштабирование; преимущества; использование
- [ ] Оптимизация: автоматическая оптимизация; влияние на производительность; настройка

### 282. Columnar индексы

- [ ] Columnstore indexes в SQL Server: колончатые индексы; использование для аналитики; compression
- [ ] Batch mode: пакетная обработка; использование columnstore; эффективность
- [ ] Использование: для аналитических запросов; компромиссы; настройка
- [ ] Оптимизация: выбор индексов; влияние на производительность; измерение

### 283. Оптимизация колончатых БД

- [ ] Выбор кодировок: автоматический выбор; влияние на сжатие; оптимизация
- [ ] Настройка сжатия: баланс сжатия и скорости; компромиссы; измерение
- [ ] Vectorized execution: использование векторных инструкций; оптимизация; измерение эффекта
- [ ] Параллелизм: параллельная обработка; масштабирование; оптимизация

---

## Часть XLVII. Большие данные и SQL поверх data lake

### 284. Presto/Trino

- [ ] Распределённый SQL движок: SQL поверх различных источников; connector архитектура; использование
- [ ] Connector архитектура: подключение к различным источникам; расширяемость; реализация
- [ ] Execution model: распределённое выполнение; координация; оптимизация
- [ ] Оптимизация запросов: cost-based оптимизация; распределение работы; эффективность
- [ ] Использование: data lake queries; аналитика; интеграция

### 285. Spark SQL

- [ ] SQL поверх Spark: использование Spark для SQL; Catalyst optimizer; производительность
- [ ] Catalyst optimizer: оптимизация запросов; rule-based и cost-based; эффективность
- [ ] DataFrame API: программируемый интерфейс; интеграция с SQL; использование
- [ ] Интеграция с data lake: чтение из различных форматов; оптимизация; использование

### 286. Hive

- [ ] SQL поверх Hadoop: использование Hadoop для SQL; MapReduce execution; производительность
- [ ] Tez engine: улучшенный execution engine; оптимизация; производительность
- [ ] LLAP (Live Long and Process): долгоживущие процессы; кэширование; производительность
- [ ] Metastore: хранилище метаданных; схема данных; использование
- [ ] Использование: data warehouse на Hadoop; аналитика; интеграция

### 287. Impala

- [ ] MPP SQL движок: massively parallel processing; высокая производительность; использование
- [ ] In-memory execution: выполнение в памяти; эффективность; ограничения
- [ ] Интеграция с HDFS: чтение из HDFS; оптимизация; производительность
- [ ] Производительность: сравнение с Hive; использование; оптимизация

### 288. Parquet формат

- [ ] Columnar формат: данные постолбцово; эффективное сжатие; использование
- [ ] Структура файла: row groups, column chunks, pages; организация; чтение
- [ ] Сжатие: эффективное сжатие колонок; кодировки; влияние на размер
- [ ] Статистика: min/max значения; использование для pruning; эффективность
- [ ] Использование: data lake формат; аналитика; интеграция с инструментами

### 289. ORC и Avro

- [ ] ORC (Optimized Row Columnar): оптимизированный колончатый формат; структура; использование
- [ ] ORC индексы: индексы для быстрого поиска; использование; эффективность
- [ ] Avro: row-based формат; schema evolution; использование
- [ ] Schema evolution: эволюция схемы; совместимость; использование
- [ ] Сравнение форматов: Parquet vs ORC vs Avro; выбор; использование

### 290. Lakehouse детали

- [ ] Delta Lake: ACID транзакции; time travel; schema evolution; использование
- [ ] Iceberg: hidden partitioning; schema evolution; использование; преимущества
- [ ] Hudi: incremental processing; upserts; использование; преимущества
- [ ] Сравнение: Delta vs Iceberg vs Hudi; выбор; использование
- [ ] ACID в data lake: транзакции поверх файлов; реализация; компромиссы

---

## Часть XLVIII. Формальная теория баз данных

### 291. Реляционное исчисление

- [ ] Tuple calculus: исчисление кортежей; выразительная мощность; связь с SQL
- [ ] Domain calculus: исчисление доменов; выразительная мощность; использование
- [ ] Связь с реляционной алгеброй: эквивалентность выразительной мощности; преобразования
- [ ] Связь с SQL: SQL как реализация исчисления; понимание SQL через исчисление
- [ ] Теорема Кодда: эквивалентность алгебры и исчисления; значение; использование

### 292. Volcano/Cascades framework

- [ ] Volcano framework: архитектура оптимизатора; search space; cost model; использование
- [ ] Cascades framework: улучшенная версия Volcano; transformation rules; эффективность
- [ ] Search space: пространство возможных планов; перебор; ограничения
- [ ] Cost model: модель стоимости; оценка планов; выбор оптимального
- [ ] Transformation rules: правила преобразования планов; применение; эффективность

### 293. Heuristic vs cost-based оптимизация

- [ ] Rule-based оптимизация: применение правил; простота; ограничения
- [ ] Cost-based оптимизация: оценка стоимости; выбор оптимального плана; эффективность
- [ ] Гибридные подходы: комбинация правил и стоимости; эффективность; использование
- [ ] Ограничения: не все планы перебираются; приближения; компромиссы
- [ ] Оптимизация оптимизатора: улучшение оценки стоимости; влияние на планы

### 294. Теория типов в SQL

- [ ] NULL как bottom type: NULL в теории типов; влияние на функции; использование
- [ ] Three-valued logic формально: TRUE, FALSE, UNKNOWN; формальное определение; использование
- [ ] Partial functions: частичные функции; NULL handling; использование
- [ ] Constraints как логические формулы: ограничения как предикаты; формальное определение; использование
- [ ] Типовая система SQL: типы в SQL; проверка типов; использование

### 295. Query optimization как поиск

- [ ] Search space планов: пространство возможных планов; размер; перебор
- [ ] Dynamic programming: динамическое программирование для поиска; эффективность; использование
- [ ] Greedy алгоритмы: жадные алгоритмы; быстрота; компромиссы
- [ ] Ограничения перебора: не все планы перебираются; эвристики; компромиссы
- [ ] Оптимизация поиска: улучшение алгоритмов поиска; влияние на производительность

### 296. Cardinality estimation

- [ ] Статистика для оценки: гистограммы; MCV; использование; точность
- [ ] Гистограммы: распределение значений; оценка селективности; использование
- [ ] Sampling: выборка данных; оценка по выборке; точность; компромиссы
- [ ] Ошибки оценки: влияние на планы; последствия; минимизация ошибок
- [ ] Улучшение оценки: более точная статистика; влияние на планы; оптимизация

### 297. Теоретические основы

- [ ] Реляционная модель формально: формальное определение; аксиомы; использование
- [ ] ACID формально: формальное определение ACID; гарантии; использование
- [ ] Транзакции как истории: транзакции как последовательности операций; формальное определение
- [ ] Serializability формально: формальное определение serializability; проверка; использование
- [ ] Теоретические основы: понимание БД через теорию; применение; использование

---

## Часть XLIX. Исследовательские темы и современная литература

### 298. NewSQL/HTAP архитектуры

- [ ] TiDB HTAP: hybrid transactional/analytical processing; архитектура; использование
- [ ] Spanner TrueTime: глобальное распределение; TrueTime для консистентности; исследования
- [ ] CockroachDB: глобальное распределение; консистентность; исследования; использование
- [ ] HTAP подходы: объединение OLTP и OLAP; компромиссы; исследования
- [ ] Современные исследования: новые архитектуры; улучшения; направления

### 299. Learned indexes

- [ ] Kraska et al. "The Case for Learned Index Structures": ML модели вместо B-tree; исследования
- [ ] Learned indexes: использование ML для индексов; компромиссы точность/скорость; исследования
- [ ] Применение: где используются learned indexes; эффективность; ограничения
- [ ] Компромиссы: точность vs скорость; обучение; использование
- [ ] Исследования: текущие исследования; направления; будущее

### 300. Learned cardinality estimation

- [ ] ML для оценки кардинальности: использование ML для улучшения оценок; исследования
- [ ] Улучшение планов: влияние на планы запросов; эффективность; использование
- [ ] Исследования: текущие исследования; направления; будущее
- [ ] Применение: где используется; эффективность; ограничения

### 301. CRDT и конфликт-устойчивая репликация

- [ ] CRDT: Conflict-free Replicated Data Types; математические основы; использование
- [ ] Типы CRDT: state-based, operation-based; примеры; использование
- [ ] Конфликт-устойчивая репликация: репликация без конфликтов; гарантии; использование
- [ ] Применение: распределённые системы; репликация; использование
- [ ] Исследования: текущие исследования; направления; будущее

### 302. Классические papers

- [ ] System R (1970s): основа реляционных БД; влияние; чтение и понимание
- [ ] Spanner (Google): глобальное распределение; TrueTime; чтение и понимание
- [ ] F1 (Google): распределённая БД; использование; чтение и понимание
- [ ] Calvin (Yale): распределённые транзакции; исследования; чтение и понимание
- [ ] FaRM (Microsoft): быстрые распределённые транзакции; исследования; чтение и понимание
- [ ] Как читать papers: подход к чтению; понимание; применение

### 303. Классические книги

- [ ] "Readings in Database Systems" (Red Book): классическая книга; темы; изучение
- [ ] "Designing Data-Intensive Applications" (Kleppmann): современная книга; темы; изучение
- [ ] Другие книги: список важных книг; темы; изучение
- [ ] Как изучать: подход к изучению; применение; использование

### 304. Современные исследования

- [ ] SIGMOD, VLDB, ICDE: конференции по БД; темы исследований; слежение
- [ ] Темы исследований: текущие направления; важность; применение
- [ ] Как следить: отслеживание исследований; источники; применение
- [ ] Применение исследований: использование исследований в практике; компромиссы

---

## Часть L. Инциденты и пост-мортемы

### 305. Real-world инциденты

- [ ] Разбор публичных postmortem'ов: анализ реальных инцидентов; извлечение уроков; применение
- [ ] Отказ репликации: примеры инцидентов; причины; решения; предотвращение
- [ ] Потеря данных: примеры инцидентов; причины; решения; предотвращение
- [ ] Lock storm: примеры инцидентов; причины; решения; предотвращение
- [ ] Network partitions: примеры инцидентов; причины; решения; предотвращение
- [ ] Уроки: извлечение уроков из инцидентов; применение; улучшение

### 306. Шаблон post-mortem

- [ ] Timeline событий: хронология инцидента; детали; документирование
- [ ] Root cause analysis: анализ корневой причины; методы; применение
- [ ] Remediation: что было сделано для решения; действия; эффективность
- [ ] Action items: что будет сделано для предотвращения; планы; отслеживание
- [ ] Шаблон: стандартный шаблон post-mortem; использование; улучшение

### 307. Типичные инциденты

- [ ] Репликация lag: типичные причины; решения; предотвращение
- [ ] OOM: типичные причины; решения; предотвращение
- [ ] Deadlock storms: типичные причины; решения; предотвращение
- [ ] Corruption данных: типичные причины; решения; предотвращение
- [ ] Network partitions: типичные причины; решения; предотвращение
- [ ] Предотвращение: стратегии предотвращения; применение; улучшение

### 308. Анализ инцидентов

- [ ] Сбор данных: логи, метрики; методы сбора; использование
- [ ] Анализ причин: методы анализа; применение; эффективность
- [ ] Предотвращение повторения: стратегии; применение; эффективность
- [ ] Документация: документирование инцидентов; использование; улучшение

### 309. Runbooks

- [ ] Процедуры обработки инцидентов: стандартные процедуры; использование; улучшение
- [ ] Автоматизация: автоматизация обработки; использование; эффективность
- [ ] Обучение команды: обучение процедурам; применение; улучшение
- [ ] Регулярное обновление: обновление runbooks; применение; улучшение

### 310. Культура надёжности

- [ ] Blameless postmortems: культура без обвинений; применение; эффективность
- [ ] Learning from failures: обучение на ошибках; применение; улучшение
- [ ] Continuous improvement: непрерывное улучшение; применение; эффективность
- [ ] SRE принципы: принципы Site Reliability Engineering; применение; использование

---

## Часть LI. Database as Code и DevOps-практики

### 311. Database as Code и миграции как код

- [ ] Миграции как код: Flyway, Liquibase, Alembic; миграции в git-репозитории
- [ ] Версионирование схемы: номера версий, up/down-миграции, idempotent SQL
- [ ] Автоматический запуск миграций в CI/CD: перед деплоем, при запуске приложения
- [ ] Стратегии отката: rollback-скрипты, hotfix-миграции, feature toggles
- [ ] Проверки миграций: dry-run, миграции на staging, валидация схемы

### 312. Infrastructure as Code для БД

- [ ] Terraform/Pulumi для БД: описания RDS/Aurora/Cloud SQL, параметров, security groups
- [ ] Управление параметрами БД как кодом: parameter groups, конфигурационные файлы
- [ ] Provisioning окружений: dev/stage/prod базы, шаблоны модулей
- [ ] Иммутабельная инфраструктура: создание новых инстансов вместо ручных правок
- [ ] Idempotency и повторяемость: создание БД и схем без побочных эффектов

### 313. DevOps-паттерны для изменений в БД

- [ ] Zero-downtime паттерны: расширяющие миграции (expand/contract), безопасные DDL
- [ ] Blue-green и canary для БД: переключение на новую схему, совместимость версий
- [ ] Feature flags: включение функционала после миграции, мгновенное отключение
- [ ] Dark reads/writes: запись в новую схему параллельно старой, сравнение результатов
- [ ] Release management: окна деплоя, freeze-периоды, согласование с бизнесом

### 314. Организация работы команд

- [ ] Роли: DBA, платформенная команда, data engineers, application devs
- [ ] Модели взаимодействия: централизованный DBA vs embedded DBA в командах
- [ ] Процесс review для изменений в схеме: code review миграций, approval-потоки
- [ ] Стандарты проектирования схем: гайды, шаблоны, чеклисты
- [ ] Документация изменений: changelog, ADR (Architecture Decision Records) по БД

---

## Часть LII. Качество данных и управление данными (Data Quality & Governance)

### 315. Качество данных и валидация

- [ ] Валидация на уровне БД: NOT NULL, CHECK, FK, доменные ограничения
- [ ] Профилирование данных: дубликаты, пропуски, выбросы; инструменты профилирования
- [ ] Контроль качества в пайплайнах: проверки в ETL/ELT, data contracts
- [ ] Мониторинг качества: метрики качества (completeness, accuracy, timeliness)

### 316. Data governance и метаданные

- [ ] Роли и ответственность: data owners, data stewards; модель владения доменами
- [ ] Data catalog: инструменты (Data Catalog, Collibra, Amundsen, DataHub); поиск наборов данных
- [ ] Business glossary: бизнес-термины, связи с таблицами и полями
- [ ] Data lineage: происхождение данных, lineage-графы, трассировка источников

### 317. MDM и мастер-данные

- [ ] Master Data Management: концепция \"золотой записи\", источники истины
- [ ] Слияние записей: matching/merging, правила разрешения конфликтов
- [ ] Синхронизация мастер-данных между системами (CDC, шины, API)
- [ ] Качество мастер-данных: регулярные проверки и отчёты

### 318. Приватность, защита и хранение данных

- [ ] Классификация данных: публичные, внутренние, конфиденциальные, чувствительные (PII/PHI)
- [ ] Политики retention: сколько хранить разные типы данных; legal hold
- [ ] Анонимизация/псевдонимизация: техники, влияние на аналитические сценарии
- [ ] Маскирование и субсеты данных для тестовых окружений

---

## Часть LIII. Современные архитектуры: federation, mesh, multi-cloud, serverless DB

### 319. Federated databases и data virtualization

- [ ] Federated queries: объединение данных из разных БД на уровне запроса
- [ ] Data virtualization: логический слой поверх множества источников
- [ ] Ограничения: производительность, консистентность, сложности отладки

### 320. Multi-region и multi-cloud для БД

- [ ] Паттерны multi-region: active-active, active-passive, geo-partitioning
- [ ] Multi-cloud стратегии: дублирование данных между облаками, portability
- [ ] Vendor lock-in: риски, абстракции, слой совместимости

### 321. Serverless базы данных

- [ ] Serverless реляционные: Aurora Serverless, Cloud SQL serverless режимы
- [ ] Serverless NoSQL: DynamoDB on-demand, Firestore; модель оплаты и масштабирования
- [ ] Ограничения и trade-offs: холодные старты, лимиты, непредсказуемая стоимость

### 322. Data/Database Mesh

- [ ] Data mesh: доменно-ориентированное владение данными; продуктовый подход к датасетам
- [ ] Database mesh: распределённые сервисы БД, общие политики, observability
- [ ] Контракты между доменами: схемы, SLA/SLI, версионирование

### 323. Оптимизация стоимости и capacity planning

- [ ] Моделирование нагрузки и стоимости: чтение/запись, storage, сеть
- [ ] Правильный выбор инстансов и storage-классов в облаке
- [ ] Автоматическое масштабирование и бюджеты, алерты по стоимости

---

## Часть LIV. Расширенное кэширование и производительность

### 324. Паттерны кэширования

- [ ] Cache-aside, read-through, write-through, write-behind, refresh-ahead
- [ ] Кэширование на уровне приложения vs на уровне БД
- [ ] TTL, инвалидация, кеш-шторм (cache stampede) и его профилактика

### 325. Кэширование результатов запросов и слоёв

- [ ] Redis/Memcached как кэш для тяжёлых запросов и агрегатов
- [ ] Кэширование на уровне API Gateway/GraphQL (persisted queries)
- [ ] Материализованные представления как persistent-кэш; стратегии обновления

### 326. Соединения и пулы соединений (advanced)

- [ ] Архитектуры пулов: PgBouncer (session/transaction), ProxySQL, Odyssey
- [ ] Лимиты соединений: расчёт max_connections, pool_size, влияние на ресурсы
- [ ] Throttling и backpressure: защита БД от перегрузки

### 327. Регрессионное тестирование производительности

- [ ] Бенчмарки и профилирование до/после изменений (SQL и схемы)
- [ ] Хранение исторических метрик и сравнение версий
- [ ] Автоматические performance-guards в CI/CD (регрессионные тесты)

### 328. Работа с hot-keys и skew

- [ ] Выявление горячих ключей и \"неравномерной\" нагрузки
- [ ] Техники разгрузки: шардирование по ключу, random suffix, write sharding
- [ ] Rate limiting, очереди и деградация сервиса под нагрузкой

---

## Часть LV. Observability, APM и distributed tracing

### 329. Метрики и SLI/SLO для БД

- [ ] Основные метрики: latency p50/p95/p99, throughput, error rate
- [ ] SLI/SLO для БД: доступность, задержка, свежесть данных
- [ ] Дашборды для БД: какие графики нужны дежурному инженеру

### 330. Логи и анализ логов БД

- [ ] Структурированные логи запросов: JSON-формат, корреляционные ID
- [ ] Агрегация логов (ELK, Loki, Cloud Logging) и фильтрация запросов
- [ ] Детальные логи ошибок и медленных запросов; хранение и ретенция

### 331. Distributed tracing с участием БД

- [ ] OpenTelemetry: spans для запросов к БД; связи с запросами приложений
- [ ] Трассировка через сервисы, очереди и БД в единой цепочке
- [ ] Анализ латентности end-to-end и поиск bottleneck'ов

### 332. APM-инструменты и профилирование

- [ ] Интеграция APM (New Relic, Datadog, AppDynamics) с БД
- [ ] Профилирование нагрузочных сценариев: CPU, I/O, lock wait
- [ ] Алертинг по симптомам (ошибки, timeouts, saturation) vs по причинам

---

## Часть LVI. Refactoring и работа с legacy-базами

### 333. Подходы к рефакторингу схем

- [ ] Strangler-fig паттерн: поэтапная замена legacy-схемы новой
- [ ] Слои совместимости: представления, триггеры, API-слой
- [ ] Миграция API без мгновенного изменения схемы

### 334. Online-миграции и минимизация риска

- [ ] expand/contract подход: добавление новых столбцов/таблиц, постепенное переключение
- [ ] Shadow-таблицы и двойная запись (dual write) для проверки корректности
- [ ] Планирование и rehearsal миграций на копиях продакшен-данных

### 335. Миграция с legacy-СУБД и гетерогенные миграции

- [ ] Переезд с Oracle/SQL Server на PostgreSQL/MySQL: типы, функции, диалекты
- [ ] Инструменты миграции схемы и данных; валидация эквивалентности
- [ ] Стратегии cutover: big bang vs поэтапный переход

### 336. Работа с накопившимися антипаттернами

- [ ] God-tables, over-normalization и under-normalization: как распознать и исправлять
- [ ] Удаление неиспользуемых таблиц, столбцов, индексов; архивация старых данных
- [ ] Постепенное улучшение схемы без больших переписок

### 337. Документация и передача знаний

- [ ] Документирование исторических решений и ограничений legacy-систем
- [ ] Планирование передачи знаний при смене команд/подрядчиков
- [ ] Построение культуры постоянного улучшения схем и запросов

---

**Справочники** (используй при создании md-файлов по темам): типы данных по СУБД, список агрегатных и оконных функций, параметры настройки (PostgreSQL, MySQL).

**Навигация:** [Краткий обзор структуры](#краткий-обзор-структуры-плана-для-навигации) — в конце документа.

---

## Краткий обзор структуры плана (для навигации)

> Порядок изучения: см. [Последовательность изучения](#последовательность-изучения-от-простого-к-сложному) в начале документа.

| Часть | Уровень | Тема |
|-------|---------|------|
| 0 | 0 | Философия, классификация, ментальные модели |
| I | 1 | Теория и модели данных (реляционная модель, нормализация, алгебра, ER) |
| II | 2 | SQL основы (DDL, DML, SELECT, агрегация, FILTER, GROUPING SETS) |
| III | 3 | SQL средний уровень (JOIN, подзапросы, окна, CTE, множества, NULL) |
| IV | 4 | Транзакции, изоляция, блокировки, MVCC, 2PC, оптимистичная блокировка |
| V | 5 | Хранение, буферный пул, WAL, формат строк, HOT, память, I/O |
| VI | 6 | Индексы (B-tree, hash, GiST/GIN/BRIN, составные, покрывающие, bloat) |
| VII | 7 | Оптимизация запросов, планы, статистика, параллельное выполнение, антипаттерны |
| XIV | 7 | Партиционирование, partition pruning, VACUUM, репликация PG, бэкап |
| VIII | 8 | Реляционные СУБД: PostgreSQL, MySQL, SQLite, другие; подключение |
| XIII | 8 | SQL углублённо: типы, JSON/полнотекст, представления, триггеры, процедуры, sequence |
| XVII | 8 | PostgreSQL детали: расширения, системные каталоги, конфигурация, типы |
| XVIII | 8 | MySQL детали: движки, InnoDB, binlog, настройки, оптимизация, инструменты |
| XIX | 9 | Геопространственные данные: PostGIS, пространственные типы, запросы, индексы |
| XX | 9 | Администрирование: настройка ОС, профилирование, бенчмаркинг, тюнинг |
| XXI | 9 | Разработка: паттерны доступа к данным, транзакции, масштабирование, антипаттерны |
| XXII | 10 | Интеграции: CDC, ETL, коннекторы, Kafka, message queues, GraphQL, REST API |
| XXIII | 10 | Инфраструктура: Docker, Kubernetes, managed БД, облачные NoSQL, multi-cloud |
| XXIV | 11 | Тестирование: unit/integration/performance тесты, ER диаграммы, документация |
| XXV | 11 | Катастрофоустойчивость: DR планы, multi-region, failover, бэкапы, тестирование |
| XXVI | 8 | SQL функции и операторы: строковые, числовые, дата/время, системные, операторы |
| XXVII | 9 | Troubleshooting: диагностика медленных запросов, блокировок, репликации, памяти, I/O, bloat |
| XXVIII | 10 | Безопасность расширенная: типы SQL-инъекций, защита, атаки, шифрование, KMS, аудит, маскирование |
| XXIX | 8 | Системные представления: information_schema, pg_catalog, метаданные, статистика, размеры |
| XXX | 9 | NoSQL расширенный: MongoDB, Redis, Cassandra, Elasticsearch, Neo4j, InfluxDB, DynamoDB детали |
| XXXI | 10 | Векторные БД расширенные: pgvector, Pinecone, Weaviate, Milvus, Qdrant детали, оптимизация |
| XXXII | 9 | Партиционирование расширенное: стратегии, управление, partition-wise операции, мониторинг |
| XXXIII | 10 | Репликация расширенная: streaming, logical, binlog, group replication, MongoDB, Redis, Cassandra |
| XXXIV | 10 | Шардирование расширенное: стратегии, Citus, Vitess, cross-shard, решардинг, роутинг |
| XXXV | 9 | Индексы расширенные: B-tree, GIN, GiST, BRIN детали, составные, частичные, по выражениям |
| XXXVI | 9 | Оптимизация расширенная: чтение планов, статистика, параллелизм, JIT, hints, JOIN, подзапросы |
| XXXVII | 10 | Транзакции расширенные: snapshot isolation, SSI, 2PC, XA, saga, outbox, длинные транзакции |
| XXXVIII | 8 | Типы данных расширенные: числовые, строковые, дата/время, JSON, массивы, диапазоны, UUID, ENUM |
| XXXIX | 10 | Мониторинг расширенный: метрики производительности, ресурсов, репликации, блокировок, кэша, роста |
| XL | 10 | Бэкапы расширенные: стратегии, физические, логические, WAL, PITR, облачные, валидация |
| XLI | 10 | Oracle и SQL Server: RAC, PL/SQL, Always On, Columnstore, сравнение, миграция, managed |
| XLII | 11 | Алгоритмы СУБД: JOIN (nested/hash/merge), сортировка, агрегация, LSM, индексы, буферный менеджер |
| XLIII | 11 | Теория транзакций: формальные модели изоляции, согласованность, 2PL, TO, CAP, CRDT |
| XLIV | 11 | LSM и write-optimized: структура уровней, compaction, amplification, RocksDB, event sourcing |
| XLV | 11 | Железо-ориентированный тюнинг: cache-friendly, NUMA, contention, NVMe/SSD, RDMA, in-memory DBMS |
| XLVI | 11 | Колончатые движки: кодировки, сжатие, vectorized execution, ClickHouse, Snowflake, columnar индексы |
| XLVII | 11 | Большие данные: Presto/Trino, Spark SQL, Hive, Impala, Parquet/ORC/Avro, Lakehouse (Delta/Iceberg/Hudi) |
| XLVIII | 12 | Формальная теория: реляционное исчисление, Volcano/Cascades, оптимизация, типы, cardinality estimation |
| XLIX | 12 | Исследования: NewSQL/HTAP, learned indexes, CRDT, классические papers/книги, современные исследования |
| L | 12 | Инциденты и пост-мортемы: разбор инцидентов, шаблоны, типичные проблемы, анализ, runbooks, культура надёжности |
| IX | 9 | NoSQL: документы, ключ–значение, широкостолбцовые, граф, временные ряды, поиск |
| X | 10 | Векторные БД: эмбеддинги, индексы, продукты, RAG |
| XI | 11 | Масштабирование: репликация, шардирование, CAP, 2PC/saga, CDC |
| XVI | 11 | Аналитика: OLAP, колоночные БД, хранилище данных, ETL, data lake |
| XII | 12 | Операции, безопасность, мониторинг, миграции, тестирование, выбор БД |

---

## Основные области (краткий указатель)

| Область | Ключевые темы |
|---------|----------------|
| **Теория** | Реляционная модель, ключи, нормализация (1NF–5NF), реляционная алгебра, ER, зависимости |
| **SQL основы** | DDL/DML, типы данных, ограничения, SELECT, агрегация, FILTER, GROUPING SETS, CUBE/ROLLUP |
| **SQL средний** | JOIN, LATERAL, подзапросы, оконные функции, CTE, UNION/INTERSECT/EXCEPT, пагинация, NULL |
| **Транзакции** | ACID, уровни изоляции, блокировки, MVCC, SSI, 2PC/XA, оптимистичная блокировка |
| **Хранение** | Страницы, буферный пул, WAL/LSN, формат строк, TOAST, HOT, visibility map, undo |
| **Индексы** | B-tree, hash, GiST/GIN/BRIN, составные, покрывающие, частичные, bloat, CLUSTER |
| **Оптимизация** | EXPLAIN, статистика, cost-based optimizer, параллельное выполнение, JIT, антипаттерны |
| **Партиционирование** | RANGE/LIST/HASH, partition pruning, partition-wise join, VACUUM, репликация, бэкап |
| **Продукты SQL** | PostgreSQL, MySQL, SQLite; расширения, системные каталоги; драйверы, пулы, ORM |
| **SQL углублённо** | Типы (коллации, таймзоны), JSON/XML/массивы/диапазоны, полнотекст, представления, триггеры, процедуры |
| **NoSQL** | Документы (MongoDB), ключ–значение (Redis), широкостолбцовые (Cassandra), граф (Neo4j), временные ряды, поиск |
| **Векторные** | Эмбеддинги, HNSW/IVF/LSH, квантизация, pgvector, Pinecone, Weaviate, RAG |
| **Масштаб** | Репликация, шардирование (Citus, Vitess), CAP/PACELC, консенсус, CDC, outbox |
| **Аналитика** | OLAP, колоночные БД (ClickHouse, Snowflake), хранилище данных, ETL, data lake |
| **PostgreSQL детали** | Расширения, системные каталоги, конфигурация, расширенные типы и функции |
| **MySQL детали** | Движки, InnoDB структура, binlog, настройки, оптимизация, инструменты |
| **Геопространственные** | PostGIS, пространственные типы (POINT, POLYGON), запросы (ST_Distance, ST_Within), индексы |
| **Администрирование** | Настройка ОС (huge pages, I/O scheduler), профилирование, бенчмаркинг, тюнинг памяти/I/O |
| **Разработка** | Паттерны (Repository, CQRS), транзакции, антипаттерны, best practices, версионирование данных |
| **Интеграции** | CDC (Debezium), ETL (Airflow, dbt), Kafka, message queues, GraphQL, REST API |
| **Инфраструктура** | Docker, Kubernetes, managed БД (RDS, Azure, GCP), облачные NoSQL, multi-cloud |
| **Тестирование** | Unit/integration/performance тесты, testcontainers, ER диаграммы, документация схемы |
| **SQL функции** | Строковые, числовые, дата/время, условные, преобразование типов, системные функции, операторы |
| **Troubleshooting** | Диагностика медленных запросов, блокировок, репликации, памяти, I/O, bloat, логи |
| **Безопасность расшир.** | Типы SQL-инъекций (blind, time-based), защита, атаки, шифрование, KMS, аудит, маскирование |
| **Метаданные** | information_schema, pg_catalog, метаданные схемы, статистика использования, размеры объектов |
| **NoSQL расшир.** | MongoDB (aggregation, change streams), Redis (структуры, Lua), Cassandra (CQL, consistency), Elasticsearch (mapping, query DSL), Neo4j (Cypher), InfluxDB (Flux), DynamoDB |
| **Векторные расшир.** | pgvector, Pinecone, Weaviate, Milvus, Qdrant детали, оптимизация поиска, метрики |
| **Партиционирование расшир.** | Стратегии (время, диапазон, список, хеш), управление, partition-wise операции, мониторинг |
| **Репликация расшир.** | Streaming, logical, binlog, group replication, MongoDB replica set, Redis Sentinel/Cluster, Cassandra |
| **Шардирование расшир.** | Стратегии, Citus, Vitess, cross-shard операции, решардинг, роутинг запросов |
| **Индексы расшир.** | B-tree/GIN/GiST/BRIN детали, составные, частичные, по выражениям, оптимизация |
| **Оптимизация расшир.** | Чтение планов, статистика/селективность, параллелизм, JIT, hints, оптимизация JOIN/подзапросов |
| **Транзакции расшир.** | Snapshot isolation, SSI, 2PC/XA, saga, outbox, длинные транзакции и их влияние |
| **Типы расшир.** | Числовые (точность), строковые (кодировка, коллации), дата/время (таймзоны), JSON/массивы/диапазоны |
| **Мониторинг расшир.** | Метрики производительности, ресурсов, репликации, блокировок, кэша, роста, алертинг |
| **Бэкапы расшир.** | Стратегии, физические/логические, WAL архивирование, PITR, облачные, валидация |
| **Oracle/SQL Server** | RAC, PL/SQL, Always On, Columnstore, сравнение СУБД, миграция, managed версии |
| **Алгоритмы СУБД** | JOIN (nested/hash/merge), сортировка (external sort), агрегация (hash/sort), LSM-деревья, альтернативные индексы, буферный менеджер (LRU, ARC, clock-sweep) |
| **Теория транзакций** | Формальные модели изоляции (conflict/view serializability), модели согласованности (linearizability, causal), 2PL, timestamp ordering, CAP формально, CRDT |
| **LSM и write-optimized** | Структура уровней, compaction (STCS/LCS/TWCS), amplification, RocksDB, event sourcing, commit log |
| **Железо-тюнинг** | Cache-friendly алгоритмы, NUMA, contention/spinlocks, NVMe/SSD vs HDD, RDMA, in-memory DBMS (VoltDB, MemSQL, Hekaton) |
| **Колончатые движки** | Кодировки (RLE, dictionary, delta), сжатие, vectorized execution/SIMD, ClickHouse, Snowflake, columnar индексы |
| **Большие данные** | Presto/Trino, Spark SQL, Hive, Impala, Parquet/ORC/Avro форматы, Lakehouse (Delta/Iceberg/Hudi) |
| **Формальная теория** | Реляционное исчисление, Volcano/Cascades framework, оптимизация как поиск, теория типов в SQL, cardinality estimation |
| **Исследования** | NewSQL/HTAP (TiDB, Spanner, CockroachDB), learned indexes, learned cardinality, CRDT, классические papers/книги |
| **Инциденты** | Разбор postmortem'ов, шаблоны анализа, типичные инциденты, runbooks, культура надёжности (blameless, SRE) |
| **DR** | Disaster recovery планы, multi-region репликация, failover, бэкап стратегии, тестирование |
| **Опер.** | Мониторинг, миграции, RLS, шифрование, SQL-инъекции, аудит, тестирование, capacity planning |

---

*План охватывает ВСЕ аспекты баз данных с максимальной детализацией: реляционные (SQL) и теорию, все SQL функции и операторы, типы данных и процедурный SQL, хранение и внутренности (WAL, VACUUM, партиционирование), индексы и оптимизацию, детали PostgreSQL и MySQL, геопространственные данные, администрирование и тюнинг, troubleshooting и диагностику, паттерны разработки, интеграции (CDC, ETL, Kafka), инфраструктуру (Docker, K8s, облака), тестирование и документацию, катастрофоустойчивость, расширенную безопасность, NoSQL (детали по каждому продукту), векторные БД (детали по каждому продукту), аналитику и хранилища данных, масштабирование и безопасность, алгоритмы и структуры данных внутри СУБД (JOIN, сортировка, агрегация, LSM), формальную теорию транзакций и согласованности, железо-ориентированный тюнинг, колончатые движки, большие данные и data lake, формальную теорию БД, исследовательские темы и современную литературу, инциденты и пост-мортемы. План включает более 310 параграфов (§) и 51 часть (0, I–L) с максимальной детализацией ВСЕХ аспектов работы с базами данных — от самых базовых концепций до самых продвинутых техник, алгоритмов, теоретических основ и исследовательских тем.*
