
# 5! = 5 *4*3*2* 1 == 120


def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact * i 
    return fact
number = int(input("Enter the number:"))
factt = factorial(number)
print("factt",factt)

