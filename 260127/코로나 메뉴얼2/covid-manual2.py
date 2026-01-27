a = input().split()
b = input().split()
c = input().split()

arr = [a,b,c]

#A,B,C,D
check_list=[0]*4

for x in arr:
    if x[0] == 'Y':
        if int(x[1]) >= 37:
            check_list[0] += 1
        else:
            check_list[2] += 1
    else:
        if int(x[1]) >= 37:
            check_list[1] += 1
        else:
            check_list[3] += 1

if check_list[0] >= 2:
    check_list.append('E')

for y in check_list:
    print(y, end=' ')

