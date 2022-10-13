# The last review done was based on an old file. Please recheck as I have reworked my code
# File was saved and submitted today

from datetime import date   #import file for date now

# store credentials as a list

user_password = {}       #dictionary to store passwords and users

with open('user.txt','r',encoding='utf-8-sig') as f :
    for line in f:
        line = line.strip()
        line = line.split(", ")
        user_password.update({line[0]:line[1]})

username = input("Enter your username\n")
password= input("Enter your password to login\n")

while username not in user_password or password not in user_password[username]: #matching of username and password
    print("You have entered an incorrect username or password, please try again")
    username = input("Enter your username\n")
    password= input("Enter your password to login\n")

# Menu of choices
if username == "admin":
        menu = input("""Select on of the following:
ds - display stats
r - registering new user
a - adding task
va - view all tasks
vm - view my tasks
e - exit
""" ).lower()
else:
        menu = input("""Select on of the following:
a - adding task
va - view all tasks
vm - view my tasks
e - exit
""" ).lower()

if menu == "ds":                                                   #display stats 
    pass
    with open(r"user.txt", "r") as fp:
        lines = len(fp.readlines())
        print("total number of tasks:", lines, "\n")
        with open(r"tasks.txt","r") as fp:
            lines=len(fp.readlines())
            print("Total number of tasks:", lines, "\n")

elif menu == "r":
    if username == "admin":
        f = open("user.txt", "a+")
        new_user = input("Enter username: ")
        new_password = input("Enter password: ")
        confirm_password = input("Confirm password:")
        f.write("\n" + new_user + "," + new_password)
        f.close()
    else:
        print("You are not admin, cannot register new users")
        pass
    
elif menu == "a":
    pass
    username = input("Enter username of user task assigned to:")
    title = input("Enter title of task:")
    description = input("Enter description of task:")
    due = input("Enter due date in format DD Aug YYYY")
    completed = input("Is it completed:Yes/No")
    today = date.today()
    date = today.strftime("%d %b %Y")                      #use date format
    with open("tasks.txt", "a") as f:
        f.write(str(username) + ", "+ str(title) + ", "+ str(description) + ", " + str(due) +", " + str(date) + ", " + str(completed)+ "\n")
        f.close()
        print()
                 
elif menu == "va":
    pass
    with open("tasks.txt","r+") as f:
        for line in f:
            if not line.strip():
                continue
            else:
                print(line)
            line = line.split(",")
##            if username == line[0]:
##                print("Task:\t\t" + line[1]+"\n"
##                        +"Assigned to:\t" + line[0]+"\n"
##                        +"Date assigned:\t" + line[3]+"\n"
##                        +"Due date:\t" + line[4] + "\n"
##                        +"Task Complete?\t" + line[5] 
##                        +"Task description:\n " + line[2]+"\n")   #ignore this section-didnt want to delete
                             
elif menu == "vm":
    pass
    with open("tasks.txt","r") as f:
           for line in f:
              line = line.split(", ")
              if username == line[0]:
                print("Task:\t\t" + line[1]+"\n"
                    +"Assigned to:\t" + line[0]+"\n"
                    +"Date assigned:\t" + line[3]+"\n"
                    +"Due date:\t" + line[4] + "\n"
                    +"Task Complete?\t" + line[5]
                    +"Task description:\n " + line[2]+"\n")             
                  
elif menu == "e":
    print("Goodbye")
    exit()
else:  
    print("You have made a wrong choice, try again")


            

    
    
    
    

              
    
                 
                 

    




