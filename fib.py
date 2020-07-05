def fib(n):
    if n==0:
        return 0
    elif n==1:  
        return 1
    else:
        return (fib(n-2) + fib(n-1))

num = input("Enter a +ve number for Fibonacci Series terms- ")
print("Fibonacci series for " + num + " terms is- ")
n = int(num)
for n in range(0,n):
    print(fib(n))
print("\n")
