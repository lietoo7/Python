# Les Dictionnaires en python:

## Introduction

Dans le chapitre précédent, nous avons exploré les listes Python, ces collections ordonnées qui fonctionnent comme des étagères numérotées. Aujourd’hui, nous franchissons une nouvelle étape dans la maîtrise des structures de données avec les **dictionnaires**, véritables piliers de la programmation Python moderne.

Si les listes excellent pour stocker des séquences d’éléments accessibles par position, les dictionnaires brillent par leur capacité à associer des données de manière logique et intuitive. Imaginez une armoire à tiroirs où chaque compartiment porte une étiquette descriptive : c’est exactement ce que permet un dictionnaire.

Ce cours vous guidera à travers tous les aspects des dictionnaires Python, des fondamentaux aux techniques avancées utilisées par les développeurs professionnels. Que vous construisiez une application web, analysiez des données ou développiez un jeu vidéo, la maîtrise des dictionnaires s’avérera indispensable.

-----

## Chapitre 1 : Fondements des Dictionnaires

### 1.1 Qu’est-ce qu’un dictionnaire ?

Un dictionnaire Python est une **structure de données associative** qui stocke des informations sous forme de paires **clé-valeur**. Contrairement aux listes qui utilisent des indices numériques séquentiels (0, 1, 2…), les dictionnaires permettent d’accéder aux données via des clés personnalisées et significatives.

**Analogie du monde réel :**

Pensez à un véritable dictionnaire linguistique :

- **Clé** : Le mot que vous recherchez (par exemple, “Python”)
- **Valeur** : La définition correspondante (“Langage de programmation de haut niveau…”)

De la même manière, un dictionnaire Python associe des clés uniques à des valeurs qui peuvent être de n’importe quel type.

### 1.2 Pourquoi les dictionnaires ?

**Problème avec les listes :**

Imaginons que vous souhaitiez stocker les notes d’étudiants :

```python
# Avec des listes (problématique)
noms = ["Alice", "Bob", "Charlie"]
notes = [15, 18, 12]

# Pour trouver la note de Bob, il faut :
# 1. Trouver l'index de "Bob" dans la liste des noms
# 2. Utiliser cet index pour accéder à la note correspondante
index_bob = noms.index("Bob")
note_bob = notes[index_bob]  # Fastidieux et source d'erreurs
```

**Solution avec un dictionnaire :**

```python
# Avec un dictionnaire (élégant)
notes = {
    "Alice": 15,
    "Bob": 18,
    "Charlie": 12
}

# Accès direct et intuitif
note_bob = notes["Bob"]  # 18
```

**Avantages clés des dictionnaires :**

1. **Lisibilité** : Le code s’auto-documente grâce aux clés descriptives
1. **Performance** : Recherche en temps constant O(1) en moyenne
1. **Flexibilité** : Les valeurs peuvent être de n’importe quel type
1. **Expressivité** : Modélise naturellement des données du monde réel

### 1.3 Création de dictionnaires

Python offre plusieurs syntaxes pour créer des dictionnaires :

#### Méthode 1 : Syntaxe littérale avec accolades `{}`

```python
# Dictionnaire vide
dico_vide = {}

# Dictionnaire avec des paires clé-valeur
personne = {
    "nom": "Dupont",
    "prenom": "Marie",
    "age": 28,
    "ville": "Lyon"
}

# Dictionnaire avec différents types de valeurs
donnees_mixtes = {
    "texte": "Bonjour",
    "nombre": 42,
    "decimal": 3.14,
    "booleen": True,
    "liste": [1, 2, 3],
    "tuple": (4, 5, 6),
    "aucune": None
}
```

#### Méthode 2 : Constructeur `dict()`

```python
# Dictionnaire vide
dico_vide = dict()

# Avec des arguments nommés
utilisateur = dict(nom="Alice", age=25, ville="Paris")

# À partir d'une liste de tuples
paires = [("a", 1), ("b", 2), ("c", 3)]
dico_depuis_liste = dict(paires)
# Résultat : {'a': 1, 'b': 2, 'c': 3}
```

#### Méthode 3 : Compréhension de dictionnaire

```python
# Créer un dictionnaire des carrés
carres = {x: x**2 for x in range(1, 6)}
# Résultat : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Avec condition
pairs_carres = {x: x**2 for x in range(10) if x % 2 == 0}
# Résultat : {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

#### Méthode 4 : Fonction `dict.fromkeys()`

```python
# Initialiser plusieurs clés avec la même valeur
cles = ["a", "b", "c"]
dico_initial = dict.fromkeys(cles, 0)
# Résultat : {'a': 0, 'b': 0, 'c': 0}

# Valeur par défaut = None si non spécifiée
vide = dict.fromkeys(["x", "y", "z"])
# Résultat : {'x': None, 'y': None, 'z': None}
```

### 1.4 Les clés : Règles et contraintes

**Règles fondamentales pour les clés :**

1. **Unicité** : Chaque clé doit être unique dans un dictionnaire

```python
# Les doublons écrasent les valeurs précédentes
dico = {"a": 1, "b": 2, "a": 3}
print(dico)  # {'a': 3, 'b': 2} - Le premier "a" est écrasé
```

1. **Immuabilité** : Les clés doivent être de types immuables

```python
# VALIDE - Types immuables
dico_valide = {
    "texte": "ok",           # str
    42: "nombre",            # int
    3.14: "pi",              # float
    (1, 2): "tuple",         # tuple
    True: "booleen"          # bool
}

# INVALIDE - Types mutables
try:
    dico_invalide = {
        [1, 2]: "liste"      # TypeError: unhashable type: 'list'
    }
except TypeError as e:
    print(f"Erreur : {e}")

try:
    dico_invalide = {
        {"a": 1}: "dict"     # TypeError: unhashable type: 'dict'
    }
except TypeError as e:
    print(f"Erreur : {e}")
```

**Pourquoi cette contrainte ?**

Python utilise une technique appelée **hachage** pour stocker et retrouver rapidement les valeurs. Seuls les objets immuables peuvent être hachés de manière fiable, garantissant ainsi l’intégrité du dictionnaire.

1. **Les valeurs sont libres** : Aucune contrainte sur les valeurs

```python
# Les valeurs peuvent être de n'importe quel type
flexible = {
    "liste": [1, 2, 3],
    "dict": {"imbriqué": True},
    "fonction": len,
    "objet": object()
}
```

-----

## Chapitre 2 : Accès et Manipulation des Données

### 2.1 Accéder aux valeurs

#### Méthode 1 : Notation entre crochets `[]`

```python
utilisateur = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Accès direct
nom = utilisateur["nom"]        # "Alice"
age = utilisateur["age"]        # 25

# ATTENTION : Erreur si la clé n'existe pas
try:
    profession = utilisateur["profession"]
except KeyError as e:
    print(f"Clé inexistante : {e}")
```

#### Méthode 2 : La méthode `.get()` (recommandée)

La méthode `.get()` est plus sûre car elle ne lève pas d’erreur si la clé est absente.

```python
utilisateur = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Avec valeur par défaut
nom = utilisateur.get("nom")              # "Alice"
profession = utilisateur.get("profession") # None (pas d'erreur)

# Spécifier une valeur par défaut personnalisée
profession = utilisateur.get("profession", "Non renseignée")
# Résultat : "Non renseignée"

# Cas d'usage pratique
score = {"joueur1": 100, "joueur2": 85}
score_joueur3 = score.get("joueur3", 0)  # 0 si le joueur n'existe pas
```

**Quand utiliser `.get()` vs `[]` ?**

- **`[]`** : Quand vous êtes certain que la clé existe et voulez une erreur en cas d’absence
- **`.get()`** : Quand la clé peut être absente et vous voulez une valeur par défaut

### 2.2 Modifier et ajouter des éléments

#### Modification d’une valeur existante

```python
personne = {
    "nom": "Dupont",
    "age": 30,
    "ville": "Lyon"
}

# Modifier une valeur
personne["age"] = 31
personne["ville"] = "Paris"

print(personne)
# {'nom': 'Dupont', 'age': 31, 'ville': 'Paris'}
```

#### Ajout de nouvelles clés

```python
personne = {
    "nom": "Dupont",
    "age": 30
}

# Ajouter de nouvelles clés
personne["profession"] = "Développeur"
personne["email"] = "dupont@email.com"

print(personne)
# {'nom': 'Dupont', 'age': 30, 'profession': 'Développeur', 'email': 'dupont@email.com'}
```

#### Méthode `.setdefault()`

Ajoute une clé seulement si elle n’existe pas déjà.

```python
config = {"theme": "sombre"}

# Si "theme" existe, retourne sa valeur sans modification
theme = config.setdefault("theme", "clair")
print(theme)  # "sombre" (valeur existante conservée)

# Si "langue" n'existe pas, l'ajoute avec la valeur par défaut
langue = config.setdefault("langue", "fr")
print(langue)  # "fr"
print(config)  # {'theme': 'sombre', 'langue': 'fr'}
```

#### Méthode `.update()`

Fusionne un dictionnaire avec un autre ou ajoute plusieurs clés-valeurs.

```python
utilisateur = {
    "nom": "Alice",
    "age": 25
}

# Mise à jour avec un autre dictionnaire
nouvelles_infos = {
    "ville": "Paris",
    "profession": "Ingénieure"
}
utilisateur.update(nouvelles_infos)

print(utilisateur)
# {'nom': 'Alice', 'age': 25, 'ville': 'Paris', 'profession': 'Ingénieure'}

# Mise à jour avec des arguments nommés
utilisateur.update(age=26, email="alice@email.com")
print(utilisateur)
# {'nom': 'Alice', 'age': 26, 'ville': 'Paris', 'profession': 'Ingénieure', 'email': 'alice@email.com'}

# Mise à jour avec une liste de tuples
utilisateur.update([("telephone", "0612345678"), ("code_postal", "75001")])
```

### 2.3 Supprimer des éléments

#### Méthode 1 : Instruction `del`

```python
personne = {
    "nom": "Martin",
    "age": 35,
    "ville": "Marseille",
    "profession": "Médecin"
}

# Supprimer une clé spécifique
del personne["profession"]
print(personne)
# {'nom': 'Martin', 'age': 35, 'ville': 'Marseille'}

# Erreur si la clé n'existe pas
try:
    del personne["email"]
except KeyError as e:
    print(f"Impossible de supprimer : {e}")
```

#### Méthode 2 : `.pop()`

Supprime et **retourne** la valeur associée à une clé.

```python
personne = {
    "nom": "Martin",
    "age": 35,
    "ville": "Marseille"
}

# Supprimer et récupérer la valeur
age = personne.pop("age")
print(f"Âge supprimé : {age}")  # 35
print(personne)  # {'nom': 'Martin', 'ville': 'Marseille'}

# Avec valeur par défaut (pas d'erreur si inexistant)
profession = personne.pop("profession", "Non renseignée")
print(profession)  # "Non renseignée"
```

#### Méthode 3 : `.popitem()`

Supprime et retourne la **dernière** paire clé-valeur (depuis Python 3.7+, les dicts sont ordonnés).

```python
config = {
    "theme": "sombre",
    "langue": "fr",
    "notifications": True
}

# Supprimer le dernier élément
dernier = config.popitem()
print(dernier)  # ('notifications', True)
print(config)   # {'theme': 'sombre', 'langue': 'fr'}
```

#### Méthode 4 : `.clear()`

Vide complètement le dictionnaire.

```python
data = {"a": 1, "b": 2, "c": 3}
data.clear()
print(data)  # {}
```

-----

## Chapitre 3 : Méthodes Essentielles des Dictionnaires

### 3.1 Méthodes d’accès aux composants

Les dictionnaires offrent trois méthodes fondamentales pour accéder séparément aux clés, valeurs, ou paires clé-valeur.

#### `.keys()` - Récupérer toutes les clés

```python
produits = {
    "pomme": 2.5,
    "banane": 1.8,
    "orange": 3.0
}

# Récupérer les clés
cles = produits.keys()
print(cles)  # dict_keys(['pomme', 'banane', 'orange'])

# Conversion en liste
liste_cles = list(produits.keys())
print(liste_cles)  # ['pomme', 'banane', 'orange']

# Vérification d'existence
if "pomme" in produits.keys():
    print("La pomme est disponible")
```

#### `.values()` - Récupérer toutes les valeurs

```python
produits = {
    "pomme": 2.5,
    "banane": 1.8,
    "orange": 3.0
}

# Récupérer les valeurs
valeurs = produits.values()
print(valeurs)  # dict_values([2.5, 1.8, 3.0])

# Conversion en liste
liste_valeurs = list(produits.values())

# Opérations sur les valeurs
prix_total = sum(produits.values())
prix_moyen = prix_total / len(produits)
print(f"Prix moyen : {prix_moyen:.2f}€")  # 2.43€

# Trouver le prix maximum
prix_max = max(produits.values())
print(f"Prix maximum : {prix_max}€")  # 3.0€
```

#### `.items()` - Récupérer les paires clé-valeur

```python
produits = {
    "pomme": 2.5,
    "banane": 1.8,
    "orange": 3.0
}

# Récupérer les paires
items = produits.items()
print(items)
# dict_items([('pomme', 2.5), ('banane', 1.8), ('orange', 3.0)])

# Conversion en liste de tuples
liste_items = list(produits.items())
print(liste_items)
# [('pomme', 2.5), ('banane', 1.8), ('orange', 3.0)]
```

### 3.2 Vérification d’existence : `in` et `not in`

```python
utilisateur = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

# Vérifier l'existence d'une clé
if "nom" in utilisateur:
    print(f"Nom : {utilisateur['nom']}")

# Vérifier l'absence
if "profession" not in utilisateur:
    print("Profession non renseignée")
    utilisateur["profession"] = "Développeuse"

# Par défaut, 'in' vérifie les clés
# Pour vérifier les valeurs :
if "Paris" in utilisateur.values():
    print("Un utilisateur habite à Paris")

# Vérifier une paire clé-valeur
if ("age", 25) in utilisateur.items():
    print("L'utilisateur a 25 ans")
```

### 3.3 Copie de dictionnaires

#### Problème : Copie par référence

```python
# PIÈGE : Assignation simple = référence
original = {"a": 1, "b": 2}
copie = original  # Pas une vraie copie !

copie["a"] = 999
print(original)  # {'a': 999, 'b': 2} - Modifié aussi !
```

#### Solution 1 : `.copy()` (copie superficielle)

```python
original = {"a": 1, "b": 2}
copie = original.copy()

copie["a"] = 999
print(original)  # {'a': 1, 'b': 2} - Non affecté ✓
print(copie)     # {'a': 999, 'b': 2}
```

#### Limitation : Dictionnaires imbriqués

```python
# Attention avec les structures imbriquées
original = {
    "nom": "Alice",
    "scores": [10, 20, 30]
}

copie = original.copy()
copie["scores"].append(40)

print(original)  # {'nom': 'Alice', 'scores': [10, 20, 30, 40]}
# La liste est modifiée dans l'original aussi !
```

#### Solution 2 : `copy.deepcopy()` (copie profonde)

```python
import copy

original = {
    "nom": "Alice",
    "scores": [10, 20, 30],
    "config": {"theme": "sombre"}
}

copie_profonde = copy.deepcopy(original)
copie_profonde["scores"].append(40)
copie_profonde["config"]["theme"] = "clair"

print(original["scores"])  # [10, 20, 30] - Non affecté ✓
print(original["config"])  # {'theme': 'sombre'} - Non affecté ✓
```

### 3.4 Longueur et vérification de vide

```python
produits = {"pomme": 2.5, "banane": 1.8}

# Nombre de paires clé-valeur
nombre = len(produits)
print(f"Nombre de produits : {nombre}")  # 2

# Vérifier si vide
panier = {}
if not panier:  # Dictionnaire vide = False
    print("Le panier est vide")

# Méthode alternative
if len(panier) == 0:
    print("Le panier est vide")
```

-----

## Chapitre 4 : Parcours et Itération

### 4.1 Parcours des clés (par défaut)

```python
notes = {"Alice": 15, "Bob": 18, "Charlie": 12}

# Parcours simple (par défaut : les clés)
for etudiant in notes:
    print(etudiant)
# Affiche : Alice, Bob, Charlie

# Accès aux valeurs via les clés
for etudiant in notes:
    print(f"{etudiant} a obtenu {notes[etudiant]}/20")
```

### 4.2 Parcours des valeurs

```python
notes = {"Alice": 15, "Bob": 18, "Charlie": 12}

# Parcourir uniquement les valeurs
for note in notes.values():
    print(f"Note : {note}")

# Calculer la moyenne
total = sum(notes.values())
moyenne = total / len(notes)
print(f"Moyenne de la classe : {moyenne:.1f}/20")
```

### 4.3 Parcours des paires clé-valeur

C’est la méthode la plus courante et la plus pythonique.

```python
notes = {"Alice": 15, "Bob": 18, "Charlie": 12}

# Parcours avec .items()
for etudiant, note in notes.items():
    print(f"{etudiant} : {note}/20")

# Avec logique conditionnelle
for etudiant, note in notes.items():
    if note >= 16:
        mention = "Très bien"
    elif note >= 14:
        mention = "Bien"
    elif note >= 12:
        mention = "Assez bien"
    else:
        mention = "Passable"
    
    print(f"{etudiant} : {mention}")
```

### 4.4 Compréhension de dictionnaire

Les compréhensions de dictionnaires permettent de créer ou transformer des dictionnaires de manière concise.

#### Syntaxe de base

```python
# {clé_expression: valeur_expression for item in iterable}

# Créer un dictionnaire des carrés
carres = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Inverser clés et valeurs
original = {"a": 1, "b": 2, "c": 3}
inverse = {valeur: cle for cle, valeur in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

#### Avec conditions

```python
# Notes supérieures à 14
notes = {"Alice": 15, "Bob": 18, "Charlie": 12, "Diana": 16}
mentions = {nom: note for nom, note in notes.items() if note >= 14}
# {'Alice': 15, 'Bob': 18, 'Diana': 16}

# Transformation conditionnelle
notes_lettres = {
    nom: 'A' if note >= 16 else 'B' if note >= 14 else 'C'
    for nom, note in notes.items()
}
# {'Alice': 'B', 'Bob': 'A', 'Charlie': 'C', 'Diana': 'A'}
```

#### Création depuis deux listes

```python
noms = ["Alice", "Bob", "Charlie"]
notes = [15, 18, 12]

# Combiner avec zip()
dictionnaire_notes = {nom: note for nom, note in zip(noms, notes)}
# {'Alice': 15, 'Bob': 18, 'Charlie': 12}
```

### 4.5 Parcours avec énumération

```python
produits = {"pomme": 2.5, "banane": 1.8, "orange": 3.0}

# Avec numérotation
for index, (nom, prix) in enumerate(produits.items(), start=1):
    print(f"{index}. {nom.capitalize()} : {prix}€")

# Sortie :
# 1. Pomme : 2.5€
# 2. Banane : 1.8€
# 3. Orange : 3.0€
```

-----

## Chapitre 5 : Dictionnaires Imbriqués et Structures Complexes

### 5.1 Dictionnaires contenant des listes

```python
# Emploi du temps
emploi_du_temps = {
    "lundi": ["Mathématiques", "Français", "Sport"],
    "mardi": ["Anglais", "Physique", "Histoire"],
    "mercredi": ["Informatique", "Chimie"]
}

# Accès aux données
cours_lundi = emploi_du_temps["lundi"]
print(cours_lundi)  # ['Mathématiques', 'Français', 'Sport']

# Accès à un cours spécifique
premier_cours_lundi = emploi_du_temps["lundi"][0]
print(premier_cours_lundi)  # "Mathématiques"

# Ajouter un cours
emploi_du_temps["lundi"].append("Musique")

# Parcourir
for jour, cours_list in emploi_du_temps.items():
    print(f"\n{jour.upper()} :")
    for i, cours in enumerate(cours_list, 1):
        print(f"  {i}. {cours}")
```

### 5.2 Dictionnaires imbriqués

Les dictionnaires imbriqués permettent de représenter des données hiérarchiques complexes.

```python
# Base de données d'utilisateurs
utilisateurs = {
    "user001": {
        "nom": "Dupont",
        "prenom": "Marie",
        "age": 28,
        "contact": {
            "email": "marie.dupont@email.com",
            "telephone": "0612345678"
        },
        "preferences": {
            "theme": "sombre",
            "langue": "fr",
            "notifications": True
        }
    },
    "user002": {
        "nom": "Martin",
        "prenom": "Jean",
        "age": 35,
        "contact": {
            "email": "jean.martin@email.com",
            "telephone": "0623456789"
        },
        "preferences": {
            "theme": "clair",
            "langue": "en",
            "notifications": False
        }
    }
}

# Accès aux données imbriquées
email_marie = utilisateurs["user001"]["contact"]["email"]
print(email_marie)  # "marie.dupont@email.com"

theme_jean = utilisateurs["user002"]["preferences"]["theme"]
print(theme_jean)  # "clair"

# Modification de données imbriquées
utilisateurs["user001"]["age"] = 29
utilisateurs["user001"]["preferences"]["theme"] = "clair"

# Parcours de structures imbriquées
for user_id, infos in utilisateurs.items():
    print(f"\n{user_id} :")
    print(f"  Nom complet : {infos['prenom']} {infos['nom']}")
    print(f"  Âge : {infos['age']} ans")
    print(f"  Email : {infos['contact']['email']}")
    print(f"  Thème : {infos['preferences']['theme']}")
```

### 5.3 Accès sécurisé aux données imbriquées

```python
# Méthode 1 : get() en chaîne
utilisateurs = {
    "user001": {
        "nom": "Dupont",
        "contact": {
            "email": "marie@email.com"
        }
    }
}

# Accès sécurisé niveau par niveau
contact = utilisateurs.get("user001", {}).get("contact", {})
email = contact.get("email", "Non renseigné")

# Méthode 2 : Gestion d'exceptions
try:
    telephone = utilisateurs["user001"]["contact"]["telephone"]
except KeyError:
    telephone = "Non renseigné"

# Méthode 3 : Fonction helper personnalisée
def get_nested(dico, *cles, defaut=None):
    """
    Récupère une valeur imbriquée en toute sécurité.
    
    Args:
        dico: Le dictionnaire à explorer
        *cles: Séquence de clés à suivre
        defaut: Valeur par défaut si le chemin n'existe pas
    
    Returns:
        La valeur trouvée ou la valeur par défaut
    """
    for cle in cles:
        if isinstance(dico, dict):
            dico = dico.get(cle, defaut)
        else:
            return defaut
    return dico

# Utilisation
email = get_nested(utilisateurs, "user001", "contact", "email", defaut="N/A")
telephone = get_nested(utilisateurs, "user001", "contact", "telephone", defaut="N/A")
```

### 5.4 Listes de dictionnaires

Structure très courante pour représenter des collections d’objets.

```python
# Liste de produits (comme une table de base de données)
produits = [
    {
        "id": 1,
        "nom": "Ordinateur portable",
        "prix": 899.99,
        "categorie": "Informatique",
        "stock": 15
    },
    {
        "id": 2,
        "nom": "Souris sans fil",
        "prix": 29.99,
        "categorie": "Informatique",
        "stock": 50
    },
    {
        "id": 3,
        "nom": "Clavier mécanique",
        "prix": 129.99,
        "categorie": "Informatique",
        "stock": 8
    }
]

# Affichage formaté
for produit in produits:
    print(f"{produit['nom']} - {produit['prix']}€ (Stock : {produit['stock']})")

# Filtrage
produits_en_stock = [p for p in produits if p['stock'] > 10]

# Recherche
def trouver_produit(produits, id_recherche):
    for produit in produits:
        if produit['id'] == id_recherche:
            return produit
    return None

produit_2 = trouver_produit(produits, 2)
print(produit_2['nom'])  # "Souris sans fil"

# Tri par prix
produits_tries = sorted(produits, key=lambda p: p['prix'])

# Calcul du prix total du stock
valeur_totale = sum(p['prix'] * p['stock'] for p in produits)
print(f"Valeur totale du stock : {valeur_totale:.2​​​​​​​​​​​​​​​​
```
f}€”)

```
---

## Chapitre 6 : Techniques Avancées

### 6.1 Fusion de dictionnaires

#### Méthode 1 : Opérateur `|` (Python 3.9+)

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Fusion avec |
fusion = dict1 | dict2
print(fusion)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Mise à jour en place avec |=
dict1 |= dict2
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# En cas de conflit, le second dictionnaire l'emporte
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 999, "c": 3}
fusion = dict1 | dict2
print(fusion)  # {'a': 1, 'b': 999, 'c': 3}
```

#### Méthode 2 : Opérateur `**` (unpacking)

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

fusion = {**dict1, **dict2}
print(fusion)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Avec valeurs surchargées
fusion = {**dict1, **dict2, "e": 5}
print(fusion)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

#### Méthode 3 : `.update()`

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### 6.2 Comptage avec dictionnaires

```python
# Compter les occurrences de lettres
texte = "bonjour le monde"

# Méthode manuelle
compteur = {}
for lettre in texte:
    if lettre != " ":
        compteur[lettre] = compteur.get(lettre, 0) + 1

print(compteur)
# {'b': 1, 'o': 3, 'n': 2, 'j': 1, 'u': 1, 'r': 1, 'l': 1, 'e': 2, 'm': 1, 'd': 1}

# Méthode avec Counter (module collections)
from collections import Counter

compteur = Counter(texte.replace(" ", ""))
print(compteur)
# Counter({'o': 3, 'n': 2, 'e': 2, 'b': 1, 'j': 1, 'u': 1, 'r': 1, 'l': 1, 'm': 1, 'd': 1})

# Méthode la plus commune
print(compteur.most_common(3))  # [('o', 3), ('n', 2), ('e', 2)]
```

### 6.3 Dictionnaires avec valeurs par défaut : `defaultdict`

```python
from collections import defaultdict

# Grouper des étudiants par niveau
etudiants = [
    {"nom": "Alice", "niveau": "L1"},
    {"nom": "Bob", "niveau": "L2"},
    {"nom": "Charlie", "niveau": "L1"},
    {"nom": "Diana", "niveau": "L3"},
    {"nom": "Eve", "niveau": "L2"}
]

# Avec defaultdict
groupes = defaultdict(list)  # Valeur par défaut = liste vide

for etudiant in etudiants:
    groupes[etudiant["niveau"]].append(etudiant["nom"])

print(dict(groupes))
# {'L1': ['Alice', 'Charlie'], 'L2': ['Bob', 'Eve'], 'L3': ['Diana']}

# Équivalent sans defaultdict (plus verbeux)
groupes_manuel = {}
for etudiant in etudiants:
    niveau = etudiant["niveau"]
    if niveau not in groupes_manuel:
        groupes_manuel[niveau] = []
    groupes_manuel[niveau].append(etudiant["nom"])
```

### 6.4 Dictionnaires ordonnés : `OrderedDict`

Depuis Python 3.7, les dictionnaires standard conservent l’ordre d’insertion. Cependant, `OrderedDict` offre des fonctionnalités supplémentaires.

```python
from collections import OrderedDict

# Créer un OrderedDict
od = OrderedDict()
od["z"] = 1
od["y"] = 2
od["x"] = 3

print(od)  # OrderedDict([('z', 1), ('y', 2), ('x', 3)])

# Déplacer un élément à la fin
od.move_to_end("z")
print(od)  # OrderedDict([('y', 2), ('x', 3), ('z', 1)])

# Déplacer au début
od.move_to_end("x", last=False)
print(od)  # OrderedDict([('x', 3), ('y', 2), ('z', 1)])

# popitem() avec ordre LIFO
dernier = od.popitem(last=True)
premier = od.popitem(last=False)
```

### 6.5 Tri de dictionnaires

```python
produits = {
    "pomme": 2.5,
    "banane": 1.8,
    "orange": 3.0,
    "kiwi": 4.5
}

# Tri par clés (alphabétique)
produits_tries_cles = dict(sorted(produits.items()))
print(produits_tries_cles)
# {'banane': 1.8, 'kiwi': 4.5, 'orange': 3.0, 'pomme': 2.5}

# Tri par valeurs (prix croissant)
produits_tries_prix = dict(sorted(produits.items(), key=lambda item: item[1]))
print(produits_tries_prix)
# {'banane': 1.8, 'pomme': 2.5, 'orange': 3.0, 'kiwi': 4.5}

# Tri décroissant par valeurs
produits_tries_desc = dict(sorted(produits.items(), key=lambda item: item[1], reverse=True))
print(produits_tries_desc)
# {'kiwi': 4.5, 'orange': 3.0, 'pomme': 2.5, 'banane': 1.8}

# Tri complexe (par longueur du nom puis alphabétique)
produits_tries_complexe = dict(sorted(produits.items(), key=lambda item: (len(item[0]), item[0])))
```

### 6.6 Inversion de dictionnaires

```python
original = {"a": 1, "b": 2, "c": 3}

# Inversion simple
inverse = {valeur: cle for cle, valeur in original.items()}
print(inverse)  # {1: 'a', 2: 'b', 3: 'c'}

# ⚠️ Attention aux doublons de valeurs
problematique = {"a": 1, "b": 2, "c": 1}
inverse_probleme = {v: k for k, v in problematique.items()}
print(inverse_probleme)  # {1: 'c', 2: 'b'} - 'a' est perdu !

# Solution : grouper les clés avec des valeurs identiques
from collections import defaultdict

inverse_complet = defaultdict(list)
for cle, valeur in problematique.items():
    inverse_complet[valeur].append(cle)

print(dict(inverse_complet))  # {1: ['a', 'c'], 2: ['b']}
```

-----

## Chapitre 7 : Cas d’Usage Pratiques

### 7.1 Configuration d’application

```python
# Fichier de configuration
config = {
    "application": {
        "nom": "MonApp",
        "version": "1.2.3",
        "environnement": "production"
    },
    "base_de_donnees": {
        "hote": "localhost",
        "port": 5432,
        "nom": "ma_base",
        "utilisateur": "admin"
    },
    "serveur": {
        "hote": "0.0.0.0",
        "port": 8000,
        "debug": False
    },
    "logs": {
        "niveau": "INFO",
        "fichier": "/var/log/monapp.log"
    }
}

# Utilisation
print(f"Démarrage de {config['application']['nom']} v{config['application']['version']}")
print(f"Serveur sur {config['serveur']['hote']}:{config['serveur']['port']}")
```

### 7.2 Cache de données

```python
# Cache simple
cache = {}

def calculer_factorielle(n):
    """Calcul avec mise en cache."""
    if n in cache:
        print(f"Récupération depuis le cache pour n={n}")
        return cache[n]
    
    print(f"Calcul pour n={n}")
    if n == 0 or n == 1:
        resultat = 1
    else:
        resultat = n * calculer_factorielle(n - 1)
    
    cache[n] = resultat
    return resultat

# Utilisation
print(calculer_factorielle(5))  # Calcul complet
print(calculer_factorielle(5))  # Depuis le cache
print(calculer_factorielle(7))  # Utilise le cache partiel
```

### 7.3 Transformation de données JSON

```python
import json

# Données JSON (typiquement reçues d'une API)
json_data = '''
{
    "utilisateurs": [
        {"id": 1, "nom": "Alice", "age": 25},
        {"id": 2, "nom": "Bob", "age": 30}
    ],
    "statut": "success"
}
'''

# Conversion JSON → dictionnaire Python
data = json.loads(json_data)

# Manipulation
for utilisateur in data["utilisateurs"]:
    utilisateur["age_futur"] = utilisateur["age"] + 10

# Conversion dictionnaire → JSON
json_modifie = json.dumps(data, indent=2, ensure_ascii=False)
print(json_modifie)
```

### 7.4 Validation de formulaires

```python
def valider_formulaire(formulaire):
    """
    Valide un formulaire et retourne les erreurs.
    
    Returns:
        dict: Dictionnaire des erreurs (vide si valide)
    """
    erreurs = {}
    
    # Champ obligatoire
    if not formulaire.get("nom"):
        erreurs["nom"] = "Le nom est obligatoire"
    
    # Validation d'email
    email = formulaire.get("email", "")
    if not email:
        erreurs["email"] = "L'email est obligatoire"
    elif "@" not in email or "." not in email:
        erreurs["email"] = "Format d'email invalide"
    
    # Validation d'âge
    age = formulaire.get("age")
    if age is None:
        erreurs["age"] = "L'âge est obligatoire"
    elif not isinstance(age, int) or age < 18:
        erreurs["age"] = "Vous devez avoir au moins 18 ans"
    
    # Validation du mot de passe
    mdp = formulaire.get("mot_de_passe", "")
    if len(mdp) < 8:
        erreurs["mot_de_passe"] = "Le mot de passe doit contenir au moins 8 caractères"
    
    return erreurs

# Utilisation
formulaire_utilisateur = {
    "nom": "Alice",
    "email": "alice@email.com",
    "age": 25,
    "mot_de_passe": "secret123"
}

erreurs = valider_formulaire(formulaire_utilisateur)

if erreurs:
    print("Formulaire invalide :")
    for champ, message in erreurs.items():
        print(f"  - {champ} : {message}")
else:
    print("Formulaire valide !")
```

### 7.5 Agrégation de données

```python
# Ventes par produit et par mois
ventes = [
    {"produit": "Laptop", "mois": "Jan", "montant": 1200},
    {"produit": "Mouse", "mois": "Jan", "montant": 30},
    {"produit": "Laptop", "mois": "Feb", "montant": 1400},
    {"produit": "Keyboard", "mois": "Jan", "montant": 100},
    {"produit": "Mouse", "mois": "Feb", "montant": 25},
]

# Agrégation par produit
from collections import defaultdict

total_par_produit = defaultdict(float)
ventes_par_produit = defaultdict(int)

for vente in ventes:
    produit = vente["produit"]
    total_par_produit[produit] += vente["montant"]
    ventes_par_produit[produit] += 1

# Affichage
print("Statistiques par produit :")
for produit in total_par_produit:
    total = total_par_produit[produit]
    nb_ventes = ventes_par_produit[produit]
    moyenne = total / nb_ventes
    print(f"{produit:10} - Total : {total:7.2f}€ - Ventes : {nb_ventes} - Moyenne : {moyenne:.2f}€")
```

-----

## Chapitre 8 : Bonnes Pratiques et Pièges à Éviter

### 8.1 Bonnes pratiques

#### 1. Noms de clés cohérents

```python
# BON : Cohérence dans le nommage
utilisateur = {
    "nom": "Dupont",
    "prenom": "Marie",
    "age": 28,
    "email": "marie@email.com"
}

# MAUVAIS : Incohérence
utilisateur_mauvais = {
    "nom": "Dupont",
    "firstName": "Marie",  # Mélange français/anglais
    "Age": 28,             # Majuscule incohérente
    "e-mail": "marie@email.com"  # Tiret vs underscore
}
```

#### 2. Utiliser `.get()` pour éviter les erreurs

```python
# BON : Sécurisé
config = {"theme": "sombre"}
langue = config.get("langue", "fr")  # Pas d'erreur

# RISQUÉ : Peut lever KeyError
try:
    langue = config["langue"]
except KeyError:
    langue = "fr"
```

#### 3. Validation des clés avant accès profond

```python
# BON : Vérification progressive
data = {"user": {"contact": {"email": "test@email.com"}}}

if "user" in data and "contact" in data["user"]:
    email = data["user"]["contact"].get("email", "N/A")
```

#### 4. Immutabilité des clés

```python
# BON : Types immuables
config = {
    "option1": True,
    42: "answer",
    (1, 2): "tuple_key"
}

# MAUVAIS : Types mutables
try:
    mauvais = {
        [1, 2]: "liste"  # TypeError
    }
except TypeError:
    pass
```

### 8.2 Pièges courants

#### Piège 1 : Modification pendant l’itération

```python
# DANGEREUX : Modification pendant le parcours
scores = {"Alice": 10, "Bob": 15, "Charlie": 8}

# ERREUR potentielle
for nom in scores:
    if scores[nom] < 10:
        del scores[nom]  # RuntimeError: dictionary changed size during iteration

# SOLUTION : Copier les clés
for nom in list(scores.keys()):
    if scores[nom] < 10:
        del scores[nom]

# MEILLEURE SOLUTION : Compréhension de dictionnaire
scores = {nom: score for nom, score in scores.items() if score >= 10}
```

#### Piège 2 : Valeurs mutables par défaut

```python
#  DANGEREUX
def ajouter_tache(tache, liste_taches={}):
    liste_taches[tache] = True
    return liste_taches

# Comportement surprenant
print(ajouter_tache("Tâche 1"))  # {'Tâche 1': True}
print(ajouter_tache("Tâche 2"))  # {'Tâche 1': True, 'Tâche 2': True} - Pas {'Tâche 2': True} !

#  CORRECT
def ajouter_tache(tache, liste_taches=None):
    if liste_taches is None:
        liste_taches = {}
    liste_taches[tache] = True
    return liste_taches
```

#### Piège 3 : Copie superficielle vs profonde

```python
#  ATTENTION : Problème avec structures imbriquées
original = {
    "nom": "Alice",
    "scores": [10, 20, 30]
}

copie = original.copy()  # Copie superficielle
copie["scores"].append(40)

print(original["scores"])  # [10, 20, 30, 40] - Modifié !

#  SOLUTION : Copie profonde
import copy

copie_profonde = copy.deepcopy(original)
copie_profonde["scores"].append(50)
print(original["scores"])  # [10, 20, 30, 40] - Non affecté
```

#### Piège 4 : Clés avec valeurs `None` vs clés absentes

```python
config = {"option1": None, "option2": "valeur"}

# Différence importante
print("option1" in config)  # True - La clé existe
print("option3" in config)  # False - La clé n'existe pas

# .get() retourne None dans les deux cas !
print(config.get("option1"))  # None (clé existe)
print(config.get("option3"))  # None (clé absente)

# Solution : Utiliser un sentinel
ABSENT = object()
valeur = config.get("option3", ABSENT)
if valeur is ABSENT:
    print("Clé vraiment absente")
```

-----

## Chapitre 9 : Exercices Pratiques

### Exercice 1 : Gestion de stocks

Créez un système de gestion de stocks avec les fonctionnalités suivantes :

- Ajouter un produit
- Mettre à jour la quantité
- Afficher le stock
- Calculer la valeur totale du stock

```python
def gerer_stock():
    stock = {}
    
    while True:
        print("\n1. Ajouter produit")
        print("2. Mettre à jour quantité")
        print("3. Afficher stock")
        print("4. Valeur totale")
        print("5. Quitter")
        
        choix = input("\nChoix : ")
        
        # À compléter...

# Solution
def gerer_stock_solution():
    stock = {}
    
    while True:
        print("\n" + "=" * 40)
        print("GESTION DE STOCK")
        print("=" * 40)
        print("1. Ajouter produit")
        print("2. Mettre à jour quantité")
        print("3. Afficher stock")
        print("4. Valeur totale")
        print("5. Quitter")
        
        choix = input("\nChoix : ").strip()
        
        if choix == "1":
            nom = input("Nom du produit : ").strip()
            prix = float(input("Prix unitaire : "))
            quantite = int(input("Quantité : "))
            
            stock[nom] = {"prix": prix, "quantite": quantite}
            print(f" {nom} ajouté au stock")
        
        elif choix == "2":
            nom = input("Nom du produit : ").strip()
            if nom in stock:
                quantite = int(input("Nouvelle quantité : "))
                stock[nom]["quantite"] = quantite
                print(f" Quantité mise à jour")
            else:
                print(f"Produit '{nom}' introuvable")
        
        elif choix == "3":
            if not stock:
                print("Stock vide")
            else:
                print("\nSTOCK ACTUEL :")
                for nom, infos in stock.items():
                    print(f"{nom:20} - {infos['quantite']:3} unités à {infos['prix']:.2f}€")
        
        elif choix == "4":
            total = sum(infos['prix'] * infos['quantite'] for infos in stock.values())
            print(f"\n Valeur totale du stock : {total:.2f}€")
        
        elif choix == "5":
            print("Au revoir !")
            break
```

### Exercice 2 : Analyse de fréquence de mots

Analysez un texte pour compter la fréquence des mots.

```python
def analyser_texte(texte):
    """
    Compte la fréquence des mots dans un texte.
    
    Returns:
        dict: Dictionnaire {mot: fréquence}
    """
    # À compléter...
    pass

# Solution
def analyser_texte_solution(texte):
    # Nettoyer et séparer les mots
    mots = texte.lower().replace(",", "").replace(".", "").split()
    
    # Compter les occurrences
    frequences = {}
    for mot in mots:
        frequences[mot] = frequences.get(mot, 0) + 1
    
    # Trier par fréquence décroissante
    mots_tries = sorted(frequences.items(), key=lambda x: x[1], reverse=True)
    
    return dict(mots_tries)

# Test
texte = "Python est un langage de programmation. Python est facile à apprendre."
resultat = analyser_texte_solution(texte)

print("Fréquence des mots :")
for mot, freq in resultat.items():
    print(f"{mot:15} : {freq}")
```

### Exercice 3 : Carnet d’adresses

Créez un carnet d’adresses avec recherche par nom.

```python
# Solution complète
def carnet_adresses():
    contacts = {}
    
    def ajouter_contact():
        nom = input("Nom : ").strip()
        telephone = input("Téléphone : ").strip()
        email = input("Email : ").strip()
        
        contacts[nom] = {
            "telephone": telephone,
            "email": email
        }
        print(f"{nom} ajouté")
    
    def rechercher_contact():
        nom = input("Nom à rechercher : ").strip()
        
        if nom in contacts:
            infos = contacts[nom]
            print(f"\n{nom}")
            print(f"  {infos['telephone']}")
            print(f"  {infos['email']}")
        else:
            print(f"{nom} introuvable")
    
    def afficher_tous():
        if not contacts:
            print("Aucun contact")
        else:
            print("\nTOUS LES CONTACTS :")
            for nom, infos in sorted(contacts.items()):
                print(f"\n{nom}")
                print(f"  {infos['telephone']}")
                print(f"  {infos['email']}")
    
    while True:
        print("\n" + "=" * 40)
        print("1. Ajouter contact")
        print("2. Rechercher contact")
        print("3. Afficher tous")
        print("4. Quitter")
        
        choix = input("\nChoix : ").strip()
        
        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            rechercher_contact()
        elif choix == "3":
            afficher_tous()
        elif choix == "4":
            break
```

-----

## Conclusion

Les dictionnaires Python constituent une pierre angulaire de la programmation moderne, offrant une flexibilité et une puissance inégalées pour la manipulation de données structurées. De la simple configuration d’application aux systèmes complexes de gestion de données, leur maîtrise est essentielle.

**Points clés à retenir :**

- Les dictionnaires stockent des paires clé-valeur pour un accès rapide et intuitif
- Les clés doivent être uniques et immuables
- Utilisez `.get()` pour un accès sécurisé
- Les compréhensions de dictionnaires offrent une syntaxe concise et élégante
- Les structures imbriquées permettent de modéliser des données complexes
- Attention aux pièges : copie superficielle, modification pendant l’itération

**Pour aller plus loin :**

- Explorez le module `collections` (Counter, defaultdict, ChainMap)
- Découvrez les dataclasses (Python 3.7+) pour des structures de données typées
- Apprenez la sérialisation JSON et YAML pour la persistance
- Maîtrisez les patrons de conception utilisant des dictionnaires

Les dictionnaires, combinés aux listes, forment le duo dynamique des structures de données Python. Leur maîtrise vous ouvrira les portes d’une programmation plus expressive, plus efficace et plus élégante. Continuez à pratiquer et à expérimenter : chaque problème résolu enrichit votre compréhension et affine votre expertise.
🚀​​​​​​​