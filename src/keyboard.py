from src.item import Item


class MixinLang:
    """Для расширения функционала Keyboard"""
    __language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Изменяет язык в клавиатуре"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLang):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
