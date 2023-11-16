def check_anagram(x,y):
    x = x.replace(" ","").lower()
    y = y.replace(" ","").lower()
    
    return "yes" if sorted(x) == sorted(y) else "no"
    
x = input()
y = input()

output = check_anagram(x,y)
print(output)