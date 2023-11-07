def pre_sorted(arr):
    sorted_arr = sorted(arr)
    count = 0
    for i in range(len(arr)):
        if arr[i] == sorted_arr[i]:
            count += 1
    return count
    
array_length = int(input())
arr = []

for i in range(array_length):
    x = int(input())
    arr.append(x)
    
output = pre_sorted(arr)
print(output)