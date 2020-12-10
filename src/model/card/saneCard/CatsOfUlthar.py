from ..SaneCard import SaneCard

class CatsOfUlthar(SaneCard):
    
    def __init__(self):
        super(CatsOfUlthar,self).__init__("CatsOfUlthar",
                       "When you discard Cats of Ulthar during your turn, choose another player and look at their hand. Do not reveal it to any other players. If all other players still in the round cannot be chosen (e.g due to Elder Sign or Liber Ivonis), this card is discarded without effect.)",
                       2)
    
    @property
    def sanity(self):
        return self._sanity


    @sanity.setter
    def sanity(self, newvalue):
        self._sanity = newvalue


    def getSanity(self):
        return self._sanity
    
    def effect(self,gameManager):
        pass
    
chat = CatsOfUlthar()
print(chat.value)