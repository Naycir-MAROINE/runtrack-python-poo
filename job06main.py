class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour représenter les plats commandés
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat '{nom_plat}' ajouté à la commande.")
        else:
            print(f"Le plat '{nom_plat}' est déjà dans la commande.")

    def annuler_commande(self):
        self.__plats_commandes.clear()
        self.__statut_commande = "annulée"
        print("La commande a été annulée.")

    def calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    def afficher_commande(self):
        print(f"Numéro de commande : {self.__numero_commande}")
        print("Plats commandés:")
        for nom_plat, details_plat in self.__plats_commandes.items():
            print(f"- {nom_plat}: {details_plat['prix']} € ({details_plat['statut']})")
        print(f"Total à payer : {self.calculer_total()} €")
        print(f"Statut de la commande : {self.__statut_commande}")

    def calculer_tva(self, taux_tva):
        tva = self.calculer_total() * taux_tva / 100
        return tva



commande1 = Commande(1)
commande1.ajouter_plat("Pizza", 10)
commande1.ajouter_plat("Pâtes", 8)
commande1.afficher_commande()
print("TVA : ", commande1.calculer_tva(20))
commande1.annuler_commande()
commande1.afficher_commande()
