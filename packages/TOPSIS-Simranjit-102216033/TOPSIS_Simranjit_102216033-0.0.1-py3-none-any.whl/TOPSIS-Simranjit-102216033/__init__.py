def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return (n * factorial(n-1))

# Driver Code
num=int(input("Enter a number: "))

result=factorial(num)
print("The factorial of the given number is: ",result)