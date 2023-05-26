import sys
n , k = map(int, sys.stdin.readline().rstrip().split())
score = list(map(int, sys.stdin.readline().rstrip().split()))
cases = []
for i in range(k):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    cases.append([s,e])

for s ,e in cases:
    print('{:.2f}'.format(round(sum(score[s-1:e])/(e-s+1),2)))