import sys
n = int(sys.stdin.readline().rstrip())
m = []  #지도
for _ in range(n):
    li = list(sys.stdin.readline().rstrip())
    m.append(li)

count = 0
def dfs(x,y):
    while True:
        if x <= -1 or y <= -1 or x >= n or y >= n:
            break
        if m[x][y] == '1':
            m[x][y] = '2'
            global count
            count += 1

            dfs(x,y-1)
            dfs(x,y+1)
            dfs(x+1,y)
            dfs(x-1,y)
            return count
        break
result = []
for i in range(n):
    for j in range(n):
        if m[i][j] == '1':
            count = 0
            result.append(dfs(i,j))
result.sort()
print(len(result))
for r in result:
    print(r)