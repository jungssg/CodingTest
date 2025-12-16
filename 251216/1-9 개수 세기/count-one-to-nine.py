num=int(input())
numbers = list(map(int, input().split()))

arr = [0] * 10

for n in numbers:
    arr[n] += 1

for i in range(1,10):
    print(arr[i])
