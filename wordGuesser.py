# Arcadia: The Land Of Fun!
import random

print("Welcome to the WordGuesser game!\nChoose a difficulty and start! You'll have attempts depend on the difficulty you choose.\nThe Word list contains adjectives, nouns and infinitive verbs without 'to'(There is not any special names.).\nGood luck!")
words = ["cat","dog","hack","code","house","white","blue","red","llama","eagle","falcon","man","woman","brother","sister","house","street","state","preload","load","code","congratulation","abandon","acquire","addict","rock","roll","punk","hard","agreement","aircraft","ship","learn","holiday","mister","sir","school","walk","meet","again","know","where","sunny","day","memory","moon","lake","live","die","death","cemetery","keyboard","mouse","computer","run","justice","city","hall","angel","decision","result","laptop"]
# I heard those while listening to music :')

def randomChoice(length):
    word  = random.choice(words)
    while len(word) != length:
        word = random.choice(words)
    return word

def menu():
    attempts = 0
    word = ""
    choice = str(input("Choose your difficulty level:\n\t1 - Easy\n\t2 - Medium\n\t3 - Hard\n"))
    match choice:
        case "1":
            number = random.randint(0,100)
            attempts = 5
            if number > 50:
                word = randomChoice(4)
            else:
                word = randomChoice(3)
        case "2":
            attempts = 4
            number = random.randint(0,100)
            if number > 15 and number < 50:
                word = randomChoice(4)
            elif number < 15:
                word = randomChoice(5)
            else:
                word = randomChoice(6)
        case "3":
            attempts = 4
            number = random.randint(0,100)
            if number < 20 and number > 5:
                word = randomChoice(14)
            elif number >= 20 and number < 30:
                word = randomChoice(7)
            elif number >= 30 and number < 45:
                word = randomChoice(8)
            elif number >= 45 and number < 59:
                word = randomChoice(9)
            elif number >= 59 and number < 70:
                word = randomChoice(10)
            elif number >= 70 and number < 79:
                word = randomChoice(11)
            elif number >= 79 and number < 90:
                word = randomChoice(12)
            elif number >= 90 and number < 100:
                word = randomChoice(13)
        case _:
            print("Please enter a right number!")
            menu()       
    print(f"The word's length is {len(word)} and you have {attempts} attempts! Good luck.") 
