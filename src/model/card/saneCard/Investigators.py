from ..SaneCard import SaneCard
class Investigators (SaneCard):

    def __init__(self):
        super().__init__("Investigators", "When you discard Investigators" +
                            "during your turn, choose another player and name" +
                            "a number (other than 1). If that player has that" +
                            "number in their hand, they are knocked out of" +
                            "the round. If all other players still in the" +
                            "round cannot be chosen (e.g due to Elder Sign or" +
                            "Liber Ivonis), this card is discarded without" +
                            "effect." , 1)

    def effect(self) :
        print('Not implemented yet')
