def guitar_string(x,y):
    y.sort(reverse=True)
    total_amt = 0
    for z in range(x):
        total_amt += y[z] * (x-z)
    return total_amt

x = int(input())
y = []
for i in range(x):
    y.append(int(input("".format(i+1))))

max_amt = guitar_string(x,y)
print(max_amt)