def largest_subarray(n, arr):
    count = {0: -1}  
    max_length = 0
    bal = 0

    for i in range(n):
        if arr[i] == 0:
            bal -= 1
        else:
            bal += 1

        if bal in count:
            max_length = max(max_length, i - count[bal])
        else:
            count[bal] = i

    return max_length

n = int(input())
arr = list(map(int, input().split()))

output = largest_subarray(n, arr)
print(output)
