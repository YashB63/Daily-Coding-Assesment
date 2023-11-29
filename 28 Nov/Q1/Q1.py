def long_palindrome(s):
    
    n = len(s)
    max_length = 0
    start = 0
    
    for i in range(n):
        left = i
        right = i
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1
            
        left = i
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1
    
    return max_length
    
def short_palindrome(s):
    return 1 if len(s) > 0 else 0

def calculate_difference(s):
    longest = long_palindrome(s)
    shortest = short_palindrome(s)
    return longest - shortest
    
s = input()
output = calculate_difference(s)
print(output)