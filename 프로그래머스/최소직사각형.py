def solution(sizes):
    sort_li = []
    for size in sizes:
        if size[0] >= size[1]:
            sort_li.append(size)
        else:
            sort_li.append([size[1], size[0]])
    first = sort_li[0][0]
    second = sort_li[0][1]
    for s in sort_li:
        if s[0] > first:
            first = s[0]
        if s[1] > second:
            second = s[1]
    answer = first * second      
        
    return answer