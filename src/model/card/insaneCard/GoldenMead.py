from ..InsaneCard import InsaneCard
from ..Sanity import Sanity

class GoldenMead(InsaneCard):

    def __init__(self):
        super(GoldenMead,self).__init__("Golden Mead",
                       "Sane : When you discard Golden Mead during your turn, choose another"
                       +" player and look at their hand. Do not reveal it to any other players."
                       +" If all other players still in the round cannot be chosen (e.g due to Elder Sign"
                       +" or Liber Ivonis), this card is discarded without effect. \n"
                       +"Insane : When you discard Golden Mead during your turn,"
                       +" choose another player and look at their hand. Do not reveal it to any"
                       +" other players. Then draw a card (you have 2 cards in your hand now) and discard one."
                       +" If all other players still in the round cannot be chosen (e.g due to Elder"
                       +" Sign or Liber Ivonis), this card is discarded without effect.", 2)

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
    Or
    Choose a player and add his hand in the player KnownCards, draw a card and discard one
    """
    def effect(self,gameManager):
        
        if self.sanity == Sanity.SANE:
            player = gameManager.getCurrentPlayer()
            chosenPlayer = gameManager.chooseTargetPlayer(1, False)
    
            #Check if a player is returned
            if(len(chosenPlayer) != 0):
                chosenPlayerHand = chosenPlayer[0].getHand()
                
                gameManager.showHandToCurrent(chosenPlayerHand)
                
                #player.addKnownCards(chosenPlayerHand)

        if self.sanity == Sanity.INSANE:
            player = gameManager.getCurrentPlayer()
            chosenPlayer = gameManager.chooseTargetPlayer(1, False)
    
            #Check if a player is returned
            if(len(chosenPlayer) != 0):
                chosenPlayerHand = chosenPlayer[0].getHand()
                
                gameManager.showHandToCurrent(chosenPlayerHand)
                
                if gameManager.deck :
                    gameManager.playerDraw(player,1)
                    gameManager.playerDiscard(player,1)