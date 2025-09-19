
import random
from collections import deque

class SnakeAndLadderGame:
    def __init__(self, num_players=2):
        self.board_specials = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78,
                               4: 14, 9: 31, 20: 38, 28: 84, 40: 59, 51: 67, 63: 81, 71: 91}
        self.players = [{'name': f'Player {i+1}', 'position': 1} for i in range(num_players)]
        self.current_player_index = 0
        self.game_over = False

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player_index, steps):
        player = self.players[player_index]
        new_position = player['position'] + steps

        if new_position > 100:
            # Optional: Implement bounce-back if desired, otherwise player waits for exact roll
            # new_position = 100 - (new_position - 100)
            pass # Player stays at current position if roll exceeds 100

        elif new_position in self.board_specials:
            print(f"{player['name']} landed on a {'snake' if new_position > self.board_specials[new_position] else 'ladder'}!")
            player['position'] = self.board_specials[new_position]
        else:
            player['position'] = new_position

        print(f"{player['name']} moved to position {player['position']}")

        if player['position'] == 100:
            self.game_over = True
            print(f"---- {player['name']} wins!!! ----")

    def play_turn(self):
        if self.game_over:
            return

        player = self.players[self.current_player_index]
        print(f"\n{player['name']}'s turn (current position: {player['position']})")
        
        dice_roll = self.roll_dice()
        print(f"Dice rolled: {dice_roll}")

        self.move_player(self.current_player_index, dice_roll)

        if not self.game_over:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def find_shortest_path(self):
        # Implementation using BFS
        # This would be a separate function or method within the class
        # It would return the minimum number of moves to reach 100
        pass

# Game execution
if __name__ == "__main__":
    game = SnakeAndLadderGame(num_players=2)
    while not game.game_over:
        game.play_turn()