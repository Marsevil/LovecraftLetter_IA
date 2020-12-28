import unittest

from ..FakeView import FakeView
from ...model.card.saneCard.ElderSign import ElderSign
from ...controller.GameManager import GameManager

class TestElderSign(unittest.TestCase) :
    def test_ElderSign(self) :
        gm = GameManager(FakeView(None), 2)
        gm.players[0].pickUp(ElderSign())
        gm.play(1)

        # immune the current player.
        self.assertTrue(gm.players[0].immune)
