# Les Tableaux en Python :

## Introduction

Dans l’univers de la programmation Python, les structures de données constituent les fondations sur lesquelles repose toute logique applicative. Parmi elles, les listes occupent une place centrale, offrant une flexibilité et une puissance qui en font l’outil de prédilection pour manipuler des collections de données.

Ce cours vous guidera à travers les méandres des tableaux en Python, depuis les concepts fondamentaux jusqu’aux techniques avancées utilisées par les professionnels. Que vous soyez débutant cherchant à comprendre les bases ou développeur souhaitant approfondir vos connaissances, vous trouverez ici les clés pour maîtriser cet outil essentiel.

## Chapitre 1 : Fondements des Listes Python

### 1.1 Qu’est-ce qu’une liste ?

Une liste en Python est une structure de données **ordonnée** et **modifiable** permettant de stocker une collection d’éléments. Contrairement aux tableaux traditionnels d’autres langages comme C ou Java, les listes Python présentent une caractéristique remarquable : elles sont **hétérogènes**, c’est-à-dire qu’elles peuvent contenir des éléments de types différents.

**Exemple conceptuel :**

Imaginez une liste comme une étagère où chaque emplacement peut accueillir n’importe quel objet : un livre, un vase, une photo. Cette flexibilité distingue Python et en fait un langage particulièrement adapté au prototypage rapide et à l’exploration de données.

### 1.2 Création de listes

La syntaxe de création d’une liste est remarquablement simple et intuitive :

```python
# Liste vide - méthode 1
mon_tableau = []

# Liste vide - méthode 2 (constructeur)
mon_tableau = list()

# Liste avec des éléments initiaux
fruits = ["pomme", "banane", "cerise"]

# Liste hétérogène (types mixtes)
collection_mixte = [42, "texte", 3.14, True, None]

# Liste de listes (structure bidimensionnelle)
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

**Bonne pratique :** Privilégiez des noms de variables explicites et utilisez le pluriel pour les listes afin d’améliorer la lisibilité de votre code.

### 1.3 Caractéristiques essentielles

Les listes Python possèdent trois propriétés fondamentales :

1. **Ordonnées** : L’ordre d’insertion est préservé, ce qui garantit la prévisibilité lors du parcours.
1. **Modifiables** (mutables) : On peut ajouter, supprimer ou modifier des éléments après la création.
1. **Dynamiques** : La taille peut croître ou diminuer selon les besoins, sans déclaration préalable.

## Chapitre 2 : L’Indexation et l’Accès aux Éléments

### 2.1 Le système d’indexation

En Python, comme dans la majorité des langages de programmation, l’indexation commence à **zéro**. Cette convention, héritée du langage C, s’explique par des considérations d’efficacité mémoire : l’index représente le décalage par rapport au début de la structure.

**Visualisation :**

```
Liste : fruits = ["pomme", "banane", "cerise", "datte"]

Index positif :    0        1         2         3
                   ↓        ↓         ↓         ↓
Valeurs :      "pomme"  "banane"  "cerise"  "datte"
                   ↑        ↑         ↑         ↑
Index négatif :   -4       -3        -2        -1
```

### 2.2 Accès par index positif

L’accès direct à un élément s’effectue en utilisant la notation entre crochets :

```python
fruits = ["pomme", "banane", "cerise", "datte"]

premier_fruit = fruits[0]      # "pomme"
deuxieme_fruit = fruits[1]     # "banane"
dernier_index = fruits[3]      # "datte"
```

**Attention aux erreurs courantes :**

```python
# ERREUR : IndexError
element = fruits[10]  # La liste n'a que 4 éléments (indices 0-3)
```

### 2.3 Accès par index négatif

Python offre une fonctionnalité élégante : l’indexation négative, qui permet d’accéder aux éléments en partant de la fin :

```python
fruits = ["pomme", "banane", "cerise", "datte"]

dernier = fruits[-1]           # "datte"
avant_dernier = fruits[-2]     # "cerise"
premier_negatif = fruits[-4]   # "pomme" (équivalent à fruits[0])
```

**Cas d’usage pratique :** Cette notation est particulièrement utile lorsque vous ne connaissez pas la taille exacte de la liste mais devez accéder aux derniers éléments.

### 2.4 Le slicing (découpage de listes)

Le slicing est une technique puissante permettant d’extraire des sous-ensembles de listes. La syntaxe générale est `liste[début:fin:pas]`.

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extraction d'une portion
portion = nombres[2:6]          # [2, 3, 4, 5] (l'index 6 est exclu)

# Omission du début (implicitement 0)
debut = nombres[:4]             # [0, 1, 2, 3]

# Omission de la fin (jusqu'à la fin)
fin = nombres[7:]               # [7, 8, 9]

# Utilisation d'un pas
pairs = nombres[::2]            # [0, 2, 4, 6, 8]
impairs = nombres[1::2]         # [1, 3, 5, 7, 9]

# Inversion d'une liste (astuce élégante)
inverse = nombres[::-1]         # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Slicing avec indices négatifs
sous_liste = nombres[-5:-2]    # [5, 6, 7]
```

**Mémo important :** Dans `liste[début:fin]`, l’élément à l’index `début` est inclus, mais celui à l’index `fin` est exclu. Pensez à l’intervalle mathématique [début, fin[.

## Chapitre 3 : Manipulation et Modification des Listes

### 3.1 Ajout d’éléments

Python propose plusieurs méthodes pour enrichir vos listes, chacune adaptée à un contexte spécifique.

#### 3.1.1 La méthode `append()`

Ajoute un élément unique à la fin de la liste. C’est la méthode la plus couramment utilisée.

```python
fruits = ["pomme", "banane"]
fruits.append("cerise")
print(fruits)  # ["pomme", "banane", "cerise"]

# Attention : append ajoute l'élément tel quel
fruits.append(["orange", "kiwi"])
print(fruits)  # ["pomme", "banane", "cerise", ["orange", "kiwi"]]
```

**Complexité temporelle :** O(1) en moyenne, ce qui en fait une opération très efficace.

#### 3.1.2 La méthode `insert()`

Insère un élément à une position spécifique, décalant les éléments suivants.

```python
fruits = ["pomme", "cerise"]
fruits.insert(1, "banane")
print(fruits)  # ["pomme", "banane", "cerise"]

# Insertion au début
fruits.insert(0, "fraise")
print(fruits)  # ["fraise", "pomme", "banane", "cerise"]

# Insertion à la fin (équivalent à append)
fruits.insert(len(fruits), "mangue")
```

**Complexité temporelle :** O(n) dans le pire cas, car tous les éléments suivants doivent être décalés.

#### 3.1.3 La méthode `extend()`

Ajoute tous les éléments d’un itérable à la fin de la liste.

```python
fruits = ["pomme", "banane"]
agrumes = ["orange", "citron"]

fruits.extend(agrumes)
print(fruits)  # ["pomme", "banane", "orange", "citron"]

# Alternative avec l'opérateur +
fruits_complets = fruits + ["kiwi", "mangue"]

# Alternative avec l'opérateur +=
fruits += ["papaye"]
```

**Différence clé :** `extend()` modifie la liste originale, tandis que `+` crée une nouvelle liste.

### 3.2 Suppression d’éléments

#### 3.2.1 La méthode `remove()`

Supprime la **première occurrence** d’une valeur spécifique.

```python
fruits = ["pomme", "banane", "cerise", "banane"]
fruits.remove("banane")
print(fruits)  # ["pomme", "cerise", "banane"]

# ATTENTION : Erreur si l'élément n'existe pas
try:
    fruits.remove("ananas")
except ValueError:
    print("L'élément n'existe pas dans la liste")
```

#### 3.2.2 L’instruction `del`

Supprime un élément par son index ou une portion de la liste.

```python
fruits = ["pomme", "banane", "cerise", "datte"]

# Suppression par index
del fruits[1]
print(fruits)  # ["pomme", "cerise", "datte"]

# Suppression d'une tranche
del fruits[1:3]
print(fruits)  # ["pomme"]

# Suppression de toute la liste
del fruits
```

#### 3.2.3 La méthode `pop()`

Retire et **retourne** l’élément à un index donné (dernier élément par défaut).

```python
fruits = ["pomme", "banane", "cerise"]

dernier = fruits.pop()
print(dernier)  # "cerise"
print(fruits)   # ["pomme", "banane"]

premier = fruits.pop(0)
print(premier)  # "pomme"
print(fruits)   # ["banane"]
```

**Cas d’usage typique :** Implémentation de piles (stacks) et de files (queues).

#### 3.2.4 La méthode `clear()`

Vide complètement la liste.

```python
fruits = ["pomme", "banane", "cerise"]
fruits.clear()
print(fruits)  # []
```

### 3.3 Modification d’éléments

La modification directe par assignation est simple et intuitive :

```python
fruits = ["pomme", "banane", "cerise"]

# Modification d'un élément unique
fruits[0] = "fraise"
print(fruits)  # ["fraise", "banane", "cerise"]

# Modification d'une tranche
fruits[1:3] = ["kiwi", "mangue", "orange"]
print(fruits)  # ["fraise", "kiwi", "mangue", "orange"]

# Remplacement par moins d'éléments
fruits[1:4] = ["ananas"]
print(fruits)  # ["fraise", "ananas"]
```

## Chapitre 4 : Parcours et Itération

### 4.1 La boucle `for` classique

Le parcours d’une liste est l’une des opérations les plus fréquentes en programmation :

```python
fruits = ["pomme", "banane", "cerise"]

for fruit in fruits:
    print(f"J'aime manger des {fruit}s")
```

**Sortie :**

```
J'aime manger des pommes
J'aime manger des bananes
J'aime manger des cerises
```

### 4.2 Parcours avec index : `enumerate()`

Lorsque vous avez besoin à la fois de l’élément et de son index :

```python
fruits = ["pomme", "banane", "cerise"]

for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")
```

**Sortie :**

```
1. pomme
2. banane
3. cerise
```

**Astuce :** Vous pouvez spécifier l’index de départ avec `enumerate(fruits, start=1)`.

### 4.3 Parcours de plusieurs listes : `zip()`

Pour itérer simultanément sur plusieurs listes :

```python
fruits = ["pomme", "banane", "cerise"]
prix = [2.5, 1.8, 3.2]
quantites = [10, 15, 8]

for fruit, prix_unitaire, qte in zip(fruits, prix, quantites):
    total = prix_unitaire * qte
    print(f"{fruit}: {qte} unités à {prix_unitaire}€ = {total}€")
```

### 4.4 List comprehensions (compréhensions de listes)

Une technique pythonique puissante pour créer des listes de manière concise :

```python
# Syntaxe de base : [expression for item in iterable]

# Carrés des nombres de 0 à 9
carres = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Avec condition
pairs = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformation de données
fruits = ["pomme", "banane", "cerise"]
fruits_majuscules = [fruit.upper() for fruit in fruits]
# ["POMME", "BANANE", "CERISE"]

# Compréhensions imbriquées (matrices)
matrice = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

**Quand utiliser les list comprehensions ?** Elles améliorent la lisibilité pour des transformations simples, mais peuvent nuire à la clarté si elles deviennent trop complexes. Privilégiez les boucles `for` traditionnelles pour les logiques élaborées.

## Chapitre 5 : Méthodes et Fonctions Essentielles

### 5.1 Méthodes de recherche et de comptage

```python
fruits = ["pomme", "banane", "cerise", "banane", "datte"]

# Trouver l'index de la première occurrence
index_banane = fruits.index("banane")  # 1

# Index avec recherche dans une plage
index_deuxieme_banane = fruits.index("banane", 2)  # 3

# Compter les occurrences
nb_bananes = fruits.count("banane")  # 2

# Vérifier l'appartenance
if "pomme" in fruits:
    print("La pomme est dans la liste")

# Vérifier l'absence
if "ananas" not in fruits:
    print("L'ananas n'est pas dans la liste")
```

### 5.2 Méthodes de tri

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]

# Tri en place (modifie la liste originale)
nombres.sort()
print(nombres)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Tri décroissant
nombres.sort(reverse=True)
print(nombres)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Fonction sorted() (crée une nouvelle liste)
nombres_originaux = [3, 1, 4, 1, 5, 9, 2, 6]
nombres_tries = sorted(nombres_originaux)
print(nombres_originaux)  # [3, 1, 4, 1, 5, 9, 2, 6] (inchangé)
print(nombres_tries)      # [1, 1, 2, 3, 4, 5, 6, 9]

# Tri personnalisé avec key
mots = ["banane", "Pomme", "cerise", "Datte"]
mots_tries = sorted(mots, key=str.lower)
print(mots_tries)  # ["banane", "cerise", "Datte", "Pomme"]

# Tri par longueur
mots.sort(key=len)
print(mots)  # ["Pomme", "Datte", "banane", "cerise"]
```

### 5.3 Inversion et copie

```python
fruits = ["pomme", "banane", "cerise"]

# Inversion en place
fruits.reverse()
print(fruits)  # ["cerise", "banane", "pomme"]

# Copie superficielle (shallow copy)
copie1 = fruits.copy()
copie2 = fruits[:]
copie3 = list(fruits)

# ATTENTION : Problème avec les listes imbriquées
import copy

liste_imbriquee = [[1, 2], [3, 4]]
copie_superficielle = liste_imbriquee.copy()
copie_profonde = copy.deepcopy(liste_imbriquee)

liste_imbriquee[0][0] = 99
print(copie_superficielle)  # [[99, 2], [3, 4]] - affectée !
print(copie_profonde)       # [[1, 2], [3, 4]] - non affectée
```

### 5.4 Fonctions utiles

```python
nombres = [3, 1, 4, 1, 5, 9, 2, 6]

# Longueur
longueur = len(nombres)  # 8

# Minimum et maximum
minimum = min(nombres)   # 1
maximum = max(nombres)   # 9

# Somme (pour les valeurs numériques)
total = sum(nombres)     # 31

# Tous les éléments sont vrais ?
valeurs_bool = [True, True, False]
tous_vrais = all(valeurs_bool)  # False

# Au moins un élément est vrai ?
au_moins_un = any(valeurs_bool)  # True
```

## Chapitre 6 : Techniques Avancées

### 6.1 Listes multidimensionnelles

Les listes peuvent contenir d’autres listes, permettant de créer des structures multidimensionnelles :

```python
# Matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accès à un élément
element = matrice[1][2]  # 6 (ligne 1, colonne 2)

# Parcours d'une matrice
for ligne in matrice:
    for valeur in ligne:
        print(valeur, end=" ")
    print()  # Nouvelle ligne

# Création avec list comprehension
matrice_zeros = [[0 for _ in range(3)] for _ in range(3)]
```

**Attention :** Évitez `[[0] * 3] * 3` qui créerait des références vers la même liste interne.

### 6.2 Filtrage et transformation avec `map()` et `filter()`

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter() - garde les éléments qui satisfont une condition
pairs = list(filter(lambda x: x % 2 == 0, nombres))
# [2, 4, 6, 8, 10]

# map() - applique une fonction à chaque élément
carres = list(map(lambda x: x**2, nombres))
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Combinaison
carres_pairs = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nombres)))
# [4, 16, 36, 64, 100]
```

**Note :** Les list comprehensions sont généralement préférées en Python pour leur lisibilité.

### 6.3 Unpacking (déballage)

```python
# Déballage simple
fruits = ["pomme", "banane", "cerise"]
premier, deuxieme, troisieme = fruits

# Déballage avec reste (*)
nombres = [1, 2, 3, 4, 5]
premier, *milieu, dernier = nombres
# premier = 1, milieu = [2, 3, 4], dernier = 5

# Échange de valeurs sans variable temporaire
a, b = 10, 20
a, b = b, a  # a = 20, b = 10
```

### 6.4 Opérations d’ensemble sur les listes

```python
# Élimination des doublons (conversion en set puis en liste)
nombres = [1, 2, 2, 3, 4, 4, 5]
uniques = list(set(nombres))  # [1, 2, 3, 4, 5]

# ATTENTION : l'ordre n'est pas garanti avec set()
# Pour préserver l'ordre :
def deduplicate(liste):
    seen = set()
    return [x for x in liste if not (x in seen or seen.add(x))]

nombres_uniques_ordonnes = deduplicate([1, 2, 2, 3, 4, 4, 5])
# [1, 2, 3, 4, 5]

# Intersection de deux listes
liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]
intersection = list(set(liste1) & set(liste2))  # [4, 5]

# Union
union = list(set(liste1) | set(liste2))  # [1, 2, 3, 4, 5, 6, 7, 8]

# Différence
difference = list(set(liste1) - set(liste2))  # [1, 2, 3]
```

## Chapitre 7 : NumPy - Les Tableaux Haute Performance

### 7.1 Introduction à NumPy

Pour les calculs scientifiques, l’analyse de données ou le machine learning, les listes Python standards montrent leurs limites en termes de performance. NumPy (Numerical Python) offre une alternative optimisée.

```python
import numpy as np

# Création d'un tableau NumPy
tableau_numpy = np.array([1, 2, 3, 4, 5])

# Différence majeure : opérations vectorisées
liste_python = [1, 2, 3, 4, 5]
tableau_numpy = np.array([1, 2, 3, 4, 5])

# Avec les listes Python (nécessite une boucle)
liste_double = [x * 2 for x in liste_python]

# Avec NumPy (opération vectorisée)
tableau_double = tableau_numpy * 2
# array([ 2,  4,  6,  8, 10])
```

### 7.2 Créations de tableaux NumPy

```python
import numpy as np

# À partir d'une liste
arr = np.array([1, 2, 3, 4, 5])

# Tableau de zéros
zeros = np.zeros(5)  # array([0., 0., 0., 0., 0.])

# Tableau de uns
uns = np.ones((3, 3))  # Matrice 3x3 de uns

# Plage de valeurs
plage = np.arange(0, 10, 2)  # array([0, 2, 4, 6, 8])

# Valeurs espacées linéairement
lineaire = np.linspace(0, 1, 5)  # array([0., 0.25, 0.5, 0.75, 1.])

# Matrice identité
identite = np.eye(3)

# Tableau aléatoire
aleatoire = np.random.rand(3, 3)  # Valeurs entre 0 et 1
```

### 7.3 Avantages de NumPy

1. **Performance** : 10 à 100 fois plus rapide que les listes Python pour les opérations mathématiques
1. **Mémoire** : Occupation mémoire réduite
1. **Syntaxe** : Opérations vectorisées élégantes
1. **Fonctionnalités** : Algèbre linéaire, transformées de Fourier, génération aléatoire, etc.

```python
import numpy as np

# Comparaison de performances
liste = list(range(1000000))
tableau = np.arange(1000000)

# Opération : multiplier chaque élément par 2
# Liste Python : nécessite une boucle ou list comprehension
# NumPy : tableau * 2 (beaucoup plus rapide)

# Opérations mathématiques avancées
arr = np.array([1, 2, 3, 4, 5])

moyenne = np.mean(arr)           # 3.0
ecart_type = np.std(arr)         # ~1.41
somme_cumulative = np.cumsum(arr) # array([ 1,  3,  6, 10, 15])
```

## Chapitre 8 : Bonnes Pratiques et Pièges à Éviter

### 8.1 Bonnes pratiques

1. **Nommage clair** : Utilisez des noms explicites au pluriel pour les listes

```python
# Bien
etudiants = ["Alice", "Bob", "Charlie"]

# À éviter
e = ["Alice", "Bob", "Charlie"]
liste1 = ["Alice", "Bob", "Charlie"]
```

1. **Immuabilité quand possible** : Utilisez des tuples pour les données non modifiables

```python
# Coordonnées (ne doivent pas changer)
point = (10, 20)  # Tuple, non modifiable

# Liste de courses (va évoluer)
courses = ["pain", "lait"]  # Liste, modifiable
```

1. **Compréhensions pour la clarté** : Mais pas au détriment de la lisibilité

```python
# Bien : simple et lisible
carres = [x**2 for x in range(10)]

# À éviter : trop complexe
resultat = [x**2 if x % 2 == 0 else x**3 for x in range(20) if x > 5]
# Préférez une boucle for classique dans ce cas
```

1. **Vérification d’appartenance** : Utilisez `in` plutôt que de parcourir manuellement

```python
# Bien
if "pomme" in fruits:
    print("Trouvé")

# À éviter
trouve = False
for fruit in fruits:
    if fruit == "pomme":
        trouve = True
```

### 8.2 Pièges courants

#### Piège 1 : Modification pendant l’itération

```python
# DANGEREUX
nombres = [1, 2, 3, 4, 5]
for nombre in nombres:
    if nombre % 2 == 0:
        nombres.remove(nombre)  # Comportement imprévisible

# CORRECT
nombres = [1, 2, 3, 4, 5]
nombres = [n for n in nombres if n % 2 != 0]
```

#### Piège 2 : Copie de référence vs copie de valeur

```python
# ATTENTION : Copie de référence
liste1 = [1, 2, 3]
liste2 = liste1  # Pas une copie, mais une référence
liste2.append(4)
print(liste1)  # [1, 2, 3, 4] - Modifiée aussi !

# CORRECT : Vraie copie
liste1 = [1, 2, 3]
liste2 = liste1.copy()
liste2.append(4)
print(liste1)  # [1, 2, 3] - Non affectée
```

#### Piège 3 : Listes par défaut dans les fonctions

```python
# DANGEREUX
def ajouter_element(element, liste=[]):
    liste.append(element)
    return liste

# Comportement surprenant
print(ajouter_element(1))  # [1]
print(ajouter_element(2))  # [1, 2] - Pas [2] !

# CORRECT
def ajouter_element(element, liste=None):
    if liste is None:
        liste = []
    liste.append(element)
    return liste
```

#### Piège 4 : Listes imbriquées avec multiplication

```python
# DANGEREUX
matrice = [[0] * 3] * 3  # Crée 3 références à la même liste
matrice[0][0] = 1
print(matrice)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - Toutes modifiées !

# CORRECT
matrice = [[0] * 3 for _ in range(3)]
matrice[0][0] = 1
print(matrice)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

## Chapitre 9 : Exercices Pratiques

### Exercice 1 : Filtrage de données

Créez une fonction qui prend une liste de nombres et retourne une nouvelle liste contenant uniquement les nombres pairs et positifs.

```python
def filtrer_pairs_positifs(nombres):
    return [n for n in nombres if n > 0 and n % 2 == 0]

# Test
resultat = filtrer_pairs_positifs([-2, 1, 2, 3, 4, -4, 6, 0])
print(resultat)  # [2, 4, 6]
```

### Exercice 2 : Rotation de liste

Implémentez une fonction qui effectue une rotation d’une liste de n positions vers la droite.

```python
def rotation(liste, n):
    if not liste:
        return liste
    n = n % len(liste)  # Gestion des rotations > longueur
    return liste[-n:] + liste[:-n]

# Test
print(rotation([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
```

### Exercice 3 : Aplatissement de liste

Transformez une liste imbriquée en liste simple (un seul niveau).

```python
def aplatir(liste):
    resultat =​​​​​​​​​​​​​​​​
```