import sys
import time
import curses as crs
from life import Life

def main(stdscr, argv):

    # initialize custom window settings 
    stdscr.clear()
    crs.curs_set(False)
    stdscr.scrollok(0)
    stdscr.nodelay(True)

    # initialize game grid
    if len(argv) > 1:
        life = Life(stdscr.getmaxyx(), read_pattern(argv[1]))
    else:
        life = Life(stdscr.getmaxyx())

    # draw game grid to screen
    draw(stdscr, life)

    running = True
    while running:
        # time.sleep(.25)

        # calc next generation
        life.next_gen()
        # update screen
        draw(stdscr, life)

        
        # get input from user
        ch = stdscr.getch()
        if ch >= 0:
            # TODO: implement options once i implement infinite grid
            """
            if ch == ord('h'):
                # move left
            elif ch == ord('j'):
                # move down
            elif ch == ord('k'):
                # move up
            elif ch == ord('l'):
                # move right
            elif ch == ord('-'):
                # zoom out
            elif ch == ord('+'):
                # zoom in
            """

            if ch == ord('r'):
                life = Life(stdscr.getmaxyx())
            elif ch == ord('q'): # end game
                running = False
                


def draw(stdscr, life):
    """draws life game board to the terminal"""

    stdscr.clear()
    
    dim = stdscr.getmaxyx()

    for i in range(min(life.rows, dim[0])):
        for j in range(min(life.cols, dim[1])):
            if life.grid[i][j]:
                stdscr.insch(i, j, 'O')

    stdscr.refresh()



def read_pattern(file_name):
    """takes a file as input, returns a bool array"""
    lines = []
    with open(file_name) as f:
        lines = f.read().split('\n')

    pattern = [[i == 'O' for i in line] for line in lines]
    pattern.pop()

    return pattern



if __name__ == '__main__':
    crs.wrapper(main, sys.argv)

