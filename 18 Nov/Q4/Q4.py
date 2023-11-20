def wedding(x, y, z):
    count = 0
    i = 0
    
    while i < z:
        n = 0
        j = i
        while j < z:
            n = n * 10 + int(x[j])
            if n > y:
                break
            count += 1
            j += 1
        i += 1
    return count
    
x = input()
y = int(input())
z = int(input())

output = wedding(x,y,z)
print(output)