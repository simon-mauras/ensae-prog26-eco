# Projet de programmation : Séances de TP

## Séance 1 : découverte de l'environnement (1h30)

Lors de cette première séance, nous allons découvrir l'environnement de travail, et commencer à coder quelques fonctions. L'objectif est de déplacer un robot dans un labyrinthe, afin de l'emmener du départ (case `S`) à l'arrivée (case `G`), en minimisant la somme des coûts sur le chemin, et sans passer par un mur (cases `#`). Voici un exemple de labyrinthe :

```
###########
#S9600#133#
###8#####9#
#08386#379#
#4###0#2###
#6#542351G#
###########
```

***Question 1.*** Quel est le plus court chemin dans ce labyrinthe ?

### Installation de l'environnement de travail

- Rendez vous sur la plateforme [Onyxia INSEE](https://datalab.sspcloud.fr/) > Connexion > Créer un compte > Utilisez votre adresse "@ensae.fr"
- Catalogue de services > Vscode-python
  - Paramètres Git > Repository :
```
https://github.com/simon-mauras/ensae-prog26-eco.git
```
  - Lancer, attendre 2 min, copier le mot de passe, ouvrir le service.

Si vous le souhaitez, vous pouvez essayer de faire le TP directement sur votre ordinateur, cependant nous ne serons pas forcément en mesure de vous aider s'il y a des problèmes d’installation.

Il existe également une plateforme [Onyxia ENSAE](https://onyxia.lab.groupe-genes.fr/), accessible directement avec votre compte ENSAE.

### Structure des fichiers

Les fichiers sont organisés de la manière suivante :

- `code` (contient tous les codes python)
  - `grid.py` (classe qui charge un labyrinthe)
  - `robot.py` (classe qui manipule un robot dans le labyrinthe)
  - `main_sandbox.py` (fichier à exécuter)
- `examples` (contient les fichiers de données)
  - `small.txt` (labyrinthe petit, sans cycle)
  - `medium.txt` (labyrinthe moyen, sans cycle)
  - `large.txt` (labyrinthe grand, sans cycle)
  - `impossible.txt` (labyrinthe sans solution)
  - `circles.txt` (labyrinthe moyen, avec cycles)
  - `empty.txt` (labyrinthe grand, avec cycles)
- `tests` (contient les tests unitaires)
  - `test_grid.py` (test pour le fichier `code/grid.py`)
  - `test_robot.py` (test pour le fichier `code/robot.py`)

***Question 2.*** Baladez vous, et découvrez les fichiers. Où se trouve la fonction permettant de trouver l'ensemble des cases adjacentes à une case du labyrinthe ?

***Question 3.*** Ouvrez le fichier `main_testing.py`. Lancez l'exécution (petit triangle en haut à droite). Quel est le message d'erreur affiché ? Dans la console qui s'est ouverte, tapez `cd ensae-prog26-eco`, puis relancez l'exécution, l'erreur devrait être résolue.

### Tests unitaires

Le dossier test contient des "test unitaires", permettant de tester les fonctions une à une, très utile pour prévenir les bugs lors d'un gros projet logiciel. Nous avons choisis d'utiliser le module pytest.

***Question 4.*** Allez lire le premier exemple dans la [documentation de pytest](https://docs.pytest.org/en/stable/getting-started.html). Quelle est la commande à exécuter pour installer pytest ? Et pour lancer les tests ?

***Question 5.***  Sur VS Code, cliquez sur le logo "fiole" sur la gauche, et configurez les tests unitaires pour pouvoir les lancer automatiquement. 

Dans la seconde partie du projet, il vous sera demandé d'écrire vos propres tests unitaires, pour tester les fonctions que vous implémenterez.


### Déplacer le robot

#### Stratégie aléatoire

Nous allons maintenant essayer d'écrire un algorithme qui amène le robot à l'arrivée. La stratégie la plus naïve consiste à le faire se déplacer de manière aléatoire, et espérer qu'il atteigne un jour l'arrivée.

***Question 6.*** Allez lire la [documentation du module random](https://docs.python.org/3/library/random.html). Comment générer un nombre (pseudo)aléatoire entre 0 et 3 (inclus) ?

***Question 7.*** Créez un fichier `main_random_walk.py` dans le dossier `code`. En vous inspirant du fichier `main_sandbox.py`, implémentez une boucle "tant que", qui déplace le robot dans une direction aléatoire tant que celui ci n'a pas atteint l'arrivé. Comparez la solution obtenue au plus court chemin calculé dans la question 1.

#### Stratégie suivre un mur

Dans un labyrinthe, un algorithme plus efficace pour ne pas se perdre consiste à suivre le mur de droite, en posant sa main dessus.

***Question 8.*** Quel est le coût de cette stratégie pour l'exemple `medium.txt` ? Et pour l'exemple `cycles.txt` ?

***Question 9.*** Créer un fichier `main_follow_wall.py` dans le dossier `code`. En vous inspirant du fichier `main_sandbox.py`, implémentez l'algorithme qui suit le mur droit. Nous vous conseillons de créer une nouvelle variable, qui stocke la direction dans laquelle le robot fait face. Comparez la solution obtenue au plus court chemin calculé dans la question 1.

\newpage

## Séance 2 : Git pull, invite de commande, et fonctions récursives (1h30)

### Mise à jour du dépot

Depuis l'environnement créé lors de la première séance, nous allons récupérer les ajouts faits à la base de code. Le logiciel Git permet de mettre à jour votre dépôt local (ici Onyxia) depuis le dépot distant (ici GitHub).

```
+------------------------------------+---------------------+
|         En local (Onyxia)          | À distance (Github) |
+------------------------------------+---------------------+
| Dossier de travail |   Dépot Git   |      Dépot Git      |
+--------------------+---------------+---------------------+
|                    |        <=== fetch ====              |
|             <=== merge ====        |                     |
|             <============ pull ============              |
+--------------------+---------------+---------------------+
```

L'opération "Fetch" permet de récupérer les modifications du dépot distant, et de les importer dans le dépot local. L'opération "Merge" permet de mettre à jour le dossier de travail avec le dépot local. L'opération "Pull" combine "Fetch" puis "Merge".

Attention, si des modifications locales et distantes concernent le même fichier, cela crée un conflit. Personne n'aime les conflits, nous essaierons de les éviter dès que possible (nous verrons comment les gérer lors des prochaines séances).

***Question 1.***  Depuis l'onglet Git de VS-Code, lancer une opération "Pull". En cas de conflit, cette semaine nous allons ignorer les modification locales, en cliquant sur "Changes" > "Discard All Changes".

### Invite de commandes

L'invite de commande (*terminal* en anglais) est un explorateur de fichier permettant de lancer des programmes. Nous allons découvrir quelques commandes de base :

- La commande "`pwd`" (**p**rint **w**orking **d**irectory) permet d'afficher le dossier dans lequel on se situe.
- La commande "`ls`" (**l**i**s**t) permet de lister le contenu du dossier courant.
- La commande "`cd nom-du-dossier`" (**c**hange **d**irectory) permet de se déplacer dans le dossier `nom-du-dossier`. Le dossier `.` est le dossier courant, et `..` est le dossier parent. La commande `cd ..` permet donc de remonter au dossier parent. 
- La commande "`mkdir nouveau-dossier`" (**m**a**k**e **dir**ectory) permet de créer le dossier `nom-du-dossier`.
- La commande "`touch nouveau-fichier`" permet de créer un fichier vide `nouveau-fichier`.

***Question 2.*** Avec l'invite de commande, créez l'arborescence suivante :
```
+-- dossier1
|   +-- dossier2
|   |   +-- fichier1.txt
|   |   +-- fichier2.py
|   +-- fichier3.csv
```

### Revenons à nos robots

Nous allons (enfin) revenir à nos robots. Nous vous rappelons que l'objectif est de faire parvenir le robot à l'arrivée, en utilisant uniquement les méthodes `move` et `at_goal` ainsi que l'attribut `position` de la classe `Robot`.

#### Stratégie simples

Commençons par terminer d'implémenter les stratégies naïves de la première séance. Afin de pouvoir changer d'exmple plus facilement, nous souhaitons pouvoir fournir en paramètre le nom du fichier à lire, par exemple :
```
python code/main_random_walk.py examples/medium.txt
```
Pour ce faire, allez lire la [documentation du module sys](https://docs.python.org/3/library/sys.html) pour apprendre à utiliser la variable `argv`.

***Question 3.*** Terminez les questions 8 et 9 de la séance 1, et ajoutez la possibilité de fournir un nom de fichier en paramètre. Les stratégies implémentées fonctionnent elles sur tous les fichiers de test ? 

#### Parcours en profondeur

Nous allons implémenter une stratégie récursive qui explore tout le labyrinthe. Il s'agit de l'algorithme de parcours en profondeur (DFS, pour *Depth-First Search* en anglais). Nous vous recommandons de consulter la [page wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur) sur cet algorithme.

***Questions 4.*** Expliquer ce que l'on obtient-on en exécutant le code :
```python
def fonction_recursive(i, lst):
  if i < 10:
    lst.append(i)
    fonction_recursive(2*i, lst)
    fonction_recursive(2*i+1, lst)

res = []
fonction_recursive(0, res)
print(res)
```

***Question 5.*** Dans un fichier `main_dfs.py`, implémentez une fonction récursive `dfs(robot, deja_vu)` qui explore le labyrinthe, renvoie `True` dès que le robot atteint l'arrivée, et renvoie `False` si le robot est revenu au point de départ sans trouver l'arrivée. Parvenez vous à résoudre tous les labyrinthes ?
