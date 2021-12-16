# Use beautiful soup to store data from animefilerlist.com
# read file passed
# turn text inro numerical values readable to machines
# store values in csv file (temporary, will be using mongodb after learning it)
# HTML Development (graphic design of website and storing static images using S3)
# 
#
#

def main():
    fname = input('enter in name of file: ')
    print(fname)
    getNumbersInArray(fname)                #gets name of file and passes to next function

def getNumbersInArray(fname):               #reads file char by char and appends to list
    cannonL = []
    count = 0
    with open(fname,'r') as filler:
        for line in filler:
            for character in line:
                cannonL.append(character)
    #print(cannonL)
    deleteSpaces(cannonL)                   

def deleteSpaces(cannonL):                  #if current element is a space or new line then delete it
    for i in range(len(cannonL)):
        if i < len(cannonL):
            if cannonL[i] == " ":
                del cannonL[i]
            if cannonL[i] == "\n":
                del cannonL[i]
    combineCompoundNumbers(cannonL)

def combineCompoundNumbers(cannonL):        #checks to see if current and next element in array are ints
    for i in range(len(cannonL)):
        if i <= len(cannonL) -2:
            if cannonL[i] != ',' and cannonL[i] != '-':
                if cannonL[i+1] != ',' and cannonL[i+1] != '-' and cannonL[i+2] != ',' and cannonL[i+2] != '-':
                    tmp = cannonL[i] + cannonL[i+1] + cannonL[i+2]
                    del cannonL[i+2]
                    del cannonL[i+1]
                    del cannonL[i]
                    cannonL.insert(i,tmp)   #insert at current element, placement matters because of dashes
                elif cannonL[i+1] != ',' and cannonL[i+1] != '-':
                    tmp = cannonL[i] + cannonL[i+1]
                    del cannonL[i+1]
                    del cannonL[i]
                    cannonL.insert(i,tmp)
                    
                    #print(tmp)
    #print(cannonL)
    deleteCommas(cannonL)


def deleteCommas(cannonL):                  #if an element is a comma it's deleted
    #print(len(cannonL))
    for i in range(len(cannonL)):
        if i < len(cannonL):
            if cannonL[i] == ',':
                del cannonL[i]
    #print(cannonL)
    convertStrToInt(cannonL)


def convertStrToInt(cannonL):           # converts str to int
    for i in range(len(cannonL)):
        if cannonL[i] != '-':
            cannonL[i] = int(cannonL[i])
    print(cannonL,end="\n \n \n")
    addBetweenDashes(cannonL)


def addBetweenDashes(cannonL):          # if there is a dash, store element before and after, iterate between them and append to list
    maximum = checkMax(cannonL)
    minimum = cannonL[0]
    for i in range(len(cannonL)):
        if cannonL[i] == '-':
            count = 0
            before = cannonL[i-1]
            after = cannonL[i+1]
            while before < after-1:
                before = before + 1
                cannonL.append(before)
    #print(cannonL)
    delDashes(cannonL)
                    
def delDashes(cannonL):             #Deletes dashes found in array
    for i in range(len(cannonL)):
        if(i < len(cannonL)):
            if cannonL[i] == "-":
                cannonL.remove("-")
    #print(cannonL)
    sortList(cannonL)


def sortList(cannonL):
    cannonL.sort()
    print(cannonL)
    userInput(cannonL)


def userInput(cannonL):
    error = False
    curEp = int(input('enter in # episode you are on:'))
    maximum = checkMax(cannonL)
    
    if curEp > maximum:
        print("The episode entered is not in list of episodes")
        error = True

    if curEp < 0:
        error = True
        print("Please enter in a positive number")
        
    elif curEp in cannonL and error == False:
        curPos = cannonL.index(curEp)
        epLeft = len(cannonL) - curPos
        print("episodes left", end = " ")
        print (epLeft)
        
    elif curEp < maximum and error == False and curEp not in cannonL:
        while curEp not in cannonL:
            curEp = curEp +1
        curPos = cannonL.index(curEp)
        epLeft = len(cannonL) - curPos
        print("episodes left", end = " ")
        print (epLeft)
    if error == True:
        userInput(cannonL)


def checkMax(cannonL):
    indx = len(cannonL)-1
    maximum = cannonL[indx]
    return maximum
        
    

main()
