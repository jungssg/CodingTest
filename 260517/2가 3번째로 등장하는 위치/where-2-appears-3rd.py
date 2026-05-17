n = input()
nums = list(map(int, input().split()))

cnt = 0
idx = -1
for i, num in enumerate(nums):
    if num == 2:
        cnt += 1
        idx = i
    if cnt == 3:
        print(idx+1)
        break;