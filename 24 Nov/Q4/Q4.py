def check_palindromme(num):
    return str(num) == str(num)[::-1]

def intermediate(low, up):
    for num in range(low+1, up):
        if check_palindromme(num):
            print(num, end=' ')
            
try:
    
    test = input()
    
    if ' ' in test:
        low, up = map(int, test.split())
        intermediate(low, up)
        
    else:
        low = int(test)
        up = int(input())
        intermediate(low, up)
        
except ValueError:
    pass