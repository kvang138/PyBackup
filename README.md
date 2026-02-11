# 📥🗂️PyBackup
A simple Python script for automated and timestamped data backups.

## Introduction
In this project, I created a Python script to automate data backups with timestamps. The timestamp allows the user to see exactly when each backup was created. The script first archives the files and folders from a specified source directory, adds a timestamp to the archive filename, and then moves the resulting archive to a designated backup destination specified by the user for safekeeping. The default timestamp format is YYYYMMDD_HHMMSS. If the destination folder does not exist, then the script automatically creates it.

Logging, custom timestamp formats, and an option to delete the original source files after successful backup will be added in a future update.

## 🔤🛠️Language
- Python

## 🚀Usage
```
python3 pybackup --backup-source <source-path> --backup-destination <backup-destination-path> --format <archive-format>
```
ℹ️Supported archive formats: tar or zip

💡This script can easily be paired with Windows Task Scheduler or a cron job (on Linux/macOS) to enable fully automated, timestamped backups.

## 📸Screenshots
![PyBackup](https://github.com/kvang138/PyBackup/blob/main/Screenshots/PyBackup.png)


