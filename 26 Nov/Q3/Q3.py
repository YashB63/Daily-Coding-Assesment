def decrypt(s, n):
    decrypted = ''
    i = 0
    
    while i < len(s):
        char = s[i]
        freq = int(s[i + 1])
        decrypted += char*freq
        i += 2
        
    if n <= len(decrypted):
        return decrypted[n - 1]
    else:
        return "-1"

s = input()
n = int(input())

output = decrypt(s, n)
print(output)