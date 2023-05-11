def check(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
        
def solution(numbers):
    answer = 0
    num_li = list(numbers)
    for idx, n in enumerate(num_li):
        if n == 0:
            continue   
        else:
            if check(int(n))==True:
                answer += 1
            for j in range(len(num_li)):
                if j == idx:
                    continue
                else:
                    if check(int(n+num_li[j]))==True:
                        answer += 1        
    return answer

print(solution('011'))