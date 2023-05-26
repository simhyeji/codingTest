# 7
# 15 11 4 8 5 2 4

n = int(input())
power = list(map(int, input().split()))
dp =[]
count = 0

for i, p in enumerate(power):
    if len(dp) == 0:
        dp.append(p)
    else:
        if dp[-1] >= p:
            dp.append(p)
        else:
            r_count = 0 #현재 수 보다 작은 값들
            for j in power[i+1:]:
                if j < p:
                    r_count += 1
            p_count = 0 #이전 수 보다 작은 값들
            for j in power[i:]:
                if j < dp[-1]:
                    p_count += 1
            if r_count >= p_count:
                dp.pop()
                dp.append(p)
                count += 1

print(count)
