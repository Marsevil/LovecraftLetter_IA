from ..InsaneCard import InsaneCard
from ..Sanity import Sanity

class TheShiningTrapezohedron(InsaneCard):

    def __init__(self):
        super(TheShiningTrapezohedron,self).__init__("The Shining Trapezohedron",
        "Sane : Unlike other cards, whose effects" +
        " are applied when they are discarded, the text of The Shining Trapezohedron" +
        " only applies when it is in your hand. If you ever have The Shining" +
        " Trapezohedron and another card that has a number higher than 4 in your hand," +
        " you must discard The Shining Trapezohedron. Of course, you can always decide" +
        " to discard The Shining Trapezohedron when that is not the case, to play mind" +
        " games with the other players...\n" +
        "Insane : Unlike other cards," +
        " whose effects are applied when they are discarded, the text of The" +
        " Shining Trapezohedron only applies when it is in your hand. If you" +
        " ever have The Shining Trapezohedron and another card that has a" +
        " number higher than 4 in your hand, you win the round.", 7)

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
