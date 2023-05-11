#-------런타임 에러 (변수들의 값이 다 너무 큼)
import sys
k, p, n = map(int, sys.stdin.readline().strip().split())

print(k*(p**n)%1000000007)

#-------k,p만 수정 -> 아직 런타임 에러
import sys
k, p, n = map(int, sys.stdin.readline().strip().split())
kr = k % 1000000007
pr = p % 1000000007

#answer = k*(p**n)
print((kr*(pr**n))%1000000007)