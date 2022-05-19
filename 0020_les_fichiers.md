# Travailler avec les fichiers sur le cluster

Votre repertoire home est directement accessible depuis le cluster mais le serveur de fichier associé n'est *pas dimensionné pour les calculs*.

Il est fortement recommandé de passer par les répertoires "*workdir*", qui sont créés pour cet usage. Ces derniers sont accessibles via `/workdir/<votre_login>` ou `/workdir2/<votre_login>` depuis le cluster.

Si aucun de ces chemin n'est accessible, vous pouvez passer voir le SVP informatique ou un.e ingénieur.e calcul qui vous créera tout ce qu'il faut.

## Accès depuis les outils graphiques

Si vous êtes sur un poste linux, vous pouvez utiliser n’importe quel navigateur de fichier (konqueror, dolphin, nautilus...) et utiliser l’adresse `sftp://cinaps` pour accéder aux répertoires et fichiers comme s’ils étaient en local, les transferts s'effectuant automatiquement. Pour Mac ou Windows, vous pouvez installer un logiciel tel que Cyberduck ou Filezilla, par ailleurs documenté [sur la page de l’intranet qui traite des transferts de fichiers de façon générique](https://intranet.imo.universite-paris-saclay.fr/-Stockage-sauvegarde-transfert-de-fichiers-72-).

À noter aussi: certain IDE comme [visual code](https://code.visualstudio.com/) permettent de [travailler sur des machines distantes comme si on était en local](https://code.visualstudio.com/docs/remote/ssh). Cette solution est extrêmement pratique si vous avez l'habitude d'utiliser un IDE, ce dernier gérant de façon rapide et transparente tout le processus de développement à distance (synchronisation des fichiers, compilation, etc...).

## Montage de repertoires distant

[sshfs](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh) permet de monter *au niveau du système* un répertoire distant comme s'il était en local. Ce répertoire sera ensuite accessible par *tous* les outils, qu'ils soient graphiques ou en ligne de commande.

Une fois `sshfs` installé, pour créer un lien vers le répertoire distant, vous pouvez taper

```bash
# à ne faire qu'une seule fois pour créer un repertoire vide
mkdir mon_rep
# puis
sshfs cinaps:/workdir/<votre_login> mon_rep
```

et `mon_rep` contiendra un lien synchronisé vers le contenu de votre workdir.

## Transferts en ligne de commande

Pour les plus courageu.ses.x, `scp` ou `rsync` permettent de réaliser les transfert à la main. `rsync` est plus rapide que `scp` lorsqu'il y a beaucoup de fichiers.



