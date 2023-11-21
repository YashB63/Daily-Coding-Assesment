def string_within_string(x, y):
    if y in x:
        return "yes"
    else:
        return "no"

x = input()
y = input()
output = string_within_string(x, y)
print(output)
