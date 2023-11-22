def duplicates(length, arr):
    unique = []
    check = set()
    
    for n in arr:
        if n not in check:
            unique.append(n)
            check.add(n)
    
    return unique

length = int(input())
arr = list(map(int, input().split()))

output = duplicates(length, arr)
print(' '.join(map(str, output)))
