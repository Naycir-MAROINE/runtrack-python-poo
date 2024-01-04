class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{titre}' supprimée.")
                return
        print(f"Tâche '{titre}' non trouvée.")

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                print(f"Tâche '{titre}' marquée comme terminée.")
                return
        print(f"Tâche '{titre}' non trouvée.")

    def afficherListe(self):
        for tache in self.taches:
            print(f"{tache.titre}: {tache.description} - {tache.statut}")

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list


# Test du code
tache1 = Tache("Faire les courses", "Acheter du lait et du pain")
tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 1 à 5")
tache3 = Tache("Faire du sport", "Jogging pendant 30 minutes")

liste_taches = ListeDeTaches()
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

print("Liste initiale:")
liste_taches.afficherListe()

print("\nSupprimer la tâche 'Faire du sport':")
liste_taches.supprimerTache("Faire du sport")
liste_taches.afficherListe()

print("\nMarquer la tâche 'Faire les courses' comme terminée:")
liste_taches.marquerCommeFinie("Faire les courses")
liste_taches.afficherListe()

print("\nListe des tâches à faire:")
taches_a_faire = liste_taches.filterListe("à faire")
for tache in taches_a_faire:
    print(f"{tache.titre}: {tache.description} - {tache.statut}")