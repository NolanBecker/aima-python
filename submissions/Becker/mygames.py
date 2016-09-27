from collections import namedtuple
from games import (Game)

class GameState:
    def __init__(self, to_move, board, label=None):
        self.to_move = to_move
        self.board = board
        self.label = label

    def __str__(self):
        if self.label == None:
            return super(GameState, self).__str__()
        return self.label

class Hex(Game):
    """ """

    def __init__(self, h=3, v=3):
        self.h = h
        self.v = v
        self.blueWin = ((1,3), (2,3), (3,3))
        self.redWin = ((1,1), (1,2), (1,3))
        self.initial = GameState(to_move='B', board={})

    def actions(self, state):
        try:
            return state.moves
        except:
            pass
        "Legal moves are any square not yet taken."
        moves = []
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                if (x, y) not in state.board.keys():
                    moves.append((x, y))
        state.moves = moves
        return moves

    # defines the order of play
    def opponent(self, player):
        if player == 'B':
            return 'R'
        if player == 'R':
            return 'B'
        return None

    def result(self, state, move):
        if move not in self.actions(state):
            return state  # Illegal move has no effect
        board = state.board.copy()
        player = state.to_move
        board[move] = player
        next_mover = self.opponent(player)
        return GameState(to_move=next_mover, board=board)

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        try:
            return state.utility if player == 'B' else -state.utility
        except:
            pass
        board = state.board
        util = self.check_win(board, 'B')
        if util == 0:
            util = -self.check_win(board, 'R')
        state.utility = util
        return util if player == 'B' else -util

    # Did I win?
    def check_win(self, board, player):
        for (x, y) in self.blueWin:
            if board.get((x, y)) == player:
                return self.is_connected(board, x, y-1, player)
        for (x, y) in self.redWin:
            if board.get((x, y)) == player:
                # return self.is_connected(board, x+1, y, player)
                return 0
        return 0

    # does player have K in a row? return 1 if so, 0 if not
    def is_connected(self, board, x, y, player):
        if x > self.v or x < 1:
            return 0
        if y > self.h or y < 1:
            return 0
        if self.check_next(board, x, y, player) == 1:
            if player == "B":
                if y == 1:
                    return 1
                else:
                    return self.is_connected(board, x, y-1, player)
            else:
                if x == 3:
                    return 1
                else:
                    return self.is_connected(board, x+1, y, player)
        elif player == "B":
            if self.check_next(board, x-1, y, player) == 1:
                # x -= 1
                if y == 1:
                    return 1
                else:
                    return self.is_connected(board, x-1, y-1, player)
            elif self.check_next(board, x+1, y, player) == 1:
                # x += 1
                if y == 1:
                    return 1
                else:
                    return self.is_connected(board, x+1, y-1, player)
            else:
                return 0
        elif player == "R":
            if self.check_next(board, x, y-1, player) == 1:
                # y -= 1
                if x == 3:
                    return 1
                else:
                    return self.is_connected(board, x+1, y-1, player)
            elif self.check_next(board, x, y+1, player) == 1:
                if x == 3:
                    return 1
                else:
                    return self.is_connected(board, x+1, y+1, player)
            else:
                return 0
        return 0

    def check_next(self, board, x, y, player):
        if board.get((x, y)) == player:
            return 1
        else:
            return 0

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        return self.utility(state, 'B') != 0 or len(self.actions(state)) == 0

    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()


myGame = Hex()



myGames = {
    myGame: [

    ]
}