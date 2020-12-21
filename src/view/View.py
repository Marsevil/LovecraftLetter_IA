import os
from model.card.Sanity import Sanity

class View():

    def setGameManager(self,gameManager):
        self.gameManager = gameManager
        
    def getGameManager(self):
        return self.gameManager

    #+chooseTargetPlayer(int : nbPlayer, List<Player> players)
    #ask for a player number
    #return a player object
    def chooseTargetPlayer(self,nbPlayer, players):
        nbPlayerStr = "There are " + str(nbPlayer) + " players in game, please choose a target"
        print(nbPlayerStr)
        playerNb = self.chooseNumber(1,nbPlayer)
        if playerNb:
            return players[playerNb-1]
    
    
    #????
    def cardCantBePlayed(self):
        print("This action cannot be done, please choose another")
    
    #Player choose between sane and insane
    def askInsanity(self):
        infoStr = "Your card can be played as Sane (1) or Insane (2) "
        print(infoStr)
        choosenState = self.chooseNumber(1,2)
        if (choosenState == 1):
            return Sanity.SANE
        else:
            if (choosenState==2):
                return Sanity.INSANE
            else:
                return None
    
    #?? Beginnnig of a new turn ?
    def redistribute(self,inGameCards):
        self.cls()
        print("In Game Cards : ")
        inGameCardsStr = ""
        for card in inGameCards:
            inGameCardsStr += card.name + ", "
        inGameCardsStr = inGameCardsStr[:-2]
        print(inGameCardsStr)


    #Choose an int number in range(min,max)
    def chooseNumber(self,minNb,maxNb):
        infoStr = "Choose a number between " + str(minNb) + " and " + str(maxNb) + " : "
        nbInput = None
        #do while 
        while True:
            try:
                nbInput = int(input(infoStr))
                if (nbInput >= minNb and nbInput <= maxNb):
                    break
            except Exception as e:
                print(e)
            
        return nbInput

    
    #???
    def showCards(self,cards):
        print("Cards : ")
        cardsStr = ""
        for card in cards:
            cardsStr += card.name + ", "
        cardsStr = cardsStr[:-2]
        print(cardsStr)
    
    #clear screen function
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
