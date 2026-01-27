scores = list(map(int, input().split()))

# 10~100점
arr = [0] * 11

for score in scores:
    if score == 0:
        break
    cnt = score // 10
    arr[cnt] += 1

for i in range(len(arr)-1,0,-1):
    print(f"{i*10} - {arr[i]}")