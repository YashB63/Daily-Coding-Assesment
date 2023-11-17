def arithmetic_progression(x2,x3,n):
    d = x3-x2
    nth_term = x2 + (n-2)*d
    return nth_term
    
x2 = int(input())
x3 = int(input())
n = int(input())

output = arithmetic_progression(x2,x3,n)
print(output)