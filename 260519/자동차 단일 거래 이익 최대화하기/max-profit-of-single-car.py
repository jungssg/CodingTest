n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
# 최대이익 초기값
answer = [0]

for i in range(n):
    for j in range(i+1,n):
        answer.append(price[j]-price[i])
print(max(answer))