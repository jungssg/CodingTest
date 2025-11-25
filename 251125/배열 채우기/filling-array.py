arr = list(map(int, input().split()))
answer = []

for num in arr:
    if num != 0:
        answer.append(num)
    else:
        break
re_answer = answer[::-1]
for i in range(len(answer)):
    print(re_answer[i], end=' ')