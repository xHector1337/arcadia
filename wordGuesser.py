# Arcadia: The Land Of Fun!
import random

words = ["cat","dog","hack","code","eye","redemption","clear","bandana","wise","freedom","game","face","house","white","blue","black","hear","red","pink","purple","wind","consciousness","llama","eagle","falcon","man","woman","brother","sister","life","paint","angry","river","house","street","state","preload","load","code","congratulation","abandon","acquire","addict","rock","roll","punk","hard","agreement","aircraft","ship","learn","holiday","mister","sir","school","walk","meet","again","heart","teacher","mom","dad","father","","know","where","sun","sunny","day","memory","moon","lake","live","die","death","cemetery","keyboard","mouse","computer","emotion","brain","run","word","justice","city","hall","angel","despicable","decision","result","laptop","absorb","destroy","people","fall","way","cowboy","cow","drive","driver","sea","see","light","flash","make","old","smile","snake","eater","solid","youth","school","homelander","deep","butcher","monkey","sloth","market","super","good","bad","ugly","star","glaze","glance","perfect","winter","jungle","boy","evil","fire","succession","title","liquid","theme","come","handkerchief","happy","girl","phone","console","mask","guess","empire","stay","ocean","climb","jump","love","interstellar","kitty","sell","world","puppy","west","north","east","south","soap","have","take","personal","alone","care","tired"]
# I heard those while listening to music :')
stored = []
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
            while len(word) < 7:
                word = random.choice(words)                 
    return word

def wordChecker(word,attempts,hints):
    if int(attempts) == 0:
        print(f"Oh, you are out of luck. The word was '{word}'")
        return
    user = str(input("Enter your guess!\n"))
    if user == "abcdefghijklmnopqrstuvwxyz" or user == "abcdefghijklmnopqrstuvwxyz".upper():
        print("Loser!")
        return
    if user == "hint" and hints > 0:
        hints -=1
        h = random.randint(0,(len(word)-1))
        if h in stored:
            while h in stored:
                h = random.randint(0,(len(word)-1))
        stored.append(h)
        print(f"There you go, here is your hint:\n{h+1}. character of the word is {word[h]}")
        wordChecker(word,attempts,hints)
    elif hints == 0 and user == "hint":
        print("You don't have any hints left!")
        wordChecker(word,attempts,hints)    
    if user == word:
            print("You have found it!")
            return
    if len(user) > 0 and user != "hint":
        attempts -= 1
        count = 0
        for i in user:
            if i in word:
                count += 1
                found = str(word).find(i)
                print(f"You're close, {found+1}. character is '{word[found]}'")
        if count == 0:
            print(f"Wrong guess!\nThe word is {'*'*len(word)}\nYou have {attempts} remaining attempts and {hints} hints!\n")
        else:
            print(f"You have {attempts} remaining attempts and {hints} hints!")    
        wordChecker(word,attempts,hints)               
        

def menu():
    print("Welcome to the WordGuesser game!\nChoose a difficulty and start! You'll have attempts depend on the difficulty you choose.\nThe Word list contains adjectives, nouns and infinitive verbs without 'to'(There is not any special names!)\nGood luck!")
    attempts = 0
    hints = 3
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
    print(f"The word's length is {len(word)}. You have {attempts} attempts and {hints} hints!\nYou can use your hints by typing 'hint'\nGood luck.")
    wordChecker(word,attempts,hints)
def randomword(amount):
    count = 0
    while count != amount:
        i = random.choice(words)
        print(i)
        count +=1
