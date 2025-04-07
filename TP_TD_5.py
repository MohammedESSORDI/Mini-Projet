                               # le code python des TP/TD 
                               # realiser par Mohammed ESSORDI 
                                           #TD/TP 5
               #Exercice 1

import numpy as np
# 1. Création des tableaux
# Tableau 1D de 0 à 9
tab1d = np.arange(10)  # équivalent à np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Tableau 2D 3x3 avec valeurs aléatoires entre 0 et 1
tab2d = np.random.rand(3, 3)
# Tableau 3D 2x3x4 rempli de zéros
tab3d = np.zeros((2, 3, 4))
# 2. Accès et modification
# Accès au 3ème élément du 1D (indice 2 car Python commence à 0)
element_3 = tab1d[2]
# Accès à la 2ème ligne, 1ère colonne du 2D
element_2d = tab2d[1, 0]  # ou tab2d[1][0]
# Modification d'un élément du 3D
tab3d[0, 1, 2] = 5  # Modifie le 1er bloc, 2ème ligne, 3ème colonne
# 3. Slicing
# Trois premiers éléments du 1D
premiers = tab1d[:3]  # ou tab1d[0:3]
# Dernière colonne du 2D
derniere_col = tab2d[:, -1]
# Affichage des résultats
print("Tableau 1D:", tab1d)
print("Tableau 2D:\n", tab2d)
print("Tableau 3D:\n", tab3d)
print("\nTroisième élément du 1D:", element_3)
print("Élément (2ème ligne, 1ère colonne) du 2D:", element_2d)
print("Trois premiers éléments du 1D:", premiers)
print("Dernière colonne du 2D:", derniere_col)


              #exercice 2
import numpy as np
# 1. Opérations arithmétiques entre deux tableaux
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b  # Attention à la division par zéro dans le cas général
print("Addition:", addition)
print("Soustraction:", soustraction)
print("Multiplication:", multiplication)
print("Division:", division)
# 2. Fonctions mathématiques
angles = np.linspace(0, np.pi, 5)  # 5 valeurs entre 0 et π
sinus = np.sin(angles)
cosinus = np.cos(angles)
exponentielle = np.exp(angles)
print("\nAngles:", angles)
print("Sinus:", sinus)
print("Cosinus:", cosinus)
print("Exponentielle:", exponentielle)
# 3. Opérations logiques
tab = np.arange(10)  # Tableau de 0 à 9
# Sélection des éléments pairs
elements_pairs = tab[tab % 2 == 0]
# Remplacement des éléments impairs par -1
tab[tab % 2 != 0] = -1
print("\nTableau original:", np.arange(10))
print("Éléments pairs:", elements_pairs)
print("Tableau modifié:", tab)


             #Exercice 3
import numpy as np
# 1. Création et redimensionnement
tab = np.arange(12)  # Tableau de 0 à 11
# Transformation en 2D (3x4)
tab2d = tab.reshape(3, 4)
print("Tableau 2D (3x4):\n", tab2d)
# Transformation en 3D (2x2x3)
tab3d = tab.reshape(2, 2, 3)
print("\nTableau 3D (2x2x3):\n", tab3d)
# 2. Manipulation d'axes
# Transposition du tableau 2D
transpose = tab2d.T
print("\nTransposé du tableau 2D:\n", transpose)
# Échange des axes 0 et 1
swap = np.swapaxes(tab2d, 0, 1)
print("\nSwap des axes 0 et 1:\n", swap)
# 3. Concaténation et division
# Création de deux tableaux 2D
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
# Concaténation verticale (axe 0)
concat_vert = np.concatenate((a, b), axis=0)
print("\nConcaténation verticale:\n", concat_vert)
# Concaténation horizontale (axe 1)
concat_hori = np.concatenate((a, b), axis=1)
print("\nConcaténation horizontale:\n", concat_hori)
# Division en sous-tableaux
sous_tableaux = np.split(concat_vert, 2)
print("\nSous-tableaux après division:\n", sous_tableaux[0], "\n", sous_tableaux[1])


               #Exercice 4 
import numpy as np
# 1. Statistiques sur un tableau aléatoire
print("=== Partie 1 ===")
mat = np.random.rand(5, 5)  # Tableau 5x5 aléatoire entre 0 et 1
# Calcul par colonne (axis=0)
moy_col = np.mean(mat, axis=0)
std_col = np.std(mat, axis=0)
min_col = np.min(mat, axis=0)
max_col = np.max(mat, axis=0)
# Calcul par ligne (axis=1)
moy_ligne = np.mean(mat, axis=1)
std_ligne = np.std(mat, axis=1)
min_ligne = np.min(mat, axis=1)
max_ligne = np.max(mat, axis=1)
print("Matrice aléatoire:\n", mat)
print("\nMoyennes par colonne:", moy_col)
print("Écarts-types par colonne:", std_col)
print("Min par colonne:", min_col)
print("Max par colonne:", max_col)
print("\nMoyennes par ligne:", moy_ligne)
print("Écarts-types par ligne:", std_ligne)
print("Min par ligne:", min_ligne)
print("Max par ligne:", max_ligne)
# 2. Tri et recherche d'éléments
print("\n=== Partie 2 ===")
tab = np.random.randint(0, 100, 10)  # 10 entiers aléatoires entre 0 et 100
tab_trie = np.sort(tab)
indice_max = np.argmax(tab)
print("Tableau original:", tab)
print("Tableau trié:", tab_trie)
print("Indice du maximum:", indice_max)
print("Valeur max:", tab[indice_max])
# 3. Broadcasting
print("\n=== Partie 3 ===")
a = np.array([1, 2, 3, 4])  # 1D (4,)
b = np.random.randint(1, 10, (3, 4))  # 2D (3,4)
result = a * b  # Broadcasting automatique
print("Tableau 1D:", a)
print("Tableau 2D:\n", b)
print("Résultat de la multiplication:\n", result)


              #Exercice 5
import numpy as np
import matplotlib.pyplot as plt
# 1. Matrice de covariance
print("=== Partie 1: Matrice de covariance ===")
data = np.random.randn(100, 3)  # 100 observations, 3 variables
cov_matrix = np.cov(data, rowvar=False)  # Calcul par colonnes
print("Dimensions des données:", data.shape)
print("Matrice de covariance (3x3):\n", cov_matrix)
# 2. Transformée de Fourier
print("\n=== Partie 2: Transformée de Fourier ===")
# Création d'un signal sinusoïdal
freq = 5  # Fréquence du signal (Hz)
t = np.linspace(0, 1, 500)  # 500 points entre 0 et 1 seconde
signal = np.sin(2 * np.pi * freq * t)
# Calcul de la FFT (Fast Fourier Transform)
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), t[1]-t[0])  # Calcul des fréquences
# Affichage du spectre
plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(t, signal)
plt.title("Signal temporel")
plt.xlabel("Temps (s)")
plt.subplot(122)
plt.plot(frequencies[:len(frequencies)//2], np.abs(fft_result[:len(fft_result)//2]))
plt.title("Spectre de fréquences")
plt.xlabel("Fréquence (Hz)")
plt.tight_layout()
plt.show()
# 3. Simulation de lancers de dés
print("\n=== Partie 3: Simulation de lancers de dés ===")
np.random.seed(42)  # Pour la reproductibilité
de1 = np.random.randint(1, 7, 1000)  # 1000 lancers dé 1
de2 = np.random.randint(1, 7, 1000)   # 1000 lancers dé 2
sommes = de1 + de2
# Affichage histogramme
plt.figure(figsize=(8, 4))
plt.hist(sommes, bins=range(2, 14), align='left', rwidth=0.8, density=True)
plt.title("Distribution des sommes de deux dés")
plt.xlabel("Somme des dés")
plt.ylabel("Probabilité")
plt.xticks(range(2, 13))
plt.grid(axis='y', alpha=0.5)
plt.show()

             #Exercice 6
import numpy as np
np.random.seed(42)  # Pour la reproductibilité
ventes = np.random.randint(100, 1001, size=(12, 3))
produits = ['P1', 'P2', 'P3']
mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 
        'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
print("Tableau des ventes mensuelles:")
print(ventes)
total_par_produit = np.sum(ventes, axis=0)
print("\nTotal des ventes par produit:")
for produit, total in zip(produits, total_par_produit):
    print(f"{produit}: {total}")
moyenne_par_produit = np.mean(ventes, axis=0)
print("\nMoyenne mensuelle par produit:")
for produit, moy in zip(produits, moyenne_par_produit):
    print(f"{produit}: {moy:.2f}")
mois_max = mois[np.argmax(ventes, axis=0)[0]], mois[np.argmax(ventes, axis=0)[1]], mois[np.argmax(ventes, axis=0)[2]]
print("\nMois avec ventes maximales:")
for produit, mois_m in zip(produits, mois_max):
    print(f"{produit}: {mois_m}")
croissance = np.diff(ventes, axis=0) / ventes[:-1] * 100
print("\nCroissance mensuelle (%):")
print(croissance)
mois_croissance_max = mois[np.argmax(croissance, axis=0)[0] + 1], mois[np.argmax(croissance, axis=0)[1] + 1], mois[np.argmax(croissance, axis=0)[2] + 1]
print("\nMois avec plus forte croissance:")
for produit, mois_c in zip(produits, mois_croissance_max):
    print(f"{produit}: {mois_c}")
total_par_mois = np.sum(ventes, axis=1)
print("\nTotal des ventes par mois:")
for mois_n, total in zip(mois, total_par_mois):
    print(f"{mois_n}: {total}")