class Ville:
    def __init__(self , nom , nombre_habitants):
        self._nom = nom
        self._nombre_habitants = nombre_habitants

    def get_nom(self):
        return self._nom

    def get_nombre_habitants(self):
        return self._nombre_habitants

    def ajouter_population(self):
        self._nombre_habitants += 1



class Personne:
    def __init__(self, nom , age , ville):
        self._nom =nom
        self._age =age
        self._ville =ville
        ville.ajouter_population()

    def get_ville(self):
        return self._ville.get_nombre_habitants()

paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)  

print(f"Nombre d'habitants a {paris.get_nom()}: {paris.get_nombre_habitants()}")
print(f"Nomnre d'habitants a {marseille.get_nom()}: {marseille.get_nombre_habitants()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4,paris)
chloe = Personne("Chloe", 18 , marseille)

print(f"Nomnbre d'habitants a {paris.get_nom()}: {paris.get_nombre_habitants()}")
print(f" Nombre d'habitants a {marseille.get_nom()}: {marseille.get_nombre_habitants()}")

print(f"Nombre d'habitants a {paris.get_nom()} apres l'arrive de John et Myrtille: {paris.get_nombre_habitants()}")
print(f"Nombre d'habitants a {marseille.get_nom()} apres l'arrive de Chloe: {marseille.get_nombre_habitants()}")