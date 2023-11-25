def FindNumbersDivisible(a, b, divi):
    count = 0
    for n in range(a, b + 1):
        if n % divi == 0:
            count += 1
    return count

a = int(input())
b = int(input())
divi = int(input())


output = FindNumbersDivisible(a, b, divi)
print(output)
