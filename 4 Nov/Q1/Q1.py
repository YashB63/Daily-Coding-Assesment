x = input()

words = x.split(' ')
sentence = []
for word in words:
    sentence.insert(0, word)
    
print(" ".join(sentence))