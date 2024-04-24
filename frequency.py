

def frequncy(numbers):
    frequncy_count = {}
    for num in numbers:
        if num in frequncy_count:
            frequncy_count[num] += 1
        else:
            frequncy_count[num] =1 
    return frequncy_count
listt= [9,5,6,3,3,4,5,6,9]
fre = frequncy(listt)
print("frequncy_count",fre)
     
