[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## 38.4 Другие hooks

### Цель раздела

Разобрать дополнительные точки расширения Celery: `task_annotations`, кастомные `Task` классы, а также custom serializers/backends/loaders.

### В этом разделе главное

- `task_annotations` — policy-слой для задач, особенно полезен для централизованных ограничений.
- `Task` subclass — лучший вариант, когда нужна управляемая логика вокруг выполнения конкретного класса задач.
- Кастомные serializers/backends/loaders дают гибкость, но увеличивают стоимость поддержки и риски совместимости.
- Любое расширение должно проходить через compatibility и rollback стратегию.

### Термины

| Термин | Формально | Простыми словами |
|---|---|---|
| **task_annotations** | Механизм массового переопределения свойств задач | «Центральная политика для task options» |
| **Task.__call__** | Обертка вызова task body | «Точка до/после выполнения кода задачи» |
| **before_start** | Хук до запуска выполнения task body | «Последняя подготовка перед работой» |
| **after_return** | Хук, вызываемый после завершения (успех/ошибка/ретрай) | «Единая финализация» |
| **Custom serializer** | Пользовательская сериализация payload | «Свой формат упаковки сообщений» |
| **Custom backend** | Пользовательская реализация хранилища результатов | «Свой способ хранить статусы/результаты» |
| **Loader** | Компонент загрузки конфигурации/контекста приложения | «Как Celery узнает настройки» |
| **Compatibility window** | Период, когда старая и новая схемы/компоненты работают одновременно | «Окно безопасной миграции» |

### Теория и правила

#### 1) `task_annotations` как функция

`task_annotations` позволяет динамически менять параметры задач:

- `rate_limit`,
- `time_limit`,
- `soft_time_limit`,
- `queue` и другие policy-аспекты.

Сильная сторона: централизованный governance без массового редактирования декораторов.

#### 2) Кастомный `Task` класс

Хуки:

- `__call__`
- `before_start`
- `on_success`
- `on_failure`
- `on_retry`
- `after_return`

Когда это лучше signals:

- когда нужен строгий контракт на уровне семейства задач;
- когда важна локальность поведения и тестируемость.

#### 3) Кастомные serializers/backends/loaders

Используются, когда стандартных вариантов недостаточно.  
Но это зона высокого риска:

- совместимость producer/consumer;
- миграции и version skew;
- security model (особенно сериализация).

Нужны:

- контракт формата;
- backward compatibility стратегия;
- интеграционные тесты на старой и новой версии.

##### Отдельно про custom backend

Кастомный backend оправдан, когда у тебя есть явное требование, которое не покрывают стандартные backend-и:

- обязательные audit-поля для compliance;
- строгие правила retention и правового удаления;
- нестандартная модель доступа к результатам (например, интеграция с внутренним secure storage).

Но цена высокая:

- нужно обеспечить корректную семантику состояний (`PENDING/STARTED/SUCCESS/FAILURE/...`);
- нужно тестировать под fan-out/fan-in сценариями (особенно chord-related нагрузки);
- нужно поддерживать backward compatibility API backend-а при обновлениях Celery.

##### Отдельно про custom loader

Custom loader нужен редко. Обычно достаточно штатных механизмов конфигурации.  
Loader имеет смысл, если требуется особая модель загрузки настроек (например, из централизованного конфиг-сервиса с внутренними политиками).

Риски custom loader:

- ломается предсказуемость старта app/worker;
- сложнее локальная отладка и onboarding новых инженеров;
- возрастает вероятность скрытого config drift между окружениями.

Практическое правило: custom loader вводится только с формальным ADR и rollback-планом.

#### Security-замечание для custom serializers

Даже если serializer технически удобен, он должен проходить security-review:

- можно ли безопасно десериализовать payload из недоверенной среды;
- есть ли риск RCE/инъекции;
- есть ли ограничение на размер и структуру payload;
- можно ли валидировать схему до обработки.

Практическое правило: если есть безопасный стандартный путь (например, JSON + явная валидация), он обычно предпочтительнее «умного» кастомного формата.

#### 4) Как выбрать точку расширения без оверинжиниринга

| Задача | Предпочтительная точка | Почему |
|---|---|---|
| добавить correlation/telemetry | signal | минимальное вмешательство |
| единая политика лимитов задач | `task_annotations` | централизованный control plane |
| общий lifecycle-контекст задач | custom `Task` class | локальная и тестируемая логика |
| инфраструктурное расширение consumer | bootstep | lifecycle-level кастомизация |
| нестандартный формат payload | custom serializer | контроль протокола обмена |

### Пошагово: выбор точки расширения

1. Сформулируй задачу расширения (например, централизованный rate limit).
2. Проверь минимальную подходящую точку:
   - policy -> `task_annotations`,
   - lifecycle конкретной задачи -> `Task` subclass,
   - инфраструктура worker -> bootstep,
   - наблюдаемость -> signals/events.
3. Зафиксируй риски совместимости.
4. Добавь тесты: unit + интеграция + upgrade path.
5. Подготовь rollback и feature-flag.
6. Убедись, что мониторинг покрывает новый слой (метрики + логи + error budget).

### Простыми словами

Не все задачи требуют «самого мощного крючка».  
Лучший hook — это самый простой, который решает проблему и не ломает архитектуру.

### Картинка в голове

Выбор hooks похож на выбор инструмента в мастерской:

- отвертка (`task_annotations`) для настройки параметров;
- набор спецключей (`Task` subclass) для повторяемой логики;
- промышленный станок (`bootsteps`) только для сложной инфраструктурной задачи.

### Как запомнить

**Сначала минимальный уровень вмешательства, потом всё остальное.**

### Примеры

#### Пример 1: `task_annotations` как функция

```python
def annotate(task):
    if task.name.startswith("billing."):
        return {"rate_limit": "20/m", "time_limit": 30, "soft_time_limit": 25}
    return {}

task_annotations = (annotate,)
```

#### Пример 2: кастомный базовый `Task`

```python
from celery import Task

class InstrumentedTask(Task):
    abstract = True

    def before_start(self, task_id, args, kwargs):
        self.app.log.get_default_logger().info("task_start id=%s name=%s", task_id, self.name)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.app.log.get_default_logger().error("task_failure id=%s exc=%s", task_id, exc)

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        self.app.log.get_default_logger().info("task_end id=%s status=%s", task_id, status)
```

#### Пример 3: где нужна осторожность с serializer

```text
Producer (new serializer v2) -> Broker -> Worker (old code expecting v1)
Result: decode error, retries, backlog growth, potential poison messages
```

#### Пример 4: безопасный план миграции serializer (упрощенно)

```text
Phase 1: workers умеют читать v1 + v2, producers still write v1
Phase 2: producers switch to v2, workers still read both
Phase 3: queue drained from v1 payloads
Phase 4: remove v1 read path
```

#### Пример 5: минимальный каркас custom Task backend (концептуально)

```text
class MyBackend(BaseBackend):
    - store_result(task_id, result, state, traceback, request)
    - get_task_meta(task_id)
    - cleanup/expire policy

Важно:
- хранить мета-данные консистентно со state machine Celery
- не блокировать worker path длительными backend-операциями
```

#### Пример 6: где custom loader может навредить

```text
Worker A loaded config from source v1
Worker B loaded config from source v2
Result: inconsistent routing/timeouts/retries across same deployment
```

### Практика / реальные сценарии

1. **Единая политика ограничений**: через `task_annotations` централизованно ограничить «дорогие» задачи.
2. **Базовый class для аудита**: корпоративный `BaseTask` с обязательным лог-контекстом.
3. **Serializer migration**: dual-read/dual-write стратегия до полного переключения.
4. **Custom backend для регуляторных требований**: хранение статусов с audit-полями и строгим retention.
5. **Custom loader для централизованного конфига**: внедрение только через ADR, canary и строгий drift-контроль.

### Типичные ошибки

- глобально переопределить параметры задач без документации, почему это сделано;
- использовать `Task.__call__` для тяжёлой логики, влияющей на latency;
- выкатывать custom serializer без совместимости со старыми сообщениями в очереди;
- создавать custom backend без стратегии очистки/retention.
- внедрять custom loader как «быстрый хак», не фиксируя источник истины конфигурации.

#### Что будет, если перепутать hooks

- Если bootstep использовать вместо `Task` subclass для прикладной логики — получишь избыточную инфраструктурную связность.
- Если signal использовать как главный слой бизнес-инвариантов — возрастет риск неявных дублей и сложных отказов.
- Если `task_annotations` применить без namespace-ограничений — можно «сломать» SLA чужих очередей.

### Что будет, если...

- **...включить агрессивные `task_annotations` для всех задач без сегментации?**  
  Возможна неожиданная деградация throughput и конфликт с уже настроенными queue/SLA профилями.

- **...менять serializer «на горячую» с непустой очередью?**  
  Высокий риск decode ошибок и застревания задач; нужна миграционная стратегия (связь с частью 30).

### Проверь себя

1. Когда `task_annotations` уместнее, чем правка каждой задачи вручную?
2. Почему `after_return` часто удобнее разрозненных хуков для финализации?
3. Какой главный риск у custom serializer/backend?

<details><summary>Ответ</summary>

1) Когда нужна единая политика для класса задач и важна централизованная управляемость.  
2) Он даёт единый путь финализации для разных исходов выполнения, снижая дублирование.  
3) Совместимость и операционная поддержка: версия формата, миграции, диагностика и rollback.

</details>

### Запомните

Выбор hook-а — архитектурное решение. Чем глубже точка вмешательства, тем выше ответственность за совместимость, тесты и эксплуатацию.

---
