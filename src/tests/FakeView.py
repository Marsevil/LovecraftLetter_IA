from src.model.card.Sanity import Sanity

class FakeView :
    def __init__(self, gameManager) :
        self.gm = gameManager

    def chooseTargetPlayer(self, nbPlayer, players) :
        choosen = []
        choosen.append(players[-1])

        return choosen

    def chooseNumber(self) :
        return 3

    def showCards(self, cards) :
        for card in cards :
            print(card.getName())

    def cardCantBePlayed(self) :
        print("Card can't be played use another :")
        newI = int(input(">"))

        return newI