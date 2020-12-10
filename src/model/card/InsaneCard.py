from .SaneCard import SaneCard
from abc import ABC, abstractmethod

## Describe AbstractInsaneCard
class InsaneCard(SaneCard):

    ## Constructor
    @abstractmethod
    def __init__(self, _name, _description, _value):
        super().__init__(_name, _description, _value)

    ## @inherit
    @staticmethod
    def hasInsane():
        return True
