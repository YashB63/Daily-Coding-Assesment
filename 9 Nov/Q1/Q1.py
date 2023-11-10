def calc_lcm(x,y):
    def calc_gcd(a,b):
        while b:
            a, b = b, a%b
        return a
        
    gcd = calc_gcd(x,y)
    lcm = (x*y)//gcd
    
    return lcm
    
x = int(input())
y = int(input())

output = calc_lcm(x,y)
print(output)