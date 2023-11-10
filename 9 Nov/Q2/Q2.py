def calc_hcf(arr):
    def calc_gcd(a,b):
        while b:
            a,b = b, a%b
        return a
    
    def calc_hcf_of_arr(arr):
        output = arr[0]
        for num in arr[1:]:
            output = calc_gcd(output, num)
        return output
    return calc_hcf_of_arr(arr)
    
try:
    x = (int(input()))
    y = [int(z) for z in input().split()]
    
    output = calc_hcf(y)
    print(output)
except ValueError:
    print("")