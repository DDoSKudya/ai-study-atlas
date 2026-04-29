# Часть 36. Матрица конфигурации (исчерпывающие категории настроек)

> Навигационная страница части: используйте ее как точку входа и маршрут по подразделам.

[← Назад к глобальному плану](../../celery_mastery_plan.md)

## Навигация по части

- [Введение, маршрут и оглавление](00_vvedenie_marshrut_i_oglavlenie.md)
- [После этой части ты сможешь](01_36_posle_etoy_chasti_ty_smozhesh.md)
- [Что желательно знать заранее](02_36_chto_zhelatelno_znat_zaranee.md)
- [Краткая шпаргалка по терминам](03_36_kratkaya_shpargalka_po_terminam.md)
- [Маршрут изучения простыми словами](04_36_marshrut_izucheniya_prostymi_slovami.md)
- [Структура материала (что в какой группе)](05_36_struktura_materiala_chto_v_kakoy_gruppe.md)
- [Как устроены разделы и как пользоваться оглавлением](06_36_kak_ustroeny_razdely_i_kak_polzovatsya_oglavleniem.md)
- [Оглавление по этапам изучения](07_36_oglavlenie_po_etapam_izucheniya.md)
- [Карта соответствия глобальному плану](08_36_karta_sootvetstviya_globalnomu_planu.md)
- [Сквозная карта влияния конфигурации](09_36_skvoznaya_karta_vliyaniya_konfiguratsii.md)
- [Быстрый вход для слабоподготовленного читателя](10_36_bystryy_vkhod_dlya_slabopodgotovlennogo_chitatelya.md)
- [Следующий шаг после этой части](11_36_sleduyushchiy_shag_posle_etoy_chasti.md)
- [36.1 Приложение и обнаружение задач](12_36_36_1_prilozhenie_i_obnaruzhenie_zadach.md)
- [36.2 Брокер и соединения](13_36_36_2_broker_i_soedineniya.md)
- [36.3 Задачи: дефолты и политика](14_36_36_3_zadachi_defolty_i_politika.md)
- [36.4 Worker](15_36_36_4_worker.md)
- [36.5 Beat и периодика](16_36_36_5_beat_i_periodika.md)
- [36.6 Result backend](17_36_36_6_result_backend.md)
- [36.7 События и мониторинг](18_36_36_7_sobytiya_i_monitoring.md)
- [36.8 Безопасность](19_36_36_8_bezopasnost.md)
- [36.9 Тесты и отладка](20_36_36_9_testy_i_otladka.md)
- [36.10 Прочее и редкое](21_36_36_10_prochee_i_redkoe.md)
- [Исчерпывающая матрица имен опций (покрытие 36.1-36.10)](22_36_ischerpyvayushchaya_matritsa_imen_optsiy_pokrytie_36_1_36_10.md)
- [Алгоритм безопасного изменения конфигурации (production playbook)](23_36_algoritm_bezopasnogo_izmeneniya_konfiguratsii_production_playbook.md)
- [Матрица зависимостей и конфликтов между категориями](24_36_matritsa_zavisimostey_i_konfliktov_mezhdu_kategoriyami.md)
- [Базовые конфигурационные профили (готовые стартовые шаблоны)](25_36_bazovye_konfiguratsionnye_profili_gotovye_startovye_shablony.md)
- [Decision flow: как выбрать направление настройки](26_36_decision_flow_kak_vybrat_napravlenie_nastroyki.md)
- [Финальный чек-лист полноты покрытия части 36](27_36_finalnyy_chek_list_polnoty_pokrytiya_chasti_36.md)
- [Диагностическая карта: симптом -> где смотреть в конфиге -> что делать](28_36_diagnosticheskaya_karta_simptom_gde_smotret_v_konfige_chto_delat.md)
- [Источники конфигурации и приоритеты (чтобы не ловить config drift)](29_36_istochniki_konfiguratsii_i_prioritety_chtoby_ne_lovit_config_drift.md)
- [Протокол миграции deprecated/renamed опций (безболезненный апгрейд)](30_36_protokol_migratsii_deprecated_renamed_optsiy_bezboleznennyy_apgreyd.md)
- [Каталог анти-паттернов конфигурации (с последствиями и исправлением)](31_36_katalog_anti_patternov_konfiguratsii_s_posledstviyami_i_ispravleniem.md)
- [Pre-release audit чек-лист конфигурации Celery](32_36_pre_release_audit_chek_list_konfiguratsii_celery.md)
- [Сквозной сценарий: клиент -> API -> Celery -> статус задачи](33_36_skvoznoy_stsenariy_klient_api_celery_status_zadachi.md)
- [Карта rollback-решений при неудачном rollout конфигурации](34_36_karta_rollback_resheniy_pri_neudachnom_rollout_konfiguratsii.md)
- [Справочник по части](35_36_spravochnik_po_chasti.md)
- [Частые сценарии](36_36_chastye_stsenarii.md)
- [Вопросы для самопроверки](37_36_voprosy_dlya_samoproverki.md)
- [Типичные ошибки по части](38_36_tipichnye_oshibki_po_chasti.md)
- [Резюме части 36](39_36_rezyume_chasti_36.md)

## Как читать эту часть

- Начните с введения и оглавления (`00_*`).
- Далее проходите тематические блоки (`01_*`, `02_*`, ...).
- Для возврата используйте ссылки вверху каждого подфайла.
