# Compréhensions et Générateurs

La seconde partie de la citation « éliminez l'essentiel » représente pour nous ce qui rend un programme informatique élégant. Nous nous efforçons constamment de trouver de meilleures façons de faire les choses afin de ne pas gaspiller de temps ou de mémoire.

Il existe des raisons valables de ne pas pousser notre code à sa limite absolue. Par exemple, il faut parfois sacrifier la lisibilité ou la maintenabilité pour obtenir une amélioration négligeable. Il n'est pas logique d'avoir une page web servie en 1 seconde avec un code illisible et complexe, alors que nous pourrions la servir en 1,05 seconde avec un code propre et lisible.

D'un autre côté, il est parfois parfaitement raisonnable de tenter de gagner une milliseconde sur une fonction, surtout lorsqu'elle est destinée à être appelée des milliers de fois. Une milliseconde économisée sur des milliers d'appels finit par représenter des secondes gagnées au total, ce qui peut être significatif pour votre application.

À la lumière de ces considérations, l'objectif de ce chapitre ne sera pas de vous donner les outils pour pousser votre code aux limites absolues de la performance et de l'optimisation à tout prix, mais plutôt de vous permettre d'écrire un code efficace et élégant qui se lit bien, s'exécute rapidement et ne gaspille pas les ressources de manière flagrante.

Dans ce chapitre, nous allons aborder les points suivants :

* Les fonctions `map()`, `zip()` et `filter()`
* Les compréhensions
* Les générateurs
* La performance

Nous effectuerons plusieurs mesures et comparaisons pour en tirer prudemment des conclusions. Gardez à l'esprit que sur une machine différente, avec une configuration ou un système d'exploitation différent, les résultats peuvent varier.

Observez ce code :

```python
# squares.py
def square1(n):
    return n**2  # mise au carré via l'opérateur de puissance

def square2(n):
    return n * n  # mise au carré via la multiplication

```

Les deux fonctions renvoient le carré de `n`, mais laquelle est la plus rapide ? D'après un simple test de performance (*benchmark*) que nous avons effectué, il semble que la seconde soit légèrement plus rapide. Si l'on y réfléchit, c'est logique : le calcul de la puissance d'un nombre implique une multiplication. Par conséquent, quel que soit l'algorithme utilisé pour l'opération de puissance, il est peu probable qu'il batte une simple multiplication comme celle de `square2`.

Ce résultat nous importe-t-il ? Dans la plupart des cas, non. Si vous codez un site de commerce électronique, il est probable que vous n'ayez jamais besoin d'élever un nombre au carré, et si c'est le cas, ce sera sans doute une opération sporadique. Vous n'avez pas besoin de vous soucier de gagner une fraction de microseconde sur une fonction que vous n'appelez que quelques fois.

Alors, quand l'optimisation devient-elle importante ? Un cas courant est celui où vous devez manipuler d'immenses collections de données. Si vous appliquez la même fonction à un million d'objets clients, vous voulez que votre fonction soit optimisée au maximum. Gagner un dixième de seconde sur une fonction appelée un million de fois vous fait gagner 100 000 secondes, soit environ 27,7 heures. Concentrons-nous donc sur les collections et voyons quels outils Python vous propose pour les gérer avec efficacité et élégance.

> **Note :** Beaucoup de concepts vus dans ce chapitre sont basés sur les **itérateurs** et les **itérables**, rencontrés au chapitre 3. Nous verrons comment coder nos propres objets itérables au chapitre 6.

Certains objets que nous allons explorer sont des itérateurs, qui économisent la mémoire en ne traitant qu'un seul élément d'une collection à la fois plutôt que de créer une copie modifiée. Par conséquent, un effort supplémentaire est nécessaire si nous voulons simplement afficher le résultat de l'opération. Nous aurons souvent recours à l'encapsulation de l'itérateur dans un constructeur `list()`. En effet, passer un itérateur à `list()` l'épuise et place tous les éléments générés dans une nouvelle liste, que nous pouvons facilement imprimer.

Voyons un exemple avec un objet `range` :

```python
>>> range(7)
range(0, 7)
>>> list(range(7))  # place tous les éléments dans une liste pour les voir
[0, 1, 2, 3, 4, 5, 6]

```

Remarquez que taper `range(7)` ne montre pas le contenu car `range` ne charge jamais la séquence entière en mémoire. L'utilisation de `list()` nous permet de visualiser les nombres générés.

---

## Les fonctions map, zip et filter

### map

Selon la documentation officielle, `map(fonction, itérable, *itérables)` renvoie un itérateur qui applique la *fonction* à chaque élément de l'*itérable*. Si plusieurs itérables sont passés, la fonction doit accepter autant d'arguments. L'itérateur s'arrête lorsque l'itérable le plus court est épuisé.

```python
# map.example.txt
>>> list(map(lambda *a: a, range(3)))  # 1 itérable
[(0,), (1,), (2,)]
>>> list(map(lambda *a: a, range(3), "abc"))  # 2 itérables
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> # map s'arrête à l'itérateur le plus court
>>> list(map(lambda *a: a, (1, 2), "abc"))  # (1, 2) est le plus court
[(1, 'a'), (2, 'b')]

```

Un exemple plus intéressant est l'idiome **decorate-sort-undecorate** (également connu sous le nom de transformée de Schwartz). Cette technique consiste à transformer un objet (décorer), le trier, puis lui redonner sa forme originale (dédécorer).

```python
# decorate.sort.undecorate.py
students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
]

def decorate(student):
    # crée un tuple (somme des crédits, dictionnaire étudiant)
    return (sum(student["credits"].values()), student)

def undecorate(decorated_student):
    return decorated_student[1]

# Tri des étudiants par la somme de leurs crédits
students = sorted(map(decorate, students), reverse=True)
students = list(map(undecorate, students))

```

### zip

La fonction `zip(*iterables, strict=False)` renvoie un itérateur de tuples, où le i-ème tuple contient le i-ème élément de chacun des itérables passés en argument. On peut voir `zip()` comme un outil qui transforme les lignes en colonnes et vice-versa, à l'image de la transposition d'une matrice.

Depuis Python 3.10, le paramètre `strict=True` permet de lever une erreur si les itérables n'ont pas la même longueur, évitant ainsi de masquer des erreurs de données.

### filter

`filter(fonction, itérable)` construit un itérateur à partir des éléments de l'itérable pour lesquels la fonction est vraie. Si la fonction est `None`, tous les éléments évalués à "faux" en Python sont supprimés.

```python
>>> test = [2, 5, 8, 0, 1, 0]
>>> list(filter(None, test))
[2, 5, 8, 1]
>>> list(filter(lambda x: x > 4, test))
[5, 8]

```

---

## Compréhensions

Une compréhension est une notation concise pour effectuer une opération sur chaque élément d'une collection et/ou sélectionner un sous-ensemble d'éléments satisfaisant une condition. Python propose des compréhensions de listes, de dictionnaires et d'ensembles.

### Compréhensions de listes

Comparons le calcul des carrés des 10 premiers nombres naturels :

**Avec une boucle for :**

```python
squares = []
for n in range(10):
    squares.append(n**2)

```

**Avec une compréhension de liste :**

```python
squares = [n**2 for n in range(10)]

```

C'est beaucoup plus lisible. On peut également ajouter une condition `if` :

```python
# Carrés des nombres pairs uniquement
sq2 = [n**2 for n in range(10) if not n % 2]
# Résultat : [0, 4, 16, 36, 64]

```

### Compréhensions imbriquées

Il est possible d'imbriquer des boucles dans une compréhension. Par exemple, pour générer toutes les paires possibles d'une séquence sans duplication :

```python
items = "ABCD"
pairs = [(items[a], items[b]) 
         for a in range(len(items)) 
         for b in range(a, len(items))]

```

L'ordre est crucial : la boucle `for` sur `b` dépendant de `a`, elle doit impérativement apparaître après celle de `a`.
---
### Filtrage dans une compréhension

Nous pouvons également appliquer un filtrage à une compréhension. Commençons par le faire avec `filter()` pour trouver tous les triplets pythagoriciens dont les côtés courts sont inférieurs à 10. Un triplet pythagoricien est un ensemble de trois entiers  satisfaisant l'équation .

Pour éviter de tester deux fois la même combinaison, nous utiliserons une astuce similaire à l'exemple précédent :

```python
# pythagorean.triple.py
from math import sqrt

mx = 10
triples = [
    (a, b, sqrt(a**2 + b**2))
    for a in range(1, mx)
    for b in range(a, mx)
]

# Filtrage des triplets non pythagoriciens
triples = list(
    filter(lambda triple: triple[2].is_integer(), triples)
)
print(triples)  # affiche : [(3, 4, 5.0), (6, 8, 10.0)]

```

Dans ce code, nous générons une liste de triplets. Chaque tuple contient deux entiers (les côtés) et l'hypoténuse. Nous filtrons ensuite pour ne garder que les cas où l'hypoténuse est un entier via `is_integer()`.

Cependant, le résultat mélange entiers et flottants. Nous pouvons utiliser `map()` pour corriger cela, mais le code devient complexe. Une **compréhension de liste** rend l'opération beaucoup plus propre :

```python
# pythagorean.triple.comprehension.py
from math import sqrt
mx = 10
triples = [
    (a, b, sqrt(a**2 + b**2))
    for a in range(1, mx)
    for b in range(a, mx)
]
# Combinaison de filter et map en une seule compréhension propre
triples = [
    (a, b, int(c)) for a, b, c in triples if c.is_integer()
]

```

Nous pouvons encore optimiser cela en utilisant l'**expression d'assignation** (opérateur *walrus* `:=`) pour éviter de calculer deux fois la racine carrée :

```python
# pythagorean.triple.walrus.py
from math import sqrt
mx = 10
triples = [
    (a, b, int(c))
    for a in range(1, mx)
    for b in range(a, mx)
    if (c := sqrt(a**2 + b**2)).is_integer()
]

```

Cette approche est élégante et économise de la mémoire en ne stockant que les résultats valides.

---

### Compréhensions de dictionnaires et d'ensembles

Les compréhensions de dictionnaires fonctionnent sur le même principe, mais utilisent des accolades et une syntaxe `clé: valeur`.

```python
# dictionary.comprehensions.py
from string import ascii_lowercase
lettermap = {c: k for k, c in enumerate(ascii_lowercase, 1)}
# {'a': 1, 'b': 2, ..., 'z': 26}

```

Notez que les dictionnaires ne permettent pas de clés en double. Si une clé est répétée, la dernière valeur l'emporte. De même, les **compréhensions d'ensembles** (*set*) utilisent des accolades mais sans le signe deux-points :

```python
# set.comprehensions.py
word = "Hello"
letters = {c for c in word}
print(letters)  # affiche : {'H', 'o', 'e', 'l'} (doublons supprimés)

```

---

## Générateurs

Les générateurs allient élégance et efficacité en produisant des éléments un par un au lieu de les stocker tous en mémoire.

### Fonctions génératrices

Contrairement aux fonctions classiques qui utilisent `return`, les générateurs utilisent `yield`. Lorsqu'une ligne `yield` est atteinte, l'exécution est suspendue et l'état de la fonction est sauvegardé.

```python
# first.n.squares.py
def get_squares_gen(n):
    for x in range(n):
        yield x**2

squares = get_squares_gen(4)
print(next(squares))  # 0
print(next(squares))  # 1

```

**Pourquoi utiliser des générateurs ?**

1. **Économie de mémoire** : Vous pouvez traiter des séquences virtuellement infinies (comme des permutations d'une liste de 20 éléments) sans saturer votre RAM.
2. **Efficacité temporelle** : Vous commencez à recevoir des données immédiatement, sans attendre la fin du calcul total.

### Expressions génératrices

Elles s'écrivent comme les compréhensions de listes, mais avec des **parenthèses** au lieu de crochets.

```python
# Exemple de gain de performance
s = sum(n**2 for n in range(10**10))  # Réussi car traité un par un
# s = sum([n**2 for n in range(10**10)])  # Échec (MemoryError) car crée d'abord la liste géante

```

---

### Considérations sur la performance

En règle générale, les compréhensions et les fonctions intégrées comme `map()` sont plus rapides que les boucles `for` classiques. Cela s'explique par le fait qu'elles s'exécutent à la vitesse du langage C au sein de l'interpréteur, tandis que les boucles `for` sont interprétées en bytecode Python, ce qui est plus lent.

* **Espace** : Utilisez des générateurs si vous n'avez pas besoin d'accéder plusieurs fois à la même donnée ou de revenir en arrière.
* **Temps** : `map()` et les compréhensions offrent des performances similaires, souvent 30 % à 50 % plus rapides qu'une boucle `append()` manuelle.

---
## Le comportement de génération dans les fonctions natives

Le comportement de type "générateur" est très courant parmi les types et fonctions intégrés de Python. C’est d’ailleurs l’une des différences majeures entre Python 2 et Python 3. Dans Python 2, des fonctions telles que `map()`, `zip()` et `filter()` renvoyaient des listes au lieu d'objets itérables.
L'idée derrière ce changement est que si vous avez besoin de transformer ces résultats en liste, vous pouvez toujours envelopper l'appel dans une classe `list()`. En revanche, si vous avez seulement besoin d'itérer et que vous souhaitez conserver une empreinte mémoire aussi légère que possible, vous pouvez utiliser ces fonctions en toute sécurité. Un autre exemple notable est la fonction `range()`. Dans Python 2, elle renvoyait une liste ; il existait une autre fonction appelée `xrange()` qui se comportait comme la fonction `range()` actuelle de Python 3.
Le concept de fonctions et de méthodes renvoyant des objets itérables est très répandu. On le retrouve dans :

* La fonction `open()`, utilisée pour manipuler des objets fichiers (voir Chapitre 8).
* La fonction `enumerate()`.
* Les méthodes de dictionnaires `keys()`, `values()` et `items()`.

Tout cela est logique : Python vise à réduire l'empreinte mémoire en évitant de gaspiller de l'espace partout où cela est possible, en particulier dans les fonctions et méthodes utilisées intensivement. Comme nous l'avons dit au début de ce chapitre, il est plus pertinent d'optimiser les performances d'un code traitant de grandes collections d'objets, plutôt que de grignoter quelques millisecondes sur une fonction appelée deux fois par jour. C'est précisément ce que fait Python ici.

---

## Un dernier exemple

Avant de terminer ce chapitre, nous allons vous présenter un problème simple que Fabrizio avait l'habitude de soumettre aux candidats pour un poste de développeur Python.
**Le problème est le suivant :** écrivez une fonction qui renvoie les termes de la suite `0 1 1 2 3 5 8 13 21 ...`, jusqu'à une certaine limite, .
Il s'agit de la suite de Fibonacci, définie par  et, pour tout . Cette suite est excellente pour tester les connaissances sur la récursivité, les techniques de mémoïsation et d'autres détails techniques, mais dans ce cas, c'était une bonne occasion de vérifier si le candidat connaissait les générateurs.
Commençons par une version rudimentaire, puis améliorons-la :

```python
# fibonacci.first.py
def fibonacci(N):
    """Renvoie tous les nombres de Fibonacci jusqu'à N."""
    result = [0]
    next_n = 1
    while next_n <= N:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result

print(fibonacci(0))   # [0]
print(fibonacci(1))   # [0, 1, 1]
print(fibonacci(50))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

**Analyse du code :** nous initialisons la liste `result` avec la valeur `[0]`. Ensuite, nous commençons l'itération à partir de l'élément suivant (`next_n`), qui est 1. Tant que l'élément suivant n'est pas supérieur à , nous continuons à l'ajouter à la liste et à calculer la valeur suivante de la suite. Nous calculons l'élément suivant en prenant une tranche (*slice*) des deux derniers éléments de la liste `result` et en la passant à la fonction `sum()`.
> **Note :** Si vous avez du mal à comprendre le code, il peut être utile d'ajouter des instructions `print()` pour voir comment les valeurs évoluent pendant l'exécution.
Lorsque la condition de la boucle devient `False`, nous sortons de la boucle et renvoyons `result`. Vous pouvez voir le résultat de ces appels dans les commentaires à côté de chaque instruction.
À ce stade, Fabrizio posait la question suivante au candidat : *« Et si je voulais simplement itérer sur ces nombres ? »* Un bon candidat modifierait alors le code ainsi :

```python
# fibonacci.second.py
def fibonacci(N):
    """Renvoie tous les nombres de Fibonacci jusqu'à N."""
    yield 0
    if N == 0:
        return
    a = 0
    b = 1
    while b <= N:
        yield b
        a, b = b, a + b

print(list(fibonacci(50))) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

Désormais, la fonction `fibonacci()` est une fonction **génératrice**. D'abord, nous produisons (`yield`) 0, puis si  vaut 0, nous quittons (ce qui lève une exception `StopIteration`). Sinon, nous bouclons en produisant `b` à chaque itération, avant de mettre à jour `a` et `b`. Cette solution repose sur le fait que nous n'avons besoin que des deux derniers éléments (`a` et `b`) pour produire le suivant.
Ce code est bien meilleur, possède une empreinte mémoire plus légère, et il suffit d'envelopper l'appel avec `list()` pour obtenir une liste, comme d'habitude. Nous pouvons cependant le rendre encore plus élégant :

```python
# fibonacci.elegant.py
def fibonacci(N):
    """Renvoie tous les nombres de Fibonacci jusqu'à N."""
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b

```

Le corps de la fonction ne fait plus que quatre lignes. Notez comment l'utilisation de l'assignation par tuple (`a, b = b, a + b`) rend le code plus court et plus lisible.

---

## Résumé

Dans ce chapitre, nous avons exploré plus en profondeur les concepts d'itération et de génération. Nous avons étudié les fonctions `map()`, `zip()` et `filter()` et appris à les utiliser comme alternatives aux boucles `for` classiques.
Ensuite, nous avons couvert le concept de **compréhensions** pour construire des listes, des dictionnaires et des ensembles. Nous avons exploré leur syntaxe et vu comment elles peuvent remplacer avantageusement l'approche classique de la boucle `for` ainsi que les fonctions `map()`, `zip()` et `filter()`.
Enfin, nous avons abordé les **générateurs** sous deux formes : les fonctions génératrices et les expressions génératrices. Nous avons appris à économiser du temps et de l'espace en utilisant ces techniques, permettant d'effectuer des opérations impossibles à réaliser avec de simples listes.
En termes de performances, nous avons vu que les boucles `for` sont les moins rapides, mais qu'elles offrent la meilleure lisibilité et flexibilité. À l'inverse, les fonctions comme `map()`, `filter()` et les compréhensions peuvent être beaucoup plus rapides. Toutefois, la complexité du code écrit avec ces techniques peut croître de manière exponentielle ; il est donc parfois nécessaire de privilégier la boucle `for` classique pour favoriser la maintenabilité.
Le chapitre suivant sera entièrement consacré aux **objets et aux classes**.

---
