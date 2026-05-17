n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = a[0]

for num in a[1:]:
    if num < min_val:
        min_val = num
cnt = a.count(min_val)
print(min_val, cnt)