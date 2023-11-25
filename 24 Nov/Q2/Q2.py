def OperationChoices(c, a, b):
    if c == 1:
        return a + b
    elif c == 2:
        return a - b
    elif c == 3:
        return a * b
    elif c == 4:
        return a // b  

test = input()
c, a, b = map(int, test.split())

output = OperationChoices(c, a, b)
print(output)
