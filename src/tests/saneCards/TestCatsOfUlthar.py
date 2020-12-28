import unittest

from ..FakeView import FakeView
from model.card.saneCard.CatsOfUlthar import CatsOfUlthar
from controller.GameManager import GameManager

class TestCatsOfUlthar(unittest.TestCase) :
    def test_CatsOfUlthar(self) :
        gm = GameManager(FakeView(None), 2)
        gm.players[0].pickUp(CatsOfUlthar())
        gm.play(1)

        # This card just show something.
        print("Something must be printed.")