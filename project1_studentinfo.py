import os, json
import pandas as pd

# Specify the names for JSON and EXCEL files
json_file = "students_information.json"
xlsx_file = "students_information.xlsx"

def help_action():
    
    print("************************************************")
    print("Welcome to Student Information Management System")
    print("Please Choose Below The Action You Want to Perform")
    print("0. Exit Student Information System")
    print("1. Create A New Student Information")
    print("2. Display All Students Information")
    print("3. Inquire A Student Information")
    print("4. Modify A Student Information")
    print("5. Delete A Student Information")
    print("6. Export the information to Excel")
    print("************************************************")
    action = input("Please Choose One Action You Want to Perform: ")
    print("************************************************")
    
    return action

def perform_action():

    while True: # or while 1:

        action = help_action()
         
        if int(action) == 1: 
            
            full_name = input("Input the student's full name: ")
            # family_name = input("Input the student's family name: ")
            # first_name = input("Input the student's first name: ")
            math_score = input("Input the student's math score: ")
            english_score = input("Input the student's english score: ")
            physics_score = input("Input the student's physics score: ")
            chemistry_score = input("Input the student's chemistry score: ")
            biology_score = input("Input the student's biology score: ")
        
            full_name = full_name.rstrip().lstrip()
            full_name = " ".join([s.capitalize() for s in full_name.split()])
            
            total_score = int(math_score) + int(english_score) + int(physics_score) + int(chemistry_score) + int(biology_score)
            
            # create a student dictionary
            score_dict = {"Math": int(math_score),
                          "English": int(english_score),
                          "Physics": int(physics_score),
                          "Chemistry": int(chemistry_score),
                          "Biology": int(biology_score),
                          "Total": total_score}
            
            info_dict = {full_name: score_dict}
                        
            # Save the student dictionary into a JSON file
            if not os.path.exists(json_file):
                with open(json_file, "w") as f:
                    json.dump(info_dict, f, indent=4)
            else:
                with open(json_file, "r") as f:
                    f_dict = json.load(f)
                f_dict.update(info_dict)
                with open(json_file, "w") as f:
                    json.dump(f_dict, f, indent=4)            

        elif int(action) == 2:  
            
            if not os.path.exists(json_file):
                print("Warning: No student information is found")
                exit(1)
            else:
                with open(json_file, "r") as f:
                    f_dict = json.load(f)          
                    # Convert student dictionary into pandas dataframe
                    df = pd.DataFrame.from_dict(f_dict, orient="index")
                    print(df)

        elif int(action) == 3:  

            full_name = input("Input the student's full name: ")
            full_name = full_name.rstrip().lstrip()
            full_name = " ".join([s.capitalize() for s in full_name.split()])
            
            if not os.path.exists(json_file):
                print("Warning: No student information is found")
                exit(1)
            else:
                with open(json_file, "r") as f:
                    f_dict = json.load(f)          
                    for k, v in f_dict.items():
                        if full_name in k:
                            print(k, v)
                            break 
                    else: 
                        print("Can not inquire the student information")
                        exit(1)

        elif int(action) == 4: 
            
            full_name = input("Input the student's full name: ")
            full_name = full_name.rstrip().lstrip()
            full_name = " ".join([s.capitalize() for s in full_name.split()])
            
            if not os.path.exists(json_file):
                print("Warning: No student information is found")
                exit(1)
            else:
                with open(json_file, "r") as f:
                    f_dict = json.load(f)          
                    for k, v in f_dict.items():
                        if full_name in k:
                            print("Input the CORRECT scores for the student")
                            math_score = input("Input the student's math score: ")
                            english_score = input("Input the student's english score: ")
                            physics_score = input("Input the student's physics score: ")
                            chemistry_score = input("Input the student's chemistry score: ")
                            biology_score = input("Input the student's biology score: ")
                            total_score = int(math_score) + int(english_score) + int(physics_score) + int(chemistry_score) + int(biology_score)
                            score_dict = {"Math": int(math_score),
                                        "English": int(english_score),
                                        "Physics": int(physics_score),
                                        "Chemistry": int(chemistry_score),
                                        "Biology": int(biology_score),
                                        "Total": total_score}
                            info_dict = {full_name: score_dict}
                            f_dict.update(info_dict)
                            print("The student information is modified")
                            with open(json_file, "w") as f:
                                json.dump(f_dict, f, indent=4)  
                            break 
                    else: 
                        print("Can not modify the student information")
                        exit(1)

        elif int(action) == 5: 
            
            full_name = input("Input the student's full name: ")
            full_name = full_name.rstrip().lstrip()
            full_name = " ".join([s.capitalize() for s in full_name.split()])
            
            if not os.path.exists(json_file):
                print("Warning: No student information found")
                exit(1)
            else:
                with open(json_file, "r") as f:
                    f_dict = json.load(f)          
                if full_name in f_dict.keys():
                    f_dict.pop(full_name)
                    print("The student information is deleted")
                    with open(json_file, "w") as f:
                        json.dump(f_dict, f, indent=4)   
                    df = pd.DataFrame.from_dict(f_dict, orient="index")
                    print(df)
                else: 
                    print("Can not delete the student information")
                    exit(1)            

        elif int(action) == 6:

            if not os.path.exists(json_file):
                print("Warning: No student information found")
                exit(1)
            else:
                with open(json_file, "r") as f:
                    f_dict = json.load(f)          
                    df = pd.DataFrame.from_dict(f_dict, orient="index")
                    df.to_excel(xlsx_file)
                                    
        elif int(action) == 0:
            
            break

        else: 
            
            print("Error: Choose The Right Action (0-6) You Want to Perform")
            exit(1)


if __name__ == "__main__":
    perform_action()

