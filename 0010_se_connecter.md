# Se connecter sur le cluster

## Depuis le réseau du laboratoire

Vous pouvez vous connecter sur le cluster en tapant

```bash
ssh cinaps
```

Si le login du laboratoire n'est pas le même que sur votre machine, vous pouvez écrire :

```bash
ssh votre_login@cinaps
```

### Se connecter sans mot de passe

Afin d'éviter d'avoir à taper le mot de passe à chaque connection, vous pouvez passer par une paire de clés ssh.

Si vous pas de paire de clés, vous pouvez en créer une en tapant :

```bash
ssh-keygen
```

Remarque : pour des raisons de sécurité, il est conseillé d'utiliser une passphrase non vide. Sur les systèmes modernes, cette passphrase ne sera demandée qu'une fois par *session* (plutôt que une fois par connection), et sera réutilisée automatiquement pour chaque connection ssh au sein de cette session.

Une fois la paire de clé créée, vous pouvez envoyer sur le cluster une copie de la partie publique avec la commande :

```bash
ssh-copy-id cinaps
```

De cette façon, `ssh cinaps` devrait fonctionner sans mot de passe ) chaque connection.

## Depuis l'extérieur

Cinaps n'étant pas accessible en dehors du réseau du laboratoire, vous devez d'abord vous connecter sur une machine d'accès extérieur pour pouvoir accéder au cluster.

### À la main

Si vous projetez de ne fonctionner qu'avec des lignes de commande, vous pouvez procéder en deux étapes :
* d'abord en se connectant sur une des machines d'accès extérieur (`ssh <votre_login>@sas1.math.u-psud.fr` ou `ssh <votre_login>@sas2.math.u-psud.fr`, si l'une est plus chargée que l'autre), en utilisant ou bien votre mot de passe LDAP ou bien une paire de clé (en envoyant la clé publique sur votre HOME du laboratoire par exemple avec `ssh-copy-id sas1.math.u-psud.fr` si ce n'est pas déjà fait),
* puis en tapant `ssh cinaps`

### Avec un `.ssh/config`

Pour éviter d'avoir à enchaîner ces étapes, vous pouvez dire à ssh que vous devez d'abord passer par une machine intermédiaire pour accéder ensuite à cinaps. Dans votre fichier `~/.ssh/config` (dans votre home), vous pouvez par exemple ajouter :

```bash
Host <cinaps_ou_autre_nom_que_vous_choisissez>
    ProxyJump <votre_login>@sas1.math.u-psud.fr
    # User <votre_login> # optionnel: à utiliser si le login n'est pas le même que sur votre machine
    HostName cinaps
```

Ensuite, vous pourrez directement accéder à cinaps en tapant

```bash
ssh <cinaps_ou_autre_nom_que_vous_choisissez>
```

### En utilisant le VPN

Si vous utilisez le [VPN du labo](le lien vers la doc du VPN), vous serez virtuellement connecté au réseau de ce dernier. Vous pourrez donc directement lancer un `ssh cinaps` même si vous n'êtes pas physiquement à l'IMO.

