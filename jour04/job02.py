class Personne: 
    def __init__(self, age=15):
        self.age = age

    def afficherAge(self):
        print(f"Age de la personne : {self.age} ans")

    def bonjour(self):
        print("Hello")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age    


class Professeur(Personne):
    def __init__(self, age=15, matiereEnseigne="Informatique"):
        super().__init__(age)
        self.matiereEnseigne = matiereEnseigne

    def enseigner(self):
        print("Le cours va commencer")   


eleve = Eleve()
professeur = Professeur(age=40, matiereEnseigne="Informatique")

eleve.bonjour()
eleve.modifierAge(15)
eleve.afficherAge()

professeur.bonjour()
professeur.enseigner()
professeur.afficherAge()