# 박시윤-20212997
def solution(lst):
    test={}
    answer=[]
    compare=1
    for i in lst: #딕셔너리에 숫자와 빈도 수 저장
        if i in test:
            test[i]+=1
        else:
            test[i]=1
    for key,values in test.items(): #가장 높은 빈도를 가진 수만 answer에 저장
        if values>compare:
            answer=[]
            compare=values
            answer.append(key)
        elif values==compare:
            answer.append(key)
    return answer if not len(answer)==len(set(lst)) else [] # lst의 숫자가 모두 같거나 모든 수의 빈도수가 같다면 answer가 lst를 집합화시킨 것과 같다는 것을 이용

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]