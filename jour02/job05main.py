class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    # Assesseurs
    def get_marque(self):
        return self._marque

    def get_modele(self):
        return self._modele

    def get_annee(self):
        return self._annee

    def get_kilometrage(self):
        return self._kilometrage

    def get_en_marche(self):
        return self._en_marche

    def get_reservoir(self):
        return self._reservoir

    # Mutateurs
    def set_marque(self, marque):
        self._marque = marque

    def set_modele(self, modele):
        self._modele = modele

    def set_annee(self, annee):
        self._annee = annee

    def set_kilometrage(self, kilometrage):
        self._kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self._en_marche = en_marche

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
            print("La voiture a démarré.")
        else:
            print("Impossible de démarrer. Réservoir insuffisant.")

    
    def arreter(self):
        self._en_marche = False
        print("La voiture s'est arrêtée.")

    
    def _verifier_plein(self):
        return self._reservoir > 5



ma_voiture = Voiture(marque="Toyota", modele="Corolla", annee=2020, kilometrage=50000)

print("Marque:", ma_voiture.get_marque())
print("Modèle:", ma_voiture.get_modele())
print("Année:", ma_voiture.get_annee())
print("Kilométrage:", ma_voiture.get_kilometrage())
print("En marche:", ma_voiture.get_en_marche())
print("Réservoir:", ma_voiture.get_reservoir())

ma_voiture.demarrer()
print("En marche:", ma_voiture.get_en_marche())

ma_voiture.arreter()
print("En marche:", ma_voiture.get_en_marche())