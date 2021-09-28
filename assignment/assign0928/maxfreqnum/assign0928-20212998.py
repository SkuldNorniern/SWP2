# 박윤재-20212998
from collections import Counter

def solution(lst):
    c = Counter(lst)
    ans=c.most_common()
    mx = ans[0][1]
    anss = []
    for i in ans:
        if i[1] == mx and mx != 1 :
             anss.append(i[0])
    return anss

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]
