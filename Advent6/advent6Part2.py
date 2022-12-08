#Advent of Code Challenge 6 part 2 in python
from pathlib import Path
file_to_open=Path("Advent6/advent6Test.txt")


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
    markerLen=4
    messageLen=14

    while True:
        line=f.readline()

        if not line:
            f.close
            break
        if line:
            if flag is False:
                for x in range(len(line)):
                    if line[x+markerLen] == "\n":
                        print("")
                        flag=False
                        break
                    buffer=line[x:x+markerLen]
                    #print (buffer)
                    reps=checkBuf(buffer)
                    #print (reps)
                    if reps == False:
                        packetStart=x+markerLen
                        print ("Packet start:  ", packetStart)
                        flag=True
                        break

        if flag == True:
#Check the rest of the text for the message, between start of packet and 
# total end len
            for x in range(packetStart,len(line)):
#Verify there isn't an eol
                if line[x+messageLen] == "\n":
                    print("here")
                    flag=False
                    break
#Make the buffer between the start of packet and the len of message
                buffer=line[x:x+messageLen]
#Check the buffer for repeats
                reps=checkBuf(buffer)

                if reps == False:
                    messageStart=x+messageLen
                    print ("Message start: ", messageStart)
                    flag=True
                    break
                
        flag=False


if __name__ == "__main__":
    main()