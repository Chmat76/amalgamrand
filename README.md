This is a simple repo simulating Chemicard's rule 172 reroll mechanic using Python

Typical result from running the code:
    
    This code will simulate rerolling for 250000 times for two dice algorithms.
    
    Current rule 172, Wild Experiment Card, algorithm:
      Roll a d10 3 times. Each itteration is a digit. Reroll 100's digit if no such rule
    
    Suggested rule change
      Roll a d10 3 times. Each itteration is a digit. Reroll ALL digits if no such rule
    
    
    Expected results if true random:
    
      Rolls in range 1 - 99:         44.395% (110986 rolls)
      Rolls in range 100 - 199:      44.843% (112107 rolls)
      Rolls in range 200 - 223:      10.762% (26905 rolls)
    
    
    Please wait for roll simulation to finish...
    Roll results
    
    Current:
    Reroll TOP digit if no existing rule
    
      Rolls in range 1 - 99:         45.638% (114095 rolls)
      Rolls in range 100 - 199:      46.198% (115496 rolls)
      Rolls in range 200 - 223:      8.164% (20409 rolls)
    
      Rerolls: 652570 ( avg. 2.610 rerolls per itteration)
    
    
    Suggested:
    Reroll ALL if no existing rule
    
      Rolls in range 1 - 99:         44.470% (111174 rolls)
      Rolls in range 100 - 199:      44.764% (111909 rolls)
      Rolls in range 200 - 223:      10.767% (26917 rolls)
    
      Rerolls: 873660 ( avg. 3.495 rerolls per itteration)
    
    
    True random created by random.randrange( 1, 224 )
    
      Rolls in range 1 - 99:         44.370% (110926 rolls)
      Rolls in range 100 - 199:      44.868% (112170 rolls)
      Rolls in range 200 - 223:      10.762% (26904 rolls)