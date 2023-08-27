############ Excersize 1 ########################
number = int(input('enter a number : '))
evenCounter = 0
while number >= 0 :
    if number % 2 == 0 :
        evenCounter = evenCounter + 1
    number = int(input('enter a number : '))
print(evenCounter)
