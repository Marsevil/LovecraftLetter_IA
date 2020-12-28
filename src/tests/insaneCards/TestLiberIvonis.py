import unittest

from tests.FakeView import FakeView
from tests.FakeViewInsane import FakeViewInsane
from controller.GameManager import GameManager
from model.card.insaneCard.LiberIvonis import LiberIvonis
from model.card.insaneCard.GoldenMead import GoldenMead
from model.card.saneCard.Investigators import Investigators

class TestLiberIvonis(unittest.TestCase) :
    def test_immunePlayer(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = [Investigators()]
        gm.players[0].pickUp(LiberIvonis())
        gm.play(1)

        # immune the current player.
        self.assertTrue(gm.players[0].immune)

    def test_playerCantBeKnockOut(self) : 
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()
        gm.players[0].hand = [Investigators()]
        # Insane card in the discard
        gm.players[0].discard = [GoldenMead()]
        gm.players[0].pickUp(LiberIvonis())
        gm.play(1)
        
        # the current player isn't knockable out
        self.assertFalse(gm.players[0].knockableOut)
