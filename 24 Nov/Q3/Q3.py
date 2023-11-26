def Calculate(m, n):
    total = 0
    
    for num in range(m, n+1):
        if num%3 == 0 and num%5 == 0:
            total += num
    
    return total

try:
    test = input()
    
    if ' ' in test:
        value = test.split()
        m = int(value[0])
        n = int(value[1])
        
    else:
        m = int(test)
        n = int(input())

    output = Calculate(m,n)
    print(output)
    
except ValueError:
    pass
