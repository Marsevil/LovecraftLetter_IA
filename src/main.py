import sys

from controller.GameManager import GameManager
from view.View import View


if __name__ == '__main__':

    nbPlayer = 1
    nbAI = 1
    nbIteration = 1

    #Argument control
    if len(sys.argv) >= 4 :
        nbPlayer = int(sys.argv[1])
        nbAI = int(sys.argv[2])
        nbIteration = int(sys.argv[3])

    gm = GameManager(View(), nbPlayer, nbAI)
    for i in range(nbIteration) :
        winner = gm.run()
#        print("Winner is player " + str(winner + 1))
    gm.printAIQtable()