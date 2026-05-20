texts = []
for i in range(5):
    texts.append(input().split())
    for j in range(3):
        texts[i][j]= texts[i][j].upper()
    print(texts[i][0], texts[i][1], texts[i][2])  