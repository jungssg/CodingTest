n = int(input())

arr = [1,n]

for i in range(2,101):
    if (arr[i-2]+arr[i-1]) >= 100:
        arr.append(arr[i-2]+arr[i-1])
        break
    else:
        arr.append(arr[i-2]+arr[i-1])

for elem in arr:
    print(elem, end=' ')
