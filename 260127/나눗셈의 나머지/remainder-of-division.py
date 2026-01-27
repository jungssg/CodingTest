a,b = map(int,input().split())
# print(a,b)

cnt = [0] * b

while a > 1 :
    x = a % b
    a = a // b
    cnt[x] += 1

# print(cnt)