#박지민 -20213001
def solution(num) :
  answer = 0
  s = set(num)

  if len(num)==len(s) :
      print("자주나타나는 숫자는없다")
  elif len(num)==1 :
      print("없다")
  else :
      dic={i:num.count(i) for i in s}

  answer = max(dic, key=dic.get)
