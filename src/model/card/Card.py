from abc import ABC, abstractmethod


"""@package card
Card abstract class for IA41 LoveCraftLetter.
General eprensentation of a game card.
"""
class Card(ABC):
    
    """
    @name Name of the card
    @description Description of what the card does
    @value Number of the card, used to determine game winner.
    """
    @abstractmethod
    def __init__(self,name,description,value):
        self._name = name
        self._description = description
        self._value = value

    
    @property
    def name(self):
        ...
        
    @name.setter
    @abstractmethod
    def name(self, newvalue):
        ...
        
    @abstractmethod
    def getName(self):
        ...

    @property
    def description(self):
        ...
        
    @description.setter
    @abstractmethod
    def description(self, newvalue):
        ...
        
    @abstractmethod
    def getDescription(self):
        ...
        
    @property
    def value(self):
        ...
        
    @value.setter
    @abstractmethod
    def value(self, newvalue):
        ...
        
    @abstractmethod
    def getValue(self):
        ...

    @property
    def sanity(self):
        ...
        
    @sanity.setter
    @abstractmethod
    def sanity(self, newvalue):
        ...
        
    @abstractmethod
    def getSanity(self):
        ...
        
    @abstractmethod
    def hasInsane(self):
        ...
    
    @abstractmethod
    def effect(self,sanity):
        ...
