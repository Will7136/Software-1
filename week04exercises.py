######################### EXERCISE 1 #############################################
def sum_digits(input):
    value = str(input)
    total = 0
    for counter in range (0, len(value)):
        digit = int(value[counter])
        total= total + digit
    return(total)


######################### EXERCISE 2 #############################################
def pairwise_digits(x, y):
    output = ""
    a = str(x)
    b = str(y)
    if int(a) >= int(b):
        print("a>b")
        return(pairwise_loop(a,b,output))
    else:
        print("a<b")
        return(pairwise_loop(b,a,output))
    
def pairwise_loop(num1, num2, str):
        for counter in range (0, len(num1)):
            if len(num2) <= counter:
                str = str + "0"
            else:
                if num1[counter] == num2[counter]:
                    str = str + "1"
                else:
                    str = str + "0"
        return(str)
    
######################### EXERCISE 3 #############################################
def to_base10(input):
    binary = str(input)
    total = 0
    for counter in range(0, len(binary)):
        if binary[counter] == "1":
            total = total + 2**(len(binary) - (counter + 1))
    return(total)

######################### EXERCISE 5 #############################################
def sum_lists(data):
    output =[]
    total = 0
    for row in data:   
        for val in row:
            total += val
        output.append(total)
        total = 0
    return(output)

    