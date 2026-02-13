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

parser.add_argument(
    "--log",
    default="Rapport",
    help="Fichier log qui genère un historique de l'exécution du programme"
);

parser.add_argument(
    "--without-log",
    action="store_true",
    help="Précise si l'on souhaite un rapport des déplacements ou non."
);

args = parser.parse_args();

racine = args.path; #Chemin du dossier
without_log = args.without_log; # Mode log
dry_run = args.dry_run; #Mode simulation
verbose = args.verbose; #Mode affichage
# Fichier log
if without_log :
    log = None
else:
    log = Path(args.log);
    if log.suffix == "":
        log = log.with_suffix(".log"); 


# IL NOUS FAUT: 
# un mode guidage
# un mode recursif
# un mode ignore

if(args.without_log and args.log):
    print("❌ Impossible : vous ne pouvez pas demander à ne pas avoir de log et définir un fichier log en même temps !");
    exit(1);

print("======================================================");
print("INITIALISATION...");
print(f"Dossier cible => {racine}");
print(f"Mode Log => {'Désactivé' if without_log else log}");
print(f"Mode Simulation => {'Activé'if dry_run else 'Désactivé'}");
print(f"Mode Verbeux => {'Activé' if verbose else 'Désactivé'}");
print("======================================================");

ListFiles = getFiles(racine); # Liste de(s) fichier(s) situé(s) dans le dossier 
ListFolders = getFolders(racine); # Liste(s) de(s) dossier(s) dans le dossier
NumberFilesToMove = lengthFilesToMove(ListFiles);

print("NOMBRES DE FICHIERS");
print(NumberFilesToMove);
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
if not without_log:
    if(detectLog(log) == False):
        create_default_rapport(log);
if(dry_run):
    printMoveFileLogic(ListFiles);
else:
    sort(racine, ListFiles, log);    
    print("TRI EFFECTUÉ 👍");
    printSummary(racine, NumberFilesToMove);    
print("======================================================");
if(verbose):
    print(f"PRÉCISION DES FICHIERS SITUÉS DANS {racine}\n");
    printAllExtensionFiles(racine, ListFiles);