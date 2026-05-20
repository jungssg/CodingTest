n=2
nums = []
for _ in range(n):
    nums.append(list(map(int,input().split())))


# 가로 평균 출력 => [0][0]/[0][1]/[0][2]/[0][3]
for i in range(2):
    sum1 = 0
    for j in range(4):
        sum1 += nums[i][j]
    print(round(sum1/4,1), end=' ')
print()

# 세로 평균 출력 => [0][0][1][0] / 
for i in range(4):
    sum2 = 0
    for j in range(2):
        sum2 += nums[j][i]
    print(round(sum2/2,1), end= ' ')
print()

# 전체평균
sum3=0
for i in range(2):
    for j in range(4):
        sum3 += nums[i][j]
print(round(sum3/8,1))