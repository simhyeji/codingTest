#일일이 append 해서 런타임 에러 뜸

# import sys
# n , m = map(int, sys.stdin.readline().rstrip().split())
# origin = []
# for _ in range(n):
#     a,b = map(int, sys.stdin.readline().rstrip().split())
#     origin.append([a,b])
# test= []
# for _ in range(m):
#     a,b = map(int, sys.stdin.readline().rstrip().split())
#     test.append([a,b])

# origin_v = []
# test_v = []
# divers = []
# for o in origin:
#     for _ in range(o[0]):
#         origin_v.append(o[1])

# for t in test:
#     for _ in range(t[0]):
#         test_v.append(t[1])

# for i in range(100):
#     if test_v[i] > origin_v[i]:
#         divers.append(test_v[i] - origin_v[i])

# print(max(divers))

#-------------다시 재풀이해서 정답 코드-------------
import sys
n , m = map(int, sys.stdin.readline().rstrip().split())
origin = []
for i in range(n):
    if i == 0:
        a,b = map(int, sys.stdin.readline().rstrip().split())
        origin.append([a,b])
    else:
        a,b = map(int, sys.stdin.readline().rstrip().split())
        origin.append([origin[i-1][0]+a,b])

test= []
for i in range(m):
    if i == 0:
        a,b = map(int, sys.stdin.readline().rstrip().split())
        test.append([a,b])
    else:
        a,b = map(int, sys.stdin.readline().rstrip().split())
        test.append([test[i-1][0]+a,b])

diverse = [0]
i = 0
j = 0
while i < n and j < m:
    if origin[i][0] < test[j][0]:
        div = test[j][1] - origin[i][1] 
        if div > 0:
            diverse.append(div)
        i += 1
    elif origin[i][0] == test[j][0]:
        div = test[j][1] - origin[i][1] 
        if div > 0:
            diverse.append(div)
        i += 1
        j += 1
    else:
        div = test[j][1] - origin[i][1] 
        if div > 0:
            diverse.append(div)
        j += 1

print(max(diverse))
