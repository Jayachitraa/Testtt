

def palindrome(word):
    reverse_word = word[::-1]
    return reverse_word == word     

check_word = input("Enter the word:")
if palindrome(check_word):
    print("the given word is palindrome")
else:
    print("the given word is not a palindrome ")








