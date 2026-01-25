# Listes de Dictionnaires et Algorithmes de Recherche

## Introduction

Dans les chapitres précédents, nous avons exploré séparément les listes et les dictionnaires. Nous franchissons maintenant une étape décisive en combinant ces deux structures pour créer ce qui constitue le fondement de la manipulation de données en Python moderne : **les listes de dictionnaires**.

Cette structure hybride est omniprésente dans le développement logiciel :

- **APIs Web** : Les réponses JSON sont essentiellement des listes de dictionnaires
- **Bases de données** : Les résultats de requêtes sont retournés sous cette forme
- **Analyse de données** : Pandas, la bibliothèque de référence, utilise cette logique
- **Applications métier** : Gestion de clients, produits, commandes, etc.

Comprendre comment manipuler efficacement ces structures, combiné à la maîtrise des algorithmes de recherche, vous permettra de traiter des volumes importants de données avec élégance et performance.

-----

## Chapitre 1 : Fondements des Listes de Dictionnaires

### 1.1 Concept et structure

Une liste de dictionnaires représente une **collection d’entités structurées**. Pensez-y comme à une table de base de données ou une feuille Excel :

```
┌─────────────────────────────────────────────┐
│              LISTE (Table)                  │
├─────────────────────────────────────────────┤
│  [0] → {"nom": "Alice", "note": 18}         │
│  [1] → {"nom": "Bob", "note": 12}           │
│  [2] → {"nom": "Charlie", "note": 15}       │
└─────────────────────────────────────────────┘
```

**Analogie du monde réel :**

Imaginez un classeur de fiches d’élèves :

- **La liste** = Le classeur (conteneur ordonné)
- **Chaque dictionnaire** = Une fiche individuelle (ensemble de propriétés)
- **Les clés du dictionnaire** = Les rubriques de la fiche (nom, note, sport…)
- **Les valeurs** = Les informations renseignées

### 1.2 Création d’une liste de dictionnaires

```python
# Exemple 1 : Base d'étudiants
etudiants = [
    {"nom": "Alice", "age": 20, "note": 18, "sport": "Judo"},
    {"nom": "Bob", "age": 22, "note": 12, "sport": "Tennis"},
    {"nom": "Charlie", "age": 21, "note": 15, "sport": "Judo"},
    {"nom": "Diana", "age": 19, "note": 16, "sport": "Natation"}
]

# Exemple 2 : Catalogue de produits
produits = [
    {
        "id": 1,
        "nom": "Laptop Dell XPS",
        "prix": 1299.99,
        "categorie": "Informatique",
        "stock": 15,
        "en_promotion": True
    },
    {
        "id": 2,
        "nom": "iPhone 15",
        "prix": 999.99,
        "categorie": "Téléphonie",
        "stock": 42,
        "en_promotion": False
    },
    {
        "id": 3,
        "nom": "Sony WH-1000XM5",
        "prix": 349.99,
        "categorie": "Audio",
        "stock": 8,
        "en_promotion": True
    }
]

# Exemple 3 : Historique de transactions
transactions = [
    {
        "date": "2024-01-15",
        "type": "achat",
        "montant": 45.50,
        "categorie": "Alimentation"
    },
    {
        "date": "2024-01-16",
        "type": "vente",
        "montant": 120.00,
        "categorie": "Électronique"
    }
]
```

### 1.3 Structure équivalente JSON

La correspondance avec JSON est directe, ce qui explique l’importance de cette structure :

```python
import json

# Python → JSON
etudiants_json = json.dumps(etudiants, indent=2, ensure_ascii=False)
print(etudiants_json)

# Résultat :
"""
[
  {
    "nom": "Alice",
    "age": 20,
    "note": 18,
    "sport": "Judo"
  },
  {
    "nom": "Bob",
    "age": 22,
    "note": 12,
    "sport": "Tennis"
  }
]
"""

# JSON → Python
donnees_json = '[{"nom": "Eve", "age": 23}]'
etudiants_charges = json.loads(donnees_json)
```

-----

## Chapitre 2 : Accès aux Données

### 2.1 Accès basique : Chaînage d’index et de clés

L’accès aux données combine la logique des listes (index) et des dictionnaires (clés).

```python
classe = [
    {"nom": "Alice", "note": 18, "sport": "Judo"},
    {"nom": "Bob", "note": 12, "sport": "Tennis"},
    {"nom": "Charlie", "note": 15, "sport": "Judo"}
]

# Accès à un dictionnaire entier (élément de la liste)
premier_etudiant = classe[0]
print(premier_etudiant)  # {'nom': 'Alice', 'note': 18, 'sport': 'Judo'}

# Accès à une valeur spécifique (chaînage)
nom_premier = classe[0]["nom"]      # "Alice"
note_deuxieme = classe[1]["note"]   # 12
sport_troisieme = classe[2]["sport"] # "Judo"

# Modification d'une valeur
classe[0]["note"] = 19
print(classe[0])  # {'nom': 'Alice', 'note': 19, 'sport': 'Judo'}

# Ajout d'une nouvelle propriété
classe[1]["ville"] = "Paris"
print(classe[1])  # {'nom': 'Bob', 'note': 12, 'sport': 'Tennis', 'ville': 'Paris'}
```

### 2.2 Parcours de base

```python
classe = [
    {"nom": "Alice", "note": 18, "sport": "Judo"},
    {"nom": "Bob", "note": 12, "sport": "Tennis"},
    {"nom": "Charlie", "note": 15, "sport": "Judo"}
]

# Parcours simple
for etudiant in classe:
    print(f"{etudiant['nom']} a obtenu {etudiant['note']}/20")

# Sortie :
# Alice a obtenu 18/20
# Bob a obtenu 12/20
# Charlie a obtenu 15/20

# Parcours avec index
for i, etudiant in enumerate(classe):
    print(f"{i+1}. {etudiant['nom']} - {etudiant['sport']}")

# Sortie :
# 1. Alice - Judo
# 2. Bob - Tennis
# 3. Charlie - Judo

# Parcours conditionnel
for etudiant in classe:
    if etudiant["note"] >= 15:
        print(f" {etudiant['nom']} : Mention Bien ou plus")
```

### 2.3 Accès sécurisé avec `.get()`

```python
produits = [
    {"nom": "Laptop", "prix": 1299.99, "stock": 15},
    {"nom": "Souris", "prix": 29.99},  # Pas de clé "stock"
]

# RISQUÉ : Peut lever KeyError
for produit in produits:
    try:
        print(f"{produit['nom']} : {produit['stock']} en stock")
    except KeyError:
        print(f"{produit['nom']} : Stock non renseigné")

# RECOMMANDÉ : Utiliser .get()
for produit in produits:
    stock = produit.get("stock", "Non renseigné")
    print(f"{produit['nom']} : {stock}")

# Sortie :
# Laptop : 15
# Souris : Non renseigné
```

-----

## Chapitre 3 : Patterns de Manipulation Fondamentaux

### 3.1 Pattern 1 : Filtrage (Recherche conditionnelle)

Le filtrage consiste à extraire un sous-ensemble de la liste selon un critère.

#### Syntaxe de base

```python
classe = [
    {"nom": "Alice", "note": 18, "sport": "Judo"},
    {"nom": "Bob", "note": 12, "sport": "Tennis"},
    {"nom": "Charlie", "note": 15, "sport": "Judo"},
    {"nom": "Diana", "note": 16, "sport": "Natation"}
]

# Filtrage simple : Tous les judokas
judokas = [eleve for eleve in classe if eleve["sport"] == "Judo"]
print(judokas)
# [{'nom': 'Alice', 'note': 18, 'sport': 'Judo'},
#  {'nom': 'Charlie', 'note': 15, 'sport': 'Judo'}]

# Filtrage par note : Mentions (>= 14)
mentions = [eleve for eleve in classe if eleve["note"] >= 14]
print(f"{len(mentions)} élèves ont une mention")

# Filtrage multiple : Judokas avec mention
judokas_mentions = [
    eleve for eleve in classe 
    if eleve["sport"] == "Judo" and eleve["note"] >= 14
]

# Filtrage avec négation : Non-judokas
non_judokas = [eleve for eleve in classe if eleve["sport"] != "Judo"]
```

#### Exemples pratiques

```python
produits = [
    {"nom": "Laptop", "prix": 1299.99, "stock": 15, "promotion": True},
    {"nom": "Souris", "prix": 29.99, "stock": 50, "promotion": False},
    {"nom": "Écran", "prix": 449.99, "stock": 8, "promotion": True},
    {"nom": "Clavier", "prix": 129.99, "stock": 0, "promotion": False}
]

# Produits en promotion
promos = [p for p in produits if p["promotion"]]

# Produits en stock (>0)
disponibles = [p for p in produits if p["stock"] > 0]

# Produits chers (>500€) en promotion
promos_cheres = [
    p for p in produits 
    if p["prix"] > 500 and p["promotion"]
]

# Produits en rupture
ruptures = [p for p in produits if p["stock"] == 0]
print(f"{len(ruptures)} produit(s) en rupture de stock")
```

### 3.2 Pattern 2 : Extraction (Projection de colonnes)

L’extraction consiste à récupérer uniquement certaines valeurs de chaque dictionnaire.

```python
classe = [
    {"nom": "Alice", "note": 18, "sport": "Judo"},
    {"nom": "Bob", "note": 12, "sport": "Tennis"},
    {"nom": "Charlie", "note": 15, "sport": "Judo"}
]

# Extraire uniquement les noms
noms = [eleve["nom"] for eleve in classe]
print(noms)  # ['Alice', 'Bob', 'Charlie']

# Extraire uniquement les notes
notes = [eleve["note"] for eleve in classe]
print(notes)  # [18, 12, 15]

# Extraire plusieurs champs (tuples)
infos = [(eleve["nom"], eleve["note"]) for eleve in classe]
print(infos)  # [('Alice', 18), ('Bob', 12), ('Charlie', 15)]

# Extraire avec transformation
noms_majuscules = [eleve["nom"].upper() for eleve in classe]
# ['ALICE', 'BOB', 'CHARLIE']

# Combiner extraction et filtrage
noms_mentions = [
    eleve["nom"] 
    for eleve in classe 
    if eleve["note"] >= 14
]
print(noms_mentions)  # ['Alice', 'Charlie']
```

### 3.3 Pattern 3 : Transformation (Mapping)

La transformation crée une nouvelle liste en modifiant chaque élément.

```python
produits = [
    {"nom": "Laptop", "prix": 1000},
    {"nom": "Souris", "prix": 25},
    {"nom": "Écran", "prix": 400}
]

# Ajouter une réduction de 10%
produits_reduits = [
    {
        **p,  # Copie toutes les clés existantes
        "prix_reduit": p["prix"] * 0.9
    }
    for p in produits
]

print(produits_reduits[0])
# {'nom': 'Laptop', 'prix': 1000, 'prix_reduit': 900.0}

# Ajouter la TVA (20%)
produits_ttc = [
    {
        "nom": p["nom"],
        "prix_ht": p["prix"],
        "prix_ttc": p["prix"] * 1.2
    }
    for p in produits
]

# Enrichissement de données
classe = [
    {"nom": "Alice", "note": 18},
    {"nom": "Bob", "note": 12},
    {"nom": "Charlie", "note": 15}
]

classe_enrichie = [
    {
        **eleve,
        "mention": "Très bien" if eleve["note"] >= 16 
                   else "Bien" if eleve["note"] >= 14 
                   else "Assez bien" if eleve["note"] >= 12 
                   else "Passable",
        "reussi": eleve["note"] >= 10
    }
    for eleve in classe
]
```

### 3.4 Pattern 4 : Agrégation (Calculs statistiques)

```python
classe = [
    {"nom": "Alice", "note": 18},
    {"nom": "Bob", "note": 12},
    {"nom": "Charlie", "note": 15},
    {"nom": "Diana", "note": 16}
]

# Moyenne de la classe
moyenne = sum(eleve["note"] for eleve in classe) / len(classe)
print(f"Moyenne : {moyenne:.2f}/20")  # 15.25

# Note minimale et maximale
note_min = min(eleve["note"] for eleve in classe)
note_max = max(eleve["note"] for eleve in classe)
print(f"Notes : {note_min} à {note_max}")

# Trouver le meilleur élève (dictionnaire complet)
meilleur = max(classe, key=lambda x: x["note"])
print(f"Meilleur élève : {meilleur['nom']} ({meilleur['note']}/20)")

# Trouver le moins bon
moins_bon = min(classe, key=lambda x: x["note"])

# Nombre d'élèves ayant la moyenne
nb_reussis = sum(1 for eleve in classe if eleve["note"] >= 10)
print(f"{nb_reussis}/{len(classe)} élèves ont la moyenne")

# Taux de réussite
taux_reussite = (nb_reussis / len(classe)) * 100
print(f"Taux de réussite : {taux_reussite:.1f}%")
```

### 3.5 Pattern 5 : Groupement (Group By)

```python
from collections import defaultdict

classe = [
    {"nom": "Alice", "sport": "Judo", "note": 18},
    {"nom": "Bob", "sport": "Tennis", "note": 12},
    {"nom": "Charlie", "sport": "Judo", "note": 15},
    {"nom": "Diana", "sport": "Natation", "note": 16},
    {"nom": "Eve", "sport": "Tennis", "note": 14}
]

# Grouper par sport
groupes_sport = defaultdict(list)

for eleve in classe:
    groupes_sport[eleve["sport"]].append(eleve)

# Affichage
for sport, eleves in groupes_sport.items():
    print(f"\n{sport} ({len(eleves)} élèves) :")
    for eleve in eleves:
        print(f"  - {eleve['nom']} : {eleve['note']}/20")

# Sortie :
# Judo (2 élèves) :
#   - Alice : 18/20
#   - Charlie : 15/20
# Tennis (2 élèves) :
#   - Bob : 12/20
#   - Eve : 14/20
# Natation (1 élèves) :
#   - Diana : 16/20

# Moyenne par sport
moyennes_sport = {
    sport: sum(e["note"] for e in eleves) / len(eleves)
    for sport, eleves in groupes_sport.items()
}

print("\nMoyennes par sport :")
for sport, moyenne in sorted(moyennes_sport.items(), key=lambda x: x[1], reverse=True):
    print(f"{sport:15} : {moyenne:.2f}/20")
```

-----

## Chapitre 4 : Introduction aux Algorithmes de Recherche

### 4.1 Pourquoi les algorithmes de recherche ?

Lorsque vous manipulez des listes de dictionnaires, une opération courante consiste à **trouver un élément spécifique**. La performance de cette recherche peut varier considérablement selon l’algorithme utilisé et la structure de vos données.

**Exemple de problématique :**

```python
utilisateurs = [
    {"id": 1, "nom": "Alice"},
    {"id": 2, "nom": "Bob"},
    # ... 10 000 utilisateurs
    {"id": 10000, "nom": "Zack"}
]

# Comment trouver rapidement l'utilisateur avec id=7543 ?
```

### 4.2 Recherche Linéaire (Séquentielle)

**Principe :** Parcourir chaque élément jusqu’à trouver celui recherché.

**Complexité temporelle :** O(n) - Dans le pire cas, on examine tous les éléments.

```python
def recherche_lineaire(liste, cle, valeur):
    """
    Recherche linéaire dans une liste de dictionnaires.
    
    Args:
        liste: Liste de dictionnaires à parcourir
        cle: La clé du dictionnaire à vérifier
        valeur: La valeur recherchée
    
    Returns:
        Le dictionnaire trouvé ou None
    """
    for element in liste:
        if element.get(cle) == valeur:
            return element
    return None

# Utilisation
etudiants = [
    {"id": 1, "nom": "Alice", "note": 18},
    {"id": 2, "nom": "Bob", "note": 12},
    {"id": 3, "nom": "Charlie", "note": 15}
]

resultat = recherche_lineaire(etudiants, "nom", "Bob")
print(resultat)  # {'id': 2, 'nom': 'Bob', 'note': 12}

# Avec list comprehension (plus pythonique)
bob = [e for e in etudiants if e["nom"] == "Bob"]
if bob:
    print(bob[0])  # Premier résultat
```

**Avantages :**

- Simple à implémenter
- Fonctionne sur des données non triées
- Efficace pour de petites listes

**Inconvénients :**

- Lent pour de grandes listes
- Parcourt potentiellement toute la liste

### 4.3 Recherche avec Index (Dictionnaire de lookup)

**Principe :** Créer un index (dictionnaire) pour accès direct en O(1).

```python
# Liste originale
produits = [
    {"id": 101, "nom": "Laptop", "prix": 1299},
    {"id": 102, "nom": "Souris", "prix": 29},
    {"id": 103, "nom": "Écran", "prix": 449}
]

# Créer un index par ID
index_id = {p["id"]: p for p in produits}

# Recherche instantanée O(1)
produit_102 = index_id.get(102)
print(produit_102)  # {'id': 102, 'nom': 'Souris', 'prix': 29}

# Index multiple (par nom)
index_nom = {p["nom"]: p for p in produits}
laptop = index_nom.get("Laptop")

# Attention aux doublons : le dernier écrase les précédents
# Pour gérer les doublons :
from collections import defaultdict

produits_avec_doublons = [
    {"categorie": "Informatique", "nom": "Laptop"},
    {"categorie": "Informatique", "nom": "Souris"},
    {"categorie": "Audio", "nom": "Casque"}
]

index_categorie = defaultdict(list)
for p in produits_avec_doublons:
    index_categorie[p["categorie"]].append(p)

print(index_categorie["Informatique"])
# [{'categorie': 'Informatique', 'nom': 'Laptop'},
#  {'categorie': 'Informatique', 'nom': 'Souris'}]
```

**Avantages :**

- Recherche ultra-rapide O(1)
- Idéal pour recherches fréquentes

**Inconvénients :**

- Consomme plus de mémoire
- Nécessite une reconstruction si les données changent

### 4.4 Recherche Binaire (sur données triées)

**Principe :** Diviser l’espace de recherche par deux à chaque itération.

**Prérequis :** Les données doivent être **triées** par le critère de recherche.

**Complexité temporelle :** O(log n) - Bien plus rapide que linéaire.

```python
def recherche_binaire_dict(liste_triee, cle, valeur):
    """
    Recherche binaire dans une liste de dictionnaires triée.
    
    Args:
        liste_triee: Liste triée par la clé spécifiée
        cle: La clé du dictionnaire à vérifier
        valeur: La valeur recherchée
    
    Returns:
        Le dictionnaire trouvé ou None
    """
    gauche, droite = 0, len(liste_triee) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        valeur_milieu = liste_triee[milieu][cle]
        
        if valeur_milieu == valeur:
            return liste_triee[milieu]
        elif valeur_milieu < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    return None

# Données triées par ID
etudiants_tries = [
    {"id": 1, "nom": "Alice"},
    {"id": 2, "nom": "Bob"},
    {"id": 3, "nom": "Charlie"},
    {"id": 4, "nom": "Diana"},
    {"id": 5, "nom": "Eve"}
]

resultat = recherche_binaire_dict(etudiants_tries, "id", 3)
print(resultat)  # {'id': 3, 'nom': 'Charlie'}
```

**Comparaison de performance :**

```python
import time

# Générer une grande liste
n = 100000
grande_liste = [{"id": i, "valeur": f"item_{i}"} for i in range(n)]

# Recherche linéaire
debut = time.time()
resultat = [item for item in grande_liste if item["id"] == 99999]
temps_lineaire = time.time() - debut

# Recherche binaire
debut = time.time()
resultat = recherche_binaire_dict(grande_liste, "id", 99999)
temps_binaire = time.time() - debut

print(f"Linéaire : {temps_lineaire:.6f}s")
print(f"Binaire  : {temps_binaire:.6f}s")
print(f"Gain     : {temps_lineaire/temps_binaire:.0f}x plus rapide")
```

### 4.5 Fonction `filter()` et recherches complexes

```python
produits = [
    {"nom": "Laptop", "prix": 1299, "stock": 15, "categorie": "Informatique"},
    {"nom": "Souris", "prix": 29, "stock": 50, "categorie": "Informatique"},
    {"nom": "Casque", "prix": 199, "stock": 8, "categorie": "Audio"},
    {"nom": "Écran", "prix": 449, "stock": 12, "categorie": "Informatique"}
]

# Recherche avec filter()
def est_informatique_cher(produit):
    return produit["categorie"] == "Informatique" and produit["prix"] > 500

resultats = list(filter(est_informatique_cher, produits))

# Équivalent avec list comprehension (plus pythonique)
resultats = [
    p for p in produits 
    if p["categorie"] == "Informatique" and p["prix"] > 500
]

# Recherche multi-critères complexe
def recherche_avancee(produits, **criteres):
    """
    Recherche flexible avec critères multiples.
    
    Args:
        produits: Liste de produits
        **criteres: Paires clé-valeur pour le filtrage
    
    Returns:
        Liste des produits correspondants
    """
    resultats = produits
    
    for cle, valeur in criteres.items():
        if callable(valeur):  # Si la valeur est une fonction
            resultats = [p for p in resultats if valeur(p.get(cle))]
        else:
            resultats = [p for p in resultats if p.get(cle) == valeur]
    
    return resultats

# Utilisation
resultats = recherche_avancee(
    produits,
    categorie="Informatique",
    prix=lambda p: p > 500,  # Prix supérieur à 500
    stock=lambda s: s > 10    # Stock supérieur à 10
)
```

### 4.6 Optimisation : Indexation Multi-critères

```python
class IndexProduits:
    """Système d'indexation multi-critères pour recherche rapide."""
    
    def __init__(self, produits):
        self.produits = produits
        self._construire_index()
    
    def _construire_index(self):
        """Construit les index pour chaque critère."""
        from collections import defaultdict
        
        self.index_id = {p["id"]: p for p in self.produits}
        self.index_categorie = defaultdict(list)
        self.index_prix = defaultdict(list)
        
        for p in self.produits:
            self.index_categorie[p["categorie"]].append(p)
            # Index par tranche de prix
            tranche = (p["prix"] // 100) * 100
            self.index_prix[tranche].append(p)
    
    def chercher_par_id(self, id_produit):
        """Recherche O(1) par ID."""
        return self.index_id.get(id_produit)
    
    def chercher_par_categorie(self, categorie):
        """Recherche O(1) par catégorie."""
        return self.index_categorie.get(categorie, [])
    
    def chercher_par_plage_prix(self, min_prix, max_prix):
        """Recherche optimisée par plage de prix."""
        resultats = []
        for tranche in range((min_prix // 100) * 100, max_prix, 100):
            resultats.extend(self.index_prix.get(tranche, []))
        
        # Filtrage précis
        return [p for p in resultats if min_prix <= p["prix"] <= max_prix]

# Utilisation
produits = [
    {"id": 1, "nom": "Laptop", "prix": 1299, "categorie": "Informatique"},
    {"id": 2, "nom": "Souris", "prix": 29, "categorie": "Informatique"},
    {"id": 3, "nom": "Casque", "prix": 199, "categorie": "Audio"}
]

index = IndexProduits(produits)

# Recherches ultra-rapides
laptop = index.chercher_par_id(1)
informatique = index.chercher_par_categorie("Informatique")
gamme_moyenne = index.chercher_par_plage_prix(100, 500)
```

-----

## Chapitre 5 : Tri de Listes de Dictionnaires

### 5.1 Tri simple avec `sorted()` et `.sort()`

```python
etudiants = [
    {"nom": "Charlie", "note": 15},
    {"nom": "Alice", "note": 18},
    {"nom": "Bob", "note": 12}
]

# Tri par nom (alphabétique)
etudiants_tries_nom = sorted(etudiants, key=lambda x: x["nom"])
print(etudiants_tries_nom)
# [{'nom': 'Alice', 'note': 18},
#  {'nom': 'Bob', 'note': 12},
#  {'nom': 'Charlie', 'note': 15}]

# Tri par note (décroissant)
etudiants_tries_note = sorted(etudiants, key=lambda x: x["note"], reverse=True)
# [{'nom': 'Alice', 'note': 18},
#  {'nom': 'Charlie', 'note': 15},
#  {'nom': 'Bob', 'note': 12}]

# Tri en place (modifie la liste originale)
etudiants.sort(key=lambda x: x["note"])
```

### 5.2 Tri multi-critères

```python
produits = [
    {"nom": "Laptop", "categorie": "Informatique", "prix": 1299},
    {"nom": "Souris", "categorie": "Informatique", "prix": 29},
    {"nom": "Casque", "categorie": "Audio", "prix": 199},
    {"nom": "Écran", "categorie": "Informatique", "prix": 449}
]

# Tri par catégorie puis par prix
produits_tries = sorted(
    produits,
    key=lambda x: (x["categorie"], x["prix"])
)

for p in produits_tries:
    print(f"{p['categorie']:15} - {p['​​​​​​​​​​​​​​​​nom’]:10} : {p[‘prix’]}€”)

# Sortie :
# Audio           - Casque     : 199€
# Informatique    - Souris     : 29€
# Informatique    - Écran      : 449€
# Informatique    - Laptop     : 1299€
# Tri complexe : catégorie croissant, prix décroissant

produits_tries_mixte = sorted(
produits,
key=lambda x: (x[“categorie”], -x[“prix”])  # Négatif pour inverser
)

```
### 5.3 Tri avec fonction personnalisée

```python
from operator import itemgetter

etudiants = [
    {"nom": "Alice", "note": 18, "age": 20},
    {"nom": "Bob", "note": 12, "age": 22},
    {"nom": "Charlie", "note": 15, "age": 19}
]

# Méthode 1 : itemgetter (plus performant)
etudiants_tries = sorted(etudiants, key=itemgetter("note"))

# Méthode 2 : Fonction personnalisée complexe
def critere_tri(etudiant):
    """Tri personnalisé : priorité aux mentions, puis à l'âge."""
    mention = etudiant["note"] >= 14
    return (not mention, etudiant["age"])  # False avant True

etudiants_tries = sorted(etudiants, key=critere_tri)
```

-----

## Chapitre 6 : Cas Pratiques Avancés

### 6.1 Système de gestion de bibliothèque

```python
bibliotheque = [
    {
        "isbn": "978-2-1234-5680-3",
        "titre": "Python pour les nuls",
        "auteur": "John Doe",
        "annee": 2023,
        "disponible": True,
        "emprunts": 15
    },
    {
        "isbn": "978-2-9876-5432-1",
        "titre": "Algorithmes avancés",
        "auteur": "Jane Smith",
        "annee": 2022,
        "disponible": False,
        "emprunts": 42
    }
]

# Rechercher un livre
def chercher_livre(bibliotheque, terme):
    """Recherche dans titre ou auteur."""
    terme = terme.lower()
    return [
        livre for livre in bibliotheque
        if terme in livre["titre"].lower() 
        or terme in livre["auteur"].lower()
    ]

# Livres disponibles
disponibles = [l for l in bibliotheque if l["disponible"]]

# Livres les plus empruntés
top_emprunts = sorted(bibliotheque, key=lambda x: x["emprunts"], reverse=True)

# Statistiques
total_livres = len(bibliotheque)
total_disponibles = sum(1 for l in bibliotheque if l["disponible"])
taux_disponibilite = (total_disponibles / total_livres) * 100

print(f"Taux de disponibilité : {taux_disponibilite:.1f}%")
```

### 6.2 Analyse de ventes e-commerce

```python
ventes = [
    {"id": 1, "produit": "Laptop", "quantite": 2, "prix_unitaire": 1299, "date": "2024-01-15"},
    {"id": 2, "produit": "Souris", "quantite": 5, "prix_unitaire": 29, "date": "2024-01-15"},
    {"id": 3, "produit": "Laptop", "quantite": 1, "prix_unitaire": 1299, "date": "2024-01-16"},
]

# Ajouter le montant total à chaque vente
ventes_enrichies = [
    {
        **vente,
        "montant_total": vente["quantite"] * vente["prix_unitaire"]
    }
    for vente in ventes
]

# Chiffre d'affaires total
ca_total = sum(v["montant_total"] for v in ventes_enrichies)
print(f"CA total : {ca_total}€")

# Ventes par produit
from collections import defaultdict

ventes_par_produit = defaultdict(lambda: {"quantite": 0, "montant": 0})

for vente in ventes_enrichies:
    produit = vente["produit"]
    ventes_par_produit[produit]["quantite"] += vente["quantite"]
    ventes_par_produit[produit]["montant"] += vente["montant_total"]

# Affichage
for produit, stats in sorted(ventes_par_produit.items(), 
                             key=lambda x: x[1]["montant"], 
                             reverse=True):
    print(f"{produit:15} : {stats['quantite']} unités - {stats['montant']}€")
```

-----

## Aide-Mémoire Rapide

|**Objectif**            |**Code Type**                                      |
|------------------------|---------------------------------------------------|
|**Ajouter un élément**  |`liste.append({"cle": "valeur"})`                  |
|**Accéder à une valeur**|`liste[index]["cle"]`                              |
|**Filtrer**             |`[x for x in liste if x["cle"] == condition]`      |
|**Extraire une colonne**|`[x["cle"] for x in liste]`                        |
|**Trier**               |`sorted(liste, key=lambda x: x["cle"])`            |
|**Trouver le max**      |`max(liste, key=lambda x: x["cle"])`               |
|**Grouper**             |Utiliser `defaultdict(list)`                       |
|**Moyenne**             |`sum(x["cle"] for x in liste) / len(liste)`        |
|**Recherche**           |`next((x for x in liste if x["cle"] == val), None)`|

-----

## Conclusion

Les listes de dictionnaires constituent le fondement de la manipulation de données en Python moderne. Combinées à une compréhension solide des algorithmes de recherche, elles vous permettent de traiter efficacement des volumes importants d’informations structurées.

**Points clés à retenir :**

- Les listes de dictionnaires modélisent naturellement des ensembles d’entités
- Les list comprehensions offrent une syntaxe élégante pour le filtrage et la transformation
- Choisissez l’algorithme de recherche adapté à vos données (linéaire, binaire, index)
- L’indexation améliore drastiquement les performances pour les recherches fréquentes
- Le tri multi-critères permet des classements complexes et pertinents

Maîtriser ces concepts vous ouvre la porte à l’analyse de données, au développement d’API, et à la manipulation de fichiers JSON complexes. Continuez à pratiquer avec des cas d’usage réels pour affiner votre expertise !🚀​​​​​​​​​​​​​