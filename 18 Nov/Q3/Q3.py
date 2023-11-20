def zombies(x,y):
    while y:
        x, y = y, x%y
    return x == 1
    
def city(a,b):
    for i in range(b - 1):
        if zombies(a[i], a[i+1]) and a[i] > a[i+1]:
            return i
            
a = list(map(int, input().split()))
b = int(input())

output = city(a,b)
print(output)