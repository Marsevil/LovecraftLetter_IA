from ..SaneCard import SaneCard

class RandolphCarter (SaneCard):

    def __init__(self):
        super().__init__("Randolph Carter", "When you discard Randolph Carter" +
        " during your turn, choose another player and trade your hand with" +
        " them. You cannot trade with a player who has been knocked out of" +
        " the round." , 6)

    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity


    def effect(self, gameManager):
        pass
