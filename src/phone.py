from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        # Вызываем метод базового класса
        super().__init__(name, price, quantity)
        # Дополнительный код
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
