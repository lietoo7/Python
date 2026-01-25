# POO, Décorateurs et Itérateurs

La programmation orientée objet (POO) est un sujet si vaste que des livres entiers lui ont été consacrés. Dans ce chapitre, nous sommes confrontés au défi de trouver l'équilibre entre l'étendue et la profondeur. Il y a tout simplement trop d'éléments à aborder, et beaucoup d'entre eux nécessiteraient plus qu'un chapitre entier si nous devions les décrire en profondeur. Par conséquent, nous allons essayer de vous donner ce que nous considérons comme une bonne vue panoramique des fondamentaux, ainsi que quelques notions qui pourront s'avérer utiles dans les prochains chapitres. La documentation officielle de Python aidera à combler les lacunes.

Dans ce chapitre, nous allons aborder les sujets suivants :

* **Décorateurs**
* **La POO avec Python**
* **Itérateurs**

## Décorateurs

Au chapitre 5, *Compréhensions et Générateurs*, nous avons mesuré le temps d'exécution de diverses expressions. Si vous vous souvenez bien, nous devions capturer l'heure de début et la soustraire de l'heure actuelle après l'exécution pour calculer le temps écoulé. Nous l'affichions également sur la console après chaque mesure. C'était peu pratique.

Chaque fois que nous nous retrouvons à répéter des actions, une alerte doit se déclencher. Pouvons-nous mettre ce code dans une fonction et éviter la répétition ? La plupart du temps, la réponse est oui. Regardons un exemple :

```python
# decorators/time.measure.start.py
from time import sleep, time

def f():
    sleep(0.3)

def g():
    sleep(0.5)

t = time()
f()
print("f a pris :", time() - t)  # f a pris : 0.3028...

t = time()
g()
print("g a pris :", time() - t)  # g a pris : 0.5079...

```

Dans le code précédent, nous avons défini deux fonctions, `f()` et `g()`, qui ne font rien d'autre que dormir (pendant 0,3 et 0,5 seconde, respectivement). Nous avons utilisé la fonction `sleep()` pour suspendre l'exécution pendant la durée souhaitée. Remarquez que la mesure du temps est assez précise. Maintenant, comment éviter de répéter ce code et ces calculs ? Une première approche potentielle pourrait être la suivante :

```python
# decorators/time.measure.dry.py
from time import sleep, time

def f():
    sleep(0.3)

def g():
    sleep(0.5)

def measure(func):
    t = time()
    func()
    print(func.__name__, "a pris :", time() - t)

measure(f)  # f a pris : 0.3043...
measure(g)  # g a pris : 0.5050...

```

C'est beaucoup mieux. Tout le mécanisme de chronométrage a été encapsulé dans une fonction, nous ne répétons donc pas le code. Nous affichons le nom de la fonction de manière dynamique et le code est simple. Et si nous devions passer des arguments à la fonction que nous mesurons ? Ce code deviendrait juste un peu plus complexe. Voyons un exemple :

```python
# decorators/time.measure.arguments.py
from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, "a pris :", time() - t)

measure(f, sleep_time=0.3)  # f a pris : 0.3009...
measure(f, 0.2)             # f a pris : 0.2050...

```

Désormais, `f()` s'attend à recevoir `sleep_time` (avec une valeur par défaut de 0,1), nous n'avons donc plus besoin de `g()`. Nous avons également dû modifier la fonction `measure()` pour qu'elle accepte désormais une fonction, ainsi que tous les arguments positionnels (`*args`) et par mots-clés (`**kwargs`) variables. De cette façon, quels que soient les arguments avec lesquels nous appelons `measure()`, nous les redirigeons vers l'appel à `func()` effectué à l'intérieur.

C'est une bonne chose, mais nous pouvons encore l'améliorer. Disons que nous voulons, d'une manière ou d'une autre, que ce comportement de chronométrage soit intégré à la fonction `f()`, nous permettant de l'appeler simplement et d'obtenir cette mesure. Voici comment nous pourrions procéder :

```python
# decorators/time.measure.deco1.py
from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "a pris :", time() - t)
    return wrapper

f = measure(f)  # Point de décoration
f(0.2)          # f a pris : 0.2012...
f(sleep_time=0.3) # f a pris : 0.3050...
print(f.__name__) # wrapper  <- oups !

```

Le code précédent n'est pas aussi direct. Voyons ce qui se passe ici. La magie réside dans le **point de décoration**. Nous réassignons `f()` avec ce qui est renvoyé par `measure()` lorsque nous l'appelons avec `f()` comme argument. À l'intérieur de `measure()`, nous définissons une autre fonction, `wrapper()`, puis nous la renvoyons. L'effet net est qu'après le point de décoration, lorsque nous appelons `f()`, nous appelons en réalité `wrapper()` (vous pouvez le constater à la dernière ligne du code). Comme la fonction `wrapper()` à l'intérieur appelle `func()`, qui est dans ce cas une référence à `f()`, la boucle est bouclée.

La fonction `wrapper()` est, sans surprise, une "enveloppe" (un *wrapper*). Elle prend des arguments variables et appelle `f()` avec ceux-ci, tout en effectuant le calcul de la mesure du temps autour de l'appel.

Cette technique est appelée **décoration**, et `measure()` est, en fait, un **décorateur**. Ce paradigme est devenu si populaire que Python a ajouté une syntaxe spéciale pour celui-ci à partir de la version 2.4 (PEP 318). La PEP 3129 a défini les décorateurs de classe pour Python 3.0, et enfin, Python 3.9 a légèrement assoupli certaines restrictions grammaticales (PEP 614).

### Syntaxe des décorateurs

Plutôt que de réassigner manuellement la fonction, nous faisons précéder la définition de la fonction par la syntaxe spéciale `@nom_du_decorateur`.

```python
# Cas d'un décorateur unique
@decorator
def func(arg1, arg2):
    pass

# Équivalent à :
# func = decorator(func)

```

Nous pouvons appliquer plusieurs décorateurs à la même fonction :

```python
@deco1
@deco2
def func(arg1, arg2):
    pass

# Équivalent à :
# func = deco1(deco2(func))

```

Lors de l'application de plusieurs décorateurs, il est important de prêter attention à l'ordre. Dans l'exemple précédent, `func()` est d'abord décoré par `deco2()`, et le résultat est ensuite décoré par `deco1()`. Une bonne règle de base est la suivante : **plus le décorateur est proche de la fonction, plus tôt il est appliqué.**

### Utilisation de `functools.wraps`

Comme nous l'avons vu précédemment, la décoration fait perdre à la fonction ses attributs originaux (comme `__name__` et sa *docstring*). Pour corriger cela, Python propose le décorateur `@wraps` du module `functools`.

```python
# decorators/time.measure.deco2.py
from time import sleep, time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, "a pris :", time() - t)
    return wrapper

@measure
def f(sleep_time=0.1):
    """Je suis un chat. J'adore dormir !"""
    sleep(sleep_time)

f(0.3)
print(f.__name__)  # f (correct !)
print(f.__doc__)   # Je suis un chat. J'adore dormir !

```

### Une fabrique de décorateurs (Decorator Factory)

Certains décorateurs peuvent prendre des arguments. Cette technique est généralement utilisée pour produire un autre décorateur.

```python
# decorators/decorators.factory.py
from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f"Le résultat est trop grand ({result}). Max autorisé : {threshold}.")
            return result
        return wrapper
    return decorator

@max_result(75)
def cube(n):
    return n**3

```

Ici, `max_result(75)` est d'abord appelé, ce qui renvoie la fonction `decorator`, laquelle est ensuite appliquée à `cube`. Grâce au mécanisme de **fermeture** (*closure*), la fonction interne `wrapper` conserve l'accès à la variable `threshold` (75) même après la fin de l'exécution de `max_result`.

---

## Programmation Orientée Objet (POO)

La programmation orientée objet est un paradigme basé sur le concept d'**objets**, qui sont des structures de données contenant des données (sous forme d'**attributs**) et du code (sous forme de fonctions appelées **méthodes**). Une caractéristique distinctive est que la méthode d'un objet peut accéder aux attributs de données de l'objet auquel elle est associée et souvent les modifier (les objets ont une notion de "soi" ou `self`).

Tout en Python est un objet. Les deux acteurs principaux sont les **objets** et les **classes**. Les classes servent à créer des objets ; on dit que les objets sont des **instances** de classes.

> **Analogie :** Si vous entendez le mot "stylo", vous savez quel type (ou classe) d'objet ce mot représente. Cependant, si nous disons "ce stylo", nous ne nous référons pas à une classe mais à une instance réelle de cette classe : un objet concret.

### La classe Python la plus simple

```python
# oop/simplest.class.py
class Simplest:
    pass

simp = Simplest()
print(type(simp)) # <class '__main__.Simplest'>

```

### Espaces de noms des classes et des objets

Lorsqu'un objet classe est créé, il représente un espace de noms. Chaque instance hérite des attributs et méthodes de la classe et possède son propre espace de noms. On utilise l'opérateur point (`.`) pour naviguer dans ces espaces.

```python
class Person:
    species = "Humain"

man = Person()
print(man.species)  # Humain (hérité)

man.name = "Darth"
man.surname = "Vader"
print(man.name, man.surname)  # Darth Vader

```

### Masquage d'attributs (Attribute Shadowing)

Lorsqu'un attribut n'est pas trouvé sur un objet, Python étend la recherche à sa classe. Cela crée un comportement de masquage :

```python
class Point:
    x = 10
    y = 7

p = Point()
print(p.x)  # 10 (vient de la classe)
p.x = 12    # p reçoit son propre attribut 'x'
print(p.x)  # 12 (trouvé sur l'instance)
print(Point.x) # 10 (l'attribut de classe reste inchangé)

```
 
