
#Put your file path here!!!
fileLocation = ThisSpaceIntentionallyLeftBlank

file = open(fileLocation)
elf = 1
total = 0
high = 0
while True:
    next_Line = file.readline()

    if next_Line.strip() != '':
        total = int(next_Line.strip()) + total
        
    else:
        #print ("total = ", total)
        if total > high:
            high = total
            #print ("New high is ", high)
        total = 0


    if not next_Line:
        print ("Highest total is", high)
        break;
        
    #print (next_Line.strip())
file.close