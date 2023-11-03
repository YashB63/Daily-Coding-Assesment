def last_block(n):
    remaining_blocks = list(range(1, n+1))
    is_odd = True
    
    while len(remaining_blocks) > 1:
        if is_odd:
            remaining_blocks = remaining_blocks[1::2]
        else:
            remianing_blocks = remaining_blocks[-2::-2]
        is_odd = not is_odd
        
    return remaining_blocks[0]
    
x = int(input())
output = last_block(x)
print(output)