from ..SaneCard import SaneCard

class GreatRaceOfYith (SaneCard):

    def __init__(self):
        super().__init__("Great Race Of Yith", "When you discard Great Race" +
        " of Yith during your turn, choose another player. You and that" +
        " player secretly compare your hands. The player with the lower" +
        " number is knocked out of the round. In case of a tie, nothing" +
        " happens. If all other players still in the round cannot be chosen" +
        " (e.g due to Elder Sign or Liber Ivonis), this card is discarded" +
        " without effect." , 3)

    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity


    def effect(self, gameManager):
        #Demande à viser un joueur
        chosenOne = gameManager.chooseTargetPlayer(1)

        #Vérifie qu'un joueur non immunisé a pu être choisi
        if not chosenOne:

            #Cherche qui a la plus petite carte pour l'éjecter, sinon rien
            player = gameManager.getCurrentPlayer()
            playerHand = player.getHand()
            targetHand = chosenOne.getHand()

            if(playerHand[0].getValue() < targetHand[0].getvalue()):
                player.knockedOut = True
            elif(playerHand[0].getValue() > targetHand[0].getvalue()):
                chosenOne.knockedOut = True
