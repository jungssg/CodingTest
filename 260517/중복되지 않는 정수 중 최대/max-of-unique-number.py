n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max_val = -1


for num in nums:
    cnt = nums.count(num)
    if cnt == 1 :
        if num > max_val :
            max_val = num
print(max_val)