

def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        print("s1",sorted(s1))
        print("s1",sorted(s2))
        print("The number is anagram")
    else:
        print("The given number is not a anagram")

list1 = "madam"
list2 = "mdam"
anagram(list1,list2)