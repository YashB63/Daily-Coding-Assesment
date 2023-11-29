def secret_message(msg):
    spl_characters = 0
    
    for char in msg:
        if not char.isalnum() and not char.isspace():
            spl_characters += 1
        
    return spl_characters
    
msg = input()

output = secret_message(msg)
print(output)