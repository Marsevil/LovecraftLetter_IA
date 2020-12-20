import unittest

from ..FakeView import FakeView
from ..FakeViewInsane import FakeViewInsane
from ...controller.GameManager import GameManager
from ...model.card.insaneCard.LiberIvonis import LiberIvonis

class TestLiberIvonis(unittest.TestCase) :
    def test_immunePlayer(self) :
        gm = GameManager(FakeView(None), 2)
        gm.players[0].pickUp(LiberIvonis())
        gm.play(1)

        # immune the current player.
        self.assertTrue(gm.players[0].immune)

    def test_playerCantBeKnockOut(self) : 
        gm = GameManager(FakeViewInsane(None), 2)
        gm.players[0].pickUp(LiberIvonis())
        gm.play(1)
        
        # the current player isn't knockable out
        self.assertFalse(gm.players[0].knockableOut)
