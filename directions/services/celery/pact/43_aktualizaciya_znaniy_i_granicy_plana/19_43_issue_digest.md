[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Issue digest
- Link:
- Affected versions:
- Transport/backend context:
- Symptom in issue:
- Does our stack match? (yes/no/partially):
- Workaround:
- Fixed in:
- Decision for our rollout:
```

**Почему важно:** без такого мини-формата обсуждение issues остаётся «прочитал и забыл», а не становится входом в решение.

#### Проверь себя: issue digest

1. Почему поле `Does our stack match?` должно быть обязательным, а не «по желанию»?
2. Какая ошибка чаще всего возникает, если в digest не указать `Fixed in`?
3. Как digest помогает в postmortem, если инцидент всё же случился?

<details><summary>Ответ</summary>

1. Без него команда не отделит релевантные баги от нерелевантных и начнёт тратить время на ложные следы.
2. Команда не понимает, лечится ли проблема апгрейдом или нужен workaround, и может зафиксироваться на неверной стратегии.
3. Он даёт контекст, какие риски были известны заранее, что было решено и где процесс сработал/не сработал.

</details>

---

<a id="uglublenie-adr-template"></a>
