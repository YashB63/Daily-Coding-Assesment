def findnumberofsuperiorelements(arr, n):
    count = 1
    max_right = arr[-1]
    
    for i in range(n - 2, -1, -1):
        if arr[i] > max_right:
            count += 1
            max_right = arr[i]
            
    return count
    
n = int(input())
arr = list(map(int, input().split()))

output = findnumberofsuperiorelements(arr, n)
print(output)