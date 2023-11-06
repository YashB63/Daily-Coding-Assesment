def check_fibonacci(x):
    if x<0:
        return False
    a, b = 0, 1
    while b < x:
        a, b = b, a+ b
    return b == x
    
n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
    
count_occurences = sum(1 for x in arr if check_fibonacci(x))
print(count_occurences)