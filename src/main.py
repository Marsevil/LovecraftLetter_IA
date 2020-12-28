from controller.GameManager import GameManager
from view.View import View

gm = GameManager(View(), 2)
gm.run()