import random
import math

itmax = 250000
numRules=223
probOneRule = 1/numRules

#Create variables
rollArrRerollTop = []
rollArrRerollAll = []
rollArrTrueRand = []
rerollsTop = 0
rerollsAll = 0
for i in range (0, int(numRules/100)+1):
    rollArrRerollTop.append(0)
    rollArrRerollAll.append(0)
    rollArrTrueRand.append(0)

#Number of dicerolls
rulesLog = int(math.log10(numRules))
rollArr = []

#Create dice roll array
for i in range (0,rulesLog+1):
    rollArr.append(0)

#Print welcome message
print("This code will simulate rerolling for", itmax, "times for two dice algorithms.\n")
print("Current rule 223 algorithm:")
print("  Roll a d10 3 times. Each itteration is a digit. Reroll 100's digit if no such rule\n")
print("Suggested rule change")
print("  Roll a d10 3 times. Each itteration is a digit. Reroll ALL digits if no such rule\n")

#Print theoretical expected results
print("\nExpected results if true random:\n")
for i in range (0, len(rollArrRerollTop)):

    if i == 0:
        print("  Rolls in range 1 - 99    :", 99*probOneRule*100, "% (", itmax/numRules*99, ")")
    elif ((i*100+99) > numRules):
        print("  Rolls in range", i*100, "-", numRules, ":", (numRules-i*100+1)*probOneRule*100, "% (", itmax/numRules*(numRules-i*100+1), ")" )
    else:
        print("  Rolls in range", i*100, "-", i*100+99, ":", 100*probOneRule*100,"% (", itmax/numRules*100, ")")


print("\n\nPlease wait for roll simulation to finish...\n")


#Do rolls for reroll-top algorithm
for i in range (0, itmax):
    
    #Roll 3 die
    for j in range (0, rulesLog+1):
        rollArr[j] = random.randrange(0,10)
    
    #Calculate rolled value
    roll = 0
    for j in range (0, rulesLog+1):
        roll = roll + rollArr[j] * 10**j

    #If rule not in range, reroll top die again and recalculate
    while roll > numRules or roll == 0:
        rerollsTop = rerollsTop + 1
        rollArr[rulesLog] = random.randrange(0,10)
        roll = 0
        for j in range (0, rulesLog+1):
            roll = roll + rollArr[j] * 10**j

    #Count up range value corresponding to roll
    rollArrRerollTop[int((roll)/100)] = rollArrRerollTop[int((roll)/100)] + 1
    
#Do rolls for reroll-all algorithm
for i in range (0, itmax):

    roll = 0
    rerollsAll = rerollsAll - 1 #Compensate for inc in loop
    
    #reroll dice until rule that exist is found
    while roll > numRules or roll == 0:

        rerollsAll = rerollsAll + 1

        #Roll 3 die
        for j in range (0, rulesLog+1):
            rollArr[j] = random.randrange(0,10)
    
        #Calculate rolled value
        roll = 0
        for j in range (0, rulesLog+1):
            roll = roll + rollArr[j] * 10**j
        
    #Count up range value corresponding to roll
    rollArrRerollAll[int((roll)/100)] = rollArrRerollAll[int((roll)/100)] + 1


#Sanity check. Have computer generate random values within range
for i in range (0, itmax):
    roll = random.randrange(1, (numRules+1))
    rollArrTrueRand[int((roll)/100)] = rollArrTrueRand[int((roll)/100)] + 1



#print results
print("\nRoll results")
print("\nCurrent:\nReroll TOP digit if no existing rule\n")

for i in range (0, len(rollArrRerollTop)):

    if i == 0:
        print("  Rolls in range 1 - 99    : ", rollArrRerollTop[i]/itmax*100, "% (", rollArrRerollTop[i], ")")

    elif ((i*100+99) > numRules):
        print("  Rolls in range", i*100, "-", numRules, ": ", rollArrRerollTop[i]/itmax*100, "% (", rollArrRerollTop[i], ")")
    
    else:
        print("  Rolls in range", i*100, "-", i*100+99, ": ", rollArrRerollTop[i]/itmax*100, "% (", rollArrRerollTop[i], ")")

print("\n  Rerolls: ", rerollsTop, "( avg. ", rerollsTop/itmax, " rerolls per itteration)\n")

print("\nSuggested:\nReroll ALL if no existing rule\n")

for i in range (0, len(rollArrRerollAll)):

    if i == 0:
        print("  Rolls in range 1 - 99    : ", rollArrRerollAll[i]/itmax*100, "% (", rollArrRerollAll[i], ")")

    elif ((i*100+99) > numRules):
        print("  Rolls in range", i*100, "-", numRules, ": ", rollArrRerollAll[i]/itmax*100, "% (", rollArrRerollAll[i], ")")
    
    else:
        print("  Rolls in range", i*100, "-", i*100+99, ": ", rollArrRerollAll[i]/itmax*100, "% (", rollArrRerollAll[i], ")")

print("\n  Rerolls: ", rerollsAll, "( avg. ", rerollsAll/itmax, " rerolls per itteration)\n")

#I know it's not TRUE true random, pedantic CS-nerd, but give me a break!
print("\nTrue random created by random.randrange( 1,", numRules+1, ")\n")
for i in range (0, len(rollArrTrueRand)):

    if i == 0:
        print("  Rolls in range 1 - 99    : ", rollArrTrueRand[i]/itmax*100, "% (", rollArrTrueRand[i], ")")

    elif ((i*100+99) > numRules):
        print("  Rolls in range", i*100, "-", numRules, ": ", rollArrTrueRand[i]/itmax*100, "% (", rollArrTrueRand[i], ")")
    
    else:
        print("  Rolls in range", i*100, "-", i*100+99, ": ", rollArrTrueRand[i]/itmax*100, "% (", rollArrTrueRand[i], ")")


print("")




