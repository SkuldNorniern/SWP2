# 백연선-20191604
from collections import Counter

def solution(lst):
    cnt = Counter(lst).most_common()
    answer = []
    for i in cnt:
        if i[1] == cnt[0][1] & cnt[0][1] != 1:
            answer.append(i[0])
        else:
            break
    answer.sort()
    return answer

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]