import SaneCard

## Describe AbstractInsaneCard
class InsaneCard(SaneCard):

    ## Constructor
    def __init__(self, _name, _description, _value):
        super().__init__(_name, _description, _value)

    ## @inherit
    def effect(sanity):
        pass

    ## @inherit
    def hasInsane():
        return True
