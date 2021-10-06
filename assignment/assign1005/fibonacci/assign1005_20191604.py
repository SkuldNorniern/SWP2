# 백연선-20191604
import time
import random

def iterfibo(n):
    list = []
    for i in range(0, n):
        if i < 2:
            list.append(1)
        else:
            list.append(list[i-1] + list[i-2])
    return list[n-1]

def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
