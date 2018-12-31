#Thesis
#Turtle 
#The turtle walks the TMS, walk converges to Koch Snowflake

from graphics import *
from TMcalculator import *

def make_turtle(s):
    #this makes a turtle
    return {"name":s, "x":540, "y":300, "facing":'R'}
def clockwise(t): 
    #turtle turns clockwise 60 degrees
    #t is the input dictionary
    #make make spinny as is - check in testing
    if t['facing'] == 'R':
        t['facing'] = 'L'
    elif t['facing'] == 'L':
        t['facing'] = 'U'
    elif t['facing'] == 'U': 
        t['facing'] = 'R'
def forward(t): 
    #turtle heads forward
    if t['facing'] == 'R':
        t['x'] = t['x'] + 1
        t['y'] = t['y'] - 1
    if t['facing'] == 'L':
        t['x'] = t['x'] - 1
        t['y'] = t['y'] - 1
    if t['facing'] == 'U':
        t['y'] = t['y'] + 1
def counterclockwise(t): 
    #turtle turns counterclockwise 60 degrees
    if t['facing'] == 'R': 
        t['facing'] = 'U'
    elif t['facing'] == 'U':
        t['facing'] = 'L'
    elif t['facing'] == 'L':
        t['facing'] = 'R'

def as_string(t): 
    return "< turtle "+ "\'" + t['name'] + "\'" + " at " + "(" + str(t['x']) + ","+ str(t['y']) + ")" + " heading " + t['facing'] + " >"
    #for testing the turning function


def intake_TM(t,n):
    #this lets the turtle walk the Thue Morse Sequence (for testing)
    #note that we can just make it walk any sequence, same with below function
    if n == 0:
        clockwise(t)
    elif n == 1: 
        forward(t)
    elif n > 1: 
        print("no")


def intake_antiTM(t,n):
    #Turtle walks the Anti Sequence (for testing)
    if n == 0:
        forward(t)
    elif n == 1:
        clockwise(t)
    elif n > 1: 
        print("no")

def parser(t,l): #this parses the string given to the turtle from TM calculator, specifically to walk the TM sequence
    k = len(l)
    i = 0
    while i <= (k-1):
        if l[i] == '0':
           clockwise(t)
           i = i+1
        else:
            forward(t)
            i = i + 1


def test():
    t = make_turtle('p')
    parser(t, TM(2)) 
    print(as_string(t)) #should print "< turtle 'p' at (-3,-2) heading L >"
    print("done!")

test()

#notes: 

#do induction of sigma function

#why does M do what it does? Why does multiplying the initial vector by M guarantee where the turtle will end?
#esp since group H = M x R is not abelian. 

#very lightly overview whole paper from beginning to end, why is it so long? what is happening where? 

#multigrades - after first other things





