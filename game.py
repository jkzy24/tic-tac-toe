

class Game:
    def __init__(self):
        self.list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def switch_player(self, player):
        """ Takes current player and returns other player"""
        if player == 'Player_one':
            return 'Player_two'
        elif player == 'Player_two':
            return 'Player_one'

    def ask(self, player):
        """ Takes player as argument and ask for position to put respective symbols, returns position as grid number"""
        if player == 'Player_one':
            symbol = "x"
        elif player == 'Player_two':
            symbol = "o"
        try:
            position = int(input(f"{player}, where would you like to put your {symbol}? (reply in grid number)"))
        except ValueError:
            return False
        return int(position)

    def show_console(self):
        """ Shows tic-tac-toe console"""
        return print(f"   {self.list[0]}| {self.list[1]} | {self.list[2]} \n --- --- --- \n" 
                     f"   {self.list[3]}| {self.list[4]} | {self.list[5]} \n --- --- --- \n" 
                     f"   {self.list[6]}| {self.list[7]} | {self.list[8]}")

    def update_and_switch(self, position, player):
        """Takes position and player as argument and put corresponding symbols to position indicated.
        Returns True if game console is successfully updated and False is not."""

        if self.list[position - 1] == "x" or self.list[position - 1] == "o":
            print("That position is taken. ⛔️")
            self.show_console()
            return False
        else:
            if player == 'Player_one':
                self.list[position - 1] = "x"
                self.show_console()
                return True

            elif player == 'Player_two':
                self.list[position - 1] = "o"
                self.show_console()
                return True

    def evaluate_winner(self):
        """ Checks if there are winning instances and returns False if there is a winner or at the end of game."""
        instances = [self.list[:3], self.list[3:6], self.list[-3:],
                     self.list[0::3], self.list[1::3], self.list[2::3],
                     self.list[0::4], self.list[2:8:2]]
        if ['x', 'x', 'x'] in instances:
            print("Player one wins 🙌 ")
            return False
        elif ['o', 'o', 'o'] in instances:
            print("Player two wins 🙌")
            return False
        elif " " not in self.list:
            print("Draw 🤝")
            return False
        else:
            return True
