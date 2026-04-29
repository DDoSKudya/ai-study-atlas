[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Вопросы для самопроверки

1. Почему современная Celery-практика начинается с platform engineering, а не с "написать побольше задач"?

<details><summary>Ответ</summary>

Потому что при росте нагрузки и сложности основная цена ошибок возникает в эксплуатации и архитектурных границах, а не в синтаксисе задач. Platform engineering делает систему предсказуемой и управляемой.

</details>

2. Что обязательно должно быть в SLO для фоновой системы?

<details><summary>Ответ</summary>

Минимум: lag/queue wait, success rate и end-to-end latency. Эти метрики напрямую отражают качество пользовательского и бизнес-потока.

</details>

3. Почему Kubernetes-контур Celery требует отдельного инженерного дизайна?

<details><summary>Ответ</summary>

Потому что pod lifecycle, probes, autoscaling и termination semantics существенно влияют на корректность выполнения задач и устойчивость системы.

</details>

4. Когда гибрид `Celery + workflow engine` оправдан?

<details><summary>Ответ</summary>

Когда orchestration-процессы требуют отдельного движка, а Celery эффективно исполняет отдельные шаги как execution layer.

</details>

5. Какой главный критерий зрелости после изучения части 26?

<details><summary>Ответ</summary>

Умение принимать архитектурные и эксплуатационные решения по Celery на основе class-fit, SLO и надежности, а не только на основе знакомого API.

</details>

---
