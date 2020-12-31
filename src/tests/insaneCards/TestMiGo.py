import unittest

from tests.FakeView import FakeView
from tests.FakeViewInsane import FakeViewInsane
from controller.GameManager import GameManager
from model.card.insaneCard.MiGo import MiGo
from model.card.saneCard.RandolphCarter import RandolphCarter
from model.card.saneCard.GreatRaceOfYith import GreatRaceOfYith
from model.card.insaneCard.MiGoBraincase import MiGoBraincase
from model.card.insaneCard.Cthulhu import Cthulhu
from model.card.saneCard.TheNecronomicon import TheNecronomicon
from model.card.saneCard.Investigators import Investigators
from model.card.insaneCard.GoldenMead import GoldenMead

class TestMiGo(unittest.TestCase) :
    def test_commonCase(self) :
        # Test common case.
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(GreatRaceOfYith())
        gm.players[0].pickUp(MiGo())

        gm.players[1].hand = []
        gm.players[1].pickUp(GreatRaceOfYith())

        gm.deck.append(RandolphCarter())

        gm.play(1)

        self.assertIsInstance(gm.players[1].hand[0], RandolphCarter)

    def test_deckEmpty(self) :
        # When the deck is empty other player should pick up MiGoBraincase.

        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].setHand([GreatRaceOfYith(), MiGo()])

        gm.players[1].setHand([GreatRaceOfYith()])

        gm.deck = []
        gm.removedCards = [RandolphCarter()]

        gm.play(1)

        self.assertIsInstance(gm.players[1].hand[0], RandolphCarter)

    def test_withChtulhu(self) :
        # When Chtulhu is in the hand of the other player the effect should be applied.
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(GreatRaceOfYith())
        gm.players[0].pickUp(MiGo())

        gm.players[1].hand = []
        gm.players[1].pickUp(Cthulhu())

        gm.play(1)

        self.assertFalse(gm.players[1].hand)
        self.assertTrue(gm.players[1].knockedOut)

    def test_withNecronomicon(self) :
        # When TheNecronomicon is in the hand of the other player the effect should be applied.
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(GreatRaceOfYith())
        gm.players[0].pickUp(MiGo())

        gm.players[1].hand = []
        gm.players[1].pickUp(TheNecronomicon())

        gm.play(1)

        self.assertFalse(gm.players[1].hand)
        self.assertTrue(gm.players[1].knockedOut)

    def test_pickMiGoBraincase(self) :
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(GreatRaceOfYith())
        gm.players[0].pickUp(MiGo())
        # Insane card in the discard
        gm.players[0].discard = [GoldenMead()]

        gm.players[1].hand = []
        gm.players[1].pickUp(Investigators())

        gm.play(1)

        # other player must take Mi-Go Braincase
        self.assertIsInstance(gm.players[1].hand[0], MiGoBraincase)
        # current player should have just one card it his hand
        # the one that have the other player earlier
        # because card 0 is discarded
        # hand[-1] give the last card that have been stacked in the hand
        self.assertIsInstance(gm.players[0].hand[-1], Investigators)
        