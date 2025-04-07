                               # le code python des TP/TD 
                               # realiser par Mohammed ESSORDI 
                                           #TD/TP 4
               #Exercice 1
def main():
    personnes = {}  # Dictionnaire vide pour stocker les données
    while True:
        print("\nMenu:")
        print("1. Ajouter une personne")
        print("2. Rechercher un âge")
        print("3. Supprimer une personne")
        print("4. Quitter")
        choix = input("Choisissez une option (1-4): ")
        if choix == "1":
            # Ajout d'une personne
            entree = input("Entrez 'Nom:Âge' (ex: Jean:25): ")
            try:
                nom, age = entree.split(":")
                personnes[nom.strip()] = int(age.strip())
                print(f"{nom} ajouté(e) avec succès!")
            except (ValueError, IndexError):
                print("Format incorrect. Utilisez 'Nom:Âge'")
        elif choix == "2":
            # Recherche d'un âge
            nom = input("Entrez le nom à rechercher: ").strip()
            if nom in personnes:
                print(f"{nom} a {personnes[nom]} ans.")
            else:
                print(f"{nom} non trouvé(e).")
        elif choix == "3":
            # Suppression d'une personne
            nom = input("Entrez le nom à supprimer: ").strip()
            if nom in personnes:
                del personnes[nom]
                print(f"{nom} supprimé(e) avec succès.")
            else:
                print(f"{nom} non trouvé(e).")
        elif choix == "4":
            # Quitter le programme
            print("Merci d'avoir utilisé ce programme!")
            break
        else:
            print("Option invalide. Veuillez choisir entre 1 et 4.")
if __name__ == "__main__":
    main()


                  #Exercice 2
def fusionner_et_trier(dict1, dict2):
    resultat = {}
    # Traitement de toutes les clés des deux dictionnaires
    for cle in set(dict1.keys()) | set(dict2.keys()):
        if cle in dict1 and cle in dict2:
            # Cas où la clé existe dans les deux dictionnaires
            if isinstance(dict1[cle], (int, float)) and isinstance(dict2[cle], (int, float)):
                resultat[cle] = dict1[cle] + dict2[cle]  # Addition pour les nombres
            else:
                resultat[cle] = str(dict1[cle]) + str(dict2[cle])  # Concaténation pour le reste
        elif cle in dict1:
            # Cas où la clé n'existe que dans le premier dictionnaire
            resultat[cle] = dict1[cle]
        else:
            # Cas où la clé n'existe que dans le deuxième dictionnaire
            resultat[cle] = dict2[cle]
    # Tri des clés par ordre alphabétique
    return dict(sorted(resultat.items()))
# Exemple d'utilisation
if __name__ == "__main__":
    d1 = { "a": 10, "b": "test" }
    d2 = { "a": 5, "c": "data" }
    resultat = fusionner_et_trier(d1, d2)
    print("Dictionnaire fusionné et trié:", resultat)


             #Exercice 3
import os
FICHIER_DONNEES = "personnes.txt"
def charger_donnees():
   
    personnes = {}
    if os.path.exists(FICHIER_DONNEES):
        with open(FICHIER_DONNEES, "r", encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne:  # Ignore les lignes vides
                    try:
                        nom, age = ligne.split(",")
                        personnes[nom.strip()] = int(age.strip())
                    except ValueError:
                        print(f"Format incorrect dans la ligne: {ligne}")
    return personnes
def sauvegarder_donnees(personnes):
   
    with open(FICHIER_DONNEES, "w", encoding="utf-8") as f:
        for nom, age in personnes.items():
            f.write(f"{nom},{age}\n")
def afficher_menu():
   
    print("\nMenu:")
    print("1. Afficher toutes les personnes")
    print("2. Ajouter/Modifier une personne")
    print("3. Quitter")
def main():
    
    # Chargement initial des données
    personnes = charger_donnees()
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-3): ")
        if choix == "1":
            # Affichage des données
            print("\nListe des personnes:")
            for nom, age in sorted(personnes.items()):
                print(f"- {nom}: {age} ans")
        elif choix == "2":
            # Ajout/Modification
            nom = input("Entrez le nom: ").strip()
            try:
                age = int(input("Entrez l'âge: ").strip())
                personnes[nom] = age
                sauvegarder_donnees(personnes)
                print(f"{nom} a été ajouté(e)/modifié(e) avec succès!")
            except ValueError:
                print("L'âge doit être un nombre entier!")
        elif choix == "3":
            # Quitter
            print("Merci d'avoir utilisé ce programme!")
            break
        else:
            print("Option invalide. Veuillez choisir entre 1 et 3.")
if __name__ == "__main__":
    # Création du fichier initial s'il n'existe pas
    if not os.path.exists(FICHIER_DONNEES):
        with open(FICHIER_DONNEES, "w", encoding="utf-8") as f:
            f.write("Alice,30\nBob,25\nCharlie,35\n")
    
    main()