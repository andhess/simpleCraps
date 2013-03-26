import random

numWins = 0
numLoss = 0
iterations = 1000000

# simulates 1 game of craps
def playCraps():

    # define the sets of rules
    winning = [ 7 , 11 ]
    losing  = [ 2, 3, 12 ]
    stage2  = [ 4, 5, 6, 8, 9, 10 ]

    # initial dice toss
    firstToss = rollDice()

    # check if winning combination
    if winning.count( firstToss ) > 0:
        return win()

    # check if losing combination
    elif losing.count( firstToss ) > 0:
        return lose()

    # otherwise advance to second round
    else:
        return crapsPartTwo( firstToss )

# the 2nd part of a game of craps
def crapsPartTwo( firstToss ):
    winning = firstToss
    count = 1

    # toss until a decision is met
    while True:
        toss = rollDice()
        count += 1

        # 
        if toss == winning:
            return win()

        # lose if roll a 7
        if toss == 7:
            return lose()

# simulates rolling 2 die
def rollDice():
    d1 = random.randint( 1 , 6 )
    d2 = random.randint( 1 , 6 )
    return d1 + d2

# increments win count
def win():
    global numWins
    numWins += 1
    return

# increments loss count
def lose():
    global numLoss
    numLoss += 1
    return

print "iterations: " + str( iterations )

# run lots of simulations
for i in range ( 0 , iterations ):
    playCraps()

print "Wins: " + str( numWins )
print "Losses: " + str( numLoss )
print "winning percentage: " + str( 1.0 * numWins / ( numWins + numLoss ) )
