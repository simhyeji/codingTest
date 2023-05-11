def solution(k, dungeons):
    answer = -1
    count_li = []
    for idx, dun in enumerate(dungeons):
        ck = k
        count = 0
        if ck >= dun[0]:
            ck = ck-dun[1]
            if ck >= 0:
                count += 1
        for j, i in enumerate(dungeons):
            if j != idx:
                if ck >= i[0]:
                    ck = ck-i[1]
                    if ck >= 0:
                        count += 1
        count_li.append(count)
    print(count_li)
                    
            
        
    return answer