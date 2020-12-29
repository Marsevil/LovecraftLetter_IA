import unittest

from tests.FakeView import FakeView
from tests.FakeViewInsane import FakeViewInsane
from controller.GameManager import GameManager
from model.card.insaneCard.HoundOfTindalos import HoundOfTindalos
from model.card.saneCard.ElderSign import ElderSign
from model.card.saneCard.TheNecronomicon import TheNecronomicon
from model.card.saneCard.Investigators import Investigators
from model.card.insaneCard.GoldenMead import GoldenMead
from model.card.insaneCard.DeepOnes import DeepOnes
from model.card.Sanity import Sanity

class TestHoundOfTindalos(unittest.TestCase) :
    def test_otherGreaterThanCurrent(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        # Using current player < other player.
        gm.players[0].hand = []
        gm.players[0].pickUp(ElderSign())
        gm.players[0].pickUp(HoundOfTindalos())

        gm.players[1].hand = []
        gm.players[1].pickUp(TheNecronomicon())

        gm.play(1)

        # Current player should be knocked out
        self.assertTrue(gm.players[0].knockedOut)
        self.assertFalse(gm.players[1].knockedOut)

    def test_currentGreaterThanOther(self) :
        # Using current player > other player.
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(TheNecronomicon())
        gm.players[0].pickUp(HoundOfTindalos())

        gm.players[1].hand = []
        gm.players[1].pickUp(ElderSign())
        
        gm.play(1)

        # Other player should be knocked out.
        self.assertTrue(gm.players[1].knockedOut)
        self.assertFalse(gm.players[0].knockedOut)
    
    def test_OtherKnockableHasNotInsane(self) : 
        # Other player could be knock out and hasn't an insane state of mind
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(ElderSign())
        gm.players[0].pickUp(HoundOfTindalos())
        gm.players[0].discard = [DeepOnes()]

        gm.players[1].hand = []
        # Only sane cards in the discard
        gm.players[1].discard = [Investigators()]
        gm.players[1].pickUp(TheNecronomicon())

        gm.play(1)

        # Other player should be knocked out
        self.assertEqual(gm.players[1].stateOfMind(), Sanity.SANE)
        self.assertTrue(gm.players[1].knockableOut)
        self.assertTrue(gm.players[1].knockedOut)

    def test_OtherKnockableHasInsane(self) :
        # Other player could be knock out and has an insane state of mind
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(ElderSign())
        gm.players[0].pickUp(HoundOfTindalos())
        gm.players[0].discard = [DeepOnes()]

        gm.players[1].hand = []
        # Insane card in the discard
        gm.players[1].discard = [GoldenMead()]
        gm.players[1].pickUp(TheNecronomicon())

        gm.play(1)

        # Other player shouldn't be knocked out
        self.assertEqual(gm.players[1].stateOfMind(), Sanity.INSANE)
        self.assertTrue(gm.players[1].knockableOut)
        self.assertFalse(gm.players[1].knockedOut)

    def test_OtherNotKnockableHasNotInsane(self) :
        # Other player couldn't be knock out and hasn't an insane state of mind
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(ElderSign())
        gm.players[0].pickUp(HoundOfTindalos())
        gm.players[0].discard = [DeepOnes()]

        gm.players[1].hand = []
        gm.players[1].discard = [Investigators()]
        gm.players[1].setKnockableOut(False)
        gm.players[1].pickUp(TheNecronomicon())

        gm.play(1)

        # Other player shouldn't be knocked out
        self.assertFalse(gm.players[1].knockableOut)
        self.assertFalse(gm.players[1].knockedOut)

    def test_OtherNotKnockableHasInsane(self) :
        # Other player couldn't be knock out and has an insane state of mind
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(ElderSign())
        gm.players[0].pickUp(HoundOfTindalos())
        gm.players[0].discard = [DeepOnes()]

        gm.players[1].hand = []
        gm.players[1].discard = [GoldenMead()]
        gm.players[1].setKnockableOut(False)
        gm.players[1].pickUp(TheNecronomicon())

        gm.play(1)

        # Other player shouldn't be knocked out
        self.assertFalse(gm.players[1].knockableOut)
        self.assertFalse(gm.players[1].knockedOut)
