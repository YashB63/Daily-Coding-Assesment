def MaxExponents(a, b):
    max_exponent = 0
    result = a

    for i in range(a, b+1):
        exponent = 0
        num = i

        while num % 2 == 0 and num > 1:
            num //= 2
            exponent += 1

        if exponent > max_exponent:
            max_exponent = exponent
            result = i

    return result

test = input()
a, b = map(int, test.split())

output = MaxExponents(a, b)
print(output)
