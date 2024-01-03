class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur
        self.disponible = True 

    def verification(self):
        
        return self.disponible

    def emprunter(self):
    
        if self.verification():  
            self.disponible = False
            print(f"Le livre '{self.titre}' a été emprunté avec succès.")
        else:
            print(f"Le livre '{self.titre}' n'est pas disponible pour l'emprunt.")

    def rendre(self):
        
        if not self.verification():  
            self.disponible = True
            print(f"Le livre '{self.titre}' a été rendu avec succès.")
        else:
            print(f"Le livre '{self.titre}' n'a pas été emprunté, donc ne peut pas être rendu.")

livre1 = Livre("Harry Potter", "J.K. Rowling")


print(f"Le livre '{livre1.titre}' est disponible : {livre1.verification()}")

livre1.emprunter()


livre1.emprunter()
livre1.rendre()


livre1.rendre()
