,,# Введение в ООП. Домашнее задание

## Описание задачи

Реализуйте класс Item в `src/item.py` для представления товара в магазине. 

Экземпляр класса `Item` содержит атрибуты:

- название товара
- цена за единицу товара
- количество товара в магазине

Класс `Item` поддерживает два атрибута класса:

- для хранения уровня цен с учетом скидки (например, 0.85, при скидке 15%)
- для хранения созданных экземпляров класса

Реализуйте методы, позволяющие:

- получить общую стоимость конкретного товара в магазине
- применить установленную скидку для конкретного товара

Тестирование:
- Напишите тесты в `tests/test_item.py`

## Ожидаемое поведение
- Код в файле `main.py` должен выдавать ожидаемые значения