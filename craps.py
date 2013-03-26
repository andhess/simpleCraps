import sys
import random

def playCraps():

    winning = [ 7 , 11 ]
    losing  = [ 2, 3, 12 ]
    stage2  = [ 4, 5, 6, 8, 9, 10 ]

    firstToss = rollDice()

    print "---- 1st Toss ----"
    print "roll: " + str( firstToss )

    if winning.count( firstToss ) > 0:
        print win()
    elif losing.count( firstToss ) > 0:
        print lose() 
    else:
        print crapsPartTwo( firstToss )

def crapsPartTwo( firstToss ):
    winning = firstToss
    count = 1

    print "---- 2nd Stage ----"

    while True:
        toss = rollDice()
        count += 1
        if toss == winning:
            return "rolled initial dice value in 2nd stage: " + win() + \
                   " on roll " + str( count )
        if toss == 7:
            return "rolled a 7 in 2nd stage: " + lose() + \
                   " on roll " + str( count )

def rollDice():
    d1 = random.randint( 1 , 6 )
    d2 = random.randint( 1 , 6 )
    return d1 + d2

def win():
    return "congratulations you win"

def lose():
    return "you lose"

playCraps()