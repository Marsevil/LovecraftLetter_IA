#from card.Card import Card
from .card.Sanity import Sanity

class Player:

    ##Constructor
    def __init__(self, saneToken, insaneToken, hand, discard, knockedOut, knockableOut, immune):
        #number of sane token
        self.saneToken = saneToken
        #number of insane token
        self.insaneToken = insaneToken
        self.hand = hand
        self.discard = discard
        #true if the player is knocked out of the current round
        self.knockedOut = knockedOut
        self.knockableOut = knockableOut
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
        
        nbInsane = self.nbInsaneCardDiscarded()

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

    def pickUp(self, card) :
        card.setOwner(self)
        self.hand.append(card)

    def getHand(self):
        return self.hand

    def setHand(self,hand):
        self.hand = hand
        for card in self.hand :
            card.setOwner(self)

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

    def isKnockableOut(self) :
        return self.isKnockableOut

    def setKnockableOut(self, knockableOut) :
        self.knockableOut = knockableOut

    def getImmune(self):
        return self.immune

    def setImmune(self,immune):
        self.immune = immune

    def getCardFromHand(self, cardNumber) :
        return self.hand.pop(cardNumber)

    def addDiscardedCard(self, card) :
        self.discard.append(card)