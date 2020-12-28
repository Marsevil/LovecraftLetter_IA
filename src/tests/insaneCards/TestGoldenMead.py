import unittest

from tests.FakeView import FakeView
from tests.FakeViewInsane import FakeViewInsane
from controller.GameManager import GameManager
from model.card.insaneCard.GoldenMead import GoldenMead
from model.card.insaneCard.DeepOnes import DeepOnes
from model.card.saneCard.Investigators import Investigators

class TestGoldenMead(unittest.TestCase) :
    def test_showHand(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].pickUp(GoldenMead())

        gm.play(1)

        # This card just show something.
        print("Something must be printed.")

    def test_drawAndDiscard(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].pickUp(DeepOnes())
        gm.players[0].pickUp(GoldenMead())
        gm.players[0].addDiscardedCard(DeepOnes())

        # Prepare the card which will be draw.
        gm.deck.append(Investigators())

        gm.play(1)

        # Show the other player's hand.
        print("Something must be printed.")

        # Choose a card to keep
        # FakeView alwayd return 0 in playerDiscard so the card freshly draw will be kept.
        self.assertIsInstance(gm.players[0].hand[0], Investigators)