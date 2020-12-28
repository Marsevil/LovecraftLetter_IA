import unittest

from tests.FakeView import FakeView
from tests.FakeViewInsane import FakeViewInsane
from controller.GameManager import GameManager
from model.card.insaneCard.DeepOnes import DeepOnes
from model.card.insaneCard.GoldenMead import GoldenMead
from model.card.insaneCard.HoundOfTindalos import HoundOfTindalos
from model.card.saneCard.Investigators import Investigators
from model.card.saneCard.ProfessorHenryArmitage import ProfessorHenryArmitage
from model.card.saneCard.GreatRaceOfYith import GreatRaceOfYith

class TestDeepOnes(unittest.TestCase) :
    def test_value3Sane(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        
        gm.players[0].pickUp(Investigators())
        # The FakeView automatically respond 3 so I place Great Race Of Yith (value 3).
        gm.players[1].hand = [GreatRaceOfYith()]

        gm.play(1)

        # The other player should be kicked out
        self.assertTrue(gm.players[1].knockedOut)

    def test_noValue3Sane(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()

        gm.players[0].pickUp(Investigators())
        # Is the other player doesn't have any card with value 3.
        gm.players[1].hand = [ProfessorHenryArmitage()]

        gm.play(1)

        self.assertFalse(gm.players[1].knockedOut)

    def test_value1(self) :
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()

        gm.players[0].hand = []
        gm.players[0].pickUp(GoldenMead())
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].addDiscardedCard(GoldenMead())
        
        # The other player must have a card with a value of one.
        gm.players[1].hand = []
        gm.players[1].pickUp(Investigators())

        gm.play(1)

        self.assertTrue(gm.players[1].knockedOut)

    def test_value3Insane(self) :
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()

        gm.players[0].hand = []
        gm.players[0].pickUp(GoldenMead())
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].addDiscardedCard(GoldenMead())

        gm.players[1].hand = []
        gm.players[1].pickUp(HoundOfTindalos())

        gm.play(1)

        self.assertTrue(gm.players[1].knockedOut)

    def test_noValue3Insane(self) :
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()

        gm.players[0].hand = []
        gm.players[0].pickUp(GoldenMead())
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].addDiscardedCard(GoldenMead())

        gm.players[1].hand = []
        gm.players[1].pickUp(GoldenMead())

        gm.play(1)

        self.assertFalse(gm.players[1].knockedOut)