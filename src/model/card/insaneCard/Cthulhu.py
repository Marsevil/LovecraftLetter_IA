from ..InsaneCard import InsaneCard
from ..Sanity import Sanity

class Cthulhu(InsaneCard):

    def __init__(self):
        super().__init__("Cthulhu", "If you ever discard Cthulhu no matter how or why" +
                        " (so even during a Sanity Check)— you lose the track of your cousin." +
                        " You are immediately knocked out of the round." +
                        " If Cthulhu was discarded due to a card effect, any remaining" +
                        " effects of that card do not apply (you do not draw a card " +
                        " from Professor Henry Armitage, for example)."
                        " Insane : When you discard Cthulhu during your turn, if you" +
                        " already have 2 or more Insanity cards in your discard pile," +
                        " you win the game. If you do not, you lose the round", 8)

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
            # You are knocked out if the round if you discard Cthulhu if the player could be knocked out
            if(gameManager.getCurrentPlayer().isKnockableOut()):
                gameManager.getCurrentPlayer().setKnockedOut(True)

        if self.sanity == Sanity.INSANE:
            player = gameManager.getCurrentPlayer()
            #check if the player have played less than 2 insane cards and could be knock out he is knocked out
            if(player.nbInsaneCardDiscarded() < 2 and player.isKnockableOut()){
                player.setKnockedOut(True)
            }