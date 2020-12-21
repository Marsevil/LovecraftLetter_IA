import os
from model.card.Sanity import Sanity

class View():

    """
    Ask for a number and return the player at this number from the list of players
    @params nbPlayer, number of players
    @params players, list of players
    @return selected player object
    """
    def chooseTargetPlayer(self,nbPlayer, players):
        self.cls()
        nbPlayerStr = "There are " + str(nbPlayer) + " players in game, please choose a target"
        print(nbPlayerStr)
        playerNb = self.chooseNumber(1,nbPlayer)
        if playerNb:
            return players[playerNb-1]
    
    
    """
    Wrong action display function
    """
    def cardCantBePlayed(self):
        print("This action cannot be done, please choose another")
    
    """
    Choose between Sane and Insane
    @return SANE or INSANE enum value (None in case of error)
    """
    def askInsanity(self):
        self.cls()
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
    
    """
    Re order a list of card
    @params inGameCards, list of card who need to be reordered
    @return list of card reordered
    """
    def redistribute(self,inGameCards):
        self.cls()
        cardsStr = "Cards : "
        for card in inGameCards:
            cardsStr += card.name + ", "
        cardsStr = cardsStr[:-2]
        cardsStr += " need to be redistribute to each player "
        print(cardsStr)
        
        nbPlayers = len(inGameCards)
        newCardsOrder = inGameCards.copy()
        playerNbAvailable = []
        for i in range(1,nbPlayers+1):
            playerNbAvailable.append(i)
        
        while len(inGameCards) > 0:
            #retrieve last card from list
            currentCard = inGameCards.pop()
            print("Distribute '" + currentCard.name + "' to a player (number) in this list : " + str(playerNbAvailable))
            nbInput = None
            while True:
                try:
                    nbInput = int(input())
                    if nbInput in playerNbAvailable:
                        break
                    else:
                        print("Wrong number please retry")
                except Exception as e:
                    print(e)
            newCardsOrder[nbInput-1] = currentCard
            playerNbAvailable.remove(nbInput)

        return newCardsOrder

    """
    @params minNb, min value
    @params maxNb, max value
    @return number between min and max
    """
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

    
    """
    Display a list of cards
    @params cards, list of cards
    """
    def showCards(self,cards):
        self.cls()
        print("Cards : ")
        cardsStr = ""
        for card in cards:
            cardsStr += card.name + ", "
        cardsStr = cardsStr[:-2]
        print(cardsStr)
    
    """
    Clear screen function
    """
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
