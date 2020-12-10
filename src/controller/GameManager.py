from ..model.Player import Player
from ..model.card.Sanity import Sanity

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
        # Fill the liste
        # Shuffle
        # Suppress the first
        print('Not implemented yet : model.Player.buildDeck()')
        deck = []
        for i in range(30) :
            deck.append('card' + str(i))

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
            if player.getDiscard[-1].getName() == "Chtulhu" :
                return i

        return -1 # -1 if no player end the game.

    ## Start a new round.
    def startNewRound(self) :
        self.currentPlayer = 0
        self.roundNumber += 1
        self.deck = GameManager.buildDeck()

        # Remove the top card of the deck.
        self.removedCards.append(self.deck.pop())

        # If 2 players game remove 5 other cards.
        if len(self.players) <= 2 :
            for i in range(5) :
                self.removedCards.append(self.deck.pop())

        # Give some cards to players
        for player in self.players :
            player.setHand(self.buildHand())
            player.setKnockedOut(False)

    ## Apply effect of the card choosen by the player.
    ## @params cardNumber index of card in the hand of currentPlayer.
    def play(self, cardNumber) :
        currentPlayer = self.players[self.currentPlayer]

        #the card that is played
        card = currentPlayer.getCardFromHand(cardNumber)

        # If insane card, user can choose which effect will be used.
        if card.hasInsanity() :
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
        # All players are knocked out.
        winner = -1
        for player in range(len(self.players)) :
            if self.players[player].getKnockedOut() :
                if winner == -1 :
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

