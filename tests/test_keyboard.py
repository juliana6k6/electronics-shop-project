from src.keyboard import Keyboard
import pytest

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_keyboard_init():
    assert str(kb) == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"


def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == "RU"
    # Сделали EN -> RU -> EN
    kb.change_lang()
    assert str(kb.language) == "EN"

#
