import re
import os
import requests

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
def rm(arg):
    if arg != "terminal.py" and arg != "wordGuesser.py":
        os.remove(arg)
    else:
        echo("Choose different thing to remove!")           
def su():
    terminal()
def wget(url,output="none"):
    req = requests.get(url)
    if output == "none":
        print(req.content)
    else:
        with open(output,"wb") as f:
            f.write(req.content)
            f.close()        
def foxsay():
    a = r"""
   /\   /\   Todd Vargo
  //\\_//\\     ____
  \_     _/    /   /
   / * * \    /^^^]
   \_\O/_/    [   ]
    /   \_    [   /
    \     \_  /  /
     [ [ /  \/ _/
    _[ [ \  /_/
    """
    print(a)    
def echo(arg):
    print(arg)
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def ls(arg=os.getcwd()):
    directory = os.listdir(arg)
    print(arg)
    for i in directory:
        print(f"""
              |
              |
              |
               --- {i}""")

def cat(arg):
    try:
        with open(arg,mode="rb") as f:
            print(f.read())
            f.close()                
    except Exception as e:
        echo(f"There is an error! {e}")    
def parser(arg,username):
    if '&&' in arg and "'&&'" not in arg:
        line = arg.split(' && ')
        for i in line:
            if "clear" in i and "'clear'" not in i:
                clear()             
            elif "echo" in i and "'echo'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    echo(match.group(1))
            elif "echo" in i and "'" not in i:
                echo("Usage: echo 'arg'")
            elif "su" in i and "'su'" not in i:
                su()
            elif "whoami" in i and "'whoami'" not in i:
                whoami(username)
            elif "exit" in i and "'exit'" not in i:
                echo("Exiting...")
            elif "foxsay" in i and "'foxsay'" not in i:
                foxsay()
            elif "wget" in i and "'wget'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    wget(match[0],match[1])
                elif len(match) == 1:
                    wget(match[0])
                else:
                    echo("Usage whet 'url' (optional: 'outputFile')")        
            elif "wget" in i and "'" not in i:
                echo("Usage: wget 'url' (optional: 'outputFile')")
            elif "ls" in i and "'ls'" not in i:
                match = re.search(r"'([^']+)",i)
                if match:
                    ls(match.group(1))
                else:
                    ls()    
            elif "cat" in i and "'cat'" not in i:
                match = re.search(r"'([^']+)'",i)    
                if match:
                    cat(match.group(1))
            elif "cat" in i and "'" not in i:
                echo("Usage: cat 'file'") 
            elif "rm" in i and "'rm'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    rm(match.group(1))
                else:
                    echo("Usage: rm 'file'")
            elif "rm" in i and "'" not in i:
                echo("Usage: rm 'file'")                                                   
            else:
                echo("An error occured, undefined command found!")
                break
    elif "&&" not in arg:
        if "clear" in arg and "'clear'" not in arg:
            clear()
        elif "echo" in arg and "'echo'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                echo(match.group(1))
        elif "echo" in arg and "'" not in arg:
            echo("Usage: echo 'arg'")
        elif "su" in arg and "'su'" not in arg:
            su()
        elif "whoami" in arg and "'whoami'" not in arg:
            whoami(username)
        elif "exit" in arg and "'exit'" not in arg:
            echo("Exiting...")
        elif "foxsay" in arg and "'foxsay'" not in arg:
            foxsay()
        elif "wget" in arg and "'wget'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                wget(match[0],match[1])
            elif len(match) == 1:
                wget(match[0])
            else:
                echo("Usage: wget 'url' (optional: 'outputFile')")                        
        elif "wget" in arg and "'" not in arg:
            echo("Usage: wget 'url' (optional: 'outputFile')")
        elif "ls" in arg and "'ls'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                ls(match.group(1))
            else:
                ls()    
        elif "cat" in arg and "'cat'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                cat(match.group(1))
        elif "cat" in arg and "'" not in arg:
            echo("Usage: cat 'file'")            
        elif "rm" in arg and "'rm'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                rm(match.group(1))
        elif "rm" in arg and "'" not in arg:
            echo("Usage: rm 'file'")        
        else:
            echo("An error occured, undefined command found!")                                                          
def terminal():
    username = login()
    user = ""
    while user != "exit":
        user = str(input(f"{username}@arcadia> "))
        parser(user,username)                 
terminal()   
