def maxindexproduct(arr, n):
    if n == 0 or arr is None:
        return -1
        
    left = [0] * n
    right = [0] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1] + 1
        stack.append(i)
        
    stack.clear()
    
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1] + 1
        stack.append(i)
    
    max_product = 0
    
    for i in range(n):
        max_product = max(max_product, left[i]*right[i])
        
    return max_product
    
n = int(input())
arr = list(map(int, input().split()))

output = maxindexproduct(arr, n)

print(output)