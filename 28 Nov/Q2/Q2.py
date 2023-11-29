def frequency_count(s):
    freq = {}
    
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    output = ''
    for char in sorted(freq.keys()):
        output += char + str(freq[char])
        
    return output
    
s = input()

output = frequency_count(s)
print(output)