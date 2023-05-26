import sys
from itertools import permutations
n , m , k = map(int, sys.stdin.readline().rstrip().split())  #레일개수, 바구니 무게, 시행횟수
lail = list(map(int, sys.stdin.readline().rstrip().split()))
cases = list(permutations(lail,n))

result = []
for case in cases:
    weight = []
    w = 0
    while len(weight) < k:
        for i in range(n):
            if w + case[i] <= m:
                w += case[i]
            else:
                weight.append(w)
                w = 0
                w += case[i]
    result.append(sum(weight[:k]))
print(min(result))