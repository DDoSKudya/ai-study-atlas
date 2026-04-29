[← Назад к индексу части 7](index.md)

## Справочник по части VII

| Тема | Ключевые пункты |
|------|------------------|
| **Планы выполнения** | EXPLAIN — план без выполнения; EXPLAIN ANALYZE — выполнение + actual time, actual rows; EXPLAIN (ANALYZE, BUFFERS) — плюс shared hit/read, temp read/write. Опции: FORMAT (TEXT/JSON/YAML), VERBOSE, COSTS, SETTINGS, TIMING, SUMMARY. Узлы: Seq Scan, Index Scan, Index Only Scan, Bitmap Index/Heap Scan; Nested Loop, Hash Join, Merge Join; Sort, Aggregate, Limit. cost — условные единицы; total cost корня — критерий выбора плана. |
| **Статистика** | ANALYZE — сбор статистики по таблице; автоанализатор — автоматический ANALYZE. pg_stats: n_distinct, histogram_bounds, most_common_vals, most_common_freqs, correlation (связь физического порядка строк с логическим по значению; используется для стоимости Index Scan при диапазонах — высокая correlation → более последовательное чтение, ниже cost). Селективность — доля строк по условию; оценка rows = селективность × число строк. Устаревшая статистика — после массовых изменений; решение ANALYZE. SET STATISTICS — увеличение детализации гистограммы по столбцу. |
| **Cost-based оптимизатор** | Планировщик выбирает план с минимальным total cost. Параметры: seq_page_cost, random_page_cost, cpu_tuple_cost; effective_cache_size — подсказка о кэше. Порядок JOIN — перебор вариантов; Nested Loop выгоден при малой внешней таблице; Hash Join при больших наборах без порядка. InitPlan — один раз; SubPlan — на каждую строку (коррелированный). Generic plan при подготовленных запросах — один план для всех параметров; возможна неоптимальность. Партиционирование: Append по партициям; partition pruning (static при константе, runtime при параметре). |
| **Параллелизм и JIT** | Gather — сбор результатов от workers. Parallel Seq Scan, Parallel Hash Join, Parallel Aggregate. max_parallel_workers_per_gather, max_parallel_workers. JIT — компиляция частей запроса; jit_above_cost — порог включения. SubPlan vs InitPlan — на каждую строку vs один раз. |
| **Антипаттерны** | N+1 — один запрос + N в цикле; решение: JOIN или batch IN. Отсутствие индекса — Seq Scan по большой таблице; решение: индекс + ANALYZE. SELECT * — лишние данные, нет index-only scan. Большой IN — батчинг или временная таблица. Несоответствие типов — приводить тип в значении, не в столбце. Повторяющийся подзапрос — CTE. Длинные транзакции — блокировки до COMMIT/ROLLBACK, bloat, отставание реплики; типы блокировок (SELECT FOR UPDATE, UPDATE/DELETE); deadlock (взаимная блокировка, СУБД прерывает жертву); мониторинг: pg_locks, pg_stat_activity (wait_event_type = Lock). Короткие транзакции; lock_timeout, statement_timeout. |
| **Настройка** | work_mem — память на Sort/Hash; при нехватке — Disk; effective_cache_size — подсказка планировщику. max_parallel_workers_per_gather, max_parallel_workers. pg_stat_statements — статистика по запросам (calls, total_exec_time, mean_exec_time); поиск тяжёлых запросов. auto_explain — логирование планов медленных запросов; log_min_duration_statement — логирование текста запросов дольше порога. |

---

### Частые сценарии: задача → решение

| Тема | Задача | Решение |
|------|--------|---------|
| **Диагностика** | Найти, почему запрос медленный | EXPLAIN (ANALYZE, BUFFERS) по запросу; смотреть узел с наибольшим actual time; при большом shared read — I/O; при temp read/write — увеличить work_mem. |
| **Оценки** | rows в плане сильно не совпадает с actual rows | Устаревшая статистика; ANALYZE таблица; при необходимости ALTER TABLE ... SET STATISTICS n по столбцу. |
| **План** | Планировщик выбирает Seq Scan вместо Index Scan | Проверить статистику (ANALYZE); на SSD уменьшить random_page_cost; проверить селективность (низкая — seq scan может быть выгоднее). |
| **Сортировка** | В плане Sort с «Disk» | Увеличить work_mem для сессии или запроса (SET work_mem = '128MB';). |
| **Параллелизм** | Запрос не использует параллельный план | Проверить max_parallel_workers_per_gather, max_parallel_workers; для маленьких таблиц параллелизм не выбирается. |
| **Тяжёлые запросы** | Найти самые тяжёлые запросы в системе | pg_stat_statements: ORDER BY total_exec_time DESC; затем EXPLAIN ANALYZE по тексту запроса. |
| **N+1** | Много одинаковых запросов с разными параметрами | Заменить цикл с запросом на один запрос с JOIN или batch IN (eager loading). |
| **Типы** | Индекс по столбцу не используется в условии | Проверить приведение типа: если col::text = $1 — приводить $1::тип_столбца или создать индекс по выражению (col::text). |

---

## Вопросы для самопроверки (часть VII)

1. Чем EXPLAIN отличается от EXPLAIN ANALYZE?  
<details><summary>Ответ</summary> **EXPLAIN** только строит план и **не выполняет** запрос; в выводе cost и rows (оценки). **EXPLAIN ANALYZE** **выполняет** запрос и добавляет actual time, actual rows (фактические время и число строк). Для диагностики медленных запросов нужен EXPLAIN ANALYZE.</details>

2. Что означают shared hit и shared read в BUFFERS?  
<details><summary>Ответ</summary> **shared hit** — страницы, прочитанные из **кэша** (shared_buffers). **shared read** — страницы, прочитанные **с диска**. Большой shared read — много дискового I/O для этого узла.</details>

3. Когда планировщик выбирает Nested Loop, а когда Hash Join?  
<details><summary>Ответ</summary> **Nested Loop** — когда **внешняя** таблица **мала** и внутренняя читается по индексу по ключу JOIN; cost = cost(внешняя) + rows(внешняя) × cost(одна строка внутренней). **Hash Join** — когда наборы **большие** и нет порядка по ключу; одна таблица строится в хеш в памяти, вторая сканируется с пробами в хеше. Планировщик выбирает вариант с меньшим cost.</details>

4. Зачем нужен ANALYZE после массовой загрузки?  
<details><summary>Ответ</summary> **ANALYZE** обновляет **статистику** по таблице (число строк, распределение, гистограммы). После массовой загрузки статистика устарела — планировщик строит планы по старым оценкам (rows, cost) и может выбрать **неоптимальный** план. Обновление статистики через ANALYZE даёт актуальные оценки и улучшает планы.</details>

5. Что такое селективность и как она влияет на план?  
<details><summary>Ответ</summary> **Селективность** — доля строк, удовлетворяющих условию. Планировщик оценивает селективность по MCV (равенство) и гистограмме (диапазон) и по ней считает **rows** (оценка числа строк). По rows считается cost узлов и выбор плана (seq vs index, порядок JOIN). Неверная селективность ведёт к неверным rows и к плохому плану.</details>

6. Что такое InitPlan и SubPlan?  
<details><summary>Ответ</summary> **InitPlan** — подзапрос выполняется **один раз** до основного запроса; результат кэшируется. **SubPlan** — подзапрос выполняется **для каждой строки** внешнего запроса (коррелированный подзапрос). SubPlan при большом числе строк — узкое место; решение — переписать в JOIN или IN с некоррелированным подзапросом.</details>

7. Что такое антипаттерн N+1 и как его исправить?  
<details><summary>Ответ</summary> **N+1** — один запрос за списком записей и **N запросов** в цикле по каждой записи (связанные данные). Итого 1 + N запросов к БД. **Исправление:** один запрос с **JOIN** (получить родителей и детей одним запросом) или один запрос за родителями + один запрос за всеми детьми с **IN (id1, id2, ...)** и сборка в приложении. В ORM — eager loading.</details>

8. На что влияет work_mem и когда его увеличивать?  
<details><summary>Ответ</summary> **work_mem** — максимальная память на **одну операцию** (Sort, Hash для JOIN/Aggregate). При нехватке данные сбрасываются на **диск** (в плане «Disk», «external merge») — запрос замедляется. **Увеличивать** при появлении «Disk» в плане Sort или Hash Aggregate; для сессии (SET work_mem) или для запроса (SET LOCAL work_mem). Учитывать число одновременных запросов — слишком большое work_mem может привести к OOM.</details>

9. Как найти самые тяжёлые запросы в PostgreSQL?  
<details><summary>Ответ</summary> Установить расширение **pg_stat_statements** (CREATE EXTENSION pg_stat_statements; требует shared_preload_libraries и перезапуск). Запросить представление **pg_stat_statements** и отсортировать по **total_exec_time DESC** — топ запросов по суммарному времени. По **calls** — самые частые. Затем по тексту запроса выполнить **EXPLAIN ANALYZE** для разбора плана.</details>

10. Зачем на SSD уменьшать random_page_cost?  
<details><summary>Ответ</summary> На **SSD** случайное чтение страницы почти так же быстро, как последовательное (в отличие от HDD). По умолчанию **random_page_cost = 4.0** — планировщик считает индексный доступ (много случайных чтений) **дорогим** и часто выбирает **Seq Scan**. **Уменьшение** random_page_cost (например, до 1.1–1.2) делает cost индексного доступа **ниже** — планировщик **чаще** выбирает Index Scan там, где он реально быстрее на SSD.</details>

11. Что такое partition pruning и чем static pruning отличается от runtime pruning?  
<details><summary>Ответ</summary> **Partition pruning** — отсечение партиций, которые **заведомо не содержат** строк по условию WHERE (по ключу партиционирования). Меньше партиций в плане — меньше I/O, быстрее запрос. **Static pruning** — отсечение на этапе **планирования**: значение в условии известно (константа, литерал), планировщик сразу оставляет в плане только нужные партиции. **Runtime pruning** — отсечение на этапе **выполнения**: значение приходит параметром ($1), на этапе планирования неизвестно; при выполнении по фактическому значению отсекаются лишние партиции. При параметре в generic плане могут фигурировать все партиции, но по факту сканируется только одна.</details>

12. Что такое correlation в pg_stats и как планировщик её использует при выборе плана?  
<details><summary>Ответ</summary> **correlation** — число от -1 до 1, связь **физического порядка строк** на диске с **логическим порядком** по значению столбца (1 — порядок совпадает, 0 — вперемешку). Планировщик использует correlation для **оценки стоимости Index Scan при диапазонных условиях** (BETWEEN, >, <): при **высокой** correlation чтение страниц таблицы по индексу считается более **последовательным** (ближе к seq_page_cost — дешевле); при **низкой** — более **случайным** (ближе к random_page_cost — дороже). Поэтому при высокой correlation Index Scan по диапазону чаще выбирается; при низкой может быть выбран Seq Scan.</details>

13. Чем плоха длинная транзакция с точки зрения блокировок и где посмотреть ожидания?  
<details><summary>Ответ</summary> **Блокировки** (на строки, страницы, таблицы при UPDATE/DELETE/SELECT FOR UPDATE) снимаются только в **COMMIT/ROLLBACK**. Длинная транзакция держит их **дольше** — другие сессии **ждут** или падают по lock_timeout. **Где смотреть:** **pg_locks** (кто какие блокировки держит или ждёт; granted = false — ожидание); **pg_stat_activity** (wait_event_type = 'Lock' — сессия ждёт блокировку). По ним видно «кто кого блокирует» и какие запросы зависли в ожидании. **Решение:** короткие транзакции; lock_timeout и statement_timeout для ограничения ожидания.</details>

---

## Резюме части VII

- **Планы выполнения:** EXPLAIN (план без выполнения, cost/rows) и EXPLAIN ANALYZE (выполнение + actual time/rows); BUFFERS — shared hit/read, temp read/write. Узлы: Seq Scan, Index Scan, Index Only Scan, Bitmap Scan; Nested Loop, Hash Join, Merge Join; Sort, Aggregate, Limit. cost — условные единицы; планировщик выбирает план с минимальным total cost.
- **Статистика:** ANALYZE собирает статистику по таблице; pg_stats хранит n_distinct, гистограммы, MCV, correlation. Селективность — доля строк по условию; оценка rows по селективности. Устаревшая статистика — после массовых изменений; решение ANALYZE; SET STATISTICS для детализации по столбцу.
- **Cost-based оптимизатор:** Параметры seq_page_cost, random_page_cost, cpu_tuple_cost; effective_cache_size. Порядок JOIN по cost; InitPlan (один раз) vs SubPlan (на каждую строку). Generic plan при подготовленных запросах — возможная неоптимальность при разных параметрах. Партиционирование: Append по партициям; partition pruning (static при константе, runtime при параметре).
- **Параллелизм и JIT:** Gather, workers; Parallel Seq Scan, Hash Join, Aggregate. max_parallel_workers_per_gather, max_parallel_workers. JIT — jit_above_cost. SubPlan vs InitPlan — коррелированный подзапрос vs некоррелированный.
- **Антипаттерны:** N+1 (один + N в цикле → JOIN или batch IN); отсутствие индексов (Seq Scan по большой таблице → индекс + ANALYZE); SELECT * (лишние данные, нет index-only); большой IN (батчинг или временная таблица); несоответствие типов (приводить в значении); повторяющийся подзапрос (CTE); длинные транзакции — блокировки до COMMIT/ROLLBACK, bloat, репликация; типы блокировок (UPDATE, SELECT FOR UPDATE); deadlock; мониторинг: pg_locks, pg_stat_activity (Lock). Короткие транзакции; lock_timeout, statement_timeout.
- **Настройка:** work_mem (память на Sort/Hash; при Disk увеличить); effective_cache_size (подсказка планировщику); max_parallel_workers_per_gather, max_parallel_workers. pg_stat_statements — поиск тяжёлых запросов; auto_explain и log_min_duration_statement — логирование медленных запросов и планов.

**Связь с частью VIII (Реляционные СУБД: продукты):** понимание планов (EXPLAIN), статистики и cost-based оптимизатора применимо к любой реляционной СУБД; детали (параметры, расширения pg_stat_statements, auto_explain) ориентированы на PostgreSQL; в других СУБД аналоги — EXPLAIN/EXPLAIN ANALYZE, статистика, настройки памяти и параллелизма, мониторинг запросов.

---

---

<!-- prev-next-nav -->
*[← 41. Настройка](06_41_nastrojka.md) | [→ Индекс части](index.md)*
