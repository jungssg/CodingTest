n = int(input())
nums = list(map(int, input().split()))

min_val = 100

for i in range(n):
    for j in range(i+1, n):
        # 정수는 오름차순으로 정렬되어 있기 때문에 뒤에 수가 무조건 더큼
        val = nums[j] - nums[i]
        if val > 0 and val < min_val:
            min_val = val
print(min_val)        