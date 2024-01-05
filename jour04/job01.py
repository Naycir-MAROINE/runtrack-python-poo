class Personne: # j'ai attribuer la class parent dans chaque class enfant
    def __init__(self, age=15):
        self.age = age

    def afficherAge(self):
        print(f"Age de la personne : {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age



class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, age=15, matiereEnseigne="Informatique"):
        super().__init__(age)
        self.matiereEnseigne = matiereEnseigne

    def enseigner(self):
        print("Le cours va commencer")

personne = Personne()
personne.afficherAge()
personne.bonjour()
personne.modifierAge(35)
personne.afficherAge()  

eleve = Eleve()
eleve.afficherAge()
eleve.bonjour()
eleve.modifierAge(16)
eleve.afficherAge()
eleve.allerEnCours()

professeur = Professeur(matiereEnseigne="Informatique")
professeur.afficherAge()
professeur.bonjour()
professeur.modifierAge(25)
professeur.afficherAge()
professeur.enseigner()

