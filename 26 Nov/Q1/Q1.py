def find_cuckoo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return 1 * find_cuckoo(n-1) + 2*find_cuckoo(n-2) + 3*1
        
n = int(input())

output = find_cuckoo(n)
print(output)