def find_minimum(n):
    for x in range(1, 10000): 
        if x % n == 0 and sum(map(int, str(x))) == n and x != n:
            return x
    return -1

n = int(input())
output = find_minimum(n)
print(output)
