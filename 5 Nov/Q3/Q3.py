def salsa_class(x,y):
    count = 0
    for i in range(8):
        if x[i] != y[i]:
            count += 1
        
    result = (count/8)*100
    return int(result)
    
x = input()
y = input()

result = salsa_class(x,y)
print(result)