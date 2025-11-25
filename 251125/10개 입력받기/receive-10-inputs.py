arr = list(map(int, input().split()))

cnt = 0

for num in arr:
    if num == 0 :
        break
    cnt += 1

SUM = sum(arr[:cnt])
AVG = SUM / cnt

print(f'{SUM} {AVG:.1f}')
