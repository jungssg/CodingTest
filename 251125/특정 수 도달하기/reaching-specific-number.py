arr = list(map(int, input().split()))
answer = []

TR = 0

for i in range(10):
    if arr[i] < 250:
        answer.append(arr[i])
    else:
        TR = i
        break

if TR == 10:
    SUM = sum(arr)
    AVG = round(sum(arr) / 10, 1)
else:
    SUM = sum(answer[:TR])
    AVG = round(sum(answer[:TR])/TR,1)
print(SUM, AVG)