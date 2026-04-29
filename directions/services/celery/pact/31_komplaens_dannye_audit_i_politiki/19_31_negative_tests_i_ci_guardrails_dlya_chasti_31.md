[← Назад к индексу части](index.md)
[↑ К глобальному плану](../mastery_plan.md)

## Negative tests и CI-guardrails для части 31

Идея: комплаенс-проверки должны быть не только "в голове", но и в автоматике.

### Что проверять автоматически

| Проверка | Что ловит | Где запускать |
|---|---|---|
| Запрещенные поля в payload fixtures | случайная передача PII/PCI | unit/integration tests |
| Запрещенные паттерны в логах | утечки email/token/card в traceback | test + log scanning stage |
| Наличие audit-полей | пропуск `actor_id/request_id/task_id` | contract tests |
| Региональный роутинг | неверная очередь для tenant_region | integration tests |
| Наличие SBOM и vulnerability report | отсутствие supply-chain артефактов | CI release pipeline |

### Пример негативного теста (концептуально)

```python
def test_payment_task_payload_must_not_contain_card_data():
    payload = build_payment_task_payload(order_id="ORD-1", token="pay_tok_1")
    forbidden = {"card_number", "cvv", "pan"}
    assert forbidden.isdisjoint(payload.keys())
```

### Pre-release чек-лист по части 31

- проверены payload contract tests для чувствительных задач;
- подтверждены `result_expires` и retention-классы;
- протестированы legal hold и deletion workflow;
- проверена корреляция audit-событий в end-to-end сценарии;
- подтверждена региональная маршрутизация и отсутствие запрещенного cross-border;
- приложены актуальные SBOM + vulnerability report + решение по CVE.

#### Проверь себя: CI-guardrails и pre-release

1. Почему negative tests важны именно для комплаенса, а не только для функциональности?

<details><summary>Ответ</summary>

Они подтверждают отсутствие запрещенного поведения (например, утечки полей), которое не всегда видно в обычных "happy path" тестах.

</details>

2. Какой пункт pre-release чаще всего пропускают и чем это опасно?

<details><summary>Ответ</summary>

Часто пропускают end-to-end корреляцию аудита. В результате при инциденте сложно собрать непрерывную цепочку событий и доказательств.

</details>

---
