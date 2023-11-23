import math

def mango_distribution(m, p):
    
    ways = math.comb(m + p - 1, p - 1)
    return ways

m = int(input())
p = int(input())

output = mango_distribution(m, p)
print(output)
