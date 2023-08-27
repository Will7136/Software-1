import string

############ Excersize 1 ########################
def isPalindrome(value):
    sanitisedValue = value.translate(str.maketrans('', '', string.punctuation))
    charList = []

    for counter in range(0, len(sanitisedValue),1):
        if sanitisedValue[counter] != " " :
            charList.append(sanitisedValue[counter])


    revValue = ""
    finValue = ""


    for index in range(len(charList)):
        revValue = revValue + charList[(index * -1) - 1]
    for index in range(len(charList)):
        finValue = finValue + charList[index]

    if revValue == finValue:
        print("is a palindrome")
    else:
        print("isn't a palindrome")
        

# entry = input("enter a word : ").lower()
# isPalindrome(entry)

############ Excersize 2 ########################
def sentenceToCamel(value):
    charList = []
    capitaliseList = [0]
    whitespaceCounter = 0

    for counter in range(0, len(value),1):
        if value[counter] != "  " and value[counter] != " ":
            charList.append(value[counter])
        else:
            capitaliseList.append((counter - whitespaceCounter))
            whitespaceCounter = whitespaceCounter + 1

    for index in range(len(capitaliseList)):
        charList[capitaliseList[index]] = (charList[capitaliseList[index]]).upper()

    finValue = ""
    for index in range(len(charList)):
        finValue = finValue + charList[index]
            
    print(finValue)

# entry = input("enter a word : ").lower()
# sentenceToCamel(entry)

############ Excersize 3 ########################
def camelToSentence(value):
    charList = []
    newWordPoints = []

    for counter in range(0, len(value),1):
        charList.append(value[counter])
        tempChar = value[counter]
        if tempChar != value[counter].lower():
            newWordPoints.append(counter)
            
    newWordPoints.append(len(value))
            
    finalWordList = []
    for y in range(len(newWordPoints) - 1):
        newWord = ""
        for x in range(newWordPoints[y],newWordPoints[y+1],1 ):
            newWord = newWord + charList[x]
        finalWordList.append(newWord)
        
    for values in finalWordList:
        print(values)

# entry = input("enter a sentence in camel case : ")
# camelToSentence(entry)