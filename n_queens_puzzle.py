from db_config import db, engine, connection, solutions_table
import time

class NQueensPuzzle:
        def __init__(self, board_size = 8, print_board = False, store_board = False):
                self.board_size = board_size
                self.print_board = print_board
                self.store_board = store_board
                self.solutions = list()
                self.time_elapsed = int(round(time.time() * 1000))

                print ("{} Queen Puzzle, Print: {} and Store: {}".format(self.board_size, self.print_board, self.store_board))
                self.solve_puzzle()

        def solve_puzzle(self):
                # Find the Solution in the Database
                ResultProxy = connection.execute(db.select([solutions_table]).where(solutions_table.columns.board_size == self.board_size))
                ResultSet = ResultProxy.fetchall()
                if ResultSet:
                        for _id, _bs, _sol in ResultSet:
                                self.solutions.append(_sol)
                else:
                        # Initialize the board
                        board = [-1] * self.board_size
                        self.find_queen(board, 0)

                        if self.store_board:
                                for board in self.solutions:
                                        self.store_board_in_db(board)

                self.time_elapsed = int(round(time.time() * 1000)) - self.time_elapsed

                if self.print_board:
                        self.print_total_solutions()

        def print_total_solutions(self):
                print('For a board of {}x{}, found {} solutions in {} milliseconds'.format(self.board_size, self.board_size, len(self.solutions), self.time_elapsed))

        def find_queen(self, board, row):
                # Scape Secuency
                if row == self.board_size:
                        if self.print_board:
                                self.print_solution(board)

                        self.solutions.append(board)
                else:
                        # Test the position
                        for column in range(self.board_size):
                                if self.test_position(board, row, column):
                                        board[row] = column
                                        # Next search
                                        self.find_queen(board, row + 1)

        def test_position(self, board, ocuppied_rows, column):
                # Check column, left diagonal and rigth diagonal
                for row in range(ocuppied_rows):
                        if (
                                board[row] == column
                                or board[row] - row == column - ocuppied_rows
                                or board[row] + row == column + ocuppied_rows
                                ):
                                return False
                return True

        def print_solution(self, board):
                # print(board)
                for row in range(len(board)):
                        _row = ""
                        for column in range(len(board)):
                                if column == board[row]:
                                        _row += 'Q'
                                else:
                                        _row += '-'
                        print(_row)
                print('\n')

        def store_board_in_db(self, board):
                ResultProxy = connection.execute(db.insert(solutions_table).values(board_size=self.board_size, solution=board))
