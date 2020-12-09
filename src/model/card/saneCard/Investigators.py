from SaneCard import SaneCard

class Investigators (SaneCard):

    @abstractmethod
    def __init__(self):
        super().__init__(_name, _description, _value)
