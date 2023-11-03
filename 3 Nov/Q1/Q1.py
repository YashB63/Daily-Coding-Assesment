def count_unique_author(s):
    author_count = {}
    
    for char in s:
        if char.isalpha():
            if char in author_count:
                author_count[char] += 1
            else:
                author_count[char] = 1
                
    unique_count = 0
    for author, count in author_count.items():
        if count == 1:
            unique_count += 1
            
    return unique_count
    
x = input()
y = count_unique_author(x)
print(y)