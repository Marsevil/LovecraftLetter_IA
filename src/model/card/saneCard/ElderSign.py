from ..SaneCard import SaneCard

class ElderSign (SaneCard):

    def __init__(self):
        super().__init__("Elder Sign", "The most plausible theory is that" +
                            "this is a weapon made to fight the Great Old" +
                            "Ones. It is a symbol carved into stone, and can" +
                            "be used as a repellent against their servitors.",1)

    @property
    def sanity(self):
        return self._sanity

    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue

    def getSanity(self):
        return self._sanity

    def effect(self, gameManager):
        #the current player is immune until his next turn
        player = gameManager.getCurrentPlayer()
        player.setImmune(True)
