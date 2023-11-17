def coding_marathon(x,y,z):
    sorted_z = sorted(z, reverse=True)
    w = sum(sorted_z[:y])
    return w
    
x = int(input())
y = int(input())
z = list(map(int, input().split()))

output = coding_marathon(x,y,z)
print(output)