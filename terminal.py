import re
import os

users = ["root","hector"]
def login():
    attempts = 3
    user = str(input("Enter the username:\t"))
    password = str(input("Enter the password:\t"))
    while attempts > 0:
        if user == "root" and password == "root":
            return "root"
        elif user == "hector" and password == "hector":
            return "hector"
        else:
            attempts -=1
            print("Try again!")        
    print("Bad luck")
    exit()
def whoami(user):
    echo(user)    
def su():
    terminal()
def echo(arg):
    print(arg)
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")        
        
def terminal():
    username = login()
    user = ""
    while user != "exit":
        user = str(input(f"{username}@arcadia> "))
        if user.startswith("echo") and "'" in user:
            match = re.search(r"'([^']+)'", user)
            if match:
                echo(match.group(1))
        elif user.startswith("echo") and "'" not in user:
            echo("Usage: echo 'arg'")
        if "clear" in user:
            clear()
        if "whoami" in user:
            whoami(username)
        if 'su' in user:
            su()
                                      
terminal()
