import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        degats = random.randint(1, 10)  # Attaque avec des dégâts aléatoires entre 1 et 10
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts.")
        adversaire.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancerJeu(self):
        self.choisirNiveau()

        points_vie_joueur = self.niveau * 10
        points_vie_ennemi = self.niveau * 10

        joueur = Personnage("Joueur", points_vie_joueur)
        ennemi = Personnage("Ennemi", points_vie_ennemi)

        print(f"Vous avez choisi le niveau {self.niveau}. Que le combat commence!\n")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)

            print(f"{joueur.nom} - Vie: {joueur.vie} | {ennemi.nom} - Vie: {ennemi.vie}\n")

        self.verifierGagnant(joueur, ennemi)

    def verifierGagnant(self, joueur, ennemi):
        if joueur.vie <= 0 and ennemi.vie <= 0:
            print("Match nul! Les deux combattants sont épuisés.")
        elif joueur.vie <= 0:
            print(f"{ennemi.nom} a gagné! {joueur.nom} est vaincu.")
        else:
            print(f"{joueur.nom} a gagné! {ennemi.nom} est vaincu.")

# Exécution du jeu
jeu = Jeu()
jeu.lancerJeu()