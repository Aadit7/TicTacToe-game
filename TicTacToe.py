# Tic Tac Toe
import random


class TicTacToe:

    def __init__(self, board):
        self.board = board

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    def inputPlayer1Letter(self):
        # Lets the player1 type which letter they want to be.
        # Returns a list with the player1's letter as the first item, and the player2's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Player1, do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player1's letter, the second is the  player2's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the players who goes first.
        if random.randint(0, 1) == 0:
            return 'player1'
        else:
            return 'player2'

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Players, do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self, letter, move):
        self.board[move] = letter

    def isWinner(self, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or # across the top
        (self.board[4] == le and self.board[5] == le and self.board[6] == le) or # across the middle
        (self.board[1] == le and self.board[2] == le and self.board[3] == le) or # across the bottom
        (self.board[7] == le and self.board[4] == le and self.board[1] == le) or # down the left side
        (self.board[8] == le and self.board[5] == le and self.board[2] == le) or # down the middle
        (self.board[9] == le and self.board[6] == le and self.board[3] == le) or # down the right side
        (self.board[7] == le and self.board[5] == le and self.board[3] == le) or # diagonal
        (self.board[9] == le and self.board[5] == le and self.board[1] == le)) # diagonal

    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in self.board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def getPlayerMove(self, turn):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print(turn + ': What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(self, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True


print('Welcome to Tic Tac Toe!')


while True:
    # Reset the board
    theBoard = [' '] * 10
    tictactoe = TicTacToe(theBoard)
    player1Letter, player2Letter = tictactoe.inputPlayer1Letter()
    turn = tictactoe.whoGoesFirst()
    print(turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player1':
            # Player1's turn.
            move = tictactoe.getPlayerMove(turn)
            tictactoe.makeMove(player1Letter, move)
            tictactoe.drawBoard()

            if tictactoe.isWinner(player1Letter):
                print('Hooray! Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if tictactoe.isBoardFull():
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player2'

        else:
            # player2's turn.
            move = tictactoe.getPlayerMove(turn)
            tictactoe.makeMove(player2Letter, move)
            tictactoe.drawBoard()

            if tictactoe.isWinner(player2Letter):
                print('Hooray! Player 2 has won the game!')
                gameIsPlaying = False
            else:
                if tictactoe.isBoardFull():
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player1'

    if not tictactoe.playAgain():
        break