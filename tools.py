# Fichiers avec fonctions et tous autres types d'outils nécessaire au bon fonctionnement du projet
from config import list_extension
import os
from pathlib import Path


def getFiles(root):
    Files = [];
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isfile(chemin)):
            Files.append(element);
    return Files;

def getFolders(root):
    Folders = [];
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin)):
            Folders.append(element);
    return Folders;

def lengthFiles(files):
    return len(files);

def printAllFiles(files):
    for element in files:    
        print(element);

def printAllFolder(folders):
    for element in folders:
        print(element);

def detectFolder(root):
    for element in os.listdir(root):
        chemin = Path(root) / element;
        if(os.path.isdir(chemin)):
            return True;
    return False;

def printAllExtensionFiles(files):
    for file in files:
        print(file, " => ", getTypeFile(getExtension(file)), " = ", getExtension(file));

def getExtension(file):
    return Path(file).suffix;

def getTypeFile(extension):
    for types in list_extension: 
        for ext in list_extension.values():
            if(ext == extension):
                return types;
