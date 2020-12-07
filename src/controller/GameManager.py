from ..model.Player import Player

class GameManager:
    def __init__(self, nbPlayer) :
        # players indice to the player currently playing.
        self.currentPlayer = 0
        # Count round from the beginning, negative number means that the game isn't started.
        self.roundNumber = -1
        # List of card defining deck.
        self.deck = []

        # Instantiate as many players as nbPlayer defines.
        for i in range(nbPlayer) :
            self.players = []
            self.players[i] = Player(0, 0, [], [], False)

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
            deck.append('card' + i)
        return deck

    ## Builds a hand by drawing
    def buildHand(self) :
        hand = []
        hand.append(self.deck.pop())

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

    def startNewRound(self) :
        self.currentPlayer = 0
        self.roundNumber += 1
        self.deck = GameManager.buildDeck()

        # If 2 players game throw 5 cards.
        if len(self.players) <= 2 :
            del self.deck[-5:]

        # Give some cards to players
        for player in self.players :
            player.setHand(self.buildHand())
