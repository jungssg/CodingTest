n = int(input())
nums = list(map(int, input().split()))

# 차이 초기값 설정
min_val = 100

# 정수는 오름차순으로 정렬되어 있기 때문에 뒤에 수가 무조건 더큼
for i in range(1,n):
    val = nums[i] - nums[i-1]
    if val < min_val :
        min_val = val
print(min_val)        