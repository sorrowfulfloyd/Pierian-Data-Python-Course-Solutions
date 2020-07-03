# WARMUPS

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser(a=0,b=0):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def crackers(text):
    wordlist = text.split()
    return wordlist[0][0].lower() == wordlist[1][0].lower()

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes(a,b):
    return a+b==20 or a==20 or b==20

# LEVEL 1 PROBLEMS

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def capp(st):
    return st[0].upper() + st[1:3] + st[3].upper() + st[4:] # or could use .capitilize() lul

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def masta(xd):
    return ' '.join(xd.split()[::-1])

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost(n):
    return ((abs(100-n) <= 10) or (abs(200-n) <= 10))

#LVL2 TOO HARD OMEGALUL BUT IMMA TRY IT

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters

def paper_doll(st):
    result = ''
    for i in st:
        result += i *3
    return result

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    result = ''
    if sum((a,b,c)) >= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) > 21:
        if a == 11 or b == 11 or c == 11:
            result = sum((a,b,c)) - 10
            if result > 21:
                return print('BUST')

blackjack(1,43,32)

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(x):

    db = [0,0,7,'x']

    for num in x:
        if num == db[0]:
            db.remove(num)
    return len(db) == 1