import os
import shutil
# take input of the folder which needs to be taken backup
folder = input("Enter the folder path that needs to taken backup ")
folder_name = os.path.basename(folder)
# function
def create_backup():
# Checks the folder exists
    try:
        backup_folder = "backup_"+folder_name
        if not os.path.exists(folder):
            print(f"{folder_name} not found")

        if not os.path.exists(backup_folder):
            
            shutil.copytree(folder, backup_folder)
        

    except Exception as e:
        print(f"Error as {e}")
    

    
create_backup()

# if not print error
# if exists check if the backup folder exits
# if the backupfolder exists rewrite it 
# if not create backup folder
# copy the content of source folder to backup folder
