from ..InsaneCard import InsaneCard
from ..Sanity import Sanity

class HoundOfTindalos (InsaneCard):

    def __init__(self):
        super(HoundOfTindalos,self).__init__("Hound of Tindalos", "Sane : When you discard Hound of Tindalos" +
        " during your turn, choose another player. You and that" +
        " player secretly compare your hands. The player with the lower" +
        " number is knocked out of the round. In case of a tie, nothing" +
        " happens. If all other players still in the round cannot be chosen" +
        " (e.g due to Elder Sign or Liber Ivonis), this card is discarded" +
        " without effect. \n"
        +"Insane : When you discard Hound of Tindalos during your turn, choose"
        +"another player. If they are not Insane, they are knocked out of the round."
        +"If all other players still in the round cannot be chosen (e.g due to Elder"
        +"Sign or Liber Ivonis), this card is discarded without effect.", 3)

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
    
                #Cherche qui a la plus petite carte pour l'éjecter, sinon rien
                player = gameManager.getCurrentPlayer()
                playerHand = player.getHand()
                targetHand = chosenOne[0].getHand()
    
                if(playerHand[0].getValue() < targetHand[0].getValue()):
                    if(player.isKnockableOut()):
                        player.setKnockedOut(True)
                elif(playerHand[0].getValue() > targetHand[0].getValue()):
                    if(chosenOne.isKnockableOut()):
                        chosenOne.setKnockedOut(True)
                        
        if self.sanity == Sanity.INSANE:
            chosenOne = gameManager.chooseTargetPlayer(1, False)
            
            
            if(len(chosenOne) != 0):
                if chosenOne.isKnockableOut() and chosenOne.stateOfMind() != Sanity.INSANE:
                    chosenOne.setKnockedOut(True)
            