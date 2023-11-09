def divisibilitybyeleven(x):
    x_str = str(x)
    count = 0
    n = len(x_str)
    
    for i in range(n):
        curr = ''
        for j in range(i,n):
            curr += x_str[j]
            if int(curr)%11 == 0:
                count += 1
    return count
    
x = int(input())
output = divisibilitybyeleven(x)
print(output)