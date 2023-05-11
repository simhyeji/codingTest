def solution(answers):
    answer = []
    solve= [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    count_li = [0]*3
    for i in range(3):
        for idx, a in enumerate(answers):
            if a == solve[i][idx%len(solve[i])]:
                count_li[i]+=1
    for idx, c in enumerate(count_li):
        if c == max(count_li):
            answer.append(idx+1)

    return answer