# Fichier main
import argparse
import os
from tools import *

parser = argparse.ArgumentParser(description="Organisateur de fichier");

parser.add_argument(
    "--path",
    type=str,
    default="./test",
    help="Chemin d'accès à trier"
);

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Mode Simulation, ne réalise aucun déplacement réel"
);

parser.add_argument(
    "--verbose",
    action="store_true",
    help="Affiche les fichiers déplacés dans le terminal"
);

args = parser.parse_args();

racine = args.path; #Chemin du dossier
dry_run = args.dry_run; #Mode simulation
verbose = args.verbose; #Mode affichage

print("======================================================");
print("INITIALISATION...");
print(f"Dossier cible {racine}");
print(f"Mode Simulation {dry_run}");
print(f"Mode Verbeux {verbose}");
print("======================================================");

ListFiles = getFiles(racine); # Liste de(s) fichier(s) situé(s) dans le dossier 
ListFolders = getFolders(racine); # Liste(s) de(s) dossier(s) dans le dossier
log = "Rapport.txt"; # Fichier log


print("NOMBRES DE FICHIERS");
print(lengthFiles(ListFiles));
print("NOMBRES DE DOSSIERS (Hors dossiers de bases)");
print(lengthFolders(ListFolders));
print("======================================================");
if not detectFoldersDefault(racine, ListFiles):
    if(dry_run):
        print("[DRY-RUN] Création de dossiers par défaut...")
    else:
        print("CONFIGURATION DES DOSSIERS EN COURS...");
        create_default_folder(racine, ListFiles);
print("CONFIGURATION DES DOSSIERS OK");
print("======================================================");
print("ÉTAT DES DOSSIERS AVANT TRI");
if not detectFoldersDefault(racine, ListFiles):
    print("PROBLÈME DE CRÉATION DE DOSSIERS DE TRI");
else:
    printDataFolderDefault(racine);
print("======================================================");
if(detectLog(log) == False):
    create_default_rapport(log);
if(dry_run):
    printMoveFileLogic(ListFiles);
else:
    sort(racine, ListFiles, log);    
    print("TRI EFFECTUÉ");
    printSummary(racine);    
print("======================================================");
if(verbose):
    print(f"PRÉCISION DES FICHIERS SITUÉS DANS {racine}");
    printAllExtensionFiles(racine, ListFiles);