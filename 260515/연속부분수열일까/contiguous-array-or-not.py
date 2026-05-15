# A의 원소들을 B의 원소 개수만큼 앞에서부터 슬라이싱
# a_len-b_len+1 만큼 반복
a_len, b_len = map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

answer=0
for i in range(0, a_len-b_len+1):
    if A[i: i+b_len] == B:
        answer = 1
        break;

if answer == 1:
    print('Yes')
else:
    print('No')