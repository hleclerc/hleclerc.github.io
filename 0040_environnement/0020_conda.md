# Conda

Pour une plus grande liberté, notamment pour Python, mais pas que, [conda](https://docs.conda.io/en/latest/miniconda.html) vous permettra d'installer des environnements quasi-complets dans un de vos répertoire.

Il y a une limite à ce qu'il est possible de faire sans les droits d'admin, mais bon nombre de programmes et de librairies sont disponibles par ce biais.

Par ailleurs, les environnements sont confinés : si par exemple vous installez un programme avec `pip` dans un environnement conda, ça ne modifiera que votre environnement conda.

Pour savoir si un programme ou une librairie est installable par ce biais, vous pouvez aller sur [anaconda.org](https://anaconda.org/).

# Installation

Une fois connecté·e sur cinaps, vous pouvez taper:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Attention, en réponse à `Miniconda3 will now be installed into this location:...`, compte tenu de la place que prennent les environnements, _il est vivement conseillé d'installer les environnements dans votre `workdir`_ (par exemple `/workdir/<login>/.miniconda`).

# Création d'environnement

Une fois l'environnement de base mis en place, vous pouvez créer un environnement spécifique avec 

```bash
conda create --name <un_nom_que_vous_choisissez>
```

Vous pouvez activer cet environnement avec :

```bash
conda activate <un_nom_que_vous_choisissez>
```

puis en sortir avec :

```bash
conda deactivate
```

# Installation de programme

Une fois dans un environnement (celui de base ou un que vous avez créé), vous pouvez installer un ou plusieurs paquets avec

```bash
conda install [-c nom_du_canal] nom_paquet_1 nom_paquet_2 ...
```

Spécifier `-c nom_du_canal` n'est utile que pour les paquets qui ne sont pas disponibles sur les canaux définis par défaut.

Pour savoir si c'est le cas, vous pouvez ou bien tester sans l'option et voir le résultat, ou bien chercher ce qui est proposé sur [anaconda.org](https://anaconda.org/).



