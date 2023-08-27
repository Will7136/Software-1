def sum_digits(value):
    total = 0
    for counter in range (0, len(value)):
        digit = int(value[counter])
        total= total + digit
    return(total)

# num = input("Please enter a number : ")
# print(sum_digits(num))


def pairwise_digits(a, b):
    output = ""
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
    
        

# num_one = input("Please enter a number : ")
# num_two = input("Please enter another number : ")
# print(pairwise_digits(num_one, num_two))
    
def to_base10(binary):
    total = 0
    for counter in range(0, len(binary)):
        if binary[counter] == "1":
            total = total + 2**(len(binary) - (counter + 1))
    return(total)

num_one = input("Please enter a number : ")
num_two = input("Please enter another number : ")
print(to_base10(num_one))

def bin_pyramid(row_num):
    for counter in range(1, (row_num +1)):
        bin_row(counter)
        
def bin_row(length):
    row_str = ""
    for x in range(0, (length)):
        if (length - x) % 2 == 0:
            row_str = row_str + "0"
        else:
            row_str = row_str + "1"
    print(row_str)
    
# rows = int(input("please enter the number of rows : "))
# bin_pyramid(rows)

def sum_lists(data):
    output =[]
    total = 0
    for row in data:   
        for val in row:
            total += val
        output.append(total)
        total = 0
    print(output)

# list = [[],[],[],[]]
# sum_lists(list)
