def SumofSetBitNumbers(x, y):
    sum = 0
    for i in range(1 << x):
        count = 0
        for j in range(x):
            if (i & (1 << j)) != 0:
                count += 1
            
        if count == y:
                sum += i
    return sum
    
x = int(input())
y = int(input())

output = SumofSetBitNumbers(x,y)
print(output)