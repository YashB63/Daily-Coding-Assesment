def placement(x,y):
    result = []
    for i in range(x):
        count = 0
        for j in range(i):
            if y[j] > y[i]:
                count += 1
        result.append(count)
    return result

x = int(input())
y = list(map(int, input().split()))

output = placement(x,y)
print(' '.join(map(str, output)))