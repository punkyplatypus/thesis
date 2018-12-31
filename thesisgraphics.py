#Turtle graphics
#Thesis 
#Carrie Padula

from graphics import * 
from TMcalculator import *

def make_turtle(s):
    #this makes a turtle
    return {"name":s, "x":140, "y":450, "facing":'R'}

def clockwise(t): 
    #turtle turns clockwise 60 degrees
    #t is the input dictionary
    #make make spinny as is - check in testing
    if t['facing'] == 'R':
        t['facing'] = 'T'
    elif t['facing'] == 'T':
        t['facing'] = 'Q'
    elif t['facing'] == 'Q': 
        t['facing'] = 'P'
    elif t['facing'] == 'P': 
        t['facing'] = 'L'
    elif t['facing'] == 'L': 
        t['facing'] = 'U'
    elif t['facing'] == 'U': 
        t['facing'] = 'R'
def forward(t): 
    #turtle heads forward
    if t['facing'] == 'R':
        t['x'] = t['x'] + 10
        t['y'] = t['y'] + 10
    if t['facing'] == 'L':
        t['x'] = t['x'] - 10
        t['y'] = t['y'] + 10
    if t['facing'] == 'U':
        t['y'] = t['y'] + 10
    if t['facing'] == 'P':
        t['x'] = t['x'] - 10
        t['y'] = t['y'] - 10
    if t['facing'] == 'Q':
        t['y'] = t['y'] - 10
    if t['facing'] == 'T':
        t['x'] = t['x'] + 10
        t['y'] = t['y'] - 10
def counterclockwise(t): 
    #turtle turns counterclockwise 60 degrees
    if t['facing'] == 'R': 
        t['facing'] = 'U'
    elif t['facing'] == 'U':
        t['facing'] = 'L'
    elif t['facing'] == 'L':
        t['facing'] = 'P'
    elif t['facing'] == 'P':
        t['facing'] = 'Q'
    elif t['facing'] == 'Q':
        t['facing'] = 'T'
    elif t['facing'] == 'T':
        t['facing'] = 'R'



def parser(t,l): #this parses the string given to the turtle from TM calculator, specifically to walk the TM sequence
    k = len(l)
    win = GraphWin("Koch Thue Morse Turtle", 1080, 600)
    win.setBackground("pink")
    i = 0
    while i <= (k-1):
        if l[i] == '0':
            clockwise(t) #we don't need to draw the rotations.
            i = i+1
        else:
            z = t["x"] #takes the starting coords
            w = t["y"]
            forward(t) #move
            f = Line(Point(z, w), Point(t["x"],t["y"])) #line from starting to new coords
            f.setWidth(2)
            f.setFill("black")
            f.draw(win) #draw
            i = i + 1
    win.getMouse() # pause for click in window, lets us decide when to close
    win.close()
def main():
    t = make_turtle('p')
    parser(t, TM(10))



main()

#tester to see why things dont work