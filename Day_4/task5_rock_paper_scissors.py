import random
rock = '''      _    
               | |   
 _ __ ___   ___| | __
| '__/ _ | / __| |/ /
| | | (_) | (__|   < 
|_|  |___/ |___|_||_
                     
                     '''
paper = '''
_ __   __ _ _ __   ___ _ __ 
| '_ | / _` | '_ | / _ | '__|
| |_) | (_| | |_) |  __/ |   
| .__/ |__,_| .__/ |___|_|   
| |         | |              
|_|         |_|            
'''

scissor = '''
   ____
  / __ |
 ( (__) |___ ___
  |________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  |____/
'''
game_images = [rock,paper,scissor]
user_choice = int(input("What Do you Choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n"))
# 0, 1, 2

if user_choice >=0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0 :
    print("you typed an invalid number. you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("you lose!")
elif user_choice > computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("It's a draw!")

