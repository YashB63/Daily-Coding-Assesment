def adj_xor(x):
    binary_num = bin(x)[2:]
    result = ['1']  
    for i in range(1, len(binary_num)):
        result.append(str(int(binary_num[i-1]) ^ int(binary_num[i])))
    
    result[-1] = str(int(result[-1]) | 0)
        
    result_str = ''.join(result)
    deci_num = int(result_str, 2)
    return deci_num

x = int(input())
print(adj_xor(x))