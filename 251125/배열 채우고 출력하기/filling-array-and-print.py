text = list(input().split())

text_rev = text[::-1]

for i in range(10):
    print(text_rev[i], end='')