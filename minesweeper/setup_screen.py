import subprocess
import sys
import time
import csv

f = open('minefield_settings.txt', 'w')

WIDTH  = 600
HEIGHT = 500

#################
# Graphic Setup #
#################

#imports the title screen images
right1 = Actor('right-raised')
left1  = Actor('left-raised')
right2 = Actor('right-raised')
left2  = Actor('left-raised')
right3 = Actor('right-raised')
left3  = Actor('left-raised')
mines  = Actor('mines')
w      = Actor('width')
h      = Actor('height')
next   = Actor('next-raised')

images = [right3, right2, right1, left3, left2, left1, next, mines, w, h]
arrows = images[:-4]

mine = 10
wide = 10
tall = 10

def arrow_raise(arrow):
    arrow.image = arrow.image[:-7] + 'raised'

def arrow_press(arrow):
    arrow.image = arrow.image[:-6] + 'pressed'

def on_mouse_down(pos):
    global mine, wide, tall
    if right1.collidepoint(pos):
        arrow_press(right1)
        wide += 1
    elif right2.collidepoint(pos):
        arrow_press(right2)
        tall += 1
    elif right3.collidepoint(pos):
        arrow_press(right3)
        mine += 1
    elif left1.collidepoint(pos):
        arrow_press(left1)
        wide -= 1
    elif left2.collidepoint(pos):
        arrow_press(left2)
        tall -= 1
    elif left3.collidepoint(pos):
        arrow_press(left3)
        mine -= 1
    elif next.collidepoint(pos):
        arrow_press(next)
    if wide <= 1:
        wide = 1
    if tall <= 1:
        tall = 1
    if mine <= 1:
        mine = 1
    if mine >= tall * wide:
        mine = tall * wide

def on_mouse_up(pos):
    for arrow in arrows:
        if arrow.collidepoint(pos):
            arrow_raise(arrow)
    if next.collidepoint(pos):
        arrow_raise(next)
        row = str((wide, tall, mine))
        f.write(row)
        f.close()
        subprocess.Popen("pgzrun main.py", shell=True)
        time.sleep(1)
        sys.exit()

def draw():
    right1.pos = 525.017, 158.627
    left1.pos  = 313.600, 158.627
    right2.pos = 525.017, 235.333
    left2.pos  = 313.600, 235.333
    right3.pos = 525.017, 312.039
    left3.pos  = 313.600, 312.039
    mines.pos  = 138.168, 312.038
    w.pos      = 133.168, 158.627
    h.pos      = 138.168, 235.333
    next.pos   = 295.605, 424.313
    screen.fill((180, 180, 180))
    for image in images:
        image.draw()
    screen.draw.text('Minesweeper', center=[300.000,  64.938], fontname="lcd_solid", fontsize=60, color='orange', gcolor='red', owidth=0.5, ocolor="black")
    screen.draw.text(str(wide)    , center=[415.703, 163.627], fontname="lcd_solid", fontsize=70)
    screen.draw.text(str(tall)    , center=[415.703, 240.333], fontname="lcd_solid", fontsize=70)
    screen.draw.text(str(mine)    , center=[415.703, 317.039], fontname="lcd_solid", fontsize=70)



