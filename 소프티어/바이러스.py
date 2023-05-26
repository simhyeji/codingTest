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


#---------지수도 나눠서 각각 나눠줘서 통과 
import sys
k, p, n = map(int, sys.stdin.readline().strip().split())
kr = k % 1000000007
pr = p % 1000000007
npr = (pr ** (n % 1000)) % 1000000007
for i in range(n // 1000):
    npr *= (pr**(1000)) % 1000000007


#answer = k*(p**n)
print((kr*npr)%1000000007)


#---- 나누는 값을 1000이 아닌 10000,100000으로 했을경우 안에 계산하는 수가 너무 커져서 오히려 시간이 더 오래걸림, 1000이 적절