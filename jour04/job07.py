import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        paquet = [Carte(valeur, couleur) for couleur in couleurs for valeur in valeurs]
        return paquet

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def donner_cartes(self, nombre_cartes):
        cartes = []
        for _ in range(nombre_cartes):
            carte = self.paquet.pop()
            cartes.append(carte)
        return cartes

def calculer_points(main):
    total_points = 0
    nombre_as = 0

    for carte in main:
        if carte.valeur in ['Valet', 'Dame', 'Roi']:
            total_points += 10
        elif carte.valeur == 'As':
            nombre_as += 1
        else:
            total_points += int(carte.valeur)

    for _ in range(nombre_as):
        if total_points + 11 <= 21:
            total_points += 11
        else:
            total_points += 1

    return total_points

def jouer_partie():
    jeu = Jeu()
    jeu.melanger_paquet()

    main_joueur = jeu.donner_cartes(2)
    main_croupier = jeu.donner_cartes(2)

    print("Main du joueur:")
    for carte in main_joueur:
        print(f"{carte.valeur} de {carte.couleur}")

    while True:
        choix = input("Voulez-vous prendre une carte ? (Oui/Non): ").lower()
        if choix == 'oui':
            nouvelle_carte = jeu.donner_cartes(1)[0]
            main_joueur.append(nouvelle_carte)
            print(f"Vous avez pioché un {nouvelle_carte.valeur} de {nouvelle_carte.couleur}")
            points_joueur = calculer_points(main_joueur)
            print(f"Total des points du joueur : {points_joueur}")

            if points_joueur > 21:
                print("Vous avez dépassé 21. Vous avez perdu.")
                break
        elif choix == 'non':
            break
        else:
            print("Veuillez entrer une réponse valide (Oui/Non).")

    while calculer_points(main_croupier) < 17:
        nouvelle_carte = jeu.donner_cartes(1)[0]
        main_croupier.append(nouvelle_carte)

    print("\nMain du croupier:")
    for carte in main_croupier:
        print(f"{carte.valeur} de {carte.couleur}")

    points_joueur = calculer_points(main_joueur)
    points_croupier = calculer_points(main_croupier)

    print(f"\nTotal des points du joueur : {points_joueur}")
    print(f"Total des points du croupier : {points_croupier}")

    if points_joueur > 21:
        print("Vous avez dépassé 21. Vous avez perdu.")
    elif points_croupier > 21:
        print("Le croupier a dépassé 21. Vous avez gagné!")
    elif points_joueur > points_croupier:
        print("Vous avez plus de points que le croupier. Vous avez gagné!")
    elif points_joueur < points_croupier:
        print("Le croupier a plus de points que vous. Vous avez perdu.")
    else:
        print("Égalité!")


jouer_partie()