# 박재우-20212999

def solution(num):
    # answer = 0
    # while(num!=0):
    #   answer += num%10
    #   num = num//10
    answer = sum([int(i) for i in str(num)])
    return answer

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
