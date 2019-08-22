def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
noOfTerms = int(input("Enter the number of Fibonacci numbers to generate: "))
fibo_list=[]
if noOfTerms<=0:
    print("Please enter number greater than 0")
else:
    print("Fibonacci sequence: ")  
    for i in range(noOfTerms):
       fibo_list.append(fibo(i)) 
print(fibo_list) 
