#coding: utf-8

class Player:

    def __init__(self, saneToken, insaneTocken, hand, discard, knockedOut):
        #number of sane tocken
        self.saneToken = saneToken
        #number of insane tocken
        self.insaneTocken = insaneTocken
        self.hand = hand
        self.discard = discard
        #true if the player is knocked out of the current round
        self.knockedOut = knockedOut
    
    def updateTocken():
        #the state of mind of the player
        mind = "sane"

        #browse the discard pile
        for card in self.getDiscard:
            if (card.hasInsane()):
                mind = "insane"

        #update state of mind tocken
        if (mind == "sane"):
            self.setSaneToken(self.getSaneTocken() + 1)
        else:
            self.setInsaneTocken(self.getInsaneTocken() + 1)

    def play():
        return 0
        
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

