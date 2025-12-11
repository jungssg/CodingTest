stu_num = int(input())

stu_pass = []

for i in range(stu_num):
    scores = list(map(int, input().split()))
    std = sum(scores)/4
    if std >= 60 :
        print('pass')
        stu_pass.append(1)
    else:
        print('fail')

print(len(stu_pass))