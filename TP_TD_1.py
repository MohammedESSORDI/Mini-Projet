
                               # le code python des TP/TD 
                               # realiser par Mohammed ESSORDI 
                                          # TD 1 
                # EXERCICE 1

texte = "Bonjour le monde"      # Variable de type texte (str)
entier = 42                     # Variable de type nombre entier (int)
decimal = 3.14                  # Variable de type nombre décimal (float)

print("Type de 'texte':", type(texte))
print("Type de 'entier':", type(entier))
print("Type de 'decimal':", type(decimal))

nom, prenom, age = ("Dupont", "Jean", 25)

print(f"Nom: {nom} (Type: {type(nom)})")
print(f"Prénom: {prenom} (Type: {type(prenom)})")
print(f"Âge: {age} (Type: {type(age)})")

                 #Exercice 2

# Saisie des notes et coefficients
anglais = float(input("Entrez la note d'Anglais: "))
coef_anglais = float(input("Entrez le coefficient d'Anglais: "))

physique = float(input("Entrez la note de Physique: "))
coef_physique = float(input("Entrez le coefficient de Physique: "))

maths = float(input("Entrez la note de Maths: "))
coef_maths = float(input("Entrez le coefficient de Maths: "))

svt = float(input("Entrez la note de SVT: "))
coef_svt = float(input("Entrez le coefficient de SVT: "))

# Calcul de la moyenne pondérée
moyenne = (anglais * coef_anglais + 
           physique * coef_physique + 
           maths * coef_maths + 
           svt * coef_svt) / (coef_anglais + coef_physique + coef_maths + coef_svt)

# Affichage du résultat
print(f"\nMoyenne pondérée: {moyenne:.2f}")

# Saisie du budget et du montant des achats
budget = float(input("\nEntrez votre budget: "))
achats = float(input("Entrez le montant des achats: "))

# Vérification si le budget est suffisant
if budget >= achats:
    print("\nLe budget est suffisant pour ces achats.")
    reste = budget - achats
    print(f"Il vous restera {reste:.2f} MAD après l'achat.")
else:
    print("\nLe budget est insuffisant pour ces achats.")
    manque = achats - budget
    print(f"Il vous manque {manque:.2f} MAD pour pouvoir payer.")


                   # EXERCICE 3

# Importation du module math pour avoir accès à pi
import math

# Saisie du rayon et de la hauteur
rayon = float(input("Entrez le rayon du cône (en cm): "))
hauteur = float(input("Entrez la hauteur du cône (en cm): "))

# Calcul du volume selon la formule V = (1/3) * π * r² * h
volume = (1/3) * math.pi * (rayon ** 2) * hauteur

# Affichage du résultat avec 2 décimales
print(f"\nLe volume du cône est de {volume:.2f} cm³")

import math

try:
    rayon = float(input("Entrez le rayon du cône (en cm): "))
    hauteur = float(input("Entrez la hauteur du cône (en cm): "))
    
    if rayon <= 0 or hauteur <= 0:
        print("Erreur : le rayon et la hauteur doivent être positifs")
    else:
        volume = (1/3) * math.pi * (rayon ** 2) * hauteur
        print(f"\nLe volume du cône est de {volume:.2f} cm³")
        
except ValueError:
    print("Erreur : vous devez entrer des nombres valides")


                 #EXERCICE 4

import math

# Saisie des rayons
Rg = float(input("Entrez le rayon du grand disque Rg (en cm): "))
Rp = float(input("Entrez le rayon du petit disque Rp (en cm): "))

# Vérification des contraintes Rp < Rg
if Rp >= Rg:
    print("Erreur : Le rayon du trou Rp doit être strictement inférieur au rayon du disque Rg")
elif Rp <= 0 or Rg <= 0:
    print("Erreur : Les rayons doivent être positifs")
else:
    # Calcul de la surface de la couronne circulaire
    surface_grand = math.pi * (Rg ** 2)
    surface_petit = math.pi * (Rp ** 2)
    surface_couronne = surface_grand - surface_petit
    
    # Affichage du résultat
    print(f"\nSurface du disque découpé (couronne circulaire): {surface_couronne:.2f} cm²")


                     #EXERCICE 5 

# Saisie de la phrase par l'utilisateur
phrase = input("Entrez une phrase : ")

# Calcul de la longueur de la phrase
longueur = len(phrase)

# Détermination si la longueur est paire ou impaire
if longueur == 0:
    print("La phrase est vide !")
elif longueur % 2 == 0:  # Longueur paire
    moitie = longueur // 2
    partie_a_afficher = phrase[:moitie]
    print(f"La phrase a une longueur paire. Première moitié : '{partie_a_afficher}'")
else:  # Longueur impaire
    moitie = longueur // 2
    partie_a_afficher = phrase[moitie:]
    print(f"La phrase a une longueur impaire. Seconde moitié : '{partie_a_afficher}'")
