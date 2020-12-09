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

    def updateTocken(self):
        #get the current state of mind
        mind = self.stateOfMind()
         
        #update state of mind tocken
        if (mind == Sanity.SANE):
            self.setSaneToken(self.getSaneTocken() + 1)
        else:
            self.setInsaneTocken(self.getInsaneTocken() + 1)

    def play(self,cardPos,effectMind):
        #delete the immunity of the player if he was immune in the last round
        if(self.getImmune):
            self.setImmune(False)

        #the card that is played
        card = self.getHand()[cardPos]

        #check if the player can apply an insane effect
        #and if the card has an insane effect
        if(effectMind == Sanity.INSANE):

            #get the current state of mind
            mind = self.stateOfMind()
         
            cardInsane = card.hasInsane()

            #if playing an insane effect is impossible
            #force to apply the sane one
            if((mind != Sanity.INSANE) or (not cardInsane)):
                effectMind = Sanity.Sane

        #apply the effect of the card
        card.effect(effectMind)

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