# LovecraftLetter_IA

## Comment jouer ?

Le *main* peut prendre plusieurs arguments `python3 main.py [nb joueur humain] [nb IA] [nb Parties]`

### Pour jouer à deux joueurs (humains)

- Se placer dans le répertoire source : `cd src`
- Lancer le jeu avec deux humains : `python3 main.py 2 0 1`

### Pour jouer contre une IA

- Se placer dans le répertoire source : `cd src`
- Lancer le jeu avec une IA et un humain (comportement par défaut) : `python3 main.py 1 1 1` **ou** `python3 main.py`

### Faire jouer des IAs

- Se placer dans le répertoire source : `cd src`
- Lancer le jeu avec zéro joueur humain et deux IAs : `python3 main.py 0 2 [nombre de parties]`

## Où trouver la QTable

La *QTable* se trouve à la racine du projet sous le nom `AIQtable.txt` elle sera générée après une première exécution du jeu, il est donc intéréssant de jouer 100 000 parties *IA vs IA* puis de faire une partie *humain vs IA*.