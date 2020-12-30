from ..SaneCard import SaneCard

class TheNecronomicon (SaneCard):

    def __init__(self):
        super().__init__("The Necronomicon",
        "If you ever discard The" +
        " Necronomicon—no matter how or why (so even during a Sanity Check) —" +
        " you lose the track of your cousin. You are immediately knocked out" +
        " of the round. If The Necronomicon was discarded due to a card" +
        " effect, any remaining effects of that card do not apply (you do not" +
        " draw a card from Professor Henry Armitage, for example)." , 8)

    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity


    def effect(self, gameManager):
        # You are knocked out if the round if you discard The Necronomicon if the player could be knocked out
        if(self.getOwner().isKnockableOut()):
            self.getOwner().setKnockedOut(True)
