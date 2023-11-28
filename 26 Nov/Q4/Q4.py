def reverse_wordwise(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    
    return reversed_string
    
s = input()

output = reverse_wordwise(s)
print(output)