from ..SaneCard import SaneCard

class CatsOfUlthar(SaneCard):
    
    def __init__(self):
        super(CatsOfUlthar,self).__init__("CatsOfUlthar",
                       "When you discard Cats of Ulthar during your turn, choose another player and look at their hand. Do not reveal it to any other players. If all other players still in the round cannot be chosen (e.g due to Elder Sign or Liber Ivonis), this card is discarded without effect.)",
                       2)
    
    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, newvalue):
        self._name = newvalue


    def getName(self):
        return self._name
    
    @property
    def description(self):
        return self._description


    @description.setter
    def description(self, newvalue):
        self._description = newvalue


    def getDescription(self):
        return self._description

    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, newvalue):
        self._value = newvalue


    def getValue(self):
        return self._value
    
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
    
