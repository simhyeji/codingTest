import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
block_map = []
block_list= []
visited=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    block_map.append(list(input().rstrip()))

# print(visited)
# print(block_map)

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def bfs(arr,cx,cy,visited,n):
    q = deque()
    q.append([cx,cy])
    visited[cx][cy]=True
    cnt = 1
    while q:
        x, y= q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # print(nx, ny)
            if nx>=0 and ny>=0 and nx<n and ny<n and arr[nx][ny]=='1':
                if not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                    cnt +=1
                    # print(q)
    return cnt

for i in range(n):
    for j in range(n):
        if block_map[i][j]=='1' and visited[i][j]==0:
            block_cnt = bfs(block_map,i,j,visited,n)
            #print("block_cnt:",block_cnt)
            block_list.append(block_cnt)
# print(block_list)
block_list.sort()
print(len(block_list))
for i in range(len(block_list)):
    print(block_list[i])