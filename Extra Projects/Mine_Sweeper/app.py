# import random
# import re
# class Board():
#     def __init__(self , dimsize, num_mines):
#         self.dimsize = dimsize
#         self.num_mines = num_mines
#         self.board = self.make_new_board()
#         self.assign_values()
#         self.dug = set()
    
#     def make_new_board(self):
#         board = [[None for _ in range(self.dimsize)] for _ in range(self.dimsize)]
#         bombs_planted = 0
#         while bombs_planted < self.num_mines:
#             loc = random.randint(0,self.dimsize**2 - 1)
#             row = loc // self.dimsize
#             col = loc % self.dimsize
            
#             if board[row][col] == '*':
#                 continue
            
#             board[row][col] = '*'
#             bombs_planted += 1
        
#         return board

#     def assign_values(self):
#         for r in range(self.dimsize):
#             for c in range(self.dimsize):
#                 if self.board[r][c] == '*':
#                     continue
#                 self.board[r][c] = self.get_num_neighboring_mines(r,c)

#     def get_num_neighboring_mines(self, row, col):
#         num_neighboring_mines = 0
#         for r in range(max(0, row - 1), min(self.dimsize - 1, row + 1) + 1):
#             for c in range(max(0, col - 1), min(self.dimsize - 1, col + 1) + 1):
#                 if r == row and c == col:
#                     continue
#                 # if r >= 0 and r < self.dimsize and c >= 0 and c < self.dimsize:
#                 if self.board[r][c] == '*':
#                     num_neighboring_mines += 1

#         return num_neighboring_mines

#     def dig(self, row, col):
#         self.dug.add((row,col))

#         if self.board[row][col] == '*':
#             return False
#         elif self.board[row][col] > 0:
#             return True

#         for r in range(max(0, row - 1), min(self.dimsize - 1, row + 1) + 1):
#             for c in range(max(0, col - 1), min(self.dimsize - 1, col + 1) + 1):
#                 if (r, c) in self.dug:
#                     continue
#                 self.dig(r, c)

#         return True

#     def __str__(self):
#         visible_board = [[None for _ in range(self.dimsize)] for _ in range(self.dimsize)]
#         for row in range(self.dimsize):
#             for col in range(self.dimsize):
#                 if (row,col) in self.dug:
#                     visible_board[row][col] = str(self.board[row][col])
#                 else:
#                     visible_board[row][col] = ' '
        
#         string_rep = ''
#         widths = []
#         for idx in range(self.dimsize):
#             columns = map(lambda x: x[idx], visible_board)
#             widths.append(
#                 len(
#                     max(columns, key = len)
#                 )
#             )

#         indices = [i for i in range(self.dimsize)]
#         indices_row = '   ' + ' '.join(map(lambda x: str(x).rjust(2), indices))
#         string_rep += indices_row + '\n'
#         for i, row in enumerate(visible_board):
#             string_rep += f'{i}'.rjust(2) + ' '
#             string_rep += ' | '.join(map(lambda x: x.rjust(widths[i]), row))
#             string_rep += ' |\n'

#         string_rep += '   ' + ' '.join(['-'*(width + 2) for width in widths]) + '\n'

#         return string_rep

# def play(dimsize=10, mines=10):
#     board = Board(dimsize, mines)
    
#     while len(board.dug) < board.dimsize ** 2 - mines:
#         # board.dig(*get_next_move(board))

#         print(board)
#         user_input = re.split(',(\\s)*', input("Enter a location to dig (row,col): "))
#         row , col = int(user_input[0]), int(user_input[-1])
#         if row < 0 or row >= board.dimsize or col < 0 or col >= board.dimsize:
#             print("Invalid location. Try again.")
#             continue

#         if board.board[row][col] == '*':
#             print("Game Over!")
            
#         safe = board.dig(row, col)
#         if not safe:
#             break
#     if safe:
#         print("You win!")
#     else:
#         print("Game Over!")
        
#         board.dug = [(r,c) for r in range(board.dimsize) for c in range(board.dimsize)]
#         print(board)
    
    
# if __name__ == '__main__':
#     play()

import random
import re

class Board():
    def __init__(self, dimsize, num_mines):
        self.dimsize = dimsize
        self.num_mines = num_mines
        self.board = self.make_new_board()
        self.assign_values()  # Fix: Assign values after creating the board
        self.dug = set()
    
    def make_new_board(self):
        board = [[None for _ in range(self.dimsize)] for _ in range(self.dimsize)]
        bombs_planted = 0
        while bombs_planted < self.num_mines:
            loc = random.randint(0, self.dimsize**2 - 1)
            row = loc // self.dimsize
            col = loc % self.dimsize
            
            if board[row][col] == '*':
                continue
            
            board[row][col] = '*'
            bombs_planted += 1
        
        return board

    def assign_values(self):
        for r in range(self.dimsize):
            for c in range(self.dimsize):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_mines(r, c)

    def get_num_neighboring_mines(self, row, col):
        num_neighboring_mines = 0
        for r in range(max(0, row - 1), min(self.dimsize, row + 2)):  # Fix range
            for c in range(max(0, col - 1), min(self.dimsize, col + 2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_mines += 1
        return num_neighboring_mines

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dimsize, row + 2)):
            for c in range(max(0, col - 1), min(self.dimsize, col + 2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.dimsize)] for _ in range(self.dimsize)]
        for row in range(self.dimsize):
            for col in range(self.dimsize):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        string_rep = ''
        widths = []
        for idx in range(self.dimsize):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key=len)))

        indices = [i for i in range(self.dimsize)]
        indices_row = '   ' + ' '.join(map(lambda x: str(x).rjust(2), indices))
        string_rep += indices_row + '\n'
        for i, row in enumerate(visible_board):
            string_rep += f'{i}'.rjust(2) + ' '
            string_rep += ' | '.join(map(lambda x: x.rjust(widths[i]), row))
            string_rep += ' |\n'

        string_rep += '   ' + ' '.join(['-' * (width + 2) for width in widths]) + '\n'

        return string_rep


def play(dimsize=10, mines=10):
    board = Board(dimsize, mines)
    
    while len(board.dug) < board.dimsize ** 2 - mines:
        print(board)
        user_input = input("Enter a location to dig (row,col): ").strip().split(',')
        
        if len(user_input) != 2 or not user_input[0].isdigit() or not user_input[1].isdigit():
            print("Invalid input. Please enter in format: row,col")
            continue
        
        row, col = int(user_input[0]), int(user_input[1])
        
        if row < 0 or row >= board.dimsize or col < 0 or col >= board.dimsize:
            print("Invalid location. Try again.")
            continue

        if board.board[row][col] == '*':
            print("Game Over!")
            board.dug = {(r, c) for r in range(board.dimsize) for c in range(board.dimsize)}  # Reveal board
            print(board)
            return
        
        safe = board.dig(row, col)
        if not safe:
            break
    
    print("You win!")
    board.dug = {(r, c) for r in range(board.dimsize) for c in range(board.dimsize)}
    print(board)


if __name__ == '__main__':
    play()
