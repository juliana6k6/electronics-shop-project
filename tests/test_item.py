"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


item1 = Item("Смартфон", 1000, 20)
item2 = Item("Планшет", 10000, 2)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 20000
    assert item2.calculate_total_price() == 20000


def test_apply_discount():
    Item.pay_rate = 0.5
    item1.apply_discount()
    assert item1.price == 500
    item2.apply_discount()
    assert item2.price == 5000


item = Item('Телефон', 10000, 5)


def test_name1():
    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

def test_name2():
    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name == 'Суперсмарт'

def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам


@pytest.mark.parametrize('num', ['5', '5.0', '5.5'])
def test_string_to_number(num):
    assert Item.string_to_number(num) == 5


def test_repr():
    item3 = Item("Телевизор", 10000, 2)
    item4 = Item("Ноутбук", 20000, 5)
    assert repr(item3) == "Item('Телевизор', 10000, 2)"
    assert repr(item4) == "Item('Ноутбук', 20000, 5)"


def test_str():
    item5 = Item("Смартфон", 10000, 50)
    item6 = Item("Ноутбук", 20000, 15)
    assert str(item5) == "Смартфон"
    assert str(item6) == "Ноутбук"
