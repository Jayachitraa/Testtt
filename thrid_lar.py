

def third_larg(numbers):
    first_lar = float("-inf")
    second_lar = float("-inf")
    third_lar = float("-inf")
    
    for num in numbers:
        if num > first_lar:
           third_lar = second_lar
           second_lar = first_lar
           first_lar = num
        elif num > second_lar and num != first_lar:
            third_lar = second_lar
            second_lar =num
        elif num > third_lar and num != first_lar and num != second_lar:
            third_lar = num

    return third_lar

   

list1 = [2,5,6,7,9]
obj = third_larg(list1)
print("obj",obj)
