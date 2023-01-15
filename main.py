import math
import time
import ESeries
import simpleParsers
import printList

def computeBestPair(testIndex, list, ratio, multiplier): #test R1 against potential R2s
    """ 'testIndex' is the index of the R1 against which the R2s will be evaluated
        'list' is the list of values being evaluated
        'ratio' is the ratio being evaluated (0 to 1) per the voltage divider equation
        'multiplier' sets decade of R2 values (multiplies R2 values by a factor of 10) """
    bestPercentError = -1
    outputList = [list[testIndex] * multiplier, list[0], bestPercentError, '%'] #Prepare output list

    for index, item in enumerate(list):
        testRatio = (list[index])/(list[testIndex] * multiplier + list[index])
        percentError = math.fabs( (testRatio - ratio)/ratio) * 100

        if percentError < bestPercentError or bestPercentError == -1: # Replace the best ratio if this one is better
            outputList[1] = item
            outputList[2] = percentError
            bestPercentError = percentError
    return outputList

#Assign imported E-Series lists to a list-of-lists
listOfESeries = [ESeries.E6, ESeries.E12, ESeries.E24, ESeries.E48, ESeries.E96]
listOfESeriesNames = ['E6', 'E12', 'E24', 'E48', 'E96']


while True:
    print("\n======== E-Series Voltage Divider Finder ========")

    # Prompt user's choice of E-Series list
    intESeriesChoice = 'invalid'
    while intESeriesChoice == 'invalid':
        print("Choose an E-Series set:\n[1]:E6\t[2]:E12\t[3]:E24\t[4]:E48\t[5]:E96" + '\n' + '[Integer 1-5:] >', end='')
        intESeriesChoice = simpleParsers.parseInt(input(), 5, 1, False) - 1

    # Print E-Series list:
    print('\n' + listOfESeriesNames[intESeriesChoice] + ':')
    printList.printBoxList(listOfESeries[intESeriesChoice], 6)

    # Prompt user's choice of ratio
    ratio = 'invalid'
    while ratio == 'invalid':
        print("Choose a ratio per the voltage divider equation: R2/(R1 + R2)" + '\n' + '[Float 0-1:] >', end='')
        ratio = simpleParsers.parseFloat(input(), 1)


    """ Begin calculating pages of values:
        Process:
            1. Calculate round(log10(R1))
                a. R1 = ( 1 - rR2^2 )/(rR2) or ( 1/(rR2) - R2
            2. Adjust multiplier
            3. Calculate pages on either side of calculated value (3 total)"""
    outputPage = [] # Will contain three pages of values: below, at, and above calculated
    estimatedR1 = (1/ratio) - 1
    multiplier = 10**round(math.log10(estimatedR1)) # Estimated multiplier necessary for R1

    for x in range(0, 3): # Creates 3 pages
        for index, item in enumerate(listOfESeries[intESeriesChoice]): # Add each best pair to the current page
            outputPage.append(computeBestPair(index, listOfESeries[intESeriesChoice], ratio, multiplier * (10**(x-1))))

    outputPage.sort(key=lambda l: l[2]) # Sort by percent error
    print('\n', "Format: [ R1 , R2 , %ERROR }", sep='')
    printList.printBoxList(outputPage, 6, 4, 2)


    print('Completed program. Restarting...\n')