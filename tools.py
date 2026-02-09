# Fichiers avec fonctions et tous autres types d'outils nécessaire au bon fonctionnement du projet
from config import list_extension
import os
import shutil
from pathlib import Path


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



# Renvoie le nombre de fichiers
def lengthFiles(files):
    return len(files);

# Affiche les fichiers et dossiers présents des listes et les extensions 
def printAllFiles(files):
    for element in files:    
        print(element);
def printAllFolder(folders):
    for element in folders:
        print(element);
def printAllExtensionFiles(files):
    for file in files:
        print(file, " => ", getExtension(file), " => ", getTypeFile(file));


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

# Fonction qui tri les fichier du dossiers choisi dans les dossiers correspondant à leur nature
def sort(root, files):
    folders = list(list_extension.keys());
    if(detectFileOther(files)):
        folders.append("Others");
    for file in files: 
        type_file = getTypeFile(file);
        source = getSource(root, file);
        folder_to_push = Path(root) / type_file;
        destination = Path(root) / type_file / file;
        counter = 1;
        while(destination.exists()):
            if(counter == 1):
                new_name = f"{fileWithoutExtension(file)}{getExtension(file)}";
            else:
                new_name = f"{fileWithoutExtension(file)}{counter}{getExtension(file)}";
            destination = Path(root) / type_file / new_name;
            counter+=1;
        shutil.move(source, destination);