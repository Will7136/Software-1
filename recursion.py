def is_power(b, a):
    try:
        isPowerBool = False
        if b/a == 1:
            return True
        elif b == 1 :
            return True
        elif b%a == 0:
            isPowerBool = is_power((b/a), a)
            return isPowerBool
        else :
            return False
    except ZeroDivisionError:
        if b ==0 :
            return True
        else:
            return False
    except:
        return False
    
def rec_sum(list):
    sum = 0
    if len(list) == 0:
        return(0)
    else:
        currentVal = list.pop(0)
        sum = rec_sum(list)
        return(sum + currentVal)
    
def sum_digits(num):
    if num == 0:
        return (0)
    sum = 0
    counter = 1
    digit = num % (10 ** counter)
    newNum = num - digit
    digitCoefficient = digit // (10 ** counter)
    sum = sum_digits(newNum)
        
    return
