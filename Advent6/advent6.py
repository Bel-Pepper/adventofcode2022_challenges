#Advent of Code Challenge 6 part 1 in python
from pathlib import Path
file_to_open=Path("Advent6/advent6.txt")


def checkBuf(x):
    Repeats=False
    for i in range(len(x)):
        if x.count(x[i]) > 1:
            Repeats=True
    return Repeats
    

def main():
    f = open(file_to_open)
    buffer=[]
    column=0
    reps=True
    flag=False

    while True:
        line=f.readline()

        if not line:
            f.close
            break
        if line:
            if flag is False:
                for x in range(len(line)):
                    if line[x+4] == "\n":
                        print("")
                        flag=False
                        break
                    buffer=line[x:x+4]
                    #print (buffer)
                    reps=checkBuf(buffer)
                    #print (reps)
                    if reps == False:
                        print (x+4)
                        flag=True
                        break
        flag=False


if __name__ == "__main__":
    main()