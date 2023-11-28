def push_zeros(n, arr):
    count = 0
    
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
            
    while count < n:
        arr[count] = 0
        count += 1
        
    return arr
    
n = int(input())
arr = list(map(int, input().split()))

output = push_zeros(n, arr)
print(' '.join(map(str,output)))