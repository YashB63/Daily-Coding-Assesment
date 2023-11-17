def message(msg):
    longest_length = 0
    longest_msg = ""
    
    curr_length = 0
    curr_msg = ""
    
    for char in msg:
        if curr_msg == "" or char == curr_msg[0]:
            curr_length += 1
            curr_msg += char
        else:
            if curr_length > longest_length:
                longest_length = curr_length
                longest_msg = curr_msg
                
            curr_length = 1
            curr_msg = char
            
    if curr_length > longest_length:
        longest_length = curr_length
        longest_msg = curr_msg
        
    return longest_length, longest_msg
    
input_msg = input()
length, lm = message(input_msg)
print(length)
print(lm)