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
