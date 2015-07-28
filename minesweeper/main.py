#to run this game type the command pgzrun main.py into the terminal whilst in this directory

###########
# Imports #
###########
from random import randint
from math import floor

#################
# Graphic Setup #
#################

#imports the top tile
cover = Actor('cover')

#creates a dictionary that stores all the possible bottom tile types
tiles = {1: Actor('one'),
         2: Actor('two'),
         3: Actor('three'),
         4: Actor('four'),
         5: Actor('five'),
         6: Actor('six'),
         7: Actor('seven'),
         8: Actor('eight'),
         'flag': Actor('flag'),
         'M': Actor('mine'),
         0: Actor('blank'),
         'question': Actor('question')}

##############
# Game Setup #
##############

#adapt these settings to suit you

#defines the number of mines that will be placed in the grid
mines = 10

#defines how many tiles tall the minefield is
tall = 9

#defines how many tiles wide the minefield is
wide = 9

##################
# Function Setup #
##################

def setup_empty_grid(wide, tall, filler):
    grid = []
    for y in range(tall):
        row = []
        for x in range(wide):
            row.append(filler)
        grid.append(row)
    return grid

def populate_grid(grid, mines, wide, tall):
    for mine in range(mines):
        x, y = randint(0, wide - 1), randint(0,tall - 1)
        while grid[y][x] == 'M':
            x, y = randint(0, wide - 1), randint(0,tall - 1)
        grid[y][x] = 'M'
    return grid

def count_mines(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != 'M':
                neighbors = [(x - 1, y - 1), (x    , y - 1), (x + 1, y - 1),
                             (x - 1, y    ),                 (x + 1, y    ),
                             (x - 1, y + 1), (x    , y + 1), (x + 1, y + 1)]
                for nx, ny in neighbors:
                    try:
                        if ny >= 0 and nx >= 0 and grid[ny][nx] == 'M':
                            grid[y][x] += 1
                    except:
                        pass
    return grid


base_grid = setup_empty_grid(wide, tall, 0)
top_grid  = setup_empty_grid(wide, tall, 1)

base_grid = populate_grid(base_grid, mines, wide, tall)

base_grid = count_mines(base_grid)

def draw():
    screen.fill((128, 0, 0))
    global base_grid, tiles
    xpos, ypos = -15, -15
    for row in range(len(base_grid)):
        ypos += 30
        xpos = -15
        for col in range(len(base_grid[0])):
            xpos += 30
            gridpos = base_grid[row][col]
            tiles[gridpos].pos = xpos, ypos
            tiles[gridpos].draw()
    xpos, ypos = -15, -15
    for row in range(len(top_grid)):
        ypos += 30
        xpos = -15
        for col in range(len(top_grid[0])):
            xpos += 30
            if top_grid[row][col] == 1:
                cover.pos = xpos, ypos
                cover.draw()

def on_mouse_down(pos):
    top_grid[floor(pos[1]/30)][floor(pos[0]/30)] = 0


################
# Screen Setup #
################

#creates two variables that define the width and height of the screen
WIDTH = ((wide * 30) + 1) #adapts the screen size to fit the number of tiles chosen
HEIGHT = ((tall * 30) + 1) #adapts the screen size to fit the number of tiles chosen

