#Solution for Advent of Code Challenge 1 part 1 in python
#Still have comments for when using the test document and actually wanting to print everything out

#Put your file path here!!!
fileLocation = "ThisSpaceIntentionallyLeftBlank"

file = open(fileLocation)
#Lets initialize some shit
elf = 1
total = 0
high = 0

#The main loop. Tell me you are used to C++ without telling me you are used to C++
while True:
    next_Line = file.readline()

#   Check to see if the current elf is done reporting calories
    if next_Line.strip() != '':
        total = int(next_Line.strip()) + total
        
    #if they are then sum up the total and check to see if it beats the high score
    
    else:
        #print ("total = ", total)
        if total > high:
            high = total
            #print ("New high is ", high)
        total = 0

    #At the end of the file print the high score and close the loop
    if not next_Line:
        print ("Highest total is", high)
        break;
        
    #print (next_Line.strip())
file.close