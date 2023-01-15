""" Print lists to print() in different ways
    inputList parameter: list of values OR list of lists of values to be sequenced
    itemsPerCell parameter: Number of items in each printed unit/bound cell
"""
from copy import deepcopy

def printBoxList(inputList, cellsPerRow=6, itemsPerCell=1, roundInt=4):
    outputList = []
    inputBuf = deepcopy(inputList)  # Create buffer of list that we can modify
    workList = inputBuf  # Create the variable that will we will point to the working list

    while True:
        if inputBuf == []:
            break
        while True:
            if inputBuf == []:
                break
            if isinstance(workList[0], list):
                if workList[0] == []:  # If that list is empty, get rid of it
                    workList.pop(0)
                    workList = inputBuf
                    continue
                else:
                    workList = workList[0]  # If workList[0] is a list, make workList that list
                    continue
            else:  # This will execute if workList IS a list, but workList[0] is NOT a list
                for item in workList:  # Add all items in workList to output
                    outputList.append(item)
                workList.clear()

                workList = inputBuf
                break
    for index, item in enumerate(outputList): # Make each item a string
        if isinstance(item, float):
            outputList[index] = round(item, roundInt) # Round any floats
            if item >= 10000: # If number is long on the other side of the decimal point, shorten using exponent
                outputList[index] = "{:.{roundInt}E}".format(item, roundInt = roundInt)
        outputList[index] = str(outputList[index])

    #Now we have a list of stitched-together values; find longest one:

    longestLength = 0
    for item in outputList: #Finding longest item in order to align output
        testLength = len(item)
        if testLength > longestLength:
            longestLength = testLength

    count = 1
    for x in range(0, len(outputList)): #Print values from outputList
        if (x % itemsPerCell == 0) and (x != 0):
            print(' ]', end='')
            count += 1
            if (count % (cellsPerRow + 1)) == 0:  # New line if cells-per-row is reached
                print()
                count = 1

        if (x + itemsPerCell) % itemsPerCell == 0: # Print start bracket at beginning of
            print('[ ', end='')
        print( "{:^{longestLength}}".format(outputList[x], longestLength = longestLength), end='') # Print item

    print(' ]')

