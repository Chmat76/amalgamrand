import random
import math

#Borrowed from https://realpython.com/python-print/
def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)

itmax = 250000
numRules=223
probOneRule = 1/numRules
progressBar = 0

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
print("Current rule 172, Wild Experiment Card, algorithm:")
print("  Roll a d10 3 times. Each itteration is a digit. Reroll 100's digit if no such rule\n")
print("Suggested rule change")
print("  Roll a d10 3 times. Each itteration is a digit. Reroll ALL digits if no such rule\n")

#Print theoretical expected results
print("\nExpected results if true random:\n")
for i in range (0, len(rollArrRerollTop)):

    if i == 0:
        low = 1
        if numRules > 99:
            high = 99
        else:
            high = numRules
        prob = high*probOneRule*100
        rolls = itmax/numRules*high
        
    elif ((i*100+99) > numRules):
        low   = i*100
        high  = numRules
        prob  = (numRules-i*100+1)*probOneRule*100
        rolls = itmax/numRules*(numRules-i*100+1)
    else:
        low   = i*100
        high  = i*100+99
        prob  = 100*probOneRule*100
        rolls = itmax/numRules*100
        
    print("  Rolls in range %(lowrange)d - %(highrange)d:\t %(prob).3f%% (%(rolls)d rolls)" % {"lowrange":low, "highrange":high, "prob":prob, "rolls":rolls})


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
    if progressBar > 0 :
        progress(int((i/itmax*100)/3))
    
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
    
    if progressBar > 0 :
        progress(33+int((i/itmax*100)/3))


#Sanity check. Have computer generate random values within range
for i in range (0, itmax):
    roll = random.randrange(1, (numRules+1))
    rollArrTrueRand[int((roll)/100)] = rollArrTrueRand[int((roll)/100)] + 1
    
    if progressBar > 0 :
        rogress(67+int((i/itmax*100)/3))



#print results
print("\nRoll results")
print("\nCurrent:\nReroll TOP digit if no existing rule\n")

for i in range (0, len(rollArrRerollTop)):

    if i == 0:
        low = 1
        if numRules > 99:
            high = 99
        else:
            high = numRules
            
        prob = rollArrRerollTop[i]/itmax*100
        rolls = rollArrRerollTop[i]

    elif ((i*100+99) > numRules):
        
        low   = i*100
        high  = numRules
        prob  = rollArrRerollTop[i]/itmax*100
        rolls = rollArrRerollTop[i]
    
    else:
        
        low   = i*100
        high  = i*100+99
        prob  = rollArrRerollTop[i]/itmax*100
        rolls = rollArrRerollTop[i]
        
    print("  Rolls in range %(lowrange)d - %(highrange)d:\t %(prob).3f%% (%(rolls)d rolls)" % {"lowrange":low, "highrange":high, "prob":prob, "rolls":rolls})

print("\n  Rerolls: %(rerolls)d ( avg. %(avg).3f rerolls per itteration)\n" % { "rerolls":rerollsTop, "avg":rerollsTop/itmax })

print("\nSuggested:\nReroll ALL if no existing rule\n")

for i in range (0, len(rollArrRerollAll)):

    if i == 0:
        low = 1
        if numRules > 99:
            high = 99
        else:
            high = numRules
            
        prob = rollArrRerollAll[i]/itmax*100
        rolls = rollArrRerollAll[i]

    elif ((i*100+99) > numRules):
        
        low   = i*100
        high  = numRules
        prob  = rollArrRerollAll[i]/itmax*100
        rolls = rollArrRerollAll[i]
    
    else:
        
        low   = i*100
        high  = i*100+99
        prob  = rollArrRerollAll[i]/itmax*100
        rolls = rollArrRerollAll[i]
        
    print("  Rolls in range %(lowrange)d - %(highrange)d:\t %(prob).3f%% (%(rolls)d rolls)" % {"lowrange":low, "highrange":high, "prob":prob, "rolls":rolls})

print("\n  Rerolls: %(rerolls)d ( avg. %(avg).3f rerolls per itteration)\n" % { "rerolls":rerollsTop, "avg":rerollsTop/itmax })

#I know it's not TRUE true random, pedantic CS-nerd, but give me a break!
print("\nTrue random created by random.randrange( 1,", numRules+1, ")\n")
for i in range (0, len(rollArrTrueRand)):

    if i == 0:
        low = 1
        if numRules > 99:
            high = 99
        else:
            high = numRules
            
        prob = rollArrTrueRand[i]/itmax*100
        rolls = rollArrTrueRand[i]

    elif ((i*100+99) > numRules):
        
        low   = i*100
        high  = numRules
        prob  = rollArrTrueRand[i]/itmax*100
        rolls = rollArrTrueRand[i]
    
    else:
        
        low   = i*100
        high  = i*100+99
        prob  = rollArrTrueRand[i]/itmax*100
        rolls = rollArrTrueRand[i]
        
    print("  Rolls in range %(lowrange)d - %(highrange)d:\t %(prob).3f%% (%(rolls)d rolls)" % {"lowrange":low, "highrange":high, "prob":prob, "rolls":rolls})


print("")


