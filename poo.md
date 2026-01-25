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
### L'argument self

Depuis l'intérieur d'une méthode de classe, nous pouvons nous référer à une instance au moyen d'un argument spécial, appelé `self` par convention. `self` est toujours le premier attribut d'une méthode d'instance. Examinons ce comportement, ainsi que la manière dont nous pouvons partager non seulement des attributs mais aussi des méthodes avec toutes les instances :

```python
# oop/class.self.py
class Square:
    side = 8
    def area(self):  # self est une référence à une instance
        return self.side**2

sq = Square()
print(sq.area())  # 64 (side est trouvé sur la classe)
print(Square.area(sq))  # 64 (équivalent à sq.area())
sq.side = 10
print(sq.area())  # 100 (side est trouvé sur l'instance)

```

Notez comment la méthode `area()` est utilisée par `sq`. Les deux appels, `Square.area(sq)` et `sq.area()`, sont équivalents et nous enseignent le fonctionnement du mécanisme. Soit vous passez l'instance à l'appel de la méthode (`Square.area(sq)`), qui prendra le nom `self` à l'intérieur de la méthode, soit vous utilisez une syntaxe plus confortable, `sq.area()`, et Python effectuera la traduction pour vous en coulisses.

Regardons un meilleur exemple :

```python
# oop/class.price.py
class Price:
    def final_price(self, vat, discount=0):
        """Renvoie le prix après application de la TVA et d'une remise fixe."""
        return (self.net_price * (100 + vat) / 100) - discount

p1 = Price()
p1.net_price = 100
print(Price.final_price(p1, 20, 10))  # 110 (100 * 1.2 - 10)
print(p1.final_price(20, 10))  # équivalent

```

Le code précédent nous montre que rien ne nous empêche d'utiliser des arguments lors de la déclaration des méthodes. Nous pouvons utiliser exactement la même syntaxe que pour les fonctions, mais nous devons nous rappeler que le premier argument sera toujours l'instance à laquelle la méthode sera liée. Il n'est pas strictement obligatoire de l'appeler `self`, mais c'est la convention, et c'est l'un des rares cas où il est très important de s'y conformer.

### Initialisation d'une instance

Avez-vous remarqué comment, avant d'appeler `p1.final_price()` dans le code ci-dessus, nous avons dû assigner `net_price` à `p1` ? Il existe une meilleure façon de procéder. Dans d'autres langages, on appellerait cela un constructeur, mais en Python, ce n'est pas le cas. Il s'agit en réalité d'un initialisateur, car il travaille sur une instance déjà créée, et il est donc appelé `__init__()`. C'est une méthode "magique" qui est exécutée juste après la création de l'objet. Les objets Python possèdent également une méthode `__new__()`, qui est le véritable constructeur. Cependant, en pratique, il est peu courant de devoir la surcharger ; c'est une technique principalement utilisée lors de l'écriture de métaclasses. Voyons maintenant un exemple d'initialisation d'objets en Python :

```python
# oop/class.init.py
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    
    def area(self):
        return self.side_a * self.side_b

r1 = Rectangle(10, 4)
print(r1.side_a, r1.side_b)  # 10 4
print(r1.area())  # 40

r2 = Rectangle(7, 3)
print(r2.area())  # 21

```

Les choses commencent enfin à prendre forme. Lorsqu'un objet est créé, la méthode `__init__()` est exécutée pour nous automatiquement. Dans ce cas, nous l'avons écrite de sorte que lorsque nous créons un objet `Rectangle` (en appelant le nom de la classe comme une fonction), nous passons des arguments à l'appel de création, comme nous le ferions pour n'importe quel appel de fonction classique. La manière dont nous passons les paramètres suit la signature de la méthode `__init__()`. Ainsi, 10 et 4 seront `side_a` et `side_b` pour `r1`, tandis que 7 et 3 le seront pour `r2`. Vous pouvez voir que l'appel à `area()` reflète le fait que les instances ont des arguments différents. Configurer les objets de cette manière est bien plus pratique.

### La POO est une question de réutilisation de code

À présent, cela devrait être clair : la POO repose entièrement sur la réutilisation du code. Nous définissons une classe, nous créons des instances, et ces instances peuvent utiliser les méthodes définies dans la classe. Elles se comporteront différemment selon la manière dont elles ont été configurées par l'initialisateur.

### Héritage et composition

Cependant, ce n'est que la moitié de l'histoire. La POO est plus que cela. Nous avons deux structures de conception principales à notre disposition : l'héritage et la composition.

L'héritage signifie que deux objets sont liés par une relation de type "Est-Un" (**Is-A**). D'un autre côté, la composition signifie que deux objets sont liés par une relation de type "A-Un" (**Has-A**). Expliquons cela par un exemple où nous déclarons des classes pour des types de moteurs :

```python
# oop/class_inheritance.py
class Engine:
    def start(self):
        pass
    def stop(self):
        pass

class ElectricEngine(Engine):  # Est-Un Engine
    pass

class V8Engine(Engine):  # Est-Un Engine
    pass

```

Ensuite, nous déclarons des types de voitures qui utiliseront ces moteurs :

```python
class Car:
    engine_cls = Engine
    def __init__(self):
        self.engine = self.engine_cls()  # A-Un Engine
    
    def start(self):
        print(
            f"Démarrage de {self.engine.__class__.__name__} pour "
            f"{self.__class__.__name__}... Vroum, vroum !"
        )
        self.engine.start()
    
    def stop(self):
        self.engine.stop()

class RaceCar(Car):  # Est-Une Car
    engine_cls = V8Engine

class CityCar(Car):  # Est-Une Car
    engine_cls = ElectricEngine

class F1Car(RaceCar):  # Est-Une RaceCar et aussi Est-Une Car
    pass  # engine_cls identique au parent

```

L'exécution de ce code produit le résultat suivant :

```bash
$ python class_inheritance.py
Démarrage de Engine pour Car... Vroum, vroum !
Démarrage de V8Engine pour RaceCar... Vroum, vroum !
Démarrage de ElectricEngine pour CityCar... Vroum, vroum !
Démarrage de V8Engine pour F1Car... Vroum, vroum !

```

L'exemple précédent illustre les deux types de relations. Considérons d'abord `Engine`. C'est une classe simple avec deux méthodes. Nous définissons ensuite `ElectricEngine` et `V8Engine`, qui en héritent toutes deux. Cela signifie qu'elles héritent des attributs et méthodes de la classe `Engine`, appelée leur classe de base (ou classe parente).

Il en va de même pour les voitures. `Car` est une classe de base pour `RaceCar` et `CityCar`. `RaceCar` est également la classe de base de `F1Car`. En d'autres termes, `F1Car` hérite de `RaceCar`, qui hérite de `Car`. Par transitivité, `F1Car` "Est-Une" `Car`.

Lorsqu'on définit `class A(B): pass`, on dit que A est l'enfant de B, et B le parent de A. Les termes classe parente et classe de base sont synonymes, tout comme enfant de et dérivée de. On dit aussi qu'une classe hérite d'une autre, ou qu'elle l'étend. C'est le mécanisme d'héritage.

Revenons au code. Chaque classe possède un attribut de classe, `engine_cls`, qui fait référence à la classe de moteur que nous voulons assigner à chaque type de voiture. Lors de l'initialisation (`__init__()`), nous créons une instance de la classe de moteur correspondante.

Il est logique de partager `engine_cls` entre toutes les instances de classe car il est probable que toutes les instances d'un même modèle de voiture aient le même type de moteur. En revanche, il ne serait pas correct d'avoir une seule instance de moteur comme attribut de classe, car cela reviendrait à partager un seul et même moteur physique entre toutes les voitures.

La relation entre une voiture et son moteur est de type "A-Un". Une voiture "A-Un" moteur. C'est ce qu'on appelle la **composition**, reflétant le fait que les objets peuvent être composés de nombreux autres objets (moteur, roues, sièges, etc.).

> **Note :** Nous avons évité les points dans le nom du fichier `class_inheritance.py`, car les points dans les noms de modules rendent les imports difficiles. En général, évitez les points dans vos noms de modules.

Vérifions la validité de nos affirmations avec la fonction `isinstance()` :

```python
# oop/class.issubclass.isinstance.py
from class_inheritance import Car, RaceCar, F1Car

car = Car()
racecar = RaceCar()
f1car = F1Car()

# Vérification des instances
# f1car est une instance de F1Car, mais aussi de RaceCar et de Car.
belongs = isinstance(f1car, Car) # True

```

Enfin, vérifions l'héritage avec `issubclass()`. On y apprend notamment qu'une classe est considérée comme une sous-classe d'elle-même.

> **Convention :** Les noms de classes s'écrivent en **CapWords** (`CommeCeci`), tandis que les fonctions et méthodes s'écrivent en **snake_case** (`comme_cela`). Si un nom entre en conflit avec un mot-clé réservé, la convention est d'ajouter un souligné à la fin (ex: `class_`).

---
## Accéder à une classe de base

Nous avons déjà vu des déclarations de classes telles que `class ClasseA: pass` et `class ClasseB(NomClasseBase): pass`. Lorsque nous ne spécifions pas explicitement une classe de base, Python définit la classe intégrée `object` comme classe de base. En fin de compte, toutes les classes dérivent de `object`. N'oubliez pas que si vous ne spécifiez pas de classe de base, les parenthèses sont facultatives et, en pratique, ne sont jamais utilisées. Par conséquent, écrire `class A: pass`, `class A(): pass` ou `class A(object): pass` est strictement équivalent. La classe `object` est spéciale car elle héberge les méthodes communes à toutes les classes Python et ne vous permet pas de définir des attributs sur elle-même.

Voyons comment accéder à une classe de base depuis l'intérieur d'une classe :

```python
# oop/super.duplication.py
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        self.title = title
        self.publisher = publisher
        self.pages = pages
        self.format_ = format_

```

Observez le code précédent. Trois des paramètres d'entrée de `Book` sont dupliqués dans `Ebook`. C'est une mauvaise pratique car nous avons maintenant deux ensembles d'instructions qui font la même chose. De plus, tout changement dans la signature de `Book.__init__()` ne sera pas répercuté dans `Ebook`. Normalement, nous voulons que les modifications d'une classe de base soient reflétées chez ses enfants. Voici une façon de corriger ce problème :

```python
# oop/super.explicit.py
class Book:
    def __init__(self, title, publisher, pages):
        self.title = title
        self.publisher = publisher
        self.pages = pages

class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        Book.__init__(self, title, publisher, pages)
        self.format_ = format_

ebook = Ebook("Learn Python Programming", "Packt Publishing", 500, "PDF")
print(ebook.title)  # Learn Python Programming

```

C'est bien mieux. Nous avons supprimé la duplication de code. Dans cet exemple, nous demandons à Python d'appeler la méthode `__init__()` de la classe `Book` ; nous passons `self` à cet appel pour nous assurer de le lier à l'instance actuelle. Cependant, cette approche nécessite toujours de modifier `Ebook` si nous renommons la classe `Book`. Pour éviter cela, on utilise `super()` :

```python
# oop/super.implicit.py
class Ebook(Book):
    def __init__(self, title, publisher, pages, format_):
        super().__init__(title, publisher, pages)
        self.format_ = format_

```

`super()` est une fonction qui renvoie un objet proxy déléguant les appels de méthode à une classe parente ou sœur.

---

## Héritage multiple

En Python, il est possible de définir des classes qui héritent de plus d'une classe de base. C'est ce qu'on appelle l'**héritage multiple**.

```python
# oop/multiple.inheritance.py
class Shape:
    geometric_type = "Forme Générique"
    def area(self):
        raise NotImplementedError
    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        print("Tracé à {}, ratio {}.".format(topleft, ratio))

class Polygon(Shape, Plotter):
    geometric_type = "Polygone"

class RegularPolygon(Polygon):
    def __init__(self, side):
        self.side = side

class Square(RegularPolygon):
    geometric_type = "Carré"
    def area(self):
        return self.side * self.side

square = Square(12)
print(square.area())  # 144
square.plot(0.93, (74, 75))  # Tracé à (74, 75), ratio 0.93.

```

L'héritage multiple permet d'enrichir vos objets avec des capacités variées. Cette technique est très populaire dans les frameworks web comme Django, qui utilise des **mixins** (des classes spéciales dont on peut utiliser les capacités immédiatement en les ajoutant comme classes de base).

---

## Ordre de résolution des méthodes (MRO)

Lorsqu'un attribut n'est pas trouvé sur un objet, Python cherche dans sa classe, puis remonte la chaîne d'héritage. Avec l'héritage multiple, Python utilise l'algorithme **C3** pour déterminer l'**Ordre de Résolution des Méthodes (MRO)**.

Vous pouvez consulter le MRO d'une classe via l'attribut `__mro__` :

```python
print(Square.__mro__)
# (<class 'Square'>, <class 'RegularPolygon'>, <class 'Polygon'>, 
#  <class 'Shape'>, <class 'Plotter'>, <class 'object'>)

```

En cas de conflit (si deux parents possèdent le même attribut), Python suit l'ordre défini dans le MRO, en privilégiant généralement la classe la plus à gauche dans la déclaration d'héritage.

---

## Méthodes de classe et méthodes statiques

Outre les méthodes d'instance classiques, il existe deux autres types de méthodes :

### Méthodes statiques

Elles sont créées avec le décorateur `@staticmethod`. Elles ne reçoivent pas d'instance (`self`) en argument et se comportent comme des fonctions normales regroupées sous l'espace de noms de la classe.

```python
# oop/static.methods.py
class StringUtil:
    @staticmethod
    def is_palindrome(s):
        s = "".join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]

print(StringUtil.is_palindrome("Radar"))  # True

```

### Méthodes de classe

Décorées avec `@classmethod`, elles reçoivent la classe elle-même (`cls`) comme premier argument. Elles sont souvent utilisées comme **factories** pour créer des instances de différentes manières.

```python
# oop/class.methods.factory.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        return cls(*coords)

p = Point.from_tuple((3, 7))

```

L'utilisation de `cls` plutôt que du nom de la classe en dur (ex: `Point`) permet de rendre le code plus robuste en cas de renommage de la classe ou d'héritage.

---

### Méthodes privées et masquage de noms (*name mangling*)

Si vous avez de l'expérience avec des langages comme Java, C# ou C++, vous savez qu'ils permettent au programmeur d'assigner un statut de confidentialité aux attributs (données et méthodes). Chaque langage a sa propre variante, mais l'idée principale est que les attributs publics sont accessibles de n'importe quel point du code, tandis que les attributs privés ne sont accessibles que dans la portée où ils sont définis.

En Python, cela n'existe pas. Tout est public ; par conséquent, nous nous appuyons sur des conventions et, pour la confidentialité, sur un mécanisme appelé **masquage de noms** (*name mangling*).

La convention est la suivante : si le nom d'un attribut ne comporte aucun soulignement (*underscore*) au début, il est considéré comme **public**. Cela signifie que vous pouvez y accéder et le modifier librement. Lorsque le nom commence par **un seul soulignement** (`_`), l'attribut est considéré comme **privé**, ce qui signifie qu'il est destiné à un usage interne : vous ne devriez pas le modifier ou l'appeler depuis l'extérieur. Un cas d'utilisation courant est celui des méthodes d'assistance (*helper methods*) destinées à être utilisées par des méthodes publiques. Un autre cas concerne les données internes que nous souhaiterions idéalement placer dans une constante, car Python n'a pas de concept de constante réelle.

Certains programmeurs ne sont pas à l'aise avec cet aspect de Python. Cependant, c'est une question de discipline et de respect des conventions. La liberté offerte par Python est la raison pour laquelle il est parfois qualifié de « langage pour adultes ».

Cela dit, le besoin de confidentialité fait sens, car sans elle, vous risquez d'introduire de réels bugs. En voici la preuve :

```python
# oop/private.attrs.py
class A:
    def __init__(self, factor):
        self._factor = factor
    def op1(self):
        print("Op1 avec le facteur {}...".format(self._factor))

class B(A):
    def op2(self, factor):
        self._factor = factor
        print("Op2 avec le facteur {}...".format(self._factor))

obj = B(100)
obj.op1()   # Op1 avec le facteur 100...
obj.op2(42) # Op2 avec le facteur 42...
obj.op1()   # Op1 avec le facteur 42...  <- C'est MAUVAIS

```

Ici, `op2` modifie `_factor`, ce qui impacte `op1`. Nous pouvons corriger cela en ajoutant un **deuxième soulignement** au début :

```python
# oop/private.attrs.fixed.py
class A:
    def __init__(self, factor):
        self.__factor = factor
    def op1(self):
        print("Op1 avec le facteur {}...".format(self.__factor))

class B(A):
    def op2(self, factor):
        self.__factor = factor
        print("Op2 avec le facteur {}...".format(self.__factor))

obj = B(100)
obj.op1()   # Op1 avec le facteur 100...
obj.op2(42) # Op2 avec le facteur 42...
obj.op1()   # Op1 avec le facteur 100...  <- Maintenant c'est bon !

```

C'est ici qu'intervient le **masquage de noms** (*name mangling*). Tout attribut commençant par au moins deux soulignements et se terminant par au plus un soulignement (ex: `__mon_attr`) est remplacé par un nom incluant le nom de la classe : `_NomClasse__mon_attr`. Cela évite les collisions de noms lors de l'héritage.

---

### Le décorateur `property`

Imaginez que vous ayez un attribut `age` dans une classe `Person` et que vous vouliez vérifier que sa valeur est comprise entre [18, 99]. Dans d'autres langages, vous écririez des méthodes d'accès (*getters* et *setters*) comme `get_age()` et `set_age()`.

Python obtient le même résultat avec le décorateur `@property`. Il permet d'utiliser une méthode comme s'il s'agissait d'un attribut de données.

```python
# oop/property.py
class PersonPythonic:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 18 <= age <= 99:
            self._age = age
        else:
            raise ValueError("L'âge doit être compris entre [18, 99]")

person = PersonPythonic(39)
print(person.age)  # 39 - Accès comme un attribut
person.age = 42    # Modification comme un attribut

```

Contrairement aux langages imposant le paradigme getter/setter par défaut, Python vous permet de commencer par un code simple et de le refactoriser plus tard sans casser l'interface de votre classe.

---

### Le décorateur `cached_property`

Parfois, la création d'un attribut est coûteuse (par exemple, se connecter à une base de données). Si nous utilisons une `@property` classique qui crée une nouvelle instance à chaque appel, nous gaspillons des ressources.

Introduit dans Python 3.8, `cached_property` permet de ne calculer la valeur qu'une seule fois et de la mettre en cache :

```python
# oop/cached.property.py
from functools import cached_property

class CachedPropertyManager:
    @cached_property
    def client(self):
        print("Configuration du client...")
        return Client()

manager = CachedPropertyManager()
manager.client  # Affiche "Configuration du client..."
manager.client  # Ne réaffiche rien, utilise le cache
del manager.client  # Supprime le cache
manager.client  # Recrée un nouveau client

```

---

### Surcharge d'opérateurs (*Operator Overloading*)

La surcharge d'opérateurs consiste à donner un sens à un opérateur selon son contexte (ex: `+` additionne des nombres mais concatène des listes). Python appelle des **méthodes spéciales** (ou méthodes "magiques") en coulisses. Par exemple, `a[k]` appelle `__getitem__`.

Voici un exemple où nous redéfinissons la longueur et le comportement booléen d'une classe :

```python
# oop/operator.overloading.py
class Weird:
    def __init__(self, s):
        self._s = s
    def __len__(self):
        return len(self._s)
    def __bool__(self):
        return "42" in self._s

weird = Weird("Bonjour ! J'ai 42 ans !")
print(len(weird))   # 25
print(bool(weird))  # True

```

Consultez le "Data Model" de la documentation officielle pour obtenir la liste complète des méthodes magiques utilisables.

---

### Polymorphisme : un bref aperçu

Le mot polymorphisme vient du grec *polys* (plusieurs, beaucoup) et *morphē* (forme, figure). Sa signification est la fourniture d'une interface unique pour des entités de types différents.

Dans notre exemple de voiture, nous appelons `engine.start()`, quel que soit le type de moteur. Tant qu'il expose la méthode `start`, nous pouvons l'appeler. C'est le polymorphisme en action.

Dans d'autres langages, comme Java, pour donner à une fonction la capacité d'accepter différents types et d'appeler une méthode sur ceux-ci, ces types doivent être codés de manière à partager une interface. De cette façon, le compilateur sait que la méthode sera disponible quel que soit le type de l'objet fourni à la fonction (tant qu'il étend l'interface spécifique, bien entendu).

En Python, les choses sont différentes. Le polymorphisme est implicite et rien ne vous empêche d'appeler une méthode sur un objet ; par conséquent, techniquement, il n'est pas nécessaire d'implémenter des interfaces ou d'autres patrons de conception.

Il existe un type spécial de polymorphisme appelé *polymorphisme ad hoc*, que nous avons vu dans la section précédente sur la surcharge d'opérateurs. Il s'agit de la capacité d'un opérateur à changer de forme selon le type de données auxquelles il est appliqué.

Le polymorphisme permet également aux programmeurs Python d'utiliser simplement l'interface (méthodes et propriétés) exposée par un objet, plutôt que de devoir vérifier de quelle classe il a été instancié. Cela permet au code d'être plus compact et de paraître plus naturel.

Nous ne pouvons pas consacrer trop de temps au polymorphisme, mais nous vous encourageons à l'étudier par vous-même ; cela enrichira votre compréhension de la POO.

### Les classes de données (Data classes)

Avant de quitter le domaine de la POO, il reste une dernière chose que nous souhaitons mentionner : les *data classes*. Introduites dans Python 3.7 par la PEP 557, elles peuvent être décrites comme des tuples nommés mutables avec des valeurs par défaut. Vous pouvez réviser les tuples nommés au Chapitre 2. Plongeons directement dans un exemple :

```python
# oop/dataclass.py
from dataclasses import dataclass

@dataclass
class Body:
    """Classe représentant un corps physique."""
    name: str
    mass: float = 0.0  # Kg
    speed: float = 1.0  # m/s

    def kinetic_energy(self) -> float:
        return (self.mass * self.speed**2) / 2

body = Body("Ball", 19, 3.1415)
print(body.kinetic_energy())  # 93.755711375 Joule
print(body)  # Body(name='Ball', mass=19, speed=3.1415)

```

> **Note :** Une autre chose à remarquer est la façon dont `name`, `mass` et `speed` sont définis. Cette technique s'appelle l'**annotation de type** (*type hinting*) et fera l'objet du Chapitre 12.

Dans le code précédent, nous avons créé une classe pour représenter un corps physique, avec une méthode permettant de calculer son énergie cinétique (via la formule ). Notez que `name` est censé être une chaîne de caractères, tandis que `mass` et `speed` sont des flottants disposant d'une valeur par défaut. Il est également intéressant de constater que nous n'avons pas eu à écrire de méthode `__init__()` ; elle est générée pour nous par le décorateur `@dataclass`, tout comme les méthodes de comparaison et de représentation textuelle de l'objet (appelée implicitement sur la dernière ligne par `print`).

---

### Écrire un itérateur personnalisé

Nous avons maintenant tous les outils pour comprendre comment écrire notre propre itérateur. Définissons d'abord les termes *itérable* et *itérateur* :

* **Itérable :** Un objet est dit itérable s'il peut renvoyer ses membres un par un. Les listes, les tuples, les chaînes et les dictionnaires sont tous des itérables. Les objets personnalisés définissant l'une des méthodes `__iter__()` ou `__getitem__()` sont également des itérables.
* **Itérateur :** Un objet est dit itérateur s'il représente un flux de données. Un itérateur personnalisé doit fournir une implémentation de la méthode `__iter__()` qui renvoie l'objet lui-même, ainsi qu'une implémentation de la méthode `__next__()` qui renvoie l'élément suivant du flux jusqu'à ce que celui-ci soit épuisé. À ce stade, tout appel successif à `__next__()` doit lever une exception `StopIteration`.

Écrivons un itérateur qui renvoie d'abord tous les caractères d'indice pair d'une chaîne, puis les caractères d'indice impair :

```python
# iterators/iterator.py
class OddEven:
    def __init__(self, data):
        self._data = data
        # Préparation des indices : pairs puis impairs
        self.indexes = list(range(0, len(data), 2)) + list(
            range(1, len(data), 2)
        )

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration

oddeven = OddEven("0123456789")
print("".join(c for c in oddeven))  # 0246813579

# Ou manuellement...
oddeven = OddEven("ABCD")
it = iter(oddeven)  # Appelle oddeven.__iter__ en interne
print(next(it))  # A
print(next(it))  # C
print(next(it))  # B
print(next(it))  # D

```

> **Note :** Les exceptions seront traitées au Chapitre 7. Elles peuvent représenter des erreurs, mais servent aussi à réguler le flux d'exécution, comme pour le protocole d'itération de Python.

Nous fournissons donc une implémentation pour `__iter__()` qui renvoie l'objet lui-même, et une pour `__next__()`. Pour ce faire, nous préparons une liste d'indices et, tant qu'il reste au moins un élément dans la liste, nous extrayons le premier (`pop(0)`) et renvoyons l'élément correspondant dans les données. Lorsque `indexes` est vide, nous levons `StopIteration`.

### Résumé

Dans ce chapitre, nous avons étudié les décorateurs, découvert leur utilité et analysé plusieurs exemples. Nous avons également vu les décorateurs acceptant des arguments, souvent utilisés comme fabriques de décorateurs.

Nous avons exploré les fondements de la POO en Python : méthodes et attributs de classe, héritage versus composition, surcharge de méthodes, propriétés, surcharge d'opérateurs et polymorphisme. Enfin, nous avons brièvement abordé les itérateurs.

 
 
