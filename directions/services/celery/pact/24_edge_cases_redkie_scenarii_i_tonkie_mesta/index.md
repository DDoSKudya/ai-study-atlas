# Часть 24. Edge cases, редкие сценарии и тонкие места

> Навигационная страница части: используйте ее как точку входа и маршрут по подразделам.

[← Назад к глобальному плану](../../mastery_plan.md)

## Навигация по части

- [Введение, маршрут и оглавление](00_vvedenie_marshrut_i_oglavlenie.md)
- [После этой части ты сможешь](01_24_posle_etoy_chasti_ty_smozhesh.md)
- [Что желательно знать заранее](02_24_chto_zhelatelno_znat_zaranee.md)
- [Краткая шпаргалка по терминам](03_24_kratkaya_shpargalka_po_terminam.md)
- [Маршрут изучения простыми словами](04_24_marshrut_izucheniya_prostymi_slovami.md)
- [Структура материала (что в какой группе)](05_24_struktura_materiala_chto_v_kakoy_gruppe.md)
- [Как устроены разделы и как пользоваться оглавлением](06_24_kak_ustroeny_razdely_i_kak_polzovatsya_oglavleniem.md)
- [Оглавление по этапам изучения](07_24_oglavlenie_po_etapam_izucheniya.md)
- [Карта соответствия глобальному плану](08_24_karta_sootvetstviya_globalnomu_planu.md)
- [Сквозная модель edge-case риска](09_24_skvoznaya_model_edge_case_riska.md)
- [Следующий шаг после этой части](10_24_sleduyushchiy_shag_posle_etoy_chasti.md)
- [24.1 Долгоживущие задачи](11_24_24_1_dolgozhivushchie_zadachi.md)
- [24.2 Очень большие payload](12_24_24_2_ochen_bolshie_payload.md)
- [24.3 Версионные несовместимости](13_24_24_3_versionnye_nesovmestimosti.md)
- [24.4 Часовые пояса и календарные эффекты](14_24_24_4_chasovye_poyasa_i_kalendarnye_effekty.md)
- [24.5 Падение внешней зависимости во время массового retry](15_24_24_5_padenie_vneshney_zavisimosti_vo_vremya_massovogo_retry.md)
- [24.6 Гонка producer vs consumer state](16_24_24_6_gonka_producer_vs_consumer_state.md)
- [24.7 Celery в гибридных environments](17_24_24_7_celery_v_gibridnykh_environments.md)
- [24.8 OOM, cgroups и лимиты контейнеров](18_24_24_8_oom_cgroups_i_limity_konteynerov.md)
- [24.9 Часы и синхронизация времени](19_24_24_9_chasy_i_sinkhronizatsiya_vremeni.md)
- [Практический runbook: как диагностировать edge-case инцидент](20_24_prakticheskiy_runbook_kak_diagnostirovat_edge_case_intsident.md)
- [Checklist полноты по части 24 (самоаудит команды)](21_24_checklist_polnoty_po_chasti_24_samoaudit_komandy.md)
- [Сравнение подходов в спорных местах (быстрый выбор)](22_24_sravnenie_podkhodov_v_spornykh_mestakh_bystryy_vybor.md)
- [Антипример: как выглядит плохой edge-case дизайн](23_24_antiprimer_kak_vyglyadit_plokhoy_edge_case_dizayn.md)
- [Мини-практикум: 3 коротких кейса](24_24_mini_praktikum_3_korotkikh_keysa.md)
- [Справочник по части](25_24_spravochnik_po_chasti.md)
- [Частые сценарии](26_24_chastye_stsenarii.md)
- [Вопросы для самопроверки](27_24_voprosy_dlya_samoproverki.md)
- [Типичные ошибки по части](28_24_tipichnye_oshibki_po_chasti.md)
- [Резюме части 24](29_24_rezyume_chasti_24.md)

## Как читать эту часть

- Начните с введения и оглавления (`00_*`).
- Далее проходите тематические блоки (`01_*`, `02_*`, ...).
- Для возврата используйте ссылки вверху каждого подфайла.
