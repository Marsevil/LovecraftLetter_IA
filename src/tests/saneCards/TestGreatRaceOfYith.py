import unittest

from tests.FakeView import FakeView
from controller.GameManager import GameManager
from model.card.saneCard.GreatRaceOfYith import GreatRaceOfYith
from model.card.saneCard.ElderSign import ElderSign
from model.card.saneCard.TheNecronomicon import TheNecronomicon

class TestGreatRaceOfYith(unittest.TestCase) :
    def test_otherGreaterThanCurrent(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        # Using current player < other player.
        gm.players[0].hand = []
        gm.players[0].pickUp(ElderSign())
        gm.players[0].pickUp(GreatRaceOfYith())

        gm.players[1].hand = []
        gm.players[1].pickUp(TheNecronomicon())

        gm.play(1)

        # Current player should be knocked out
        self.assertTrue(gm.players[0].knockedOut)
        self.assertFalse(gm.players[1].knockedOut)

    def test_currentGreaterThanOther(self) :
        # Using current player > other player.
        gm = GameManager(FakeView(None), 2)
        gm.players[0].hand = []
        gm.players[0].pickUp(TheNecronomicon())
        gm.players[0].pickUp(GreatRaceOfYith())

        gm.players[1].hand = []
        gm.players[1].pickUp(ElderSign())
        
        gm.play(1)

        # Other player should be knocked out.
        self.assertTrue(gm.players[1].knockedOut)
        self.assertFalse(gm.players[0].knockedOut)