arr = list(map(int, input().split()))

numbers = [0]*7

for elem in arr:
    numbers[elem] += 1

for i in range(1,7):
    print(i,'',numbers[i])