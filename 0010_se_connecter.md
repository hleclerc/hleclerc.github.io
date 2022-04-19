# Se connecter sur le cluster

## Depuis le réseau du laboratoire

Vous pouvez vous connecter sur le cluster en tapant

```bash
ssh cinaps
```

ou

```bash
ssh votre_login@cinaps
```

Si le login du laboratoire n'est pas le même que sur votre machine.

### Supprimer le mot de passe

Afind d'éviter d'avoir systématiquement à taper le mot de passe, vous pouvez utiliser une paire de clé ssh.

Si vous n'en avez pas, vous pouvez en créer une en tapant :

```bash
ssh-keygen
```

Remarque : pour des raisons de sécurité, il est conseillé d'utiliser une passphrase non vide. Sur les systèmes modernes, cette passphrase ne sera demandée qu'une fois par session, et sera réutilisée automatiquement pour chaque connection ssh au sein de cette session.

Un fois la paire de clé créée, vous pouvez envoyer une copie de la partie publique avec la commande :

```bash
ssh-copy-id cinaps
```

## Depuis l'extérieur

Cinaps n'étant pas accessible en dehors du réseau du laboratoire, vous devez d'abord vous y connecter pour accéder au cluster.

### À la main

Si vous projetez de ne fonctionner qu'avec des lignes de commande, vous pouvez procéder en deux étapes :
* d'abord en se connectant sur une des machines d'accès extérieur (`ssh <votre_login>@sas1.math.u-psud.fr` ou `ssh <votre_login>@sas2.math.u-psud.fr`, si l'une est plus chargée que l'autre), en utilisant votre mot de passe LDAP (ou votre paire de clé),
* puis en faisant un `ssh cinaps`

### Avec un `.ssh/config`

Pour éviter d'avoir à enchaîner les commandes, vous pouvez dire à ssh que vous devez passer par une machine intermédiaire. Vous pouvez par exemple ajouter 

```bash
Host cinaps_ou_autre_nom_que_vous_choisissez
    ProxyJump <votre_login>@sas1.math.u-psud.fr
    # User <votre_login> # optionnel
    HostName cinaps
```

dans votre fichier `~/.ssh/config` (dans votre home). Ensuite, un

```bash
ssh cinaps_ou_autre_nom_que_vous_choisissez
```

fera pour vous l'enchainement des commandes.

### En utilisant le VPN

Si vous utilisez le [VPN du labo](le lien vers la doc du VPN), vous serez connecté au réseau de ce dernier. Vous pourrez donc directement lancer un `ssh cinaps` même si vous n'êtes pas physiquement à l'IMO.

