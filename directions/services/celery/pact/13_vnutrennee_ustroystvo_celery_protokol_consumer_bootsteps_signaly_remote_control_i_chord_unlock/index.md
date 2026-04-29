# Часть 13. Внутреннее устройство Celery: протокол, consumer pipeline, bootsteps, signals, remote control и chord unlock

> Навигационная страница части: используйте ее как точку входа и маршрут по подразделам.

[← Назад к глобальному плану](../../celery_mastery_plan.md)

## Навигация по части

- [Введение, маршрут и оглавление](00_vvedenie_marshrut_i_oglavlenie.md)
- [После этой части ты сможешь](01_13_posle_etoy_chasti_ty_smozhesh.md)
- [Что желательно знать заранее](02_13_chto_zhelatelno_znat_zaranee.md)
- [Краткая шпаргалка по терминам](03_13_kratkaya_shpargalka_po_terminam.md)
- [Маршрут изучения простыми словами](04_13_marshrut_izucheniya_prostymi_slovami.md)
- [Структура материала (что в какой группе)](05_13_struktura_materiala_chto_v_kakoy_gruppe.md)
- [Как устроены разделы и как пользоваться оглавлением](06_13_kak_ustroeny_razdely_i_kak_polzovatsya_oglavleniem.md)
- [Оглавление по этапам изучения](07_13_oglavlenie_po_etapam_izucheniya.md)
- [Карта соответствия глобальному плану (часть 13)](08_13_karta_sootvetstviya_globalnomu_planu_chast_13.md)
- [Следующий шаг после этой части](09_13_sleduyushchiy_shag_posle_etoy_chasti.md)
- [13.1. Как Celery устроен “под капотом”](10_13_13_1_kak_celery_ustroen_pod_kapotom.md)
- [13.2. Task message protocol: что лежит в очереди](11_13_13_2_task_message_protocol_chto_lezhit_v_ocheredi.md)
- [13.3. Consumer pipeline: от broker до pool](12_13_13_3_consumer_pipeline_ot_broker_do_pool.md)
- [13.4. Bootsteps: жизненный цикл worker и расширения](13_13_13_4_bootsteps_zhiznennyy_tsikl_worker_i_rasshireniya.md)
- [13.5. Signals: hooks для observability и инициализации](14_13_13_5_signals_hooks_dlya_observability_i_initsializatsii.md)
- [13.6. Remote control internals: inspect/control/broadcast](15_13_13_6_remote_control_internals_inspect_control_broadcast.md)
- [13.7. Chord internals: chord unlock и зависимость от backend](16_13_13_7_chord_internals_chord_unlock_i_zavisimost_ot_backend.md)
- [13.8. Internal debugging: как чинить странности](17_13_13_8_internal_debugging_kak_chinit_strannosti.md)
- [Финал. Справочник, сценарии, самопроверка, ошибки, резюме](18_13_final_spravochnik_stsenarii_samoproverka_oshibki_rezyume.md)

## Как читать эту часть

- Начните с введения и оглавления (`00_*`).
- Далее проходите тематические блоки (`01_*`, `02_*`, ...).
- Для возврата используйте ссылки вверху каждого подфайла.
