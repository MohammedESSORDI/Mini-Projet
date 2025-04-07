                               # le code python des TP/TD 
                               # realiser par Mohammed ESSORDI 
                                         # TD 2

        #EXERCICE 1  

# Création de la liste des jours de la semaine
Semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

# Affichage de la liste complète
print("Jours de la semaine:", Semaine)

# Création d'une liste vide
Couleurs = []

# Ajout de 5 couleurs différentes
Couleurs.append("rouge")
Couleurs.append("vert")
Couleurs.append("bleu")
Couleurs.append("jaune")
Couleurs.append("noir")

# Affichage de la liste
print("Liste de couleurs:", Couleurs)

# Création d'une liste de 7 réels
reels = [3.14, 2.71, 1.618, 0.577, 1.414, 1.732, 2.236]

# Affichage des éléments aux indices 1, 3 et 5
print("Élément à l'indice 1:", reels[1])
print("Élément à l'indice 3:", reels[3])
print("Élément à l'indice 5:", reels[5])"


         #Exercice 2

mylist = ['apple', 'banana', 'cherry']
print(mylist[1])  # Affiche 'banana'

mylist = ['apple', 'banana', 'banana', 'cherry']
print(mylist[2])  # Affiche 'banana' (le 3ème élément)

thislist = ['apple', 'banana', 'cherry']
print(len(thislist))  # Affiche 3

mylist = ['apple', 'banana', 'cherry']
print(mylist[-1])  # Affiche 'cherry'

fruits = ['apple', "banana", "cherry"]
print(fruits[1])  # Affiche 'banana'

mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])  # Affiche ['banana', 'cherry', 'orange']

fruits = ['apple', "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])  # Affiche ['cherry', 'orange', 'kiwi']


         #Exercice 3
# Création de la liste des matières
matieres = ["Anglais", "Physique", "Maths", "Svt"]
# Affichage de la liste initiale
print("Liste initiale des matières:", matieres)
# Ajout de nouvelles matières
matieres.append("Histoire")
matieres.append("Geographie")
# Affichage de la liste mise à jour
print("\nListe après ajout:", matieres)
# Affichage des 4 premiers éléments
print("\na) 4 premiers éléments:", matieres[:4])
# Affichage des 3 derniers éléments
print("b) 3 derniers éléments:", matieres[-3:])
# Affichage de 3 éléments à partir du second indice
print("c) 3 éléments depuis le 2nd indice:", matieres[1:4])


         # Exercice 4

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'  # Remplace 'apple' par 'kiwi'
print(mylist[1])    # Affiche 'banana'
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"  # Modification directe par indice
print(fruits)       # Affiche ['kiwi', 'banana', 'cherry']
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']  # Remplace l'élément 1 par deux nouveaux éléments
print(mylist[2])  # Affiche 'mango'
mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')  # Ajoute 'orange' en position 0
print(mylist[1])  # Affiche 'apple'
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Ajoute à la fin
print(fruits)  # Affiche ['apple', 'banana', 'cherry', 'orange']
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")  # Insère à la position 1
print(fruits)  # Affiche ['apple', 'lemon', 'banana', 'cherry']


             #Exercice 5

Semaine = ['lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim']
Semaine.remove('mer')  # Supprime l'élément ayant la valeur 'mer'
print(Semaine)  # Affiche ['lun', 'mar', 'jeu', 'ven', 'sam', 'dim']
mylist = ['apple', 'banana', 'cherry']
mylist.pop(1)  # Supprime l'élément à l'indice 1 ('banana')
print(mylist)  # Affiche ['apple', 'cherry']
fruits = ['apple', 'banana', 'cherry']
fruits.clear()  # Vide complètement la liste
print(fruits)  # Affiche []
