import re
import os
import requests
import wordGuesser
import time
import random
import base64
import ruskiroulette
import slotgame
import schopenhauer as s
import turtle

def randomdraw(number):
    try:
        i = 0
        t = turtle.Turtle()
        t.speed(10)
        turtle.Screen().screensize(800,600)
        while i < int(number):
            n = random.randint(0,600)
            chance = random.randint(0,100)
            if chance < 30:
                t.right(n)
            elif chance < 50:
                t.forward(n)
            elif chance < 70:
                t.left(n)
            else:
                t.circle(n)
            i += 1
        turtle.done()
    except Exception as e:
        print(f"Oh, we have lost the pen! {e}")                
                    
            
        


users = ["root","hector"]
lastOutput = ""
def login(attempts):
    user = str(input("Enter the username:\t"))
    password = str(input("Enter the password:\t"))
    if attempts == 0:      
        print("Bad luck")    
        exit()
    elif user == "root" and password == "root":
        return "root"
    elif user == "hector" and password == "hector":
        return "hector"
    else:
        return login(attempts-1)    
def pwd():
    print(os.getcwd())
def checkhttp(arg):
    try:
        req = requests.get(arg)
        if req.status_code == 200:
            print(f"[{req.status_code}] It's up!")
        elif req.status_code != 200:
            print(f"[{req.status_code}] It's down!")
        else:
            print("Oh wow, an error blocks our way!")
    except Exception as e:
        print(f"An error blocks our way: {e}")            
def randomnumber(start,end):
    if start < end:
        print(random.randint(start,end))
    elif end < start:
        print(random.randint(end,start))
    elif end == start:
        print(start)    
    else:
        print("We couldn't get your number!")                           
def whatismyipv6():
    try:
        req = requests.get("https://api6.ipify.org")
        print(req.text)
    except Exception as e:
        print(f"We couldn't get your ipv6: {e}")        
def run(arg,user):
    try:
        with open(arg,'r+') as f:
            lines = f.readlines()
            if ".arcadia" not in arg:
                print("It is not a '.arcadia' file!")
                return
            if len(lines) == 0:
                print("Empty file!")
                return 
            if lines[0].strip() == "arcadia":
                i = 1
                while i < len(lines):
                    parser(lines[i],user)
                    i+=1
                f.close()    
            else:
                print(f"Make sure your file starts with 'arcadia'")
    except Exception as e:
        print(f"There is a run error! {e}")                        
def randomword(amount):
    wordGuesser.randomword(amount)    
def russianroulette():
    ruskiroulette.game()
def cp(arg,new):
    try:
        with open(arg,"r+") as f:
            data = f.read()
            with open(new,"w+") as n:
                n.write(data)
                n.close()
            f.close()
    except Exception as e:
        print(f"An error occured, {e}")            
def weather(arg="none"):
    if arg == "none":
        try:
            req = requests.get("https://wttr.in/")
            print(req.text)
        except Exception as e:
            print(f"There is an error! {e}")    
    else:
        try:
            req = requests.get(f"https://wttr.in/{arg}")
            print(req.text)
        except Exception as e:
            print(f"There is an error! {e}")    
    print("Source: https://wttr.in/")    
def whatismyip():
    try:
        req = requests.get("https://api.ipify.org")
        print(req.text)
    except Exception as e:
        print(f"Couldn't get your ip: {e}")            
def schopenhauer():
    s.status()                        
def write(arg,content):
    try:
        with open(arg,"w+") as f:
            f.write(content.replace('\\n','\n').replace('\\t','\t'))
            f.close()
    except Exception as e:
        print("An error occured:",e)
def mkdir(arg):
    if os.path.isdir(arg):
        echo("The directory you are trying to create already exists.")
    else:    
        try:
            os.mkdir(arg)
        except Exception as e:
            echo(f"An error occured: {e}")
def rmdir(arg):
        try:
            os.rmdir(arg)
        except Exception as e:
            echo(f"An error occured: {e}")
def slot():
    slotgame.game()                         
def touch(arg):
    try:
        with open(arg,"w") as f:
            f.close()
    except Exception as e:
        print("There is an error,",e)                           
def coinflip():
    if random.randint(0,100) > 50:
        echo("Heads!")
    else:
        echo("Tails!")
def catappend(arg):
    try:
        with open(arg,"a+") as f:
            f.seek(0)
            data = f.readlines()
            for i in data:
                print(i)
            content = str(input("\n"))
            f.write(content.replace('\\n','\n').replace('\\t','\t'))
            f.close()
    except Exception as e:
        print(f"An error occured: {e}")        
                                     
def append(arg,content):
    try:
        with open(arg,"a+") as f:
            f.write(content.replace('\\n','\n').replace('\\t','\t'))
            f.close()
    except Exception as e:
        print(f"An error occured: {e}")                        
def  wordguess():
    wordGuesser.menu()      
def whoami(user):
    echo(user)
def date():
    t = time.time()
    echo(time.ctime(t))
def sleep(arg):
    time.sleep(int(arg))        
def reverse(arg):
    arg = arg.replace("\\n","\n")
    print(str(arg)[::-1])
def upper(arg):
    arg = arg.replace("\\n","\n")
    echo(str(arg).upper())
def lower(arg):
    arg = arg.replace("\\n","\n")
    echo(str(arg).lower())
def rm(arg):
    if arg != "terminal.py" and arg != "wordGuesser.py" and arg != "ruskiroulette.py" and arg != "slot.py":
        if os.path.isfile(arg):
            try:
                os.remove(arg)
            except Exception as e:
                echo(f"An error occured: {e}")
        else:
            print(f"The file '{arg}' doesn't exist.")            
    else:
        echo("Choose a different thing to remove!")           
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
def meow():
    a = r""" 
            *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *
          /     \
          |     |
         /       \
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  jgs|  |  |  |  |  |  |  |  |  |  |  |  |  |"""
    
    print(a)        
def b64(arg,method):
    if method == "encode" or method == "e":
        arg = base64.b64encode(str(arg).encode())
        print(arg.decode('utf-8'))
    elif method == "decode" or method == "d":
        arg = base64.b64decode(str(arg).encode())
        print(arg.decode('utf-8'))
    else:
        print("Enter a valid option!")           

def echo(arg):
    print(arg.replace('\\n','\n'))
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def cd(arg):
    try:
        os.chdir(arg)
    except Exception as e:
        print(f"An error occured: {e}")    
def countup(start,end):
    y = re.search(r"[a-z]",start)
    f = re.search(r"[a-z]",end)
    if y:
        echo("Enter an integer not a string!")
    elif f:
        echo("Enter an integer not a string!")
    else:
        if int(start) <= int(end):
            for i in range(int(start),int(end)+1):
                print(i)
        elif int(end) <= int(start):
            for i in range(int(end),int(start)+1):
                print(i)
        else:
            echo("countup error!")
def countdown(start,end):
    l = re.search(r"[a-z]",start)
    m = re.search(r"[a-z]",end)
    if l:
        echo("Enter an integer not string!")
    elif m:
        echo("Enter an integer not a string!")
    else:
        if int(start) <= int(end):
            for i in range(int(end),int(start)-1,-1):
                print(i)
        elif int(end) <= int(start):
            for i in range(int(start),int(end)-1,-1):
                print(i)
        else:
            echo("countdown error!")                                                                
def ls(arg="none"):
    directory = ""
    if arg == "none":
        directory = os.getcwd()
    else:
        directory = arg    
    contents = os.listdir(directory)    
    print(f"\t{arg}")
    for i in contents:
        if os.path.isdir(i):
            print(f"""
              |
              |
              |
               --- {i}/""")
        else:
            print(f"""
              |
              |
              |
               --- {i}""")    
def b32(arg,method):
    if method == "encode" or method == "e":
        arg = base64.b32encode(str(arg).encode())
        print(arg.decode('utf-8'))
    elif method == "decode" or method == "d":
        arg = base64.b32decode(str(arg).encode())
        print(arg.decode('utf-8'))
    else:
        print("Enter a valid option!")
def b16(arg,method):
    if method == "encode" or method == "e":
        arg = base64.b16encode(str(arg).encode())
        print(arg.decode('utf-8'))
    elif method == "decode" or method == "d":
        arg = base64.b16decode(str(arg).encode())
        print(arg.decode('utf-8'))
    else:
        print("Enter a valid option!")
                                    
def cat(arg):
    try:
        with open(arg,mode="rb") as f:
            print(f.read().decode('utf-8'))
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
                else:
                    echo("Usage: echo 'text'")
            elif "su" in i and "'su'" not in i:
                su()
            elif "whoami" in i and "'whoami'" not in i:
                whoami(username)
            elif "exit" in i and "'exit'" not in i:
                echo("Exiting...")
                exit()
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
            elif "ls" in i and "'ls'" not in i:
                match = re.search(r"'([^']+)",i)
                if match:
                    ls(match.group(1))
                else:
                    ls()    
            elif "cat" in i and "'cat'" not in i and "catappend" not in i:
                match = re.search(r"'([^']+)'",i)    
                if match:
                    cat(match.group(1))
                else:
                    echo("Usage: cat 'file'")
            elif "rm" in i and "'rm'" not in i and "rmdir" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    rm(match.group(1))
                else:
                    echo("Usage: rm 'file'")
            elif "write" in i and "'write'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    write(match[0],match[1])
                else:
                    echo("Usage write 'file' 'content'")                                                                 
            elif "append" in i and "'append'" and "catappend" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    append(match[0],match[1])
                else:
                    echo("Usage: append 'file' 'content'")
            elif "wordguess" in i and "'wordguess'" not in i:
                wordguess()
            elif "date" in i and "'date'" not in i:
                date()
            elif "sleep" in i and "'sleep'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    sleep(match.group(1))
                else:
                    echo("Usage: sleep 'time'")
            elif "coinflip" in i and "'coinflip'" not in i:
                coinflip()
            elif "reverse" in i and "'reverse'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    reverse(match.group(1))
                else:
                    echo("Usage: reverse 'text'")                                         
            elif "b64" in i and "'b64'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                   b64(match[0],match[1])
                else:
                    echo("Usage: b64 'text' 'method'")
            elif "b32" in i and "'b32'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    b32(match[0],match[1])
                else:
                    echo("Usage: b32 'text' 'method'")
            elif "upper" in i and "'b32'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    upper(match.group(1))
                else:
                    echo("Usage: upper 'text'")
            elif "lower" in i and "'lower'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    lower(match.group(1))
                else:
                    echo("Usage: lower 'text'")
            elif "b16" in i and "'b16'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    b16(match[0],match[1])
                else:
                    echo("Usage: b16 'text' 'method'")
            elif "countup" in i and "'countup'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    countup(match[0],match[1])
                else:
                    echo("Usage: countup 'integer' 'integer'")
            elif "countdown" in i and "'countdown'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    countdown(match[0],match[1])
                else:
                    echo("Usage: countdown 'integer' 'integer'")
            elif "mkdir" in i and "'mkdir'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    mkdir(match.group(1))
                else:
                    echo("Usage: mkdir 'directory'")
            elif "touch" in i and "'touch'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    touch(match.group(1))
                else:
                    echo("Usage: touch 'file'")
            elif "pwd" in i and "'pwd'" not in i:
                pwd()
            elif "cd" in i and "'cd'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    cd(match.group(1))
                else:
                    echo("Usage: cd 'directory'")                
            elif "rmdir" in i and "'rmdir'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    rmdir(match.group(1))
                else:
                    echo("Usage: rmdir 'directory'")
            elif "meow" in i and "'meow'" not in i:
                meow()
            elif "russianroulette" in i and "'russianroulette'" not in i:
                russianroulette()
            elif "randomword" in i and "'randomword'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    randomword(int(match.group(1)))
                else:
                    echo("Usage: randomword 'amount'")    
            elif "slot" in i and "'slot'" not in i:
                slot()
            elif "whatismyip" in i and "'whatismyip'" not in i:
                whatismyip()
            elif "weather" in i and "'weather'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    weather(match.group(1))
                else:
                    weather()
            elif "catappend" in i and "'catappend'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    catappend(match.group(1))
                else:
                    echo("Usage: catappend 'file'")            
            elif "schopenhauer" in i and "'schopenhauer'" not in i:
                schopenhauer()        
            elif "run" in i and "'run'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    run(match.group(1),username)
                else:
                    echo("Usage: run 'file'")
            elif "whatismyipv6" in i and "'whatismyipv6'" not in i:
                whatismyipv6()
            elif "cp" in i and "'cp'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    cp(match[0],match[1])
                else:
                    echo("Usage: cp 'source' 'destination'")
            elif "randomnumber" in i and "'randomnumber'" not in i:
                match = re.findall(r"'([^']+)'",i)
                if len(match) == 2:
                    randomnumber(int(match[0]),int(match[1]))
                else:
                    echo("Usage: randomnumber 'integer' 'integer'")
            elif "randomdraw" in i and "'randomdraw'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    randomdraw(int(match.group(1)))
                else:
                    echo("Usage: randomdraw 'integer'")            
            elif "checkhttp" and "'checkhttp'" not in i:
                match = re.search(r"'([^']+)'",i)
                if match:
                    checkhttp(match.group(1))
                else:
                    print("Usage: checkhttp 'url'")                                                                                                                                                                                                            
            else:
                echo("An error occured, undefined command found!")
                break
    elif " && " not in arg:
        if "clear" in arg and "'clear'" not in arg:
            clear()
        elif "echo" in arg and "'echo'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                echo(match.group(1))
            else:
                echo("Usage: echo 'text'")
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
        elif "ls" in arg and "'ls'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                ls(match.group(1))
            else:
                ls()    
        elif "cat" in arg and "'cat'" and "catappend" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                cat(match.group(1))
            else:
                echo("Usage: cat 'file'")          
        elif "rm" in arg and "'rm'" not in arg and "rmdir" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                rm(match.group(1))
            else:
                echo("Usage: rm 'file'")
        elif "write" in arg and "'write'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
             write(match[0],match[1])
            else:
                echo("Usage: write 'file' 'content'")
        elif "append" in arg and "'append'" and "catappend" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                append(match[0],match[1])
            else:
                echo("Usage: append 'file' 'content'")
        elif "wordguess" in arg and "'worguess'" not in arg:
            wordguess()
        elif "date" in arg and "'date'" not in arg:
            date()
        elif "sleep" in arg and "'sleep'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                sleep(match.group(1))
            else:    
                echo("Usage: sleep 'time'")
        elif "coinflip" in arg and "'coinflip'" not in arg:
            coinflip()
        elif "reverse" in arg and "'reverse'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                reverse(match.group(1))
            else:
                echo("Usage: reverse 'text'")
        elif "upper" in arg and "'upper'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                upper(match.group(1))
            else:
                echo("Usage: upper 'text'")
        elif "lower" in arg and "'lower'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                lower(match.group(1))
            else:
                echo("Usage: lower 'text'")
        elif "b64" in arg and "'b64'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                b64(match[0],match[1])
            else:
                echo("Usage: b64 'text' 'method'")
        elif "b32" in arg and "'b32'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                b32(match[0],match[1])
            else:
                echo("Usage: b32 'text' 'method'")
        elif "russianroulette" in arg and "'russianroulette'" not in arg:
            russianroulette()        
        elif "b16" in arg and "'b16'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                b16(match[0],match[1])
            else:
                echo("Usage: b16 'text' 'method'")
        elif "mkdir" in arg and "'mkdir'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                mkdir(match.group(1))
            else:
                echo("Usage: mkdir 'directory'")            
        elif "countup" in arg and "'countup'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                countup(match[0],match[1])
            else:
                echo("Usage: countup 'integer' 'integer'")
        elif "countdown" in arg and "'countdown'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                countdown(match[0],match[1])
            else:
                echo("Usage: countdown 'integer' 'integer'")
        elif "touch" in arg and "'touch'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                touch(match.group(1))
            else:
                echo("Usage: touch 'file'")
        elif "rmdir" in arg and "'rmdir'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                rmdir(match.group(1))
            else:
                echo("Usage: rmdir 'directory'")
        elif "meow" in arg and "'meow'" not in arg:
            meow()
        elif "schopenhauer" in arg and "'schopenhauer'" not in arg:
            schopenhauer()                                                                                                                                         
        elif "cd" in arg and "'cd'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                cd(match.group(1))
            else:
                echo("Usage: cd 'directory'")
        elif "pwd" in arg and "'pwd'" not in arg:
            pwd()
        elif "randomword" in arg and "'randomword'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                randomword(int(match.group(1)))
            else:
                echo("Usage: randomword 'amount'")   
        elif "slot" in arg and "'slot'" not in arg:
            slot()
        elif "whatismyip" in arg and "'whatismyip'" not in arg:
            whatismyip()
        elif "weather" in arg and "'weather'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                weather(match.group(1))
            else:
                weather()
        elif "run" in arg and"'run'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                run(match.group(1),username)
            else:
                print("Usage: run 'file'")
        elif "whatismyipv6" in arg and "'whatismyipv6'" not in arg:
            whatismyipv6()
        elif "cp" in arg and "'cp'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                cp(match[0],match[1])
            else:
                echo("Usage: cp 'source' 'destination'")
        elif "checkhttp" in arg and "'checkhttp'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                checkhttp(match.group(1))
            else:
                echo("Usage: checkhttp 'url'")    
        elif "randomnumber" in arg and "'randomnumber'" not in arg:
            match = re.findall(r"'([^']+)'",arg)
            if len(match) == 2:
                randomnumber(int(match[0]),int(match[1]))
            else:
                echo("Usage: randomnumber 'integer' 'integer'")
        elif "catappend" in arg and "'catappend'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                catappend(match.group(1))
            else:
                echo("Usage: catappend 'file'")
        elif "randomdraw" in arg and "'randomdraw'" not in arg:
            match = re.search(r"'([^']+)'",arg)
            if match:
                randomdraw(int(match.group(1)))
            else:
                echo("Usage: randomdraw 'integer'")                                                                                                         
        else:
            echo("An error occured, undefined command found!")                          
       
                                                                      
def terminal():
    username = login(3)    
    user = ""
    while user != "exit":
        user = str(input(f"{username}@arcadia> "))
        parser(user,username)                 
terminal()
