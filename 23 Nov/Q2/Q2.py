def largesmallsum(arr):
    length = len(arr)
    
    if length == 0 or length <= 3:
        return 0
    
    even = [arr[i] for i in range(1, length) if i % 2 == 0]
    odd = [arr[i] for i in range(1, length) if i % 2 != 0]
    
    even.sort()
    odd.sort()
    
    second_even = even[-2] if len(even) >= 2 else 0
    second_odd = odd[1] if len(odd) >= 2 else 0
    
    return second_even + second_odd

length = int(input())
arr = list(map(int, input().split()))

output = largesmallsum(arr)
print(output)
