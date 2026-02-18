# smart_file_organizer
Objectif, construire un petit projet qui organise automatiquement les fichiers d'un dossier.

## Lancement du projet

Ce projet peut se lancer de différentes façons, finalement tout dépend de ce que vous souhaitez faire.

## Avant tout :
Pour trier un dossier non trié, il est nécessaire de le déplacer à la racine du projet.<br>
Donc, si vous triez votre dossier, veuillez le placer à la racine de ce projet, soit dans le dossier "smart_file_organizer".<br>
Pour ce faire, déplacez votre dossier comme vous le feriez dans n'importe quelle autre situation.<br>
Si vous préférez plus exécuter le programme dans un autre dossier, vous pouvez également utiliser le dossier par défaut configurer dans le projet qui a pour nom "test".<br>
Pour le créer, veuillez tapez les commandes suivantes dans un terminal:
```bash
ls # Nom obligatoire mais utile si vous voulez savoir où vous vous trouvez (Note : Dites-vous que vous êtes au bon endroit quand vous verrez le fichier organize.py)
mkdir test
```

### Si vous souhaitez purement et simplement trier votre dossier, il suffit de :

1. Prendre votre dossier non trié.
2. Le déplacer dans la racine du projet.
3. Lancer la commande suivante :

    ```bash
    python3 organize.py --path nom_du_dossier
    ```
5. Une fois cela fait, vous vous retrouverez avec plusieurs dossiers contenant vos fichiers triés dans votre dossier.<br>Il ne vous restera plus qu'à déplacer ces dossiers triés où vous le souhaitez.

### Si vous souhaitez trier vos fichiers sans importer votre dossier, il suffit de :

1. Prendre votre dossier non trié.
2. Sélectionnez l'ensemble de tous les fichiers situés dans ce dernier. (Que vous souhaiter triées)
3. Les déplacés dans le dossier /test présent dans la base du projet. (Voir le Avant Tout)
4. Lancer la commande suivante :

    ```bash
    python3 organize.py
    ```
5. Une fois cela fait, vous vous retrouverez avec plusieurs dossiers contenant vos fichiers triés dans le dossier /test.<br>Il ne vous restera plus qu'à déplacer ces dossiers triés où vous le souhaitez.

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
Vous pouvez également retrouver un ensemble des détails de déplacement effectué dans le fichier généré nommé "Rapport.log"

D'ailleurs si vous souhaitez générer ce fichier vous même vous pouvez rajouter: 

```
--log nom_du_fichier
```
Par exemple :
```bash
python3 organize.py --log test # Résultat: Un fichier nommé test.log est apparu à la racine du projet
```
Par défaut, le fichier sera un fichier .log.<br>
Néanmoins, si vous voulez absolument un fichier d'une extension différente, vous le pouvez, mais pensez à taper une extension valide.
Par exemple :
```bash
python3 organize.py --log test.txt # Résultat: Un fichier nommé test.txt est apparu à la racine du projet
```

A l'inverse, si vous souhaitez que ces détails ne soient pas pris en compte et ne s'affichent pas, vous pouvez rajouter la commande correspondante:
```bash
--without-log
```
Par exemple :
```bash
python3 organize.py --without-log 
```
> **Attention :** Ne taper pas 
```bash
python3 organize.py --log test --without-log 
```
Cela revient à demander de créer un fichier de détails x tout en demandant de ne rien écrire.

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
Vous vous retrouverez avec les détails de ce que le programme aurait effectué en situation réelle.

### Si vous souhaitez trier votre dossier mais que ce dernier contient un ou plusieurs sous-dossiers, vous pouvez :

#### Soit ignorer vos sous-dossiers et donc tapé la commande de base.

#### Soit trier également vos sous-dossiers, dans ce cas:

1. Prenez votre dossier non trié contenant un ou des sous-dossiers(à trier).
2. Le déplacer dans la racine du projet.
3. Lancer la commande suivante :

    ```bash
    python3 organize.py --path nom_du_dossier --récursif
    ```
5. Une fois cela fait, vous vous retrouverez avec plusieurs dossiers contenant vos fichiers triés dans votre dossier, accompagné des sous-dossiers présent à l'origine dans votre dossier.<br>Il ne vous restera plus qu'à déplacer ces dossiers triés où vous le souhaitez.

> **Attention**: Les fichiers contenus dans vos sous-dossiers seront triés dans les dossiers créés par le programme. Par conséquent, certains fichiers situés à la racine de votre dossier de base pourraient être déplacés et se retrouver mélangés avec ceux provenant de vos sous-dossiers.

### Si vous souhaitez trier votre dossier mais certains éléments ne doivent pas être triés, vous pouvez :

1. Sélectionnez l'un des premiers cas ci-dessus.
2. A l'instant où vous vous apprêtez à taper la commande correspondante, rajouter:

    ```bash
    --ignore extension_valide
    ```
Par exemple :
```bash
python3 organize.py --ignore .txt 
```
Résultat : Tous vos fichiers seront triés et déplacés, sauf tous les fichiers .txt.

Vous pouvez faire de même avec un dossier entier:<br>
Par exemple :
```bash
python3 organize.py --récursif --ignore ./nom_du_dossier
```

### Si vous souhaitez avoir un contrôle total sur l'exécution du programme, vous pouvez :

1. Sélectionnez l'un des premiers cas ci-dessus.
2. A l'instant où vous vous apprêtez à taper la commande correspondante, rajouter:

    ```bash
    --guide
    ```
Par exemple :
```bash
python3 organize.py --guide
```
Résultat : Vous entrerez dans le mode Interactif qui vous permettra de choisir plus d'options.<br><br>
Par exemple, vous pourrez créer des dossiers par défaut en plus de ceux de base, supprimer des dossiers devenus vides suite au tri, déplacer un fichier dans un dossier non adéquat.

## Détails Utiles

Vous l'aurez compris sans difficultés, mais vous pouvez combiner toutes ces options. Si vous souhaitez avoir un ensemble de ces options, vous pouvez taper:
```bash
python3 organize.py --help
```
Néanmoins, combiner toutes ces options est faisable, mais il faut éviter de se contredire.<br>
Par exemple, comme vu plus tôt, évitez de taper:

```bash
python3 organize.py --log test --without-log
```

Ou encore: 

```bash
python3 organize.py --dry-run --guide
```

Ou même de façon encore plus simple:

```bash
python3 organize.py --path ../..////.//./test # Ou n'importe quel autre chemin erroné
```


### Note Importante 

Ce projet peut également se lancer sous forme d'exécutable<br>
Néanmoins, pour le moment, ce dernier n'est pas vraiment opérationnel à 100% étant donné qu'il peut y avoir des soucis liés au chemin de vos dossiers ainsi qu'à l'environnement sur lequel vous lancez ce projet.
Si tout de même vous avez envie d'essayer, vous pouvez taper la commande suivante :
```bash
pyinstaller --onefile --add-data "tools.py:." --add-data "config.py:." organize.py
```
Veuillez au préalable installer pyinstaller: 
```bash
pip install pyinstaller # Sur Linux par exemple
```
Une fois cela fait, rendez-vous dans le dossier "dist" et lancez l'exécutable de la même manière qu'avant mais en s'adaptant au chemin:
```bash
cd dist;
./organize --path ../test # "../" car la racine du projet en lui-même n'est plus la même, pensez à faire de même si vous souhaitez lancer le projet par défaut : ./organize
```

## Compatibilité 

Actuellement ce projet n'a pas pu être effectué sur MacOS, donc rien ne confirme que ce dernier marche sur cet environnement.<br>
En revanche, ce dernier a été testé sous Linux et Windows.(Attention, Windows est plus limitée)

De plus, je précise que ce projet compile et s'exécute sans problème avec:
```bash
Python 3.10.12
Pyinstaller 6.19.0
```
