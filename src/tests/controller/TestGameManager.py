import unittest

from controller.GameManager import GameManager
from tests.FakeViewInsane import FakeViewInsane
from model.card.insaneCard.DeepOnes import DeepOnes
from model.card.insaneCard.Cthulhu import Cthulhu
from model.card.insaneCard.TheShiningTrapezohedron import TheShiningTrapezohedron
from model.card.insaneCard.GoldenMead import GoldenMead
from model.card.saneCard.TheSilverKey import TheSilverKey
from model.card.saneCard.ProfessorHenryArmitage import ProfessorHenryArmitage

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

    def testRoundWinCthulhuXArmitage(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].setHand([DeepOnes(), ProfessorHenryArmitage()])
        gm.players[1].setHand([Cthulhu()])
        gm.players[1].setDiscard([DeepOnes(), DeepOnes()])

        gm.play(1)

        self.assertEqual(1, gm.findWinnerWthSpecialEffect())

    def testGameWinCthulhu(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].setHand([DeepOnes(), Cthulhu()])
        gm.players[0].addDiscardedCard(DeepOnes())
        gm.players[0].addDiscardedCard(DeepOnes())

        gm.play(1)

        self.assertEqual(0, gm.isGameEnd())

    def testGameEndWithSaneToken(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].saneToken = 2

        self.assertEqual(0, gm.isGameEnd())

    def testGameEndWithInsaneToken(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].insaneToken = 3

        self.assertEqual(0, gm.isGameEnd())

    def testGameNoEndWithSaneToken(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].saneToken = 1

        self.assertEqual(-1, gm.isGameEnd())

    def testGameNoEndWithInsaneToken(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].insaneToken = 2

        self.assertEqual(-1, gm.isGameEnd())

    def testResetStateAfterPlay(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].hand = []
        gm.players[0].setHand([DeepOnes(), Cthulhu()])
        gm.players[0].addDiscardedCard(DeepOnes())
        gm.players[0].addDiscardedCard(DeepOnes())
        gm.players[0].immune = True
        gm.players[0].knockableOut = False

        gm.play(1)

        self.assertTrue(gm.players[0].isKnockableOut())
        self.assertFalse(gm.players[0].getImmune())

    def testResetStateStartNewRound(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        gm.players[0].immune = True
        gm.players[0].knockableOut = False
        gm.players[0].knockedOut = True

        gm.startNewRound()

        self.assertFalse(gm.players[0].getKnockedOut())
        self.assertFalse(gm.players[0].getImmune())
        self.assertTrue(gm.players[0].isKnockableOut())

    def testIsRoundEndWinKnockedOut(self) :
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()

        gm.players[1].knockedOut = True

        self.assertEqual(0, gm.isRoundEnd())

    def testIsRoundEndNoWinKnockedOut(self) :
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()

        self.assertEqual(-1, gm.isRoundEnd())

    def testIsRoundEndWinGreatestCard(self) :
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()

        # Give known card to players
        gm.players[0].hand = []
        gm.players[1].hand = []
        gm.players[0].pickUp(TheShiningTrapezohedron())
        gm.players[1].pickUp(DeepOnes())

        # Emty Deck
        gm.deck = []

        # P0 should win because the shining trapezohedron is greater than Deep ones.
        self.assertEqual(0, gm.isRoundEnd())

    def testIsRoundEndTie(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        # Give cards with same value to each player
        gm.players[0].setHand([TheSilverKey()])
        gm.players[1].setHand([TheShiningTrapezohedron()])

        # Empty deck
        gm.deck = []

        self.assertEqual(-2, gm.isRoundEnd())

    def testCheckPlayableCardFalse(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        # If the other card is greater than 4 with TheSilverKey.
        gm.players[0].setHand([ProfessorHenryArmitage(), TheSilverKey()])
        self.assertFalse(gm.checkPlayableCard())

        # If the other card is greater than 4 with TheShiningTrapezohedron.
        gm.players[0].setHand([ProfessorHenryArmitage(), TheShiningTrapezohedron()])
        self.assertFalse(gm.checkPlayableCard())

    def testCheckPlayableCardTrue(self) :
        gm = GameManager(FakeViewInsane(None), 2)

        # If the other card is lower than 4 with TheSilverKey
        gm.players[0].setHand([DeepOnes(), TheSilverKey()])
        self.assertTrue(gm.checkPlayableCard())

        # If the other card is lower than 4 with TheShiningTrapezohedron
        gm.players[0].setHand([DeepOnes(), TheShiningTrapezohedron()])
        self.assertTrue(gm.checkPlayableCard())

        # If the two cards are TheShiningTrapezohedron AND TheSilverKey
        gm.players[0].setHand([TheSilverKey(), TheShiningTrapezohedron()])
        self.assertTrue(gm.checkPlayableCard())

        gm.players[0].setHand([TheShiningTrapezohedron(), TheSilverKey()])
        self.assertTrue(gm.checkPlayableCard())
