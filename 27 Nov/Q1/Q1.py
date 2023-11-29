from collections import Counter

x = int(input())
element = list(map(int, input().split()))

freq = Counter(element)

sorted_element = sorted(element, key=lambda x: (-freq[x], element.index(x)))

print(*sorted_element)