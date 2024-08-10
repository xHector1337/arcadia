import random


moods = ["sleepy","playful","hungry","happy","chilling","angry","bored"]

def status():
    mood = random.choice(moods)
    choice = 0
    if mood == "playful":
        if random.randint(0,100) > 50:
            print(r"""
            _,'|             _.-''``-...___..--';)
           /_ \'.      __..-' ,      ,--...--'''
          <\    .`--'''       `     /'
           `-';'               ;   ; ;
     __...--''     ___...--_..'  .;.'
    (,__....----'''       (,..--''   Felix Lee """)
        else:
            print(r"""
                      __     __,
                      \,`~"~` /
      .-=-.           /    . .\
     / .-. \          {  =    Y}=
    (_/   \ \          \      / 
           \ \        _/`'`'`b
            \ `.__.-'`        \-._
             |            '.__ `'-;_
             |            _.' `'-.__)
              \    ;_..--'/     //  \
              |   /  /   |     //    |
        jgs   \  \ \__)   \   //    /
               \__)        './/   .'
                             `'-'`""")    
        print("Schopenhauer wants to play! Go and spend some time with him.")
        choice = int(input("1. Play with Schopenhauer\n2. Leave him alone.\nEnter your choice: "))
        if choice == 1:
            print(r'''
              /\____/\    __
             .'  """"  `,-'  `--.__
        __,- :   -  -  ;  " ::     `-. -.__
     ,-sssss `._  `' _,'"     ,'~~~::`.sssss-.
    |ssssss ,' ,_`--'_    __,' ::  `  `.ssssss|
   |sssssss `-._____~ `,,'_______,---_;; ssssss|
    |ssssssssss     `--'~{__   ____   ,'ssssss|
     `-ssssssssssssssssss ~~~~~~~~~~~~ ssss.-'
          `---.sssssssssssssssssssss.---' Susie Oviatt
                  ''')
            print("Schopenhauer is tired now. He needs to get some rest. :3")
        elif choice == 2:
            print(r"""                               ,
              ,-.       _,---._ __  / \
             /  )    .-'       `./ /   \
            (  (   ,'            `/    /|
             \  `-"             \'\   / |
              `.              ,  \ \ /  |
               /`.          ,'-`----Y   |
              (            ;        |   '
              |  ,-.    ,-'         |  /
              |  | (   |        hjw | /
              )  |  \  `.___________|/
              `--'   `--'""")
            print("Well, he knows how to entertain himself. He does not need you!")
        else:
            print("Do you think you can fool Schopenhauer?")        
    elif mood == "angry":
        print(r"""
                .
       |'.._     __......._    _.-'.
       \M\  ^'.-'          ''-/   /
        :M'._                ^'\ ;
        'MMM'.                  '
       '.MMMM/ ;._            ,,|
         \M; .   /.#\      /''  |
          ;     /d' #.___./d \ ":
          "|    '---:dM   +\-/  ;
           :        _.d._'^.    \
           ',      /    |   ;   ;
             ..,___'.._,:\..' \\   ha""")
        if random.randint(0,100) > 50:
            print("\nSchopenhauer is angry for something and he wants to be alone.")
        else:
            print("\nSchopenhauer is angry, you might spend some time with him to make him happier.\n1. Be with him\n2. Leave him alone.")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(r"""
                  ,
                 \)\_
                /    '. .---._
              =P ^     `      '.
               `--.       /     \
               .-'(       \      |
              (.-'   )-..__>   , ;
              (_.--``    (__.-/ /
                      .-.__.-'.'
                jgs    '-...-'""")
                print("Schopenhauer is better now!")
            elif choice == 2:
                print("Yeah, you should leave him alone.")
            else:
                print("Do you think you can fool Schopenhauer?")
    
    elif mood == "hungry":
        print(r"""
                                    _.---.
                      |\---/|  / ) ca|
          ------------;     |-/ /|foo|---
                      )     (' / `---'
          ===========(       ,'==========
          ||   _     |      |
          || o/ )    |      | o
          || ( (    /       ;
          ||  \ `._/       /
          ||   `._        /|
          ||      |\    _/||
        __||_____.' )  |__||____________
         ________\  |  |_________________
                  \ \  `-.
                   `-`---'  hjw""")
        print("Schopenhauer is hungry!")
        choice = int(input("1. Feed him.\n2. Go away.\nEnter your choice: "))
        if choice == 1:
            print(r"""
    |\      _,,,---,,_
   /,`.-'`'    -.  ;-;;,_
  |,4-  ) )-,_..;\ (  `'-'
 '---''(_/--'  `-'\_)  
                 
                 """)
            print("Well, he is extremely happy and going to take some nap.")   
        elif choice == 2:
            print(r'''
                 ,.     ,.
                {^ \-"-/ ^}
                "   """   "
               { <O> _ <O> }
               ==_ .:Y:. _==
             .""  `--^--' "".
            (,~-~."" "" ,~-~.)
      ------(     )----(     )-----
            ^-'-'-^    ^-'-'-^
      _____________________________
            |"""" /~.^.~\ """"|
      hjw    ,i-i-i(""(  i-i-i.
      `97   (o o o ))"")( o o o)
             \(_) /(""(  \ (_)/
              `--'  \""\  `--'
                     )"")
                    (""/
                     `''')    
            print("Well, Schopenhauer is a clever cat. He does not need you!")
        else:
            print("Do you think you can fool Schopenhauer? He is a genius!")    
    elif mood == "bored":
        print(r"""
                _                       
                \`*-.                   
                 )  _`-.                
                .  : `. .               
                : _   '  \              
                ; *` _.   `*-._         
                `-.-'          `-.      
                  ;       `       `.    
                  :.       .        \   
                  . \  .   :   .-'   .  
                  '  `+.;  ;  '      :  
                  :  '  |    ;       ;-.
                  ; '   : :`-:     _.`* ;
         [bug] .*' /  .*' ; .*`- +'  `*'
               `*-*   `*-*  `*-*'        """)
        print("Schopenhauer is bored. You might spend some time with him.")
        choice = int(input("\n1. Play with him.\n2. Leave him alone."))
    elif choice == 1:
        print(r'''
  --.
 '-. \            |\\_
    \ \           /  a'.
     \ \__..---../  ,__/
      \             |
      |            /
      /\ \-"""-'\ \ \
     / / /_      \ \ \_
  jgs\_\___)      \__)_)''')
        print("Schopenhauer is extremely happy. He loves you too much! :3")
    elif choice == 2:
        print(r''' 
                   .-o=o-.
               ,  /=o=o=o=\ .--.
              _|\|=o=O=o=O=|    \
          __.'  a`\=o=o=o=(`\   /
          '.   a 4/`|.-""'`\ \ ;'`)   .---.
            \   .'  /   .--'  |_.'   / .-._)
             `)  _.'   /     /`-.__.' /
          jgs `'-.____;     /'-.___.-'
                       `"""`''')
        print("Well, he knows how to entertain himself. He does not need you!")
    else:
        print("Do you think you can fool Schopenhauer?")        


status()                                                         
    
