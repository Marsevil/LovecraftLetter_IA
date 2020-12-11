from ..SaneCard import SaneCard

class TheSilverKey (SaneCard):

    def __init__(self):
        super().__init__("The Silver Key", "Unlike other cards, whose effects" +
        " are applied when they are discarded, the text of The Silver Key" +
        " only applies when it is in your hand. If you ever have The Silver" +
        " Key and another card that has a number higher than 4 in your hand," +
        " you must discard The Silver Key. Of course, you can always decide" +
        " to discard The Silver Key when that is not the case, to play mind" +
        "games with the other players..." , 7)

    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity


    def effect(self, gameManager):
        pass


    def whenDraw(self, gameManager):
        # Get player hand
        player = gameManager.getCurrentPlayer()
        playerHand = player.getHand()

        # Check if the card in hand before picking Silver Key has a value > 4
        if(playerHand[0].getValue() > 4):
            # Insérer fonction qui oblige le joueur à discard playerHand[1]

        # Sinon il peut jouer la carte qu'il veut donc je crois qu'il n'y a
        # rien à rajouter ici
