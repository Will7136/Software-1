# baseNum = int(input("enter a positive number :"))
# numTracker = 0 
# total = 0
# for counter in range(0, baseNum, 1):
#     if numTracker <= baseNum:
#         numTracker = numTracker + 1
#         if numTracker % 2 == 0:
#             total = total + numTracker
# print(total)

baseNum = int(input("enter a positive number :"))
for counter in range(0, 12, 1):
    print((counter + 1)* baseNum)

# baseNum = int(input("enter a positive number :"))
# total = 1
# for counter in range(0, baseNum, 1):
#     total = total * (baseNum - counter)
# print(total)