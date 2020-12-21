from view.View import View
from model.Player import Player
from controller.GameManager import GameManager
from model.card.insaneCard import *

if __name__ == '__main__':
    print("test")
    p = Player(0, 0, [], [], False, False)
    LP=View()
    gameManager = GameManager(LP,2)
    LP.cls()
#    LP.chooseTargetPlayer(8,None)
#    print(LP.chooseNumber(1,10))
#    print(LP.askInsanity())
    
    
    listCards = [DeepOnes(),GoldenMead(),LiberIvonis()]
    newList = LP.redistribute(listCards)
    strT = ""
    for c in newList:
        strT += c.name
    print(strT)