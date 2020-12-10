from ..SaneCard import SaneCard

class ProfessorHenryArmitage (SaneCard):

    def __init__(self):
        super().__init__("Professor Henry Armitage", "When you discard" +
        " Professor Henry Armitage during your turn, choose a player" +
        " (including yourself). That player discards their hand (but doesn’t" +
        " apply its effects, unless it is the The Necronomicon or Cthulhu)" +
        " and draws a new card. If the player cannot draw a card due to the" +
        " deck being empty, they draw the card that was removed at the start" +
        " of the round. If all other players still in the round are immune," +
        " you must choose yourself." , 5)

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
