# Часть 4. Архитектура Celery: компоненты и их взаимодействие

> Навигационная страница части: используйте ее как точку входа и маршрут по подразделам.

[← Назад к глобальному плану](../../celery_mastery_plan.md)

## Навигация по части

- [Введение, маршрут и оглавление](00_vvedenie_marshrut_i_oglavlenie.md)
- [После этой части ты сможешь](01_04_posle_etoy_chasti_ty_smozhesh.md)
- [Что желательно знать заранее](02_04_chto_zhelatelno_znat_zaranee.md)
- [Краткая шпаргалка по терминам](03_04_kratkaya_shpargalka_po_terminam.md)
- [Маршрут изучения простыми словами](04_04_marshrut_izucheniya_prostymi_slovami.md)
- [Структура материала](05_04_struktura_materiala.md)
- [Как устроены разделы и как пользоваться оглавлением](06_04_kak_ustroeny_razdely_i_kak_polzovatsya_oglavleniem.md)
- [Оглавление по этапам изучения](07_04_oglavlenie_po_etapam_izucheniya.md)
- [Карта соответствия глобальному плану (часть 4)](08_04_karta_sootvetstviya_globalnomu_planu_chast_4.md)
- [Следующий шаг после этой части](09_04_sleduyushchiy_shag_posle_etoy_chasti.md)
- [4.1. Producer, broker, worker, result backend](10_04_4_1_producer_broker_worker_result_backend.md)
- [4.2. Message flow end-to-end](11_04_4_2_message_flow_end_to_end.md)
- [4.3. Роль Kombu](12_04_4_3_rol_kombu.md)
- [4.4. Result backend как отдельная подсистема](13_04_4_4_result_backend_kak_otdelnaya_podsistema.md)
- [4.5. Event system и remote control](14_04_4_5_event_system_i_remote_control.md)
- [4.6. Разделение зон отказа](15_04_4_6_razdelenie_zon_otkaza.md)
- [Ключевые тезисы (зафиксировать в контенте как короткие тезисы)](16_04_klyuchevye_tezisy_zafiksirovat_v_kontente_kak_korotkie_tezisy.md)
- [Справочник по части 4](17_04_spravochnik_po_chasti_4.md)
- [Частые сценарии](18_04_chastye_stsenarii.md)
- [Вопросы для самопроверки по части 4](19_04_voprosy_dlya_samoproverki_po_chasti_4.md)
- [Типичные ошибки и антипаттерны](20_04_tipichnye_oshibki_i_antipatterny.md)
- [Резюме части 4](21_04_rezyume_chasti_4.md)

## Как читать эту часть

- Начните с введения и оглавления (`00_*`).
- Далее проходите тематические блоки (`01_*`, `02_*`, ...).
- Для возврата используйте ссылки вверху каждого подфайла.
