class SaneCard:
    """ SaneCard class (abstract) is defined by :
        - SaneCard(_name : string, _description : string, _value : int)
        - effect(sanity : Sanity)
        - hasInsane() """


    def __init__(self, _name, _description, _value):
        self.name = _name
        self.description = _description
        self.value = _value


    def hasInsane():
        return False
