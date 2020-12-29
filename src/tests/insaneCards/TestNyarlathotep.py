import unittest

from controller.GameManager import GameManager
from tests.FakeView import FakeView
from tests.FakeViewInsane import FakeViewInsane
from model.card.saneCard.ElderSign import ElderSign
from model.card.insaneCard.Nyarlathotep import Nyarlathotep
from model.card.insaneCard.DeepOnes import DeepOnes
from model.card.insaneCard.GoldenMead import GoldenMead

class TestNyarlathotep(unittest.TestCase) :
    def testSwitchCard(self) :
        gm = GameManager(FakeView(None), 2)

        player = gm.players[0]
        player.hand = []
        player.pickUp(ElderSign())
        player.pickUp(Nyarlathotep())

        player = gm.players[1]
        player.hand = []
        player.pickUp(DeepOnes())

        gm.play(1)

        self.assertIsInstance(gm.players[0].hand[0], DeepOnes)
        self.assertIsInstance(gm.players[1].hand[0], ElderSign)

    def testWithTwoPlayer(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        player = gm.players[0]
        player.hand = []
        player.pickUp(ElderSign())
        player.pickUp(Nyarlathotep())
        player.addDiscardedCard(DeepOnes())

        player = gm.players[1]
        player.hand = []
        player.pickUp(GoldenMead())
        
        gm.play(1)

        self.assertIsInstance(gm.players[1].hand[0], GoldenMead)

    def testWithThreePlayer(self) :
        gm = GameManager(FakeViewInsane(None), 3)

        player = gm.players[0]
        player.hand = []
        player.pickUp(ElderSign())
        player.pickUp(Nyarlathotep())
        player.addDiscardedCard(DeepOnes())

        player = gm.players[1]
        player.hand = []
        player.pickUp(GoldenMead())

        player = gm.players[2]
        player.hand = []
        player.pickUp(DeepOnes())

        gm.play(1)

        self.assertIsInstance(gm.players[1].hand[0], DeepOnes)
        self.assertIsInstance(gm.players[2].hand[0], GoldenMead)
