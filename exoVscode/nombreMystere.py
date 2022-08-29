"""
Le but de ce projet est de permettre à un joueur d'essayer de deviner un nombre mystère généré aléatoirement par l'ordinateur, en 5 essais ou moins.
👉 Déroulé du script
Au début du script, vous devez générer un nombre aléatoire compris entre 0 et 100 (vous pouvez agrandir ou réduire cet intervalle pour simplifier ou complexifier le jeu).
Le joueur dispose alors de 5 essais (là encore, libre à vous de changer cette valeur) pour trouver le nombre mystère.
À chaque essai, vous devez indiquer au joueur si le nombre qu'il a entré est plus petit ou plus grand que le nombre mystère.
Si le nombre entré par l'utilisateur est égal au nombre mystère, alors le joueur gagne la partie.
Dans le cas d'une victoire, vous devez indiquer au joueur combien d'essais lui ont été nécessaire pour gagner.
Si le joueur ne trouve pas le nombre mystère avec les 5 essais disponibles, il perd la partie.
"""

import random

# i = 1
# for i in range(50):
#     nbRandom = random.randint(0, 100)
#     print(nbRandom)
#     i +=1


import sys
nbRandom = random.randint(0, 100)
nbFois = 0

while True:

    nbFois +=1
    answer = int(input("donner un nombre entre 1 et 100"))
    if answer != nbRandom:
        if nbRandom > answer and nbFois <= 5:
            print(f"Le nombre recherché est plus grand que {answer}")
        elif nbRandom < answer and nbFois <= 5:
            print(f"Le nombre recherché est plus petit que {answer}")
        else:
            print(f"Oups ça fait {nbFois} fois que vous essayez, vous avez perdu !")
            print(f"Le nombre recherché était {nbRandom}")
            sys.exit()
    else:
        print(f"Bravo le nombre était bien {nbRandom}, et vous l'avez trouvé en {nbFois} coups")
        sys.exit()


