from ..InsaneCard import InsaneCard
from ..Sanity import Sanity

class LiberIvonis(InsaneCard):

    def __init__(self):
        super().__init__("Liber Ivonis",
                        "Sane : When you discard Liber Ivonis during your turn, you are" +
                        "immune to card effects of other players until the start of your" +
                        "next turn. If all players still in the round other than the" +
                        "player whose turn it is are immune, that player must choose" +
                        "themselves for their card’s effects, if possible. \n" +
                        "Insane : When you discard Liber Ivonis during your turn," +
                        "you cannot be knocked out by effects until the end of the" +
                        "round. This includes:" +
                        "Sanity checks (you must still do them every turn). \n" +
                        "Someone discarding Investigators or Deep Ones and" +
                        "correctly guessing the number in your hand (just reply yes). \n" +
                        "Having a lower number when chosen by someone discarding Great" +
                        "Race of Yith or Hound of Tindalos (Sane effect). \n" +
                        "Discarding The Necronomicon, or Cthulhu during your turn (Sane effect). \n" +
                        "Discarding Mi-Go Braincase during your turn (Sane and Insane effect).", 4)

    @property
    def sanity(self):
        return self._sanity

    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue

    def getSanity(self):
        return self._sanity

    def effect(self,gameManager):
        
        if self.sanity == Sanity.SANE:
            #the current player is immune until his next turn
            player = gameManager.getCurrentPlayer()
            player.setImmune(True)

        if self.sanity == Sanity.INSANE:
            #the current player can't be knocked out until his next turn
            player = gameManager.getCurrentPlayer()
            player.setKnockableOut(False)