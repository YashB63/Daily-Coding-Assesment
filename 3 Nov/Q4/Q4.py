def FirstNonRepeat(str):
    char_count = {}
    
    for char in str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    for char in str:
        if char_count[char] == 1:
            return char
            
    return '0'
    
output = FirstNonRepeat(input())
print(output)