N, Q = map(int, input().split())

n_list = list(map(int, input().split()))

# 질문 목록
for i in range(Q):
    q_list = list(map(int, input().split()))

    if q_list[0] == 1:
        print(n_list[q_list[1]-1])
    elif q_list[0] == 2:
        if q_list[1] not in n_list:
            print(0)
        else:
            print(n_list.index(q_list[1])+1)
    elif q_list[0] == 3:
        for i in range(q_list[1]-1, q_list[2]):
            print(n_list[i], end=' ')
        print(end= '\n')
