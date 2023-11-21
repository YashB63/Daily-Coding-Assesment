def minimum_penalty(length, n):
    n.sort()  
    
    x = [0] * length
    
    for i in range(1, length):
        x[i] = x[i - 1] + abs(n[i] - n[i - 1])
    
    return x[length - 1]

length = int(input())
arr = list(map(int, input().split()))

output = minimum_penalty(length, arr)
print(output)