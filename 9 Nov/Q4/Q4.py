def string_permutation(x,y):
    count_x = {}
    count_y = {}
    
    for char in x:
        count_x[char] = count_x.get(char, 0) + 1
        
    for char in y:
        count_y[char] = count_y.get(char, 0) + 1
        
    return "yes" if count_x == count_y else "no"

try:
    a = input()
    b = input()
    output = string_permutation(a,b)
    print(output)
except ValueError:
    print("")