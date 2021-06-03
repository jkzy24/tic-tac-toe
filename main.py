from game import Game
import os


def clear():
    """ Clears the console. """
    os.system('clear')


def play_game():
    """ The function of the game tic-tac-toe"""
    clear()
    print("  1 | 2 | 3 \n --- --- --- \n"
          "  4 | 5 | 6 \n --- --- --- \n"
          "  7 | 8 | 9 ")
    player = 'Player_one'
    continue_game = True
    while continue_game:
        position = game.ask(player=player)
        if position is False:
            print("Please enter a number from 1-9.")
            position = game.ask(player=player)
        clear()
        update_and_switch = game.update_and_switch(position, player=player)
        if update_and_switch is False:
            position = game.ask(player=player)
            game.update_and_switch(position, player=player)
        else:
            player = game.switch_player(player)
        continue_game = game.evaluate_winner()

    restart = input("Do you want to play again? (yes or no)\n").lower()
    if restart == 'yes':
        game.list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        play_game()

    else:
        clear()
        print("Bye 👋  Hope you had fun!")


game = Game()

print("Welcome to tic-tac-toe!")
start = input("Would you like to play? (Yes or no)").lower()
if start == "yes":
    play_game()
else:
    clear()
    print("Thanks for your time. 😄")
