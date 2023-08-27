# aWord = input("Please enter a word : ")
# f = open("exo1.txt", 'a')
# f.write(aWord)
# f.close()




# def SaveList2File(sentences, filename):
#     f = open(filename, 'w')
#     for words in sentences:
#         f.write(words + '\n')
#     f.close()
#     print("complete")

# def MakeList():
#     entry = input("enter :")
#     newList = []
#     while entry != "stop":
#         newList.append(entry)
#         entry = input("Enter a word to add to a list : ")
#     return(newList)

# filePath = input("Please enter a filepath : ")
# wordList = []
# wordList = MakeList()
# SaveList2File(wordList, filePath)


def SaveToLog(entry, logFile):
    f = open(logFile, 'a')
    f.write(entry)
    f.close()

filepath = input("enter a filepath : ")
value = input("enter a value : ")
SaveToLog(value, filepath)