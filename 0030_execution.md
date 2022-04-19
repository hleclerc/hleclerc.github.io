# Exécution de commande

La connexion ssh ne vous donne accès qu’à la machine "maître" qui n’est pas dimensionnée pour faire des calculs. Pour profiter du cluster, les ressources doivent être demandées via une file d’attente.

Il existe sur internet des documentations détaillées et extrêmement bien faites pour [le gestionnaire que nous utilisons (slurm)](https://slurm.schedmd.com/documentation.html). Nous vous livrons ici une version synthétique qui correspond à l'usage attendu de notre cluster.

## Lancement immédiat (srun)

Si vous souhaitez lancer une commande simple et attendre le résultat avec un retour direct sur votre terminal, vous pouvez utiliser `srun` :

```bash
srun [options de srun] ma_commande [options pour ma_commande]
```

Voici quelques options importantes:
* `-N` permet de spécifier le nombre de noeuds sur lesquels lancer

## Lancement différé (sbatch)

Pour envoyer un job dans la file d’attente, il faut utiliser la commande sbatch. Pour utiliser cette commande il faut créer un script bash qui va contenir à la fois les commandes pour lancer le programme et les options d’exécution (telles que les ressources nécessaires (la RAM, nombre de processeurs...), ou des options liées à la gestion du job (le nom du job, ...)).

sbatch is used to submit a job script for later execution. The script will typically contain one or more srun commands to launch parallel tasks.

Options supplied on the command line would override any options specified within the script



## Suivi des jobs

sattach is used to attach standard input, output, and error plus signal capabilities to a currently running job or job step. One can attach to and detach from jobs multiple times.

scancel

squeue  reports the state of jobs or job steps. It has a wide variety of filtering, sorting, and formatting options. By default, it reports the running jobs in priority order and then the pending jobs in priority order.

sinfo

##




<!--
 
4.1.3-La commande srun dans le fichier .sh : A REDIGER
4.1.4-Script bash basique :
#!/bin/bash 

# Nom du calcul, répertoire de travail : 
#SBATCH  --job-name=nom_du_job
#SBATCH --chdir=/workdir2/votre_login/chemin_dossier 
# Optionnel, pour être notifié par email : 
#SBATCH  --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=adresse@email.com 
# Sortie standard et d'erreur dans le fichier .output : 
#SBATCH --output=./%j.stdout
#SBATCH --error =./%j.stderr
module load R/3.6.1 
# Eventuellement assignation de quelques variables en entrée du code : 
d=2 
n=100 
nloc=100 
N=20 

R --vanilla --slave "--args $d $n $nloc $N" < script_test.R > sortie 
Vous pouvez télécharger un fichier bash d’exemple, exemple_r.sh pour un calcul non parallèle ainsi qu’un script R, script_test.R, associé.
Un autre exemple (exemple_py.sh) non parallèle avec python (test.py).
Un exemple (exemple_pe.sh) de calcul parallèle avec un script en C qui nécessite d’être compilé via le chargement du module rocks-openmpi et la commande make (qui nécessite le makefile).
4.2-La commande sbatch
Une fois que le script bash est créé, on peut lancer son exécution via la commande sbatch :
sbatch exemple.sh 
  5 - Autres commandes utiles
La commande ’squeue’ liste les jobs soumis avec leur job_identifier. S’ils sont en cours d’exécution leur statut est r, s’ils sont en attente, leur statut est qw :
squeue

sstat donne des infos sur les ressources utilisées par un job

La commande scancel permet de supprimer un job soumis et d’arrêter un job en cours d’exécution :
scancel <job_id>
La commande sacct permet de retrouver des infos sur un job terminé :
sacct <job_id> 
On pourra trouver une doc complète ici.
Sur la page ganglia vous trouverez des graphiques sur l’utilisation du cluster et des différents noeuds (RAM, CPU,...). -->