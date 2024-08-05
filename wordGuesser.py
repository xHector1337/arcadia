# Arcadia: The Land Of Fun!
import random

print("Welcome to the WordGuesser game!\nChoose a difficulty and start! You'll have attempts depend on the difficulty you choose.\nThe Word list contains adjectives, nouns and infinitive verbs without 'to'(There is not any special names!)\nGood luck!")
words = ["cat","dog","hack","code","eye","redemption","bandana","freedom","game","face","house","white","blue","black","hear","red","pink","purple","consciousness","llama","eagle","falcon","man","woman","brother","sister","house","street","state","preload","load","code","congratulation","abandon","acquire","addict","rock","roll","punk","hard","agreement","aircraft","ship","learn","holiday","mister","sir","school","walk","meet","again","heart","know","where","sun","sunny","day","memory","moon","lake","live","die","death","cemetery","keyboard","mouse","computer","emotion","brain","run","word","justice","city","hall","angel","decision","result","laptop","absorb","destroy","people","fall","way","cowboy","cow","sea","see","light","flash","make","old","smile","snake","eater","solid","youth","school","homelander","deep","butcher","market","super","good","bad","ugly","star","glaze","glance","perfect","winter","jungle","evil","fire","succession","title","liquid","theme","come","handkerchief","phone","console","mask","guess","empire","stay","interstellar","kitty","puppy"]
# I heard those while listening to music :')

def randomChoice(difficulty):
    word = random.choice(words)
    match difficulty:
        case "easy":
            while len(word) != 3 and len(word) != 4:
                word = random.choice(words)
        case "medium":
            while len(word) != 4 and len(word) != 5 and len(word) != 6:
                word = random.choice(words)
        case "hard":
            while len(word) != 7 and len(word) != 8 and len(word) != 9 and len(word) != 10 and len(word) != 11 and len(word) != 12 and len(word) != 13 and len(word) != 14:
                word = random.choice(words)                 
    return word

def wordChecker(word,attempts):
    if int(attempts) == 0:
        print(f"Oh, you are out of luck. The word was '{word}'")
        exit()
    user = str(input("Enter your guess!\n"))
    if user == word:
            print("You have found it!")
            exit()
    if len(user) > 0:
        attempts -= 1
        count = 0
        for i in user:
            if i in word:
                count += 1
                found = str(word).find(i)
                print(f"You're close, {found+1}. character is '{word[found]}'")
        if count == 0:
            print(f"Wrong guess!\nThe word is {'*'*len(word)}\nYou have {attempts} remaining attempts!")
        else:
            print(f"You have {attempts} remaining attempts!")    
        wordChecker(word,attempts)               
        

def menu():
    attempts = 0
    word = ""
    choice = str(input("Choose your difficulty level:\n\t1 - Easy\n\t2 - Medium\n\t3 - Hard\n"))
    match choice:
        case "1":
            attempts = 5
            word = randomChoice("easy")
        case "2":
            attempts = 4
            word = randomChoice("medium")
        case "3":
            attempts = 4
            word = randomChoice("hard")
        case _:
            print("Please enter a right number!")
            menu()
    if len(word) == 0:
        print("You got an error! Please enter your choice again!")
        menu()   
    print(f"The word is {'*'*len(word)}")        
    print(f"The word's length is {len(word)} and you have {attempts} attempts! Good luck.")
    wordChecker(word,attempts)
menu()
