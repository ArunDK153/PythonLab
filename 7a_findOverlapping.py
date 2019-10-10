with open('prime.txt') as f:
    list1 = [[int(x) for x in line.split()] for line in f]
primeList = list1[0]
with open('happy.txt') as f:
    list2 = [[int(x) for x in line.split()] for line in f]    
happyList = list2[0]

def intersection(list1,list2):
    listSet = set(list2)
    list3 = [value for value in list1 if value in listSet]
    return list3
print("Overlapping numbers between prime and happy numbers under 1000: \n")  
print(*intersection(happyList,primeList), sep=", ")
