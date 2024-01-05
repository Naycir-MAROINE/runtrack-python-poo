class Vehicule:
    def __init__(self, marque,modele,annee,prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
    def informationVehicule(self):
        print(f"Marque : {self.marque}")
        print(f" Modele: {self.modele}") 
        print(f" Annee: {self.annee}")
        print(f"Prix:{self.prix} euros")
    
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix,portes=4):
        super().__init__(marque, modele, annee, prix)
        self.portes = portes

    def informationVehicule(self):
         super().informationVehicule()   
         print("Nombre de portes: 4")

    def demarrer(self):
        print("Vroum vroum! La voiture demarre.")


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        super().__init__(marque, modele, annee, prix) 
        self.roues = roues   

    def informationVehicule(self):
        super().informationVehicule()  
        print(f"Nombre de roues : {self.roues}")  

    def demarrer(self):
        print("Vroum! La moto demarre") 

ma_voiture = Voiture("Toyota","Camry",2022,25000)
ma_voiture.informationVehicule()
ma_voiture.demarrer

ma_moto = Moto("Harley-Davidson", "Sportster", 2021,12000)
ma_moto.informationVehicule()
ma_moto.demarrer()