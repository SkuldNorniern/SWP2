# 박시윤-20212997
def solution(num):
    list = [int(i) for i in str(num)]
    answer=sum(list)
    return answer

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
