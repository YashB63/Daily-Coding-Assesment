def divisibility_by_product(arr, arr_length):
    count = 0
    for i in range(arr_length):
        sum_of_digits = 0
        prod_of_digits = 1
        
        if sum_of_digits == 0:
            continue
        
        while arr[i] > 0:
            digit = arr[i]%10
            sum_of_digits += digit
            prod_of_digits *= digit
            arr[i] //= 10
            
        if arr[i] % sum_of_digits == 0 or arr[i] % prod_of_digits == 0:
            count += 1
    return count
    
    
arr_length = int(input())
arr = []
for i in range(arr_length):
    arr.append(int(input("".format(i+1))))
count = divisibility_by_product(arr, arr_length)
print(count)