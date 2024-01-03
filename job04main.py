class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()

    def add_credits(self, nombre_credits):
        if nombre_credits > 0:
            self.__credits += nombre_credits
            print(f"{nombre_credits} crédits ajoutés. Total de crédits : {self.__credits}")
        else:
            print("Veuillez entrer un nombre de crédits valide.")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def student_info(self):
        print(f"Informations de l'étudiant:")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")
        print(f"Numéro d'étudiant: {self.__num_etudiant}")
        print(f"Niveau: {self.__level}")

# Instanciation de l'objet représentant l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(40)
john_doe.add_credits(35)
john_doe.add_credits(60)

# Affichage des informations de l'étudiant
john_doe.student_info()