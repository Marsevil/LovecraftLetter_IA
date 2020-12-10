#from card.Card import Card
#from card.Sanity import Sanity

class Player:

    ##Constructor
    def __init__(self, saneToken, insaneToken, hand, discard, knockedOut, immune):
        #number of sane token
        self.saneToken = saneToken
        #number of insane token
        self.insaneToken = insaneToken
        self.hand = hand
        self.discard = discard
        #true if the player is knocked out of the current round
        self.knockedOut = knockedOut
        #true if the player is immuned to card effect of other players for the current round
        self.immune = immune

    def nbInsaneCardDiscarded(self):
        #seach the number of insane card in the discard pile
        nbInsane = 0

        #browse the discard pile
        for card in self.getDiscard():
            if (card.hasInsane()):
                nbInsane += 1

        return nbInsane

    def stateOfMind(self):
        #search the current state of mind of the player
        mind = Sanity.SANE
        
        nbInsane = self.stateOfMind()

        if (nbInsane != 0):
            mind = Sanity.INSANE
    
        return mind

    def updateToken(self):
        #get the current state of mind
        mind = self.stateOfMind()
         
        #update state of mind token
        if (mind == Sanity.SANE):
            self.setSaneToken(self.getSaneToken() + 1)
        else:
            self.setInsaneToken(self.getInsaneToken() + 1)

    def play(self,cardPos,effectSanity):
        #delete the immunity of the player if he was immune in the last round
        if(self.getImmune):
            self.setImmune(False)

        #the card that is played
        card = self.getHand()[cardPos]

        #apply the effect of the card
        card.effect(effectSanity)

        #move the card in the discard pile
        newDiscard = self.getDiscard().push(card)
        self.setDiscard(newDiscard)
        newHand = self.getHand().remove(card)
        self.setHand(newHand)

    def getHand(self):
        return self.hand

    def setHand(self,hand):
        self.hand = hand

    def getDiscard(self):
        return self.discard

    def setDiscard(self,discard):
        self.discard = discard

    def getSaneToken(self):
        return self.saneToken

    def setSaneToken(self,saneToken):
        self.saneToken = saneToken

    def getInsaneToken(self):
        return self.insaneToken

    def setInsaneToken(self,insaneToken):
        self.insaneToken = insaneToken

    def getKnockedOut(self):
        return self.knockedOut

    def setKnockedOut(self,knockedOut):
        self.knockedOut = knockedOut

    def getImmune(self):
        return self.immune

    def setImmune(self,immune):
        self.immune = immune