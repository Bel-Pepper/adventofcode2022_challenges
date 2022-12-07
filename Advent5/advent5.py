#Advent of Code Challenge 5 part 1 in python
#20221205 ~BF
from pathlib import Path


def ScrubStr(x):
    #removes all strings that can't be turned into an int from a list
    #and convert remainder to ints
    length=len(x)
    i=0
    while True:
        if i < len(x):
            try:
                int(x[i])
            except:
                del x[i]
            else:
                i+=1
        else:
            break
    for y in range(len(x)):
        x[y]=int(x[y])
    return x

def getCols():
    file_to_open=Path("Advent5/advent5TestStart.txt")
    arrays=open(file_to_open)
    stackcol=[]
    col=0
    while True:
        char=arrays.read(1)
        col+=1
        if char.isnumeric():
            stackcol.append(col)
        if char == "\n":
            col=0
        if not char:
            arrays.close()
            return stackcol

def main():
#the part that builds the stacks
    stackNums=getCols()
    file_to_open=Path("Advent5/advent5TestStart.txt")
    arrays=open(file_to_open)
    stackNums.reverse()
    lastStack=stackNums[0]
    stackNums.reverse()
    stacks=[]
    for i in range(len(stackNums)):
        stacks.append([stackNums[i]])
    print ("Columns with data are", stacks)

#the part that handles instructions
    file_to_open=Path("Advent5/advent5Testinstructions.txt")
    f=open(file_to_open)
    column=0
    i=0
    while True:
        char = arrays.read(1)
        #print (ord(char))
        if not char: 
            break
        #if '\n' in char:
        #    print("here")
        #    column=0
        #    i=0

#make sure there is a character before doing stuff
        if char:
#add to the times you've read (The column you're in)
            column+=1
            if column == stacks[i][0]:
                if char.isalpha():
                    stacks[i].append([char])
                i+=1
            if i >= len(stacks):
                i=0
            if char == "\n":
                column=0
                i=0
            
    for i in range(len(stackNums)):
        print (stacks[i])
#print (stacks[i].pop())
    arrays.close()
                
#Takes the instructions file and turns the whole thing into a single 
    for line in f:

        if line:
            instructions=line.split()
            instructions=ScrubStr(instructions)
            print (instructions)
            flagInstruc=True

        if not line:
            f.close()

#time to actually make this shit
        if flagInstruc:
            for i in range(len(instructions)):
                for y in range(0,instructions[0]):
                    print (len(stacks[i]))
                    print(" ")
                    print ("Moving", stacks[instructions[1]][len(stacks[i])], end=" ")
                    print ("from stack", instructions[1], end=" ")
                    print ("To stack", instructions[2])
                    stacks[instructions[2]].append(stacks[instructions[1]].pop())
                    print (stacks[y])
            flagInstruc=False
    print (stacks)




if __name__ == "__main__":
    main()