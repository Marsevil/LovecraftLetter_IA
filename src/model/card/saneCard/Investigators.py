from ..SaneCard import SaneCard
class Investigators (SaneCard):

    def __init__(self):
        super().__init__("Investigators", "When you discard Investigators" +
                            "during your turn, choose another player and name" +
                            "a number (other than 1). If that player has that" +
                            "number in their hand, they are knocked out of" +
                            "the round. If all other players still in the" +
                            "round cannot be chosen (e.g due to Elder Sign or" +
                            "Liber Ivonis), this card is discarded without" +
                            "effect." , 1)

    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity


    def effect(self, gameManager):
        #Demande à viser 1 joueur
        chosenOne = gameManager.chooseTargetPlayer(1)

        #Demande à choisir un nombre supérieur à 1
        chosenCard = gameManager.chooseNumber()

        #Éjecte le joueur désigné s'il possède la carte choisie
        hand = chosenOne.getHand()
        for(i in range (hand)):
            if (hand[i] == chosenCard):
                chosenOne.knockedOut = True
