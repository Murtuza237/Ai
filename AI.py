# Fibonacci Sequence using Recursion 
def Fibonacci_Sequence(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return Fibonacci_Sequence(n-1)+Fibonacci_Sequence(n-2)
#Input Validation
while True:
    try:
        n=int(input("Fibonacci Sequence up to:"))
        if n>=0:
            break
    except ValueError:
        print("Please enter a valid number.")

#Inserting Fibonacci Sequence into a list
fibo=[]
for i in range(1,n+1):
    fibo.append(Fibonacci_Sequence(i))
print("Fibonacci Sequence of", n, "is:")
for i in range(1,n+1):
    print(Fibonacci_Sequence(i), end=" ")
