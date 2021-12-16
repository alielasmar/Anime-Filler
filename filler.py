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
    fillerL = []
    count = 0
    with open(fname,'r') as filler:
        for line in filler:
            for character in line:
                fillerL.append(character)
    #print(fillerL)
    deleteSpaces(fillerL)                   

def deleteSpaces(fillerL):                  #if current element is a space or new line then delete it
    for i in range(len(fillerL)):
        if i < len(fillerL):
            if fillerL[i] == " ":
                del fillerL[i]
            if fillerL[i] == "\n":
                del fillerL[i]
    combineCompoundNumbers(fillerL)

def combineCompoundNumbers(fillerL):        #checks to see if current and next element in array are ints
    for i in range(len(fillerL)):
        if i <= len(fillerL) -2:
            if fillerL[i] != ',' and fillerL[i] != '-':
                if fillerL[i+1] != ',' and fillerL[i+1] != '-' and fillerL[i+2] != ',' and fillerL[i+2] != '-':
                    tmp = fillerL[i] + fillerL[i+1] + fillerL[i+2]
                    del fillerL[i+2]
                    del fillerL[i+1]
                    del fillerL[i]
                    fillerL.insert(i,tmp)   #insert at current element, placement matters because of dashes
                elif fillerL[i+1] != ',' and fillerL[i+1] != '-':
                    tmp = fillerL[i] + fillerL[i+1]
                    del fillerL[i+1]
                    del fillerL[i]
                    fillerL.insert(i,tmp)
                    
                    #print(tmp)
    #print(fillerL)
    deleteCommas(fillerL)


def deleteCommas(fillerL):                  #if an element is a comma it's deleted
    #print(len(fillerL))
    for i in range(len(fillerL)):
        if i < len(fillerL):
            if fillerL[i] == ',':
                del fillerL[i]
    #print(fillerL)
    convertStrToInt(fillerL)


def convertStrToInt(fillerL):           # converts str to int
    for i in range(len(fillerL)):
        if fillerL[i] != '-':
            fillerL[i] = int(fillerL[i])
    print(fillerL,end="\n \n \n")
    addBetweenDashes(fillerL)


def addBetweenDashes(fillerL):          # if there is a dash, store element before and after, iterate between them and append to list
    maximum = checkMax(fillerL)
    minimum = fillerL[0]
    for i in range(len(fillerL)):
        if fillerL[i] == '-':
            count = 0
            before = fillerL[i-1]
            after = fillerL[i+1]
            while before < after-1:
                before = before + 1
                #print('before: ',end=" ")
                #print(before)
                if not before < minimum:
                    #print(not before < minimum, end = ",")
                    #print('before: ',end=" ")
                    #print(before)
                    fillerL.append(before)
    #print(fillerL)
    delDashes(fillerL)
                    
def delDashes(fillerL):             #Deletes dashes found in array
    for i in range(len(fillerL)):
        if(i < len(fillerL)):
            if fillerL[i] == "-":
                fillerL.remove("-")
    print(fillerL)
    #sortList(fillerL)

#DISABLED OTHER FUNCTIONS TEMPORARILY













def sortList(fillerL):
    fillerL.sort()
    print(fillerL)
    userInput(fillerL)


def userInput(fillerL):
    error = False
    curEp = int(input('enter in # episode you are on:'))
    maximum = checkMax(fillerL)
    print( curEp in fillerL and error == True)
    
    if curEp > maximum:
        print("The episode entered is not in list of episodes")
        error = True
        
    elif curEp in fillerL and error == False:
        print("episode found")
        curPos = fillerL.index(curEp)
        epLeft = len(fillerL) - curPos
        print("episodes left", end = " ")
        print (epLeft)
        
    elif curEp < maximum and error == False and curEp not in fillerL:
        print("searching for episode")
        while curEp not in fillerL:
            curEp = curEp +1
        curPos = fillerL.index(curEp)
        epLeft = len(fillerL) - curPos
        print("episodes left", end = " ")
        print (epLeft)


def checkMax(fillerL):
    indx = len(fillerL)-1
    maximum = fillerL[indx]
    return maximum
        
    

main()
