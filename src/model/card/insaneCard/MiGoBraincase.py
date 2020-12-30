from ..InsaneCard import InsaneCard
from ..Sanity import Sanity

class MiGoBraincase(InsaneCard):
    
    def __init__(self):
        super(MiGoBraincase,self).__init__("Mi-Go Braincase",
        "Sane : When you discard" +
        "this card during your turn, you lose the round.\n" +
        "Insane : When you discard this card during your turn, you lose the round", 0)
        
    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity


    def effect(self, gameManager):
        
        if self.sanity == Sanity.SANE or self.sanity == Sanity.INSANE:
            self.getOwner().setKnockedOut(True)