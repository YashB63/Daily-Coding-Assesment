def escape(x,y,n,h):
    jump = 0
    for ht in h:
        jump_needed = 0
        while ht > 0:
            ht -= x
            jump_needed += 1
            if ht > 0:
                ht += y
        jump += jump_needed
    return jump
    
x = int(input())
y = int(input())
n = int(input())
h = list(map(int, input().split()))

output = escape(x,y,n,h)
print(output)