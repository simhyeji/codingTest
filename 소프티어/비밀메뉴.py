import sys
m , n , k = map(int, sys.stdin.readline().rstrip().split())
secret = sys.stdin.readline().rstrip()
user = sys.stdin.readline().rstrip()

if secret in user:
    print('secret')
else:
    print('normal')