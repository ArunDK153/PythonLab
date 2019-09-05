import random
import string

def passwordGen():
    pwd = ""
    count = 0
    length = random.randint(10,16)
    while count!= length:
        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        everything = upper + lower + num + symbol
        pwd+= random.choice(everything)
        count+= 1
        if count == length:
            print(pwd)
            break
passwordGen()
