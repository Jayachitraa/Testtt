

def second_larg(numbers):
    first_lar = float("-inf")
    second_lar = float("-inf")
    for num in numbers:
        if num > first_lar:
           second_lar = first_lar
           first_lar = num
    
    for num in numbers:
        if num > second_lar and num != first_lar:
            second_lar =num

    return second_lar

list1 = [2,5,6,7,9]
obj = second_larg(list1)
print("obj",obj)
