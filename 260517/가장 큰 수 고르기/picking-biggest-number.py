nums = list(map(int, input().split(' ')))

max = 1

for num in nums:
    if num > max:
        max = num
print(max)