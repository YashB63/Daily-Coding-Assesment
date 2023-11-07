import math

def find_lcm(x,y):
    return x*y // math.gcd(x,y)
    
arr_length = int(input())
arr = list(map(int, input().split()))

big_lcm = find_lcm(arr[0], arr[1])

for i in range(1, arr_length - 1):
    lcm = find_lcm(arr[i], arr[i+1])
    big_lcm = max(big_lcm, lcm)

print(big_lcm)