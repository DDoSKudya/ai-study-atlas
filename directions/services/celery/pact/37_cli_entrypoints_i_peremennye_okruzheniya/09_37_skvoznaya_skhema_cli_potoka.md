[← Назад к индексу части](index.md)
[↑ К глобальному плану](../../mastery_plan.md)

## Сквозная схема CLI-потока

```mermaid
flowchart LR
    A[Shell command] --> B[Global flags\n-A --config --workdir]
    B --> C[Celery app loading\nentrypoint + config]
    C --> D[Subcommand parsing\nworker/beat/inspect/...]
    D --> E[Runtime action\nstart worker / send control / inspect]
    E --> F[Broker + Worker + Backend side effects]
    G[Environment vars\nCELERY_*] --> C
    G --> D
```

Интуиция по схеме:

- сначала CLI должен понять, **какое приложение** ты хочешь запустить;
- затем подхватывается контекст (`config`, `workdir`, env);
- только после этого интерпретируется подкоманда и её флаги;
- операционные эффекты происходят уже в связке с брокером и worker-ами.

---
