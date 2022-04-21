# Chargement de l’environnement de travail (interpréteur, compilateur...)

Pour faire cohabiter les différentes versions des programmes que les utilisateurs souhaitent utiliser, l’environnement par défaut est minimal.

## module (pour les besoins les plus courants)

Pour les environnements/librairies/outils les plus courants (ceux que nous avons installés), vous pouvez utiliser la commande `module`.

Par exemple, si vous voulez lancer un programme avec R version 3.5.3, vous pouvez taper

```bash
module load R/3.5.3
```

et le shell dans lequel cette commande a été tapée aura accès à cette version de R (exécutable, librairies, etc...).

Pour connaître la liste des modules disponibles (C++, Python, R, etc...), vous pouvez taper

```bash
module avail
```

Pour connaitre la liste des modules chargés :

```bash
module list 
```

Enfin, on peut détacher un module via

```bash
module unload <nom_du_module> 
```

## conda (plutôt pour Python)

Pour une plus grande liberté sur les environnements Python, [miniconda](https://docs.conda.io/en/latest/miniconda.html) vous permettra d'installer des environnements quasi-complets en local.

Compte-tenu de la taille des répertoires générés, nous vous conseillons d'installer les environnements dans votre workdir.

Conda fonctionne bien pour les modules Python qui ne demandent pas de dépendances "système" compliquées.

## singularity (pour tous les environnements)

Singularity peut être vu comme le "docker du calcul". Il résoud tous les problèmes d'environnement au prix d'une besoin de stockage légèrement plus élevé (mais pas si gigantesque par rapport à conda par exemple)

Il permet de définir un système complet sans nécessiter d'accès root. Il devient donc possible d'installer n'importe quel package dans un environnement confiné.

Les images peuvent par ailleurs être utilisées sur le cluster comme en local, permettant d'utiliser les mêmes environnements et compilations sur votre machine et sur le cluster.

Pour installer singularity en local, vous pourrez trouver de [très bons tutoriels](https://sylabs.io/guides/3.0/user-guide/installation.html). Sur le cluster, Singularity est disponible via les modules (`module load Singularity`)

### Un exemple avec pytorch

Singularity peut créer des images avec son propre format de description ou à partir de données docker. Une grande quantité d'image sont référencées notamment dans les serveurs de sylabs.io (`singularity search pytorch` par exemple) ou [dockerhub](https://hub.docker.com/).

Si par exemple on choisit la version officielle, on pourra taper :

```bash
singularity pull docker://pytorch/pytorch
```

qui créera un fichier `pytorch.sif`, utilisable pour lancer une ligne de commande

```bash
singularity shell pytorch.sif
```

ou pour exécuter un programme (par exemple un script python)

```bash
singularity run pytorch.sif python mon_fichier.py [mes options]
```

### Images les plus courantes

Afin 


### GPU

Pour donner accès aux GPUs, il suffit d'ajouter `--nv` aux options de lancement (`run`, `shell`, ...) comme dans :

```bash
singularity shell --nv pytorch_latest.sif
# nvidia-smi devrait vous lister les GPU disponibles
```

### MPI

TODO

### Accès à l'environnement depuis un IDE

Pour que l'IDE ait connaissance des librairies installées (pour l'autocomplétion par exemple) et puisse lancer des compilations ou des debugs dans cet environnement, vous pouvez le référencer comme une machine distante dans votre `.ssh/config`. Par exemple, en y ajoutant 

```bash
Host mon_env
    RemoteCommand singularity shell /.../le.sif # pytorch_latest.sif sur l'exemple précédant
    HostName localhost
```

Ensuite, vous pouvez utiliser les capacité "remote ssh" de votre IDE (ctrl-shift-p puis `remote-ssh connect to host` pour ce qui concerne visual code) pour vous connecter sur cette machine virtuelle (ce chroot pour être plus précis).



### Création d'images

setbuid

```bash
# singularity build --fakeroot test.sif test.def

Bootstrap: library
From: ubuntu:21.04
Stage: build

%post
    apt-get -y update 
    apt-get -y install software-properties-common 
    add-apt-repository -y universe 
    apt-get -y update 
    apt-get -y install python-is-python3 gcc libopenmpi-dev

%runscript
    echo "Container was created $NOW"
    echo "Arguments received: $*"
```
