# Часть 5. Модель задач и API Celery

> Навигационная страница части: используйте ее как точку входа и маршрут по подразделам.

[← Назад к глобальному плану](../../celery_mastery_plan.md)

## Навигация по части

- [Введение, маршрут и оглавление](00_vvedenie_marshrut_i_oglavlenie.md)
- [После этой части ты сможешь](01_05_posle_etoy_chasti_ty_smozhesh.md)
- [Что желательно знать заранее](02_05_chto_zhelatelno_znat_zaranee.md)
- [Краткая шпаргалка по терминам](03_05_kratkaya_shpargalka_po_terminam.md)
- [Маршрут изучения простыми словами](04_05_marshrut_izucheniya_prostymi_slovami.md)
- [Структура материала](05_05_struktura_materiala.md)
- [Как устроены разделы и как пользоваться оглавлением](06_05_kak_ustroeny_razdely_i_kak_polzovatsya_oglavleniem.md)
- [Оглавление по этапам изучения](07_05_oglavlenie_po_etapam_izucheniya.md)
- [Карта API: от кода до сообщения](08_05_karta_api_ot_koda_do_soobshcheniya.md)
- [Карта соответствия глобальному плану (часть 5)](09_05_karta_sootvetstviya_globalnomu_planu_chast_5.md)
- [Следующий шаг после этой части](10_05_sleduyushchiy_shag_posle_etoy_chasti.md)
- [5.1. Декларация задач](11_05_5_1_deklaratsiya_zadach.md)
- [5.2. Вызов задач](12_05_5_2_vyzov_zadach.md)
- [5.3. Сигнатуры и сериализуемость](13_05_5_3_signatury_i_serializuemost.md)
- [5.4. Контекст задачи (`self.request`)](14_05_5_4_kontekst_zadachi_self_request.md)
- [5.5. Состояния и ошибки](15_05_5_5_sostoyaniya_i_oshibki.md)
- [5.6. Опции задач](16_05_5_6_optsii_zadach.md)
- [5.7. Заголовки, приоритет, routing key в `apply_async`](17_05_5_7_zagolovki_prioritet_routing_key_v_apply_async.md)
- [5.8. Идентичность и дедупликация на уровне приложения](18_05_5_8_identichnost_i_deduplikatsiya_na_urovne_prilozheniya.md)
- [5.9. Замена задачи и отмена](19_05_5_9_zamena_zadachi_i_otmena.md)
- [5.10. Локальный вызов и отладка](20_05_5_10_lokalnyy_vyzov_i_otladka.md)
- [Справочник по части](21_05_spravochnik_po_chasti.md)
- [Частые сценарии](22_05_chastye_stsenarii.md)
- [Вопросы для самопроверки (сводно)](23_05_voprosy_dlya_samoproverki_svodno.md)
- [Типичные ошибки (агрегировано из плана)](24_05_tipichnye_oshibki_agregirovano_iz_plana.md)
- [Анти-паттерны из глобального плана (развёрнуто)](25_05_anti_patterny_iz_globalnogo_plana_razvernuto.md)
- [Резюме части](26_05_rezyume_chasti.md)

## Как читать эту часть

- Начните с введения и оглавления (`00_*`).
- Далее проходите тематические блоки (`01_*`, `02_*`, ...).
- Для возврата используйте ссылки вверху каждого подфайла.
