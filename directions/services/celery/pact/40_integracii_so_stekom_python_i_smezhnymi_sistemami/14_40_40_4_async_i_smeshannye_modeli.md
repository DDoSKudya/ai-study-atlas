[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## 40.4 Async и смешанные модели

### Цель раздела

Разобраться, как корректно сочетать Celery с `asyncio` и когда лучше разделять sync/async контуры, чтобы избежать конфликтов event loop и непредсказуемых performance-эффектов.

### В этом разделе главное

- Celery worker и `asyncio` loop — разные модели управления исполнением;
- `asyncio.run()` внутри sync-задачи допустим как bridge, но не универсальный паттерн;
- gevent/eventlet/threads/prefork дают разную модель I/O и изоляции;
- mixed-модель требует явных ограничений и тестов на реальном runtime.

### Термины

| Термин | Значение |
|---|---|
| **Concurrency model mismatch** | Несовпадение ожиданий между двумя моделями конкуренции. |
| **Event loop ownership** | Кто создает и управляет lifecycle `asyncio` loop. |
| **Bridge pattern** | Временный мост между sync task и async-функцией. |
| **Cooperative scheduling** | Модель gevent/eventlet, где задачи сами уступают управление. |

### Теория и правила

1. **Не путай "асинхронная задача" и "задача Celery"**  
   Celery асинхронен на уровне межпроцессной доставки; `asyncio` — внутри процесса.

2. **`asyncio.run` внутри задачи**  
   Работает для отдельных вызовов, но дорого при массовых коротких задачах. Может конфликтовать, если loop уже управляется иначе.

3. **Когда выделять отдельный контур**  
   Если большая доля I/O-async логики, лучше выделить async-сервис/воркер-слой, а Celery оставить orchestrator-ом.

4. **gevent/eventlet vs prefork**  
   Cooperative-пулы эффективны для I/O, но требуют совместимых библиотек и дисциплины monkeypatching. Prefork проще ментально для CPU-bound и изоляции.

5. **Граница ответственности**  
   Celery отвечает за доставку и scheduling попыток, async-слой — за эффективный I/O внутри попытки.

### Матрица выбора pool/model для задач

| Профиль задач | Чаще подходит | Почему | Осторожности |
|---|---|---|---|
| CPU-bound | `prefork` | изоляция процессов, предсказуемость | память на process, warm-up время |
| Умеренный I/O + sync SDK | `threads`/`prefork` | проще эксплуатация | GIL и блокирующие библиотеки |
| Массовый I/O + совместимый стек | `gevent`/`eventlet` | высокая плотность I/O ожиданий | monkeypatch discipline, library compatibility |
| Сложный async-first контур | отдельный async layer | прозрачная ownership loop | усложнение архитектуры |

### Пошагово: решение "нужен async-клиент в Celery"

1. Классифицируй workload: CPU-bound или I/O-bound.
2. Если точечный async-вызов — используй bridge с `asyncio.run`.
3. Если поток задач массово async — вынеси в отдельный async execution layer.
4. Проверь совместимость библиотек с выбранным pool.
5. Измерь latency/throughput на staging с профилем, похожим на prod.

### Простыми словами

Celery и `asyncio` — это два разных "диспетчера". Если два диспетчера одновременно считают, что они главные, на перекрестке возникает хаос.

### Картинка в голове

```text
Celery -> orchestrates attempts/retries/queueing
asyncio -> orchestrates awaitable I/O inside one attempt

Они могут работать вместе, если четко разделены роли.
```

### Как запомнить

**Celery управляет "когда и сколько раз", asyncio — "как ждать I/O внутри одной попытки".**

### Примеры

```python
import asyncio
from celery import shared_task

async def fetch_profile(user_id: str) -> dict:
    # async I/O logic here
    ...

@shared_task
def refresh_profile(user_id: str):
    # bridge pattern: acceptable for limited use
    return asyncio.run(fetch_profile(user_id))
```

### Практика / реальные сценарии

- **Временный bridge:** legacy sync-воркеры, но один новый async SDK; допустимо как этап миграции.
- **Антипаттерн:** 90% задач требуют async I/O, но всё продолжают крутить через sync bridge -> растут задержки и сложность диагностики.

### Типичные ошибки

- считать, что Celery "сам по себе asyncio";
- бездумно использовать gevent/eventlet без проверки совместимости библиотек;
- строить смешанный стек без performance-теста на realistic профиле.

### Что будет, если...

- **...перегрузить sync-worker массовым `asyncio.run`?**  
  Повышается накладной overhead, растет latency и появляется "дрожание" времени выполнения.

- **...игнорировать модель pool-а?**  
  Получишь нестабильное поведение библиотек, сложные race и трудно воспроизводимые баги.

### Проверь себя

1. В чем ключевая разница между async в Celery и async в `asyncio`?
2. Когда bridge-паттерн приемлем, а когда нужен отдельный async-контур?
3. Почему выбор pool-а должен идти вместе с выбором SDK/библиотек?

<details><summary>Ответ</summary>

1) Celery асинхронен между процессами/очередями, `asyncio` — внутри процесса при I/O ожиданиях.  
2) Bridge приемлем для ограниченного числа задач; при массовом async workload лучше выделенный слой.  
3) Потому что не все SDK корректно работают с cooperative scheduling и monkeypatching.

</details>

### Запомните

Смешанные модели допустимы, если роли разделены явно и подтверждены нагрузочным тестом.

---
