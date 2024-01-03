class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}%"
        return infos

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA


# Création de plusieurs produits
produit1 = Produit("Ordinateur", 900, 20)
produit2 = Produit("Téléphone", 600, 15)

# Appels de méthodes
print(f"Produit 1 initial: {produit1.afficher()}")
print(f"Produit 2 initial: {produit2.afficher()}")

# Calcul des prix TTC pour chaque produit
prix_ttc_produit1 = produit1.calculerPrixTTC()
prix_ttc_produit2 = produit2.calculerPrixTTC()

print(f"Prix TTC du {produit1.obtenirNom()}: {prix_ttc_produit1}")
print(f"Prix TTC du {produit2.obtenirNom()}: {prix_ttc_produit2}")

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Laptop")
produit2.modifierPrixHT(650)

# Appels de méthodes après modification
print(f"Produit 1 après modification: {produit1.afficher()}")
print(f"Produit 2 après modification: {produit2.afficher()}")

# Affichage des nouveaux prix TTC
print(f"Nouveau prix TTC du {produit1.obtenirNom()}: {produit1.calculerPrixTTC()}")
print(f"Nouveau prix TTC du {produit2.obtenirNom()}: {produit2.calculerPrixTTC()}")