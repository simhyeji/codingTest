import sys
n = int(sys.stdin.readline().rstrip())
test = []
for _ in range(n):
    f ,s = sys.stdin.readline().rstrip().split()
    test.append([list(f.rjust(5, '-')),list(s.rjust(5,'-'))])

right = {'-':[0,0,0,0,0,0,0],'0': [1,1,1,0,1,1,1], '1':[0,0,1,0,0,1,0], '2': [1,0,1,1,1,0,1], '3': [1,0,1,1,0,1,1],'4':[0,1,1,1,0,1,0],'5':[1,1,0,1,0,1,1],'6':[1,1,0,1,1,1,1],'7':[1,1,1,0,0,1,0],'8':[1,1,1,1,1,1,1],'9':[1,1,1,1,0,1,1]}

for first, second in test:
    f_right = []
    for f in first:
        f_right.append(right[f])
    s_right = []
    for s in second:
        s_right.append(right[s])
    count = 0
    for i in range(5):
        for j in range(7):
            if f_right[i][j] != s_right[i][j]:
                count += 1
    print(count) 