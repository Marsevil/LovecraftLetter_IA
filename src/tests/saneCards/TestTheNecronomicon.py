import unittest

from tests.FakeView import FakeView
from controller.GameManager import GameManager
from model.card.saneCard.TheNecronomicon import TheNecronomicon
from model.card.saneCard.CatsOfUlthar import CatsOfUlthar

class TestTheNecronomicon(unittest.TestCase) :
    def test_knockedOut(self) :
        gm = GameManager(FakeView(None), 2)
        gm.players[0].hand = []
        gm.players[0].pickUp(CatsOfUlthar())
        gm.players[0].pickUp(TheNecronomicon())

        gm.play(1)

        self.assertTrue(gm.players[0].knockedOut)