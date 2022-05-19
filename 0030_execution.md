# Exécution de commande

La connexion ssh ne vous donne accès qu’à la machine "maître", qui ne sert que de système d'aiguillage et qui n’est pas dimensionnée pour faire des calculs. Pour profiter des possibilités du cluster, il faut passer par un système de *file d’attente*.

Le gestionnaire que nous utilisons (slurm) est très bien [documenté sur internet](https://slurm.schedmd.com/documentation.html). Nous vous livrons ici une version synthétique, correspondant à l'usage le plus courant sur notre cluster.

## Lancement immédiat (srun)

Si vous souhaitez lancer une commande simple et attendre le résultat avec un retour direct sur votre terminal, vous pouvez utiliser `srun` :

```bash
srun [options de srun] ma_commande [options pour ma_commande]
```

Attention cependant, lancer directement via `srun` est surtout utile pour les calculs courts et les tests sur lesquels on veut avoir un retour immédiat. Pour les calculs plus longs, vous pourrez utiliser `sbatch`, qui est décrit dans la section suivante.


## Options d'exécution

Voici quelques options importantes (utilisables aussi dans `sbatch`) :

### Nombre et choix des nœuds

* `-N` permet de spécifier le nombre minimum de nœuds (i.e. machine) sur lesquels lancer la commande.
* `--nodelist=...` permet de spécifier les nœuds à utiliser.
* `--gpus=n` permet de définir le nombre de gpus à utiliser. `--mem-per-gpu=n` pour donner la mémoire minimum pour chaque gpu.
* `--mem=MB` permet de définir le taille minimale de mémoire pour chaque processus.

### Mpi/Single Programme Multiple Data

Par défaut, Slurm lance les processus de façon indépendante, et il n'y a que les variables d'environnement qui différent. `SLURM_PROCID` donne l'index du processus, `SLURM_NTASKS` donne le nombre de processus, etc... Cf. [cette page](https://slurm.schedmd.com/sbatch.html#lbAK) pour un tour des variables mises en place par slurm.

Si vous utilisez mpi et si vous voulez que `rank` et `size` soient correctement initialisés pour vos programmes, il faut ajouter l'option `--mpi=pmi2` aux commandes `srun`. En utilisant cette option, `srun` prend la place du traditionnel `mpirun`, en se chargeant à la fois de l'allocation des ressources ET de l'association d'un `rank` à chaque processus.

### Remarque sur le multicore/multithreading

Sauf contre-ordre, slurm ne lance qu'un seul processus par nœud et chaque processus peut utiliser tous les cores comme il l'entend. Slurm ne met pas de barrières sur le nombre de threads que chaque processus peut utiliser.

Dans le cas ou vos programmes sont conçus pour fonctionner avec un nombre fixe de threads (1 par exemple :) ), vous pouvez demander à slurm d'allouer des "cores" plutôt que des nœuds (i.e. des machines complètes) en utilisant les options suivantes :
* `-n` permet de spécifier le nombre de processus à lancer en parallèle. Cette approche est à adopter notamment si vous ne gérez pas le multithreading dans vos processus. Si `-c` n'est pas spécifié, Slurm utilisera un "core" par processus de sorte qu'un nœud pourra se retrouver avec plusieurs processus.
* `-c` permet de spécifier le nombre de core "alloué" par processus. Ce n'est pas un allocation *stricto sensu* vu que les processus réservent autant de threads qu'ils le souhaitent... mais ça permettra de fixer le nombre de HW threads que chaque processus pourra utiliser sans marcher sur les autres. Rq: pour une gestion des affinités notamment lorsqu'il y a plusieurs sockets, voir par exemple [cette page](https://slurm.schedmd.com/mc_support.html)

## Lancement différé et graphes de taches (sbatch)

Pour envoyer un job dans la file d’attente sans bloquer le terminal, vous pouvez utiliser la commande `sbatch`. De cette manière, il est possible de se déloguer sans stopper le calcul.

La commande `sbatch` prend en entrée un script bash, qui pourra contenir à la fois les commandes pour lancer le(s) programme(s), les options concernant les ressources (la RAM, nombre de processeurs...), et les options liées aux entrées/sorties.

Attention: `sbatch` ne se substitue pas à `srun`. Le script bash sert à définir le contexte, pour pouvoir ensuite y lancer une ou plusieurs commandes `srun`, qui pourront s'exécuter de façon séquentielle ou avec des dépendances de type graphe.

Voici un exemple de script qui lance une commande sur 2 nœuds :

```bash
#!/bin/bash 

# -- Nom du calcul, répertoire de travail : 
#SBATCH --job-name=nom_du_job
#SBATCH --chdir=/workdir/votre_login/chemin_dossier 
# -- Optionnel, pour être notifié par email : 
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=adresse@email.com 
# -- Sortie standard et d'erreur dans le fichier .output : 
#SBATCH --output=./%j.stdout
#SBATCH --error=./%j.stderr
# -- Contexte matériel
#SBATCH --nodes=2

# En l'absence de srun, les commandes ne sont exécutée que sur *une seule machine*.
# Cependant srun pourra utiliser les variables d'environnement en résultant
conda activate mon_environnement
module load mon_module

# Pour une exécution en parallèle, il faut utiliser srun.
# Par défaut srun utilise toutes les ressources demandées par sbatch
#  et s'il y a plusieurs srun, ils sont exécutés de façon séquentielle.
srun python mon_script.py
```

### Job arrays

L'option `-array=...` permet de générer des lancement multiples d'un même programme.

Chaque job sera lancé avec un index, mis dans la variable d'environnement `SLURM_ARRAY_TASK_ID`. `SLURM_ARRAY_TASK_MAX` donnera l'index maximal.

Voici quelque exemples:

```bash
# 'mon_programme' sera lancé 32 fois, avec `SLURM_ARRAY_TASK_ID` qui ira de 0 à 31
$ sbatch --array=0-31 mon_programme

# pareil avec 1, 3, 5 and 7 comme indices
$ sbatch --array=1,3,5,7 mon_programme

# on peut définir des pas. Dans ce cas on aura 1, 3, 5 and 7
$ sbatch --array=1-7:2 mon_programme
```

Cf. [cette page](https://slurm.schedmd.com/job_array.html) pour une description plus détaillée.

## Suivi des jobs

`squeue` permet de voir les jobs en attente ou en train de tourner. S'ils tournent, il y aura un `R` dans la colonne `ST`.

`sattach` permet d'attacher sur le terminal les E/S d'un job en train de tourner. Ça permet de surveiller l'avancée d'un job, ou par exemple d'interagir avec un debugger. `ctrl-c` permet de détacher de nouveau le job et de le laisser de nouveau tourner en fond (de manière non bloquante).

`scancel` permet permet de supprimer une soumission ou d’arrêter le job s'il est en cours d’exécution.

`sstat` donne des infos sur les ressources utilisées par un job
