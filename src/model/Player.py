from card import Card
from card import Sanity

class Player:

    ##Constructor
    def __init__(self, saneToken, insaneTocken, hand, discard, knockedOut, immune):
        #number of sane tocken
        self.saneToken = saneToken
        #number of insane tocken
        self.insaneTocken = insaneTocken
        self.hand = hand
        self.discard = discard
        #true if the player is knocked out of the current round
        self.knockedOut = knockedOut
        #true if the player is immuned to card effect of other players for the current round
        self.immune = immune

    def stateOfMind(self):
        #search the current state of mind of the player
        mind = Sanity.SANE
        
        #browse the discard pile
        for card in self.getDiscard(card):
            if (card.hasInsane(card)):
                mind = Sanity.INSANE
    
        return mind

    def updateTocken(self):
        #get the current state of mind
        mind = self.stateOfMind(self)

        #update state of mind tocken
        if (mind == Sanity.SANE):
            self.setSaneToken(self,self.getSaneTocken(self) + 1)
        else:
            self.setInsaneTocken(self,self.getInsaneTocken(self) + 1)

    def play(self,cardPos,effectMind):
        #the card that is played
        card = self.getHand(self)[cardPos]

        #check if the player can apply an insane effect
        #and if the card has an insane effect
        if(effectMind == Sanity.INSANE):

            #get the current state of mind
            mind = self.stateOfMind(self)

            cardInsane = card.hasInsane(card)

            #if playing an insane effect is impossible
            #force to apply the sane one
            if((mind != Sanity.INSANE) or (not cardInsane)):
                effectMind = Sanity.Sane

        #apply the effect of the card
        card.effect(card,effectMind)

        #move the card in the discard pile
        newDiscard = self.getDiscard(self).push(card)
        self.setDiscard(self,newDiscard)
        newHand = self.getHand(self).remove(card)
        self.setHand(self,newHand)

    def getHand(self):
        return self.hand

    def setHand(self,hand):
        self.hand = hand

    def getDiscard(self):
        return self.discard

    def setDiscard(self,discard):
        self.discard = discard

    def getSaneTocken(self):
        return self.saneToken

    def setSaneTocken(self,saneToken):
        self.saneToken = saneToken

    def getInsaneTocken(self):
        return self.insaneTocken

    def setInsaneTocken(self,insaneToken):
        self.insaneToken = insaneToken

    def getKnockedOut(self):
        return self.knockedOut

    def setKnockedOut(self,knockedOut):
        self.knockedOut = knockedOut

    def getImmune(self):
        return self.immune

    def setImmune(self,immune):
        self.immune = immune