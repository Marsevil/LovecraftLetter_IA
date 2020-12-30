import unittest

from controller.GameManager import GameManager
from tests.FakeViewInsane import FakeViewInsane
from model.card.insaneCard.DeepOnes import DeepOnes
from model.card.insaneCard.Cthulhu import Cthulhu
from model.card.insaneCard.TheShiningTrapezohedron import TheShiningTrapezohedron
from model.card.insaneCard.GoldenMead import GoldenMead

class TestGameManager(unittest.TestCase) :
    def testRoundWinShiningTrapezohedron(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].pickUp(Cthulhu())
        gm.players[0].pickUp(TheShiningTrapezohedron())
        gm.players[0].addDiscardedCard(GoldenMead())

        gm.play(1)

        self.assertEqual(0, gm.findWinnerWthSpecialEffect())

    def testNoRoundWinShiningTrapezohedron(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].pickUp(TheShiningTrapezohedron())
        gm.players[0].addDiscardedCard(GoldenMead())

        gm.play(1)

        self.assertEqual(-1, gm.findWinnerWthSpecialEffect())

    def testRoundWinCthulhu(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].pickUp(Cthulhu())
        gm.players[0].addDiscardedCard(DeepOnes())
        gm.players[0].addDiscardedCard(DeepOnes())

        gm.play(1)

        self.assertEqual(0, gm.findWinnerWthSpecialEffect())

    def testGameWinCthulhu(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].setHand([DeepOnes(), Cthulhu()])
        gm.players[0].addDiscardedCard(DeepOnes())
        gm.players[0].addDiscardedCard(DeepOnes())

        gm.play(1)

        self.assertEqual(0, gm.isGameEnd())
