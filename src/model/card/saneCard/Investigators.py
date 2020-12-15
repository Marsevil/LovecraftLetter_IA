from ..SaneCard import SaneCard

class Investigators (SaneCard):

    def __init__(self):
        super().__init__("Investigators", "When you discard Investigators" +
        " during your turn, choose another player and name a number (other" +
        " than 1). If that player has that number in their hand, they are" +
        " knocked out of the round. If all other players still in the round" +
        " cannot be chosen (e.g due to Elder Sign or Liber Ivonis), this card" +
        " is discarded without effect." , 1)

    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity


    def effect(self, gameManager):

        #Demande à viser un autre joueur
        chosenOne = gameManager.chooseTargetPlayer(1, False)
    
        #Vérifie qu'un joueur non immunisé a pu être choisi
        if(len(chosenOne) != 0):
    
            #Demande à choisir un nombre supérieur à 1
            chosenCardNumber = gameManager.chooseNumber()
    
            #Éjecte le joueur désigné s'il possède la carte choisie et qu'il peut être éjecté
            targetHand = chosenOne.getHand()
            if ((targetHand[0].value == chosenCardNumber) and chosenOne.isKnockableOut()):
                chosenOne.setKnockedOut(True)
