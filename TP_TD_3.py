                               # le code python des TP/TD 
                               # realiser par Mohammed ESSORDI 
                                           #TD/TP 3
         # Exercice 1
# Partie 1 - Création de la liste
nombres = [4, 8, 15, 16, 23, 42]
print("Ma liste de nombres:", nombres)

# Partie 2 - Fonction d'affichage
def affListe(ma_liste):
    #Affiche chaque élément d'une liste sur une ligne séparée
    for element in ma_liste:
        print(element)

# Test de la fonction
print("\nAffichage élément par élément:")
affListe(nombres)


             #Exercice 2

def somme_liste(liste):
    total = 0
    for nombre in liste:
        total += nombre
    return total

def moyenne_liste(liste):

    somme = somme_liste(liste)
    return somme / len(liste) if len(liste) > 0 else 0

# Liste de nombres
nombres = [4, 8, 15, 16, 23, 42]

# Calcul et affichage
print("Liste:", nombres)
print("Somme:", somme_liste(nombres))
print("Moyenne:", moyenne_liste(nombres))



             #Exercice 3

# 1. Fonction pour calculer la somme d'une liste
def somme_liste(liste):
    
    return sum(liste)  # Utilisation de la fonction sum() intégrée de Python

# 2. Fonction pour calculer la moyenne
def moyenne_liste(liste):
    
    if len(liste) == 0:  # Gestion du cas d'une liste vide
        return 0
    return somme_liste(liste) / len(liste)  # Utilisation de la fonction somme_liste

# 3. Utilisation des fonctions
if __name__ == "__main__":
    # Liste d'exemple
    nombres = [4, 8, 15, 16, 23, 42]
    
    # Calculs
    somme = somme_liste(nombres)
    moyenne = moyenne_liste(nombres)
    
    # Affichage des résultats
    print(f"Liste: {nombres}")
    print(f"Somme des éléments: {somme}")
    print(f"Moyenne des éléments: {moyenne:.2f}")  # Formatage à 2 décimales


              #Exercice 4

# 1. Fonction de vérification d'existence d'un élément
def element_existe(liste, element):
   
    return element in liste

# 2. Tests de la fonction
if __name__ == "__main__":
    # Liste de démonstration
    nombres = [4, 8, 15, 16, 23, 42]
    
    # Test avec l'élément 15 (présent)
    resultat1 = element_existe(nombres, 15)
    print(f"15 existe dans la liste: {resultat1}")  # Devrait afficher True
    
    # Test avec l'élément 50 (absent)
    resultat2 = element_existe(nombres, 50)
    print(f"50 existe dans la liste: {resultat2}")  # Devrait afficher False



             #Exercice 5 
def liste_carres(liste):
    
    return [x**2 for x in liste]  # Utilisation d'une liste en compréhension

# Test de la fonction
if __name__ == "__main__":
    # Liste de démonstration
    nombres = [4, 8, 15, 16, 23, 42]
    
    # Application de la fonction
    carres = liste_carres(nombres)
    
    # Affichage des résultats
    print(f"Liste originale: {nombres}")
    print(f"Liste des carrés: {carres}")



              #Exercice 6
def trouver_min_max(liste):
   
    if not liste:  # Si la liste est vide
        return (None, None)
    return (min(liste), max(liste))

# Test de la fonction
if __name__ == "__main__":
    # Liste de démonstration
    nombres = [4, 8, 15, 16, 23, 42]
    
    # Application de la fonction
    minimum, maximum = trouver_min_max(nombres)
    
    # Affichage des résultats
    print(f"Liste analysée: {nombres}")
    print(f"Minimum: {minimum}, Maximum: {maximum}")


              #Exercice 7
# 1. Création de la deuxième liste
autres_nombres = [7, 11, 19, 24, 33]

# 2. Fonction de fusion et tri
def fusionner_et_trier(liste1, liste2):
    
    liste_fusionnee = liste1 + liste2  # Fusion des deux listes
    liste_fusionnee.sort()  # Tri en place
    return liste_fusionnee

# 3. Test de la fonction
if __name__ == "__main__":
    # Liste existante
    nombres = [4, 8, 15, 16, 23, 42]
    
    # Application de la fonction
    liste_triee = fusionner_et_trier(nombres, autres_nombres)
    
    # Affichage des résultats
    print(f"Liste 1: {nombres}")
    print(f"Liste 2: {autres_nombres}")
    print(f"Liste fusionnée et triée: {liste_triee}")


               #Exercice 8
def est_palindrome(mot):
    
    mot = mot.lower()  # Convertit en minuscules pour ignorer la casse
    return mot == mot[::-1]  # Compare le mot avec sa version inversée

# Tests de la fonction
if __name__ == "__main__":
    mots_a_tester = ["radar", "python", "level"]
    
    for mot in mots_a_tester:
        resultat = est_palindrome(mot)
        print(f"'{mot}' est un palindrome: {resultat}")
