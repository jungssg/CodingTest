p1, p2 = map(int,input().split())

arr = [p1, p2]

for i in range(3, 11):
    n = (arr[-1]+arr[-2])%10
    arr.append(n)

for num in arr:
    print(num, end=' ')