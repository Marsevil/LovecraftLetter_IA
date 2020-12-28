import unittest

from tests.FakeView import FakeView
from controller.GameManager import GameManager
from model.card.saneCard.RandolphCarter import RandolphCarter
from model.card.saneCard.CatsOfUlthar import CatsOfUlthar
from model.card.saneCard.ElderSign import ElderSign

class TestRandolphCarter(unittest.TestCase) :
    def test_trade(self) :
        gm = GameManager(FakeView(None), 2)
        gm.startNewRound()
        gm.players[0].hand = []
        gm.players[0].pickUp(CatsOfUlthar())
        gm.players[0].pickUp(RandolphCarter())

        gm.players[1].hand = []
        gm.players[1].pickUp(ElderSign())

        gm.play(1)

        self.assertIsInstance(gm.players[0].hand[0], ElderSign)
        self.assertIsInstance(gm.players[1].hand[0], CatsOfUlthar)

        self.assertEqual(gm.players[0].hand[0]._owner, gm.players[0])
        self.assertEqual(gm.players[1].hand[0]._owner, gm.players[1])