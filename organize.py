# Fichier main
import os
from tools import *

racine = "./test";

ListFiles = getFiles(racine);
ListFolders = getFolders(racine);

print("======================================================");
print("NUMBER OF ELEMENTS");
print(lengthFiles(ListFiles));
print("======================================================");
print("FOLDER");
if(detectFoldersDefault(racine, ListFiles)):
    print("Les dossiers sont déjà là");
    printAllFolder(ListFolders);
else:
    print("Il manque des dossiers");
    create_default_folder(racine, ListFiles);
print("======================================================");
print("FILES");
printAllExtensionFiles(ListFiles);
print("======================================================");
sort(racine, ListFiles);