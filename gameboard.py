
class GameBoard:
    def __init__(self):
        self.board = None
        self.board_size = 0
        # self.goal_state = None
        # self.initial_state = None
        self.readFile()

    def readFile(self):
        question = input('Please enter the name of the file you would like to use as the board' + '\n')
        try:
            with open(question,'r') as f:
                #board = [[]]
                file_text = f.readlines()
                board_size = file_text[0].strip()
                print('The size of the board: ' + board_size + 'x' + board_size)
                self.board_size = board_size
                file_board = [x.strip() for x in file_text[1:]]
                #print(file_board)
                # 2D List
                self.board = [[(y) for y in list(x)] for x in file_board]
        except:
            print('Please enter a valid file name')
            self.readFile()
