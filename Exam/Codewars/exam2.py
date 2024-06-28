# get character from ASCII Value
def get_char(c):
    return chr(c)


# Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    lists = []
    for i in numbers:
        if i % divisor == 0:
            lists.append(i)
    return lists


#Alternate capitalization
def capitalize(s):
    word = ""
    word2 = ""
    for index,character in enumerate(s):
        if index % 2 == 0:
            word += character.upper()
        else:
            word += character
        if index % 2 != 0:
            word2 += character.upper()
        else:
            word2 += character
    return [word,word2]



#Minimize Sum Of Array (Array Series #1)
def min_sum(arr):
    lists = []
    while len(arr) > 0:
        mins = min(arr)
        maxs = max(arr)
        lists.append(mins * maxs)
        arr.remove(mins)
        arr.remove(maxs)
    return sum(lists)




#Sum consecutives
def sum_consecutives(lst):
    num = None
    lists = []
    for i in lst:
        if num == i:
            lists[-1] += i
        else:
            lists.append(i)
            num = i
    return lists



# Least Common Multiple
import math
def lcm(*args):
    return math.lcm(*args)




#Mean Square Error
def solution(array_a, array_b):
    num = 0
    for i in range(len(array_a)):
        word = (array_b[i] - array_a[i]) ** 2
        num += word
        
    word2 = num / len(array_a)
    return word2






#Human readable duration format

def format_duration(seconds):
    years = seconds // (365 * 24 * 60 * 60)
    days = (seconds % (365 * 24 * 60 * 60)) // (24 * 60 * 60)
    hours = (seconds % (365 * 24 * 60 * 60)) % (24 * 60 * 60) // (60 * 60)
    minutes = ((seconds % (365 * 24 * 60 * 60)) % (24 * 60 * 60) % (60 * 60)) // 60
    seconds = (((seconds % (365 * 24 * 60 * 60)) % (24 * 60 * 60) % (60 * 60))) % 60
    
    my_dict = {
        'years': years,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }
    listn = []

    for key,value in my_dict.items():
        if value == 1:
            listn.append(value)
            listn.append(key[:-1])
        elif value == 0:
            pass
        else:
            listn.append(value)
            listn.append(key)
    
    if listn == []:
        return "now"
    else:
        z = 0
        listm = []
        while z < len(listn):
            listm.append(str(listn[z]) + " " + str(listn[z+1]))
            z += 2
        lstn = ", ".join(listm[:-2]) + ", "
        lstm = " and ".join(listm[-2:])
        if ", " == lstn[0:2]:
            lstn = lstn[2:]
        return lstn + lstm
                         