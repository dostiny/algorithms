import sys; sys.stdin = open('1221_input.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    K, N = map(str, input().split())
    N = int(N)
    arr = list(map(str, input().split()))
    for i in range(N):
        if arr[i] == 'ZRO':
            arr[i] = 0
        elif arr[i] == 'ONE':
            arr[i] = 1
        elif arr[i] == 'TWO':
            arr[i] = 2
        elif arr[i] == 'THR':
            arr[i] = 3
        elif arr[i] == 'FOR':
            arr[i] = 4
        elif arr[i] == 'FIV':
            arr[i] = 5
        elif arr[i] == 'SIX':
            arr[i] = 6
        elif arr[i] == 'SVN':
            arr[i] = 7
        elif arr[i] == 'EGT':
            arr[i] = 8
        elif arr[i] == 'NIN':
            arr[i] = 9
    for y in range(len(arr), 0, -1):
        for x in range(1, y):
            if arr[x - 1] == arr[x]:
                pass
            elif arr[x - 1] > arr[x]:
                arr[x - 1], arr[x] = arr[x], arr[x - 1]
    for i in range(N):
        if arr[i] == 0:
            arr[i] = 'ZRO'
        elif arr[i] == 1:
            arr[i] = 'ONE'
        elif arr[i] == 2:
            arr[i] = 'TWO'
        elif arr[i] == 3:
            arr[i] = 'THR'
        elif arr[i] == 4:
            arr[i] = 'FOR'
        elif arr[i] == 5:
            arr[i] = 'FIV'
        elif arr[i] == 6:
            arr[i] = 'SIX'
        elif arr[i] == 7:
            arr[i] = 'SVN'
        elif arr[i] == 8:
            arr[i] = 'EGT'
        elif arr[i] == 9:
            arr[i] = 'NIN'
    print(K)
    print(*arr)