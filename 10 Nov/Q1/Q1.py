def longest_common_subsequence(x, y):
    a = len(x)
    b = len(y)
    
    lcs = [[0] * (b+1) for _ in range(a+1)]
    
    for i in range(1, a+1):
        for j in range(1, b+1):
            if x[i-1] == y[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
                
    return lcs[a][b]
    
c = input()
d = input()

output = longest_common_subsequence(c,d)
print(output)