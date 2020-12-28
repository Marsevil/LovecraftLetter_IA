import unittest

from tests.FakeView import FakeView
from controller.GameManager import GameManager
from model.card.saneCard.Investigators import Investigators
from model.card.saneCard.GreatRaceOfYith import GreatRaceOfYith
from model.card.saneCard.ProfessorHenryArmitage import ProfessorHenryArmitage

class TestInvestigators(unittest.TestCase) :
    def test_value3(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].pickUp(Investigators())
        # The FakeView automatically respond 3 so I place Great Race Of Yith (value 3).
        gm.players[1].hand = [GreatRaceOfYith()]

        gm.play(1)

        # The other player should be kicked out
        self.assertTrue(gm.players[1].knockedOut)

    def test_noValue3(self) :
        gm = GameManager(FakeView(None), 2)
        gm.players[0].pickUp(Investigators())
        # Is the other player doesn't have any card with value 3.
        gm.players[1].hand = [ProfessorHenryArmitage()]

        gm.play(1)

        self.assertFalse(gm.players[1].knockedOut)
