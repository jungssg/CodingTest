arr = list(map(int, input().split()))

arr2 = []

for num in arr:
    if num != 0:
        arr2.append(num)
    else:
        rev_arr = arr2[::-1]
        print(sum(rev_arr[0:3]))
        break
