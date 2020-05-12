# game-of-life

A simulator for Conway's game of life, to be used from the terminal.
This implementation uses a wrap-around array instead of an infinite grid.

To run with a random setup, you can just run `python main.py`. Or alternatively,
you can run it with a preset pattern with `python main.py [filepath]`. For example,
you can run `python main.py patterns/spaceships/glider.txt` and the program will load
up with a glider.

Once it's running, you can press `r` to randomize the grid, and `q` to quit.
