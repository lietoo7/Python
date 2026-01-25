# Trois Mini-Projets Python avec Tableaux

## Projet 1 : Encodeur/Décodeur Binaire

### Objectif du projet

Créer un programme qui convertit du texte en code binaire (et inversement) en utilisant des tableaux pour stocker les représentations binaires de chaque caractère.

### Concepts utilisés

- Conversion de caractères en valeurs ASCII
- Manipulation de chaînes et de listes
- Fonctions de conversion binaire
- Boucles et itérations

-----

### Guide Pas à Pas

#### **Étape 1 : Comprendre le fonctionnement**

Avant de coder, comprenez le mécanisme :

- Chaque caractère a un code ASCII (par exemple : ‘A’ = 65, ‘a’ = 97, ’ ’ = 32)
- Ce code peut être converti en binaire (65 → ‘1000001’)
- Pour décoder, on fait l’inverse : binaire → ASCII → caractère

**À faire :**

- Testez manuellement avec Python :
  
  ```python
  # Essayez ces commandes dans la console
  ord('A')           # Donne le code ASCII
  bin(65)            # Convertit en binaire (renvoie '0b1000001')
  chr(65)            # Convertit ASCII en caractère
  int('1000001', 2)  # Convertit binaire en décimal
  ```

#### **Étape 2 : Créer la fonction d’encodage**

**Objectif :** Transformer “Hello” → [‘1001000’, ‘1100101’, ‘1101100’, ‘1101100’, ‘1101111’]

**Indices :**

1. Créez une fonction `encoder_texte(texte)`
1. Initialisez un tableau vide pour stocker les codes binaires
1. Parcourez chaque caractère du texte
1. Pour chaque caractère :

- Trouvez son code ASCII avec `ord()`
- Convertissez en binaire avec `bin()`
- Nettoyez le préfixe ‘0b’ (utilisez le slicing `[2:]`)
- Ajoutez au tableau

1. Retournez le tableau

**Questions à vous poser :**

- Quelle méthode utiliser pour ajouter un élément à un tableau ?
- Comment enlever les deux premiers caractères d’une chaîne ?

#### **Étape 3 : Créer la fonction de décodage**

**Objectif :** Transformer [‘1001000’, ‘1100101’] → “He”

**Indices :**

1. Créez une fonction `decoder_binaire(tableau_binaire)`
1. Initialisez une chaîne vide pour construire le texte
1. Parcourez chaque code binaire du tableau
1. Pour chaque code :

- Convertissez le binaire en décimal avec `int(code, 2)`
- Convertissez le décimal en caractère avec `chr()`
- Ajoutez le caractère à votre chaîne

1. Retournez la chaîne complète

**Astuce :** Vous pouvez construire une chaîne avec l’opérateur `+=` ou utiliser une liste + `''.join()`

#### **Étape 4 : Afficher joliment les résultats**

**Objectif :** Rendre la sortie lisible

**Suggestions :**

- Affichez le texte original
- Affichez le tableau binaire (peut-être avec un séparateur visuel comme “ | “)
- Affichez le texte décodé pour vérifier
- Ajoutez des messages explicatifs

**Exemple de format attendu :**

```
=== ENCODEUR BINAIRE ===
Texte original : Hello

Codes binaires :
1001000 | 1100101 | 1101100 | 1101100 | 1101111

Texte décodé : Hello
```

#### **Étape 5 : Créer le menu interactif**

**Fonctionnalités à implémenter :**

1. Afficher un menu avec 3 choix :

- Encoder un texte
- Décoder un code binaire
- Quitter

1. Demander le choix de l’utilisateur
1. Selon le choix :

- **Encodage :** Demander un texte, encoder, afficher
- **Décodage :** Demander des codes binaires séparés par des espaces, décoder, afficher
- **Quitter :** Terminer le programme

1. Utiliser une boucle pour revenir au menu après chaque opération

**Indices pour le décodage utilisateur :**

- Pour saisir plusieurs codes : `input().split()` crée automatiquement un tableau
- Exemple : “1001000 1100101” → [‘1001000’, ‘1100101’]

#### **Bonus (optionnel) :**

- Ajouter une gestion d’erreurs avec `try/except` pour les codes binaires invalides
- Permettre l’encodage avec un formatage sur 8 bits (ajouter des zéros devant si nécessaire)
- Sauvegarder l’encodage dans un fichier texte

-----

### Corrigé du Projet 1

```python
def encoder_texte(texte):
    """
    Encode un texte en une liste de codes binaires.
    
    Args:
        texte (str): Le texte à encoder
        
    Returns:
        list: Liste des représentations binaires de chaque caractère
    """
    codes_binaires = []
    
    for caractere in texte:
        # Obtenir le code ASCII
        code_ascii = ord(caractere)
        
        # Convertir en binaire et enlever le préfixe '0b'
        code_binaire = bin(code_ascii)[2:]
        
        # Optionnel : formater sur 8 bits (padding avec des zéros)
        code_binaire = code_binaire.zfill(8)
        
        codes_binaires.append(code_binaire)
    
    return codes_binaires


def decoder_binaire(tableau_binaire):
    """
    Décode une liste de codes binaires en texte.
    
    Args:
        tableau_binaire (list): Liste des codes binaires
        
    Returns:
        str: Le texte décodé
    """
    texte_decode = ""
    
    for code_binaire in tableau_binaire:
        # Convertir le binaire en décimal
        code_ascii = int(code_binaire, 2)
        
        # Convertir le code ASCII en caractère
        caractere = chr(code_ascii)
        
        texte_decode += caractere
    
    return texte_decode


def afficher_encodage(texte, codes_binaires):
    """
    Affiche joliment le résultat de l'encodage.
    """
    print("\n" + "=" * 50)
    print("RÉSULTAT DE L'ENCODAGE")
    print("=" * 50)
    print(f"Texte original : {texte}")
    print(f"\nNombre de caractères : {len(texte)}")
    print("\nCodes binaires :")
    print(" | ".join(codes_binaires))
    print("=" * 50 + "\n")


def afficher_decodage(codes_binaires, texte_decode):
    """
    Affiche joliment le résultat du décodage.
    """
    print("\n" + "=" * 50)
    print("RÉSULTAT DU DÉCODAGE")
    print("=" * 50)
    print("Codes binaires reçus :")
    print(" | ".join(codes_binaires))
    print(f"\nTexte décodé : {texte_decode}")
    print("=" * 50 + "\n")


def afficher_menu():
    """
    Affiche le menu principal.
    """
    print("\n" + "=" * 50)
    print("ENCODEUR/DÉCODEUR BINAIRE")
    print("=" * 50)
    print("1. Encoder un texte en binaire")
    print("2. Décoder un code binaire en texte")
    print("3. Quitter")
    print("=" * 50)


def main():
    """
    Fonction principale du programme.
    """
    while True:
        afficher_menu()
        
        choix = input("\nVotre choix (1-3) : ").strip()
        
        if choix == "1":
            # Encodage
            texte = input("\nEntrez le texte à encoder : ")
            
            if texte:
                codes_binaires = encoder_texte(texte)
                afficher_encodage(texte, codes_binaires)
                
                # Vérification automatique
                texte_verifie = decoder_binaire(codes_binaires)
                print(f"Vérification : {texte_verifie}")
            else:
                print("Erreur : Texte vide !")
        
        elif choix == "2":
            # Décodage
            print("\nEntrez les codes binaires séparés par des espaces :")
            print("Exemple : 01001000 01100101 01101100 01101100 01101111")
            
            entree = input("\nCodes binaires : ").strip()
            
            if entree:
                try:
                    codes_binaires = entree.split()
                    texte_decode = decoder_binaire(codes_binaires)
                    afficher_decodage(codes_binaires, texte_decode)
                except ValueError:
                    print("Erreur : Codes binaires invalides !")
            else:
                print("Erreur : Aucun code saisi !")
        
        elif choix == "3":
            # Quitter
            print("\nAu revoir !")
            break
        
        else:
            print("\nChoix invalide ! Veuillez choisir 1, 2 ou 3.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()
```

**Exemple d’exécution :**

```
==================================================
ENCODEUR/DÉCODEUR BINAIRE
==================================================
1. Encoder un texte en binaire
2. Décoder un code binaire en texte
3. Quitter
==================================================

Votre choix (1-3) : 1

Entrez le texte à encoder : Python

==================================================
RÉSULTAT DE L'ENCODAGE
==================================================
Texte original : Python

Nombre de caractères : 6

Codes binaires :
01010000 | 01111001 | 01110100 | 01101000 | 01101111 | 01101110
==================================================

Vérification : Python
```

-----

## Projet 2 : Cryptage ROT13

### Objectif du projet

Implémenter l’algorithme de chiffrement ROT13, une méthode de substitution simple où chaque lettre est remplacée par la lettre située 13 positions plus loin dans l’alphabet.

### Concepts utilisés

- Manipulation de chaînes de caractères
- Tableaux de référence (alphabet)
- Opérations modulo
- Distinction majuscules/minuscules

-----

### Guide Pas à Pas

#### **Étape 1 : Comprendre ROT13**

**Principe :**

- ROT13 décale chaque lettre de 13 positions dans l’alphabet
- A → N, B → O, C → P, …, M → Z, N → A, …, Z → M
- Les chiffres et caractères spéciaux restent inchangés
- ROT13 est réversible : appliquer ROT13 deux fois redonne le texte original

**À tester manuellement :**

```
"HELLO" → "URYYB"
"BONJOUR" → "OBAWBHE"
"Python 3.9" → "Clguba 3.9" (les chiffres ne changent pas)
```

**Astuce :** Il y a 26 lettres dans l’alphabet, donc décaler de 13 à deux reprises = décaler de 26 = revenir au début.

#### **Étape 2 : Créer les tableaux de référence**

**Objectif :** Avoir les alphabets sous forme de listes

**Indices :**

1. Créez deux tableaux (ou un seul si vous préférez) :

- Un pour les minuscules : [‘a’, ‘b’, ‘c’, …, ‘z’]
- Un pour les majuscules : [‘A’, ‘B’, ‘C’, …, ‘Z’]

1. **Méthode facile :** Utilisez la compréhension de liste avec `chr()` et `range()`
   
   ```python
   # Indices ASCII : 'a' = 97, 'A' = 65
   # Il y a 26 lettres
   ```
1. **Alternative :** Utilisez le module `string`
   
   ```python
   import string
   # string.ascii_lowercase contient 'abcdefghijklmnopqrstuvwxyz'
   # string.ascii_uppercase contient 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   ```

#### **Étape 3 : Créer la fonction ROT13**

**Objectif :** Transformer “Hello” → “Uryyb”

**Algorithme à implémenter :**

Pour chaque caractère du texte :

1. **Si c’est une lettre minuscule :**

- Trouver sa position dans l’alphabet (0-25)
- Ajouter 13 à cette position
- Utiliser le modulo 26 pour “boucler” (car 26 lettres)
- Récupérer la lettre à cette nouvelle position

1. **Si c’est une lettre majuscule :**

- Faire la même chose avec l’alphabet des majuscules

1. **Sinon (chiffre, espace, ponctuation) :**

- Garder le caractère tel quel

**Indices techniques :**

1. Pour trouver la position d’un caractère dans un tableau :
   
   ```python
   alphabet = ['a', 'b', 'c', 'd', 'e']
   position = alphabet.index('c')  # Retourne 2
   ```
1. Pour le modulo (boucler dans l’alphabet) :
   
   ```python
   nouvelle_position = (position + 13) % 26
   ```
1. Pour vérifier si un caractère est une lettre :
   
   ```python
   caractere.isalpha()  # True si lettre
   caractere.islower()  # True si minuscule
   caractere.isupper()  # True si majuscule
   ```

#### **Étape 4 : Structure de la fonction**

**Squelette à compléter :**

```python
def rot13(texte):
    # 1. Créer les alphabets de référence
    
    # 2. Initialiser une variable pour construire le résultat
    
    # 3. Parcourir chaque caractère
    
        # 4. Vérifier le type de caractère et appliquer la transformation
        
    # 5. Retourner le résultat
```

#### **Étape 5 : Créer l’interface utilisateur**

**Fonctionnalités :**

1. Menu avec options :

- Crypter un message
- Décrypter un message (même fonction que crypter !)
- Quitter

1. Pour chaque opération :

- Demander le texte
- Appliquer ROT13
- Afficher le résultat original et transformé

**Rappel important :** ROT13 est symétrique, donc crypter = décrypter !

#### **Étape 6 : Affichage amélioré**

**Suggestions :**

- Afficher le texte original et le texte crypté côte à côte
- Montrer un tableau de correspondance des lettres
- Afficher des statistiques (nombre de lettres transformées)

#### **Bonus (optionnel) :**

- Créer une variante ROT-N où l’utilisateur choisit le décalage (1-25)
- Ajouter la fréquence des lettres pour l’analyse cryptographique
- Créer une fonction de “brute force” qui teste tous les décalages possibles

-----

### Corrigé du Projet 2

```python
import string


def creer_alphabets():
    """
    Crée les tableaux d'alphabets minuscules et majuscules.
    
    Returns:
        tuple: (alphabet_minuscules, alphabet_majuscules)
    """
    # Méthode 1 : Avec le module string (plus simple)
    alpha_min = list(string.ascii_lowercase)
    alpha_maj = list(string.ascii_uppercase)
    
    # Méthode 2 : Avec chr() et range()
    # alpha_min = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # alpha_maj = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    
    return alpha_min, alpha_maj


def rot13(texte):
    """
    Applique le chiffrement ROT13 sur un texte.
    
    Args:
        texte (str): Le texte à crypter/décrypter
        
    Returns:
        str: Le texte transformé
    """
    alpha_min, alpha_maj = creer_alphabets()
    resultat = ""
    
    for caractere in texte:
        if caractere.islower():
            # Traitement des minuscules
            position = alpha_min.index(caractere)
            nouvelle_position = (position + 13) % 26
            resultat += alpha_min[nouvelle_position]
            
        elif caractere.isupper():
            # Traitement des majuscules
            position = alpha_maj.index(caractere)
            nouvelle_position = (position + 13) % 26
            resultat += alpha_maj[nouvelle_position]
            
        else:
            # Caractères non alphabétiques (chiffres, espaces, ponctuation)
            resultat += caractere
    
    return resultat


def rot_n(texte, decalage):
    """
    Version générique permettant un décalage personnalisé.
    
    Args:
        texte (str): Le texte à transformer
        decalage (int): Le nombre de positions à décaler
        
    Returns:
        str: Le texte transformé
    """
    alpha_min, alpha_maj = creer_alphabets()
    resultat = ""
    
    for caractere in texte:
        if caractere.islower():
            position = alpha_min.index(caractere)
            nouvelle_position = (position + decalage) % 26
            resultat += alpha_min[nouvelle_position]
            
        elif caractere.isupper():
            position = alpha_maj.index(caractere)
            nouvelle_position = (position + decalage) % 26
            resultat += alpha_maj[nouvelle_position]
            
        else:
            resultat += caractere
    
    return resultat


def afficher_tableau_correspondance():
    """
    Affiche un tableau montrant la correspondance ROT13.
    """
    print("\nTABLEAU DE CORRESPONDANCE ROT13")
    print("=" * 60)
    
    alpha_min, alpha_maj = creer_alphabets()
    
    print("Original : ", end="")
    for lettre in alpha_min:
        print(lettre, end=" ")
    
    print("\nROT13    : ", end="")
    for lettre in alpha_min:
        print(rot13(lettre), end=" ")
    
    print("\n" + "=" * 60 + "\n")


def afficher_resultat(texte_original, texte_transforme, operation):
    """
    Affiche le résultat de manière formatée.
    """
    print("\n" + "=" * 60)
    print(f"RÉSULTAT DU {operation.upper()}")
    print("=" * 60)
    print(f"Texte original    : {texte_original}")
    print(f"Texte transformé  : {texte_transforme}")
    
    # Statistiques
    nb_lettres = sum(1 for c in texte_original if c.isalpha())
    print(f"\nStatistiques      : {nb_lettres} lettres transformées")
    print("=" * 60 + "\n")


def brute_force(texte_crypte):
    """
    Teste tous les décalages possibles (1-25) pour aider au décryptage.
    """
    print("\n" + "=" * 60)
    print("BRUTE FORCE - TOUS LES DÉCALAGES POSSIBLES")
    print("=" * 60)
    
    for decalage in range(1, 26):
        resultat = rot_n(texte_crypte, decalage)
        print(f"ROT{decalage:2d}  : {resultat}")
    
    print("=" * 60 + "\n")


def afficher_menu():
    """
    Affiche le menu principal.
    """
    print("\n" + "=" * 60)
    print("CRYPTAGE ROT13")
    print("=" * 60)
    print("1. Crypter un message")
    print("2. Décrypter un message (ROT13)")
    print("3. Afficher le tableau de correspondance")
    print("4. Brute force (tester tous les décalages)")
    print("5. ROT-N personnalisé")
    print("6. Quitter")
    print("=" * 60)


def main():
    """
    Fonction principale du programme.
    """
    print("\nBienvenue dans le crypteur ROT13 !")
    print("Info : ROT13 est réversible (crypter 2 fois = texte original)")
    
    while True:
        afficher_menu()
        
        choix = input("\nVotre choix (1-6) : ").strip()
        
        if choix == "1":
            # Cryptage
            texte = input("\nEntrez le message à crypter : ")
            
            if texte:
                texte_crypte = rot13(texte)
                afficher_resultat(texte, texte_crypte, "cryptage")
                
                # Vérification
                verification = rot13(texte_crypte)
                print(f"Vérification (double ROT13) : {verification}")
            else:
                print("Erreur : Message vide !")
        
        elif choix == "2":
            # Décryptage (identique au cryptage pour ROT13)
            texte_crypte = input("\nEntrez le message à décrypter : ")
            
            if texte_crypte:
                texte_original = rot13(texte_crypte)
                afficher_resultat(texte_crypte, texte_original, "décryptage")
            else:
                print("Erreur : Message vide !")
        
        elif choix == "3":
            # Tableau de correspondance
            afficher_tableau_correspondance()
        
        elif choix == "4":
            # Brute force
            texte_crypte = input("\n🔍 Entrez le texte crypté : ")
            
            if texte_crypte:
                brute_force(texte_crypte)
            else:
                print("Erreur : Texte vide !")
        
        elif choix == "5":
            # ROT-N personnalisé
            texte = input("\nEntrez le texte : ")
            
            if texte:
                try:
                    decalage = int(input("Entrez le décalage (1-25) : "))
                    
                    if 1 <= decalage <= 25:
                        texte_transforme = rot_n(texte, decalage)
                        afficher_resultat(texte, texte_transforme, f"ROT{decalage}")
                    else:
                        print("Erreur : Le décalage doit être entre 1 et 25 !")
                except ValueError:
                    print("Erreur : Veuillez entrer un nombre valide !")
            else:
                print("Erreur : Texte vide !")
        
        elif choix == "6":
            # Quitter
            print("\nAu revoir !")
            break
        
        else:
            print("\nChoix invalide ! Veuillez choisir entre 1 et 6.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()
```

**Exemple d’exécution :**

```
==================================================
CRYPTAGE ROT13
==================================================
1. Crypter un message
2. Décrypter un message (ROT13)
3. Afficher le tableau de correspondance
4. Brute force (tester tous les décalages)
5. ROT-N personnalisé
6. Quitter
==================================================

Votre choix (1-6) : 1

Entrez le message à crypter : Bonjour Python!

============================================================
RÉSULTAT DU CRYPTAGE
============================================================
Texte original    : Bonjour Python!
Texte transformé  : Obawbhe Clguba!

Statistiques      : 13 lettres transformées
============================================================

Vérification (double ROT13) : Bonjour Python!
```

-----

## Projet 3 : Gestionnaire de Contacts avec Recherche et Tri

### Objectif du projet

Créer un gestionnaire de contacts complet utilisant des tableaux pour stocker les informations, avec des fonctionnalités de tri, recherche et filtrage.

### Concepts utilisés

- Listes de dictionnaires (tableaux d’objets structurés)
- Tri multicritères
- Recherche et filtrage
- Validation de données
- Persistance des données (bonus)

-----

### Guide Pas à Pas

#### **Étape 1 : Concevoir la structure de données**

**Objectif :** Définir comment stocker un contact

**Réflexions :**

- Quelles informations pour chaque contact ? (nom, prénom, téléphone, email, ville, etc.)
- Comment organiser ces données ?

**Suggestion de structure :**

```python
# Un contact = un dictionnaire
contact = {
    'nom': 'Dupont',
    'prenom': 'Marie',
    'telephone': '0612345678',
    'email': 'marie.dupont@email.com',
    'ville': 'Paris'
}

# Tous les contacts = une liste de dictionnaires
contacts = [contact1, contact2, contact3, ...]
```

**À faire :**

- Définissez les champs obligatoires et optionnels
- Créez une fonction `creer_contact()` qui demande les infos et retourne un dictionnaire

#### **Étape 2 : Implémenter l’ajout de contacts**

**Fonctionnalité :** Ajouter un nouveau contact au tableau

**Indices :**

1. Créez une fonction `ajouter_contact(contacts)`
1. Demandez les informations à l’utilisateur
1. Validez les données (téléphone = chiffres, email contient @, etc.)
1. Créez un dictionnaire avec ces infos
1. Ajoutez-le au tableau `contacts`

**Questions de validation :**

- Comment vérifier qu’un email contient un @ ?
- Comment s’assurer qu’un téléphone ne contient que des chiffres ?
- Faut-il vérifier les doublons ?

**Astuce validation :**

```python
# Vérifier si une chaîne contient uniquement des chiffres
telephone.isdigit()

# Vérifier la présence d'un caractère
'@' in email
```

#### **Étape 3 : Afficher tous les contacts**

**Objectif :** Créer un affichage clair et lisible

**Suggestions de format :**

```
============================================================
LISTE DES CONTACTS (3 contacts)
============================================================
[1] Marie DUPONT
    0612345678
    marie.dupont@email.com
    Paris
------------------------------------------------------------
[2] Jean MARTIN
    0623456789
    jean.martin@email.com
    Lyon
------------------------------------------------------------
```

**Indices :**

1. Créez une fonction `afficher_contacts(contacts)`
1. Utilisez `enumerate()` pour la numérotation
1. Formatez joliment avec des emojis et des lignes

#### **Étape 4 : Rechercher des contacts**

**Fonctionnalités à implémenter :**

1. **Recherche par nom** : Trouver tous les contacts dont le nom contient une chaîne
1. **Recherche par ville** : Filtrer par localisation
1. **Recherche globale** : Chercher dans tous les champs

**Algorithme de recherche simple :**

```python
# Rechercher "Dup" dans les noms
resultats = []
for contact in contacts:
    if "Dup".lower() in contact['nom'].lower():
        resultats.append(contact)
```

**Amélioration avec list comprehension :**

```python
resultats = [c for c in contacts if terme in c['nom'].lower()]
```

**Indices :**

- Utilisez `.lower()` pour une recherche insensible à la casse
- Retournez une nouvelle liste avec les résultats
- Affichez le nombre de résultats trouvés

#### **Étape 5 : Trier les contacts**

**Critères de tri à implémenter :**

1. Par nom (A→Z ou Z→A)
1. Par prénom
1. Par ville

**Rappel sur le tri :**

```python
# Tri d'une liste de dictionnaires par une clé
contacts.sort(key=lambda x: x['nom'])

# Tri décroissant
contacts.sort(key=lambda x: x['nom'], reverse=True)

# Fonction sorted() pour ne pas modifier l'original
contacts_tries = sorted(contacts, key=lambda x: x['nom'])
```

**À implémenter :**

1. Créez une fonction `trier_contacts(contacts, critere, ordre)`
1. `critere` peut être : ‘nom’, ‘prenom’, ‘ville’
1. `ordre` peut être : ‘croissant’ ou ‘decroissant’

#### **Étape 6 : Supprimer et modifier des contacts**

**Suppression :**

- Afficher la liste avec numéros
- Demander le numéro à supprimer
- Utiliser `del` ou `.pop()` pour retirer de la liste

**Modification :**

- Afficher le contact actuel
- Demander quels ch​​​​​​​​​​​​​​​​amps modifier

- Permettre de garder les valeurs actuelles (en appuyant sur Entrée)

**Indices pour la modification :**

```python
# Proposer de garder l'ancienne valeur
nouveau_nom = input(f"Nom [{contact['nom']}] : ") or contact['nom']
```

#### **Étape 7 : Statistiques et analyses**

**Fonctionnalités bonus :**

1. Nombre total de contacts
1. Répartition par ville
1. Contacts sans email
1. Contact le plus récent/ancien (si vous ajoutez une date de création)

**Exemple de statistiques :**

```python
def statistiques(contacts):
    print(f"Nombre total : {len(contacts)}")
    
    # Répartition par ville
    villes = {}
    for contact in contacts:
        ville = contact.get('ville', 'Non renseigné')
        villes[ville] = villes.get(ville, 0) + 1
    
    for ville, count in villes.items():
        print(f"{ville} : {count} contact(s)")
```

#### **Étape 8 : Sauvegarder et charger (bonus)**

**Objectif :** Persister les données entre les sessions

**Options :**

1. **Fichier JSON** (recommandé)
1. Fichier texte CSV
1. Fichier pickle

**Avec JSON :**

```python
import json

# Sauvegarder
with open('contacts.json', 'w', encoding='utf-8') as f:
    json.dump(contacts, f, ensure_ascii=False, indent=2)

# Charger
with open('contacts.json', 'r', encoding='utf-8') as f:
    contacts = json.load(f)
```

#### **Étape 9 : Menu principal complet**

**Structure du menu :**

```
1. Ajouter un contact
2. Afficher tous les contacts
3. Rechercher un contact
4. Trier les contacts
5. Modifier un contact
6. Supprimer un contact
7. Statistiques
8. Sauvegarder
9. Charger
0. Quitter
```

**Bonne pratique :** Organisez votre code en fonctions claires et réutilisables.

-----

### Corrigé du Projet 3

```python
import json
import os
from datetime import datetime


# ============================================================
# GESTION DES CONTACTS
# ============================================================

def creer_contact():
    """
    Crée un nouveau contact en demandant les informations à l'utilisateur.
    
    Returns:
        dict: Le contact créé ou None si annulé
    """
    print("\n" + "=" * 60)
    print("NOUVEAU CONTACT")
    print("=" * 60)
    print("Laissez vide pour annuler\n")
    
    nom = input("Nom * : ").strip()
    if not nom:
        print("Création annulée")
        return None
    
    prenom = input("Prénom * : ").strip()
    if not prenom:
        print("Création annulée")
        return None
    
    # Validation du téléphone
    while True:
        telephone = input("Téléphone (10 chiffres) * : ").strip()
        if not telephone:
            print("Création annulée")
            return None
        
        # Retirer les espaces et tirets éventuels
        telephone = telephone.replace(" ", "").replace("-", "")
        
        if telephone.isdigit() and len(telephone) == 10:
            break
        else:
            print("Format invalide ! Entrez 10 chiffres.")
    
    # Validation de l'email
    while True:
        email = input("Email * : ").strip().lower()
        if not email:
            print("Création annulée")
            return None
        
        if '@' in email and '.' in email.split('@')[1]:
            break
        else:
            print("Email invalide ! Doit contenir @ et un domaine.")
    
    ville = input("Ville : ").strip() or "Non renseignée"
    adresse = input("Adresse : ").strip() or "Non renseignée"
    
    contact = {
        'nom': nom.upper(),
        'prenom': prenom.capitalize(),
        'telephone': telephone,
        'email': email,
        'ville': ville.capitalize(),
        'adresse': adresse,
        'date_creation': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    print("\nContact créé avec succès !")
    return contact


def ajouter_contact(contacts):
    """
    Ajoute un nouveau contact à la liste.
    """
    contact = creer_contact()
    
    if contact:
        contacts.append(contact)
        print(f"{contact['prenom']} {contact['nom']} ajouté(e) aux contacts")
    
    return contacts


def afficher_contact(contact, numero=None):
    """
    Affiche un contact de manière formatée.
    """
    if numero is not None:
        print(f"\n[{numero}] {contact['prenom']} {contact['nom']}")
    else:
        print(f"\n{contact['prenom']} {contact['nom']}")
    
    print(f"    {contact['telephone']}")
    print(f"    {contact['email']}")
    print(f"    {contact['ville']}")
    
    if contact['adresse'] != "Non renseignée":
        print(f"    {contact['adresse']}")
    
    print(f"    Créé le : {contact['date_creation']}")
    print("-" * 60)


def afficher_contacts(contacts):
    """
    Affiche tous les contacts.
    """
    if not contacts:
        print("\nAucun contact dans le répertoire.")
        return
    
    print("\n" + "=" * 60)
    print(f"LISTE DES CONTACTS ({len(contacts)} contact(s))")
    print("=" * 60)
    
    for i, contact in enumerate(contacts, 1):
        afficher_contact(contact, i)


# ============================================================
# RECHERCHE
# ============================================================

def rechercher_contacts(contacts):
    """
    Recherche des contacts selon différents critères.
    """
    if not contacts:
        print("\nAucun contact à rechercher.")
        return
    
    print("\n" + "=" * 60)
    print("RECHERCHE DE CONTACTS")
    print("=" * 60)
    print("1. Rechercher par nom")
    print("2. Rechercher par prénom")
    print("3. Rechercher par ville")
    print("4. Recherche globale (tous les champs)")
    print("=" * 60)
    
    choix = input("\nVotre choix (1-4) : ").strip()
    terme = input("Terme de recherche : ").strip().lower()
    
    if not terme:
        print("Recherche annulée.")
        return
    
    resultats = []
    
    if choix == "1":
        resultats = [c for c in contacts if terme in c['nom'].lower()]
    elif choix == "2":
        resultats = [c for c in contacts if terme in c['prenom'].lower()]
    elif choix == "3":
        resultats = [c for c in contacts if terme in c['ville'].lower()]
    elif choix == "4":
        # Recherche dans tous les champs
        for contact in contacts:
            texte_complet = ' '.join(contact.values()).lower()
            if terme in texte_complet:
                resultats.append(contact)
    else:
        print("Choix invalide.")
        return
    
    # Affichage des résultats
    if resultats:
        print(f"\n{len(resultats)} résultat(s) trouvé(s) :")
        print("=" * 60)
        
        for i, contact in enumerate(resultats, 1):
            afficher_contact(contact, i)
    else:
        print(f"\nAucun contact trouvé pour '{terme}'")


# ============================================================
# TRI
# ============================================================

def trier_contacts(contacts):
    """
    Trie les contacts selon un critère choisi.
    """
    if not contacts:
        print("\nAucun contact à trier.")
        return contacts
    
    print("\n" + "=" * 60)
    print("TRI DES CONTACTS")
    print("=" * 60)
    print("1. Trier par nom")
    print("2. Trier par prénom")
    print("3. Trier par ville")
    print("4. Trier par date de création")
    print("=" * 60)
    
    choix = input("\nVotre choix (1-4) : ").strip()
    ordre = input("Ordre (c=croissant, d=décroissant) [c] : ").strip().lower() or 'c'
    
    reverse = (ordre == 'd')
    
    if choix == "1":
        contacts.sort(key=lambda x: x['nom'], reverse=reverse)
        print(f"Contacts triés par nom ({'Z→A' if reverse else 'A→Z'})")
    elif choix == "2":
        contacts.sort(key=lambda x: x['prenom'], reverse=reverse)
        print(f"Contacts triés par prénom ({'Z→A' if reverse else 'A→Z'})")
    elif choix == "3":
        contacts.sort(key=lambda x: x['ville'], reverse=reverse)
        print(f"Contacts triés par ville ({'Z→A' if reverse else 'A→Z'})")
    elif choix == "4":
        contacts.sort(key=lambda x: x['date_creation'], reverse=reverse)
        print(f"Contacts triés par date ({'récent→ancien' if reverse else 'ancien→récent'})")
    else:
        print("Choix invalide.")
    
    return contacts


# ============================================================
# MODIFICATION ET SUPPRESSION
# ============================================================

def modifier_contact(contacts):
    """
    Modifie un contact existant.
    """
    if not contacts:
        print("\nAucun contact à modifier.")
        return contacts
    
    afficher_contacts(contacts)
    
    try:
        numero = int(input("\nNuméro du contact à modifier : "))
        
        if 1 <= numero <= len(contacts):
            contact = contacts[numero - 1]
            
            print("\n" + "=" * 60)
            print("MODIFICATION DU CONTACT")
            print("=" * 60)
            print("Appuyez sur Entrée pour conserver la valeur actuelle\n")
            
            # Modification des champs
            contact['nom'] = (input(f"Nom [{contact['nom']}] : ").strip() or contact['nom']).upper()
            contact['prenom'] = (input(f"Prénom [{contact['prenom']}] : ").strip() or contact['prenom']).capitalize()
            
            nouveau_tel = input(f"Téléphone [{contact['telephone']}] : ").strip().replace(" ", "").replace("-", "")
            if nouveau_tel and nouveau_tel.isdigit() and len(nouveau_tel) == 10:
                contact['telephone'] = nouveau_tel
            
            nouvel_email = input(f"Email [{contact['email']}] : ").strip().lower()
            if nouvel_email and '@' in nouvel_email:
                contact['email'] = nouvel_email
            
            contact['ville'] = (input(f"Ville [{contact['ville']}] : ").strip() or contact['ville']).capitalize()
            contact['adresse'] = input(f"Adresse [{contact['adresse']}] : ").strip() or contact['adresse']
            
            print("\nContact modifié avec succès !")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    
    return contacts


def supprimer_contact(contacts):
    """
    Supprime un contact.
    """
    if not contacts:
        print("\nAucun contact à supprimer.")
        return contacts
    
    afficher_contacts(contacts)
    
    try:
        numero = int(input("\nNuméro du contact à supprimer : "))
        
        if 1 <= numero <= len(contacts):
            contact = contacts[numero - 1]
            confirmation = input(f"Confirmer la suppression de {contact['prenom']} {contact['nom']} ? (o/n) : ").strip().lower()
            
            if confirmation == 'o':
                contacts.pop(numero - 1)
                print("Contact supprimé avec succès !")
            else:
                print("Suppression annulée.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un nombre valide.")
    
    return contacts


# ============================================================
# STATISTIQUES
# ============================================================

def afficher_statistiques(contacts):
    """
    Affiche des statistiques sur les contacts.
    """
    if not contacts:
        print("\nAucun contact pour les statistiques.")
        return
    
    print("\n" + "=" * 60)
    print("STATISTIQUES")
    print("=" * 60)
    
    # Nombre total
    print(f"Nombre total de contacts : {len(contacts)}")
    
    # Répartition par ville
    villes = {}
    for contact in contacts:
        ville = contact['ville']
        villes[ville] = villes.get(ville, 0) + 1
    
    print("\nRépartition par ville :")
    for ville, count in sorted(villes.items(), key=lambda x: x[1], reverse=True):
        print(f"  • {ville} : {count} contact(s)")
    
    # Contacts récents
    contacts_tries = sorted(contacts, key=lambda x: x['date_creation'], reverse=True)
    
    print("\nDerniers contacts ajoutés :")
    for contact in contacts_tries[:3]:
        print(f"  • {contact['prenom']} {contact['nom']} - {contact['date_creation']}")
    
    print("=" * 60)


# ============================================================
# SAUVEGARDE ET CHARGEMENT
# ============================================================

def sauvegarder_contacts(contacts, fichier='contacts.json'):
    """
    Sauvegarde les contacts dans un fichier JSON.
    """
    try:
        with open(fichier, 'w', encoding='utf-8') as f:
            json.dump(contacts, f, ensure_ascii=False, indent=2)
        print(f"{len(contacts)} contact(s) sauvegardé(s) dans '{fichier}'")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")


def charger_contacts(fichier='contacts.json'):
    """
    Charge les contacts depuis un fichier JSON.
    
    Returns:
        list: Liste des contacts chargés
    """
    if not os.path.exists(fichier):
        print(f"Aucun fichier '{fichier}' trouvé. Démarrage avec un répertoire vide.")
        return []
    
    try:
        with open(fichier, 'r', encoding='utf-8') as f:
            contacts = json.load(f)
        print(f" {len(contacts)} contact(s) chargé(s) depuis '{fichier}'")
        return contacts
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
        return []


# ============================================================
# MENU PRINCIPAL
# ============================================================

def afficher_menu():
    """
    Affiche le menu principal.
    """
    print("\n" + "=" * 60)
    print("GESTIONNAIRE DE CONTACTS")
    print("=" * 60)
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Rechercher un contact")
    print("4. Trier les contacts")
    print("5. Modifier un contact")
    print("6. Supprimer un contact")
    print("7. Statistiques")
    print("8. Sauvegarder")
    print("9. Recharger depuis le fichier")
    print("0. Quitter")
    print("=" * 60)


def main():
    """
    Fonction principale du programme.
    """
    print("\nBienvenue dans le Gestionnaire de Contacts !")
    
    # Chargement automatique au démarrage
    contacts = charger_contacts()
    
    while True:
        afficher_menu()
        
        choix = input("\nVotre choix (0-9) : ").strip()
        
        if choix == "1":
            contacts = ajouter_contact(contacts)
        
        elif choix == "2":
            afficher_contacts(contacts)
        
        elif choix == "3":
            rechercher_contacts(contacts)
        
        elif choix == "4":
            contacts = trier_contacts(contacts)
        
        elif choix == "5":
            contacts = modifier_contact(contacts)
        
        elif choix == "6":
            contacts = supprimer_contact(contacts)
        
        elif choix == "7":
            afficher_statistiques(contacts)
        
        elif choix == "8":
            sauvegarder_contacts(contacts)
        
        elif choix == "9":
            contacts = charger_contacts()
        
        elif choix == "0":
            # Proposition de sauvegarde avant de quitter
            if contacts:
                sauvegarde = input("\nSauvegarder avant de quitter ? (o/n) : ").strip().lower()
                if sauvegarde == 'o':
                    sauvegarder_contacts(contacts)
            
            print("\nAu revoir !")
            break
        
        else:
            print("\nChoix invalide ! Veuillez choisir entre 0 et 9.")


# Point d'entrée du programme
if __name__ == "__main__":
    main()
```

**Exemple d’exécution :**

```
Bienvenue dans le Gestionnaire de Contacts !
Aucun fichier 'contacts.json' trouvé. Démarrage avec un répertoire vide.

============================================================
GESTIONNAIRE DE CONTACTS
============================================================
1. Ajouter un contact
2. Afficher tous les contacts
3. Rechercher un contact
4. Trier les contacts
5. Modifier un contact
6. Supprimer un contact
7. Statistiques
8. Sauvegarder
9. Recharger depuis le fichier
0. Quitter
============================================================

Votre choix (0-9) : 1

============================================================
+ NOUVEAU CONTACT
============================================================
Laissez vide pour annuler

Nom * : Dupont
Prénom * : Marie
Téléphone (10 chiffres) * : 0612345678
Email * : marie.dupont@email.com
Ville : Paris
Adresse : 123 rue de la Paix

Contact créé avec succès !
Marie DUPONT ajouté(e) aux contacts
```

-----

## Conclusion

Ces trois projets vous permettent de maîtriser les tableaux Python dans des contextes variés :

1. **Projet 1** : Manipulation de chaînes et conversions (binaire)
1. **Projet 2** : Algorithmes de chiffrement et transformations
1. **Projet 3** : Gestion de données structurées complexes

**Points clés appris :**

- Création et manipulation de listes
- Parcours avec boucles et compréhensions
- Tri et recherche
- Structures de données imbriquées (listes de dictionnaires)
- Validation de données
- Persistance avec JSON

**Pour aller plus loin :**

- Ajoutez une interface graphique (tkinter)
- Créez une version web (Flask/Django)
- Implémentez d’autres algorithmes de cryptage (César, Vigenère)
- Ajoutez l’import/export CSV pour le gestionnaire de contacts

Bon codage !🚀