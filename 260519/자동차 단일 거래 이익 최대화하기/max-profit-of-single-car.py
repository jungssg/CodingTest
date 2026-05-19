n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
# 최대이익 초기값
answer = [0]

for i in range(n):
    for j in range(i+1,n):
        # 이익은 파는값 - 산값 => price[j] - price[i]
        profit = price[j] - price[i]
        if profit > 0 :
            answer.append(profit)
print(max(answer))