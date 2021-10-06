# 박시윤-20212997
import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

'''def iterfibo(n):
    first=0
    second=1
    temp=0
    for i in range(n):
        temp=second
        second=first+second
        first=temp
    return first'''

def iterfibo(n):
    list=[]
    for i in range(n):
        if i<2:
            list.append(1)
        else:
            list.append(list[i-1]+list[i-2])
    return list[n-1]

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" % (nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
