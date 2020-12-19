from ..InsaneCard import InsaneCard
from ..Sanity import Sanity


class DeepOnes (InsaneCard):

    def __init__(self):
        super(DeepOnes,self).__init__("Deep Ones", "Sane : When you discard Investigators" +
        " during your turn, choose another player and name a number (other" +
        " than 1). If that player has that number in their hand, they are" +
        " knocked out of the round. If all other players still in the round" +
        " cannot be chosen (e.g due to Elder Sign or Liber Ivonis), this card" +
        " is discarded without effect. \n" 
        +"Insane : When you discard Deep Ones during your turn, choose another"
        +"player. If they have a 1 in their hand, they are knocked out of the round. If"
        +"they do not, you name a number (other than 1). If they have that number"
        +"in their hand, they are knocked out of the round."
        +"If all other players still in the round cannot be chosen (e.g due to Elder"
        +"Sign or Liber Ivonis), this card is discarded without effect.", 1)

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
    
                #Demande à choisir un nombre supérieur à 1
                chosenCardNumber = gameManager.chooseNumber()
    
                #Éjecte le joueur désigné s'il possède la carte choisie et qu'il peut être éjecté
                targetHand = chosenOne[0].getHand()
                if ((targetHand[0].value == chosenCardNumber) and chosenOne.isKnockableOut()):
                    chosenOne.setKnockedOut(True)

        if self.sanity == Sanity.INSANE:
            #Demande à viser un autre joueur
            chosenOne = gameManager.chooseTargetPlayer(1, False)
    
            #Vérifie qu'un joueur non immunisé a pu être choisi
            if(len(chosenOne) != 0):
                targetHand = chosenOne[0].getHand()
                
                if (targetHand[0].value == 1):
                    if chosenOne[0].isKnockableOut():
                        chosenOne[0].setKnockedOut(True)
                else:
                    chosenCardNumber = gameManager.chooseNumber()
                    if ((targetHand[0].value == chosenCardNumber) and chosenOne[0].isKnockableOut()):
                        chosenOne[0].setKnockedOut(True)