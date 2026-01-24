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

**Question 1.** Quel est le plus court chemin dans ce labyrinthe ?

### Installation de l'environnement de travail

- Rendez vous sur la plateforme [Onyxia INSEE](https://datalab.sspcloud.fr/) > Connexion > Créer un compte > Utilisez votre adresse "@ensae.fr"
- Catalogue de services > Vscode-python
  - Paramètres : Git > Repository à `https://github.com/simon-mauras/ensae-prog26-eco.git`
  - Lancer, attendre 2 min, copier le mot de passe, ouvrir le service.

Si vous le souhaitez, vous pouvez essayer de faire le TP en local, cependant nous ne serons pas forcément en mesure de vous aider s'il y a un des problèmes d’installation.

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

**Question 2.** Baladez vous, et découvrez les fichiers. Où se trouve la fonction permettant de trouver l'ensemble des cases adjacentes à une case du labyrinthe ?

**Question 3.** Ouvrez le fichier `main_testing.py`. Lancez l'exécution (petit triangle en haut à droite). Quel est le message d'erreur affiché ? Dans la console qui s'est ouverte, tapez `cd ensae-prog26-eco`, puis relancez l'exécution, l'erreur devrait être résolue.

### Tests unitaires

Le dossier test contient des "test unitaires", permettant de tester les fonctions une à une, très utile pour prévenir les bugs lors d'un gros projet logiciel. Nous avons choisis d'utiliser le module pytest.

**Question 4.** Allez lire le premier exemple dans la [documentation de pytest](https://docs.pytest.org/en/stable/getting-started.html). Quelle est la commande à exécuter pour installer pytest ? Et pour lancer les tests ?

**Question 5.**  Sur VS Code, cliquez sur le logo "fiole" sur la gauche, et configurez les tests unitaires pour pouvoir les lancer automatiquement. 

Dans la seconde partie du projet, il vous sera demandé d'écrire vos propres tests unitaires, pour tester les fonctions que vous implémenterez.


### Déplacer le robot

#### Stratégie aléatoire

Nous allons maintenant essayer d'écrire un algorithme qui amène le robot à l'arrivée. La stratégie la plus naïve consiste à le faire se déplacer de manière aléatoire, et espérer qu'il atteigne un jour l'arrivée.

**Question 6.** Allez lire la [documentation du module random](https://docs.python.org/3/library/random.html). Comment générer un nombre (pseudo)aléatoire entre 0 et 3 (inclus) ?

**Question 7.** Créez un fichier `main_random_walk.py` dans le dossier `code`. En vous inspirant du fichier `main_sandbox.py`, implémentez une boucle "tant que", qui déplace le robot dans une direction aléatoire tant que celui ci n'a pas atteint l'arrivé. Comparez la solution obtenue au plus court chemin calculé dans la question 1.

#### Stratégie suivre un mur

Dans un labyrinthe, un algorithme plus efficace pour ne pas se perdre consiste à suivre le mur de droite, en posant sa main dessus.

**Question 8.** Quel est le coût de cette stratégie pour l'exemple `medium.txt` ? Et pour l'exemple `cycles.txt` ?

**Question 9.** Créer un fichier `main_follow_wall.py` dans le dossier `code`. En vous inspirant du fichier `main_sandbox.py`, implémentez l'algorithme qui suit le mur droit. Nous vous conseillons de créer une nouvelle variable, qui stocke la direction dans laquelle le robot fait face. Comparez la solution obtenue au plus court chemin calculé dans la question 1.
