



def prime(num):
    flage = False
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                flage = True
                break
    if flage:
        print("The given number is not a prime number")
    else:
        print("The given number is prime number")

number = int(input("Enter the number you want to check:"))
Prime_number = prime(number)
