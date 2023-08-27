# num = int(input("Enter a number : "))
# sum = num
# while num > 0 :
#     num =  int(input("Enter a number : "))
#     sum = sum + num
# print(sum)


# num = int(input("Enter a number : "))
# sum = num
# counter = 1
# while num > 0 :
#     num =  int(input("Enter a number : "))
#     sum = sum + num
#     counter = counter + 1
# print((sum/counter))

# num = int(input("Enter a number : "))
# evenCounter = 0
# if num % 2 == 0:
#     evenCounter = 1
# while num > 0 :
#     num =  int(input("Enter a number : "))
#     if num % 2 == 0:
#         evenCounter = evenCounter + 1
# print(evenCounter)

# num = int(input("Please enter a number : "))
# sum = 0
# for counter in range (0, (num + 1)):
#     if (num - counter) % 2 == 0:
#         sum = sum + (num - counter)

# print(sum)


# num = int(input("Please enter a number : "))
# for counter in range (1, 13):
#     print(counter * num)

num = int(input("Please enter a number : "))
total = 1
for counter in range (0, num ):
        total = total * (num - counter)

print(total)