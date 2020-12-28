import unittest

from tests.FakeViewInsane import FakeViewInsane
from tests.FakeView import FakeView
from controller.GameManager import GameManager
from model.card.insaneCard.Cthulhu import Cthulhu
from model.card.insaneCard.DeepOnes import DeepOnes
from model.card.insaneCard.GoldenMead import GoldenMead
from model.card.insaneCard.LiberIvonis import LiberIvonis

class TestChtulhu(unittest.TestCase) :
    def test_knockedOutSane(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()

        gm.players[0].hand = []
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].pickUp(Cthulhu())

        gm.play(1)

        self.assertTrue(gm.players[0].knockedOut)

    def test_knockedOutInsane(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].addDiscardedCard(DeepOnes())
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].pickUp(Cthulhu())

        gm.play(1)

        self.assertTrue(gm.players[0].knockedOut)

    def test_noKnockedOutInsane(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].pickUp(Cthulhu())
        gm.players[0].addDiscardedCard(GoldenMead())
        gm.players[0].addDiscardedCard(LiberIvonis())

        gm.play(1)

        self.assertFalse(gm.players[0].knockedOut)
