# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    gold_li = []
    for i in range(0,n*m,4):
        gold_li.append(a[i:i+m])
    #print(gold_li) [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]
    for j in range(1,m):
        for i in range(n):
            #왼쪽 위에서 오는 것
            if i == 0:
                left_up = 0
            else:
                left_up = gold_li[i][j] + gold_li[i-1][j-1]
            #왼쪽 아래서 오는 것
            if i == n-1:
                left_down = 0
            else:
                left_down = gold_li[i][j] + gold_li[i+1][j-1]
            #왼쪽에서 오는 것
            left = gold_li[i][j] + gold_li[i][j-1]
            gold_li[i][j] = max(left,left_down,left_up)
    result = 0
    for k in range(n):
        result = max(result, gold_li[k][m-1])
    print(result)

    



