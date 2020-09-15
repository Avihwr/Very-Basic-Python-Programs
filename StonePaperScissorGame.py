import random
import time

CHOICES = ['Stone', 'Paper', 'Scissor']

print('1. Stone')
print('2. Paper')
print('3. Scissor')
print("game about to begin")

time.sleep(2)

stone = CHOICES[0]
paper = CHOICES[1]
scissor = CHOICES[2]

i = 1
while i > 0:
    user_name = input("Enter your Name: ")
    user_choice = int(input("Enter your Choice: "))
    if user_choice == 1:
        print(f"{user_name} Choose {stone}")
        choice = random.choice(CHOICES)
        PC = choice
        time.sleep(2)
        print(f"Your PC Chooses {PC}")
        time.sleep(2)
        if PC == 'Paper':
            print(f"-----------Sorry {user_name} Lost to PC-----------")
            print(f"-----------Because PC chose {PC}-----------")
        elif PC == 'Scissor':
            print(f"-----------Congrats {user_name} Won-----------")
            print(f"-----------Because PC chose {PC}-----------")
        elif PC == 'Stone':
            print(f"-----------Match Draw-----------")
            print(f"-----------Because PC chose {PC}-----------")

    elif user_choice == 2:
        print(f"{user_name} Choose {paper}")
        choice = random.choice(CHOICES)
        PC = choice
        time.sleep(2)
        print(f"Your PC Chooses {PC}")
        time.sleep(2)
        if PC == 'Scissor':
            print(f"-----------Sorry {user_name} Lost to PC-----------")
            print(f"-----------Because PC chose {PC}-----------")
        elif PC == 'Stone':
            print(f"-----------Congrats {user_name} Won-----------")
            print(f"-----------Because PC chose {PC}-----------")
        elif PC == 'Paper':
            print(f"-----------Match Draw-----------")
            print(f"-----------Because PC chose {PC}-----------")

    elif user_choice == 3:
        print(f"{user_name} Choose {scissor}")
        choice = random.choice(CHOICES)
        PC = choice
        time.sleep(2)
        print(f"Your PC Chooses {PC}")
        time.sleep(2)
        if PC == 'Stone':
            print(f"-----------Sorry {user_name} Lost to PC-----------")
            print(f"-----------Because PC chose {PC}-----------")
        elif PC == 'Paper':
            print(f"-----------Congrats {user_name} Won-----------")
            print(f"-----------Because PC chose {PC}-----------")
        elif PC == 'Scissor':
            print(f"-----------Match Draw-----------")
            print(f"-----------Because PC chose {PC}-----------")
    else:
        print("choose a valid option")
    q = int(input("Press 0 to stop and 9 to play again"))
    if q == 0:
        break
    elif q == 9:
        continue
print("you want play again?")
i += 1
