
import math
import pdb
import sys

# Creating a class to be able to keep track of points alot easier
class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class PPoint:
    def __init__(self, row, col, f):
        self.row = row
        self.col = col
        self.f = f

class PosDetails:
    def __init__(self, origRow, origCol, row, col):
        self.original = Point(origRow, origCol)
        self.current = Point(row, col)
        self.f = 0.0
        self.g = 0.0
        self.h = 0.0

class aStarManhattan:
    def __init__(self, board, boardSize, barrierCoords):
        self.board_size = boardSize
        #A 2D array containing  the location of the coordinates
        self.barriersCoords = barrierCoords
        self.board = board
        self.aStarManhattan_path_cost = 0
        """for i in range(len(self.barriersCoords)):
            print(self.barriersCoords[i][0])
            print(self.barriersCoords[i][1])
            print("\n")"""

    def isGoal(self, row, col, goal):
        if row == goal.row and col == goal.col:
            return True
        else:
            return False

    def trace(self, pos_list, destination):
        print("Result")
        row = destination.row
        col = destination.col

        path = []
        while(not (pos_list[row][col].original.row == row and pos_list[row][col].original.col == col)):
            path.append(Point(row,col))
            temp_row = pos_list[row][col].original.row
            temp_col = pos_list[row][col].original.col
            row = temp_row
            col = temp_col

        path.append(Point(row, col))
        #for index in range(len(path)):
            #self.replace_euclidean(path[index].row, path[index].col)
            #print("{},{}".format(path[index].row, path[index].col))
        path.pop(0)
        path.pop(len(path)-1)
        for i in reversed(path):
            self.aStarManhattan_path_cost += 1
            self.replace_aStarManhattan(i.row, i.col)
        print("Total aStarManhattan Path Cost: {}".format(self.aStarManhattan_path_cost))

    def replace_aStarManhattan(self, i_row, i_col):
        self.board[i_row][i_col] = 'o'
        self.prettyPrint(self.board)

    # Check if our point is not blocked
    def isAvailable(self, row, col):
        for index in range(len(self.barriersCoords)):
            if row == self.barriersCoords[index][0] and col == self.barriersCoords[index][1]:
                return False
        return True

    def printPotentialList(self):
        for index in range(len(self.potential_list)):
            print("Row: {} Col: {}".format(self.potential_list[index].current.row, self.potential_list[index].current.col))

        print("#"*20)

    def grabPotentialCells(self, list, i_row, i_col):
        west_col = i_col - 1
        # Right cell
        east_col = i_col + 1
        # Top cell
        north_row = i_row - 1
        # Bottom cell
        south_row = i_row + 1
        self.list.append(PosDetails(i_row, i_col, i_row, west_col))
        self.list.append(PosDetails(i_row, i_col, i_row, east_col))
        self.list.append(PosDetails(i_row, i_col, north_row, i_col))
        self.list.append(PosDetails(i_row, i_col, south_row, i_col))

        tempList = []

        #print(len(list))
        for index in range(len(self.list)):
            #print(index)
            if self.isAvailable(self.list[index].current.row,self.list[index].current.col):
                tempList.append(self.list[index])
        self.list.clear()
        self.list = tempList.copy()
        print("Avaiable Cells..")
        self.printPotentialList()
        return list

    def calculateDistance(self, list, i_row, i_col, goal : Point):
        # Make sure we have the latest potential List
        # Updating Potential List
        list.clear()
        list = self.grabPotentialCells(list, i_row, i_col).copy()

        for index in range(len(self.list)):
            print("Original: {},{}".format(self.list[index].original.row, self.list[index].original.col))
            print("Original: {},{}".format(self.list[index].current.row, self.list[index].current.col))
            self.list[index].g = self.calculate_aStarManhattan(self.list[index].original.row, self.list[index].original.col, self.list[index].current.row, self.list[index].current.col)
            print(self.list[index].g)
            self.list[index].h = self.calculate_aStarManhattan(self.list[index].current.row, self.list[index].current.col, goal.row, goal.col)
            print(self.list[index].h)
            self.list[index].f = self.list[index].g + self.list[index].h
            print(self.list[index].f)
        return list
    # Function checking the range for row and col
    def isValid(self, row, col):
        if (row >= 0) and (row < int(self.board_size)) and (col >= 0) and (col < int(self.board_size)):
            return True


    def prettyPrint(self, board):
        for row in range(len(board)):
            currentRow = ""
            for col in range(len(board[row])):
                currentRow += board[row][col]
            print(currentRow)
        print("\n")

    def calculate_aStarManhattan(self, i_row, i_col, goal_row, goal_col):
        aStarManhattan_distance = abs(i_row-goal_row) + abs(i_col-goal_col)
        return aStarManhattan_distance
        #print(euclidean_distance)

    def search_aStarManhattan(self, i_row, i_col, goal_row, goal_col):

        goal = Point(goal_row, goal_col)
        row = i_row
        col = i_col

        visited_list = []
        for i in range(int(self.board_size)):
            new = []
            for j in range(int(self.board_size)):
                new.append(False)
            visited_list.append(new)

        ##################################################
        pos_list = [[PosDetails(0,0,0,0) for i in range(int(self.board_size))] for j in range(int(self.board_size))]

        for i in range(int(self.board_size)):
            for j in range(int(self.board_size)):
                pos_list[i][j].f = sys.float_info.max
                pos_list[i][j].g = sys.float_info.max
                pos_list[i][j].h = sys.float_info.max
                pos_list[i][j].original.row = -1
                pos_list[i][j].original.col = -1
        ###################################################

        pos_list[row][col].original.row = row
        pos_list[row][col].original.col = col

        path_list = [] # PPoint object
        path_list.append(PPoint(row, col, 0.0))

        print(len(path_list))
        while(len(path_list) > 0):
            p = path_list[0] # grab the first PPoint
            path_list.pop(0) # remove it

            row = p.row
            col = p.col
            visited_list[row][col] = True
            # Left cell
            west_col = col - 1
            # Right cell
            east_col = col + 1
            # Top cell
            north_row = row - 1
            # Bottom cell
            south_row = row + 1

            newG = 0.0
            newH = 0.0
            newF = 0.0

            if not self.isValid(i_row, i_col):
                print("Initial Point is invalid!")
                return
            if self.isValid(goal.row, goal.col) == False:
                print("Destination Point is invalid!!")
                return
            if self.isGoal(i_row, i_col, goal):
                print("We already at the goal!")
                return
            ################################ NORTH ################################################
            if self.isValid(north_row, col):
                # Check if distination coordinates is the same as goal
                if self.isGoal(north_row, col, goal):
                    post_list[north_row][col].original.row = row
                    post_list[north_row][col].origina.col = col
                    self.trace(pos_list, goal)
                    return
                elif visited_list[north_row][col] == False and self.isAvailable(north_row, col) == True:
                    newG = pos_list[row][col].g + 1.0
                    newH = float(self.calculate_aStarManhattan(north_row, col, goal.row, goal.col))
                    newF = newG + newH

                    if pos_list[north_row][col].f == sys.float_info.max or pos_list[north_row][col].f > newF:
                        path_list.append(PPoint(north_row, col, newF))
                        pos_list[north_row][col].f = newF
                        pos_list[north_row][col].g = newG
                        pos_list[north_row][col].h = newH
                        pos_list[north_row][col].original.row = row
                        pos_list[north_row][col].original.col = col



            ############################# SOUTH ####################################################
            if self.isValid(south_row, col):
                if self.isGoal(south_row, col, goal):
                    pos_list[south_row][col].original.row = row
                    pos_list[south_row][col].original.col = col
                    self.trace(pos_list, goal)
                    return
                elif visited_list[south_row][col] == False and self.isAvailable(south_row, col) == True:
                    newG = pos_list[row][col].g + 1.0
                    newH = float(self.calculate_aStarManhattan(south_row, col, goal.row, goal.col))
                    newF = newG + newH

                    if pos_list[south_row][col].f == sys.float_info.max or pos_list[south_row][col].f > newF:
                        path_list.append(PPoint(south_row, col, newF))
                        pos_list[south_row][col].f = newF
                        pos_list[south_row][col].g = newG
                        pos_list[south_row][col].h = newH
                        pos_list[south_row][col].original.row = row
                        pos_list[south_row][col].original.col = col

            ############################# EAST ####################################################
            if self.isValid(row, east_col):
                if self.isGoal(row, east_col, goal):
                    pos_list[row][east_col].original.row = row
                    pos_list[row][east_col].original.col = col
                    self.trace(pos_list, goal)
                    return
                elif visited_list[row][east_col] == False and self.isAvailable(row, east_col) == True:
                    newG = pos_list[row][col].g + 1.0
                    newH = float(self.calculate_aStarManhattan(row, east_col, goal.row, goal.col))
                    newF = newG + newH

                    if pos_list[row][east_col].f == sys.float_info.max or pos_list[row][east_col].f > newF:
                        path_list.append(PPoint(row, east_col, newF))
                        pos_list[row][east_col].f = newF
                        pos_list[row][east_col].g = newG
                        pos_list[row][east_col].h = newH
                        pos_list[row][east_col].original.row = row
                        pos_list[row][east_col].original.col = col


            ################################# West ####################################################

            if self.isValid(row, west_col):
                if self.isGoal(row, west_col, goal):
                    pos_list[row][west_col].original.row = row
                    pos_list[row][west_col].original.col = col
                    self.trace(pos_list, goal)
                    return
                elif visited_list[row][west_col] == False and self.isAvailable(row, west_col) == True:
                    newG = pos_list[row][col].g + 1.0
                    newH = float(self.calculate_aStarManhattan(row, west_col, goal.row, goal.col))
                    newF = newG + newH

                    if pos_list[row][west_col].f == sys.float_info.max or pos_list[row][west_col].f > newF:
                        path_list.append(PPoint(row, west_col, newF))
                        pos_list[row][west_col].f = newF
                        pos_list[row][west_col].g = newG
                        pos_list[row][west_col].h = newH
                        pos_list[row][west_col].original.row = row
                        pos_list[row][west_col].original.col = col
