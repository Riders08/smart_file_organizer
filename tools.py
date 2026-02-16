# Fichiers avec fonctions et tous autres types d'outils nécessaire au bon fonctionnement du projet
from config import list_extension, list_icon
import os
import shutil
import datetime
from pathlib import Path


# GETTERS/SETTERS


def fileWithoutExtension(file):
    return file.replace(getExtension(file),"");

# Génére une liste de tous les fichiers
def getFiles(root, ignore, récursif):
    Files = [];
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isfile(chemin)):
            if(ignore is None or getExtension(element) not in ignore):
                Files.append(chemin);          
    if récursif: 
        for element in os.listdir(root):
            chemin = Path(root) / element;
            if(os.path.isdir(chemin)):  
                list_folders_require = list(list_extension.keys());
                if(element != "Others" and element not in list_folders_require):
                    if(ignore is None or ("./" + element) not in ignore):
                        Files.extend(getFiles(chemin, ignore, récursif));          
    return Files;

# Génére une liste de tous les dossiers
def getFolders(root, ignore, récursif):
    Folders = [];
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin)):
            list_folders_require = list(list_extension.keys());
            if(element != "Others" and element not in list_folders_require):
                if(ignore == None or ("./" + element) not in ignore):
                    Folders.append(chemin);
                    if(récursif):
                       Folders.extend(getFolders(chemin, ignore, récursif));  
    return Folders;

# Renvoie les dossiers par défaut actuellement présent à la racine
def getFoldersDéfault(root):
    ListFolderDefault = [];
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin) and (element in list_extension or element == "Others")):
            ListFolderDefault.append(element);
    return ListFolderDefault;

# renvoie l'extension du fichier
def getExtension(file):
    return Path(file).suffix;

#renvoie l'icone qui illustre le type du fichier
def getIcon(file):
    type_file = getTypeFile(file);
    return list_icon.get(type_file, "❓");

# renvoie le type correspondant à l'extension donnée
def getTypeExtension(extension):
    for types in list_extension: 
        for ext in list_extension[types]:
            if(ext == extension):
                return types;            
    return "Others";

# renvoie le type du fichier
def getTypeFile(file):
    return getTypeExtension(getExtension(file));

# revoie l'heure exacte
def getTime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");

#LONGUEURS

# Renvoie le nombre de fichiers
def lengthFiles(files):
    return len(files);

# Renvoie le nombre de dossiers
def lengthFolders(folders):
    list_folders_require = list(list_extension.keys());
    compteur = 0;
    for f in folders:
        if(f != "Others" and f not in list_folders_require):
            compteur+=1;
    return compteur;

# AFFICHAGE

# Affiche les fichiers et dossiers présents des listes et les extensions 
def printAllFiles(files):
    for element in files:    
        print(element);
def printAllFolder(folders):
    for element in folders:
        print(element);
def printAllExtensionFiles(root,files):
    if len(files) <= 0:
        print(f"AUCUN FICHIER SITUÉ DANS {root} NI DANS AUCUN SOUS-DOSSIER");
    for file in files:
        filename = Path(file).name;
        parent = Path(file).parent;
        print(f"Le fichier {filename}, \n    {getIcon(file)} => située : ./{parent},\n        et qui a pour extension {getExtension(file)} doit aller dans le dossier : {root}/{getTypeFile(file)}");    
def printMoveFileLogic(files):
    for file in files:
        filename = Path(file).name
        print(f"[DRY-RUN] Le fichier nommé {filename} irait dans {getTypeFile(file)}");
def printDataFolderDefault(root, ignore, récursif):
    list_folders_default = list(list_extension.keys());
    list_folders = getFoldersDéfault(root);
    for folder in list_folders:
        if folder in list_folders_default or folder == "Others": 
            print(f"{ '❓' if folder == 'Others' else list_icon.get(folder)} {folder} => 📄: {lengthFiles(getFiles(Path(root)/folder, ignore, récursif))} fichier(s) présent(s)");

def printSummary(root, length, ignore, récursif):
    print("===================RESUMER============================");
    print(f" {length} ont été déplacé(s):"); 
    list_folders_default = list(list_extension.keys());
    list_folders = getFoldersDéfault(root);
    for folder in list_folders:
        if folder in list_folders_default or folder == "Others": 
            print(f"{ '❓' if folder == 'Others' else list_icon.get(folder)} {folder} => 📄: {lengthFiles(getFiles(Path(root)/folder, ignore, récursif))} fichier(s) présent(s)");

# CHECKS
# Vérifie si il y a un dossier qui existe déjà à la racine avec ce nom
def folderAlreadyExist(root, filename):
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin)):
            if element == filename:
                return True;
    return False;

# Detect si il y a un dossier
def detectFolder(root):
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin)):
            return True;
    return False;

# Verifie si on a les dossiers par défault
def detectFoldersDefault(root, files, ignore):
    list_folders = [];
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin)):
            list_folders.append(element);
    list_extension_necessary = [];
    for file in files:
        list_extension_necessary.append(getExtension(file));
    require_folders = [];
    for element in list_extension:
        for extension in list_extension_necessary:
            if extension in list_extension[element]:
                require_folders.append(element);
    if(detectFileOther(files)):
        require_folders.append("Others");
    for f in require_folders:
        if(f not in list_folders):
            return False;
    return True;

# Verifie si on a un fichier ayant une extension inconnue
def detectFileOther(files):
    for file in files: 
        if(getTypeFile(file) == "Others"):
            return True;
    return False;

# Verifie si on a bien le fichier de logs
def detectLog(log):
    return os.path.exists(log);

# INITIALISATION DES DOSSIERS

# Création d'un dossier spécifique souhaitez par l'utilisateur
def create_folder_user(root,filename):
        chemin =Path(root)/filename;
        if(os.path.isdir(chemin)):
            print(f"ERREUR : UN DOSSIER DU MÊME NOM EXISTE DÉJÀ ET A ÉTÉ TROUVÉ : ./{chemin}");
        else:
            os.mkdir(Path(root)/ filename);
            print(f"CRÉATION DU DOSSIER {filename} EFFECTUÉE AVEC SUCCÈS")

# Initialisation des dossiers
def create_default_folder(root, files):
    ListExtensionNecessary = [];
    for file in files:
        ListExtensionNecessary.append(getExtension(file));
    for element in list_extension:
        for extension in ListExtensionNecessary:
            if extension in list_extension[element]:
                chemin = Path(element);
                if(os.path.exists(Path(root) / element)):
                    continue;
                else:
                    os.mkdir(Path(root) / chemin.name);
    if(detectFileOther(files)):
        create_default_folder_other(root);

# Initialise un dossier Others si on a des fichiers avec une extension inconnue au bataillon
def create_default_folder_other(root):
    if(os.path.exists(Path(root) / "Others") == False):
        os.mkdir(Path(root) / "Others");

def create_default_rapport(log):
    rapport = open(log, "w");
    with open(log, "a") as rapport:
        rapport.write("LOGS DES DEPLACEMENTS\n\n");
    rapport.close();

# TRI

# Fonction qui tri les fichier du dossiers choisi dans les dossiers correspondant à leur nature
def sort(root, files, log):
    folders = list(list_extension.keys());
    if(detectFileOther(files)):
        folders.append("Others");
    cpt = 0;
    for file in files: 
        chemin = Path(file);
        f = chemin.name;
        type_file = getTypeFile(file);
        source = file;
        folder_to_push = Path(root) / type_file;
        destination = folder_to_push / f;
        counter = 1;
        while(destination.exists()):
            if(counter == 1):
                new_name = f"{fileWithoutExtension(f)}{getExtension(file)}";
            else:
                new_name = f"{fileWithoutExtension(f)}{counter}{getExtension(file)}";
            destination = Path(root) / type_file / new_name;
            counter+=1;
        cpt += 1;
        shutil.move(source, destination);
        if log:
            folder_destination = Path(destination);
            DetailsMove(file, folder_destination.parent, log);
    if log:
        if(cpt == 0):
            AnyMove(log);

# LOGS
# Si fichiers déplacé
def DetailsMove(file, destination, log):
    source = Path(file).parent;
    filename = Path(file).name;
    with open(log, "a") as rapport:
        rapport.write(f"{getTime()}\n");
        rapport.write(f"LOG: Deplacement du fichier {getIcon(file)} => {filename} située dans ./{source} vers la destination ./{destination} de part son type {getTypeFile(file)} via son extension {getExtension(file)}\n\n");
    rapport.close();
    
# Sinon aucun fichiers déplacés
def AnyMove(log):
    with open(log, "a") as rapport:
        rapport.write(f"{getTime()}\n");
        rapport.write(f"AUCUN FICHIER DÉPLACÉ.\n\n");
    rapport.close();