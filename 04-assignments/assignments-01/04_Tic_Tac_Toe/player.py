import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
    
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, game, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        
        if game.current_winner == other_player:
            return {'position':None,
                    'score': 1 * (game.num_empty_squares() + 1) if other_player == max_player else -1 * (game.num_empty_squares() + 1)}
        elif not game.empty_squares():
            return {'position': None, 'score': 0}
        
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        
        if game.current_winner or not game.empty_squares():
            return {'position': None, 'score': game.score_board(player)}
        
        for possible_move in game.available_moves():
            game.make_move(possible_move, player)
            sim_score = self.minimax(game, other_player)['score']
            game.board[possible_move] = ' '
            game.current_winner = None
            if player == max_player:
                if sim_score > best['score']:
                    best = {'position': possible_move, 'score': sim_score}
            else:
                if sim_score < best['score']:
                    best = {'position': possible_move, 'score': sim_score}
        return best