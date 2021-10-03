def solution(num):
    answer = 0
    num = str(num)
    for i in range(len(num)):
        answer += int(num[i])

    return answer

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
