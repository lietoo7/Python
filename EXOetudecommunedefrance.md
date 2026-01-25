# EXO : Etude démographique de la communauté de communes Pévéloises

Voici un tableau de dictionnaires comportant les noms des communes de la Pévèle, leur superficie et leur nombre d'habitants en Janvier 2020 :
```
communautePevele = [
    {'Commune': 'Attiches', 'Population': '2229', 'Superficie': '668'},
    {'Commune': 'Avelin', 'Population': '2304', 'Superficie': '1376'},
    {'Commune': 'Bachy', 'Population': '1396', 'Superficie': '641'},
    {'Commune': 'Bersée', 'Population': '2120', 'Superficie': '1093'},
    {'Commune': 'Bourghelles', 'Population': '1418', 'Superficie': '655'},
    {'Commune': 'Camphin-en-Pévèle', 'Population': '1570', 'Superficie': '645'},
    {'Commune': 'Cappelle-en-Pévèle', 'Population': '1959', 'Superficie': '811'},
    {'Commune': 'Cobrieux', 'Population': '518', 'Superficie': '284'},
    {'Commune': 'Cysoing', 'Population': '4427', 'Superficie': '1362'},
    {'Commune': 'Ennevelin', 'Population': '1973', 'Superficie': '992'},
    {'Commune': 'Genech', 'Population': '2050', 'Superficie': '746'},
    {'Commune': 'Louvil', 'Population': '835', 'Superficie': '250'},
    {'Commune': 'Mérignies', 'Population': '2105', 'Superficie': '861'},
    {'Commune': 'Moncheaux', 'Population': '1315', 'Superficie': '497'},
    {'Commune': 'Mons-en-Pévèle', 'Population': '2054', 'Superficie': '1237'},
    {'Commune': 'Mouchin', 'Population': '1340', 'Superficie': '919'},
    {'Commune': 'Templeuve', 'Population': '5778', 'Superficie': '1584'},
    {'Commune': 'Tourmignies', 'Population': '756', 'Superficie': '203'},
    {'Commune': 'Wannehain', 'Population': '839', 'Superficie': '371'}
]
```

Votre travail consiste à écrire puis à implémenter un algorithme sous la forme de fonctions permettant de déterminer :

la ville la plus peuplée.
la ville la moins peuplée.
le nombre moyen d'habitants par km² dans la Pévèle.

---
### Étape 1 : Analyser la structure des données

Avant de coder, regardez comment est faite la variable `communautePevele`.

* C'est une **liste** (crochets `[]`).
* Elle contient des **dictionnaires** (accolades `{}`).
* **Piège :** Les nombres sont entre guillemets (ex: `'2229'`). Ce sont des chaînes de caractères. Pour faire des calculs ou des comparaisons numériques, vous devrez utiliser `int()`.

### Étape 2 : Trouver le maximum (ville la plus peuplée)

Pour trouver le maximum dans une liste de dictionnaires :

1. Créez une variable pour stocker la "ville max" (au début, prenez la première de la liste).
2. Parcourez la liste avec une boucle `for`.
3. À chaque étape, comparez la population de la ville actuelle avec celle de votre "ville max".
4. Si la population actuelle est plus grande, remplacez votre "ville max" par la ville actuelle.

### Étape 3 : Trouver le minimum (ville la moins peuplée)

C'est exactement la même logique que pour le maximum, mais vous changez le signe de comparaison (`<` au lieu de `>`).

### Étape 4 : Calculer la densité moyenne

Ici, on ne cherche pas une ville précise, mais une moyenne globale.

1. Créez deux variables compteurs : `total_population` et `total_superficie`, initialisées à 0.
2. Parcourez toute la liste et additionnez chaque population et chaque superficie à vos compteurs (n'oubliez pas `int()`).
3. Une fois la boucle finie, divisez le total de la population par le total de la superficie.
* *Note :* La superficie semble être en hectares ou unités locales (ex: 668 pour Attiches). Si le résultat doit être par , vérifiez l'unité, mais mathématiquement la formule reste .



---

### Code complet (Solution)

Voici l'implémentation propre en Python :

```python
communautePevele = [
    {'Commune': 'Attiches', 'Population': '2229', 'Superficie': '668'},
    {'Commune': 'Avelin', 'Population': '2304', 'Superficie': '1376'},
    {'Commune': 'Bachy', 'Population': '1396', 'Superficie': '641'},
    {'Commune': 'Bersée', 'Population': '2120', 'Superficie': '1093'},
    {'Commune': 'Bourghelles', 'Population': '1418', 'Superficie': '655'},
    {'Commune': 'Camphin-en-Pévèle', 'Population': '1570', 'Superficie': '645'},
    {'Commune': 'Cappelle-en-Pévèle', 'Population': '1959', 'Superficie': '811'},
    {'Commune': 'Cobrieux', 'Population': '518', 'Superficie': '284'},
    {'Commune': 'Cysoing', 'Population': '4427', 'Superficie': '1362'},
    {'Commune': 'Ennevelin', 'Population': '1973', 'Superficie': '992'},
    {'Commune': 'Genech', 'Population': '2050', 'Superficie': '746'},
    {'Commune': 'Louvil', 'Population': '835', 'Superficie': '250'},
    {'Commune': 'Mérignies', 'Population': '2105', 'Superficie': '861'},
    {'Commune': 'Moncheaux', 'Population': '1315', 'Superficie': '497'},
    {'Commune': 'Mons-en-Pévèle', 'Population': '2054', 'Superficie': '1237'},
    {'Commune': 'Mouchin', 'Population': '1340', 'Superficie': '919'},
    {'Commune': 'Templeuve', 'Population': '5778', 'Superficie': '1584'},
    {'Commune': 'Tourmignies', 'Population': '756', 'Superficie': '203'},
    {'Commune': 'Wannehain', 'Population': '839', 'Superficie': '371'}
]

def ville_plus_peuplee(data):
    max_ville = data[0]
    for ville in data:
        if int(ville['Population']) > int(max_ville['Population']):
            max_ville = ville
    return max_ville['Commune']

def ville_moins_peuplee(data):
    min_ville = data[0]
    for ville in data:
        if int(ville['Population']) < int(min_ville['Population']):
            min_ville = ville
    return min_ville['Commune']

def moyenne_habitants_km2(data):
    total_pop = 0
    total_surf = 0
    for ville in data:
        total_pop += int(ville['Population'])
        total_surf += int(ville['Superficie'])
    
    # On suppose ici que la superficie est en hectares, 
    # donc on divise par 100 pour avoir des km2 si nécessaire, 
    # mais suivons l'énoncé brut : pop / superficie
    return total_pop / total_surf

# --- Tests ---
print(f"Ville la plus peuplée : {ville_plus_peuplee(communautePevele)}")
print(f"Ville la moins peuplée : {ville_moins_peuplee(communautePevele)}")
print(f"Moyenne d'habitants par unité de surface : {moyenne_habitants_km2(communautePevele):.2f}")

```
