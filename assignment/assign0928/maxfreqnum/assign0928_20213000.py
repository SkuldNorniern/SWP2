def solution(lst):
    answer = []
    dic = {}
    max = 0
    for i in lst:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for key, value in dic.items():
        if max < value:
            max = value

    for key, value in dic.items():
        if max == value:
            answer.append(key)

    if len(answer) == len(lst):
        answer = []
        
    return answer


print(solution([1, 2, 3, 4, 5, 5]))  # [5]
print(solution([12, 17, 19, 17, 23]))  # [17]
print(solution([26, 37, 26, 37, 91]))  # [26, 37]
print(solution([28, 30, 32, 34, 144]))  # []