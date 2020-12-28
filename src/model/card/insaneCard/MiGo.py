from ..InsaneCard import InsaneCard
from ..Sanity import Sanity

from .MiGoBraincase import MiGoBraincase


class MiGo (InsaneCard):

    def __init__(self):
        super(MiGo,self).__init__("Mi-Go", "Sane : When you discard" +
        " Professor Henry Armitage during your turn, choose a player" +
        " (including yourself). That player discards their hand (but doesn’t" +
        " apply its effects, unless it is the The Necronomicon or Cthulhu)" +
        " and draws a new card. If the player cannot draw a card due to the" +
        " deck being empty, they draw the card that was removed at the start" +
        " of the round. If all other players still in the round are immune," +
        " you must choose yourself."
        +"When you discard Mi-Go during your turn, choose another player."
        +"You add their hand in yours (you have 2 cards in your hand now). They"
        +"must take Mi-Go Braincase in their hand (they now have one card). Since"
        +"you have 2 cards in hand, you discard a card."
        +"If all other players still in the round cannot be chosen (e.g due to Elder"
        +"Sign or Liber Ivonis), this card is discarded without effect.", 5)

    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity


    def effect(self, gameManager):
        
        if self.sanity == Sanity.SANE:
            #Choose a player (including itself)
            chosenOne = gameManager.chooseTargetPlayer(1, True)

            #Check if a not immuned player could has been chosen
            if(len(chosenOne) != 0):

                #Discard the hand of the target player
                targetHand = chosenOne[0].getHand()
                for card in targetHand:

                    #Only apply the effect if the card is The Necromicon
                    if (card.getName() == "The Necromicon"):
                        card.effect(gameManager)
                    #or cthulhu, but this time ask the view for the saniy of its effect
                    elif (card.getName() == "Cthulhu"):
                        effectSanity = gameManager.askInsanity(card)
                        card.sanity = (effectSanity)
                        card.effect(gameManager)
                    else:
                        chosenOne[0].addDiscardedCard(card)

                        #The target player draws a new card
                        if gameManager.deck :
                            #Draw a card
                            chosenOne[0].pickUp(gameManager.deck.pop())
                            #If the deck is empty he draws the first card
                            #that was removed at the start of the round
                        else:
                            chosenOne[0].pickUp(gameManager.removedCards.pop())

        if self.sanity == Sanity.INSANE:
            
            player = gameManager.getCurrentPlayer()
            
            #Choose a player (including itself)
            chosenOne = gameManager.chooseTargetPlayer(1, True)

            #Check if a not immuned player could has been chosen
            if(len(chosenOne) != 0):

                #Discard the hand of the target player
                targetHand = chosenOne.getHand()
                player.pickUp(targetHand[0])
                
                #TODO Implement gameManager, "player" discard "x" card
                gameManager.playerDiscard(player,1)
                
                chosenOne.pickUp(MiGoBraincase())
                