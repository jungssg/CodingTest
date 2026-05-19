# 최대값 설정 => 가장 왼쪽 인덱스
# 다시 최대값 설정 => 가장 왼쪽 인덱스
n = int(input())
a = list(map(int, input().split()))

# # Please write your code here.
# answer = []
# max_val = max(a)
# max_idx = a.index(max_val)
# answer.append(max_idx + 1)

# for i in range(n):
#     if max_idx == 0:
#         break;
#     else:
#         max_val = max(a[:max_idx])
#         max_idx = a[:max_idx].index(max_val)
#         answer.append(max_idx + 1)

# for num in answer:
    # print(num, end=' ')


prev_max_idx = n
while True:
    max_idx = 0
    for i in range(1, prev_max_idx):
        if a[i] > a[max_idx]:
            max_idx = i
    print(max_idx +1 , end=' ')
    if max_idx == 0:
        break
    prev_max_idx = max_idx
