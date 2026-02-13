# Fichiers avec fonctions et tous autres types d'outils nécessaire au bon fonctionnement du projet
from config import list_extension, list_icon
import os
import shutil
import datetime
from pathlib import Path


# GETTERS/SETTERS

# Génére le chemin du fichier
def getSource(root, file):
    return Path(root) / file;


def fileWithoutExtension(file):
    return file.replace(getExtension(file),"");

# Génére une liste de tous les fichiers
def getFiles(root):
    Files = [];
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isfile(chemin)):
            Files.append(element);
    return Files;

# Génére une liste de tous les dossiers
def getFolders(root):
    Folders = [];
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin)):
            Folders.append(element);
    return Folders;

# renvoie l'extension du fichier
def getExtension(file):
    return Path(file.casefold()).suffix;

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

#OTHERS

# Renvoie le nombre de fichiers
def lengthFiles(files):
    return len(files);

def lengthFilesToMove(files):
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
    for file in files:
        print(f"\nLe fichier {file}, \n    {getIcon(file)} => située : {getSource(root ,file)},\n        et qui a pour extension {getExtension(file)} doit aller dans le dossier : {getTypeFile(file)}");    
def printMoveFileLogic(files):
    for file in files:
        print(f"[DRY-RUN] Le fichier nommé {file} irait dans {getTypeFile(file)}");
def printDataFolderDefault(root):
    list_folders_default = list(list_extension.keys());
    list_folders = getFolders(root);
    for folder in list_folders:
        if folder in list_folders_default or folder == "Others": 
            print(f"{ '❓' if folder == 'Others' else list_icon.get(folder)} {folder} => 📁: {lengthFiles(getFolders(Path(root)/folder))} dossier(s) présent(s), 📄: {lengthFiles(getFiles(Path(root)/folder))} fichier(s) présent(s)");

def printSummary(root, length):
    print("===================RESUMER============================");
    print(f" {length} ont été déplacé(s):"); # MARCHE PAS ENCORE
    list_folders_default = list(list_extension.keys());
    list_folders = getFolders(root);
    for folder in list_folders:
        if folder in list_folders_default or folder == "Others": 
            print(f"{ '❓' if folder == 'Others' else list_icon.get(folder)} {folder} => 📁: {lengthFiles(getFolders(Path(root)/folder))} dossier(s) présent(s), 📄: {lengthFiles(getFiles(Path(root)/folder))} fichier(s) présent(s)");
# CHECKS

# Detect si il y a un dossier
def detectFolder(root):
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin)):
            return True;
    return False;

# Verifie si on a les dossiers par défault
def detectFoldersDefault(root, files):
    list_folders = getFolders(root);
    require_folders = list(list_extension.keys());
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

# Initialisation des dossiers
def create_default_folder(root, files):
    for element in list_extension:
        if(os.path.exists(Path(root) / element)):
            continue;
        else:
            os.mkdir(Path(root) / element);
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
    if(len(files) <= 0):
        AnyMove(log);
    for file in files: 
        type_file = getTypeFile(file);
        source = getSource(root, file);
        folder_to_push = Path(root) / type_file;
        destination = folder_to_push / file;
        counter = 1;
        while(destination.exists()):
            if(counter == 1):
                new_name = f"{fileWithoutExtension(file)}{getExtension(file)}";
            else:
                new_name = f"{fileWithoutExtension(file)}{counter}{getExtension(file)}";
            destination = Path(root) / type_file / new_name;
            counter+=1;
        shutil.move(source, destination);
        DetailsMove(root, file, destination, log);

# LOGS
# Si fichiers déplacé
def DetailsMove(root, file, destination, log):
    source = getSource(root, file);
    with open(log, "a") as rapport:
        rapport.write(f"{getTime()}\n");
        rapport.write(f"LOG: Deplacement d'un fichier {getIcon(file)} => {file} située {source} vers la destination {destination} de part son type {getTypeFile(file)} via son extension {getExtension(file)}\n\n");
    rapport.close();
    
# Sinon aucun fichiers déplacés
def AnyMove(log):
    with open(log, "a") as rapport:
        rapport.write(f"{getTime()}\n");
        rapport.write(f"AUCUN FICHIER DÉPLACÉ.\n\n");
    rapport.close();