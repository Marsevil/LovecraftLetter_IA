from card import Card, Sanity

class Player:

    ##Constructor
    def __init__(self, saneToken, insaneTocken, hand, discard, knockedOut):
        #number of sane tocken
        self.saneToken = saneToken
        #number of insane tocken
        self.insaneTocken = insaneTocken
        self.hand = hand
        self.discard = discard
        #true if the player is knocked out of the current round
        self.knockedOut = knockedOut

    def stateOfMind():
        #search the current state of mind of the player
        mind = Sanity.SANE
        
        #browse the discard pile
        for card in self.getDiscard:
            if (card.hasInsane()):
                mind = Sanity.INSANE
    
        return mind

    def updateTocken():
        #get the current state of mind
        mind = self.stateOfMind()

        #update state of mind tocken
        if (mind == Sanity.SANE):
            self.setSaneToken(self.getSaneTocken() + 1)
        else:
            self.setInsaneTocken(self.getInsaneTocken() + 1)

    def play(cardPos,effectMind):
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

    def getHand():
        return self.hand

    def setHand(hand):
        self.hand = hand

    def getDiscard():
        return self.discard

    def setDiscard(discard):
        self.discard = discard

    def getSaneTocken():
        return self.saneToken

    def setSaneTocken(saneToken):
        self.saneToken = saneToken

    def getInsaneTocken():
        return self.insaneTocken

    def setInsaneTocken(insaneToken):
        self.insaneToken = insaneToken
