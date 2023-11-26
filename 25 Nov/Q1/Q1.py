def replaceCharacter(s, ch1, ch2):
    if s is None:
        return None

    if ch1 not in s and ch2 not in s or ch1 == ch2:
        return s

    mod_str = s.replace(ch1, '#').replace(ch2, ch1).replace('#', ch2)

    return mod_str

s = input()
ch1, ch2 = input().split()

output = replaceCharacter(s, ch1, ch2)
print(output)
