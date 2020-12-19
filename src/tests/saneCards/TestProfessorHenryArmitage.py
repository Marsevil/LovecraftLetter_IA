import unittest

from ..FakeView import FakeView
from ...controller.GameManager import GameManager
from ...model.card.saneCard.ProfessorHenryArmitage import ProfessorHenryArmitage
from ...model.card.saneCard.RandolphCarter import RandolphCarter
from ...model.card.saneCard.GreatRaceOfYith import GreatRaceOfYith
from ...model.card.insaneCard.MiGoBraincase import MiGoBraincase
from ...model.card.insaneCard.Cthulhu import Cthulhu
from ...model.card.saneCard.TheNecronomicon import TheNecronomicon

class TestProfessorHenryArmitage(unittest.TestCase) :
    def test_commonCase(self) :
        # Test common case.
        gm = GameManager(FakeView(None), 2)
        gm.players[0].hand = [GreatRaceOfYith(), ProfessorHenryArmitage()]
        gm.players[1].hand = [GreatRaceOfYith()]
        gm.deck.append(RandolphCarter())

        gm.play(1)

        self.assertIsInstance(gm.players[1].hand[0], RandolphCarter)

    def test_deckEmpty(self) :
        # When the deck is empty other player should pick up MiGoBraincase.

        gm = GameManager(FakeView(None), 2)
        gm.players[0].hand = [GreatRaceOfYith(), ProfessorHenryArmitage()]
        gm.players[1].hand = [GreatRaceOfYith()]
        gm.deck = []

        gm.play(1)

        self.assertIsInstance(gm.players[1].hand[0], MiGoBraincase)

    def test_withChtulhu(self) :
        # When Chtulhu is in the hand of the other player the effect should be applied.

        gm = GameManager(FakeView(None), 2)
        gm.players[0].hand = [GreatRaceOfYith(), ProfessorHenryArmitage()]
        gm.players[1].hand = [Cthulhu()]

        gm.play(1)

        # La carte chtulhu s'applique sur le current player.
        self.assertTrue(gm.players[1].knockedOut)