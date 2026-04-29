[← Назад к индексу части](index.md)
[↑ К глобальному плану](../celery_mastery_plan.md)

## Исчерпывающая матрица имен опций (покрытие 36.1-36.10)

Ниже — тот самый "инвентарный слой", который нужен по мастер-плану: не только концепции, но и полный перечень категорий и имен параметров, с которыми команда реально работает в `celeryconfig`.

> Важно: конкретные дефолты и доступность некоторых ключей зависят от версии Celery и транспорта. Поэтому в таблицах акцент на **что проверять и зачем**, а финальную валидацию делать по документации вашей целевой версии (связка с частью `43`).

### 1) `36.1` Приложение и обнаружение задач

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `imports` | Явный импорт модулей задач | `inspect registered` одинаков на всех worker |
| `include` | Дополнительные модули задач | при старте нет `Received unregistered task` |
| `autodiscover_tasks` | Автопоиск задач по пакетам | структура пакетов единообразна |
| `timezone` | Бизнес-таймзона для scheduler/ETA | cron/interval корректны в нужной TZ |
| `enable_utc` | Работа времени в UTC | логи/метрики/ETA не конфликтуют по времени |

### 2) `36.2` Брокер и соединения

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `broker_url` | Основной endpoint брокера | publish и consume проходят в baseline |
| `broker_read_url` | URL чтения (consumer) | worker стабильно читает при split topology |
| `broker_write_url` | URL записи (producer) | producer публикует при read/write split |
| `broker_connection_retry` | retry подключения | временный outage не валит процесс сразу |
| `broker_connection_retry_on_startup` | retry на старте | worker/producer поднимаются после короткого outage |
| `broker_connection_max_retries` | лимит retry | нет бесконечного storm без алерта |
| `broker_pool_limit` | размер пула соединений | нет fd pressure и лишних reconnect |
| `broker_heartbeat` | heartbeat AMQP-сессий | обрыв соединения обнаруживается вовремя |
| `broker_channel_error_retry` | retry при channel-level ошибках | channel reset не приводит к долгой деградации |
| `broker_transport_options` | transport-specific параметры | ключи валидны для текущего транспорта |
| `broker_use_ssl` | TLS к брокеру | сертификаты валидируются, MITM-риски снижены |
| `broker_login_method` | метод аутентификации | соответствует политике брокера |
| `broker_failover_strategy` | стратегия failover endpoint-ов | predictable порядок переключения |

### 3) `36.3` Задачи: дефолты и политика

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `task_serializer` | формат task payload | только допустимые форматы в проде |
| `result_serializer` | формат результата | читается клиентами и backend без конфликтов |
| `accept_content` | whitelist входящих форматов | небезопасные serializer отключены |
| `task_compression` | компрессия task payload | баланс CPU и network |
| `result_compression` | компрессия result payload | снижение трафика без перегруза CPU |
| `task_protocol` | версия task protocol | producer/worker совместимы |
| `task_acks_late` | ack после выполнения | идемпотентность реально обеспечена |
| `task_reject_on_worker_lost` | redelivery при потере worker | нет silent loss при crash |
| `task_ignore_result` | хранить ли результат | backend не раздувается лишними данными |
| `task_track_started` | состояние STARTED | есть прозрачный progress state |
| `task_send_sent_event` | событие отправки | publish-стадия видна мониторингу |
| `task_store_eager_result` | результат в eager mode | unit/integration test не расходятся по ожиданиям |
| `task_time_limit` | hard limit выполнения | runaway задачи ограничены |
| `task_soft_time_limit` | soft limit выполнения | graceful cleanup в задаче работает |
| `task_default_rate_limit` | дефолт throttling | нет перегруза downstream API |
| `task_max_retries` | лимит retry задачи | retry storm ограничен |
| `task_default_retry_delay` | базовый интервал retry | retry cadence согласован с SLA |
| `task_publish_retry` | retry publish | публикация устойчива к кратким сбоям |
| `task_publish_retry_policy` | стратегия publish retry | retry bounded и предсказуем |
| `task_remote_tracebacks` | remote traceback детали | диагностика богаче, но контролируема по данным |
| `task_eager_propagates` | propagate исключений в eager | тесты не скрывают ошибки |
| `task_always_eager` | локальное выполнение задач | строго только в тест/локалке |
| `task_eager_limit` | ограничения eager-режима (если доступно) | eager не имитирует прод-семантику |
| `task_annotations` | map переопределений по задачам | policy централизована и не размазана |
| `task_routes` | маршрутизация по очередям | классы задач изолированы |
| `task_queue_max_priority` | максимум приоритета очередей | согласовано с транспортом/очередями |
| `task_default_priority` | дефолтный приоритет задач | нет "случайного" starvation |
| `task_default_delivery_mode` | transient/persistent delivery mode | durability согласована с SLA |
| `task_queues` | явное описание очередей | очереди описаны и проверяемы |
| `task_create_missing_queues` | авто-создание очередей | исключены неожиданные "случайные" очереди |
| `task_default_queue` | дефолтная очередь | fallback понятен и контролируем |
| `task_default_exchange` | дефолтный exchange | маршрутизация предсказуема |
| `task_default_exchange_type` | тип exchange | соответствует маршрутизационной модели |
| `task_default_routing_key` | дефолт routing key | нет "размывания" трафика |
| `task_inherit_parent_priority` | наследование приоритета в цепочках | canvas ведет себя ожидаемо |
| `task_queue_ha_policy` | legacy HA policy (где применимо) | используется только осознанно и по версии |

### 4) `36.4` Worker

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `worker_prefetch_multiplier` | жадность резервирования задач | fairness и latency сбалансированы |
| `worker_concurrency` | параллелизм worker | нет oversubscription CPU/RAM |
| `worker_pool` | модель пула | подходит природе workload |
| `worker_pool_restarts` | перезапуск pool через control | recovery/maintenance возможны без full restart |
| `worker_max_tasks_per_child` | recycle child по count | утечки "обрезаются" по циклу |
| `worker_max_memory_per_child` | recycle child по memory | runaway memory ограничена |
| `worker_disable_rate_limits` | отключение rate limits | включается только осознанно |
| `worker_state_db` | persisted state worker | revoke/state не теряются при restart |
| `worker_timer_precision` | точность internal timer | ETA/timer jitter в допустимых пределах |
| `worker_log_format` | формат логов worker | удобный парсинг/корреляция |
| `worker_task_log_format` | формат task-логов | есть task_id/task_name в каждой строке |
| `worker_log_color` | цветной вывод | только для локальной диагностики |
| `worker_hijack_root_logger` | перехват root logger | logging stack не ломается |
| `worker_redirect_stdouts` | redirect stdout/stderr | не теряются print/trace output |
| `worker_redirect_stdouts_level` | уровень redirected логов | шум контролируется |
| `worker_send_task_events` | генерация событий task lifecycle | observability соответствует цели |
| `worker_enable_remote_control` | доступность remote control | ограничено сетью/ролью |
| `worker_direct` | direct queue per worker (где нужно) | точечная маршрутизация работает |
| `worker_cancel_long_running_tasks_on_connection_loss` | отмена долгих задач при потере broker | риск двойного выполнения контролируется |
| `worker_proc_alive_timeout` | ожидание живости child process | startup/restart не зависают |
| `worker_lost_wait` | ожидание при потере worker процесса | recovery path предсказуем |
| `worker_deduplicate_successful_tasks` | дедуп успешно завершенных задач (если доступно) | риск повторной обработки снижен |
| `worker_consumer` | custom consumer class | расширение управляемо и протестировано |
| `worker_pool_putlocks` | lock при put в pool | конкурентный доступ корректен |
| `worker_autoscaler` | custom autoscaler class | масштабирование контролируется политикой |

### 5) `36.5` Beat и периодика

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `beat_schedule` | расписания задач | расписание соответствует бизнес-календарю |
| `beat_scheduler` | класс scheduler | выбранный backend scheduler стабилен |
| `beat_schedule_filename` | файл scheduler state | перезапуск не создает хаос |
| `beat_sync_every` | частота sync state | потери state минимальны |
| `beat_max_loop_interval` | шаг цикла beat | точность vs нагрузка сбалансированы |
| `beat_cron_starting_deadline` | окно допустимого старта cron (по версии) | после downtime нет нежелательных догонов |
| `beat_cron_end_deadline` | окно завершения cron (по версии) | просроченные окна корректно отбрасываются |
| `beat_init_callback` | init hook beat | кастомная инициализация предсказуема |

### 6) `36.6` Result backend

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `result_backend` | тип backend | доступность и latency в целевых пределах |
| `result_backend_transport_options` | transport-specific backend options | опции валидны для backend-драйвера |
| `result_expires` | TTL результатов | рост хранилища ограничен |
| `result_extended` | расширенные result meta | observability полезна, cost приемлем |
| `result_chord_join_timeout` | timeout ожидания chord join | нет бесконечного ожидания callback |
| `result_chord_retry_interval` | шаг retry join | chord recovery предсказуем |
| `result_backend_always_retry` | retry операций backend | краткие сбои backend не роняют поток |
| `result_serializer` | формат сериализации result | совместимость чтения результата |
| `result_compression` | компрессия результата | network/storage оптимизированы |
| `result_cache_max` | кэш чтения result | memory footprint контролируется |

### 7) `36.7` События и мониторинг

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `event_queue_expires` | время жизни event queue | "мертвые" очереди не копятся |
| `event_queue_ttl` | TTL event messages | служебные сообщения не раздувают контур |
| `event_queue_prefix` | namespace событий | изоляция окружений/сервисов |
| `event_serializer` | формат event payload | tooling читает события стабильно |
| `event_queue_persistent` | persistence event queue | durable/non-durable выбрано осознанно |
| `worker_send_task_events` | task events от worker | хватает данных для RCA |
| `task_send_sent_event` | publish sent event | виден ранний этап lifecycle |

### 8) `36.8` Безопасность

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `security_key` | приватный ключ подписи | ключ хранится в secret manager |
| `security_certificate` | сертификат подписи | цепочка доверия валидна |
| `security_cert_store` | trust store сертификатов | только доверенные certs |
| `security_digest` | digest алгоритм | соответствует security policy |

### 9) `36.9` Тесты и отладка

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `task_always_eager` | локальное выполнение задач | включено только в test/dev |
| `task_eager_propagates` | проброс ошибок eager | падения не маскируются |
| `task_store_eager_result` | result в eager | тесты на чтение статусов валидны |
| `worker_hijack_root_logger` | интеграция логирования в dev | dev UX удобен без порчи prod-logging |

### 10) `36.10` Прочее и редкое

| Опция | Что контролирует | Практическая проверка |
|---|---|---|
| `enable_remote_control` | legacy/alias управления control plane | semantics совпадает с профилем безопасности |
| `control_queue_ttl` | TTL control сообщений | control queue не разрастается |
| `control_queue_expires` | expiration control queue | stale control queue удаляются |
| `redis_backend_use_ssl` | TLS для Redis backend | backend traffic защищен |
| deprecated names | миграционный риск | checklist апгрейда обязателен перед релизом |

#### Проверь себя: матрица опций

1. Почему важно иметь именно "таблицу имен опций", если уже есть объяснения принципов?
2. Какие 3 группы опций чаще всего конфликтуют между собой при внедрении?
3. Как использовать эту матрицу в PR-ревью конфигурации?

<details><summary>Ответ</summary>

1) Потому что в боевой работе обсуждают не только идеи, но конкретные ключи; таблица снижает риск пропустить критичный параметр.  
2) Task policy (`ack/retry/time limits`), worker runtime (`prefetch/pool/concurrency`) и transport/backend options (`visibility timeout/retry/TLS`).  
3) Делать чек "измененная опция -> категория -> влияние -> метрика проверки -> rollback plan", а не принимать изменение по принципу "выглядит разумно".

</details>

---
