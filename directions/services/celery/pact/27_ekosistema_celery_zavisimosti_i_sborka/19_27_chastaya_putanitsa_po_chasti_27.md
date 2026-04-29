[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Частая путаница по части 27

| Путают | Как правильно | Практический критерий |
|---|---|---|
| **"Celery обновили"** и **"стек обновлён корректно"** | Обновляется весь связанный контур: Celery/Kombu/Billiard/transport deps | есть lock-diff и canary-результат |
| **"image собрался"** и **"image безопасен и воспроизводим"** | Нужны SBOM, scan-gates, единый lock-source | сборка проходит policy checks, а не только `docker build` |
| **"локально работает"** и **"совместимо с CI/production"** | Нужен parity окружений и transport-aware тест | одинаковый dependency source в локальной и CI среде |
| **"extra установлен"** и **"фича production-ready"** | Extra — это только начало, дальше идут IAM/таймауты/retry semantics/runbook | есть integration test + owner + rollback plan |

### Проверь себя: частая путаница

1. Почему “зелёный unit-тест” не подтверждает готовность dependency-обновления к production?

<details><summary>Ответ</summary>

Unit-тест подтверждает локальную корректность кода, но не проверяет transport/runtime-совместимость, нагрузочный профиль и поведение в реальном контуре брокера.

</details>

2. Что означает “parity окружений” в контексте части 27?

<details><summary>Ответ</summary>

Это совпадение ключевых условий сборки и запуска между локальной, CI и production средой: версия Python, lock-source, важные runtime-параметры и transport-профиль.

</details>

---
