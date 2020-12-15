from ..SaneCard import SaneCard

class ElderSign (SaneCard):

    def __init__(self):
        super().__init__("Elder Sign", "When you discard Elder Sign during your turn, you are" +
                            "immune to card effects of other players until the start of your" +
                            "next turn. If all players still in the round other than the" +
                            "player whose turn it is are immune, that player must choose" +
                            "themselves for their card’s effects, if possible.",4)

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
