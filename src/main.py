from controller.GameManager import GameManager
from view.View import View


if __name__ == '__main__':

    gm = GameManager(View(), 2)
    for i in range(500):
        winner = gm.run()
#        print("Winner is player " + str(winner + 1))
    gm.printAIQtable()