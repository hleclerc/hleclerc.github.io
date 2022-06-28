# Exemple avec pytorch

Pytorch peut par exemple être installé via `pip`, `conda` ou `singularity`. `pip` modifie votre environnement global, ce qui peut poser des soucis lorsque vous voulez utiliser d'autres outils pour d'autres projets qui pourraient demander des dépendances incompatibles...

A contrario, `conda` permettant de créer des environnements spécifiques, vous pourrez en l'utilisant isoler vos installations et projets les uns des autres.

`singularity` permet d'aller encore plus loin en installant un système complet, mais ce n'est pas utile pour les installations simples de pytorch.

Pour cet exemple d'utilisation basique de pytorch, nous utiliserons donc `conda`.

## Installation

Après connexion sur cinaps (cf. [Se connecter](0010_se_connecter.md)), et éventuellement [installation locale de conda](0040_environnement/0020_conda.md) (pas obligatoire, mais utile pour des exécutions plus rapides), vous pouvez taper :

```bash
# creation d'un environnement (vous pouvez changer le nom :) )
conda create --name mon_pytorch
# activation: les exécutions et les commandes d'installation 
# fonctionneront avec cet environnement
conda activate mon_pytorch
# installation des paquets, comme recommandé dans https://pytorch.org/
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

## Test en direct (`srun`)

Pour tester si l'installation fonctionne bien avec CUDA, on pourra utiliser `srun` qui permet de lancer une commande en mode interactif. La commande est lancée sur une autre machine, mais vous avez un retour direct et pouvez interagir avec le clavier.

```bash
# On va sélectionner une machine avec au moins 1 GPU
srun --gres=gpu:1 python -c "import torch; print(torch.cuda.device_count())"
# Vous obtiendrait en principe 1 ou plus
```

## En exemple avec `sbatch`

Pour les calculs long, vous pouvez utiliser `sbatch`, qui lance par défaut les processus en tache de fond. De cette manière vous pouvez vous déconnecter - puis éteindre votre ordinateur et débrancher la prise si vous voulez :) - et le calcul continuera de tourner sur le cluster, sans interruption.

`sbatch` utilise un fichier shell pour définir l'environnement et les commandes à exécuter. Voici un exemple synthétique (cf. la section [Exécution](0030_execution.md) pour plus de détails) :

```bash
#!/bin/bash 

#SBATCH --mail-user=adresse@email.com 
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --job-name=nom_du_job
#SBATCH --output=./%j.stdout
#SBATCH --error=./%j.stderr
#SBATCH --gres=gpu:1

python -c "import torch; print(torch.cuda.device_count())"
```

Vous aurez les résultat dans `num_du_job.stdout` et `num_du_job.stderr`.

Remarque importante : `srun` et `sbatch` copient les l'état des variables d'environnement du shell au moment du lancement, incluant le répertoire de travail, les modules installées, etc... Si par exemple vous avez activé `conda` avant de lancer `srun` ou `sbatch`, l'environnement sera toujours valide dans les commandes qui y sont lancées.

Activer les environnements a posteriori, peut néanmoins être intéressant, notamment pour ne pas avoir à le préparer de nouveau à chaque fois que vous vous connectez. Dans ce cas, le fichier shell pourra ressembler à :

```bash
#!/bin/bash 

# Contexte slurm
#SBATCH ...

# Environnement.
#  Rq: pour conda, il faut redéfinir les fonctions 
#  ces dernières n'étant pas exportés dans les sous-shells :(
source $CONDA_PREFIX/etc/profile.d/conda.sh
#  mais après ça, on peut executer les commandes conda habituelles
conda activate mon_pytorch

# Exécution
python -c "import torch; print(torch.cuda.device_count())"
```

## En exemple avec du calcul parallèle

[Cette page](https://gist.github.com/TengdaHan/1dd10d335c7ca6f13810fff41e809904) contient un exemple complet de calcul parallèle avec slurm.

On pourra essentiellement retenir que c'est à l'utilisat·eur·rice de faire le lien. En particulier, quand on demande à slurm de lancer plusieurs processus, il les lance de façon identique, avec seulement quelques changements dans les variables d'environnement (`SLURM_...`) dont pytorch se moque.

Si vous ne faîtes rien (i.e. pas de lien), le même programme sera lancé *n* fois avec le même jeu de donnée (il fera *n* fois le même calcul). La solution est donc de lire les variables d'environnement mises en place par slurm (par exemple `os.environ['SLURM_PROCID']`) puis de mettre les résultats dans la configuration des classes de pytorch.

