# Programmation Conditionnelle et Itération

## Programmation conditionnelle

La programmation conditionnelle, ou branchement, est une activité que vous pratiquez à chaque instant de votre vie. Essentiellement, cela consiste à évaluer des conditions et à décider de l'action à entreprendre : *si* le feu est vert, *alors* je peux traverser ; *si* il pleut, *alors* je prends mon parapluie ; et *si* je suis en retard au travail, *alors* j'appellerai mon responsable.

### L'instruction `if`

L'outil principal de la programmation conditionnelle en Python est l'instruction `if`. Sa fonction est d'évaluer une expression et, selon le résultat, de choisir la partie du code à exécuter. Comme à notre habitude, examinons un exemple :

```python
# conditional.1.py
late = True
if late:
    print("Je dois appeler mon responsable !")

```

C'est l'exemple le plus simple possible : l'instruction `if` évalue l'expression `late` dans un contexte booléen (exactement comme si nous appelions `bool(late)`). Si le résultat de l'évaluation est `True`, alors nous entrons dans le corps du code immédiatement après l'instruction `if`. Remarquez que l'instruction `print` est indentée, ce qui signifie qu'elle appartient à une portée définie par la clause `if`. L'exécution de ce code donne :

```bash
$ python conditional.1.py
Je dois appeler mon responsable !

```

Puisque `late` est `True`, l'instruction `print()` a été exécutée. Nous pouvons enrichir l'instruction `if` de base en ajoutant une clause `else`. Celle-ci fournit un ensemble d'instructions alternatives à exécuter lorsque l'expression de la clause `if` est évaluée à `False`.

```python
# conditional.2.py
late = False
if late:
    print("Je dois appeler mon responsable !")  # 1
else:
    print("Pas besoin d'appeler mon responsable...")  # 2

```

Cette fois, nous avons défini `late = False`. Le résultat est donc différent :

```bash
$ python conditional.2.py
Pas besoin d'appeler mon responsable...

```

Selon le résultat de l'évaluation de `late`, nous pouvons entrer soit dans le bloc #1, soit dans le bloc #2, mais jamais dans les deux.

### Un `else` spécialisé : `elif`

Ce que nous avons vu jusqu'à présent suffit lorsque vous n'avez qu'une seule condition à évaluer et, au plus, deux chemins alternatifs. Parfois, cependant, vous devez évaluer plus d'une condition pour choisir parmi plusieurs voies.

Prenons l'exemple d'un simple calculateur d'impôts. Supposons les règles suivantes :

* Revenu < 10 000 $ : 0% d'impôt.
* Entre 10 000  : 20% d'impôt.
* Entre 30 000  : 35% d'impôt.
* Plus de 100 000 $ : 45% d'impôt.

Voici la traduction en code Python :

```python
# taxes.py
income = 15000
if income < 10000:
    tax_coefficient = 0.0  # 1
elif income < 30000:
    tax_coefficient = 0.2  # 2
elif income < 100000:
    tax_coefficient = 0.35  # 3
else:
    tax_coefficient = 0.45  # 4

print(f"Vous paierez : ${income * tax_coefficient} d'impôts")

```

L'ordre est obligatoire : `if` en premier, puis (optionnellement) autant de clauses `elif` que nécessaire, et enfin (optionnellement) une seule clause `else`. Testez toujours les valeurs limites (10 000, 30 000, etc.) pour vous assurer que vos opérateurs (`<` ou `<=`) produisent le résultat escompté.

### Imbrication d'instructions `if`

Vous pouvez également imbriquer des instructions `if`. Imaginons un système d'alerte d'erreurs :

```python
# errorsalert.py
alert_system = "console"  # peut être "email"
error_severity = "critical"  # "medium" ou "low"
error_message = "Quelque chose de terrible est arrivé !"

if alert_system == "console":
    print(error_message)  # 1
elif alert_system == "email":
    if error_severity == "critical":  # imbriqué
        send_email("admin@example.com", error_message)  # 2
    elif error_severity == "medium":
        send_email("support.1@example.com", error_message)  # 3
    else:
        send_email("support.2@example.com", error_message)  # 4

```

### L'opérateur ternaire

En Python, on l'appelle aussi expression conditionnelle. Il se comporte comme une version courte et en ligne d'un `if`. Au lieu de :

```python
if order_total > 100:
    discount = 25
else:
    discount = 0

```

On peut écrire :

```python
discount = 25 if order_total > 100 else 0

```

---

## Pattern Matching (Correspondance de motifs)

Introduit dans Python 3.10 (PEP 634), le `match` compare une valeur à plusieurs motifs :

```python
# match.py
day_number = 4
match day_number:
    case 1 | 2 | 3 | 4 | 5:
        print("Jour de la semaine")
    case 6:
        print("Samedi")
    case 7:
        print("Dimanche")
    case _:
        print(f"{day_number} n'est pas un numéro de jour valide")

```

Le symbole `_` est un joker (wildcard) qui correspond à n'importe quelle valeur.

---

## Les Boucles (Looping)

Boucler signifie répéter l'exécution d'un bloc de code. Python distille cela en deux instructions : `for` et `while`.

### La boucle `for`

Elle est utilisée pour parcourir une séquence (liste, tuple, chaîne de caractères).

```python
for number in range(5):
    print(number)

```

La fonction `range()` est essentielle :

* `range(10)` : de 0 à 9.
* `range(3, 8)` : de 3 à 7.
* `range(-10, 10, 4)` : de -10 à 10 par pas de 4.

#### Itérer avec `enumerate()` et `zip()`

Pour obtenir à la fois l'index et la valeur, utilisez `enumerate()` :

```python
surnames = ["Rivest", "Shamir", "Adleman"]
for position, surname in enumerate(surnames):
    print(position, surname)

```

Pour parcourir deux listes en parallèle, utilisez `zip()` :

```python
people = ["Nick", "Rick", "Roger", "Syd"]
ages = [23, 24, 23, 21]
for person, age in zip(people, ages):
    print(person, age)

```

### La boucle `while`

Elle tourne tant qu'une condition est satisfaite. Exemple de conversion d'un nombre en binaire :

```python
# binary.py
n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
remainders.reverse()
print(remainders)

```

---

## Les instructions `break` et `continue`

* **`continue`** : Arrête l'itération actuelle et passe immédiatement à la suivante.
* **`break`** : Sort prématurément de la boucle.

Exemple de recherche avec un drapeau (*flag*) :

```python
items = [0, None, 0.0, True, 0, 7]
found = False
for item in items:
    if item:
        found = True
        break  # On a trouvé un élément True, on s'arrête là.

```

 
