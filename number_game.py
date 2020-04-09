import random

RANDOM_LIST = [1,2,3,4,5,6,7,8,9,10]

HIGH_SCORE = 0

print("\n       ***Welcome to the Number Guessing Game***\nTo win the game, you must guess what number im thinking of between 1 to 10\n                I will give you hints along the way!\n               ---------------Let's Begin!-----------")

          
def start_game():
    try_count = 0
    
    global HIGH_SCORE
    
    print("                    The current High Score is {}".format(HIGH_SCORE))
    comp_choice = random.choice(RANDOM_LIST)
    
    game_running = True
    
    while game_running:
        try:
            player_choice = int(input("Pick a number between 1 and 10: "))
            if player_choice < 1 or player_choice > 10:
                raise("Please choose a number between 1 and 10")
        except ValueError as err:
            print("Please choose a number between 1 and 10")
        except TypeError as err:
            print("Please choose a number between 1 and 10")          
        else:    
            if player_choice > comp_choice:
                try_count +=1
                print("Nice try! The number is actually lower!")
                if try_count < 2:
                    print("That was your first attempt")
                else:          
                    print("You have tried {} times".format(try_count))   
            elif player_choice > comp_choice:
                try_count +=1
                print("Nice try! The number is actually lower!")
                if try_count < 2:
                    print("that was your first attempt")
                else:          
                    print("You have tried {} times".format(try_count))
            elif player_choice < comp_choice:
                try_count +=1
                print("Nice try! The number is actually higher!")
                if try_count < 2:
                    print("that was your first attempt")
                else:          
                    print("You have tried {} times".format(try_count))
            else: 
                try_count +=1
                if HIGH_SCORE == 0:
                    HIGH_SCORE = try_count
                elif HIGH_SCORE > try_count and HIGH_SCORE > 0:
                    HIGH_SCORE = try_count                    
                if try_count == 1:
                    print("Wow you got it on your first try! It can't get better than that!")
                else:
                    print("Wow you got it!, it took you {} tries".format(try_count))   
                new_game = input("If you would like to play again? Type in 'YES' : ")
                if new_game == "YES":
                    start_game()
                elif new_game == "NO":
                    print("Thanks for playing! See you next time!")
                    game_running = False  
                else:
                    print("Thanks for playing! See you next time!")
                    game_running = False                               

#if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
start_game()
