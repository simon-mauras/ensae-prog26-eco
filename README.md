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

### Mise à jour du dépôt

Depuis l'environnement créé lors de la première séance, nous allons récupérer les ajouts faits à la base de code. Le logiciel Git permet de mettre à jour votre dépôt local (ici Onyxia) depuis le dépôt distant (ici GitHub).

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

L'opération "Fetch" permet de récupérer les modifications du dépôt distant, et de les importer dans le dépôt local. L'opération "Merge" permet de mettre à jour le dossier de travail avec le dépôt local. L'opération "Pull" combine "Fetch" puis "Merge".

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

L'invite de commande permet aussi de lancer l'exécution de programmes. Par exemple, lancer l'exécution du fichier `main_sandbox.py` depuis VS-Code (petit triangle) est un raccourci pour la commande "`python code/main_sandbox.py`" (ou équivalente).

Afin de pouvoir tester des exemples différents avec le même code python, nous allons utiliser la possibilité de fournir un paramètre à une commande. 

***Question 3.*** Dans le fichier `main_sandbox.py` ajouter les lignes suivante :
```python
import sys
print(sys.argv)
```
Qu'obtient on avec la commande "`python code/main_sandbox.py`" ? Et avec la commande "`python code/main_sandbox.py examples/medium.txt`" ? Expliquer les résultats en utilisant la [documentation du module sys](https://docs.python.org/3/library/sys.html).

### Revenons à nos robots

Nous allons (enfin) revenir à nos robots. Nous vous rappelons que l'objectif est de faire parvenir le robot à l'arrivée, en utilisant uniquement les méthodes `move` et `at_goal` ainsi que l'attribut `position` de la classe `Robot`.

#### Stratégie simples

Commençons par terminer d'implémenter les stratégies naïves de la première séance. Afin de pouvoir changer d'exemple plus facilement, nous souhaitons pouvoir fournir en paramètre le nom du fichier à lire en utilisant la variable `sys.argv`.

***Question 4.*** Terminez les questions 7 et 9 de la séance 1, et ajoutez la possibilité de fournir un nom de fichier en paramètre. Les stratégies implémentées fonctionnent elles sur tous les fichiers d'exemple ? 

#### Parcours en profondeur

Nous allons implémenter une stratégie récursive qui explore tout le labyrinthe. Il s'agit de l'algorithme de parcours en profondeur (DFS, pour *Depth-First Search* en anglais). Nous vous recommandons de consulter la [page wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur) sur cet algorithme.

***Questions 5.*** Expliquer ce que l'on obtient-on en exécutant le code :
```python
def fonction_recursive(i, lst):
  if i < 10:
    lst.append(i)
    fonction_recursive(2*i, lst)
    fonction_recursive(2*i+1, lst)

res = []
fonction_recursive(1, res)
print(res)
```

***Question 6.*** Dans un fichier `main_dfs.py`, implémentez une fonction récursive `dfs(robot, deja_vu)` qui explore le labyrinthe, renvoie `True` dès que le robot atteint l'arrivée, et renvoie `False` si le robot est revenu au point de départ sans trouver l'arrivée. Parvenez vous à résoudre tous les labyrinthes ?

\newpage

## Séance 3&4 : Plus court chemin (3h)

Dans cette (double) séance, nous allons aborder la théorie des graphes, comment elle nous permet de modéliser notre problème de labyrinthe, et quels sont les algorithmes pour calculer un plus court chemin.

***Question 1.***  Depuis l'onglet Git de VS-Code, lancer une opération "Pull". Comparez les solutions pour les stratégies "aléatoire" et "suivre le mur" avec vos implémentations.

***Question 2.*** Finissez l'implémentation de la stratégie "récursive" dans le fichier `main_dfs.py`. N'hésitez pas à demander de l'aide à votre chargé de TP !

### Théorie des graphes

Un graphe est un objet mathématique permettant de modéliser divers scénarios (réseau routier, réseau social, jeu à deux joueurs, ...).

***Question 3.*** Allez lire la [page wikipédia](https://fr.wikipedia.org/wiki/Graphe_(mathématiques_discrètes)) sur les graphes. Nous allons modéliser notre problème avec un graphe orienté et pondéré. Quels sont les sommets ? Quels sont les poids des arêtes ? Quelle est la question à résoudre dans ce graphe ?

### Parcours de graphe

Dans le parcours en profondeur que vous avez implémenté, le robot se promène récursivement sur toutes les cases du labyrinthe. Par exemple, on peut avoir le parcours suivant, ou les cases sont numérotées dans l'ordre dans lequel elles sont découvertes pour la première fois.
```
######
#S123#
##4###
#8567#
######
```
Dans un parcours en largeur (BFS, pour *Breadth-First Search* en anglais), les cases sont parcourues par distance au départ croissante (où la distance est nombre minimal de cases à traverser). Par exemple, les cases peuvent être découvertes dans l'ordre suivant :
```
######
#S124#
##3###
#7568#
######
```
On remarquera que si un seul robot devait explorer les cases dans cet ordre là, il ferait beaucoup de chemin inutile. Par conséquent, un parcours en largeur crée une "copie" du robot à chaque fois qu'il découvre une nouvelle case. Pour traiter les copies par ordre de création, nous les stockerons dans une "file" implémentée par le type `collections.deque`. Nous vous recommandons de consulter la [documentation du module collections](https://docs.python.org/3/library/collections.html#collections.deque) ainsi que la [page wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur) sur le parcours en largeur.

***Question 4.*** Afin de pouvoir créer une copie du robot, implémentez une méthode `copy(self)` dans la classe `Robot` qui renvoie une copie du robot, avec la même position et le même coût. Attention, il ne faut pas se contenter de renvoyer l'objet actuel car on veut pouvoir déplacer la copie du robot sans déplacer l'original !!

***Question 5.*** Dans un fichier `main_bfs.py` implémentez l'algorithme du parcours en largeur, qui stocke dans une "file" toute nouvelle copie de robot lors de la découverte d'une nouvelle case, et les traite par ordre de création.

### Algorithme de Dijkstra

Le parcours en largeur permet de calculer le chemin dans un graphe qui utilise le moins d'arête possible. Cependant, dans notre problème, chaque arête a un coût (entier entre 0 et 9). L'algorithme de Dijkstra permet de calculer le chemin de coût minimal. Pour ce faire, on parcourt les sommets par distance au départ croissante (où la distance est le coût minimal des arêtes à traverser), en remplaçant la "file" du parcours en largeur par une "file à priorité" implémentée par le module `heapq`. Nous vous recommandons de consulter la [documentation du module heapq](https://docs.python.org/3/library/heapq.html) ainsi que la [page wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_parcours_en_profondeur) sur l'algorithme de Dijkstra.

***Question 6.*** Afin de pouvoir comparer deux copies du robot, et savoir laquelle doit être traitée en premier, implémentez une méthode `__lt__(self, other)` dans la classe `Robot`, qui compare les coût du robot `self` et du robot `other`. Il sera désormais possible de faire la comparaison `robot1 < robot2` qui sera évaluée par Python avec l'appel de fonction `__lt__(robot1, robot2)`.

***Question 7.*** Dans un fichier `main_dijkstra.py` implémentez l'algorithme de Dijkstra, qui stocke dans une "file à priorité" toute nouvelle copie de robot lors de la découverte d'une nouvelle case, et les traite par coût croissant.

