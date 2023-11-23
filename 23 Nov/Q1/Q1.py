def differenceofsum(n, m):
    div_sum = 0
    non_div_sum = 0
    
    for i in range(1, m + 1):
        if i % n == 0:
            div_sum += i
        else:
            non_div_sum += i
    
    return non_div_sum - div_sum

n = int(input())
m = int(input())
output = differenceofsum(n,m)
print(output)