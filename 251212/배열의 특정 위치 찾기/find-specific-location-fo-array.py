arr = list(map(int, input().split()))

num1 = sum(arr[1::2])
num2 = sum(arr[2::3])/len(arr[2::3])

print(num1, num2)