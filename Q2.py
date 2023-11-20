def david(n):
    mod = 1000000007
    
    if n <= 3:
        return sum(range(1, n+1)) % mod
        
    x = [0] * (n+1)
    x[1], x[2], x[3] = 1, 2, 3
        
    for i in range(4, n+1):
            x[i] = (x[i-1] + x[i-2] + x[i-3]) % mod
        
    return x[n]
        
n = int(input())
output = david(n)
print(output)