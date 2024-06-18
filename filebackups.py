import os
import shutil
#  take input of file which you want to take backup
file_path = input("Enter the file path to take backup ")
file_name = os.path.basename(file_path)
backup_file = "backup"+file_name
#  search for that file
#  if not found return "not found"
def find_file():
    try:
        if os.path.exists(file_path):

            os.open(backup_file,os.O_CREAT)
            
            shutil.copyfile(file_name, backup_file)

        else:
            print(f"{file_name} not found")
            
    
    except Exception as e:
        print(f"Error as {e}")
    
find_file()

#  if found create a new file and copy context of old file




