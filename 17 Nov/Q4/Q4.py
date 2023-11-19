def electrostatics(m, c, n):
    total = 0
    for i in range(n):
        if c[i] == 'P':
            total += m[i]
        elif c[i] == 'N':
            total -= m[i]
    
    max_field = abs(total)*100
    return max_field
    
m = list(map(int, input().split()))
c = input()
n = len(m)

output = electrostatics(m,c,n)
print(output)