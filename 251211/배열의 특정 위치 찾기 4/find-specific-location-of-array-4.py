arr = list(map(int,input().split()))
arr2 = []

for x in arr:
    if x != 0:
        if x % 2 == 0:
            arr2.append(x)

print(len(arr2), sum(arr2))