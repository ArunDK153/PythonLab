from bisect import bisect_left
def search(numList,searchEle):
    idx=bisect_left(numList,searchEle)
    if idx!= len(numList) and numList[idx] == searchEle: 
        return True 
    else: 
        return False

num_list = list(map(int, input("Enter list of numbers in sorted order: ").split()))
ele = int(input("Enter search element: "))
res = search(num_list,ele)
if res==True:
    print("Element present.")
else:
    print("Element not present.")
