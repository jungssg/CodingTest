n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_val1 = max(a)
a.remove(max_val1)
max_val2 = max(a)
print(max_val1, max_val2)