import sys, getopt
from n_queens_puzzle import NQueensPuzzle

def main(argv):
        try:
                myopts, args = getopt.getopt(argv,"b:p:s:")

                # print(myopts, args)
                if (len(myopts) == 0):
                        print("Usage: %s -b board_size -p bolean_print -s boolean_store" % sys.argv[0])
                        sys.exit(2)
 
                for o, a in myopts:
                        # print(o, a)
                        if o == '-p':
                                print_board = True if a == 'True' else False
                        elif o == '-s':
                                store_board = True if a == 'True' else False
                        elif o == '-b':
                                board_size = int(a)

        except getopt.GetoptError as e:
                print(str(e))
                print("Usage: %s -p bolean_print -s boolean_store" % sys.argv[0])
                sys.exit(2)
 
        NQueensPuzzle(board_size, print_board, store_board)
	
if __name__ == "__main__":
	main(sys.argv[1:])
