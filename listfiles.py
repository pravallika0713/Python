import os

folders = (input("provide list of folder names")).split()

for folder in folders:

    try:
      files = os.listdir(folder)
      print(f"files in {folder}")
      for file in files:
        print(file)
    except:
       print(f"{folder} Folder doesn't exist")
    
   






   




