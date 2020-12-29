import unittest

from tests.FakeView import FakeView
from tests.FakeViewInsane import FakeViewInsane
from controller.GameManager import GameManager
from model.card.insaneCard.MiGoBraincase import MiGoBraincase
from model.card.insaneCard.GoldenMead import GoldenMead
from model.card.saneCard.Investigators import Investigators
from model.card.saneCard.CatsOfUlthar import CatsOfUlthar

class TestMiGoBraincase(unittest.TestCase) :
    def test_loseRoundSaneKnockable(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = [Investigators()]
        gm.players[0].pickUp(MiGoBraincase())
        # Only sane card in the discard
        gm.players[0].discard = [CatsOfUlthar()]

        gm.play(1)

        # player will lose the round so is knocked out
        self.assertTrue(gm.players[0].knockedOut)

    def test_loseRoundSaneNotKnockable(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = [Investigators()]
        gm.players[0].pickUp(MiGoBraincase())
        # Only sane card in the discard
        gm.players[0].discard = [CatsOfUlthar()]
        gm.players[0].setKnockableOut(False)

        gm.play(1)

        # player will lose the round so is knocked out even if he was not knockable
        self.assertTrue(gm.players[0].knockedOut)

    def test_loseRoundInsaneKnockable(self) : 
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()
        gm.players[0].hand = [Investigators()]
        gm.players[0].pickUp(MiGoBraincase())
        # Insane card in the discard
        gm.players[0].discard = [GoldenMead()]

        gm.play(1)
        
        # player will lose the round so is knocked out
        self.assertTrue(gm.players[0].knockedOut)

    def test_loseRoundInsaneNotKnockable(self) :
        gm = GameManager(FakeViewInsane(None), 2)
        gm.startNewRound()
        gm.players[0].hand = [Investigators()]
        gm.players[0].pickUp(MiGoBraincase())
        # Only sane card in the discard
        gm.players[0].discard = [GoldenMead()]
        gm.players[0].setKnockableOut(False)

        gm.play(1)

        # player will lose the round so is knocked out even if he was not knockable
        self.assertTrue(gm.players[0].knockedOut)
