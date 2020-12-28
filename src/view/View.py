import os
from model.card.Sanity import Sanity

class View():
    
    """
    Ask for a number and return the player at this number from the list of players
    @params nbPlayer, number of players to choose
    @params players, list of players
    @return selected player object
    """
    def chooseTargetPlayer(self,nbPlayer, players):
        self._displayNewAction()
        playersAvailable = []
        for i in range(len(players)):
            playersAvailable.append(i+1)
        choosenPlayersList =[]
        while len(choosenPlayersList) < nbPlayer:
            print("Please choose a target (number) in this list : " + str(playersAvailable))
            nbInput = None
            while True:
                try:
                    nbInput = int(input())
                    if nbInput in playersAvailable:
                        break
                    else:
                        print("Wrong number please retry")
                except Exception as e:
                    print(e)
            choosenPlayersList.append(players.pop(nbInput-1-len(choosenPlayersList)))
            playersAvailable.remove(nbInput)
        return choosenPlayersList
    
    """
    Ask for which card to play
    @params playerHand, playable cards
    @çeturn card object
    """
    def cardToPlay(self,playerHand):
        self._displayNewAction()
        cardStr = "You can play " + playerHand[0].name + "(1) or " + playerHand[1].name + "(2) (You can also view cards info with 3)"
        print(cardStr)
        cardNb = self.chooseNumber(1,3)
        #Display cards info
        if cardNb == 3:
            self.showCards(playerHand)
            cardNb = self.chooseNumber(1,2)
#        if cardNb:
        return cardNb-1
#        return None
    
    
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
        self._displayNewAction()
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
        self._displayNewAction()
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
        self._displayNewAction()
        print("Cards : ")
        for card in cards:
            print("\t Name : " + card.name)
            print("\t Value : " + str(card.value))
            print("\t Effect : \n\t\t" + card.description)
            print("")
    
    """
    Discard hand function
    
    """
    def playerDiscard(self,player,nbCard):
        returnList = []
        returnList.append(self.cardToPlay(player.hand))
        return returnList
#        hand = player.hand
#        handStr = ""
#        for card in hand:
#            handStr += str(card.name) + ", "
#        handStr = handStr[:-2]
#        discardStr = "You need to discard " + str(nbCard) + " cards from "+ handStr
    
    
    
    """
    Display Turn and Round info
    """
    def displayNewTurn(self,gameManager):
        self.cls()
        currentPlayer = gameManager.currentPlayer
        roundNumber = gameManager.roundNumber
        infoStr = "========================"
        infoStr1 = "Round number "+ str(roundNumber)
        infoStr2 = "Player number " + str(currentPlayer) + " playing"
        print(infoStr)
        print(infoStr1)
        print(infoStr2)
        print(infoStr)
    
    
    """
    Display new action
    """
    def _displayNewAction(self):
        print("----------------------------------------------------------")
    
    """
    Clear screen function
    """
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')
