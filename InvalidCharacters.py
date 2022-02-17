def main():

    # these static values are the number ranges for valid characters when converted to integers using the ord function
    numericValuesAndColon = (48,58)
    lowerAlphaValues = (97,122)
    upperAlphaValuesAndAt = (64,90)
    underScoreValue = 95
    dashPeriodForwardSlash = (45,47) 
    dollarSignValue = 36
    equalSignValue = 61
    newLineValue = 10
    spaceValue = 32

    # put these in a list to shorten code for conditional statements below
    singularValues = [dollarSignValue,equalSignValue,underScoreValue]

    # not sure if new lines and spaces count as alphanumeric so I have their values stored just in case
    unsureValues = [newLineValue, spaceValue]
    try:
        fileLocation = input("Please enter path of .ach file: ")
        if (fileLocation[-4:] != ".ach"):
            print("You have entered an incorrect file type")
        
        fileToProcess = open(fileLocation, 'r')
        Lines = fileToProcess.readlines()

        #tracking index and number of characters that are in the unsure list
        numberOfSpacesNewLines = 0
        characterIndex = 0
        lineIndex = 0
        for line in Lines:
            for character in line:
                decValue = ord(character)
                if not (lowerAlphaValues[0] <= decValue <= lowerAlphaValues[1]) \
                    and not (numericValuesAndColon[0] <= decValue <= numericValuesAndColon[1]):
                    if not (upperAlphaValuesAndAt[0] <= decValue <= upperAlphaValuesAndAt[1])\
                         and not (dashPeriodForwardSlash[0] <= decValue <= dashPeriodForwardSlash[1]):
                        if (decValue not in singularValues):
                            if decValue in unsureValues:
                                # left this code here to show that if we needed to consider newlines or spaces as not
                                # alphanumeric there is logic for it

                                # print("This is either a new line or a space")
                                # print("found on line: "+ str(lineIndex) +"\nat position: " +str(characterIndex) + '\n')
                                # print("either a space or newline")
                                numberOfSpacesNewLines += 1


                            else:
                                print("The following character is not alphanumeric: "+character)
                                print("found on line: "+ str(lineIndex) +"\nat position: " +str(characterIndex) + '\n')
                
                characterIndex += 1
            characterIndex = 0
            lineIndex += 1
        print("Number of spaces and newlines characters: " + str(numberOfSpacesNewLines))



    # very basic error handling
    except BaseException as err:
        print("Something went wrong due to the following error: "+str(err))



main()