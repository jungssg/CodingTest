inputs = []
for i in range(4):
    inputs.append(list(map(int, input().split())))
    print(sum(inputs[i]))