import sys
input = sys.stdin.readline

n,m = map(int, input().split())

room_list = {}

for _ in range(n):
    room = input().rstrip()
    room_list[room] = [0]*(9)

for _  in range(m):
    room, start, end = input().split()
    start, end = int(start)-9, int(end)-9
    for i in range((end - start)):
        room_list[room][start+i]=1
    print(room_list)