num = int(input())
cnt = 0
for i in range(1, 11):
    if num % 5 != 0:
        print(num * i, end=' ')
    else:
        cnt += 1
        print(num * i, end=' ')
        if cnt == 2:
            break