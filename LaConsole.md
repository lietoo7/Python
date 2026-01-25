# La console Python

Nous utiliserons le terme « console » de manière interchangeable pour désigner la console Linux, l'invite de commande Windows (ou PowerShell) et le Terminal macOS. Nous indiquerons également l'invite de commande avec le format Linux par défaut, comme ceci :
`$ sudo apt-get update`
Si vous n'êtes pas familier avec cela, veuillez prendre le temps d'apprendre les bases du fonctionnement d'une console. En résumé, après le signe `$`, vous taperez vos instructions. Portez une attention particulière à la casse (majuscules/minuscules) et aux espaces, car ils sont très importants.
Quelle que soit la console que vous ouvrez, tapez `python` à l'invite (`py` sous Windows) et assurez-vous que le shell interactif Python apparaît. Tapez `exit()` pour quitter. Gardez à l'esprit que vous devrez peut-être spécifier `python3` ou `python3.12` si votre système d'exploitation est livré avec d'autres versions de Python préinstallées.
> Nous appelons souvent le shell interactif Python simplement la **console Python**.
Voici approximativement ce que vous devriez voir lorsque vous lancez Python (certains détails changeront selon la version et le système d'exploitation) :

```bash
$ python
Python 3.12.2 (main, Feb 14 2024, 14:16:36)
[Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

Maintenant que Python est configuré et que vous pouvez l'exécuter, il est temps de vous assurer que vous disposez de l'autre outil indispensable pour suivre les exemples de ce livre : **un environnement virtuel**.

## À propos des environnements virtuels
Lorsqu'on travaille avec Python, il est très courant d'utiliser des environnements virtuels. Voyons ce qu'ils sont et pourquoi nous en avons besoin à l'aide d'un exemple simple.
Imaginez que vous installiez Python sur votre système et que vous commenciez à travailler sur un site Web pour un client X. Vous créez un dossier de projet et commencez à coder. En chemin, vous installez également des bibliothèques, par exemple le framework Django. Disons que la version de Django que vous avez installée pour le Projet X est la **4.2**.
Maintenant, votre site Web est si performant que vous obtenez un autre client, Y. Elle souhaite que vous construisiez un autre site. Vous commencez donc le Projet Y et vous devez à nouveau installer Django. Le seul problème est que la version actuelle de Django est désormais la **5.0** et vous ne pouvez pas l'installer globalement sur votre système, car cela remplacerait la version installée pour le Projet X. Vous ne voulez pas risquer d'introduire des problèmes d'incompatibilité. Vous avez donc deux choix : soit vous restez avec la version actuelle de votre machine, soit vous la mettez à jour en vous assurant que le premier projet fonctionne toujours correctement avec la nouvelle version.
Soyons honnêtes : aucune de ces options n'est très séduisante, n'est-ce pas ? Absolument pas. Mais il existe une solution : les environnements virtuels !
Les environnements virtuels sont des **environnements Python isolés**, chacun étant un dossier contenant tous les exécutables nécessaires pour utiliser les paquets dont un projet Python aurait besoin (considérez les paquets comme des bibliothèques pour le moment).
Ainsi, vous créez un environnement virtuel pour le Projet X, installez toutes les dépendances, puis vous créez un environnement virtuel pour le Projet Y et installez toutes ses dépendances sans la moindre inquiétude, car chaque bibliothèque que vous installez finit dans les limites de l'environnement virtuel approprié. Dans notre exemple, le Projet X conservera Django 4.2, tandis que le Projet Y conservera Django 5.0.
> **Important** : Il est d'une importance capitale de ne jamais installer de bibliothèques directement au niveau du système. Linux, par exemple, s'appuie sur Python pour de nombreuses tâches et opérations ; si vous modifiez l'installation système de Python, vous risquez de compromettre l'intégrité de l'ensemble du système. Prenez donc ceci comme une règle : **créez toujours un environnement virtuel lorsque vous commencez un nouveau projet.**
Pour créer un environnement virtuel sur votre système, il existe plusieurs méthodes. Depuis Python 3.5, la méthode suggérée est d'utiliser le module `venv`. Vous pouvez consulter la page de documentation officielle ([https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)) pour plus d'informations.
Si vous utilisez une distribution Linux basée sur Debian, par exemple, vous devrez installer le module `venv` avant de pouvoir l'utiliser :

`$ sudo apt-get install python3.12-venv`

Une autre façon courante de créer des environnements virtuels est d'utiliser le paquet tiers `virtualenv`. Vous pouvez le trouver sur son site officiel : [https://virtualenv.pypa.io](https://virtualenv.pypa.io).
Dans ce livre, nous utiliserons la technique recommandée, qui exploite le module `venv` de la bibliothèque standard de Python.

## Votre premier environnement virtuel

Il est très facile de créer un environnement virtuel, mais selon la configuration de votre système et la version de Python que vous souhaitez utiliser, vous devez exécuter la commande correctement. Une autre chose que vous devrez faire lorsque vous voudrez travailler avec, c'est de **l'activer**.
L'activation des environnements virtuels produit une manipulation des chemins d'accès (« path juggling ») en arrière-plan afin que, lorsque vous appelez l'interpréteur Python depuis ce shell, il provienne de l'intérieur de l'environnement virtuel et non du système. Nous allons vous montrer un exemple complet sur macOS et Windows (sur Linux, ce sera très similaire à macOS). Nous allons :

1. Ouvrir un terminal et se déplacer dans le dossier racine de nos projets (notre dossier s'appelle `code`). Nous allons créer un nouveau dossier appelé `my-project` et y entrer.
2. Créer un environnement virtuel appelé `lpp4ed`.
3. Activer l'environnement virtuel après sa création (les méthodes diffèrent légèrement entre Linux, macOS et Windows).
4. Vérifier que nous utilisons la version de Python souhaitée (3.12.X) en lançant le shell interactif.
5. Enfin, désactiver l'environnement virtuel.

Voici l'exemple sur **macOS** (notez que vous pourriez obtenir un résultat légèrement différent selon votre OS et version) :

```bash
fab@m1:~/code$ mkdir my-project  # étape 1
fab@m1:~/code$ cd my-project
fab@m1:~/code/my-project$ which python3.12  # vérification python système
/usr/bin/python3.12  # <-- python3.12 du système
fab@m1:~/code/my-project$ python3.12 -m venv lpp4ed  # étape 2
fab@m1:~/code/my-project$ source ./lpp4ed/bin/activate  # étape 3
# vérification à nouveau : utilise maintenant celui de l'env virtuel
(lpp4ed) fab@m1:~/code/my-project$ which python
/Users/fab/code/my-project/lpp4ed/bin/python
(lpp4ed) fab@m1:~/code/my-project$ python  # étape 4
Python 3.12.2 (main, Feb 14 2024, 14:16:36)
[Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
>>> exit()
(lpp4ed) fab@m1:~/code/my-project$ deactivate  # étape 5
fab@m1:~/code/my-project$

```

> Certains développeurs préfèrent nommer tous leurs environnements virtuels de la même manière (par exemple, `.venv`). Ainsi, ils peuvent configurer leurs outils pour n'importe quel projet en connaissant simplement cet emplacement. Le point dans `.venv` sert à rendre le dossier « invisible » sur Linux/macOS.
Sur un terminal **Windows 11 PowerShell**, les étapes sont les suivantes :

```powershell
PS C:\Users\H\Code> mkdir my-project  # étape 1
PS C:\Users\H\Code> cd .\my-project\
# vérification des versions installées
PS C:\Users\H\Code\my-project> py --list-paths
 -V:3.12 * C:\Users\H\AppData\Local\Programs\Python\Python312\python.exe
PS C:\Users\H\Code\my-project> py -3.12 -m venv lpp4ed  # étape 2
PS C:\Users\H\Code\my-project> .\lpp4ed\Scripts\activate  # étape 3
# vérification : utilise maintenant l'environnement virtuel
(lpp4ed) PS C:\Users\H\Code\my-project> py --list-paths
  * C:\Users\H\Code\my-project\lpp4ed\Scripts\python.exe
 -V:3.12 C:\Users\H\AppData\Local\Programs\Python\Python312\python.exe
(lpp4ed) PS C:\Users\H\Code\my-project> python  # étape 4
Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36)
>>> exit()
(lpp4ed) PS C:\Users\H\Code\my-project> deactivate  # étape 5
PS C:\Users\H\Code\my-project>

```
À ce stade, vous devriez être capable de créer et d'activer un environnement virtuel. N'oubliez pas : nous ne travaillons jamais au niveau du système avec Python.

## Installation de bibliothèques tierces

Pour installer des bibliothèques tierces, nous devons utiliser l'installateur de paquets Python, connu sous le nom de **pip**. Il est probable qu'il soit déjà disponible dans votre environnement virtuel.
L'exemple suivant montre comment installer des bibliothèques à partir d'un fichier `requirements.txt` :

```bash
(lpp4ed) fab@m1:~/code/my-project$ cat requirements.txt
django==5.0.3
requests==2.31.0
(lpp4ed) fab@m1:~/code/my-project$ pip install -r requirements.txt
Collecting django==5.0.3 ...
Installing collected packages: ..., requests, django
Successfully installed ... django-5.0.3 requests-2.31.0

```

## La console

À l'ère des interfaces graphiques et du tactile, utiliser une console peut sembler archaïque. Pourtant, chaque fois que vous quittez le clavier pour la souris, vous perdez du temps. La console permet une productivité et une vitesse supérieures.
De plus, si vous développez du code pour un serveur, la console sera souvent votre **seul outil d'accès**. Un bon développeur ne doit jamais se sentir perdu lors d'une connexion SSH vers un serveur distant.
Maintenant, revenons à Python.

---
### Comment exécuter un programme Python

Il existe plusieurs façons d'exécuter un programme Python.

#### Exécution de scripts Python

Python peut être utilisé comme un langage de script ; en fait, il s'avère toujours très utile à cet égard. Les scripts sont des fichiers (généralement de petite taille) que l'on exécute normalement pour accomplir une tâche spécifique. De nombreux développeurs finissent par se constituer un arsenal d'outils qu'ils utilisent lorsqu'ils ont besoin d'effectuer une opération. Par exemple, vous pouvez avoir des scripts pour analyser des données dans un format et les transformer dans un autre, ou vous pouvez utiliser un script pour manipuler des fichiers et des dossiers ; vous pouvez créer ou modifier des fichiers de configuration — techniquement, il n'y a pas grand-chose qui ne puisse être fait par un script.

Il est assez courant d'avoir des scripts s'exécutant à une heure précise sur un serveur. Par exemple, si la base de données de votre site web a besoin d'un nettoyage toutes les 24 heures (pour nettoyer régulièrement les sessions utilisateur expirées), vous pourriez configurer une tâche **Cron** qui lance votre script à 1h00 du matin chaque jour.

> Selon Wikipédia, l'utilitaire logiciel **Cron** est un planificateur de tâches basé sur le temps dans les systèmes d'exploitation de type Unix. Les personnes qui configurent et maintiennent des environnements logiciels utilisent Cron (ou une technologie similaire) pour planifier des tâches (commandes ou scripts shell) afin qu'elles s'exécutent périodiquement à des heures, dates ou intervalles fixes.

Nous utilisons des scripts Python pour effectuer toutes les tâches ingrates qui nous prendraient des minutes ou plus à faire manuellement, et qu'à un moment donné, nous avons décidé d'automatiser.

#### Exécution de l'interpréteur interactif Python

Une autre façon de lancer Python est d'appeler l'interpréteur interactif (shell). C'est ce que nous avons vu lorsque nous avons tapé `python` dans la ligne de commande de notre console.

Ouvrez donc une console, activez votre environnement virtuel (ce qui, à présent, devrait être une seconde nature pour vous, n'est-ce pas ?) et tapez `python`. Quelques lignes s'afficheront, ressemblant probablement à ceci :

```bash
(lpp4ed) fab@m1 ~/code/lpp4ed$ python
Python 3.12.2 (main, Feb 14 2024, 14:16:36)
[Clang 15.0.0 (clang-1500.1.0.2.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

Ces `>>>` constituent l'invite de commande (prompt) de l'interpréteur. Ils indiquent que Python attend que vous saisissiez quelque chose. Si vous tapez une instruction simple qui tient sur une ligne, c'est tout ce que vous verrez. Cependant, si vous tapez quelque chose qui nécessite plus d'une ligne de code, l'interpréteur changera l'invite en `...`, vous donnant un indice visuel que vous rédigez une instruction multiligne.

Allez-y, essayez ; faisons quelques calculs de base :

```python
>>> 3 + 7
10
>>> 10 / 4
2.5
>>> 2 ** 1024
179769313486231590772930519078902473361797697894230657273430081157
732675805500963132708477322407536021120113879871393357658789768814
416622492847430639474124377767893424865485276302219601246094119453
082952085005768838150682342462881473913110540827237163350510684586
298239947245938479716304835356329624224137216

```

La dernière opération montre quelque chose d'incroyable. Nous élevons 2 à la puissance 1024, et Python gère cette tâche sans aucune difficulté. Essayez de faire cela en Java, C++ ou C#. Cela ne fonctionnera pas, à moins d'utiliser des bibliothèques spéciales pour gérer des nombres aussi grands.

Nous utilisons l'interpréteur interactif tous les jours. Il est extrêmement utile pour déboguer rapidement ; par exemple, pour vérifier si une structure de données supporte une opération, ou pour inspecter un morceau de code. Vous découvrirez que l'interpréteur interactif deviendra vite l'un de vos meilleurs alliés dans ce voyage que vous entreprenez.

Une autre solution, dotée d'une interface graphique plus agréable, consiste à utiliser l'**IDLE** (*Integrated Development and Learning Environment*). C'est un environnement de développement intégré (IDE) assez simple, destiné principalement aux débutants. Il possède un ensemble de fonctionnalités légèrement plus étendu que l'interpréteur de base de la console. Il est inclus gratuitement dans les installateurs Python pour Windows et macOS, et s'installe facilement sur tout autre système.

> Guido Van Rossum a nommé Python d'après le groupe de comédie britannique Monty Python. La rumeur veut donc que le nom **IDLE** ait été choisi en l'honneur d'Eric Idle, l'un des membres fondateurs des Monty Python.

#### Exécution de Python en tant que service

En plus d'être exécuté comme un script ou dans les limites d'un interpréteur, Python peut être codé et lancé comme une application. Nous verrons des exemples de ce mode tout au long de ce livre. Nous l'examinerons plus en détail dans un instant, lorsque nous parlerons de l'organisation et de l'exécution du code Python.

#### Exécution de Python en tant qu'application GUI

Python peut également être utilisé pour créer des interfaces graphiques (**GUI**). Plusieurs frameworks sont disponibles, certains multiplateformes et d'autres spécifiques à un système. Un exemple populaire est **Tkinter**, qui est une couche orientée objet au-dessus de Tk.

> **Tk** est un toolkit GUI qui porte le développement d'applications de bureau à un niveau supérieur à l'approche conventionnelle. C'est l'interface graphique standard pour Tcl (*Tool Command Language*), mais aussi pour de nombreux autres langues dynamiques, permettant de produire des applications natives riches sur Windows, Linux, macOS, et plus encore.

Tkinter est livré avec Python ; il offre donc au programmeur un accès facile au monde des interfaces graphiques. Les autres frameworks GUI largement utilisés incluent :

* PyQT / PySide
* wxPython
* Kivy

Leur description détaillée dépasse le cadre de ce livre, mais vous trouverez toutes les informations nécessaires sur le site de Python : `https://docs.python.org/3/faq/gui.html`.

---

### Comment le code Python est-il organisé ?

Parlons un peu de l'organisation du code Python. Dans cette section, nous allons commencer à entrer dans le vif du sujet et introduire des termes et concepts plus techniques.

Pour commencer par l'essentiel : comment le code Python est-il organisé ? Bien sûr, vous écrivez votre code dans des fichiers. Lorsque vous enregistrez un fichier avec l'extension `.py`, ce fichier est appelé un **module** Python.

> Si vous êtes sur Windows ou macOS, qui cachent généralement les extensions de fichiers, nous vous recommandons de modifier la configuration pour voir les noms complets. Ce n'est pas une exigence stricte, mais une suggestion pratique pour distinguer les fichiers les uns des autres.

Il serait peu pratique d'enregistrer tout le code nécessaire au fonctionnement d'un logiciel dans un seul fichier. Cette solution fonctionne pour les scripts, qui ne dépassent généralement pas quelques centaines de lignes.

Une application Python complète peut comporter des centaines de milliers de lignes de code ; vous devrez donc les répartir dans différents modules, ce qui est mieux, mais pas suffisant. Pour remédier à cela, Python propose une autre structure appelée **package** (paquet), qui permet de regrouper des modules.

Un package n'est rien d'autre qu'un dossier. Dans les anciennes versions de Python, un fichier spécial nommé `__init__.py` était requis pour marquer un répertoire comme étant un package. Ce fichier n'a pas besoin de contenir de code, et bien que sa présence ne soit plus obligatoire, il reste conseillé de l'inclure pour des raisons pratiques.

Comme toujours, un exemple rendra tout cela plus clair. Voici la structure d'une application simple (obtenue avec la commande `tree`) :

```text
example
├── core.py
├── run.py
└── util
    ├── __init__.py
    ├── db.py
    ├── maths.py
    └── network.py

```

À la racine de cet exemple, nous avons deux modules, `core.py` et `run.py`, et un package, `util`. `core.py` contient probablement la logique centrale de notre application, tandis que `run.py` contient la logique de démarrage. Dans le package `util`, nous trouvons des outils utilitaires : `db.py` pour les bases de données, `maths.py` pour les outils mathématiques et `network.py` pour la gestion du réseau.

Si ce logiciel n'avait été organisé qu'en modules (sans package), sa structure serait plus difficile à déchiffrer :

```text
files_only
├── core.py
├── db.py
├── maths.py
├── network.py
└── run.py

```

Il est plus difficile de deviner le rôle de chaque module, n'est-ce pas ? Imaginez la complexité pour une application réelle sans cette organisation en packages.

---

### Comment utilisons-nous les modules et les packages ?

Lorsqu'un développeur écrit une application, il est probable qu'il doive appliquer la même logique à différents endroits. Par exemple, pour valider si un champ contient un nombre dans un formulaire web.

Dans une application de sondage, plusieurs questions peuvent nécessiter une réponse numérique :

* Quel est votre âge ?
* Combien d'animaux possédez-vous ?
* Combien d'enfants avez-vous ?

> Il serait de mauvaise pratique de copier/coller la logique de validation partout. Cela violerait le principe **DRY** (*Don't Repeat Yourself*), qui stipule que vous ne devriez jamais répéter le même morceau de code plus d'une fois dans votre application. Nous insistons : ne répétez jamais le même code !

Répéter la même logique est problématique car :

1. Un bug dans la logique devrait être corrigé dans chaque copie.
2. Toute modification de la méthode de validation nécessiterait de modifier chaque occurrence.
3. Vous pourriez oublier de mettre à jour une copie, créant un comportement incohérent.
4. Votre code serait inutilement long.

#### Les Fonctions

Pour réutiliser le code, Python utilise une construction appelée **fonction**. Une fonction est un bloc de code organisé et réutilisable permettant d'effectuer une tâche. Elles sont les briques de base de la modularité. Nous les explorerons en détail au Chapitre 4.

#### Les Bibliothèques (Libraries)

Une bibliothèque est une collection de fonctions et d'objets enrichissant les capacités d'un langage. Par exemple, la bibliothèque `math` de Python contient la fonction `factorial`.
> En mathématiques, la factorielle d'un entier  () est le produit de tous les entiers positifs inférieurs ou égaux à .
> Exemple : .
Pour utiliser cette fonction, il suffit de l'**importer** :

```python
>>> from math import factorial
>>> factorial(5)
120

```

Dans notre exemple précédent, le package `util` est notre bibliothèque utilitaire personnalisée. Elle contient nos outils réutilisables (`db.py`, `network.py`, etc.).
Nous verrons en détail comment importer et utiliser des fonctions dans le chapitre dédié. Parlons maintenant d'un autre concept crucial : le modèle d'exécution de Python.
 
