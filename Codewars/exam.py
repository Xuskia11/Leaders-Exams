# Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    cats = 0
    dogs = 0
    if human_years == 1:
        cats = 15
        dogs = 15
    elif human_years == 2:
        cats = 24
        dogs = 24
    else:
        cats = 4 * (human_years - 2) + 24
        dogs = 5 * (human_years - 2) + 24
    return [human_years,cats,dogs]

#Find Nearest square number
def nearest_sq(n):
    number = round(n ** 0.5)
    return number ** 2


#Sum of array singles
def repeats(arr):
    number = 0
    for i in arr:
        if arr.count(i) >= 2:
            arr.remove(i)
    return arr


#Triangular Treasure
def triangular(n):
    if n < 0:
        return 0
    elif n == 0:
        return 0
    return n * (n + 1) // 2





# Playing with digits
def dig_pow(n, p):
    num = 0
    for i in list(str(n)):
        num = num + (int(i) ** p)
        p += 1
    if num % n == 0:
        return int(num / n)
    return -1





#The Hashtag Generator
def generate_hashtag(s):
    s = "#" + s.title()
    s = s.split(" ")
    s = "".join(s)
    if len(s) in range(2,141):
        return s
    else:
        return False




# So Many Permutations!
def permutations(s):
    word = set([s])
    if len(s) == 2:
        word.add(s[1] + s[0])
    elif len(s) > 2:
        for i, x in enumerate(s):
            for v in permutations(s[:i] + s[i + 1:]):
                word.add(x + v)
    
    return list(word)

