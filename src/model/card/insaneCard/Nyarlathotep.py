from ..InsaneCard import InsaneCard
from ..Sanity import Sanity

class Nyarlathotep(InsaneCard):

    def __init__(self):
        super(Nyarlathotep,self).__init__("Nyarlathotep",
        "Sane : When you discard Nyarlathotep" +
        " during your turn, choose another player and trade your hand with" +
        " them. You cannot trade with a player who has been knocked out of" +
        " the round.\n" +
        "Insane : When you discard Nyarlathotep during your" +
        " turn, collect the hands of all the other players still in the" +
        " round. You may look at them. Then redistribute one card of your" +
        " choice to each player. This effect does not put their cards in your" +
        " hand, thus you cannot give the card you have in hand away.", 6)


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
            #Demande à viser un autre joueur
            chosenOne = gameManager.chooseTargetPlayer(1, False)

            #Vérifie qu'un joueur non immunisé a pu être choisi
            if(len(chosenOne) != 0):

                #Échange la main avec le joueur
                player = self.getOwner()
                target = chosenOne[0]

                temp = player.getCardFromHand(0)
                player.pickUp(target.getCardFromHand(0))
                target.pickUp(temp)

        if self.sanity == Sanity.INSANE:
            # Call the function to show all the players card and to redistribute
            gameManager.redistribute()

    
