#Solution for Advent of Code Challenge 2 part 1 in python

#Put your file path here!!!
fileLocation = "ThisSpaceIntentionallyLeftBlank"
file = open(fileLocation)

#initialize some variables
oppChoice = 0
plaChoice = 0
plaTotal = 0
scoreTotal = 0
resNeeded = 0

#Check to see if you won or lost. Your moves are x, opponents are y
def WinLose(x,y):
    if x == y:
        result="Draw"
    elif x == "R":
        if y == "P":
            result="Lose"
        elif y == "S": 
            result="Win"

    elif x == "P":
        if y == "R":
            result = "Win"
        elif y == "S": 
            result = "Lose"
    elif x == "S":
        if y == "R":
            result = "Lose"
        elif y== "P":
            result = "Win"
    return result

#gets the score from your result
def resScore(x):
    if x == "Win":
        score = 6
    elif x == "Lose":
        score = 0
    elif x == "Draw":
        score = 3
    return score

#gets the score from what you played
#I don't think this is how people actually play RPS
#Elves are fucking weird
def playScore(x):
    if x == "R":
        score=1
    elif x == "P":
        score=2
    elif x == "S":
        score=3
    return score
#Tells you what you need to choose
#based on what the desired outcome is (x) and what the opponent chose (y)
def whatDo(x,y):
    if x == "W":
        if y=="R":
            do = "P"
        elif y=="P":
            do = "S"
        elif y== "S":
            do = "R"
    if x == "L":
        if y=="R":
            do = "S"
        elif y=="P":
            do = "R"
        elif y== "S":
            do = "P"

    if x == "D":
        do=y
    return do



while True:

    next_Line=(file.readline())
    
    print (next_Line)
#Takes in what you did and what you needed do
    if next_Line:
        if "A" in next_Line:
            #print ("Opponent chose Rock")
            oppChoice="R"
        elif "B" in next_Line:
            #print ("Opponent chose Paper")
            oppChoice="P"
        elif "C" in next_Line:
            #print ("Opponent chose Scissors")
            oppChoice="S"
            
        if "X" in next_Line:
            #print ("You chose Rock")
            resNeeded="L"
        elif "Y" in next_Line:
            #print ("You chose Paper")
            resNeeded="D"
        elif "Z" in next_Line:
            #print ("You chose Scissors")
            resNeeded="W"
#Now calls all the things that actually do the things

#Tells you what to do, saves it to plaChoice
        plaChoice = whatDo(resNeeded, oppChoice)

#Now to calculate score, and then add to the
        result = WinLose(plaChoice, oppChoice)
        #print ("Your result:", result)
        score = resScore(result)+playScore(plaChoice)
        #print ("You scored ", score)
        scoreTotal=scoreTotal+score
    if not next_Line:
        print ("Total Score=", scoreTotal)
        break

file.close