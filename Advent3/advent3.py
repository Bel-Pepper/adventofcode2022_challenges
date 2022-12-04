#Solution for Advent of Code Challenge 3 part 1 in python
#Time to start actually using some style guides 
#and try to make it look //pythonic//

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

    file_to_open=Path("Advent3/advent3Test.txt")
    f=open(file_to_open)

    #init vars
    tot=0

    for line in f:
        #Check to make sure there is a line to read, then split it into
        #two compartments, one for each half of the line
        if line:
            size=getCompartmentSize(line)
            comp1=line[:size]
            comp2=line[size:]

            #This part takes the list of letters in the first compartment
            #and checks for a match in the second
            #It takes that match and asks score() to asign it a value
            #Then adds the value to the running total
            search=list(comp1)
            for x in search:
                if x in comp2:
                    tot=tot+score(x)
                    break

        if not line:
            print (tot)
            f.close()
            break
    print ("Total is", tot)

if __name__ == "__main__":
    main()