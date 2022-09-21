import os

GLOB_PATH = os.getcwd() + "/files"

is_file_or_folder = lambda x : "file" if x == 1 else "folder"


class FileSystem:
    
    def create(self, file_or_folder:str, name:str):
        try: 
            if file_or_folder == "file":
                file = open(GLOB_PATH + f"/{name}", "w")
            elif file_or_folder == "folder":
                os.mkdir(GLOB_PATH + f"/{name}")
        except:
            print(f"An error ocurred while creating a {file_or_folder}")
        else:
            print(f"Successsfully created a {file_or_folder}")
    
    def read(self, file_or_folder:str, name:str):
        try: 
            if file_or_folder == "file":
                file = open(GLOB_PATH + f"/{name}", "r")
                print(file.readlines())
            elif file_or_folder == "folder":
                print(os.listdir(GLOB_PATH))
        except:
            print(f"An error ocurred while reading a {file_or_folder}")
        else:
            print(f"Successsfully reading a {file_or_folder}")

    def delete(self, file_or_folder:str, name:str):
        try: 
            if file_or_folder == "file":
                os.remove(GLOB_PATH + f"/{name}")
                
            elif file_or_folder == "folder":
                os.rmdir(GLOB_PATH + f"/{name}")
        except:
            print(f"An error ocurred while deleting a {file_or_folder}")
        else:
            print(f"Successsfully deleted a {file_or_folder}")


    def update(self, file_or_folder:str, name:str, content):
        try: 
            if file_or_folder == "file":
                file = open(GLOB_PATH + f"/{name}", "a")

                file.write(content)
                
            elif file_or_folder == "folder":
                os.rename(GLOB_PATH + f"/{name}", GLOB_PATH + f"/{content}")
        except:
            print(f"An error ocurred while update a {file_or_folder}")
        else:
            print(f"Successsfully updated a {file_or_folder}")


while True: 
    try:
        print("Interactive File Sytem")
        print("Perform operations on : ")
        print("1. File")
        print("2. Folder")

        file_or_folder = int(input("Enter a valid number: "))


        print(f"1. Create a {is_file_or_folder(file_or_folder)}")
        print(f"2. Read a {is_file_or_folder(file_or_folder)}")
        print(f"3. Update a {is_file_or_folder(file_or_folder)}")
        print(f"4. Delete a {is_file_or_folder(file_or_folder)}")
        print(f"5. Quit File System")

        crud = int(input("Enter a valid number: "))

        fs = FileSystem()

        if crud == 1:
            fs.create(is_file_or_folder(file_or_folder), input(f"Enter a {is_file_or_folder(file_or_folder)} name : "))
        elif crud == 2:
            fs.read(is_file_or_folder(file_or_folder), input(f"Enter a {is_file_or_folder(file_or_folder)} name : "))
        elif crud == 3:
            fs.update(is_file_or_folder(file_or_folder), input(f"Enter a {is_file_or_folder(file_or_folder)} name : "), input(f"Enter the content : "))
        elif crud == 4:
            fs.delete(is_file_or_folder(file_or_folder), input(f"Enter a {is_file_or_folder(file_or_folder)} name : "))
        elif crud == 5:
            quit() 
    except:
        print("Please enter a valid number")