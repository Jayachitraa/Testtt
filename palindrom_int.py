
def palindrome(num):
    original_num = num 
    reverse_num = 0
    while original_num > 0:
        digit = original_num%10
        reverse_num = (reverse_num *10 )+ digit
        original_num =original_num //10
    if reverse_num == num:
        print("The given number is palindrome")
    else:
        print("The given number is not a palindrome")

number = int(input("Enter the Number:"))
obj = palindrome(number)

    