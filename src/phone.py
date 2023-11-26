from src.item import Item


class Phone(Item):
    """
    Дочерний класс от 'item', который содержит атрибут, содержащий количество сим-карт
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создает новый экземпляр класса Phone с такими параметрами: название телефона,
        цена телефона, количество телефонов, количество SIM-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """
        Возвращает количество SIM-карт.
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_count):
        """
        Устанавливает количество SIM-карт.
        """
        if isinstance(sim_count, int) and sim_count >= 0:
            self.__number_of_sim = sim_count
        else:
            raise ValueError("Количество SIM-карт должно быть целым и больше нуля.")

    def __repr__(self):
        """
        Отображает информацию об объекте класса в режиме отладки
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        """
        Отображает информации об объекте класса для пользователей
        """
        return f"{self.name}"

    def __add__(self, other):
        """
        Рeализует возможность сложения экземпляров класса `Phone` и `Item` по количеству товара в магазине,
        при этом нельзя складывать `Phone` или `Item` с экземплярами не `Phone` или `Item` классов
        """
        if not isinstance(other, Phone):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity
