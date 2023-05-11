import sys
data = sys.stdin.readline().strip()
num = int(data)
point = 2
line = 1
for i in range(num):
    point += line
    line *= 2

print(point*point)

# 변의개수 = 2 4 6
# 한변에 점 개수 = 3 5 9
# 2 + 1, 3+2, 5+4 
# 현재 점의 개수 + 이전 변의 개수