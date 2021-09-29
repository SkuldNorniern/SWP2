# 백연선-20191604
def solution(num):
    # 1
    # answer = 0
    # while num > 0:
    #     answer += num % 10
    #     num //= 10
    # return answer
    #2
    return sum([int(i) for i in str(num)])

print(solution(5923)) #19
print(solution(200)) #2
print(solution(1234567890)) #45
print(solution(2364759387)) #54