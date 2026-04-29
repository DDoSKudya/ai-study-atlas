[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## RACI для части 31 (кто за что отвечает)

Чтобы не было "все думали, что это делает кто-то другой", полезно фиксировать зону ответственности.

| Направление | R (делает) | A (отвечает) | C (консультирует) | I (информируется) |
|---|---|---|---|---|
| Политика payload и токенизация | Backend team | Tech lead | Security | Product/Support |
| Retention и deletion workflow | Platform/Data ops | Engineering manager | Compliance/Legal | Backend teams |
| Audit schema и корреляция | Backend + SRE | Tech lead | Compliance | Incident manager |
| Резидентность и региональный роутинг | Platform/SRE | Platform lead | Security/Legal | Backend teams |
| SBOM/CVE процесс | Security + Platform | Security lead | Backend lead | Release manager |

Практический эффект RACI: меньше серых зон в инцидентах и быстрее прохождение аудита.

#### Проверь себя: RACI

1. Что чаще ломается без роли `A (отвечает)` даже при наличии `R (делает)`?

<details><summary>Ответ</summary>

Финальное принятие решений и эскалация. Работы могут выполняться, но без владельца ответственности спорные случаи "зависают".

</details>

2. Почему RACI особенно важен для legal hold и deletion?

<details><summary>Ответ</summary>

Потому что эти процессы пересекают инженерные, правовые и операционные контуры; без явных ролей велик риск противоречивых действий.

</details>

---
