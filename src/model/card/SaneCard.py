class SaneCard (Card):
    """ SaneCard class (abstract) is defined by :
        - SaneCard(_name : string, _description : string, _value : int)
        - effect(sanity : Sanity)
        - hasInsane() """


    def __init__(self, _name, _description, _value):
        super().__init__(_name, _description, _value)


    def hasInsane():
        return False
