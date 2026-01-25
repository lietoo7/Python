# Types de Données Intégrés

Tout ce que vous faites avec un ordinateur revient à gérer des données. Les données se présentent sous de nombreuses formes et saveurs. Il s'agit de la musique que vous écoutez, des films que vous regardez en streaming, des PDF que vous ouvrez. Même la source du chapitre que vous lisez en ce moment même n'est qu'un fichier, c'est-à-dire une donnée.
Les données peuvent être simples, comme un nombre entier pour représenter un âge, ou structurées et complexes, comme une commande passée sur un site web. Elles peuvent concerner un objet unique ou une collection d'objets. Les données peuvent même porter sur d'autres données : c'est ce qu'on appelle les **métadonnées**. Ce sont des données qui décrivent la conception d'autres structures de données, ou qui décrivent les données d'une application ou leur contexte.
En Python, les **objets** sont une abstraction pour les données. Python possède une variété impressionnante de structures de données que vous pouvez utiliser pour représenter des informations ou les combiner pour créer vos propres données personnalisées.

Dans ce chapitre, nous allons aborder les points suivants :

* La structure des objets Python
* La mutabilité et l'immutabilité
* Les types de données intégrés : nombres, chaînes de caractères (strings), dates et heures, séquences, collections et types de correspondance (mapping)
* Le module `collections` (brièvement)
* Les énumérations

---

## Tout est un objet

Avant d'entrer dans les détails, nous voulons que vous soyez très au clair sur les objets en Python. Tout en Python est un objet, et chaque objet possède une **identité (ID)**, un **type** et une **valeur**. Mais que se passe-t-il réellement lorsque vous tapez une instruction comme `age = 42` dans un module Python ?
> **Conseil :** Si vous vous rendez sur [https://pythontutor.com/](https://pythontutor.com/), vous pouvez taper cette instruction et obtenir sa représentation visuelle. Gardez ce site en mémoire ; il est très utile pour consolider votre compréhension de ce qui se passe en coulisses.
Ce qui se passe, c'est qu'un objet est créé. Il reçoit un ID, son type est défini sur `int` (nombre entier) et sa valeur sur `42`. Un nom, `age`, est placé dans l'espace de noms global (global namespace), pointant vers cet objet. Par conséquent, chaque fois que nous sommes dans l'espace de noms global après l'exécution de cette ligne, nous pouvons récupérer cet objet simplement en y accédant via son nom : `age`.
Si vous déménagiez, vous mettriez tous les couteaux, fourchettes et cuillères dans une boîte étiquetée "couverts". C'est exactement le même concept. Pour le reste de ce chapitre, chaque fois que vous lirez quelque chose comme `nom = valeur`, imaginez un nom placé dans l'espace de noms lié à la portée (scope) dans laquelle l'instruction a été écrite, avec une flèche pointant vers un objet qui possède un ID, un type et une valeur.

---

## Mutabilité

La première distinction fondamentale que Python fait concernant les données est de savoir si la valeur d'un objet peut changer. Si la valeur peut changer, l'objet est dit **mutable**, sinon l'objet est dit **immutable**.
Il est important de comprendre cette distinction car elle affecte le code que vous écrivez. Examinons l'exemple suivant :
```python
>>> age = 42
>>> age
42
>>> age = 43  # A
>>> age
43

```

Dans le code précédent, à la ligne #A, avons-nous changé la valeur d'age ? Eh bien, non. Pourtant, c'est maintenant 43... Oui, c'est 43, mais 42 était un nombre entier de type `int`, qui est **immutable**.
Ce qui s'est réellement passé, c'est qu'à la première ligne, `age` est un nom configuré pour pointer vers un objet `int` dont la valeur est 42. Lorsque nous tapons `age = 43`, un autre objet `int` est créé avec la valeur 43 (son ID sera également différent), et le nom `age` est configuré pour pointer vers lui. Nous n'avons pas transformé 42 en 43 ; nous avons juste pointé le nom `age` vers un nouvel emplacement. Vérifions les identifiants (IDs) :

```python
>>> age = 42
>>> id(age)
4377553168
>>> age = 43
>>> id(age)
4377553200

```

Notez que nous utilisons la fonction intégrée `id()`. Les IDs sont différents, comme prévu. `age` pointe vers un seul objet à la fois.
Voyons maintenant le même exemple avec un objet **mutable**, en utilisant le type `set` (ensemble) :

```python
>>> numbers = set()
>>> id(numbers)
4368427136
>>> numbers
set()
>>> numbers.add(3)
>>> numbers.add(7)
>>> id(numbers)
4368427136
>>> numbers
{3, 7}

```

Ici, l'ID reste le même avant et après l'ajout de nombres. La valeur de l'objet a changé, mais son identité demeure. C'est le comportement typique d'un objet mutable.

---

## Nombres

Python a été conçu par un mathématicien, il est donc logique qu'il offre un support étendu pour les nombres. Les nombres sont des objets **immutables**.

### Entiers (Integers)

Les entiers en Python ont une portée illimitée, sous réserve de la mémoire virtuelle disponible. Ils peuvent être positifs, négatifs ou nuls (0). Leur type est `int`.

```python
>>> a = 14
>>> b = 3
>>> a + b  # addition
17
>>> a - b  # soustraction
11
>>> a * b  # multiplication
42
>>> a / b  # division réelle
4.666666666666667
>>> a // b # division entière (quotient)
4
>>> a % b  # modulo (reste de la division)
2
>>> a ** b # puissance
2744

```

**Note sur la division :** Python propose la division réelle (`/`) et la division entière (`//`). Pour les nombres négatifs, la division entière est toujours arrondie vers moins l'infini.

### Booséens (Booleans)

En Python, `True` (Vrai) et `False` (Faux) sont des mots-clés représentant les valeurs de vérité. Les booséens sont une sous-classe des entiers : `True` se comporte comme 1 et `False` comme 0.

### Nombres réels (Floats)

Représentés selon la norme IEEE 754 en double précision (64 bits). Attention aux problèmes d'approximation :

```python
>>> 0.3 - 0.1 * 3
-5.551115123125783e-17 # Au lieu de 0.0 !

```

Pour une précision absolue (finance, science), utilisez le type `Decimal`.

### Nombres complexes

Python supporte les nombres complexes sous la forme `a + bj`.

```python
>>> c = 3.14 + 2.73j
>>> c.real
3.14
>>> c.imag
2.73

```

### Fractions et Décimaux

Le module `fractions` permet de manipuler des nombres rationnels :

```python
>>> from fractions import Fraction
>>> Fraction(10, 6)
Fraction(5, 3) # Simplification automatique

```

Le type `Decimal` est préférable pour les calculs monétaires où l'approximation des nombres flottants est inacceptable.

---

## Séquences Immutables

### Chaînes de caractères (Strings) et Bytes

Les objets `str` sont des séquences immutables de points de code Unicode.

* **Déclaration** : Utilisation de guillemets simples (`'`), doubles (`"`) ou triples (`'''` ou `"""`) pour les chaînes multilignes.
* **Méthodes utiles** (Python 3.9+) : `removeprefix()` et `removesuffix()`.
* **Encodage** : `s.encode("utf-8")` transforme une chaîne en objet `bytes`.

### Indexation et Slicing

L'accès aux éléments se fait par index (commençant à 0). Le "slicing" permet d'extraire des sous-séquences : `ma_sequence[début:fin:pas]`.

```python
>>> s = "The trouble is you think you have time."
>>> s[0]
'T'
>>> s[:4]
'The '

```

### Formatage de chaînes

Il existe plusieurs méthodes, mais les **f-strings** (introduites en Python 3.6) sont les plus modernes et rapides :

```python
>>> name = "Fab"
>>> age = 48
>>> f"Hello! My name is {name} and I'm {age}"
"Hello! My name is Fab and I'm 48"

```

Python 3.8 a ajouté le spécificateur `=` (ex: `{user=}`) pour faciliter le débogage.

### Tuples

Un tuple est une séquence d'objets arbitraires séparés par des virgules. Ils sont souvent utilisés pour retourner plusieurs valeurs d'une fonction ou pour des assignations multiples :

```python
>>> a, b = 1, 2
>>> a, b = b, a # Échange de variables en une ligne (Pythonique)

```
---

Souhaitez-vous que je poursuive la traduction avec la section sur le module `collections` ou que j'approfondisse un exemple spécifique de cet extrait ?
