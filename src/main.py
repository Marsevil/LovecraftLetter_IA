from controller.GameManager import GameManager
from view.View import View

gm = GameManager(View(), 2)
winner = gm.run()

print("Winner is player " + str(winner + 1))