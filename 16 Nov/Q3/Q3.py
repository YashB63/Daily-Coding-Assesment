def ben(n, candies):
    max_count = 0
    flavour = {}
    start = 0
    
    for i in range(n):
        if candies[i] in flavour and flavour[candies[i]] >= start:
            start = flavour[candies[i]] + 1
            
        flavour[candies[i]] = i
        max_count = max(max_count, i - start + 1)
        
    return max_count
    
n = int(input())
candies = list(map(int, input().split()))
output = ben(n, candies)
print(output)