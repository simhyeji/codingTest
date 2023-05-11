def solution(answers):
    answer = []
    solve= [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count_li = []
    for sol in solve:
        count = 0
        for i in range(1,len(answers)+1):
            j = len(sol) if (i % len(sol) == 0) else i % len(sol)
            if answers[i-1] == sol[j-1]:
                count += 1
        count_li.append(count)
    check = count_li[0]
    answer.append(1)
    for i in range(1,len(count_li)):
        if count_li[i] > check:
            check = count_li[i]
            answer = [i+1]
        elif count_li[i] == check:
            answer.append(i+1)
        else:
            continue    
                
    return answer