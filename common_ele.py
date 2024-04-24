

def common_element(listt1,listt2):
    emp_list = []
    for num in listt1:
        if num in list2:
            emp_list.append(num)
    return emp_list
list1 = [2,4,6,8,0,1]
list2 = [3,4,8,6,2,8]

obj = common_element(list1,list2)
print("Here is the commom Elements between two list:",obj)

