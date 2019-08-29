def printType1(str):
    word_list = str.split()
    rev_list = word_list
    rev_list.reverse()
    return ' '.join(rev_list) 

def printType2(str):
    list = str[::-1].split(' ')
    list.reverse()
    return ' '.join(list)

str = input("Enter string: ")
print("Output 1: ",printType1(str))
print("Output 2: ",printType2(str))

