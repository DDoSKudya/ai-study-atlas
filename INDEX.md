# AI Study Atlas — индекс базы

AI Study Atlas — база для самостоятельного изучения технических тем по структуре "направление -> трек -> план -> учебные части -> самопроверка".
Этот файл — основная точка входа: от него удобно начинать работу и к нему удобно возвращаться при навигации.

## Что находится в проекте

- `directions/` — учебные направления и треки.
- `prompts/` — рабочие промпты для сборки и улучшения материалов.
- `docs/` — правила ведения базы (контракт контента и именование).
- `CHANGELOG.md` — журнал изменений проекта.
- `README.md` — краткое описание идеи и формата проекта.

## Реестр направлений и треков

Ниже — рабочая таблица, которую удобно расширять по мере роста базы.
Один ряд = один трек.

| Направление     | Трек              | Путь                             | План |
| --------------- | ----------------- | -------------------------------- | ---- |
| Architecture    | Core Architecture | `directions/architecture/`       | [`mastery_plan.md`](directions/architecture/mastery_plan.md) |
| Backend         | Python            | `directions/backend/python/`     | [`mastery_plan.md`](directions/backend/python/mastery_plan.md) |
| CS Fundamentals | Databases         | `directions/cs_fundamentals/db/` | [`mastery_plan.md`](directions/cs_fundamentals/db/mastery_plan.md) |
| CS Fundamentals | Clean Code        | `directions/cs_fundamentals/clean_code/` | [`mastery_plan.md`](directions/cs_fundamentals/clean_code/mastery_plan.md) |
| Services        | Celery            | `directions/services/celery/`    | [`mastery_plan.md`](directions/services/celery/mastery_plan.md) |

### Шаблон новой строки

Скопируйте строку ниже и заполните поля:

`| <Direction> | <Track> | directions/<direction_slug>/<track_slug>/ | [mastery_plan.md](directions/<direction_slug>/<track_slug>/mastery_plan.md) |`

## Как проходить любой трек

1. Открыть `mastery_plan.md`.
2. Перейти в `pact/` и идти по частям в порядке плана.
3. В каждой части сначала изучить объяснение, затем пройти self-check.

## Рекомендуемый workflow по материалам

Базовый путь работы:

1. Сформировать/усилить общий план.
2. На основе плана создать учебные части.
3. Добавить и проверить self-check.
4. Сделать финальный аудит связности и структуры.

Подробный порядок запусков и итераций описан в:

- `prompts/HOW_TO_USE_PROMPTS.md`

## Рекомендуемый ридер

Для регулярной работы с Markdown-базой рекомендуется [study-md-desk](https://github.com/DDoSKudya/study-md-desk): удобная навигация по файлам, быстрые переходы и фокус на чтении длинных учебных материалов.

## Связанные документы

- `docs/content_contract.md` — требования к качеству и структуре учебного контента.
- `docs/naming_convention.md` — правила именования файлов и директорий.
- `CHANGELOG.md` — журнал изменений и план следующих итераций.
