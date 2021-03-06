from ..SaneCard import SaneCard

class CatsOfUlthar(SaneCard):

    def __init__(self):
        super(CatsOfUlthar,self).__init__("CatsOfUlthar",
                       "When you discard Cats of Ulthar during your turn," +
                       " choose another player and look at their hand. Do" +
                       " not reveal it to any other players. If all other" +
                       " players still in the round cannot be chosen (e.g" +
                       " due to Elder Sign or Liber Ivonis), this card is" +
                       " discarded without effect.)", 2)

    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity

    """
    @params gameManager, gameManager entity
    
    Choose a player and add his hand in the player KnownCards
    """
    def effect(self,gameManager):
        chosenPlayer = gameManager.chooseTargetPlayer(1, False)

        #Check if a player is returned
        if(len(chosenPlayer) != 0):
            chosenPlayerHand = chosenPlayer[0].getHand()
            
            gameManager.showHandToCurrent(chosenPlayerHand)
            
            #player.addKnownCards(chosenPlayerHand)
