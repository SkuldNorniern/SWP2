# 박재우 - 20212999

def solution(lst):
    answer = []
    dic = {}
    count = 0

    for i in lst:
        count = lst.count(i)
        dic[i] = count
    
    for k,v in dic.items():
        if max(dic.values()) == v:
            answer.append(k)
        elif max(dic.values()) == 1:
            answer = []

    return answer

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]