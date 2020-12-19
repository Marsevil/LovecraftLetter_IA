from ..SaneCard import SaneCard
from ..insaneCard.Cthulhu import Cthulhu
from ..saneCard.TheNecronomicon import TheNecronomicon

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
        #Choose a player (including itself)
        chosenOne = gameManager.chooseTargetPlayer(1, True)

        #Check if a not immuned player could has been chosen
        if(len(chosenOne) != 0):

            #Discard the hand of the target player
            targetHand = chosenOne[0].getHand()
            for _i in range(len(targetHand)):

                card = targetHand.pop()

                #Only apply the effect if the card is The Necromicon
                if isinstance(card, TheNecronomicon):
                    card.effect(gameManager)
                #or cthulhu, but this time ask the view for the saniy of its effect
                elif isinstance(card, Cthulhu) :
                    effectSanity = gameManager.askInsanity(card)
                    card.sanity = effectSanity
                    card.effect(gameManager)
                else:
                    #The target player draws a new card
                    if gameManager.deck :
                        #Draw a card
                        chosenOne[0].pickUp(gameManager.deck.pop())
                    #If the deck is empty he draws the first card
                    #that was removed at the start of the round
                    else:
                        chosenOne[0].pickUp(gameManager.removedCards.pop(0))

                chosenOne[0].addDiscardedCard(card)
