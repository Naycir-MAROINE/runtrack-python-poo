class Animal:
    def __init__(self):
        self.age = 5
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom

# Instancier un objet Animal
mon_animal = Animal()

# Afficher l'âge initial
print("Âge initial de l'animal :", mon_animal.age)

# Faire vieillir l'animal
mon_animal.vieillir()

# Afficher l'âge après vieillissement
print("Âge de l'animal après vieillissement :", mon_animal.age)

# Nommer l'animal
mon_animal.nommer("Luna")

# Afficher le nom de l'animal
print("l'animal se nomme ", mon_animal.prenom)
