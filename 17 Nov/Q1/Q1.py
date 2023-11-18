def rev_bits(x):
    result = 0
    for i in range(32):
        result <<= 1
        result |= x & 1
        x >>= 1
        
    if result >= 2**31:
        result -= 2**32
    return result
    
x = int(input())

output = rev_bits(x)

print(output)