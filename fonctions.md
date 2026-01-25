# Les fonctions, blocs de construction du code

Dans les chapitres précédents, nous avons vu que tout est objet en Python, et les fonctions ne font pas exception. Mais qu'est-ce qu'une fonction exactement ? Une fonction est un bloc de code réutilisable conçu pour effectuer une tâche spécifique ou un groupe de tâches connexes. Cette unité peut ensuite être importée et utilisée partout où elle est nécessaire. L'utilisation des fonctions dans votre code présente de nombreux avantages, comme nous le verrons bientôt.

Dans ce chapitre, nous allons aborder les points suivants :

* Les fonctions : ce qu'elles sont et pourquoi nous devrions les utiliser.
* Les portées (*scopes*) et la résolution de noms.
* Les signatures de fonction : paramètres d'entrée et valeurs de retour.
* Les fonctions récursives et anonymes.
* L'importation d'objets pour la réutilisation du code.

Nous pensons que l'adage « une image vaut mille mots » est particulièrement vrai lorsqu'il s'agit d'expliquer les fonctions à quelqu'un qui découvre ce concept. Veuillez donc examiner la figure suivante :

Comme vous pouvez le voir, une fonction est un bloc d'instructions, emballé comme un tout, tel une boîte. Les fonctions peuvent accepter des paramètres d'entrée et produire des valeurs de sortie. Ces deux éléments sont optionnels, comme nous le verrons dans les exemples de ce chapitre.

Une fonction en Python est définie à l'aide du mot-clé `def`, suivi du nom de la fonction, se terminant par une paire de parenthèses (qui peuvent ou non contenir des paramètres d'entrée) ; un deux-points (`:`) signale ensuite la fin de la définition de la fonction. Immédiatement après, indenté par quatre espaces, nous trouvons le corps de la fonction, qui est l'ensemble des instructions que la fonction exécutera lorsqu'elle sera appelée.

> **Note :** L'indentation de quatre espaces n'est pas obligatoire, mais c'est le nombre d'espaces suggéré par la PEP 8 et, en pratique, c'est la mesure d'espacement la plus largement utilisée.

Une fonction peut ou non renvoyer une sortie. Si une fonction souhaite renvoyer un résultat, elle le fait en utilisant le mot-clé `return`, suivi de la sortie souhaitée. Vous avez peut-être remarqué le petit astérisque après "Optionnel" dans la section de sortie du diagramme précédent. C'est parce qu'une fonction renvoie toujours quelque chose en Python, même si vous n'utilisez pas explicitement l'instruction `return`. Si la fonction n'a pas d'instruction `return` dans son corps, ou si aucune valeur n'est donnée à l'instruction `return` elle-même, la fonction renvoie `None`.

Ce choix de conception est ancré dans plusieurs raisons, dont les plus importantes sont :

* **Simplicité et cohérence :** Que la fonction renvoie explicitement une valeur ou non, son comportement reste cohérent.
* **Réduction de la complexité :** Plusieurs langues font une distinction entre les fonctions (qui renvoient une valeur) et les procédures (qui n'en renvoient pas). En Python, les fonctions peuvent jouer les deux rôles, sans avoir besoin de structures distinctes. Cela minimise le nombre de concepts qu'un programmeur doit apprendre.
* **Cohérence pour les chemins multiples :** Les fonctions comportant plusieurs branches conditionnelles renverront `None` lorsqu'aucune autre instruction `return` n'est exécutée. `None` est donc une valeur par défaut utile.

La liste fournie démontre la multitude de facteurs qui peuvent influencer une décision de conception apparemment simple. Ce sont les choix prudents et délibérés qui sous-tendent la conception de Python qui contribuent à son élégance, sa simplicité et sa polyvalence.

## Pourquoi utiliser des fonctions ?

Les fonctions figurent parmi les concepts et structures les plus importants de tout langage. Voici quelques raisons pour lesquelles nous en avons besoin :

* Elles réduisent la duplication de code dans un programme. L'encapsulation des instructions d'une tâche dans une fonction que nous pouvons importer et appeler quand nous le voulons nous permet d'éviter de dupliquer l'implémentation.
* Elles aident à diviser une tâche ou une procédure complexe en blocs plus petits, chacun devenant une fonction.
* Elles masquent les détails d'implémentation aux utilisateurs.
* Elles améliorent la traçabilité.
* Elles améliorent la lisibilité.

Examinons maintenant quelques exemples pour mieux comprendre chaque point.

### Réduction de la duplication de code

Imaginez que vous écriviez un logiciel scientifique et que vous ayez besoin de calculer des nombres premiers jusqu'à une certaine limite — comme nous l'avons fait au chapitre précédent. Vous avez un algorithme pour les calculer, vous le copiez et le collez partout où vous en avez besoin. Un jour, cependant, un collègue vous donne un algorithme plus performant. À ce stade, vous devez parcourir toute votre base de code et remplacer l'ancien code par le nouveau.

Cette procédure est source d'erreurs. Vous pouvez facilement supprimer par erreur des parties du code environnant ou oublier de supprimer certains morceaux de code. Vous risquez également de manquer certains endroits où le calcul est effectué, laissant votre logiciel dans un état incohérent. Si, au lieu de remplacer le code par une meilleure version, vous deviez corriger un bogue et que vous en oubliez un, ce serait encore pire.

Pour éviter tout cela, vous écrivez une fonction, `get_prime_numbers(upto)`, et vous l'utilisez partout où vous devez calculer une liste de nombres premiers. Lorsque votre collègue vous donne une meilleure implémentation, tout ce que vous avez à faire est de remplacer le corps de cette fonction par le nouveau code. Le reste du logiciel s'adaptera automatiquement puisqu'il ne fait qu'appeler la fonction.

### Division d'une tâche complexe

Les fonctions sont également utiles pour diviser des tâches longues ou complexes en tâches plus petites. Le code en bénéficie de plusieurs manières, notamment en termes de lisibilité, de testabilité et de réutilisabilité.

Prenons un exemple simple : imaginez que vous prépariez un rapport. Votre code doit récupérer des données, les analyser, les filtrer et les affiner, puis exécuter une série d'algorithmes pour produire les résultats. Il est courant de voir des procédures de ce type qui ne sont qu'une seule grosse fonction `do_report(data_source)`.

Voici une meilleure approche :

```python
# data.science.example.py
def do_report(data_source):
    # Récupérer et préparer les données
    data = fetch_data(data_source)
    parsed_data = parse_data(data)
    filtered_data = filter_data(parsed_data)
    polished_data = polish_data(filtered_data)
    
    # Exécuter les algorithmes sur les données
    final_data = analyse(polished_data)
    
    # Créer et renvoyer le rapport
    report = Report(final_data)
    return report

```

### Masquer les détails d'implémentation

En parcourant le code de la fonction `do_report()`, on peut obtenir une compréhension surprenante du processus sans lire une seule ligne d'implémentation. Si nous n'avons pas besoin de plonger dans les détails, nous n'y sommes pas obligés. Cela réduit le temps passé à lire le code, ce qui est crucial dans un environnement professionnel où la lecture du code prend beaucoup plus de temps que son écriture.

### Améliorer la lisibilité

Certains programmeurs ne voient pas l'intérêt d'écrire une fonction pour une ou deux lignes de code. Comparons ces deux exemples de multiplication de matrices :

**Sans fonction :**

```python
# matrix.multiplication.nofunc.py
a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]
c = [
    [sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a
]

```

**Avec fonction :**

```python
# matrix.multiplication.func.py
def matrix_mul(a, b):
    return [
        [sum(i * j for i, j in zip(r, c)) for c in zip(*b)]
        for r in a
    ]

a = [[1, 2], [3, 4]]
b = [[5, 1], [2, 1]]
c = matrix_mul(a, b)

```

La lisibilité est grandement améliorée car nous n'avons pas besoin de déchiffrer la compréhension de liste complexe pour comprendre que `c` est le résultat de la multiplication.

---

## Portées et résolution de noms

En Python, la résolution de noms suit la règle **LEGB** (Local, Enclosing, Global, Built-in).

### Les instructions `global` et `nonlocal`

* **`nonlocal`** : Permet de modifier une variable définie dans la portée parente la plus proche (excluant la portée globale).
* **`global`** : Permet de lier un nom à la portée globale du module.

```python
# scoping.level.2.nonlocal.py
def outer():
    test = 1
    def inner():
        nonlocal test
        test = 2
        print("inner:", test)
    inner()
    print("outer:", test)

test = 0
outer()
print("global:", test)

```

*Sortie :*

```text
inner: 2
outer: 2
global: 0

```

---

## Paramètres d'entrée

Il y a trois points clés à retenir sur le passage d'arguments :

1. Le passage d'argument n'est rien d'autre que l'assignation d'un objet à un nom de variable locale.
2. L'assignation d'un objet à un nom d'argument à l'intérieur d'une fonction n'affecte pas l'appelant.
3. La modification d'un objet **mutable** passé en argument affecte l'appelant.

---
## Passage d'arguments

Examinons le code suivant. Nous déclarons un nom, `x`, dans la portée globale, puis nous déclarons une fonction, `func(y)`, et enfin, nous l'appelons en lui passant `x` :

```python
# key.points.argument.passing.py
x = 3
def func(y):
    print(y)

func(x)  # affiche : 3

```

Lorsque `func()` est appelée avec `x`, un nom `y` est créé dans sa portée locale, et celui-ci pointe vers le même objet que celui vers lequel pointe `x`. Cela est mieux clarifié dans la Figure 4.2 (ne vous inquiétez pas du fait que cet exemple ait été exécuté avec Python 3.11 ; il s'agit d'une fonctionnalité qui n'a pas changé).

Le côté droit de la Figure 4.2 illustre l'état du programme lorsque l'exécution a atteint la fin, après que `func()` a renvoyé sa valeur (`None`). Regardez la colonne **Frames** (Cadres) : nous avons deux noms, `x` et `func()`, dans l'espace de noms global (**Global frame**), pointant respectivement vers un entier (de valeur 3) et vers un objet fonction. Juste en dessous, dans le rectangle intitulé `func`, nous voyons l'espace de noms local de la fonction, dans lequel un seul nom a été défini : `y`. Puisque nous avons appelé `func()` avec `x`, `y` pointe vers le même objet que `x`.

C'est ce qui se passe sous le capot lorsqu'un argument est passé à une fonction. Si nous avions utilisé le nom `x` au lieu de `y` dans la définition de la fonction, le résultat aurait été exactement le même (bien qu'un peu confus au début) : il y aurait un `x` local dans la fonction et un `x` global à l'extérieur, comme nous l'avons vu dans la section sur les portées. En résumé, la fonction crée, dans sa portée locale, les noms définis comme paramètres et, lorsque nous l'appelons, nous indiquons à Python vers quels objets ces noms doivent pointer.

### Assignation aux noms de paramètres

L'assignation à un nom de paramètre n'affecte pas l'appelant. Cela peut être difficile à comprendre au début, alors regardons un exemple :

```python
# key.points.assignment.py
x = 3
def func(x):
    x = 7  # définition d'un x local, ne change pas le x global

func(x)
print(x)  # affiche : 3

```

Dans le code précédent, l'instruction `x = 7` est exécutée dans la portée locale de la fonction `func()`. Le nom `x` est dirigé vers un entier de valeur 7, laissant le `x` global inchangé.

### Modification d'un objet mutable

La modification d'un objet mutable affecte l'appelant. C'est important car, bien que Python semble se comporter différemment avec les objets mutables, le comportement est en réalité parfaitement cohérent :

```python
# key.points.mutable.py
x = [1, 2, 3]
def func(x):
    x[1] = 42  # ceci affecte l'argument `x` !

func(x)
print(x)  # affiche : [1, 42, 3]

```

Comme vous pouvez le voir, nous avons modifié l'objet original. Lorsque nous appelons `func(x)`, le nom `x` dans l'espace de noms de la fonction pointe vers le même objet que le `x` global. Dans le corps de la fonction, nous ne changeons pas l'objet vers lequel `x` pointe, nous accédons simplement à l'élément à la position 1 de cet objet pour modifier sa valeur.

Rappelez-vous le point n°2 de la section sur les paramètres d'entrée : l'assignation d'un objet à un nom de paramètre n'affecte pas l'appelant. Si cela est clair, le code suivant ne devrait pas vous surprendre :

```python
# key.points.mutable.assignment.py
x = [1, 2, 3]
def func(x):
    x[1] = 42  # modifie l'argument original `x` !
    x = "autre chose"  # pointe x vers un nouvel objet chaîne

func(x)
print(x)  # affiche toujours : [1, 42, 3]

```

D'abord, nous accédons à l'objet de l'appelant à la position 1 pour changer la valeur à 42. Ensuite, nous réassignons `x` pour qu'il pointe vers la chaîne 'autre chose'. Cela laisse l'appelant inchangé. Prenez le temps de tester ce concept avec la fonction `id()` jusqu'à ce que tout soit clair. Le site **Python Tutor** ([http://www.pythontutor.com/](http://www.pythontutor.com/)) vous aidera énormément grâce à ses représentations visuelles.

---

## Les différentes manières de passer des arguments

Il existe quatre façons de passer des arguments à une fonction :

* Arguments positionnels
* Arguments par mots-clés (*keyword arguments*)
* Dépaquetage d'itérables (*iterable unpacking*)
* Dépaquetage de dictionnaires (*dictionary unpacking*)

### Arguments positionnels

Chaque argument est assigné au paramètre correspondant à sa position dans la définition :

```python
# arguments.positional.py
def func(a, b, c):
    print(a, b, c)

func(1, 2, 3)  # affiche : 1 2 3

```

### Arguments par mots-clés

On utilise la syntaxe `nom=valeur`. L'ordre n'a alors plus besoin de correspondre à celui de la définition :

```python
# arguments.keyword.py
func(a=1, c=2, b=3)  # affiche : 1 3 2

```

Cela rend le code plus lisible et facile à déboguer. Vous pouvez mélanger les deux types, mais **les arguments positionnels doivent toujours être placés avant les arguments par mots-clés**. Sinon, Python lèvera une `SyntaxError`.

### Dépaquetage d'itérables et de dictionnaires

Le dépaquetage d'itérables utilise `*nom_iterable` pour passer des éléments comme arguments positionnels. Le dépaquetage de dictionnaires utilise `**nom_dictionnaire` pour les arguments par mots-clés.

```python
# arguments.unpack.iterable.py
values = (1, 3, -7)
func(*values)  # équivaut à : func(1, 3, -7)

# arguments.unpack.dict.py
values = {"b": 1, "c": 2, "a": 42}
func(**values)  # équivaut à : func(b=1, c=2, a=42)

```

### Ordre de combinaison des arguments

Lors de la combinaison, respectez cet ordre :

1. Arguments positionnels (ordinaires et dépaquetage `*`).
2. Arguments par mots-clés (ordinaires et dépaquetage `*`).
3. Dépaquetage de dictionnaires (`**`).

---

## Définition des paramètres

Les paramètres peuvent être classés en cinq groupes :

* **Positionnels ou par mots-clés** : acceptent les deux types d'arguments.
* **Positionnels variables (`*args`)** : collectent les arguments dans un tuple.
* **Mots-clés variables (`**kwargs`)** : collectent les arguments dans un dictionnaire.
* **Positionnels uniquement** : ne peuvent pas être passés par mot-clé (utilisent `/`).
* **Mots-clés uniquement** : ne peuvent pas être passés par position (utilisent `*`).

### Paramètres optionnels

Ils possèdent une valeur par défaut (`nom=valeur`). Les paramètres obligatoires doivent toujours être placés à gauche des paramètres optionnels dans la définition.

```python
# parameters.default.py
def func(a, b=4, c=88):
    print(a, b, c)

```

### Paramètres positionnels variables (`*args`)

Utiles lorsque le nombre d'arguments n'est pas fixe. À l'intérieur de la fonction, ces arguments sont accessibles via un tuple.

```python
# parameters.variable.positional.py
def minimum(*n):
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

```

### Paramètres mots-clés variables (`**kwargs`)

Similaires aux précédents, mais collectent les arguments dans un dictionnaire. C'est idéal pour passer des options de configuration, comme pour une connexion à une base de données.

---

## Paramètres positionnels uniquement (`/`) et mots-clés uniquement (`*`)

* **Positionnels uniquement** : Introduits par la PEP 570. Tout ce qui se trouve avant le symbole `/` doit être passé par position.
* **Mots-clés uniquement** : Tout ce qui se trouve après un `*` (ou après un paramètre `*args`) doit être nommé explicitement lors de l'appel.

```python
def func(a, b, /, c, *, d):
    # a, b : positionnels uniquement
    # c : positionnel ou mot-clé
    # d : mot-clé uniquement
    pass

```

---

## Le piège des valeurs par défaut mutables

**Attention :** En Python, les valeurs par défaut sont créées au moment de la définition de la fonction, pas à chaque appel. Si vous utilisez une liste vide `[]` comme valeur par défaut, elle sera partagée entre tous les appels !

**Solution recommandée :**

```python
def func(a=None):
    if a is None:
        a = []

```

---

## Valeurs de retour

Pour renvoyer une valeur, utilisez `return`. Si aucun `return` n'est présent, la fonction renvoie `None`.

### Renvoyer plusieurs valeurs

C'est très simple en Python : il suffit de renvoyer un tuple.

```python
def moddiv(a, b):
    return a // b, a % b

resultat, reste = moddiv(20, 7)

```

### Quelques conseils utiles

* **Une seule tâche** : Une fonction doit faire une seule chose.
* **Petite taille** : Plus une fonction est courte, plus elle est facile à tester.
* **Limiter les paramètres** : Trop de paramètres rendent la fonction difficile à gérer.
* **Pas d'effets de bord** : Visez des fonctions "pures" qui ne modifient pas l'état global ou les arguments d'entrée.

---
### Fonctions récursives

Lorsqu'une fonction s'appelle elle-même pour produire un résultat, on dit qu'elle est **récursive**. Les fonctions récursives sont parfois très utiles car elles simplifient l'écriture de la logique. Certains algorithmes sont très faciles à écrire par récursion, d'autres moins. Il n'existe aucune fonction récursive qui ne puisse être réécrite de manière itérative ; c'est donc généralement au programmeur de choisir la meilleure approche pour le cas présent.

Le corps d'une fonction récursive comporte généralement deux sections : une où la valeur de retour dépend d'un appel ultérieur à elle-même, et une où ce n'est pas le cas (appelée **cas de base**).

Prenons l'exemple de la fonction factorielle (). Le cas de base est lorsque  vaut 0 ou 1 : la fonction renvoie 1 sans calcul supplémentaire. Dans le cas général,  renvoie le produit :


En y réfléchissant,  peut être réécrit ainsi : . Par exemple :


Voici la traduction en code :

```python
# recursive.factorial.py
def factorial(n):
    if n in (0, 1):  # cas de base
        return 1
    return factorial(n - 1) * n  # cas récursif

```

> **Note :** Lors de l'écriture de fonctions récursives, tenez toujours compte du nombre d'appels imbriqués, car il existe une limite. Pour plus d'informations, consultez `sys.getrecursionlimit()` et `sys.setrecursionlimit()`.

---

### Fonctions anonymes (lambdas)

Un dernier type de fonction est la fonction anonyme. Appelées **lambdas** en Python, elles sont utilisées lorsqu'une fonction complète avec son propre nom serait superflue, et que nous voulons simplement une instruction rapide d'une seule ligne.

Imaginons que nous voulions une liste de tous les nombres jusqu'à  qui sont multiples de cinq. Nous pourrions utiliser la fonction `filter()`, qui nécessite une fonction et un itérable.

**Sans fonction anonyme :**

```python
# filter.regular.py
def is_multiple_of_five(n):
    return not n % 5

def get_multiples_of_five(n):
    return list(filter(is_multiple_of_five, range(n)))

```

**Avec une fonction lambda :**

```python
# filter.lambda.py
def get_multiples_of_five(n):
    return list(filter(lambda k: not k % 5, range(n)))

```

La syntaxe d'une lambda est la suivante :
`nom_func = lambda [liste_parametres]: expression`

---

### Attributs de fonction

Chaque fonction est un objet à part entière et possède plusieurs attributs. Certains sont spéciaux et permettent l'introspection de l'objet au moment de l'exécution.

```python
# func.attributes.py
def multiplication(a, b=1):
    """Renvoie a multiplié par b."""
    return a * b

if __name__ == "__main__":
    special_attributes = [
        "__doc__", "__name__", "__qualname__", "__module__",
        "__defaults__", "__code__", "__globals__", "__dict__",
        "__closure__", "__annotations__", "__kwdefaults__",
    ]
    for attribute in special_attributes:
        print(attribute, "->", getattr(multiplication, attribute))

```

L'instruction `if __name__ == "__main__":` garantit que le code qui suit n'est exécuté que si le module est lancé directement, et non s'il est importé.

---

### Documenter votre code

Nous sommes partisans d'un code auto-explicatif, mais l'ajout de **docstrings** est souvent indispensable. Les directives officielles se trouvent dans la **PEP 257**.

**Exemple d'une ligne :**

```python
def square(n):
    """Renvoie le carré d'un nombre n."""
    return n**2

```

**Exemple multiligne (format Sphinx) :**

```python
def connect(host, port, user, password):
    """Connecte à une base de données.
    
    Connecte directement à une base de données PostgreSQL en utilisant
    les paramètres fournis.
    
    :param host: L'adresse IP de l'hôte.
    :param port: Le port souhaité.
    :param user: Le nom d'utilisateur.
    :param password: Le mot de passe.
    :return: L'objet de connexion.
    """
    return connection

```

---

### Importer des objets

L'intérêt des fonctions est la réutilisation. En Python, cela passe par l'importation. Les formes les plus courantes sont :

1. `import nom_module`
2. `from nom_module import nom_fonction`

Selon la **PEP 8**, les imports doivent être groupés dans cet ordre :

1. Bibliothèque standard.
2. Bibliothèques tierces.
3. Code local.

#### Imports relatifs

Ils sont utiles lors de la restructuration de projets. On utilise des points pour remonter dans l'arborescence :
`from .mymodule import myfunc`

---

### Un dernier exemple : optimisation des nombres premiers

Optimisons la fonction de génération de nombres premiers vue au chapitre 3. Pour savoir si  est premier, il suffit de tester les diviseurs jusqu'à .

```python
# primes.py
from math import sqrt, ceil

def get_primes(n):
    """Calcule une liste de nombres premiers jusqu'à n (inclus)."""
    primelist = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = ceil(sqrt(candidate))  # limite de division
        for prime in primelist:
            if prime > root:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist

```

### Résumé

Dans ce chapitre, nous avons exploré les fonctions, piliers de la réutilisation de code et de l'encapsulation. Vous savez désormais comment les définir, les documenter, les importer et les appeler de diverses manières. Dans le prochain chapitre, nous accélérerons le rythme pour approfondir vos connaissances.
 
 
