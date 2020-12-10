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
