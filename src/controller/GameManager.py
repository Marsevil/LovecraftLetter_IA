import random

from ..model.Player import Player
from ..model.card.Sanity import Sanity
from ..model.card.saneCard import *
from ..model.card.insaneCard import *

class GameManager:
    def __init__(self, view, nbPlayer) :
        self.view = view
        # players indice to the player currently playing.
        self.currentPlayer = 0
        # Count round from the beginning, negative number means that the game isn't started.
        self.roundNumber = -1
        # List of card defining deck.
        self.deck = []
        self.players = []
        # List of cards that are removed at the beginnig of a round
        self.removedCards = []

        # Instantiate as many players as nbPlayer defines.
        for _i in range(nbPlayer) :
            self.players.append(Player(0, 0, [], [], False, False))

        self.startNewRound()

    ## Builds deck by creating card list & shuffles it.
    @staticmethod
    def buildDeck() :
        deck = []
        # Fill the liste
        # Sane Cards
        # Once in the deck
        deck.append(TheNecronomicon())
        deck.append(TheSilverKey())
        deck.append(RandolphCarter())
        # Twice in the deck
        for _i in range(2) :
            deck.append(ProfessorHenryArmitage())
            deck.append(ElderSign())
            deck.append(GreatRaceOfYith())
            deck.append(CatsOfUlthar())
        # Five times in the deck
        for _i in range(5) :
            deck.append(Investigators())

        # Insane cards
        # once in the deck
        deck.append(Cthulhu())
        deck.append(TheShiningTrapezohedron())
        deck.append(Nyarlathotep())
        deck.append(MiGo())
        deck.append(LiberIvonis())
        deck.append(HoundOfTindalos())
        deck.append(GoldenMead())
        deck.append(DeepOnes())
        
        # Shuffle
        for _i in range(1) :
            random.shuffle(deck)

        return deck

    ## Builds a hand by drawing
    def buildHand(self) :
        hand = []
        hand.append(self.deck.pop())

        return hand

    ## Determines if the game is finished.
    def isGameEnd(self) :
        for i in range(len(self.players)) :
            player = self.players[i]
            if player.getSaneToken() >= 2 :
                return i
            if player.getInsaneToken() >= 3 :
                return i

        return -1 # -1 if no player end the game.

    ## Start a new round.
    def startNewRound(self) :
        self.currentPlayer = 0
        self.roundNumber += 1
        self.deck = GameManager.buildDeck()

        # Add Mi-Go Braincase to general discarded cards
        self.removedCards.append(MiGoBraincase())
        # Remove the top card of the deck.
        self.removedCards.append(self.deck.pop())
        # If 2 players game remove 5 other cards.
        if len(self.players) <= 2 :
            for _i in range(5) :
                self.removedCards.append(self.deck.pop())

        # Give some cards to players
        for player in self.players :
            player.setHand(self.buildHand())
            player.setKnockedOut(False)

    ## Apply effect of the card choosen by the player.
    ## @params cardNumber index of card in the hand of currentPlayer.
    def play(self, cardNumber) :
        currentPlayer = self.players[self.currentPlayer]

        # The card that the player want to play.
        card = currentPlayer.getCardFromHand(cardNumber)

        #the card that is played
        while (self.checkPlayableCard(card)) :
            currentPlayer.pickUp(card)

            card = currentPlayer.getCardFromHand(self.view.cardCantBePlayed())

        # If insane card, user can choose which effect will be used.
        if card.hasInsanity() and currentPlayer.stateOfMind == Sanity.INSANE :
            card.sanity(self.view.askInsanity())
        else :
            card.sanity(Sanity.SANE)

        # Apply card effect
        card.effect(self)

        # Push on the discard stack.
        currentPlayer.addDiscardedCard(card)

        #delete the immunity of the player if he was immune in the last round
        if(currentPlayer.getImmune()):
            currentPlayer.setImmune(False)

        # Switch to the next player.
        self.currentPlayer = self.currentPlayer + 1 if self.currentPlayer < len(self.players) else 0

        if self.deck :
            # Pick up a card
            self.players[self.currentPlayer].pickUp(self.deck.pop())

    ## Check if the round is ended.
    def isRoundEnd(self) :
        winner = self.findWinnerWthSpecialEffect()

        # All players are knocked out.
        if (winner == -1) :
            for player in range(len(self.players)) :
                if not self.players[player].getKnockedOut() :
                    if winner != -1 :
                        winner = -1
                        break

                    winner = player
            
        # Le deck est vide : chaque joueur joue la carte qu'il a en main et celui qui a la plus grosse gagne.
        if not self.players and winner == -1 :
            greaterValue = -1
            for player in range(len(self.players)) :
                value = self.players[player].getHand()[-1].getValue()
                if value > greaterValue :
                    greaterValue = value
                    winner = player
                elif value == greaterValue :
                    # Si plusieurs on le même ils sont éliminés.
                    self.players[player].setKnockedOut(True)
                    self.players[winner].setKnockedOut(True)
                    winner = self.isRoundEnd()

            if winner == -1 :
                winner = -2

        return winner

    ## @return the player who is playing.
    def getCurrentPlayer(self) :
        return self.players[self.currentPlayer]

    ## @params nbPlayer number of player to ask.
    ## @params allowCurrentPlayer if the current player could targets imself or not.
    ## @return targets choose by the current player.
    def chooseTargetPlayer(self, nbPlayer, allowCurrentPlayer) :
        notImmunePlayers = []
        for player in self.players :
            if (not player.getImmune()) and ((player != self.currentPlayer) or (allowCurrentPlayer)):
                notImmunePlayers.append(player)

        return self.view.chooseTargetPlayer(nbPlayer, notImmunePlayers)

    def getPlayers(self) :
        return self.players

    def checkPlayableCard(self, card) :
        otherCard = self.getCurrentPlayer().getHand()[0]

        if ((isinstance(otherCard, TheSilverKey) or isinstance(otherCard, TheShiningTrapezohedron)) and card.getValue() > 4) :
            return False
        else :
            return True

    ## Detect if card like The shining trapezohedron was played.
    ## @returs -1 if no card end the game. A value that point to the player who won.
    def findWinnerWthSpecialEffect(self) :
        winner = -1

        if not self.players[self.currentPlayer - 1].getKnockedOut() :

            lastCardPlayed = self.getPlayers()[self.currentPlayer - 1].getHand()[-1]

            if (isinstance(lastCardPlayed, TheShiningTrapezohedron) and lastCardPlayed.sanity == Sanity.INSANE) :
                winner = self.currentPlayer - 1 if self.currentPlayer - 1 > 0 else len(self.players) - 1

            if (isinstance(lastCardPlayed, Cthulhu) and lastCardPlayed.sanity == Sanity.INSANE) :
                winner = self.currentPlayer - 1 if self.currentPlayer - 1 > 0 else len(self.players) -1

        return winner

    def sanityCheck(self, player) :
        for _i in range(player.nbInsaneCardDiscarded()) :
            if not self.deck :
                break

            card = self.deck.pop()
            self.removedCards.append(card)

            if card.hasInsanity() :
                player.setKnockedOut(True)
                break

    ## Redistribute cards to the people according to the user choice.
    def redistribute(self) :
        inGameCards = []

        for player in self.players :
            inGameCards.extend(player.getHand())
            player.getHand().clear()

        redistributedCards = self.view.redistribute(inGameCards)

        for ip in range(len(self.players)) :
            self.players[ip].setHand(redistributedCards[ip])
