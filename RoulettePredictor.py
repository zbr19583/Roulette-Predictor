#American roulette predictor
#Brian Mar
#1/21/14

import random


startingBet = raw_input("How much money for starting bet?")

amountDesired = raw_input("How much money do you want to win?")

startingBet = float(startingBet)
amountDesired = float(amountDesired)

amountEarned = 0
nextBet = float(startingBet)
gamesPlayed = 0
n = 1
maximumBet = 0

while (amountEarned <= amountDesired):
    x = random.randrange(0, 38)	#add an extra number to account for "00"
    if (x >= 1 and x <= 18):
        amountEarned += nextBet
        n = 1
        gamesPlayed += 1
    else:
        amountEarned -= nextBet
        nextBet = startingBet * 2 ** n
        if (nextBet + amountEarned) >= maximumBet:
            maximumBet = nextBet + amountEarned
        n += 1
        gamesPlayed += 1
    
print "Amount Desired: $" + str(amountDesired)
print "Starting Bet: $" + str(startingBet)
print ""
print "You will need to play " + str(gamesPlayed) + " times" 
print "You will need to use $" + str(maximumBet) + " dollars"

