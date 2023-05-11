import sys
w , n = map(int, sys.stdin.readline().rstrip().split())
gold = []
for _ in range(n):
    m, c = map(int, sys.stdin.readline().rstrip().split())
    gold.append([m,c])

sort_g = sorted(gold, key= lambda x:x[1], reverse= True)

price = 0

for m , p in sort_g:
    if w >=m:
        price += m*p
        w -= m
    else:
        price += w*p
        break
print(price)