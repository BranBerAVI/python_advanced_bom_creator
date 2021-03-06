import subprocess
import os
import platform

choice = 0

def clear_screen():
    system = platform.system()

    if(system == "Linux"):
        subprocess.call("clear", shell=True)
    else:
        subprocess.call("cls", shell=True)

while(choice != 2):
    
    print("-"*20)
    print("1. Create bom from project directory")
    print("2. Exit")
    print("-"*20)
    choice = int(input("Enter Choice: "))
    
    clear_screen()

    if(choice < 1 or choice > 2):
        print("Invalid Choice..")

    dir_input = ""
    requirement_contents = ""

    current_dir = os.getcwd()

    

    if(choice == 1):
        while(not os.path.isdir(dir_input)):
            dir_input = input("Enter the file path of your project: ")
            requirement_list_contents = []

            if(not os.path.isdir(dir_input)):
                print("Folder does not exist")
            else:
                print("Looking for requirements...")
                for subdir, dirs, files in os.walk(dir_input):
                    for file in files:
                        if file.lower() == "requirements.txt":
                            requirements_file_path = os.path.join(subdir, file)   
                                                    
                            requirements_file = open(requirements_file_path, "r")
                            
                            requirement_contents = requirements_file.readlines()
                            
                            requirement_list_contents = list(set([*requirement_list_contents, *requirement_contents]))
                            requirements_file.close()

                if(requirement_list_contents != []):

                    if(not os.path.isdir("Mother_Of_All_Requirements")):
                        os.mkdir("Mother_Of_All_Requirements")

                    os.chdir("Mother_Of_All_Requirements")

                    mother_of_all_reqs = open("requirements.txt", "w")
                    mother_of_all_reqs.writelines(requirement_list_contents)
                    mother_of_all_reqs.close()

                    subprocess.run(["cyclonedx-py", "-o", "bom.xml"], shell=True)
                    os.chdir(current_dir)

                    print("done!")
                


