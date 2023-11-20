def cutAdd(word, m, n):
    def rotate(s, count):
        return s[-count:] + s[:-count]
    
    turns = 0
    curr = word
    
    while True:
        curr = rotate(curr,m)
        turns += 1
        
        if curr == word:
            break
        
        curr = rotate(curr,n)
        turns += 1
        
        if curr == word:
            break
        
    return turns
    
word = input()
m = int(input())
n = int(input())

output = cutAdd(word, m, n)
print(output)