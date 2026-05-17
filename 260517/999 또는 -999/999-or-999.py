nums = list(map(int, input().split()))

end_1 = 999
end_2 = -999
idx = 0
for i, num in enumerate(nums):
    if num == end_1 or num == end_2:
       idx = i
       new_nums = nums[:idx]
print(max(new_nums), min(new_nums))