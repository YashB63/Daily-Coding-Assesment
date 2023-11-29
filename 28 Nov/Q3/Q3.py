def check_palindrome(word):
    return word == word[::-1]
    
def count_palindrome(s):
    words = s.split()
    count = 0
    
    for word in words:
        if check_palindrome(word):
            count += 1
    
    return count
    
s = input()

output = count_palindrome(s)
print(output)