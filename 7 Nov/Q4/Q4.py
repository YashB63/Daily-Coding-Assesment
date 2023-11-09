def CountDigiOccurences(i,u,x):
    count = 0
    for j in range(i, u+1):
        num_str = str(j)
        for dig in num_str:
            if dig == str(x):
                count += 1
                
    return count
    
i = int(input())
u = int(input())
x = int(input())

output = CountDigiOccurences(i,u,x)
print(output)