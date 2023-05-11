import sys
n , m = map(int, sys.stdin.readline().rstrip().split())
room_li = {}
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    room_li[tmp] = [0]*9
meet_li = []
for _ in range(m):
    r,s,e = sys.stdin.readline().rstrip().split()
    meet_li.append([r,int(s), int(e)])

for meet in meet_li:
    r,s,e = meet[0], meet[1], meet[2]
    for i in range(s-9,e-9):
        room_li[r][i] =1

sort_li =list(room_li.keys())
sort_li.sort()

for s in sort_li:
    start = []
    end = []
    for i, c in enumerate(room_li[s]):
        if c == 0:
            if i == 0:
                start.append(i+9)
            else:
                if room_li[s][i-1] == 0: #이전시간과 연속인지 확인
                    continue
                else:
                    start.append(i+9)
        else:
            if i == 0:
                continue
            else:
                if room_li[s][i-1] == 0:
                    end.append(i+9)
                else:
                    continue
    if len(start) != len(end):
        end.append(18)
    print(f'Room {s}:')
    if len(start) != 0:
        print(f'{len(start)} available:')
        for j in range(len(start)):
            print(f'{start[j]:02d}-{end[j]:02d}')
    else:
        print('Not available')
    if s != sort_li[-1]:
        print('-----')