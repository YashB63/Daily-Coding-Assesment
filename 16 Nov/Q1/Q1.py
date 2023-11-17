def mars_stone(m,n, earth_stone):
    earth_stone_set = set(earth_stone)
    mu = 0
    
    for i in range(1,m+1):
        if i not in earth_stone_set:
            mu += 1
    return min(mu, m)
    
m = int(input())
n = int(input())
earth_stone = list(map(int, input().split()))
output = mars_stone(m,n,earth_stone)
print(output)