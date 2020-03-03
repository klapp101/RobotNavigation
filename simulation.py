import gameboard
from euclidean import Euclidean
from manhattan import Manhattan
from aEuclidean import aStarEuclidean
from aManhattan import aStarManhattan
class Barriers:
    def __init__(self):
        self.coordinates = []

    def addBarrier(self, row, col):
        self.coordinates.append((row,col))

class Simulation:
    def __init__(self):
        self.gameBoard = gameboard.GameBoard()

    def create_simulation(self):

        board = self.gameBoard.board
        board_size = self.gameBoard.board_size

        euclidean_board = [[]]
        manhattan_board = [[]]
        aStar_euclidean_board = [[]]
        aStar_manhattan_board = [[]]

        i_row = 0
        i_col = 0
        goal_row = 0
        goal_col = 0
        # cost = self.aStarEuclidean_path_cost
        barrier = Barriers()

        # Searching for initial and goal state
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'i':
                    i_row = row
                    i_col = col
                if board[row][col] == 'g':
                    goal_row = row
                    goal_col = col
                if board[row][col] == '+':
                    barrier.addBarrier(row, col)

        euclidean_board = board
        manhattan_board = board
        aStar_euclidean_board = board
        aStar_manhattan_board = board

        """for row in board:
            for col in row:
                euclidean_board[row[col] = board[row][col]
                manhattan_board[row][col] = board[row][col]
                aStar_euclidean_board[row][col] = board[row][col]
                aStar_manhattan_board[row][col] = board[row][col]"""
        search = Euclidean(euclidean_board, board_size, barrier.coordinates)
        search.search_euclidean(i_row, i_col, goal_row, goal_col)
        search = Manhattan(manhattan_board, board_size, barrier.coordinates)
        search.search_manhattan(i_row,i_col,goal_row,goal_col)
        search = aStarEuclidean(aStar_euclidean_board, board_size, barrier.coordinates)
        search.search_aStarEuclidean(i_row,i_col,goal_row,goal_col)
        search = aStarManhattan(aStar_manhattan_board, board_size, barrier.coordinates)
        search.search_aStarManhattan(i_row,i_col,goal_row,goal_col)


sim = Simulation()
sim.create_simulation()
