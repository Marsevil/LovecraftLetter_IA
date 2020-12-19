import unittest

from ..FakeView import FakeView
from ...controller.GameManager import GameManager
from ...model.card.saneCard.GreatRaceOfYith import GreatRaceOfYith
from ...model.card.saneCard.ElderSign import ElderSign
from ...model.card.saneCard.TheNecronomicon import TheNecronomicon

class TestGreatRaceOfYith(unittest.TestCase) :
    def test_otherGreaterThanCurrent(self) :
        gm = GameManager(FakeView(None), 2)
        # Using current player < other player.
        gm.players[0].hand = [ElderSign(), GreatRaceOfYith()]
        gm.players[1].hand = [TheNecronomicon()]
        gm.play(1)

        # Current player should be knocked out
        self.assertTrue(gm.players[0].knockedOut)
        self.assertFalse(gm.players[1].knockedOut)

    def test_currentGreaterThanOther(self) :
        # Using current player > other player.
        gm = GameManager(FakeView(None), 2)
        gm.players[0].hand = [TheNecronomicon(), GreatRaceOfYith()]
        gm.players[1].hand = [ElderSign()]
        gm.play(1)

        # Other player should be knocked out.
        self.assertTrue(gm.players[1].knockedOut)
        self.assertFalse(gm.players[0].knockedOut)