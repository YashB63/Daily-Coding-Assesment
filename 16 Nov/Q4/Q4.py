def totalOccurence(ip1, ip2):
    count = 0
    for i in range(ip2 + 1):
        n = i
        
        while n > 0:
            digit = n%10
            if digit == ip1:
                count += 1
            n //= 10
            
    return count
    
ip1 = int(input())
ip2 = int(input())

output = totalOccurence(ip1, ip2)
print(output)