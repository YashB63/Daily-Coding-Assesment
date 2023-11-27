def MinNumberOfNotes(n):
    if n == 0:
        return 0
    
    notes = [100, 50, 20, 10, 5, 2, 1] 
    
    count = 0
    i = 0
    
    while n>0 and i<len(notes):
        if n >= notes[i]:
            count += n//notes[i]
            n %= notes[i]
        i += 1
    
    return count

n = int(input())

output = MinNumberOfNotes(n)
print(output)
