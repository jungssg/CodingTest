# 초기 500 초과 중 가장 작은 수, 500 미만 중 가장 큰 수 설정
nums = list(map(int, input().split()))

pre_min_num = 0
pre_max_num = 1000
for num in nums:
    if num < 500 and num > pre_min_num:
            pre_min_num = num
    if num > 500 and num < pre_max_num:
            pre_max_num = num

print(pre_min_num, pre_max_num)