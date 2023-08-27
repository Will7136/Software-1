############ Excersize 1 ########################
aWord = input("Please enter a word : ")
f = open("exo1.txt", 'a')
f.write(aWord)
f.close()

############ Excersize 2 ########################
def SaveList2File(sentences, filename):
    f = open(filename, 'w')
    for words in sentences:
        f.write(words + '\n')
    f.close()
    print("complete")

############ Excersize 3 ########################
def SaveToLog(entry, logFile):
    f = open(logFile, 'a')
    f.write(entry)
    f.close()

