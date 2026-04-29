# Часть 9. Надёжность, идемпотентность и обработка ошибок

> Навигационная страница части: используйте ее как точку входа и маршрут по подразделам.

[← Назад к глобальному плану](../../celery_mastery_plan.md)

## Навигация по части

- [Введение, маршрут и оглавление](00_vvedenie_marshrut_i_oglavlenie.md)
- [После этой части ты сможешь](01_09_posle_etoy_chasti_ty_smozhesh.md)
- [Что желательно знать заранее](02_09_chto_zhelatelno_znat_zaranee.md)
- [Краткая шпаргалка по терминам](03_09_kratkaya_shpargalka_po_terminam.md)
- [Маршрут изучения простыми словами](04_09_marshrut_izucheniya_prostymi_slovami.md)
- [Структура материала (что в какой группе)](05_09_struktura_materiala_chto_v_kakoy_gruppe.md)
- [Как устроены разделы и как пользоваться оглавлением](06_09_kak_ustroeny_razdely_i_kak_polzovatsya_oglavleniem.md)
- [Оглавление по этапам изучения](07_09_oglavlenie_po_etapam_izucheniya.md)
- [Сквозная карта надёжности (как всё связано)](08_09_skvoznaya_karta_nadezhnosti_kak_vse_svyazano.md)
- [Карта соответствия глобальному плану (часть 9)](09_09_karta_sootvetstviya_globalnomu_planu_chast_9.md)
- [Следующий шаг после этой части](10_09_sleduyushchiy_shag_posle_etoy_chasti.md)
- [9.1. Идемпотентность как базовый принцип](11_09_9_1_idempotentnost_kak_bazovyy_printsip.md)
- [9.2. Классификация ошибок](12_09_9_2_klassifikatsiya_oshibok.md)
- [9.3. Retry-стратегия](13_09_9_3_retry_strategiya.md)
- [9.4. Таймауты и ограничения выполнения](14_09_9_4_taymauty_i_ogranicheniya_vypolneniya.md)
- [9.5. Компенсации и транзакционные границы](15_09_9_5_kompensatsii_i_tranzaktsionnye_granitsy.md)
- [9.6. Poison tasks и bad payloads](16_09_9_6_poison_tasks_i_bad_payloads.md)
- [9.7. Дубли и race conditions](17_09_9_7_dubli_i_race_conditions.md)
- [9.8. Отмена, отзыв и мягкая остановка](18_09_9_8_otmena_otzyv_i_myagkaya_ostanovka.md)
- [9.9. Частично применённые побочные эффекты](19_09_9_9_chastichno_primenennye_pobochnye_effekty.md)
- [Справочник по части](20_09_spravochnik_po_chasti.md)
- [Частые сценарии](21_09_chastye_stsenarii.md)
- [Вопросы для самопроверки](22_09_voprosy_dlya_samoproverki.md)
- [Типичные ошибки в части](23_09_tipichnye_oshibki_v_chasti.md)
- [Анти-паттерны (чего лучше не делать)](24_09_anti_patterny_chego_luchshe_ne_delat.md)
- [Резюме части](25_09_rezyume_chasti.md)

## Как читать эту часть

- Начните с введения и оглавления (`00_*`).
- Далее проходите тематические блоки (`01_*`, `02_*`, ...).
- Для возврата используйте ссылки вверху каждого подфайла.
