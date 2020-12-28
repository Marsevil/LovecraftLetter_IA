from .FakeView import FakeView
from model.card.Sanity import Sanity

class FakeViewInsane(FakeView) :
    def __init__(self, gameManager) :
        super().__init__(gameManager)

    def askInsanity(self) :
        return Sanity.INSANE
