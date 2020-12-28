import random


#import when running testMain.py in src
from model.Player import Player
#from ..model.Player import Player
from model.card.Sanity import Sanity
#from ..model.card.Sanity import Sanity
from model.card.saneCard import *
#from ..model.card.saneCard import *
from model.card.insaneCard import *
#from ..model.card.insaneCard import *

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
            self.players.append(Player(0, 0, [], [], False, True, False))

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

        #delete the immunity of the player if he was immune in the last round
        if(currentPlayer.getImmune()):
            currentPlayer.setImmune(False)

        # The card that the player want to play.
        card = currentPlayer.getCardFromHand(cardNumber)

        #the card that is played
        while (not self.checkPlayableCard(card)) :
            currentPlayer.pickUp(card)

            card = currentPlayer.getCardFromHand(self.view.cardCantBePlayed())

        card.sanity = self.askInsanity(card)

        # Apply card effect
        card.effect(self)

        # Push on the discard stack.
        currentPlayer.addDiscardedCard(card)

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

        for i in range(len(self.players)) :
            player = self.players[i]

            if not player.getKnockedOut() and player.hand :

                lastCardPlayed = player.getDiscard()[-1]

                if (
                    isinstance(lastCardPlayed, TheShiningTrapezohedron)
                    and lastCardPlayed.sanity == Sanity.INSANE
                    and player.getHand()[0].getValue() > 4
                ) :
                    winner = i
                    break

                if (isinstance(lastCardPlayed, Cthulhu) and lastCardPlayed.sanity == Sanity.INSANE) :
                    winner = i
                    break

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

    ## Ask to the view a number > 1
    def chooseNumber(self) :
        while True :
            number = self.view.chooseNumber()

            if number > 1 :
                break

        return number

    ## Send hand to the view to be shown
    ## @params hand is a list of cards
    def showHandToCurrent(self, hand) :
        self.view.showCards(hand)

    ## @params card is a Card.
    ## @return Sanity.SANE if its the only one possibility else ask to the view.
    def askInsanity(self, card) :
        # If insane card, user can choose which effect will be used.
        if card.hasInsane() and self.getCurrentPlayer().stateOfMind() == Sanity.INSANE :
            return self.view.askInsanity()
        else :
            return Sanity.SANE

    ## Draw nbCard for the player
    ## @params player who cards will be given.
    ## @params nbCard number of card which have to be given to the player.
    def playerDraw(self, player, nbCard) :
        for _i in range(nbCard) :
            if self.deck :
                player.pickUp(self.deck.pop())

    ## Discard nbCard from the hand of player.
    ## @params player who discard the cards.
    ## @params nbCard number of cards which must be discarded.
    def playerDiscard(self, player, nbCard) :
        discardedCard = self.view.playerDiscard(player, nbCard)

        for i in discardedCard :
            player.addDiscardedCard(player.getCardFromHand(i))

    ## Loop for each round.
    def run(self) :
        gameWinner = -1

        # Game loop
        while True :

            self.startNewRound()
            roundWinner = -1

            # Round loop
            while True :
                # Player draw a card
                self.playerDraw(self.getCurrentPlayer(), 1)
                # Choose a card to play & apply effect.
                self.play(self.view.cardToPlay(self.getCurrentPlayer().getHand()))
                # Switch to the next player
                self.currentPlayer = self.currentPlayer + 1 if self.currentPlayer < len(self.players) else 0

                # Check if the round is not end.
                roundWinner = self.isRoundEnd()
                if roundWinner != -1 :
                    break

            gameWinner = self.isGameEnd()
            if gameWinner != -1 :
                break
