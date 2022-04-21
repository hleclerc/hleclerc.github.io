# Exécution de commande

La connexion ssh ne vous donne accès qu’à la machine "maître", qui ne sert que de système d'aiguillage et qui n’est pas dimensionnée pour faire des calculs. Pour profiter des possibilités du cluster, il faut passer par un système de *file d’attente*.

Le gestionnaire que nous utilisons (slurm) est très bien [documenté sur internet](https://slurm.schedmd.com/documentation.html). Nous vous livrons ici une version synthétique, correspondant à l'usage le plus courant sur notre cluster.

## Lancement immédiat (srun)

Si vous souhaitez lancer une commande simple et attendre le résultat avec un retour direct sur votre terminal, vous pouvez utiliser `srun` :

```bash
srun [options de srun] ma_commande [options pour ma_commande]
```

Voici quelques options importantes:
* `-N` permet de spécifier le nombre minimum de nœuds (i.e. machine) sur lesquels lancer la commande. Si `-n` ou `-c` n'est pas spécifié (voir plus bas), il y aura un seul processus par nœud et chaque processus pourra donc utiliser tous les cores de son nœud via le multithreading (chaque processus gère le multithreading comme il l'entend, Slurm ne gère pas ces questions là).
* `-n` permet de spécifier le nombre de processus à lancer en parallèle. Cette approche est à adopter notamment si vous ne gérez pas le multithreading dans vos processus. Si `-c` n'est pas spécifié, Slurm utilisera un "core" par processus de sorte qu'un nœud pourra se retrouver avec plusieurs processus.
* `-c` permet de spécifier le nombre de core "alloué" par processus. Ce n'est pas un allocation *stricto sensu* vu que les processus réservent autant de threads qu'ils le souhaitent... mais ça permettra de fixer le nombre de HW threads que chaque processus pourra utiliser sans marcher sur les autres. Rq: pour une gestion des affinités, voir par exemple [cette page](https://slurm.schedmd.com/mc_support.html)
* `--mpi=pmi2` pour produire le même effet qu'un `mpirun` (`mpirun` est remplacé par `srun` qui se charge de l'allocation ET d'associer un `rank` à chaque processus).
* `--nodelist=...` permet de spécifier les nœuds à utiliser.

Par défaut, Slurm lance les processus de façon indépendante, et il n'y a que quelques variables d'environnement qui différent. Par exemple, `SLURM_PROCID` donne l'index du processus, `SLURM_NTASKS` donne le nombre de processus, etc... Cf. [cette page](https://slurm.schedmd.com/sbatch.html#lbAK) pour un tour des variables mises en place par slurm.

Comme écrit plus haut, si vous utilisez mpi et si vous voulez que `rank` et `size` soient corrects, il faut ajouter l'option `--mpi=pmi2` et utiliser une commande Slurm comme `srun` ou `sbatch` à la place de `mpirun`, `mpiexec` ou autre commande mpi.

## Lancement différé et graph de taches (sbatch)

Pour envoyer un job dans la file d’attente sans bloquer le terminal (de sorte qu'il est possible de se déloguer sans stopper le calcul), vous pouvez utiliser la commande `sbatch`. Cette dernière prend en entrée un script bash, qui va contenir à la fois les commandes pour lancer le programme, et les options d’exécution telles que les ressources nécessaires (la RAM, nombre de processeurs...), ou des options liées à la gestion du job.

Attention: `sbatch` ne se substitue pas à `srun`. Le script bash sert à définir le contexte, pour pouvoir ensuite y lancer une ou plusieurs commandes `srun`, qui pourront s'exécuter de façon séquentielle ou avec des dépendances fines.

Voici un exemple de script avec un seul srun, qui lancer un script sur 2 nœuds :

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

## Suivi des jobs

`squeue` permet de voir les jobs en attente ou en train de tourner (`R` dans la colonne `ST`).

`sattach` permet d'attacher sur le terminal les E/S d'un job en train de tourner. Ça permet de surveiller l'avancée d'un job, ou par exemple d'interagir avec un debugger. `ctrl-c` permet de détacher de nouveau le job et de le laisser de nouveau tourner en fond (de manière non bloquante).

`scancel` permet permet de supprimer une soumission ou d’arrêter le job s'il est en cours d’exécution.

`sstat` donne des infos sur les ressources utilisées par un job
