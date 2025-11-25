score = list(map(float, input().split()))

SUM = sum(score)
AVG = SUM / len(score)

print(f'{AVG:.1f}')