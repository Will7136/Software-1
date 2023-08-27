word = (input("Please enter a word : ")).lower()
charList = []
shift = int(input("Please enter a shift value : "))

for x in range (0, len(word), 1):
    charList.append(word[x])


letterArr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
newWord = ""
newChars = []
for values in charList:
    for letterCounter in range (0, len(letterArr)):
        if values == letterArr[letterCounter]:
            newChars.append(letterArr[((letterCounter + shift) % 26)])
            break


for letters in newChars:
    newWord = newWord + letters
    
print(newWord)
