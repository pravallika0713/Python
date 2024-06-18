import os
import shutil

given_path = input("path to take backup ")

def file_backup():
    file_name = os.path.basename(given_path)
    backup_file = "backup_"+file_name
    try:
        if not os.path.exists(given_path):
            print(f"{given_path} not found")
        
        if not os.path.exists(backup_file):
            shutil.copyfile(given_path, backup_file)

            
    except Exception as e:
        print(f"Error as {e}")
    
def folder_backup():
# Checks the folder exists
    folder_name = os.path.basename(given_path)
    backup_folder = "backup_"+folder_name
    try:
        if not os.path.exists(given_path):
            print(f"{folder_name} not found")

        if not os.path.exists(backup_folder):
            shutil.copytree(given_path, backup_folder)
        

    except Exception as e:
        print(f"Error as {e}")
    


if os.path.isfile(given_path):
    file_backup()
elif os.path.isdir(given_path):
    folder_backup()




