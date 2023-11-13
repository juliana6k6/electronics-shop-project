import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.z
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        """
        Рeализует возможность сложения экземпляров класса `Phone` и `Item` по количеству товара в магазине,
        при этом нельзя складывать `Phone` или `Item` с экземплярами не `Phone` или `Item` классов
        """
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        else:
            raise TypeError("Нельзя сложить классы 'Item' и чем-то другим.")

    @property
    def name(self):
        """
        Возвращает полное наименование товара
        """
        return self.__name

    @name.setter
    def name(self, product_name):
        """
        Если длина наименования товара больше 10 символов, сокращает наименование до 10 символов,
        если нет - оставляет таким же
        """
        self.__name = product_name[:10]
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @staticmethod
    def string_to_number(number):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(number))
    @classmethod
    def instantiate_from_csv(cls, file_name):
        """
        инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        with open(file_name, encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(name, price, quantity)






