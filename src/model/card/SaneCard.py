from .Card import Card
from abc import ABC, abstractmethod


class SaneCard (Card):
    """ SaneCard class (abstract) is defined by :
        - SaneCard(_name : string, _description : string, _value : int)
        - effect(sanity : Sanity)
        - hasInsane() """

    @abstractmethod
    def __init__(self, _name, _description, _value):
        super().__init__(_name, _description, _value)

    @staticmethod
    def hasInsane():
        return False
