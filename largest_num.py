
def largest_number(numbers):
    lar_num = numbers[0]
    for num in numbers:
        if num > lar_num:
            lar_num = num
    return lar_num
    
range_of_numbers = int(input("Enter the range:"))
emp_list = []
for rangee in range(range_of_numbers):
    emp_list.append(int(input("Enter the numbers:")))

obj = largest_number(emp_list)
print("The largest number in the given list is:",obj)



        
     


