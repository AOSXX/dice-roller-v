# tests/test_dice.py
from dice_roller.dice import Dice

class TestDice():
    def test_is_int(self):
        dice = Dice()
        roll = dice.roll()
        assert isinstance(roll, int)

    def test_is_higher_0(self):
        dice = Dice()
        roll = dice.roll()
        assert roll > 0

    def test_is_lower_7(self):
        dice = Dice()
        roll = dice.roll()
        assert roll < 7
