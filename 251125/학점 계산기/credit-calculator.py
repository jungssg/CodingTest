n = int(input())
score = list(map(float, input().split()))

avg = sum(score) / n

if avg >= 4.0:
    print(round(avg,1))
    print('Perfect')
elif avg >= 3.0:
    print(round(avg,1))
    print('Good')
else:
    print(round(avg,1))
    print('Poor')