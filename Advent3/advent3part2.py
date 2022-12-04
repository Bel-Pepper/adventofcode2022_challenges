#Solution for Advent of Code Challenge 3 part 2 in python

#pathlib's "Path" will take your file path and convert its format 
#to whatever the current OS wants
from pathlib import Path

#This gets the size of each compartment
#which is to say, it 
def getCompartmentSize(x):
    x=x.strip()
    full_len=len(x)
    compSize=full_len / 2
    compSize=int(compSize)
    return compSize

    
#I would love it if I could make a range for these. Too bad ascii
#ranges are Uppercase first. Could still make it work but feels ok.
#has two arrays, basically multidimensional but too lazy for numpy
#correlates rows. Worth looking into a better execution
#returns the point value of the letter
def score(x):
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
    "p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F",
    "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W",
    "X","Y","Z"]
    points=[*range(1,53)]
    conversion=letters.index(x)
    output=points[conversion]
    return output


def main():

    file_to_open=Path("Advent3/advent3.txt")
    f=open(file_to_open)

    #init vars
    tot=0

    for line in f:

        #Check to make sure there is a line to read (This makes less sense 
        #in p2) then saves first three lines, strips \n 's from them
        #and then breaks elfA's list into component characters
        if line:
            size=getCompartmentSize(line)
            elfA=line
            elfA=elfA.strip()
            elfB=f.readline()
            elfB=elfB.strip()
            elfC=f.readline()
            elfC=elfC.strip()
            searchA=list(elfA)

            #Check to see if something is in A and B, then see if its also
            #in C. If it is, score and add to total. 
            for x in searchA:
                if x in elfB:
                    if x in elfC:
                        sc=score(x)
                        tot=tot+sc
                        break
                
        if not line:
            print (tot)
            f.close()
            break
    print ("Total is", tot)

if __name__ == "__main__":
    main()