def amstrong(num):
    original_num = num
    sum = 0
    while original_num > 0:
        digit = original_num % 10
        sum += digit ** 3  # accumulate the sum of cubes of digits
        original_num = original_num // 10
    if num == sum:
        print("The given number is an Armstrong number")
    else:
        print("The given number is not an Armstrong number")

number = int(input("Enter the number: "))
amstrong(number)
