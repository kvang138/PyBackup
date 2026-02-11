#
#   This python script will backup all folders and files specified by the backup source to the specified backup destination
#

import os
import shutil
from datetime import datetime
import argparse
from pathlib import Path

argparser = argparse.ArgumentParser(description="Backup argument parser")

# Add the arguments to the argument parsers
argparser.add_argument("-s", "--backup-source", help="The source folder containing the files and folders to backup.", required=True)
argparser.add_argument("-d", "--backup-destination", help="The backup destination folder for the soruce files and folders.", required=True)
argparser.add_argument("-f", "--format", help="The archive file format.", choices=["tar", "zip"], default="zip")

# Only parse the argument we want.
args, _ = argparser.parse_known_args()

# If the destination doesn't exist, then created first before initiating the backup
os.makedirs(args.backup_destination, exist_ok=True)

# The backup file name
backup_filename = f"backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.{args.format}" 

# The backup path with the file name
backup_path = os.path.join(args.backup_destination, backup_filename)

# Perform the backup
try:
    print(f"ℹ️[{datetime.now().strftime("%Y%m%d %H%M%S")}] Now archiving to backup...\r\n\t{Path(args.backup_source).resolve()}{os.path.sep}*.* => {Path(backup_path).resolve()}")
    
    shutil.make_archive(backup_path.replace(f".{args.format}", ""), f"{args.format}", args.backup_source)
    
    print(f"ℹ️[{datetime.now().strftime("%Y%m%d %H%M%S")}] Backup completed successfully.")
except Exception as e:
    # Let user know if there are any error while backing up the files and folders
    print(f"❌[{datetime.now().strftime("%Y%m%d %H%M%S")} Error while backing up.\r\n\t{e}")
