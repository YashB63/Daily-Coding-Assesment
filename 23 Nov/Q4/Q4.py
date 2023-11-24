def numberofcarries(num1, num2):
    carry = 0
    total_carry = 0

    while num1 > 0 or num2 > 0:
        dig1 = num1 % 10
        dig2 = num2 % 10

        total = dig1 + dig2 + carry

        if total >= 10:
            carry = 1
            total_carry += 1
        else:
            carry = 0

        num1 //= 10
        num2 //= 10

    return total_carry

num1 = int(input())
num2 = int(input())

output = numberofcarries(num1, num2)
print(output)
