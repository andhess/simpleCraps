import sys
import random

numWins = 0
numLoss = 0
iterations = 1000000

def playCraps():

    winning = [ 7 , 11 ]
    losing  = [ 2, 3, 12 ]
    stage2  = [ 4, 5, 6, 8, 9, 10 ]

    firstToss = rollDice()

    if winning.count( firstToss ) > 0:
        return win()
    elif losing.count( firstToss ) > 0:
        return lose()
    else:
        return crapsPartTwo( firstToss )

def crapsPartTwo( firstToss ):
    winning = firstToss
    count = 1

    while True:
        toss = rollDice()
        count += 1
        if toss == winning:
            return win()
        if toss == 7:
            return lose()

def rollDice():
    d1 = random.randint( 1 , 6 )
    d2 = random.randint( 1 , 6 )
    return d1 + d2

def win():
    global numWins
    numWins += 1
    return

def lose():
    global numLoss
    numLoss += 1
    return

print "iterations: " + str( iterations )

for i in range ( 0 , iterations ):
    playCraps()

print numWins
print numLoss
print "winning percentage: " + str( 1.0 * numWins / ( numWins + numLoss ) )


