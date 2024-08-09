import random

def getchar():
    i = str(input("Press <ENTER> to continue."))
def game():
    enemy = 1
    user = 1
    bullet = random.randint(1,8)
    while 1:
        print("Your enemy takes a shot!")
        enemy += 1
        getchar()
        if enemy == bullet:
            print("You won!")
            break
        print("Your turn!")
        user += 1
        getchar()
        if user == bullet:
            print("You lost")
            break            
