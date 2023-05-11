n = int(input())
students = []  # 0: 이름, 1:국어 , 2:영어, 3:수학
for _ in range(n):
    students.append(list(input().split()))
#1. 국어점수 감소 순으로 정렬
#li_1 = sorted(students, key=lambda x: x[1], reverse=True)
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if students[min_index][1] > students[j][1]:
            min_index = j
        elif students[min_index][1] == students[j][1]:
            if 




