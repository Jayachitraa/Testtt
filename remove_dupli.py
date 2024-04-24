
def remove_duplicates(numbers):
    unique_nums = []
    for num in numbers:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

list1 = [9,3,5,9,2,1,3,5]
obj = remove_duplicates(list1)
print("remove duplicates:",obj)

