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
