# Fichier main
from tools import lengthFiles, printAllFiles, printAllFolder, detectFolder, getFiles, getFolders, printAllExtensionFiles
import os

racine = "./test";

ListFiles = getFiles(racine);
ListFolders = getFolders(racine);

print("======================================================");
print("NUMBER OF ELEMENTS");
print(lengthFiles(ListFiles));
print("======================================================");
print("FOLDER");
if(detectFolder(racine)):
    printAllFolder(ListFolders);
else:
    print("NO FOLDER FIND");
print("======================================================");
print("FILES");
printAllExtensionFiles(ListFiles);
print("======================================================");
