def arrangement(n, arr):
    arr.sort() 
    even = sorted([x for x in arr if x % 2 == 0]) 
    odd = sorted([x for x in arr if x % 2 != 0])  

    result = []
    even_idx = 0
    odd_idx = 0
    try:
        if arr[0] % 2 == 0:
            while even_idx < len(even) and odd_idx < len(odd):
                result.append(even[even_idx])
                even_idx += 1
                result.append(odd[odd_idx])
                odd_idx += 1
        else:
            while even_idx < len(even) and odd_idx < len(odd):
                result.append(odd[odd_idx])
                odd_idx += 1
                result.append(even[even_idx])
                even_idx += 1

        while even_idx < len(even):
            result.append(even[even_idx])
            even_idx += 1
        while odd_idx < len(odd):
            result.append(odd[odd_idx])
            odd_idx += 1
    except IndexError:
        pass

    return result

n = int(input())
arr = list(map(int, input().split()))

output = arrangement(n, arr)
print(' '.join(map(str, output)))
