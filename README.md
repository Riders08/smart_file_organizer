# smart_file_organizer
Objectif, construire un petit projet qui organise automatiquement les fichiers d'un dossier.

## Lancement du projet

Ce projet peut se lancer de différentes façons, finalement tout dépend de ce que vous souhaitez faire.

### Si vous souhaitez purement et simplement trier votre dossier non trié, il suffit de :

1. Prendre votre dossier non trié
2. Sélectionnez l'ensemble de tous les fichiers situés dans ce dernier
3. Les déplacés dans le dossier /test présent de base dans le projet
4. Lancer la commande suivante :

    ```bash
    python3 organize.py
    ```
5. Une fois cela fait, vous vous retrouverez avec plusieurs dossiers contenant vos fichiers triés dans le dossier /test.<br>Il ne vous restera plus qu'à déplacer ces dossiers triés où vous le souhaitez.

### Si vous préférez trié votre dossier sans deplacés les éléments présents à l'interieur vous pouvez:

1. Prendre votre dossier non trié
2. Le deplacé dans la racine du projet 
3. Lancer la commande suivante:

    ```bash
    python3 organize.py --path nom_du_dossier
    ```
4. Une fois le programme exécuté, vous aurez votre dossier trié, il ne restera plus qu'à déplacer votre dossier où vous le souhaitez.

### Si vous voulez avoir des détails concernant les déplacements de vos fichiers, vous pouvez :

1. Sélectionnez l'un des deux cas ci-dessus.
2. A l'instant où vous vous apprêtez à taper la commande correspondante, rajouter:

    ```bash
    --verbose
    ```

Par exemple :
```bash
python3 organize.py --verbose
```

### Si vous ne souhaitez pas réellement effectuer de déplacement mais juste voir à quoi cela pourrait ressembler, vous pouvez :

1. Sélectionnez l'un des deux premiers cas ci-dessus.
2. A l'instant où vous vous apprêtez à taper la commande correspondante, rajouter:

    ```bash
    --dry-run
    ```
Par exemple :
```bash
python3 organize.py --dry-run
```

### Note Importante 

Vous pouvez combiner ces fonctionnalités.<br>
Donc, par exemple, si vous souhaitez voir comment serait trié votre propre dossier sans le mettre dans le dossier /test proposé avec des détails, vous pouvez:
```bash
python3 organize.py --path nom_du_dossier --verbose --dry-run
```

## Compatibilité 

Actuellement ce projet n'a pas pu être effectué sur MacOS, donc rien ne confirme que ce dernier marche sur cet environnement
En revanche, ce dernier a été testé sous Linux et Windows.(Attention, Windows est plus limitée)

De plus, je précise que ce projet compile et s'exécute sans problème avec:
```bash
Python 3.10.12
```
