def min_chars(x):
    if x == x[::-1]:
        return "NULL"
    def is_pal(substr):
        return substr == substr[::-1]
    
    for i in range(1, len(x)):
        if is_pal(x[i:]):
            return x[:i][::-1]
    
    return x[:-1][::-1]
    
n = input()
result = min_chars(n)
print(result)