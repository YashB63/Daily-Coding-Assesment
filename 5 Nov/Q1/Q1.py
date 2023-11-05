def decodedmessage(msg):
    if msg == "NULL" or len(msg) == 0:
        return "NULL"
        
    decoded_message = []
    encoded_parts = msg.split()
    
    for part in encoded_parts:
        if part == "#":
            decoded_message.append(encoded_parts[encoded_parts.index(part) + 1])
        else:
            decoded_chars = [chr(int(char) + 64) if char.isdigit() else '_' if char == '_' else char for char in part]
            decoded_message.extend(decoded_chars)
            
    return ' '.join(decoded_message).replace('_', ' ')
    
input_msg = input()
output_msg = decodedmessage(input_msg)
print(output_msg)