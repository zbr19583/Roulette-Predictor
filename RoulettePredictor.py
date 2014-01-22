#American roulette predictor
#Brian Mar
#1/21/14

import random
import math


startingBet = raw_input("How much money for bet increment?")
amountToSpend = raw_input("How much money do you want to begin with?")
amountDesired = raw_input("How much money do you want to end up with?")


startingBet = float(startingBet)
amountDesired = float(amountDesired)
amountToSpend = float(amountToSpend)

amountBalance = amountToSpend
nextBet = float(startingBet)
gamesPlayed = 0
n = 1

winCount = 0
loseCount = 0

i = 0
while (winCount + loseCount) < 1000: #1000 represents the number of casino sessions where you either go home a winner or lose all your money
    if (amountBalance <= amountDesired) and (amountBalance > 0):
        x = random.randrange(0, 38)	#add an extra number to account for "00"
        if (x >= 1 and x <= 18):
            amountBalance += nextBet
            nextBet = startingBet
            n = 1
            gamesPlayed += 1
        else:
            amountBalance -= nextBet
            nextBet = startingBet * 2 ** n
            n += 1
            gamesPlayed += 1
    elif (amountBalance <= 0):
        loseCount += 1
        amountBalance = amountToSpend
        nextBet = float(startingBet)
        n = 1
    else:
        winCount += 1
        amountBalance = amountToSpend
        nextBet = float(startingBet)
        n = 1

loseCount = float(loseCount)
winCount = float(winCount)
percDenominator = loseCount + winCount
print "Goal Amount: $" + str(amountDesired)
print "Bet Increment: $" + str(startingBet)
print "Amount willing to spend: $" + str(amountToSpend)
print ""
print "Chance of losing all your money is " + str((loseCount/percDenominator)*100) + "%"
print "Chance of going home a winner is " + str((winCount/percDenominator)*100) + "%"

#print "You will need to play " + str(gamesPlayed) + " times"
#print "You will need to use $" + str(abs(amountSpent)) + " dollars"
