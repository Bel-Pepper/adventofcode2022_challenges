#Solution for Advent of Code Challenge 4 part 1 in python

#pathlib's "Path" will take your file path and convert its format 
#to whatever the current OS wants
from pathlib import Path

def main():
    overlap=0
    total=0
    file_to_open=Path("Advent4/advent4.txt")
    f=open(file_to_open)

    for line in f:
        if line:
            tally=0
            #split the input into an array, then remove /n
            elves=line.split(",")
            elves[1]=elves[1].strip()
            #create elfA array, turn it into ints, and fill
            #the blanks with the missing range
            elfA=elves[0]
            elfA=elfA.split("-")
            elfA[0]=int(elfA[0])
            elfA[1]=int(elfA[1])
            elfA=range(elfA[0], elfA[1]+1)
            #second verse same as the first
            elfB=elves[1]
            elfB=elfB.split("-")
            elfB[0]=int(elfB[0])
            elfB[1]=int(elfB[1])
            elfB=range(elfB[0], elfB[1]+1)

            #print(list(elfA), list(elfB))

            #compare the smaller to the larger
            if len(elfA) >= len(elfB):
                smaller=len(elfB)
                for x, val in enumerate(elfB):
                    if elfB[x] in elfA:
                        tally=tally+1

            elif len(elfB) > len(elfA):
                smaller=len(elfA)
                for x, val in enumerate(elfA):
                    if elfA[x] in elfB:
                        tally=tally+1
            if tally == smaller:
                total=total+1
            print ("overlap ==", total)
        
        if not line:
            print ("done")
            f.close()
            
    
if __name__ == "__main__":
    main()