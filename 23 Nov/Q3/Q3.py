def dectonbase(n, num):
    if n <= 1 or n > 36:
        return "Invalid base"
    
    notation = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if num == 0:
        return "0"
    
    result = ''
    
    while num > 0:
        remainder = num % n
        result = notation[remainder] + result
        num //= n
    
    return result

n = int(input())
num = int(input())

output = dectonbase(n, num)
print(output)
