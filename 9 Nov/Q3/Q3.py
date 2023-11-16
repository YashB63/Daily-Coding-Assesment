def rotate_arr(x,y,z):
    z = z%x
    rotated_arr = y[z:] + y[:z]
    return rotated_arr
    
try:
    x = int(input())
    y = [int(a) for a in input().split()]
    z = int(input())
    
    output = rotate_arr(x,y,z)
    print(*output)
except ValueError:
    print("")