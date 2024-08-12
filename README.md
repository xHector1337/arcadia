# Welcome to The Arcadia, The Land of Fun! 

Well, you are lucky if you made this! You have found it, The Arcadia! Arcadia means arcade plus “-ia”  - the land of arcade- Arcadia is the best virtual arcade machine you can have. It has its own mini, cute shell which you can run Arcadia commands. Alright, less talk more work. Let’s start with its installation. 

# Installing Arcadia 

If you have already installed requests python library, you can skip this part and run Arcadia by cloning or downloading it to your computer! 

You can start with downloading/cloning Arcadia to your computer. You can use this command to clone it: 

`git clone https://github.com/xHector1337/arcadia.git` 

Open up your command line inside of the arcadia directory and install the requirements by writing `pip install –r requirements.txt` 

Well, we are done! You can run it by typing `python terminal.py` or `python3 terminal.py` 

	 

# Basic Usage 

 

As soon as we run it, it’ll ask for a username and a password. Well, there are two users as built-in, `hector` and `root`. The passwords are same with the usernames. You can add your own users by adding another condition to login function. 

 

# Commands 

## System 

+ echo  ‘text’   --> It prints out what you pass as an argument.  

+ clear    --> It cleans the shell screen. 

+ whoami --> It prints out the current user. 

+ pwd --> It prints out the current working directory. 

+ ls ‘directory (optional)’ --> If it takes an argument it prints out the contents of the directory passed as the argument; else it prints out the content of the current working directory. 

+ cd ‘directory’ --> It changes the current working directory as the argument you pass. 

+ cat ‘file’ --> It prints out the contents of the file you pass as the argument. 

+ write ‘file’ ‘content’ --> It writes the content to the file you pass as the arguments. (It creates the file if it doesn’t exist.) 

+ append ‘file’ ‘content’ --> It appends the content to the file you pass as the arguments. (It creates the file if it doesn’t exist.) 

+ catappend ‘file’ --> It is basically “cat + append” It takes ‘file’ name as the argument, prints out its content and takes input to append. 

+ touch ‘file’ --> It creates the file you pass as the argument. 

+ mkdir ‘directory’ --> It creates the directory you pass as the argument. 

+ rm ‘file’ --> It removes the file you pass as the argument. 

+ rmdir ‘directory’ --> It removes the directory you pass as the argument. (Directory must be empty.) 

+ cp ‘source’  ‘destination’ --> It copies the source file to the destination file. (It can create the destination file.) 

+ su --> Changes the current user. 

+ sleep ‘time’ --> The terminal sleeps for the time you pass as the argument. (It takes argument as seconds.) 

+ date --> Prints out the date. 

+ b64 ‘text’ ‘method’ --> It does base64 encoding or decoding job for the text you pass as the argument. 

+ b32 ‘text’ ‘method’ --> It does base32 encoding or decoding job for the text you pass as the argument. 

+ b16 ‘text’ ‘method’ --> It does base16 encoding or decoding job for the text you pass as the argument. 

+ run ‘file’ --> Runs `.arcadia` files. We’ll talk about scripting with arcadia later. 

## Games 

 

+ slot --> Runs the slot game. Test your luck! 

+ wordguess --> Runs the Word Guesser game. 

+ flipcoin --> Flips a coin for you. 

+ russianroulette --> Runs the Russian Roulette game. 

+ schopenhauer --> Schopenhauer is a smart cat who lives in Arcadia. Interact with him by calling this command, he always finds a way to amaze you! 

+ meow --> Prints out a beautiful ascii art. 

+ foxsay --> Prints out a beautiful ascii art made by Todd Vargo. 

+ randomnumber ‘start’ ‘end’ --> Prints out a random number between the range you give as the arguments. (It includes both endpoints.) 

+ randomword ‘amount’ --> Prints out random words as much as you pass as the argument. 

+ randomdraw ‘amount’ --> Randomly draws as much as you pass as the argument. 

## Network 

+ checkhttp ‘url’ --> Checks if the host is up or down, prints out its state. 

+ whatismyip --> Prints out your public ipv4 address by sending a get request to `https://api.ipify.org`. 

+ whatismyipv6 --> Prints out your public ipv6 address by sending a get request to `https://api6.ipify.org`. 

+ wget ‘url’ ‘output file (optional)’ --> Prints out contents of the url you pass as the argument, if you wish you can save it by passing a filename as the second argument. 

 

## Misc 

 

+ reverse ‘text’ --> Prints out the text you pass as the argument in reverse order. 

+ upper ‘text’ --> Prints out the text you pass as the argument in upper case. 

+ lower ‘text’ --> Prints out the capitalized text you pass as the argument in lower case. 

+ countup ‘start’ ‘end’ --> Counts up to end from start you pass as the arguments and prints out every number. (It includes both endpoints.) 

+ countdown ‘start’ ‘end’ --> Counts down to end from start you pass as the arguments and prints out every number. (It includes both endpoints.) 

+ weather ‘place (optional)’ --> Prints out the weather of the place you live or the place you pass as the argument by sending a get request to `https://wttr.in/`. 

 

 

# Scripting 

We have learnt commands and we can go on now. Login as your favourite user and create a arcadia script by typing `write ‘script.arcadia’ ‘arcadia’ `. You can name your script as you wish but it must end with `.arcadia` extension, also file content must be starting with `arcadia`. Then, run `catappend  ‘script.arcadia` to see its content and append new lines to the content. Type `\necho ‘hello’\nwhoami` (Yes, you must use **\n** to add a new line.) After that, write `run ‘script.arcadia` to Arcadia and boom! You have written your first Arcadia script! 

If you are wondering if there is a way other than keep adding new lines for each command, yes there is! This time try running this command; `catappend ‘script.arcadia’`and add this line `\necho ‘we are at:’ && pwd` to the file. Then run the file. Also, you can use the trick on Arcadia’s shell! 

Wow, congrats traveller! Now, you are ready to have fun with Arcadia. Go and try some new tricks! 

 

# Last Words 

 

Thanks for your interest in my project. English is not my first language and I’m not a professional programmer so if you find any mistakes in my project, please contact me! Also, using Arcadia for system-based chores such as removing files, it is your own risk! 

Have fun with Arcadia! 
