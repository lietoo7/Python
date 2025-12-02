Tableaux et Dictionnaires en Python 3.13

## Tableaux

### Définition
Un **tableau** en Python est une liste dynamique et flexible qui peut contenir plusieurs types de données.

### Création et Initialisation
```python
# Méthodes de création
liste_vide = []
liste_vide = list()
liste_avec_elements = [1, 2, 3, 'texte', True]
```

### Opérations Fondamentales
```python
# Ajout d'éléments
ma_liste = [1, 2, 3]
ma_liste.append(4)  # Ajoute à la fin
ma_liste.insert(0, 0)  # Insère à un index spécifique

# Suppression
del ma_liste[1]  # Supprime par index
ma_liste.remove(2)  # Supprime la première occurrence

# Slicing
sous_liste = ma_liste[1:4]  # Extraction de sous-liste
```

### Méthodes Avancées
```python
# Transformation et manipulation
liste_triee = sorted(ma_liste)
liste_inversee = ma_liste[::-1]
longueur = len(ma_liste)
```

## Dictionnaires

### Définition
Un **dictionnaire** est une structure de données de type table de hachage permettant un stockage clé-valeur.

### Création et Initialisation
```python
# Méthodes de création
dict_vide = {}
dict_vide = dict()

# Création avec des valeurs
utilisateur = {
    'nom': 'Dupont',
    'age': 30,
    'actif': True
}
```

### Opérations Fondamentales
```python
# Accès et modification
valeur = utilisateur['nom']
utilisateur['email'] = 'dupont@exemple.com'  # Ajout

# Méthodes sécurisées
valeur = utilisateur.get('prenom', 'Non défini')
```

## Implémentation Interne

### Tableaux (Liste)
- **Allocation dynamique**
- Croissance exponentielle
- Réallocation mémoire automatique

```python
class ListePersonnalisee:
    def __init__(self):
        self._capacite = 4
        self._elements = [None] * self._capacite
        self._taille = 0

    def ajouter(self, element):
        if self._taille == self._capacite:
            # Mécanisme de redimensionnement
            self._capacite *= 2
            nouvelle_liste = [None] * self._capacite
            for i in range(self._taille):
                nouvelle_liste[i] = self._elements[i]
            self._elements = nouvelle_liste
        
        self._elements[self._taille] = element
        self._taille += 1
```

### Dictionnaires
- **Table de hachage**
- Gestion des collisions
- Fonction de hachage optimisée

```python
class DictionnairePersonnalise:
    def __init__(self):
        self._taille = 8
        self._table = [[] for _ in range(self._taille)]
    def _hacher(self, cle):
        return hash(cle) % self._taille

    def ajouter(self, cle, valeur):
        index = self._hacher(cle)
        for item in self._table[index]:
            if item[0] == cle:
                item[1] = valeur
                return
        self._table[index].append([cle, valeur])
```

## Nouveautés Python 3.13

### Compilation et Performance
- **Nouveau moteur JIT (Just-In-Time)**
- Optimisations des structures de données
- Amélioration des performances d'exécution

### Exemples de Nouveautés
```python
# Nouvelles fonctionnalités de fusion
dict_base = {'a': 1, 'b': 2}
dict_maj = {'b': 3, 'c': 4}

# Fusion avec priorité aux valeurs de dict_maj
dict_final = dict_base | dict_maj
```

## Techniques Avancées

### Collections Spécialisées
```python
from collections import defaultdict, OrderedDict

# Dictionnaire avec valeur par défaut
compteur = defaultdict(int)
compteur['nouveau'] += 1  # Initialisation automatique

# Dictionnaire ordonné
config = OrderedDict([
    ('version', '3.13'),
    ('debug', True)
])
```

### Compréhensions
```python
# Création rapide de listes
carres = [x**2 for x in range(10)]

# Compréhension de dictionnaire
dict_carres = {x: x**2 for x in range(10)}
```

## Performances et Optimisations

### Complexités Temporelles

| Structure | Accès | Insertion | Suppression |
|-----------|-------|-----------|-------------|
| **Liste** | O(1) | O(n) | O(n) |
| **Dictionnaire** | O(1) | O(1) | O(1) |

### Stratégies d'Optimisation
- Préallocation de mémoire
- Utilisation de compréhensions
- Choix judicieux de la structure

```python
# Préallocation efficace
grand_tableau = [0] * 1000  # Plus performant que l'ajout successif

# Utilisation de générateurs pour l'économie mémoire
generateur = (x**2 for x in range(1000))
```

## Bonnes Pratiques

### Tableaux (Listes)
- Utiliser `.append()` pour l'ajout
- Éviter les insertions fréquentes au début
- Préallouer si la taille est connue

### Dictionnaires
- Préférer `.get()` pour les accès conditionnels
- Utiliser des clés immuables
- Gérer les clés inexistantes avec `.get()`

## Sécurité et Limitations

### Considérations Importantes
- Thread-safe depuis Python 3.12
- Limitation à la mémoire disponible
- Protection contre les attaques par collision de hachage

## Exemple Complet

```python
class GestionnaireUtilisateurs:
    def __init__(self):
        self._utilisateurs = {}
    
    def ajouter_utilisateur(self, identifiant, donnees):
        """Ajoute ou met à jour un utilisateur"""
        self._utilisateurs[identifiant] = donnees
    
    def obtenir_utilisateur(self, identifiant):
        """Récupère un utilisateur de manière sécurisée"""
        return self._utilisateurs.get(identifiant, None)
    
    def supprimer_utilisateur(self, identifiant):
        """Supprime un utilisateur"""
        if identifiant in self._utilisateurs:
            del self._utilisateurs[identifiant]
    
    def lister_utilisateurs(self):
        """Retourne tous les utilisateurs"""
        return list(self._utilisateurs.keys())

# Util
Je vais poursuivre le cours avec la dernière partie :

## Exemple Complet (suite)

```python
# Exemple d'utilisation
gestionnaire = GestionnaireUtilisateurs()

# Ajout d'utilisateurs
gestionnaire.ajouter_utilisateur('user1', {
    'nom': 'Dupont',
    'age': 30,
    'email': 'dupont@exemple.com'
})

gestionnaire.ajouter_utilisateur('user2', {
    'nom': 'Martin',
    'age': 25,
    'email': 'martin@exemple.com'
})

# Récupération et manipulation
utilisateur = gestionnaire.obtenir_utilisateur('user1')
print(utilisateur)  # Affiche les détails de l'utilisateur
```

## Patterns Avancés

### Dictionnaires Imbriqués
```python
# Structure complexe
entreprise = {
    'nom': 'TechCorp',
    'departements': {
        'informatique': {
            'employes': ['Alice', 'Bob'],
            'budget': 500000
        },
        'marketing': {
            'employes': ['Charlie', 'David'],
            'budget': 250000
        }
    }
}

# Accès imbriqué
employes_info = entreprise['departements']['informatique']['employes']
```

## Debugging et Inspection

### Méthodes Utiles
```python
# Inspection de structures
ma_liste = [1, 2, 3, 4, 5]
mon_dict = {'a': 1, 'b': 2}

# Méthodes d'inspection
print(len(ma_liste))  # Longueur
print(list(mon_dict.keys()))  # Clés
print(list(mon_dict.values()))  # Valeurs
```

## Considérations Avancées

### Typage et Annotations
```python
from typing import List, Dict, Any

def traiter_donnees(donnees: List[Dict[str, Any]]) -> None:
    """Fonction avec typage explicite"""
    for item in donnees:
        print(item)

# Utilisation
donnees = [
    {'nom': 'Dupont', 'age': 30},
    {'nom': 'Martin', 'age': 25}
]
traiter_donnees(donnees)
```

## Cas Particuliers

### Dictionnaires Ordonnés
```python
from collections import OrderedDict

# Dictionnaire qui maintient l'ordre d'insertion
config = OrderedDict()
config['version'] = '3.13'
config['debug'] = True
config['mode'] = 'production'

# L'ordre est préservé
for cle, valeur in config.items():
    print(f"{cle}: {valeur}")
```

## Erreurs Courantes et Solutions

### Gestion des Erreurs
```python
# Accès sécurisé
mon_dict = {'a': 1}

# Méthode recommandée
valeur = mon_dict.get('cle_inexistante', 'Valeur par défaut')

# Anti-pattern à éviter
try:
    valeur = mon_dict['cle_inexistante']
except KeyError:
    valeur = 'Valeur par défaut'
```

## Performance Comparée

### Benchmark Simplifié
```python
import timeit

# Comparaison de performances
def test_liste():
    return [x for x in range(1000)]

def test_generateur():
    return (x for x in range(1000))

# Mesure du temps d'exécution
temps_liste = timeit.timeit(test_liste, number=1000)
temps_generateur = timeit.timeit(test_generateur, number=1000)

print(f"Temps Liste: {temps_liste}")
print(f"Temps Générateur: {temps_generateur}")
```

Je vais ajouter une section détaillée sur les algorithmes de tri pour les listes en Python. Je l'intégrerai dans le cours, après la section sur les techniques avancées.

## Algorithmes de Tri

### Introduction aux Algorithmes de Tri

Les algorithmes de tri sont essentiels pour organiser et manipuler des données efficacement. Python propose plusieurs méthodes de tri, chacune avec ses propres caractéristiques de performance.

### Méthodes Intégrées de Tri

#### Tri Simple
```python
# Tri de base
ma_liste = [5, 2, 9, 1, 7]
ma_liste.sort()  # Tri en place
liste_triee = sorted(ma_liste)  # Nouveau tableau trié
```

### Algorithmes de Tri Détaillés

#### 1. Tri à Bulles (Bubble Sort)
```python
def tri_bulles(tableau):
    n = len(tableau)
    for i in range(n):
        # Optimisation : arrêter si aucun échange
        echange_effectue = False
        
        for j in range(0, n - i - 1):
            if tableau[j] > tableau[j + 1]:
                # Échange des éléments
                tableau[j], tableau[j + 1] = tableau[j + 1], tableau[j]
                echange_effectue = True
        
        # Si aucun échange, le tableau est déjà trié
        if not echange_effectue:
            break
    
    return tableau

# Exemple d'utilisation
liste = [64, 34, 25, 12, 22, 11, 90]
print(tri_bulles(liste))
```

#### 2. Tri par Insertion
```python
def tri_insertion(tableau):
    for i in range(1, len(tableau)):
        cle = tableau[i]
        j = i - 1
        
        # Déplacer les éléments du tableau qui sont plus grands que la clé
        while j >= 0 and tableau[j] > cle:
            tableau[j + 1] = tableau[j]
            j -= 1
        
        tableau[j + 1] = cle
    
    return tableau

# Exemple d'utilisation
liste = [64, 34, 25, 12, 22, 11, 90]
print(tri_insertion(liste))
```

#### 3. Tri Rapide (Quick Sort)
```python
def partition(tableau, bas, haut):
    pivot = tableau[haut]
    i = bas - 1
    
    for j in range(bas, haut):
        if tableau[j] <= pivot:
            i += 1
            tableau[i], tableau[j] = tableau[j], tableau[i]
    
    tableau[i + 1], tableau[haut] = tableau[haut], tableau[i + 1]
    return i + 1

def tri_rapide(tableau, bas, haut):
    if bas < haut:
        # Indice de partition
        pi = partition(tableau, bas, haut)
        
        # Trier séparément avant et après la partition
        tri_rapide(tableau, bas, pi - 1)
        tri_rapide(tableau, pi + 1, haut)
    
    return tableau

# Exemple d'utilisation
liste = [64, 34, 25, 12, 22, 11, 90]
print(tri_rapide(liste, 0, len(liste) - 1))
```

#### 4. Tri Fusion (Merge Sort)
```python
def fusionner(gauche, droite):
    resultat = []
    i = j = 0
    
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    
    resultat.extend(gauche[i:])
Je vais continuer la section sur les algorithmes de tri :

```python
    resultat.extend(droite[j:])
    return resultat

def tri_fusion(tableau):
    # Cas de base : tableau de 0 ou 1 élément
    if len(tableau) <= 1:
        return tableau
    
    # Division du tableau
    milieu = len(tableau) // 2
    gauche = tri_fusion(tableau[:milieu])
    droite = tri_fusion(tableau[milieu:])
    
    # Fusion des sous-tableaux triés
    return fusionner(gauche, droite)

# Exemple d'utilisation
liste = [64, 34, 25, 12, 22, 11, 90]
print(tri_fusion(liste))
```

### Comparaison des Algorithmes de Tri

| Algorithme | Complexité Temporelle | Complexité Spatiale | Stabilité |
|-----------|----------------------|---------------------|-----------|
| **Tri à Bulles** | O(n²) | O(1) | Stable |
| **Tri par Insertion** | O(n²) | O(1) | Stable |
| **Tri Rapide** | O(n log n) | O(log n) | Non stable |
| **Tri Fusion** | O(n log n) | O(n) | Stable |
| **Tri Python (Timsort)** | O(n log n) | O(n) | Stable |

### Algorithme de Tri Hybride de Python (Timsort)

```python
# Timsort est l'algorithme de tri par défaut de Python
# Combinaison de Merge Sort et Insertion Sort

def timsort(tableau):
    # Implémentation interne optimisée
    return sorted(tableau)

# Exemple
liste = [64, 34, 25, 12, 22, 11, 90]
print(timsort(liste))
```

### Tri Personnalisé

```python
# Tri avec clé de comparaison personnalisée
etudiants = [
    {'nom': 'Alice', 'note': 85},
    {'nom': 'Bob', 'note': 92},
    {'nom': 'Charlie', 'note': 78}
]

# Tri par note
tries_par_note = sorted(etudiants, key=lambda x: x['note'], reverse=True)
print(tries_par_note)

# Tri multi-critères
tries_complexe = sorted(
    etudiants, 
    key=lambda x: (-x['note'], x['nom'])
)
```

### Optimisations Avancées

```python
import array
import numpy as np

# Utilisation de tableaux pour des performances optimales
# Tableau Python
tableau_python = array.array('i', [5, 2, 9, 1, 7])
tableau_python.sort()

# Numpy pour des calculs intensifs
tableau_numpy = np.array([5, 2, 9, 1, 7])
tableau_numpy.sort()
```

### Exercice Pratique : Tri Personnalisé

```python
class SystemeTri:
    @staticmethod
    def trier_par_criteres_multiples(collection, criteres):
        """
        Trie une collection selon plusieurs critères
        
        :param collection: Liste à trier
        :param criteres: Liste de fonctions de clé de tri
        :return: Liste triée
        """
        def cle_composee(element):
            return tuple(critere(element) for critere in criteres)
        
        return sorted(collection, key=cle_composee)

# Exemple d'utilisation
produits = [
    {'nom': 'Ordinateur', 'prix': 1000, 'stock': 5},
    {'nom': 'Téléphone', 'prix': 500, 'stock': 10},
    {'nom': 'Tablette', 'prix': 300, 'stock': 5}
]

Je vais continuer avec la fin de l'exemple et ajouter quelques sections supplémentaires :

```python
# Trier par prix croissant, puis par stock décroissant
tries = SystemeTri.trier_par_criteres_multiples(
    produits, 
    [
        lambda x: x['prix'],  # Premier critère : prix croissant
        lambda x: -x['stock']  # Deuxième critère : stock décroissant
    ]
)
print(tries)
```

### Algorithmes de Recherche Avancés

```python
def recherche_binaire(tableau, element):
    """
    Algorithme de recherche binaire efficace
    
    :param tableau: Liste triée
    :param element: Élément à rechercher
    :return: Index de l'élément ou -1
    """
    gauche, droite = 0, len(tableau) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        
        if tableau[milieu] == element:
            return milieu
        elif tableau[milieu] < element:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    return -1

# Exemple d'utilisation
tableau_trie = [1, 3, 5, 7, 9, 11, 13, 15]
print(recherche_binaire(tableau_trie, 7))  # Retourne l'index
```

### Techniques de Tri Avancées

#### Tri Parallèle
```python
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def tri_parallele(grand_tableau):
    """
    Implémentation de tri parallèle
    
    :param grand_tableau: Liste à trier
    :return: Liste triée
    """
    # Nombre de cœurs disponibles
    nombre_coeurs = multiprocessing.cpu_count()
    
    # Division du tableau
    taille_chunk = len(grand_tableau) // nombre_coeurs
    chunks = [
        grand_tableau[i:i + taille_chunk] 
        for i in range(0, len(grand_tableau), taille_chunk)
    ]
    
    # Tri parallèle
    with ProcessPoolExecutor() as executeur:
        chunks_tries = list(executeur.map(sorted, chunks))
    
    # Fusion des résultats
    resultat_final = []
    while chunks_tries:
        chunk_min = min(
            (chunk[0] for chunk in chunks_tries if chunk), 
            key=lambda x: x
        )
        
        for i, chunk in enumerate(chunks_tries):
            if chunk and chunk[0] == chunk_min:
                resultat_final.append(chunk.pop(0))
                if not chunk:
                    del chunks_tries[i]
                break
    
    return resultat_final

# Exemple
grand_tableau = list(range(1000000, 0, -1))
tableau_trie = tri_parallele(grand_tableau)
```

### Optimisations et Bonnes Pratiques

1. **Choix de l'Algorithme**
   - Utiliser `sorted()` pour la plupart des cas
   - Préférer le tri en place avec `.sort()`
   - Éviter les tris manuels pour de grands ensembles

2. **Performances Comparatives**
```python
import timeit

def benchmark_tri():
    tableau_test = list(range(10000, 0, -1))
    
    # Comparaison des performances
    temps_sort = timeit.timeit(
        lambda: sorted(tableau_test), 
        number=100
    )
    
    temps_quicksort = timeit.timeit(
        lambda: tri_rapide(tableau_test, 0, len(tableau_test) - 1), 
        number=100
    )
    
    print(f"Temps Timsort (Python): {temps_sort}")
    print(f"Temps Quick Sort: {temps_quicksort}")

benchmark_tri()
```

### Considérations Avancées de Tri

#### Tri pour Grands Ensembles de Données
```python
import heapq

def tri_par_tas_externe(fichier_entree, fichier_sortie, taille_memoire=1000):
    """
    Algorithme de tri externe pour fichiers volumineux
    
    :param fichier_entree: Chemin du fichier à trier
    :param fichier_sortie: Chemin du fichier de sortie
    :param taille_memoire: Nombre d'éléments à charger en mémoire
    """
    # Lecture et tri de fragments
    fragments = []
    with open(fichier_entree, 'r') as fichier:
        while True:
            fragment = list(heapq.nsmallest(
                taille_memoire, 
                (float(ligne.strip()) for ligne in fichier)
            ))
            
            if not fragment:
                break
            
            fragment.sort()
            fragments.append(fragment)
    
    # Fusion des fragments triés
    with open(fichier_sortie, 'w') as sortie:
        for element in heapq.merge(*fragments):
            sortie.write(f"{element}\n")
```

### Algorithmes de Tri Spécialisés

#### Tri Counting (pour entiers)
```python
def tri_counting(tableau):
    """
    Algorithme de tri par comptage
    Optimal pour les entiers dans une plage limitée
    
    :param tableau: Liste d'entiers
    :return: Liste triée
    """
    if not tableau:
        return tableau
    
    # Trouver la plage des valeurs
    min_val = min(tableau)
    max_val = max(tableau)
    
    # Création du tableau de comptage
    comptage = [0] * (max_val - min_val + 1)
    
    # Compter les occurrences
    for nombre in tableau:
        comptage[nombre - min_val] += 1
    
    # Reconstruction du tableau trié
    resultat = []
    for i, count in enumerate(comptage):
        resultat.extend([i + min_val] * count)
    
    return resultat

# Exemple
nombres = [4, 2, 2, 8, 3, 3, 1]
print(tri_counting(nombres))
```

### Annexe : Complexités et Caractéristiques

#### Tableau Comparatif Détaillé

| Algorithme | Meilleur Cas | Cas Moyen | Pire Cas | Mémoire | Stable |
|-----------|--------------|-----------|----------|---------|--------|
| Tri à Bulles | O(n) | O(n²) | O(n²) | O(1) | Oui |
| Tri par Insertion | O(n) | O(n²) | O(n²) | O(1) | Oui |
| Tri Rapide | O(n log n) | O(n log n) | O(n²) | O(log n) | Non |
| Tri Fusion | O(n log n) | O(n log n) | O(n log n) | O(n) | Oui |
| Tri par Tas | O(n log n) | O(n log n) | O(n log n) | O(1) | Non |

### Conclusion des Algorithmes de Tri

#### Points Clés
- Comprendre les différents algorithmes de tri
- Choisir l'algorithme adapté selon le contexte
- Privilégier les méthodes intégrées de Python
- Optimiser selon la taille et le type de données

### Perspectives et Tendances Futures

1. **Intelligence Artificielle**
   - Algorithmes de tri adaptatifs
   - Optimisation par apprentiss
