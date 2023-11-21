import itertools

def perfect(arr, target):
    count = 0
    for r in range(1, len(arr) + 1):
        for sub in itertools.combinations(arr, r):
            if sum(sub) == target:
                count += 1
    return count

length = int(input())
arr = list(map(int, input().split()))
target = int(input())

output = perfect(arr, target)
print(output)

