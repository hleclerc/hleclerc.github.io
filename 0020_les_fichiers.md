# Travailler avec les fichiers sur le cluster

Votre repertoire home est directement accessible depuis le cluster mais le serveur pour ces fichiers n'est pas dimensionné pour les calculs.

Il est fortement recommandé de passer par les *workdir* qui sont dédiés au calcul (qui sont accessible via `/workdir/<votre_login>` ou `/workdir2/<votre_login>` depuis le cluster).

Si vous n'en avez pas, ou si ça ne vous dit rien, vous pouvez passer nous voir (les ingénieurs calcul) pour que nous vous en créons un.

## Accès depuis les outils graphiques

Si vous êtes sur un poste linux, vous pouvez utiliser n’importe quel navigateur de fichier (konqueror, dolphin, nautilus...) et utiliser l’adresse `sftp://cinaps` pour accéder au répertoires et fichiers comme s’ils étaient en local, faire des transferts, etc... Pour Mac ou Windows, vous pouvez installer un logiciel tel que Cyberduck ou Filezilla, par ailleurs documenté [sur la page de l’intranet qui traite des transferts de fichiers de façon générique](la page de l'intranet).

À noter aussi: certain IDE comme visual code permettent de [travailler sur des machines distantes comme si on était en local](https://code.visualstudio.com/docs/remote/ssh). Cette solution est extrêmement pratique si vous avez l'habitude d'utiliser un IDE, puisqu'il gérera tout le processus de développement sur la machine distante (les transferts de fichiers, la compilation, etc...) de façon automatique.

## Montage de repertoires distant

[sshfs](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh) permet de "monter" un répertoire distant comme s'il était local. Ce répertoire sera ensuite accessible par tout votre système que ça soit par les outils graphiques ou par la ligne de commande.

Une fois installé, vous pouvez par exemple taper

```bash
# à ne faire qu'une seule fois pour créer un repertoire vide
mkdir mon_rep
# puis
sshfs cinaps:/workdir/<votre_login> mon_rep
```

et `mon_rep` contiendra un lien synchronisé vers le contenu de votre workdir.

## Transferts en ligne de commande

Pour les plus courageu.ses.x, `scp` ou `rsync` permettent de réaliser des transfert manuels.



