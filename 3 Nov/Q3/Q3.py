def CheckPassword(x):
    n=len(x)
    if n<4:
        return 0
    if x[0].isdigit():
        return 0
    capt=0
    num=0
    for i in range(n):
        if x[i] == '' or x[i]=='/':
            return 0
        if x[i]>='A' and x[i]<='Z':
            capt+=1
        elif x[i].isdigit():
            num+=1
    if capt>0 and num>0:
        return 1
    else:
        return 0

x=input()
print(CheckPassword(x))