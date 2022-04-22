# Module (pour les besoins les plus courants)

Pour les environnements/librairies/outils les plus courants, vous pouvez tester la commande `module`.

Cette dernière change les variables d'environnement du shell courant pour rendre accessible des programmes installés dans des répertoires qui ne sont pas du système.

## Charger un module

Par exemple, si vous voulez lancer un programme avec R version 3.5.3, vous pouvez taper

```bash
module load R/3.5.3
```

et le shell dans lequel cette commande a été tapée aura accès à cette version de R (exécutable, librairies, etc...).

Si vous souhaitez utiliser la dernière version, vous pouvez taper

```bash
module load R
```

## Modules disponibles

Pour connaître la liste des modules disponibles, vous pouvez taper

```bash
module avail
```

Si vous avez besoin d'un programme ou d'une librairie non disponible par ce biais, mais qui pourrait être un besoin commun, n'hésitez pas à contacter un référent.

## Autres commandes 

Pour connaître la liste des modules chargés :

```bash
module list 
```

Enfin, pour décharger un module :

```bash
module unload <nom_du_module> 
```
