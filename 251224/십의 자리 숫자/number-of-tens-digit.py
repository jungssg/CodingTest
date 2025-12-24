arr = list(map(int, input().split()))
numbers = [0]*10

for i in range(len(arr)):
    if arr[i] == 0:
        break
    numbers[arr[i]//10] += 1

for i in range(1,10):
    print(i,'-',numbers[i])