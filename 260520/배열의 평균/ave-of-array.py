n=2
nums = []
garo = []
sero = []

for _ in range(n):
    nums.append(list(map(int,input().split())))
    
print(round(sum(nums[0])/4, 1), round(sum(nums[1])/4,1))
print(round((nums[0][0]+nums[1][0])/2,1), round((nums[0][1]+nums[1][1])/2,1),round((nums[0][2]+nums[1][2])/2, 1),round((nums[0][3]+nums[1][3])/2,1))
print(round((sum(nums[0])+sum(nums[1]))/8, 1))