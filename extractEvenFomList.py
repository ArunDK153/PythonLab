list_num = list(map(int, input("Enter list elements separated by space: ").split()))
even_list = [num for num in list_num if num%2==0]
print("Even List: ", even_list)
