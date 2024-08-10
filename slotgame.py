import random

characters = ["\U0001F63B","\U0001F98A","\U0001F34D","\U0001F352","\U0001F36B"]
def  game():
    one = random.randint(0,(len(characters)-1))
    two = random.randint(0,(len(characters)-1))
    three = random.randint(0,(len(characters)-1))
    print(f"--> {characters[one]} {characters[two]} {characters[three]}")
    if one == two == three:
        if one == "\U0001F98A":
            if random.randint(0,100) > 50:
                print(f" Good job boss. It is a rank Foxhound job. \U0001F98A")
            else:
                print(f"Amazing boss! \U0001F4B0")
        if random.randint(0,100) > 50:        
            print(f"You won, lucky guy! \U0001F942")
        else:
            print(f"That's the spirit! \U0001F911")
    else:
        print(f"Sorry champ! \U0001F4A9 \U0001F480")       
